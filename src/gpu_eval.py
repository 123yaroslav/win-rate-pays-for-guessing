"""Study 5, evaluation by the key. Runs on a GPU pod, needs only torch, transformers and peft.

For the base model and for each LoRA adapter the script writes one greedy response per question: no system
prompt, the user turn is exactly the item's `qtext`, the model's chat template with thinking switched off,
at most 300 new tokens. The final line is parsed and scored against the key.

    python gpu_eval.py --items medqa_eval.jsonl --out out
    python gpu_eval.py --items medqa_eval.jsonl --out out --adapters J=adapters/J F=adapters/F K=adapters/K R=adapters/R

Per model it writes `out/eval_<name>.jsonl` and `out/eval_<name>_summary.json`, and `out/eval_summary.json`
for all models of the call. A model whose output file is complete is skipped unless `--force` is given. All
rates are shares of all questions, so abstention, accuracy, wrong and unparsed add up to 1. The penalised
score is the mean of +1 for right, -1 for wrong or unparsed and 0 for an abstention.

Reference runs, outside the registered evaluation:

    --system-file assert=assert.txt     the base model with the text of the file as system prompt,
                                        written to eval_base_assert.jsonl
    --probe train_R.jsonl               mean loss of training completions under several prompt formats, for
                                        the base and every adapter, written to format_probe.json. The format
                                        the adapter was trained in has the lowest loss
    --assistant-start think_open        another start of the assistant turn, written to eval_<name>__think_open

If an adapter folder ships tokenizer files or a chat template that turn any question into other tokens than
the base tokenizer does, the adapter is also run with the shipped files, written to eval_<name>_shipped.

    python gpu_eval.py --make-test-adapter /workspace/test_adapter

writes a throwaway rank 8 adapter on q_proj and v_proj with random weights, to test the adapter path.
"""
from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import re
import time
from pathlib import Path

import torch

BASE = "Qwen/Qwen3.5-9B"
STARTS = ("think_off", "think_open", "plain")
_FINAL = re.compile(r"^final answer\s*:\s*(.*)$", re.I)
_LETTER = re.compile(r"^\(?([A-D])\)?(?:[.):,\s].*)?$")
_IDK = re.compile(r"^i\s+(?:don['’]?t|do\s+not)\s+know\b", re.I)
_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_-]*")
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


def render(tok, qtext: str, system: str | None = None, start: str = "think_off") -> str:
    """One user turn, an optional system prompt, and the start of the assistant turn.

    think_off: thinking switched off, the registered setting (the prompt ends with an empty think block).
    think_open: the template default (the prompt ends with an open think tag). plain: no think tag at all.
    """
    msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": qtext}]
    if start == "think_off":
        kw = {"enable_thinking": False} if "enable_thinking" in (tok.chat_template or "") else {}
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, **kw)
    text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    return text if start == "think_open" else text.removesuffix("<think>\n")


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


# ---------------------------------------------------------------- which format was the adapter trained in
PROBE_FORMATS = {
    "chat_think_off": lambda tok, q: render(tok, q),
    "chat_think_open": lambda tok, q: render(tok, q, start="think_open"),
    "chat_plain": lambda tok, q: render(tok, q, start="plain"),
    "chat_json_as_user_text": lambda tok, q: render(tok, json.dumps([{"role": "user", "content": q}])),
    "raw_text": lambda tok, q: q,
    "raw_json": lambda tok, q: json.dumps([{"role": "user", "content": q}]),
}


