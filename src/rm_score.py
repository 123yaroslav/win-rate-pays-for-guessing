"""Reward-model scores for Amendment 4, part B. Runs on a GPU machine.

Every row of the inputs file (src/rm_inputs.py) is scored alone as a two-turn chat [user, assistant]
rendered with the model's own chat template. Weights in bfloat16, one forward pass per response, no
sampling. The score is the single logit of the sequence-classification head, as on the model cards.

    python rm_score.py --inputs inputs.jsonl --out scores.jsonl \
        --models Skywork/Skywork-Reward-V2-Llama-3.1-8B Skywork/Skywork-Reward-V2-Qwen3-8B

A model that is already complete in the output file is skipped. Per model the hub revision, the
rendered text of the first row and the token counts go to <out>.meta.jsonl.
"""
from __future__ import annotations

import argparse
import json
import shutil
import time
import traceback
from pathlib import Path

import torch
from huggingface_hub import snapshot_download
from transformers import AutoModel, AutoModelForSequenceClassification, AutoTokenizer

REMOTE_CODE = {"internlm/internlm2-7b-reward"}   # fallback model whose card loads it with its own code


def load(name: str, path: str):
    tok = AutoTokenizer.from_pretrained(path, trust_remote_code=name in REMOTE_CODE)
    kw = {"device_map": "cuda", "trust_remote_code": name in REMOTE_CODE}
    cls = AutoModel if name in REMOTE_CODE else AutoModelForSequenceClassification
    if cls is AutoModelForSequenceClassification:
        kw["num_labels"] = 1
    try:
        model = cls.from_pretrained(path, dtype=torch.bfloat16, **kw)
    except TypeError:
        model = cls.from_pretrained(path, torch_dtype=torch.bfloat16, **kw)
    model.eval()
    return tok, model


def render(tok, user: str, assistant: str) -> str:
    return tok.apply_chat_template([{"role": "user", "content": user}, {"role": "assistant", "content": assistant}],
                                   tokenize=False)


@torch.no_grad()
def score(name: str, tok, model, user: str, assistant: str) -> tuple[float, int, bool]:
    if name in REMOTE_CODE:   # the card's documented call, which applies the template itself
        chat = [{"role": "user", "content": user}, {"role": "assistant", "content": assistant}]
        return float(model.get_score(tok, chat)), -1, False
    text = render(tok, user, assistant)
    # the same tokens as apply_chat_template(tokenize=True): the template already holds any BOS token
    ids = tok(text, add_special_tokens=False, return_tensors="pt").to(model.device)
    logits = model(**ids).logits
    # the head reads the last token that is not the pad token, so a final pad-id token is noted
    last_is_pad = int(ids["input_ids"][0, -1]) == getattr(model.config, "pad_token_id", None)
    return float(logits[0][0].float().item()), int(ids["input_ids"].shape[1]), last_is_pad


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--cache", default="/workspace/hf")
    ap.add_argument("--keep-cache", action="store_true")
    a = ap.parse_args()
    rows = [json.loads(ln) for ln in Path(a.inputs).read_text().splitlines() if ln.strip()]
    out, meta = Path(a.out), Path(a.out + ".meta.jsonl")
    done: dict[str, int] = {}
    if out.exists():
        for ln in out.read_text().splitlines():
            if ln.strip():
                m = json.loads(ln)["model"]
                done[m] = done.get(m, 0) + 1
    for name in a.models:
        if done.get(name, 0) == len(rows):
            print(f"{name}: already complete", flush=True)
            continue
        if done.get(name):
            raise SystemExit(f"{name}: partial output in {out}, remove its lines first")
        t0 = time.time()
        try:
            pats = ["*.json", "*.safetensors", "*.model", "*.py", "*.txt", "*.jinja", "tokenizer*"]
            path = snapshot_download(name, cache_dir=a.cache, allow_patterns=pats)
            if not list(Path(path).glob("*.safetensors")):   # a repository with .bin weights only
                path = snapshot_download(name, cache_dir=a.cache, allow_patterns=pats + ["*.bin"])
            revision = Path(path).name
            tok, model = load(name, path)
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            with meta.open("a") as f:
                f.write(json.dumps({"model": name, "status": "load_failed", "error": repr(e)[:2000]}) + "\n")
            print(f"{name}: LOAD FAILED {e!r}", flush=True)
            continue
        t1 = time.time()
        first = render(tok, rows[0]["user"], rows[0]["assistant"]) if name not in REMOTE_CODE else None
        recs, ntok, npad = [], [], 0
        for r in rows:
            s, n, lp = score(name, tok, model, r["user"], r["assistant"])
            recs.append({"model": name, "set": r["set"], "item": r["item"], "resp": r["resp"], "score": s})
            ntok.append(n)
            npad += lp
        with out.open("a") as f:
            f.write("".join(json.dumps(x) + "\n" for x in recs))
        info = {"model": name, "status": "ok", "revision": revision, "n": len(recs),
                "download_load_s": round(t1 - t0, 1), "score_s": round(time.time() - t1, 1),
                "tokens_min": min(ntok), "tokens_max": max(ntok), "rows_ending_in_pad_id": npad,
                "bos": tok.bos_token, "eos": tok.eos_token, "pad": tok.pad_token,
                "pad_token_id_config": getattr(model.config, "pad_token_id", None),
                "rendered_first_row": first,
                "torch": torch.__version__, "transformers": __import__("transformers").__version__}
        with meta.open("a") as f:
            f.write(json.dumps(info) + "\n")
        print(f"{name}: revision {revision}, {len(recs)} scores, load {info['download_load_s']} s, "
              f"score {info['score_s']} s, scores {min(x['score'] for x in recs):.3f} to "
              f"{max(x['score'] for x in recs):.3f}", flush=True)
        del model
        torch.cuda.empty_cache()
        if not a.keep_cache:
            shutil.rmtree(Path(a.cache) / ("models--" + name.replace("/", "--")), ignore_errors=True)


if __name__ == "__main__":
    main()
