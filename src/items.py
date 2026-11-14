"""Build item files (multiple-choice questions with a key) from the Hugging Face datasets server.

Each row gets a stable id and one planted wrong option, drawn with a seed that depends only on the id.

    python src/items.py --domain medqa --offset 400 --n 100 --out data/items/medqa_confirm.jsonl
    python src/items.py --domain law   --offset 100 --n 100 --out data/items/law_confirm.jsonl
"""
from __future__ import annotations

import argparse
import json
import random
import time
import urllib.parse
import urllib.request
from pathlib import Path

SOURCES = {
    "medqa": ("GBaker/MedQA-USMLE-4-options", "default"),
    "law": ("cais/mmlu", "professional_law"),
    "geo": ("cais/mmlu", "high_school_geography"),
}
SEED = 20261115


def fetch(dataset: str, config: str, offset: int, n: int, split: str = "test") -> list[dict]:
    rows: list[dict] = []
    while len(rows) < n:
        q = urllib.parse.urlencode({"dataset": dataset, "config": config, "split": split,
                                    "offset": offset + len(rows), "length": min(100, n - len(rows))})
        for attempt in range(6):
            try:
                with urllib.request.urlopen(f"https://datasets-server.huggingface.co/rows?{q}", timeout=60) as r:
                    page = json.load(r)["rows"]
                break
            except Exception:  # noqa: BLE001
                time.sleep(3 * (attempt + 1))
        else:
            raise RuntimeError("datasets server did not answer")
        if not page:
            break
        rows += [{"row_idx": p["row_idx"], **p["row"]} for p in page]
    return rows


def normalise(domain: str, r: dict, split: str = "test") -> dict:
    if domain == "medqa":
        options, answer = dict(sorted(r["options"].items())), r["answer_idx"]
    else:
        options, answer = dict(zip("ABCD", r["choices"])), "ABCD"[r["answer"]]
    iid = f"{domain}-{r['row_idx']}" if split == "test" else f"{domain}-{split}-{r['row_idx']}"
    wrong = random.Random(f"{SEED}:{iid}").choice([k for k in options if k != answer])
    qtext = r["question"].strip() + "\n" + "\n".join(f"{k}. {v}" for k, v in options.items())
    return {"id": iid, "domain": domain, "question": r["question"].strip(), "options": options,
            "answer": answer, "wrong": wrong, "qtext": qtext}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", choices=sorted(SOURCES), required=True)
    ap.add_argument("--offset", type=int, required=True)
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--split", default="test")
    a = ap.parse_args()
    items = [normalise(a.domain, r, a.split) for r in fetch(*SOURCES[a.domain], a.offset, a.n, a.split)]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(it) + "\n" for it in items))
    print(a.domain, "items", len(items), "->", out)


if __name__ == "__main__":
    main()
