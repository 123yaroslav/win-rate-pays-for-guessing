"""Inputs for the reward-model scoring of Amendment 4, part B.

One row per item and response, with the question as the judges saw it in the duels and the response
text of the duels, both built by the functions of src/duels.py (multiple-choice items) and
src/freeform.py (free-form items). The file is sent to the GPU pod and scored by src/rm_score.py.

    python src/rm_inputs.py            # -> results/reward_models/inputs.jsonl
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import duels  # noqa: E402
import freeform  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MCQ = [ROOT / f"data/items/{d}_fresh.jsonl" for d in ("medqa", "law", "geo")]
FREE = ROOT / "data/items/trivia_free.jsonl"
RESPONSES = ("CC", "CW", "IDK", "IDK2")
OUT = ROOT / "results/reward_models/inputs.jsonl"


def read(p: Path) -> list[dict]:
    return [json.loads(ln) for ln in p.read_text().splitlines() if ln.strip()]


def main() -> None:
    rows = []
    for p in MCQ:
        for it in read(p):
            for k in RESPONSES:
                # the duel prompt shows item["qtext"], the question with its four options
                rows.append({"set": "mcq", "item": it["id"], "resp": k, "user": it["qtext"],
                             "assistant": duels.response_text(k, it)})
    for it in read(FREE):
        for k in RESPONSES:
            # the free-form duel prompt shows it["question"]
            rows.append({"set": "free", "item": it["id"], "resp": k, "user": it["question"],
                         "assistant": freeform.response_text(k, it)})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"{len(rows)} rows -> {OUT}, sha256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    for s in ("mcq", "free"):
        for k in RESPONSES:
            for r in [r for r in rows if r["set"] == s and r["resp"] == k][:2]:
                print(f"--- {s} {r['item']} {k}\nUSER: {r['user'][-220:]}\nASSISTANT: {r['assistant']}")


if __name__ == "__main__":
    main()