@torch.inference_mode()
def probe(model, tok, rows: list[dict], batch_size: int = 8) -> dict[str, float]:
    """Mean negative log-likelihood per completion token, with the prompt put in each candidate format."""
    out = {}
    for name, fmt in PROBE_FORMATS.items():
        seqs = [(tok(fmt(tok, r["prompt"]), add_special_tokens=False).input_ids,
                 tok(r["completion"], add_special_tokens=False).input_ids) for r in rows]
        total, count = 0.0, 0
        for s in range(0, len(seqs), batch_size):
            chunk = seqs[s:s + batch_size]
            width = max(len(p) + len(c) for p, c in chunk)
            ids = torch.full((len(chunk), width), tok.pad_token_id, dtype=torch.long)
            mask = torch.zeros_like(ids)
            target = torch.zeros_like(ids, dtype=torch.bool)
            for i, (p, c) in enumerate(chunk):
                ids[i, width - len(p) - len(c):] = torch.tensor(p + c)
                mask[i, width - len(p) - len(c):] = 1
                target[i, width - len(c):] = True
            ids, mask = ids.to(model.device), mask.to(model.device)
            sel = target[:, 1:].to(model.device)
            logp = torch.log_softmax(model(input_ids=ids, attention_mask=mask).logits[:, :-1][sel].float(), -1)
            total += float(-logp.gather(-1, ids[:, 1:][sel].unsqueeze(-1)).sum())
            count += int(sel.sum())
        out[name] = round(total / count, 4)
    return out


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


def attach(base, name: str, adapter_dir: Path) -> tuple[object, dict]:
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
    info = {
        "dir": str(adapter_dir),
        "sha256": sha256(weights),
        "tensors_in_file": len(saved),
        "tensors_placed": n_slots,
        "placed_by_module_path": remapped,
        "r": cfg.get("r"),
        "lora_alpha": cfg.get("lora_alpha"),
        "target_modules": sorted(cfg.get("target_modules") or []),
        "trained_on": cfg.get("base_model_name_or_path"),
    }
    return model, info


def shipped_files(adapter_dir: Path, tok, items: list[dict], prompts: list[str], start: str):
    """Compares the tokenizer files and the chat template in the adapter folder with the base ones.

    Returns the findings, and the shipped tokenizer with its prompts if any question becomes other tokens.
    """
    from transformers import AutoTokenizer

    info: dict = {"ships_chat_template": (adapter_dir / "chat_template.jinja").exists(),
                  "ships_tokenizer": (adapter_dir / "tokenizer.json").exists()}
    if not (info["ships_chat_template"] or info["ships_tokenizer"]):
        return info, None, None
    try:
        own = AutoTokenizer.from_pretrained(str(adapter_dir))
    except Exception as e:  # noqa: BLE001
        info["tokenizer_load_error"] = f"{type(e).__name__}: {e}"[:300]
        own = copy.deepcopy(tok)        # the base tokenizer with the shipped template
        if info["ships_chat_template"]:
            own.chat_template = (adapter_dir / "chat_template.jinja").read_text()
    own.padding_side = "left"
    if own.pad_token_id is None:
        own.pad_token = own.eos_token
    info["chat_template_same_text"] = own.chat_template == tok.chat_template
    info["chat_template_diff"] = list(difflib.unified_diff(
        (tok.chat_template or "").splitlines(), (own.chat_template or "").splitlines(),
        "base", "adapter", lineterm="", n=1))[:80]
    own_prompts = [render(own, it["qtext"], start=start) for it in items]
    ids = lambda t, ps: [t(p, add_special_tokens=False).input_ids for p in ps]  # noqa: E731
    info["prompts_same_text"] = sum(a == b for a, b in zip(prompts, own_prompts))
    info["prompts_same_token_ids"] = sum(a == b for a, b in zip(ids(tok, prompts), ids(own, own_prompts)))
    info["prompts"] = len(prompts)
    if info["prompts_same_token_ids"] == len(prompts):
        return info, None, None
    return info, own, own_prompts


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


def pairs(specs: list[str], what: str, must_hold: str | None = None) -> list[tuple[str, Path]]:
    out = []
    for spec in specs:
        name, _, p = spec.partition("=")
        ok = _NAME.fullmatch(name) and name != "base" and Path(p).exists()
        if not ok or (must_hold and not (Path(p) / must_hold).exists()):
            raise SystemExit(f"bad {what} {spec!r}: expected NAME=PATH" + (f", PATH holding {must_hold}" if must_hold else ""))
        out.append((name, Path(p)))
    return out


