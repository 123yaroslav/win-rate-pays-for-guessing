"""How much do the main rates depend on the reply parser? (Reported in the deviations.)

The duel parser takes the first standalone A or B in a reply. A strict reading accepts only replies
that are a bare letter, optionally with a period, brackets or the word "Response". This script
recomputes b on known questions for the primary pair under the strict reading.

    python src/strict_parse_check.py
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ["results/study1_openrouter", "results/study1_adaption"]
STRICT = re.compile(r"^\W*(?:RESPONSE\s+)?([AB])\W*$")
LOOSE = re.compile(r"\b([AB])\b")
KNOW = re.compile(r"\b([ABCD])\b")


def main() -> None:
    items = {}
    for f in ("medqa", "law", "geo"):
        for ln in (ROOT / f"data/items/{f}_confirm.jsonl").read_text().splitlines():
            it = json.loads(ln)
            items[it["id"]] = it
    own, calls = {}, defaultdict(list)
    for run in RUNS:
        for ln in (ROOT / run / "calls.jsonl").read_text().splitlines():
            d = json.loads(ln)
            if d["kind"] == "knows":
                m = KNOW.search(d["text"].strip().upper())
                own[(d["judge"], d["item"])] = m.group(1) if m else None
            elif d["kind"] == "duel" and d.get("variant") == "default" and d["pair"] == "CW-IDK":
                calls[d["judge"]].append(d)
    out = {}
    for j, cs in sorted(calls.items()):
        rec = {"calls": len(cs)}
        for name, rx in (("loose", LOOSE), ("strict", STRICT)):
            sc, miss = defaultdict(list), 0
            for d in cs:
                m = rx.search(d["text"].strip().upper())
                if not m:
                    miss += 1
                    continue
                winner = d["first"] if m.group(1) == "A" else d["second"]
                if own.get((j, d["item"])) == items[d["item"]]["answer"]:
                    sc[d["item"]].append(1.0 if winner == "CW" else 0.0)
            rec[name] = {"no_verdict": miss, "share_no_verdict": miss / len(cs), "known_questions": len(sc),
                         "b_knows": sum(sum(v) / len(v) for v in sc.values()) / len(sc)}
        out[j] = rec
        print(j.split("/")[-1], {k: (round(v["share_no_verdict"], 3), v["known_questions"], round(v["b_knows"], 3))
                                 for k, v in rec.items() if k != "calls"})
    (ROOT / "results/study1/strict_parse.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
