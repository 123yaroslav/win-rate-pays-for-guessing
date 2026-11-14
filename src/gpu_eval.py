"""Study 5, evaluation by the key. Runs on a GPU pod, needs only torch, transformers and peft.

For the base model and for each LoRA adapter the script writes one greedy response per question: no system
prompt, the user turn is exactly the item's `qtext`, the model's chat template with thinking switched off,
at most 300 new tokens. The final line is parsed and scored against the key.

    python gpu_eval.py --items medqa_eval.jsonl --out out
    python gpu_eval.py --items medqa_eval.jsonl --out out --adapters J=adapters/J F=adapters/F K=adapters/K R=adapters/R

Per model it writes `out/eval_<name>.jsonl` and `out/eval_<name>_summary.json`. A model whose output file is
complete is skipped unless `--force` is given. All rates are shares of all questions, so abstention, accuracy,
wrong and unparsed add up to 1. The penalised score is the mean of +1 for right, -1 for wrong or unparsed and
0 for an abstention.

    python gpu_eval.py --make-test-adapter /workspace/test_adapter

writes a throwaway rank 8 adapter on q_proj and v_proj with random weights, to test the adapter path.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from pathlib import Path

import torch

BASE = "Qwen/Qwen3.5-9B"
_FINAL = re.compile(r"^final answer\s*:\s*(.*)$", re.I)
_LETTER = re.compile(r"^\(?([A-D])\)?(?:[.):,\s].*)?$")
_IDK = re.compile(r"^i\s+(?:don['’]?t|do\s+not)\s+know\b", re.I)
_SCORE = {"correct": 1, "wrong": -1, "unparsed": -1, "abstain": 0}


# ---------------------------------------------------------------- parsing and scoring
def _value(line: str) -> str | None:
    m = _FINAL.match(line.strip("*_`# ").strip())
    return m.group(1).strip("*_` ").strip() if m else None


def _read(value: str | None) -> str:
    if value is None:
        return "UNPARSED"
    if _IDK.match(value):
        return "ABSTAIN"
    m = _LETTER.match(value)
    return m.group(1) if m else "UNPARSED"


def parse_final(text: str) -> tuple[str, str]:
    """Returns (parsed, parsed_lastline): a letter A to D, "ABSTAIN" or "UNPARSED".

    `parsed` reads the last line that starts with "Final answer:". `parsed_lastline` asks that this line is
    also the last non-empty line of the response, the rule of `loop_common.parse_final`.
    """
    lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
    values = [v for v in map(_value, lines) if v is not None]
    return _read(values[-1] if values else None), _read(_value(lines[-1]) if lines else None)


def outcome(parsed: str, key: str) -> str:
    if parsed == "ABSTAIN":
        return "abstain"
    if parsed == "UNPARSED":
        return "unparsed"
    return "correct" if parsed == key else "wrong"


def summarise(rows: list[dict]) -> dict:
    n = len(rows)
    c = {k: sum(r["outcome"] == k for r in rows) for k in _SCORE}
    return {
        "n": n,
        "counts": c,
        "abstention_rate": c["abstain"] / n,
        "accuracy": c["correct"] / n,
        "wrong_rate": c["wrong"] / n,
        "unparsed_rate": c["unparsed"] / n,
        "penalised_score": sum(_SCORE[r["outcome"]] for r in rows) / n,
        "hit_token_limit": sum(r["finish"] == "length" for r in rows),
        "lastline_rule_differs": sum(r["parsed"] != r["parsed_lastline"] for r in rows),
    }


# ---------------------------------------------------------------- model
def load_base(model_id: str, revision: str | None):
    from transformers import AutoModelForCausalLM, AutoModelForImageTextToText, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(model_id, revision=revision)
    tok.padding_side = "left"
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    kw = dict(revision=revision, dtype=torch.bfloat16, device_map="cuda")
    try:
        model = AutoModelForCausalLM.from_pretrained(model_id, **kw)       # text tower only
    except Exception as e:  # noqa: BLE001
        print(f"AutoModelForCausalLM failed ({type(e).__name__}: {e}); loading the full multimodal class")
        model = AutoModelForImageTextToText.from_pretrained(model_id, **kw)
    model.eval()
    return tok, model


def render(tok, qtext: str) -> str:
    """One user turn, no system prompt, thinking off if the template has the switch."""
    kw = {"enable_thinking": False} if "enable_thinking" in (tok.chat_template or "") else {}
    return tok.apply_chat_template([{"role": "user", "content": qtext}], tokenize=False,
                                   add_generation_prompt=True, **kw)


def stop_ids(tok) -> list[int]:
    ids = {tok.eos_token_id, tok.pad_token_id, tok.convert_tokens_to_ids("<|im_end|>"),
           tok.convert_tokens_to_ids("<|endoftext|>")}
    return sorted(i for i in ids if isinstance(i, int) and i >= 0 and i != tok.unk_token_id)


@torch.inference_mode()
def fingerprint(model, tok, prompt: str) -> torch.Tensor:
    """Next-token logits for one prompt: shows that an adapter acts and that the base is restored after it."""
    enc = tok(prompt, return_tensors="pt", add_special_tokens=False).to(model.device)
    return model(**enc).logits[0, -1].float().cpu()


@torch.inference_mode()
def generate(model, tok, prompts: list[str], batch_size: int, max_new_tokens: int) -> list[dict]:
    """Greedy decoding. Batches are fixed by prompt length, so a rerun sees the same batches."""
    from transformers import GenerationConfig

    stops = stop_ids(tok)
    cfg = GenerationConfig(do_sample=False, num_beams=1, repetition_penalty=1.0, max_new_tokens=max_new_tokens,
                           eos_token_id=stops, pad_token_id=tok.pad_token_id)
    lengths = [len(tok(p, add_special_tokens=False).input_ids) for p in prompts]
    order = sorted(range(len(prompts)), key=lambda i: (-lengths[i], i))
    out: list[dict | None] = [None] * len(prompts)
    t0 = time.time()
    for start in range(0, len(order), batch_size):
        idx = order[start:start + batch_size]
        enc = tok([prompts[i] for i in idx], return_tensors="pt", padding=True,
                  add_special_tokens=False).to(model.device)
        new = model.generate(**enc, generation_config=cfg)[:, enc.input_ids.shape[1]:].tolist()
        for i, ids in zip(idx, new):
            cut = next((j for j, t in enumerate(ids) if t in stops), None)
            kept = ids if cut is None else ids[:cut]
            out[i] = {"text": tok.decode(kept, skip_special_tokens=True), "n_tokens": len(kept),
                      "prompt_tokens": lengths[i], "finish": "length" if cut is None else "stop"}
        done = min(start + batch_size, len(order))
        print(f"  {done}/{len(order)} responses, {time.time() - t0:.0f} s", flush=True)
    return out  # type: ignore[return-value]


# ---------------------------------------------------------------- adapters
def _tail(key: str, name: str | None = None) -> str:
    """Module path from "layers." on, without the adapter name, so keys saved from any wrapper class match."""
    if name is not None:
        key = re.sub(rf"\.(lora_\w+)\.{re.escape(name)}(?=\.|$)", r".\1", key)
    return key[key.index("layers."):] if "layers." in key else key


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def attach(base, tok, name: str, adapter_dir: Path) -> tuple[object, dict]:
    """Loads a PEFT LoRA adapter and proves that every saved tensor sits in the model. Stops if not."""
    from peft import PeftModel
    from peft.utils import set_peft_model_state_dict
    from safetensors.torch import load_file

    weights = adapter_dir / "adapter_model.safetensors"
    saved = load_file(str(weights))
    model = PeftModel.from_pretrained(base, str(adapter_dir), adapter_name=name)
    model.eval()

    def slots() -> dict[str, tuple[str, torch.Tensor]]:
        return {_tail(k, name): (k, v) for k, v in model.state_dict().items()
                if re.search(rf"\.lora_\w+\.{re.escape(name)}(\.|$)", k)}

    def unplaced() -> list[str]:
        s = slots()
        return [k for k, v in saved.items() if _tail(k) not in s or s[_tail(k)][1].shape != v.shape
                or not torch.equal(s[_tail(k)][1].cpu(), v.to(s[_tail(k)][1].dtype))]

    remapped = False
    if unplaced():      # saved from another wrapper class: place the tensors by their module path
        s = slots()
        gone = [k for k in saved if _tail(k) not in s]
        if gone:
            raise SystemExit(f"adapter {name}: {len(gone)} tensors have no module in the base model, "
                             f"for example {gone[0]}")
        fixed = {re.sub(rf"\.(lora_\w+)\.{re.escape(name)}(?=\.|$)", r".\1", s[_tail(k)][0]): v
                 for k, v in saved.items()}
        set_peft_model_state_dict(model, fixed, adapter_name=name)
        remapped = True
    bad, n_slots = unplaced(), len(slots())
    if bad or n_slots != len(saved):
        raise SystemExit(f"adapter {name}: {len(bad)} of {len(saved)} saved tensors are not in the model, and "
                         f"the model has {n_slots} adapter tensors. First problem: {(bad or ['count'])[0]}")

    cfg = json.loads((adapter_dir / "adapter_config.json").read_text())
    own_template = adapter_dir / "chat_template.jinja"
    info = {
        "dir": str(adapter_dir),
        "sha256": sha256(weights),
        "tensors_in_file": len(saved),
        "tensors_placed": n_slots,
        "placed_by_module_path": remapped,
        "r": cfg.get("r"),
        "lora_alpha": cfg.get("lora_alpha"),
        "target_modules": cfg.get("target_modules"),
        "trained_on": cfg.get("base_model_name_or_path"),
        "ships_other_chat_template": own_template.exists() and own_template.read_text() != tok.chat_template,
    }
    return model, info


def make_test_adapter(base, out_dir: Path) -> None:
    from peft import LoraConfig, get_peft_model

    cfg = LoraConfig(r=8, lora_alpha=16, lora_dropout=0.0, bias="none", task_type="CAUSAL_LM",
                     target_modules=["q_proj", "v_proj"])
    model = get_peft_model(base, cfg)
    torch.manual_seed(0)
    for n, p in model.named_parameters():
        if "lora_B" in n:           # B starts at zero, which would leave the model unchanged
            torch.nn.init.normal_(p, std=0.02)
    model.save_pretrained(str(out_dir))
    model.unload()
    print("test adapter ->", out_dir, sorted(f.name for f in out_dir.iterdir()))


# ---------------------------------------------------------------- run
def versions() -> dict:
    import peft
    import transformers

    return {"torch": torch.__version__, "transformers": transformers.__version__, "peft": peft.__version__,
            "gpu": torch.cuda.get_device_name(0), "cuda": torch.version.cuda}


def complete(out: Path, name: str, ids: list[str], adapter_sha: str | None) -> bool:
    rows, summary = out / f"eval_{name}.jsonl", out / f"eval_{name}_summary.json"
    if not (rows.exists() and summary.exists()):
        return False
    have = [json.loads(ln)["id"] for ln in rows.read_text().splitlines() if ln.strip()]
    return have == ids and (json.loads(summary.read_text()).get("adapter") or {}).get("sha256") == adapter_sha


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", help="JSONL with id, qtext and answer")
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--revision", default=None, help="commit of the base model on the Hub")
    ap.add_argument("--adapters", nargs="*", default=[], metavar="NAME=DIR")
    ap.add_argument("--out", default="out")
    ap.add_argument("--skip-base", action="store_true")
    ap.add_argument("--force", action="store_true", help="rerun models whose output is already complete")
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--max-new-tokens", type=int, default=300)
    ap.add_argument("--limit", type=int, default=0, help="first N items only, for a smoke test")
    ap.add_argument("--make-test-adapter", metavar="DIR", help="write a random adapter to DIR and exit")
    a = ap.parse_args()

    adapters: list[tuple[str, Path]] = []
    for spec in a.adapters:
        name, _, d = spec.partition("=")
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", name) or name == "base" or not (Path(d) / "adapter_config.json").exists():
            raise SystemExit(f"bad adapter {spec!r}: expected NAME=DIR, DIR holding adapter_config.json")
        adapters.append((name, Path(d)))

    tok, model = load_base(a.base, a.revision)
    if a.make_test_adapter:
        make_test_adapter(model, Path(a.make_test_adapter))
        return
    if not a.items:
        raise SystemExit("--items is required")

    items = [json.loads(ln) for ln in Path(a.items).read_text().splitlines() if ln.strip()]
    items = items[:a.limit] if a.limit else items
    ids = [it["id"] for it in items]
    prompts = [render(tok, it["qtext"]) for it in items]
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    common = {
        "base_model": a.base,
        "revision": getattr(model.config, "_commit_hash", None) or a.revision,
        "model_class": type(model).__name__,
        "items": a.items,
        "generation": {"do_sample": False, "temperature": 0, "max_new_tokens": a.max_new_tokens,
                       "batch_size": a.batch_size, "dtype": "bfloat16", "system_prompt": None,
                       "thinking_switch_in_template": "enable_thinking" in (tok.chat_template or ""),
                       "enable_thinking": False},
        "prompt_example": prompts[0],
        "versions": versions(),
    }
    base_print = fingerprint(model, tok, prompts[0])
    summaries: dict[str, dict] = {}

    def run(name: str, m, adapter: dict | None) -> None:
        t0 = time.time()
        print(f"[{name}] generating {len(prompts)} responses", flush=True)
        rows = []
        for it, g in zip(items, generate(m, tok, prompts, a.batch_size, a.max_new_tokens)):
            parsed, lastline = parse_final(g["text"])
            o = outcome(parsed, it["answer"])
            rows.append({"id": it["id"], "model": name, "answer": it["answer"], "text": g["text"],
                         "parsed": parsed, "parsed_lastline": lastline, "outcome": o, "correct": o == "correct",
                         "n_tokens": g["n_tokens"], "prompt_tokens": g["prompt_tokens"], "finish": g["finish"]})
        (out / f"eval_{name}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        s = {"model": name, **summarise(rows), "adapter": adapter, "seconds": round(time.time() - t0, 1), **common}
        base_rows = out / "eval_base.jsonl"
        if adapter and base_rows.exists():
            base_text = {d["id"]: d["text"] for d in map(json.loads, base_rows.read_text().splitlines())}
            s["responses_differing_from_base"] = sum(base_text.get(r["id"]) != r["text"] for r in rows)
        (out / f"eval_{name}_summary.json").write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n")
        summaries[name] = s

    if not a.skip_base:
        if complete(out, "base", ids, None) and not a.force:
            print("[base] output is complete, skipped")
            summaries["base"] = json.loads((out / "eval_base_summary.json").read_text())
        else:
            run("base", model, None)

    for name, d in adapters:
        if complete(out, name, ids, sha256(d / "adapter_model.safetensors")) and not a.force:
            print(f"[{name}] output is complete, skipped")
            summaries[name] = json.loads((out / f"eval_{name}_summary.json").read_text())
            continue
        peft_model, info = attach(model, tok, name, d)
        info["logit_shift_first_prompt"] = float((fingerprint(peft_model, tok, prompts[0]) - base_print).abs().max())
        if info["logit_shift_first_prompt"] == 0:
            print(f"WARNING [{name}] the adapter does not change the logits of the first prompt")
        if info["ships_other_chat_template"]:
            print(f"WARNING [{name}] the adapter folder has its own chat template; the base template is used")
        run(name, peft_model, info)
        model = peft_model.unload()
        del peft_model
        torch.cuda.empty_cache()
        drift = float((fingerprint(model, tok, prompts[0]) - base_print).abs().max())
        if drift > 1e-3:
            raise SystemExit(f"base model not restored after adapter {name}: logit drift {drift}")

    print(f"\n{'model':<10}{'n':>5}{'abstain':>9}{'accuracy':>10}{'wrong':>8}{'unparsed':>10}{'penalised':>11}")
    for name, s in summaries.items():
        print(f"{name:<10}{s['n']:>5}{s['abstention_rate']:>9.3f}{s['accuracy']:>10.3f}{s['wrong_rate']:>8.3f}"
              f"{s['unparsed_rate']:>10.3f}{s['penalised_score']:>11.3f}")


if __name__ == "__main__":
    main()
