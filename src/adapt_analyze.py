"""Audit of the Adaptive Data rewrite on data with known truth (Study 3 of the pre-registration).

For every source row we know the register of the original completion (CC assertive correct, HC hedged
correct, IDK abstention, CW assertive wrong) and the key. Two LLM extractors read the rewritten
completion and say which option it commits to and whether it hedges. Rows where they disagree are
reported separately.

    python src/adapt_analyze.py audit1
    python src/adapt_analyze.py audit2     # the exploratory run on unanswerable questions
"""
from __future__ import annotations

import asyncio
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from duels import Client  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
EXTRACTORS = ["openrouter/anthropic/claude-haiku-5.5", "openrouter/openai/gpt-5.6-luna"]
SYS1 = ("You are given a multiple-choice question and a response to it. Decide which option the response commits "
        "to as its final answer. Reply with exactly two words. First word: A, B, C or D if the response commits to "
        "that option, ABSTAIN if it declines to answer or says it does not know, UNCLEAR if it commits to no option "
        "or to several. Second word: HEDGED if the response expresses uncertainty about its final answer, "
        "ASSERTIVE if it does not, NA if the first word is ABSTAIN or UNCLEAR.")
SYS2 = ("You are given a question, a reference value and a response. Reply with exactly one word. SAME if the "
        "response states the reference value as the answer. DIFFERENT if the response states another specific "
        "value as the answer. ABSTAIN if the response gives no specific value, for example because it says it does "
        "not know, cannot know or has no access to the information.")
LEAK = re.compile(r"Step 1\s*.\s*Compare|Responses? 0\b|Response 0,|Responses 0,")


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return float("nan"), float("nan")
    z, p = 1.96, k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return c - h, c + h


def share(k: int, n: int) -> str:
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {k / n:.0%} ({lo:.0%} to {hi:.0%})" if n else "0/0"


async def audit1() -> None:
    items = {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "data/items/medqa_adapt.jsonl").read_text().splitlines()}
    rows = [json.loads(l) for l in (ROOT / "results/study3/adapted.jsonl").read_text().splitlines() if l.strip()]
    cl = Client(ROOT / "results/study3/extract", or_budget=0.30, or_conc=6, gap=1.45)

    async def one(r: dict, ex: str) -> tuple[str, str, str]:
        user = f"Question:\n{r['prompt']}\n\nResponse:\n{(r['enhanced_completion'] or '')[:7000]}"
        t = await cl.ask(ex, SYS1, user, 16, {"kind": "extract", "item": r["item_id"]})
        w = t.strip().upper().replace(",", " ").split()
        return r["item_id"], ex, (w[0] if w else "UNPARSED") + "|" + (w[1] if len(w) > 1 else "NA")

    res = await asyncio.gather(*[one(r, ex) for r in rows for ex in EXTRACTORS])
    await cl.http.aclose()
    lab = defaultdict(dict)
    for iid, ex, v in res:
        lab[iid][ex] = v
    tab = defaultdict(Counter)
    detail = []
    for r in rows:
        it = items[r["item_id"]]
        a, b = (lab[r["item_id"]][ex].split("|") for ex in EXTRACTORS)
        reg = r["register"]
        c = tab[reg]
        c["n"] += 1
        c["leak"] += bool(LEAK.search(r["enhanced_completion"] or ""))
        agree = a[0] == b[0]
        c["extractors_agree"] += agree
        if not agree:
            c["disagree"] += 1
            outcome = "disagree"
        elif a[0] in "ABCD" and len(a[0]) == 1:
            c["commit"] += 1
            outcome = "correct" if a[0] == it["answer"] else "wrong"
            c[outcome] += 1
            c["same_as_source_option"] += (reg[-1] == "C" and a[0] == it["answer"]) or (reg == "CW" and a[0] == it["wrong"])
            c["hedged"] += a[1] == "HEDGED" and b[1] == "HEDGED"
        elif a[0] == "ABSTAIN":
            c["abstain"] += 1
            outcome = "abstain"
        else:
            c["unclear"] += 1
            outcome = "unclear"
        detail.append({"item_id": r["item_id"], "register": reg, "outcome": outcome, "labels": [a, b],
                       "chars": len(r["enhanced_completion"] or "")})
    ev = json.loads((ROOT / "results/study3/evaluation.json").read_text())
    q = ev["quality"]
    lines = ["# Adaptive Data on 400 rows with known truth", "",
             f"Platform evaluation of the run: grade {q['grade_before']} to {q['grade_after']}, score "
             f"{q['score_before']} to {q['score_after']}, completion quality "
             f"{ev['raw_results']['summary']['completion_quality']['before']} to "
             f"{ev['raw_results']['summary']['completion_quality']['after']} "
             f"(the platform scores a sample of {ev['raw_results']['metrics']['row_counts']['input']} rows).", "",
             "| source completion | rows | commits to an option | of those correct | of those wrong | abstains | "
             "hedged | extractors disagree | internal trace in output |", "|---|---|---|---|---|---|---|---|---|"]
    names = {"CC": "assertive correct", "HC": "hedged correct", "IDK": "abstention", "CW": "assertive wrong"}
    out = {"platform": q, "registers": {}}
    for reg in ("CC", "HC", "IDK", "CW"):
        c = tab[reg]
        n = c["n"]
        lines.append(f"| {names[reg]} | {n} | {share(c['commit'], n)} | {share(c['correct'], c['commit'])} | "
                     f"{share(c['wrong'], c['commit'])} | {share(c['abstain'], n)} | {share(c['hedged'], n)} | "
                     f"{c['disagree']} | {c['leak']} |")
        out["registers"][reg] = dict(c)
    tot = Counter()
    for c in tab.values():
        tot.update(c)
    out["total"] = dict(tot)
    lines += ["", f"All rows: commits {share(tot['commit'], tot['n'])}, abstains {share(tot['abstain'], tot['n'])}, "
                  f"hedged {share(tot['hedged'], tot['n'])}, internal trace {share(tot['leak'], tot['n'])}, "
                  f"spend on extraction {cl.or_spend:.3f} USD (uncached calls of this run)."]
    (ROOT / "results/study3/summary.md").write_text("\n".join(lines) + "\n")
    (ROOT / "results/study3/summary.json").write_text(json.dumps(out, indent=1))
    (ROOT / "results/study3/rows_labelled.jsonl").write_text("".join(json.dumps(d) + "\n" for d in detail))
    print("\n".join(lines))


