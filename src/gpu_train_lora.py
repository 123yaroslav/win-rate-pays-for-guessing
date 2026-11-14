"""Study 5 follow-up: direct LoRA training on the GPU pod. Needs only torch, transformers and peft.

For each arm the script trains one LoRA adapter on `train_<arm>.jsonl` (rows with `prompt` and `completion`)
and saves it in PEFT format, in the layout that `gpu_eval.py` loads. All arms get the same settings, the same
seed, the same initial adapter weights and the same order of questions. The base weights are read from disk
again for every arm.

    python gpu_train_lora.py --arms C J K R --data . --out adapters_followup --log-dir out_followup \
        --eval-items medqa_eval.jsonl --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a

Settings (fixed in `results/study5/deviations.md` before any follow-up training): base `Qwen/Qwen3.5-9B` in
bfloat16, LoRA rank 16, alpha 32, dropout 0 on the q, k, v, o, gate, up and down projections, three epochs,
16 examples per optimiser step, AdamW, peak learning rate 1e-4 with 10% linear warm-up and cosine decay, loss
on the completion tokens only, seed 20261115.

Format of a training example: the prompt of the evaluation (one user turn with the question text, no system
prompt, the model's chat template with thinking switched off), then the completion, then `<|im_end|>`. The
loss covers the completion and the `<|im_end|>` token. Nothing is truncated.

Memory: `--micro-batch N` computes the 16 examples of a step in chunks of N and adds up the gradients. The
loss of a step is the sum over all completion tokens of the 16 examples divided by their number, so the step
is the same as for one batch of 16. Inside a step the examples are sorted by length to cut padding.

    --preflight       measure memory and time of the heaviest step for several chunk sizes, train nothing
    --max-steps 3     smoke test: a few steps, then save
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import random
import time
from pathlib import Path

import torch

BASE = "Qwen/Qwen3.5-9B"
SEED = 20261115
EPOCHS = 3
BATCH = 16
LR = 1e-4
WARMUP_SHARE = 0.10
RANK, ALPHA, DROPOUT = 16, 32, 0.0
TARGETS = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
BETAS, EPS, WEIGHT_DECAY, MAX_GRAD_NORM = (0.9, 0.999), 1e-8, 0.0, 1.0
END_OF_TURN = "<|im_end|>"
IGNORE = -100


# ---------------------------------------------------------------- format
def render(tok, qtext: str) -> str:
    """The prompt of the registered evaluation, the same call as `gpu_eval.render` with its defaults."""
    msgs = [{"role": "user", "content": qtext}]
    kw = {"enable_thinking": False} if "enable_thinking" in (tok.chat_template or "") else {}
    return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, **kw)


def question_text(prompt) -> str:
    """`prompt` is the question text, or a JSON list of chat turns with a single user turn."""
    turns = prompt
    if isinstance(prompt, str):
        try:
            turns = json.loads(prompt) if prompt.lstrip().startswith("[") else prompt
        except json.JSONDecodeError:
            turns = prompt
    if isinstance(turns, str):
        return turns
    if not (isinstance(turns, list) and len(turns) == 1 and turns[0].get("role") == "user"):
        raise SystemExit(f"prompt is not a single user turn: {str(prompt)[:120]!r}")
    return turns[0]["content"]


def encode(tok, rows: list[dict]) -> list[dict]:
    end = tok.convert_tokens_to_ids(END_OF_TURN)
    assert isinstance(end, int) and end >= 0 and end != tok.unk_token_id, "no end-of-turn token"
    out = []
    for r in rows:
        text = render(tok, question_text(r["prompt"]))
        p = tok(text, add_special_tokens=False).input_ids
        c = tok(r["completion"], add_special_tokens=False).input_ids
        out.append({"id": r.get("id"), "ids": p + c + [end], "n_prompt": len(p), "n_target": len(c) + 1,
                    "prompt_text": text})
    return out


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------- model
def load_base(model_id: str, revision: str | None):
    """The same class and options as `gpu_eval.load_base`: the text tower of the checkpoint, bfloat16."""
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(model_id, revision=revision)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_id, revision=revision, dtype=torch.bfloat16,
                                                 device_map="cuda")
    return tok, model


def add_lora(base):
    from peft import LoraConfig, get_peft_model

    cfg = LoraConfig(r=RANK, lora_alpha=ALPHA, lora_dropout=DROPOUT, bias="none", task_type="CAUSAL_LM",
                     target_modules=list(TARGETS))
    torch.manual_seed(SEED)          # the same initial adapter weights for every arm
    return get_peft_model(base, cfg)


def collate(examples: list[dict], pad_id: int, device):
    width = max(len(e["ids"]) for e in examples)
    ids = torch.full((len(examples), width), pad_id, dtype=torch.long)
    mask = torch.zeros_like(ids)
    labels = torch.full_like(ids, IGNORE)
    for i, e in enumerate(examples):
        n = len(e["ids"])
        ids[i, :n] = torch.tensor(e["ids"])
        mask[i, :n] = 1
        labels[i, e["n_prompt"]:n] = torch.tensor(e["ids"][e["n_prompt"]:])
    return ids.to(device), mask.to(device), labels.to(device)


def loss_sum(body, head, ids, mask, labels) -> tuple[torch.Tensor, int]:
    """Sum of the negative log-likelihood over the completion tokens. The output layer is applied only at
    the positions that predict a completion token, the vocabulary is too large to do it everywhere."""
    with torch.autocast("cuda", dtype=torch.bfloat16):
        out = body(input_ids=ids, attention_mask=mask, use_cache=False)
        h = out.last_hidden_state if hasattr(out, "last_hidden_state") else out[0]
        sel = labels[:, 1:] != IGNORE
        logits = head(h[:, :-1][sel])
    loss = torch.nn.functional.cross_entropy(logits.float(), labels[:, 1:][sel], reduction="sum")
    return loss, int(sel.sum())


def chunks(step: list[int], data: list[dict], micro: int) -> list[list[dict]]:
    by_len = sorted(step, key=lambda i: (-len(data[i]["ids"]), i))
    return [[data[i] for i in by_len[s:s + micro]] for s in range(0, len(by_len), micro)]


def step_grad(body, head, step: list[int], data: list[dict], micro: int, pad_id: int, device) -> tuple[float, int]:
    """Gradient of the mean loss over all completion tokens of the step. Returns (mean loss, tokens)."""
    n_tok = sum(data[i]["n_target"] for i in step)
    total = 0.0
    for part in chunks(step, data, micro):
        ids, mask, labels = collate(part, pad_id, device)
        loss, _ = loss_sum(body, head, ids, mask, labels)
        (loss / n_tok).backward()
        total += float(loss.detach())
        del loss, ids, mask, labels
    return total / n_tok, n_tok


def lr_factor(step: int, total: int, warmup: int) -> float:
    """Linear warm-up, then cosine decay to zero (the schedule of get_cosine_schedule_with_warmup)."""
    if step < warmup:
        return step / max(1, warmup)
    return 0.5 * (1.0 + math.cos(math.pi * (step - warmup) / max(1, total - warmup)))


def data_order(n: int) -> list[list[list[int]]]:
    rng = random.Random(SEED)
    epochs = []
    for _ in range(EPOCHS):
        perm = list(range(n))
        rng.shuffle(perm)
        epochs.append([perm[i:i + BATCH] for i in range(0, n, BATCH)])
    return epochs


def versions() -> dict:
    import peft
    import transformers

    return {"torch": torch.__version__, "transformers": transformers.__version__, "peft": peft.__version__,
            "gpu": torch.cuda.get_device_name(0), "cuda": torch.version.cuda}


# ---------------------------------------------------------------- checks
def head_check(base, body, head, data: list[dict], pad_id: int) -> float:
    """The loss through body and output layer against the loss from the model's own logits, two examples."""
    ids, mask, labels = collate(data[:2], pad_id, base.device)
    with torch.no_grad():
        a, n = loss_sum(body, head, ids, mask, labels)
        with torch.autocast("cuda", dtype=torch.bfloat16):
            full = base(input_ids=ids, attention_mask=mask, use_cache=False).logits
        sel = labels[:, 1:] != IGNORE
        b = torch.nn.functional.cross_entropy(full[:, :-1][sel].float(), labels[:, 1:][sel], reduction="sum")
    return abs(float(a) - float(b)) / n