def complete(out: Path, name: str, ids: list[str], adapter_sha: str | None, system: str | None) -> bool:
    rows, summary = out / f"eval_{name}.jsonl", out / f"eval_{name}_summary.json"
    if not (rows.exists() and summary.exists()):
        return False
    have = [json.loads(ln)["id"] for ln in rows.read_text().splitlines() if ln.strip()]
    s = json.loads(summary.read_text())
    return have == ids and (s.get("adapter") or {}).get("sha256") == adapter_sha and s.get("system_prompt") == system


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", help="JSONL with id, qtext and answer")
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--revision", default=None, help="commit of the base model on the Hub")
    ap.add_argument("--adapters", nargs="*", default=[], metavar="NAME=DIR")
    ap.add_argument("--system-file", nargs="*", default=[], metavar="NAME=FILE",
                    help="reference run: the base model with the text of FILE as system prompt, output base_NAME")
    ap.add_argument("--assistant-start", choices=STARTS, default="think_off",
                    help="think_off is the registered setting; the others write to eval_<name>__<start>")
    ap.add_argument("--probe", metavar="JSONL", help="rows with prompt and completion, for the format probe")
    ap.add_argument("--probe-n", type=int, default=64)
    ap.add_argument("--out", default="out")
    ap.add_argument("--skip-base", action="store_true")
    ap.add_argument("--force", action="store_true", help="rerun models whose output is already complete")
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--max-new-tokens", type=int, default=300)
    ap.add_argument("--limit", type=int, default=0, help="first N items only, for a smoke test")
    ap.add_argument("--make-test-adapter", metavar="DIR", help="write a random adapter to DIR and exit")
    a = ap.parse_args()

    adapters = pairs(a.adapters, "adapter", "adapter_config.json")
    systems = [(n, p.read_text()) for n, p in pairs(a.system_file, "system file")]
    tok, model = load_base(a.base, a.revision)
    if a.make_test_adapter:
        make_test_adapter(model, Path(a.make_test_adapter))
        return
    if not a.items:
        raise SystemExit("--items is required")

    items = [json.loads(ln) for ln in Path(a.items).read_text().splitlines() if ln.strip()]
    items = items[:a.limit] if a.limit else items
    ids = [it["id"] for it in items]
    prompts = [render(tok, it["qtext"], start=a.assistant_start) for it in items]
    suffix = "" if a.assistant_start == "think_off" else f"__{a.assistant_start}"
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    common = {
        "base_model": a.base,
        "revision": getattr(model.config, "_commit_hash", None) or a.revision,
        "model_class": type(model).__name__,
        "items": a.items,
        "generation": {"do_sample": False, "temperature": 0, "max_new_tokens": a.max_new_tokens,
                       "batch_size": a.batch_size, "dtype": "bfloat16",
                       "thinking_switch_in_template": "enable_thinking" in (tok.chat_template or ""),
                       "assistant_start": a.assistant_start},
        "versions": versions(),
    }
    base_print = fingerprint(model, tok, prompts[0])
    summaries: dict[str, dict] = {}
    probe_rows = ([json.loads(ln) for ln in Path(a.probe).read_text().splitlines() if ln.strip()][:a.probe_n]
                  if a.probe else [])
    probes: dict[str, dict] = {}

    def run(name: str, m, tk, run_prompts: list[str], adapter: dict | None = None, system: str | None = None) -> None:
        if complete(out, name, ids, (adapter or {}).get("sha256"), system) and not a.force:
            print(f"[{name}] output is complete, skipped")
            summaries[name] = json.loads((out / f"eval_{name}_summary.json").read_text())
            return
        t0 = time.time()
        print(f"[{name}] generating {len(run_prompts)} responses", flush=True)
        rows = []
        for it, g in zip(items, generate(m, tk, run_prompts, a.batch_size, a.max_new_tokens)):
            parsed, lastline = parse_final(g["text"])
            o = outcome(parsed, it["answer"])
            rows.append({"id": it["id"], "model": name, "answer": it["answer"], "text": g["text"],
                         "parsed": parsed, "parsed_lastline": lastline, "outcome": o, "correct": o == "correct",
                         "n_tokens": g["n_tokens"], "prompt_tokens": g["prompt_tokens"], "finish": g["finish"]})
        (out / f"eval_{name}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        s = {"model": name, **summarise(rows), "adapter": adapter, "system_prompt": system,
             "seconds": round(time.time() - t0, 1), **common, "prompt_example": run_prompts[0]}
        base_rows = out / "eval_base.jsonl"
        if adapter and base_rows.exists():
            base_text = {d["id"]: d["text"] for d in map(json.loads, base_rows.read_text().splitlines())}
            s["responses_differing_from_base"] = sum(base_text.get(r["id"]) != r["text"] for r in rows)
        (out / f"eval_{name}_summary.json").write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n")
        summaries[name] = s

    if not a.skip_base:
        run(f"base{suffix}", model, tok, prompts)
    for name, text in systems:
        run(f"base_{name}{suffix}", model, tok,
            [render(tok, it["qtext"], system=text, start=a.assistant_start) for it in items], system=text)
    if probe_rows:
        probes["base"] = probe(model, tok, probe_rows)
        print("[base] format probe", probes["base"], flush=True)

    for name, d in adapters:
        peft_model, info = attach(model, name, d)
        info["logit_shift_first_prompt"] = float((fingerprint(peft_model, tok, prompts[0]) - base_print).abs().max())
        if info["logit_shift_first_prompt"] == 0:
            print(f"WARNING [{name}] the adapter does not change the logits of the first prompt")
        shipped, own_tok, own_prompts = shipped_files(d, tok, items, prompts, a.assistant_start)
        info["shipped_files"] = shipped
        if shipped.get("chat_template_same_text") is False:
            print(f"NOTE [{name}] the adapter folder ships another chat template; with it "
                  f"{shipped['prompts_same_token_ids']} of {shipped['prompts']} prompts are the same tokens")
        if probe_rows:
            probes[name] = probe(peft_model, tok, probe_rows)
            print(f"[{name}] format probe", probes[name], flush=True)
        run(f"{name}{suffix}", peft_model, tok, prompts, adapter=info)
        if own_tok is not None:
            run(f"{name}_shipped{suffix}", peft_model, own_tok, own_prompts, adapter=info)
        model = peft_model.unload()
        del peft_model
        torch.cuda.empty_cache()
        drift = float((fingerprint(model, tok, prompts[0]) - base_print).abs().max())
        if drift > 1e-3:
            raise SystemExit(f"base model not restored after adapter {name}: logit drift {drift}")

    (out / f"eval_summary{suffix}.json").write_text(json.dumps(summaries, indent=2, ensure_ascii=False) + "\n")
    if probes:
        (out / "format_probe.json").write_text(json.dumps(
            {"rows": a.probe, "n": len(probe_rows), "unit": "mean negative log-likelihood per completion token",
             "models": probes}, indent=2) + "\n")
    print(f"\n{'model':<24}{'n':>5}{'abstain':>9}{'accuracy':>10}{'wrong':>8}{'unparsed':>10}{'penalised':>11}")
    for name, s in summaries.items():
        print(f"{name:<24}{s['n']:>5}{s['abstention_rate']:>9.3f}{s['accuracy']:>10.3f}{s['wrong_rate']:>8.3f}"
              f"{s['unparsed_rate']:>10.3f}{s['penalised_score']:>11.3f}")


if __name__ == "__main__":
    main()