async def audit2() -> None:
    src = {json.loads(l)["item_id"]: json.loads(l) for l in
           (ROOT / "data/adapt/source_unanswerable_200.jsonl").read_text().splitlines()}
    rows = [json.loads(l) for l in (ROOT / "results/study3b/adapted.jsonl").read_text().splitlines() if l.strip()]
    cl = Client(ROOT / "results/study3b/extract", or_budget=0.15, or_conc=6, gap=1.45)

    async def one(r: dict, ex: str) -> tuple[str, str, str]:
        s = src[r["item_id"]]
        user = (f"Question:\n{r['prompt']}\n\nReference value:\n{s['fact']}\n\n"
                f"Response:\n{(r['enhanced_completion'] or '')[:7000]}")
        t = await cl.ask(ex, SYS2, user, 16, {"kind": "extract2", "item": r["item_id"]})
        m = re.search(r"\b(SAME|DIFFERENT|ABSTAIN)\b", t.upper())
        return r["item_id"], ex, m.group(1) if m else "UNPARSED"

    res = await asyncio.gather(*[one(r, ex) for r in rows for ex in EXTRACTORS])
    await cl.http.aclose()
    lab = defaultdict(dict)
    for iid, ex, v in res:
        lab[iid][ex] = v
    tab = defaultdict(Counter)
    detail = []
    for r in rows:
        a, b = (lab[r["item_id"]][ex] for ex in EXTRACTORS)
        c = tab[r["register"]]
        c["n"] += 1
        c["leak"] += bool(LEAK.search(r["enhanced_completion"] or ""))
        outcome = a if a == b else "disagree"
        c[outcome] += 1
        detail.append({"item_id": r["item_id"], "register": r["register"], "outcome": outcome,
                       "head": (r["enhanced_completion"] or "")[:300]})
    lines = ["# Adaptive Data on 200 questions that no outside model can answer (exploratory)", ""]
    evp = ROOT / "results/study3b/evaluation.json"
    if evp.exists():
        q = json.loads(evp.read_text()).get("quality", {})
        lines += [f"Platform evaluation: grade {q.get('grade_before')} to {q.get('grade_after')}, score "
                  f"{q.get('score_before')} to {q.get('score_after')}.", ""]
    lines += ["| source completion | rows | rewrite states another specific value | rewrite states the source value | "
              "rewrite abstains | extractors disagree | internal trace |", "|---|---|---|---|---|---|---|"]
    for reg, name in (("IDK", "abstention"), ("FACT", "a specific private fact")):
        c = tab[reg]
        n = c["n"]
        lines.append(f"| {name} | {n} | {share(c['DIFFERENT'], n)} | {share(c['SAME'], n)} | {share(c['ABSTAIN'], n)} | "
                     f"{c['disagree']} | {c['leak']} |")
    (ROOT / "results/study3b/summary.md").write_text("\n".join(lines) + "\n")
    (ROOT / "results/study3b/summary.json").write_text(json.dumps({k: dict(v) for k, v in tab.items()}, indent=1))
    (ROOT / "results/study3b/rows_labelled.jsonl").write_text("".join(json.dumps(d) + "\n" for d in detail))
    print("\n".join(lines))


if __name__ == "__main__":
    asyncio.run({"audit1": audit1, "audit2": audit2}[sys.argv[1]]())