def format_report(tok, rows: list[dict], data: list[dict], eval_items: str | None) -> dict:
    """One fully rendered training example, one rendered evaluation prompt, and what the checks say."""
    e = data[0]
    rep = {
        "training_example_rendered": tok.decode(e["ids"], skip_special_tokens=False),
        "training_example_loss_part": tok.decode(e["ids"][e["n_prompt"]:], skip_special_tokens=False),
        "training_prompt_ends_with": e["prompt_text"][-60:],
    }
    joint = sum(tok(d["prompt_text"] + r["completion"], add_special_tokens=False).input_ids != d["ids"][:-1]
                for d, r in zip(data, rows))
    rep["examples_where_joint_tokenisation_differs"] = joint
    turns = [{"role": "user", "content": question_text(rows[0]["prompt"])},
             {"role": "assistant", "content": rows[0]["completion"]}]
    kw = {"enable_thinking": False} if "enable_thinking" in (tok.chat_template or "") else {}
    try:
        whole = tok.apply_chat_template(turns, tokenize=False, add_generation_prompt=False, **kw)
        mine = e["prompt_text"] + rows[0]["completion"] + END_OF_TURN
        rep["template_render_of_the_two_turns_equal"] = whole.rstrip("\n") == mine
        if whole.rstrip("\n") != mine:
            rep["template_render_of_the_two_turns_tail"] = whole[-(len(rows[0]["completion"]) + 80):]
    except Exception as err:  # noqa: BLE001
        rep["template_render_of_the_two_turns_error"] = f"{type(err).__name__}: {err}"[:200]
    if eval_items:
        item = json.loads(Path(eval_items).read_text().splitlines()[0])
        rep["evaluation_prompt_rendered"] = render(tok, item["qtext"])
        try:
            import gpu_eval

            same = [gpu_eval.render(tok, question_text(r["prompt"])) == d["prompt_text"]
                    for r, d in zip(rows[:200], data[:200])]
            rep["prompts_equal_to_gpu_eval_render"] = f"{sum(same)} of {len(same)}"
            assert all(same), "the training prompt is not the prompt gpu_eval.py builds"
        except ImportError:
            rep["prompts_equal_to_gpu_eval_render"] = "gpu_eval.py not importable, not checked"
        head_q, tail_q = e["prompt_text"].split(question_text(rows[0]["prompt"]))
        head_e, tail_e = rep["evaluation_prompt_rendered"].split(item["qtext"])
        rep["same_wrapping_as_evaluation_prompt"] = (head_q, tail_q) == (head_e, tail_e)
        assert rep["same_wrapping_as_evaluation_prompt"], "training and evaluation prompts are wrapped differently"
    return rep


