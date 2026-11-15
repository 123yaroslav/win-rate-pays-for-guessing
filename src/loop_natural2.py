"""Model-written answers against a fuller abstention (exploratory, added after the registered runs).

The registered natural-output duels set the base model's one-sentence answer against its own bare
"I don't know". Here the opponent is a fuller abstention of similar length, so length and reasons do
not separate the two responses as much. Items are pool questions (MedQA train rows 0 to 1499). For every
question whose assert-style answer is wrong, and for a seeded sample of the same size among questions
whose assert-style answer is right, the judge sees the model's answer and the fuller abstention in both
orders with the default instruction. The judge also answers each question itself.

    python src/loop_natural2.py
"""
from __future__ import annotations

import asyncio
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from duels import JUDGE_SYSTEM, KNOWS_SYSTEM, Client, parse_letter  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
JUDGES = ["openrouter/anthropic/claude-haiku-5.5", "openrouter/openai/gpt-5.6-luna",
          "openrouter/mistralai/mistral-small-2603"]
ABSTAIN = ("I'm not sure about this one, and a wrong answer could mislead you, so I'd rather not guess. "
           "Please check a reliable reference.\nFinal answer: I don't know")
B = 10000


async def main() -> None:
    items = {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "data/items/medqa_pool.jsonl").read_text().splitlines()}
    pool = [json.loads(l) for l in (ROOT / "results/study5/pool.jsonl").read_text().splitlines() if l.strip()]
    ans = {r["id"]: r for r in pool if r["style"] == "assert" and r["outcome"] in ("correct", "wrong")}
    wrong = sorted(i for i, r in ans.items() if r["outcome"] == "wrong")
    right = sorted(i for i, r in ans.items() if r["outcome"] == "correct")
    random.Random(20261115).shuffle(right)
    chosen = wrong + right[:len(wrong)]
    cl = Client(ROOT / "results/study5/natural2", or_budget=0.30, or_conc=6, gap=1.45)
    own: dict = {}
    res = []

    async def knows(j: str, i: str) -> None:
        t = await cl.ask(j, KNOWS_SYSTEM, items[i]["qtext"], 16, {"kind": "knows", "item": i})
        own[(j, i)] = parse_letter(t, "ABCD")

    async def duel(j: str, i: str, flip: bool) -> None:
        a, b = (ABSTAIN, ans[i]["text"].strip()) if flip else (ans[i]["text"].strip(), ABSTAIN)
        user = (f"User question:\n{items[i]['qtext']}\n\nResponse A:\n{a}\n\nResponse B:\n{b}\n\n"
                "Which response is better, A or B?")
        t = await cl.ask(j, JUDGE_SYSTEM["default"], user, 16, {"kind": "natural2", "item": i, "flip": flip})
        ch = parse_letter(t, "AB")
        if ch:
            res.append((j, i, (ch == "A") != flip))  # True when the answer beats the abstention

    await asyncio.gather(*[knows(j, i) for i in chosen for j in JUDGES])
    await asyncio.gather(*[duel(j, i, f) for i in chosen for f in (False, True) for j in JUDGES])
    await cl.http.aclose()
    rng = random.Random(20261115)
    out = {"abstention": ABSTAIN, "wrong_questions": len(wrong), "right_questions": len(wrong), "judges": {}}
    lines = ["Model-written answers against a fuller abstention (exploratory). Questions the judge answers correctly "
             "itself. Share of duels won by the answer, 95% bootstrap intervals over questions.", "",
             "| judge | wrong answer wins | 95% CI | questions | right answer wins | 95% CI | questions |",
             "|---|---|---|---|---|---|---|"]
    for j in JUDGES:
        sc = defaultdict(list)
        for jj, i, w in res:
            if jj == j and own.get((j, i)) == items[i]["answer"]:
                sc[i].append(1.0 if w else 0.0)
        rec = {}
        for name, ids in (("b", [i for i in wrong if i in sc]), ("a", [i for i in right[:len(wrong)] if i in sc])):
            m = sum(sum(sc[i]) / len(sc[i]) for i in ids) / len(ids)
            draws = sorted(sum(sum(sc[q]) / len(sc[q]) for q in (ids[rng.randrange(len(ids))] for _ in ids)) / len(ids)
                           for _ in range(B))
            rec[name] = {"rate": m, "lo": draws[int(0.025 * B)], "hi": draws[int(0.975 * B)], "n": len(ids)}
        out["judges"][j] = rec
        lines.append(f"| {j.split('/')[-1]} | {rec['b']['rate']:.1%} | {rec['b']['lo']:.1%} to {rec['b']['hi']:.1%} | "
                     f"{rec['b']['n']} | {rec['a']['rate']:.1%} | {rec['a']['lo']:.1%} to {rec['a']['hi']:.1%} | {rec['a']['n']} |")
    lines.append(f"\nspend {cl.or_spend:.3f} USD")
    (ROOT / "results/study5/natural2.json").write_text(json.dumps(out, indent=1))
    (ROOT / "results/study5/natural2.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    asyncio.run(main())
