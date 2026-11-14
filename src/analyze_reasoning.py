"""Did the judge reason before the verdict, and does the preference for a wrong answer depend on it?

EXPLORATORY. The "think" variant leaves the provider's reasoning mode on and lets the model decide
whether to reason. The "reason" variant requests a reasoning effort explicitly. A call counts as
reasoned when it returned at least 20 output tokens (a bare verdict is 2 to 5 tokens). Rates are over
calls on questions the judge answers correctly itself, with intervals from a bootstrap over questions.

    python src/analyze_reasoning.py
"""
from __future__ import annotations

import json
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = {"think": ["results/study4_openrouter_think300"], "reason": ["results/study4_openrouter_reason"]}
ITEMS = ["data/items/medqa_confirm.jsonl", "data/items/law_confirm.jsonl", "data/items/geo_confirm.jsonl"]
B = 10000


def letter(text: str, allowed: str) -> str | None:
    m = re.search(rf"\b([{allowed}])\b", text.strip().upper())
    return m.group(1) if m else None


def main() -> None:
    items = {}
    for f in ITEMS:
        for ln in (ROOT / f).read_text().splitlines():
            it = json.loads(ln)
            items[it["id"]] = it
    own = {}
    for ln in (ROOT / "results/study1_openrouter/calls.jsonl").read_text().splitlines():
        d = json.loads(ln)
        if d["kind"] == "knows":
            own[(d["judge"], d["item"])] = letter(d["text"], "ABCD")
    rng = random.Random(20261115)
    out: dict = {}
    lines = ["Reasoning before the verdict (exploratory). Calls on questions the judge answers correctly itself.", "",
             "| variant | judge | questions | calls that reasoned | b when it reasoned | 95% CI | calls | "
             "b when it did not | 95% CI | calls | a when it reasoned | a when it did not |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for variant, runs in RUNS.items():
        rows = defaultdict(list)   # (judge, pair, reasoned) -> [(item, win of first-named response)]
        seen = defaultdict(set)
        for run in runs:
            p = ROOT / run / "calls.jsonl"
            if not p.exists():
                continue
            for ln in p.read_text().splitlines():
                d = json.loads(ln)
                if d.get("kind") != "duel" or d.get("variant") != variant:
                    continue
                if own.get((d["judge"], d["item"])) != items[d["item"]]["answer"]:
                    continue
                ch = letter(d["text"], "AB")
                if ch is None:
                    continue
                winner = d["first"] if ch == "A" else d["second"]
                reasoned = (d.get("out") or 0) >= 20
                rows[(d["judge"], d["pair"], reasoned)].append((d["item"], 1.0 if winner == d["pair"].split("-")[0] else 0.0))
                seen[d["judge"]].add(d["item"])
        for j in sorted(seen):
            def rate(pair: str, reasoned: bool):
                xs = rows.get((j, pair, reasoned), [])
                if not xs:
                    return None
                by = defaultdict(list)
                for i, w in xs:
                    by[i].append(w)
                ids = list(by)
                m = sum(w for _, w in xs) / len(xs)
                draws = []
                for _ in range(B):
                    s = [ids[rng.randrange(len(ids))] for _ in ids]
                    tot = sum(sum(by[i]) for i in s)
                    n = sum(len(by[i]) for i in s)
                    draws.append(tot / n)
                draws.sort()
                return {"rate": m, "lo": draws[int(0.025 * B)], "hi": draws[int(0.975 * B)], "calls": len(xs),
                        "questions": len(ids)}
            n_r = sum(len(rows.get((j, p, True), [])) for p in ("CW-IDK", "CC-IDK"))
            n_n = sum(len(rows.get((j, p, False), [])) for p in ("CW-IDK", "CC-IDK"))
            rec = {"questions": len(seen[j]), "share_reasoned": n_r / (n_r + n_n) if n_r + n_n else float("nan"),
                   "b_reasoned": rate("CW-IDK", True), "b_not": rate("CW-IDK", False),
                   "a_reasoned": rate("CC-IDK", True), "a_not": rate("CC-IDK", False)}
            out[f"{variant}|{j}"] = rec

            def f(c, k="rate"):
                return "-" if not c else f"{c[k]:.0%}"
            def ci(c):
                return "-" if not c else f"{c['lo']:.0%} to {c['hi']:.0%}"
            def n(c):
                return "-" if not c else str(c["calls"])
            lines.append(f"| {variant} | {j.split('/')[-1]} | {rec['questions']} | {rec['share_reasoned']:.0%} | "
                         f"{f(rec['b_reasoned'])} | {ci(rec['b_reasoned'])} | {n(rec['b_reasoned'])} | "
                         f"{f(rec['b_not'])} | {ci(rec['b_not'])} | {n(rec['b_not'])} | {f(rec['a_reasoned'])} | {f(rec['a_not'])} |")
    (ROOT / "results/study4/reasoning.json").write_text(json.dumps(out, indent=1))
    (ROOT / "results/study4/reasoning.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