def preflight(base, body, head, tok, all_data: dict[str, list[dict]], sizes: list[int]) -> None:
    """Memory and time of the heaviest step of any arm, for each chunk size. Trains nothing."""
    model = add_lora(base)
    model.train()
    names = [n for n, p in model.named_parameters() if p.requires_grad]
    print(f"trainable tensors {len(names)}, parameters "
          f"{sum(p.numel() for p in model.parameters() if p.requires_grad):,}", flush=True)
    n = len(next(iter(all_data.values())))
    steps = [s for ep in data_order(n) for s in ep]
    for micro in sizes:
        heavy = max(((arm, s) for arm in all_data for s in steps), key=lambda x: max(
            len(c) * len(c[0]["ids"]) for c in chunks(x[1], all_data[x[0]], micro)))
        arm, step = heavy
        padded = max(len(c) * len(c[0]["ids"]) for c in chunks(step, all_data[arm], micro))
        try:
            torch.cuda.empty_cache()
            torch.cuda.reset_peak_memory_stats()
            t0 = time.time()
            loss, n_tok = step_grad(body, head, step, all_data[arm], micro, tok.pad_token_id, base.device)
            torch.cuda.synchronize()
            heavy_s = time.time() - t0
            peak = torch.cuda.max_memory_allocated() / 2**30
            model.zero_grad(set_to_none=True)
            first = next(iter(all_data))
            t0 = time.time()
            for s in steps[:3]:
                step_grad(body, head, s, all_data[first], micro, tok.pad_token_id, base.device)
                model.zero_grad(set_to_none=True)
            torch.cuda.synchronize()
            typical = (time.time() - t0) / 3
            print(f"chunk {micro:>2}: heaviest step (arm {arm}, largest chunk {padded} padded tokens) "
                  f"peak {peak:.1f} GB, {heavy_s:.1f} s, loss {loss:.3f}; first three steps {typical:.2f} s each, "
                  f"peak so far {torch.cuda.max_memory_allocated() / 2**30:.1f} GB", flush=True)
        except torch.OutOfMemoryError:
            model.zero_grad(set_to_none=True)
            gc.collect()
            torch.cuda.empty_cache()
            print(f"chunk {micro:>2}: out of memory on the heaviest step (arm {arm}, {padded} padded tokens)",
                  flush=True)


