"""Study 5, follow-up (exploratory, designed after the registered evaluation was seen).

Rule C, "the cautious policy with no selection": for every pool question the abstain-style response is
kept as it is, with its abstentions and its unparsed responses. Nothing is filtered and no judge and no
key is used. The set is written in the row format of the other training files, and its composition is
tabled next to the registered J and K sets.

    python src/loop_followup.py

Outputs in results/study5: train_C.jsonl, selection_table_followup.json, selection_table_followup.md.
"""
from __future__ import annotations

import argparse
import json

import numpy as np

from loop_common import OUT, boot_means, interval, load_items, read_jsonl

POOL_ITEMS = "data/items/medqa_pool.jsonl"
OUTCOMES = ["abstain", "correct", "wrong", "unparsed"]
RULES = ["C", "J", "K"]
NAMES = {"C": "C, abstain style, no selection (follow-up)", "J": "J, judge, default instruction",
         "K": "K, by the key"}
B = 10000


def build_c() -> list[dict]:
    items = load_items(POOL_ITEMS)
    pool = {r["id"]: r for r in read_jsonl(OUT / "pool.jsonl") if r["style"] == "abstain"}
    assert len(pool) == len(items) == 1500
    rows = []
    for it in items:
        c = pool[it["id"]]
        rows.append({"id": it["id"], "rule": "C", "style": "abstain", "prompt": it["qtext"],
                     "completion": c["text"].strip(), "parsed": c["parsed"], "outcome": c["outcome"],
                     "key": c["key"], "how": {"by": "abstain style, no selection"}})
    (OUT / "train_C.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    return rows


def table(sets: dict[str, list[dict]], boot: int) -> dict:
    ids = [r["id"] for r in sets["C"]]
    assert all([r["id"] for r in sets[k]] == ids for k in sets), "the sets must list the same questions in order"
    n = len(ids)
    cols = [(r, o) for r in RULES for o in OUTCOMES]
    mat = np.array([[float(sets[r][i]["outcome"] == o) for r, o in cols] for i in range(n)])
    draws = boot_means(mat, boot)                     # same seed and resamples as the registered table
    col = {c: j for j, c in enumerate(cols)}
    out: dict = {"n_questions": n, "bootstrap": boot, "rules": {}, "differences": {},
                 "note": "Post hoc. Rule C was added after the registered evaluation was seen. The J and K rows "
                         "repeat the registered selection table."}
    for r in RULES:
        out["rules"][r] = {}
        for o in OUTCOMES:
            j = col[(r, o)]
            lo, hi = interval(draws[:, j])
            out["rules"][r][o] = {"share": float(mat[:, j].mean()), "count": int(mat[:, j].sum()), "lo": lo, "hi": hi}
    for a, b in [("C", "K"), ("C", "J"), ("J", "K")]:
        out["differences"][f"{a}-{b}"] = {}
        for o in OUTCOMES:
            d = draws[:, col[(a, o)]] - draws[:, col[(b, o)]]
            lo, hi = interval(d)
            out["differences"][f"{a}-{b}"][o] = {"diff": float(mat[:, col[(a, o)]].mean() - mat[:, col[(b, o)]].mean()),
                                                 "lo": lo, "hi": hi}
    return out


def markdown(t: dict) -> str:
    def cell(x: dict) -> str:
        return f"{x['share']:.1%} ({x['lo']:.1%} to {x['hi']:.1%}), {x['count']}"

    def dcell(x: dict) -> str:
        return f"{x['diff'] * 100:+.1f} pp ({x['lo'] * 100:+.1f} to {x['hi'] * 100:+.1f})"

    lines = ["Follow-up training sets (post hoc, exploratory). Rule C was added after the registered evaluation "
             "was seen: it keeps the abstain-style response of every pool question as it is, with no selection. "
             "The J and K rows repeat the registered table.", "",
             f"Composition, {t['n_questions']} questions each. Share, 95% percentile bootstrap over questions "
             f"({t['bootstrap']} resamples), and count.", "",
             "| rule | abstentions | correct | wrong | unparsed |", "|---|---|---|---|---|"]
    for r in RULES:
        lines.append(f"| {NAMES[r]} | " + " | ".join(cell(t["rules"][r][o]) for o in OUTCOMES) + " |")
    lines += ["", "Paired differences (same resampled questions).", "",
              "| difference | abstentions | correct | wrong | unparsed |", "|---|---|---|---|---|"]
    for k, row in t["differences"].items():
        lines.append(f"| {k} | " + " | ".join(dcell(row[o]) for o in OUTCOMES) + " |")
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=B)
    a = ap.parse_args()
    sets = {"C": build_c(), "J": read_jsonl(OUT / "train_J.jsonl"), "K": read_jsonl(OUT / "train_K.jsonl")}
    t = table(sets, a.boot)
    (OUT / "selection_table_followup.json").write_text(json.dumps(t, indent=1))
    md = markdown(t)
    (OUT / "selection_table_followup.md").write_text(md)
    print(md)


if __name__ == "__main__":
    main()
