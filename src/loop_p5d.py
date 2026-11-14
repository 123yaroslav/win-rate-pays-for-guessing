"""Prediction P5d of the pre-registration: judge duels between the test outputs of two fine-tuned models.

For every evaluation question where the two models' outputs differ in the option named or in abstaining,
the two raw outputs are judged against each other with the default instruction by the three OpenRouter
judges, in both orders. The score of a question is the share of its two orders won by the first model.

    python src/loop_p5d.py J K
"""
from __future__ import annotations

import asyncio
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from duels import JUDGE_SYSTEM, Client, parse_letter  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
JUDGES = ["openrouter/anthropic/claude-haiku-5.5", "openrouter/openai/gpt-5.6-luna",
          "openrouter/mistralai/mistral-small-2603"]
B = 10000


def load(name: str) -> dict[str, dict]:
    rows = [json.loads(l) for l in (ROOT / f"results/study5/eval_{name}.jsonl").read_text().splitlines() if l.strip()]
    return {r.get("id") or r.get("item") or r.get("item_id"): r for r in rows}


def text_of(r: dict) -> str:
    return r.get("text") or r.get("raw") or r.get("response") or ""


async def main(m1: str, m2: str) -> None:
    items = {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "data/items/medqa_eval.jsonl").read_text().splitlines()}
    r1, r2 = load(m1), load(m2)
    ids = [i for i in items if i in r1 and i in r2 and r1[i].get("parsed") != r2[i].get("parsed")]
    cl = Client(ROOT / f"results/study5/p5d_{m1}_{m2}", or_budget=0.35, or_conc=6, gap=1.45)
    res = []

    async def duel(j: str, i: str, flip: bool) -> None:
        first, second = (r2[i], r1[i]) if flip else (r1[i], r2[i])
        user = (f"User question:\n{items[i]['qtext']}\n\nResponse A:\n{text_of(first).strip()}\n\n"
                f"Response B:\n{text_of(second).strip()}\n\nWhich response is better, A or B?")
        t = await cl.ask(j, JUDGE_SYSTEM["default"], user, 16, {"kind": "p5d", "item": i, "flip": flip})
        ch = parse_letter(t, "AB")
        if ch:
            res.append((j, i, (ch == "A") != flip))  # True when the first model wins

    await asyncio.gather(*[duel(j, i, f) for i in ids for f in (False, True) for j in JUDGES])
    await cl.http.aclose()
    rng = random.Random(20261115)
    out = {"model_1": m1, "model_2": m2, "questions_that_differ": len(ids), "questions": len(items), "judges": {}}
    key = {i: items[i]["answer"] for i in ids}

    def kind(i: str) -> str:
        a, b = r1[i].get("parsed"), r2[i].get("parsed")
        def c(x):
            return "abstain" if x == "ABSTAIN" else "right" if x == key[i] else "wrong"
        return f"{m1} {c(a)}, {m2} {c(b)}"

    lines = [f"Duels between the test outputs of model {m1} and model {m2}. {len(ids)} of {len(items)} questions "
             f"differ in option or abstention.", "",
             f"| judge | {m1} wins | 95% CI | questions | bootstrap share at or below 0.5 |", "|---|---|---|---|---|"]
    for j in JUDGES:
        sc: dict[str, list[float]] = {}
        for jj, i, w in res:
            if jj == j:
                sc.setdefault(i, []).append(1.0 if w else 0.0)
        qs = list(sc)
        m = sum(sum(v) / len(v) for v in sc.values()) / len(qs) if qs else float("nan")
        draws = sorted(sum(sum(sc[q]) / len(sc[q]) for q in (rng.choice(qs) for _ in qs)) / len(qs) for _ in range(B)) if qs else []
        lo, hi = (draws[int(0.025 * B)], draws[int(0.975 * B)]) if draws else (float("nan"), float("nan"))
        p = sum(d <= 0.5 for d in draws) / B if draws else float("nan")
        by = {}
        for q in qs:
            by.setdefault(kind(q), []).append(sum(sc[q]) / len(sc[q]))
        out["judges"][j] = {"rate": m, "lo": lo, "hi": hi, "n": len(qs), "p_le_half": p,
                            "by_kind": {k: {"rate": sum(v) / len(v), "n": len(v)} for k, v in sorted(by.items())}}
        lines.append(f"| {j.split('/')[-1]} | {m:.1%} | {lo:.1%} to {hi:.1%} | {len(qs)} | {p:.4f} |")
    lines += ["", f"By what the two outputs are (share of duels won by {m1}, pooled view per judge in the JSON).", ""]
    kinds = sorted({k for j in JUDGES for k in out["judges"][j]["by_kind"]})
    lines += ["| outputs | " + " | ".join(j.split("/")[-1] for j in JUDGES) + " | questions |", "|---|" + "---|" * (len(JUDGES) + 1)]
    for k in kinds:
        cells = [out["judges"][j]["by_kind"].get(k) for j in JUDGES]
        n = max((c["n"] for c in cells if c), default=0)
        lines.append(f"| {k} | " + " | ".join("-" if not c else f"{c['rate']:.0%}" for c in cells) + f" | {n} |")
    lines.append(f"\nspend {cl.or_spend:.3f} USD")
    (ROOT / f"results/study5/p5d_{m1}_{m2}.md").write_text("\n".join(lines) + "\n")
    (ROOT / f"results/study5/p5d_{m1}_{m2}.json").write_text(json.dumps(out, indent=1))
    print("\n".join(lines))


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