# ---------------------------------------------------------------- training of one arm
def train_arm(arm: str, a, common: dict) -> dict:
    data_file = Path(a.data) / f"train_{arm}.jsonl"
    rows = [json.loads(ln) for ln in data_file.read_text().splitlines() if ln.strip()]
    tok, base = load_base(a.base, a.revision)        # fresh weights from disk for every arm
    body, head = base.model, base.get_output_embeddings()
    data = encode(tok, rows)
    longest = max(data, key=lambda d: len(d["ids"]))
    assert len(longest["ids"]) <= a.max_length, f"{arm}: an example has {len(longest['ids'])} tokens"
    report = format_report(tok, rows, data, a.eval_items)
    print(f"\n===== arm {arm}: {len(rows)} rows from {data_file}, model class {type(base).__name__}")
    print(f"longest example {len(longest['ids'])} tokens ({longest['id']}), limit {a.max_length}, none truncated")
    print("--- one training example, fully rendered ---\n" + report["training_example_rendered"])
    print("--- the part the loss covers ---\n" + report["training_example_loss_part"])
    if "evaluation_prompt_rendered" in report:
        print("--- one evaluation prompt, rendered ---\n" + report["evaluation_prompt_rendered"] + "[generation starts here]")
    print("--- format checks ---\n" + json.dumps({k: v for k, v in report.items() if "rendered" not in k and
                                                      k != "training_example_loss_part"}, ensure_ascii=False))
    gap = head_check(base, body, head, data, tok.pad_token_id)
    print(f"loss through the output layer at completion positions against the model's own logits: "
          f"{gap:.2e} per token apart", flush=True)
    assert gap < 1e-3, "the short path to the loss does not match the model's logits"

    model = add_lora(base)
    model.train()
    params = [p for p in model.parameters() if p.requires_grad]
    names = [n for n, p in model.named_parameters() if p.requires_grad]
    assert names and all("lora_" in n for n in names), "only LoRA tensors may be trainable"
    opt = torch.optim.AdamW(params, lr=LR, betas=BETAS, eps=EPS, weight_decay=WEIGHT_DECAY)
    epochs = data_order(len(data))
    steps = [(e, s) for e, ep in enumerate(epochs) for s in ep]
    total, warmup = len(steps), math.ceil(WARMUP_SHARE * len(steps))
    print(f"trainable tensors {len(names)} ({sum(p.numel() for p in params):,} parameters, {params[0].dtype}), "
          f"{total} steps, {warmup} warm-up steps, chunk size {a.micro_batch}", flush=True)

    log, t0 = [], time.time()
    torch.cuda.reset_peak_memory_stats()
    for k, (epoch, step) in enumerate(steps[:a.max_steps] if a.max_steps else steps):
        lr = LR * lr_factor(k, total, warmup)
        for g in opt.param_groups:
            g["lr"] = lr
        loss, n_tok = step_grad(body, head, step, data, a.micro_batch, tok.pad_token_id, base.device)
        if not math.isfinite(loss):
            raise SystemExit(f"arm {arm}: loss is {loss} at step {k + 1}, nothing saved")
        norm = float(torch.nn.utils.clip_grad_norm_(params, MAX_GRAD_NORM))
        opt.step()
        opt.zero_grad(set_to_none=True)
        log.append({"step": k + 1, "epoch": epoch + 1, "lr": lr, "loss": loss, "completion_tokens": n_tok,
                    "examples": len(step), "grad_norm": norm, "seconds": round(time.time() - t0, 1)})
        if (k + 1) % 10 == 0 or k == 0 or k + 1 == total:
            print(f"[{arm}] step {k + 1}/{total} epoch {epoch + 1} lr {lr:.2e} loss {loss:.4f} "
                  f"grad {norm:.2f} {time.time() - t0:.0f} s", flush=True)

    out_dir = Path(a.out) / f"{arm}{a.suffix}"
    out_dir.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(str(out_dir))
    from safetensors.torch import load_file

    saved = load_file(str(out_dir / "adapter_model.safetensors"))
    assert all(torch.isfinite(v).all() for v in saved.values()), "saved adapter has non-finite values"
    moved = sum(bool(v.abs().sum() > 0) for k, v in saved.items() if "lora_B" in k)
    by_epoch = {str(e + 1): [r["loss"] for r in log if r["epoch"] == e + 1] for e in range(EPOCHS)}
    summary = {
        "arm": arm, "adapter_name": f"{arm}{a.suffix}", "adapter_dir": str(out_dir),
        "adapter_sha256": sha256(out_dir / "adapter_model.safetensors"),
        "adapter_tensors": len(saved), "lora_B_tensors_changed": moved,
        "data_file": str(data_file), "data_sha256": sha256(data_file), "rows": len(rows),
        "question_order_sha256": hashlib.sha256("\n".join(str(d["id"]) for d in data).encode()).hexdigest(),
        "settings": {
            **common, "rank": RANK, "alpha": ALPHA, "dropout": DROPOUT, "target_modules": TARGETS,
            "epochs": EPOCHS, "examples_per_step": BATCH, "chunk_size_within_step": a.micro_batch,
            "optimizer": "AdamW", "betas": list(BETAS), "eps": EPS, "weight_decay": WEIGHT_DECAY,
            "peak_lr": LR, "warmup_steps": warmup, "total_steps": total, "schedule": "linear warm-up, cosine decay",
            "max_grad_norm": MAX_GRAD_NORM, "seed": SEED, "loss": "mean over the completion tokens and the "
            "end-of-turn token of the 16 examples", "base_dtype": "bfloat16", "adapter_dtype": str(params[0].dtype),
            "autocast": "bfloat16", "max_length": a.max_length, "truncated_examples": 0,
        },
        "longest_example_tokens": len(longest["ids"]), "longest_example_id": longest["id"],
        "mean_example_tokens": round(sum(len(d["ids"]) for d in data) / len(data), 1),
        "completion_tokens_per_epoch": sum(d["n_target"] for d in data),
        "steps_done": len(log), "seconds": round(time.time() - t0, 1),
        "peak_gpu_memory_gb": round(torch.cuda.max_memory_allocated() / 2**30, 1),
        "first_step_loss": log[0]["loss"], "final_step_loss": log[-1]["loss"],
        "mean_loss_last_10_steps": sum(r["loss"] for r in log[-10:]) / len(log[-10:]),
        "mean_loss_by_epoch": {e: sum(v) / len(v) for e, v in by_epoch.items() if v},
        "head_check_gap_per_token": gap, "format": report, "versions": versions(), "steps": log,
    }
    Path(a.log_dir).mkdir(parents=True, exist_ok=True)
    (Path(a.log_dir) / f"followup_train_log_{arm}.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    print(f"[{arm}] saved {len(saved)} tensors to {out_dir}, {moved} lora_B tensors changed, final step loss "
          f"{log[-1]['loss']:.4f}, mean of the last 10 steps {summary['mean_loss_last_10_steps']:.4f}, "
          f"{summary['seconds']:.0f} s, peak memory {summary['peak_gpu_memory_gb']} GB", flush=True)

    del model, opt, params, body, head, base
    gc.collect()
    torch.cuda.empty_cache()
    return summary


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", nargs="+", default=["C", "J", "K", "R"])
    ap.add_argument("--data", default=".", help="folder with train_<arm>.jsonl")
    ap.add_argument("--out", default="adapters_followup", help="one folder per adapter is written here")
    ap.add_argument("--suffix", default="3", help="the adapter of arm C is named C3")
    ap.add_argument("--log-dir", default="out_followup")
    ap.add_argument("--eval-items", default=None, help="the evaluation file, to print one evaluation prompt")
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--revision", default=None)
    ap.add_argument("--micro-batch", type=int, default=BATCH, help="examples per forward pass inside a step")
    ap.add_argument("--max-length", type=int, default=4096, help="a check only, nothing is ever truncated")
    ap.add_argument("--max-steps", type=int, default=0, help="smoke test: stop after N steps")
    ap.add_argument("--preflight", nargs="*", type=int, default=None, metavar="CHUNK",
                    help="measure the heaviest step for these chunk sizes and exit")
    a = ap.parse_args()
    assert BATCH % a.micro_batch == 0 or a.micro_batch >= BATCH, "the chunk size must divide 16"

    if a.preflight is not None:
        tok, base = load_base(a.base, a.revision)
        all_data = {arm: encode(tok, [json.loads(ln) for ln in (Path(a.data) / f"train_{arm}.jsonl")
                                      .read_text().splitlines() if ln.strip()]) for arm in a.arms}
        for arm, d in all_data.items():
            print(f"arm {arm}: {len(d)} rows, longest example {max(len(x['ids']) for x in d)} tokens, mean "
                  f"{sum(len(x['ids']) for x in d) / len(d):.0f}, completion tokens {sum(x['n_target'] for x in d)}")
        print("model class", type(base).__name__, "| body", type(base.model).__name__, "| output layer",
              type(base.get_output_embeddings()).__name__)
        print("head check", head_check(base, base.model, base.get_output_embeddings(), all_data[a.arms[0]],
                                       tok.pad_token_id))
        preflight(base, base.model, base.get_output_embeddings(), tok, all_data, a.preflight or [16, 8, 4])
        return

    common = {"base_model": a.base, "revision": a.revision}
    done = [train_arm(arm, a, common) for arm in a.arms]
    orders = {s["question_order_sha256"] for s in done}
    print(f"\nquestion order identical across the arms of this call: {len(orders) == 1}")
    print(f"{'arm':<5}{'steps':>6}{'first loss':>12}{'final loss':>12}{'last 10':>10}{'seconds':>9}{'longest':>9}")
    for s in done:
        print(f"{s['arm']:<5}{s['steps_done']:>6}{s['first_step_loss']:>12.4f}{s['final_step_loss']:>12.4f}"
              f"{s['mean_loss_last_10_steps']:>10.4f}{s['seconds']:>9.0f}{s['longest_example_tokens']:>9}")


if __name__ == "__main__":
    main()
