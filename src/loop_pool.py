"""Study 5, step 2: the base model answers every pool question under the three fixed style instructions.

The instructions come from results/study5/style_prompts.json (written by loop_tune.py before this step).
Output: results/study5/pool.jsonl, one row per question and style, and pool_summary.json.

    python src/loop_pool.py
"""
from __future__ import annotations

import argparse
import asyncio
import json
import statistics

import numpy as np

from loop_common import (BASE_MODEL, OUT, STYLES, Client, boot_means, interval, load_items, outcome,
                         parse_final, read_jsonl, strict_final)

POOL_ITEMS = "data/items/medqa_pool.jsonl"
B = 10000


def summarise(rows: list[dict], boot: int) -> dict:
    out = {}
    kinds = ("abstain", "correct", "wrong", "unparsed")
    for s in STYLES:
        rs = [r for r in rows if r["style"] == s]
        res = {"n": len(rs)}
        mat = np.array([[float(r["outcome"] == o) for o in kinds] for r in rs])
        draws = boot_means(mat, boot)
        for j, o in enumerate(kinds):
            lo, hi = interval(draws[:, j])
            res[o] = {"share": float(mat[:, j].mean()), "lo": lo, "hi": hi, "count": int(mat[:, j].sum())}
        answered = [r for r in rs if r["outcome"] in ("correct", "wrong")]
        res["accuracy_when_answering"] = sum(r["outcome"] == "correct" for r in answered) / max(1, len(answered))
        res["strict_format"] = sum(r["strict_format"] for r in rs) / len(rs)
        res["cut_by_max_tokens"] = sum(r["finish"] == "length" for r in rs) / len(rs)
        res["median_words"] = statistics.median(len(r["text"].split()) for r in rs)
        res["median_words_when_answering"] = statistics.median([len(r["text"].split()) for r in answered] or [0])
        res["providers"] = sorted({str(r["provider"]) for r in rs})
        out[s] = res
    return out


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--conc", type=int, default=6)
    ap.add_argument("--boot", type=int, default=B)
    a = ap.parse_args()
    cfg = json.loads((OUT / "style_prompts.json").read_text())
    items = load_items(POOL_ITEMS)[:a.limit or None]
    cl = Client("gen", a.conc)
    recs: dict[tuple[str, str], dict | None] = {}

    async def one(it: dict, s: str) -> None:
        recs[(it["id"], s)] = await cl.ask(BASE_MODEL, cfg["prompts"][s], it["qtext"], cfg["max_tokens"],
                                           {"kind": "pool", "item": it["id"], "style": s}, provider=cfg["provider"])

    await asyncio.gather(*[one(it, s) for it in items for s in STYLES])
    await cl.close()
    missing = [k for k, r in recs.items() if r is None]
    if missing:
        raise SystemExit(f"{len(missing)} calls failed, rerun to fill them in: {missing[:5]}")
    rows = []
    for it in items:
        for s in STYLES:
            r = recs[(it["id"], s)]
            p = parse_final(r["text"])
            rows.append({"id": it["id"], "style": s, "text": r["text"], "parsed": p, "key": it["answer"],
                         "correct": p == it["answer"], "outcome": outcome(p, it["answer"]),
                         "strict_format": strict_final(r["text"]), "finish": r.get("finish"),
                         "out_tokens": r.get("out"), "provider": r.get("provider")})
    (OUT / "pool.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    summ = summarise(rows, a.boot)
    spend = sum(float(d.get("cost") or 0) for d in read_jsonl(cl.path) if d.get("kind") == "pool")
    summ["_meta"] = {"questions": len(items), "rows": len(rows), "pool_spend_usd": round(spend, 4),
                     "gen_step_spend_usd": round(cl.spent, 4), "bootstrap": a.boot,
                     "identical_text_across_styles": sum(
                         len({recs[(it["id"], s)]["text"] for s in STYLES}) < 3 for it in items)}
    (OUT / "pool_summary.json").write_text(json.dumps(summ, indent=1))
    for s in STYLES:
        r = summ[s]
        print(s, " ".join(f"{o} {r[o]['share']:.3f} [{r[o]['lo']:.3f}, {r[o]['hi']:.3f}]"
                          for o in ("abstain", "correct", "wrong", "unparsed")),
              f"acc when answering {r['accuracy_when_answering']:.3f} median words {r['median_words']}")
    print(summ["_meta"])


if __name__ == "__main__":
    asyncio.run(main())
