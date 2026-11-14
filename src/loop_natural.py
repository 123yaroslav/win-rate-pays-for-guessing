"""Study 5, natural-output duels (prediction P5a).

On pool questions where the abstain-style response abstains, the assert-style response of the same model
is judged against that abstention, in both orders, with the default instruction, by the three OpenRouter
judges. b_nat is the rate at which a WRONG assert-style answer beats the abstention, a_nat the same for a
CORRECT one. The score of a question is the share of its two orders won by the assert-style response.

If more than 400 questions qualify, a seeded sample of 400 is used. Questions whose assert-style response
has no parsed option cannot be classed as right or wrong and are left out (counted in the output).

    python src/loop_natural.py
"""
from __future__ import annotations

import argparse
import asyncio
import json
import random

import numpy as np

from duels import JUDGE_SYSTEM, parse_letter
from loop_common import OUT, SEED, Client, boot_means, interval, load_items, read_jsonl
from loop_select import natural_duel_prompt

POOL_ITEMS = "data/items/medqa_pool.jsonl"
JUDGES = ["anthropic/claude-haiku-5.5", "openai/gpt-5.6-luna", "mistralai/mistral-small-2603"]
MAX_ITEMS = 400
B = 10000


def rate(scores: list[float], boot: int, seed: int) -> dict:
    if not scores:
        return {"rate": None, "n": 0}
    v = np.array(scores)[:, None]
    d = boot_means(v, boot, seed)[:, 0]
    lo, hi = interval(d)
    return {"rate": float(v.mean()), "lo": lo, "hi": hi, "n": len(scores),
            "boot_share_le_half": float((d <= 0.5).mean()), "boot_share_ge_half": float((d >= 0.5).mean())}


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="use only the first N sampled questions (smoke test)")
    ap.add_argument("--conc", type=int, default=6)
    ap.add_argument("--boot", type=int, default=B)
    a = ap.parse_args()
    items = {it["id"]: it for it in load_items(POOL_ITEMS)}
    pool: dict[str, dict[str, dict]] = {}
    for r in read_jsonl(OUT / "pool.jsonl"):
        pool.setdefault(r["id"], {})[r["style"]] = r
    eligible = [i for i in items if pool[i]["abstain"]["outcome"] == "abstain"]
    sample = eligible if len(eligible) <= MAX_ITEMS else random.Random(f"{SEED}:natural").sample(eligible, MAX_ITEMS)
    used = [i for i in sample if pool[i]["assert"]["outcome"] in ("correct", "wrong")]
    left_out = {o: sum(pool[i]["assert"]["outcome"] == o for i in sample) for o in ("abstain", "unparsed")}
    if a.limit:
        used = used[:a.limit]

    cl = Client("natural", a.conc, reuse=("select",))
    wins: dict[tuple[str, str], list[float]] = {}
    counts = {j: {"calls": 0, "unparsed": 0, "first": 0, "parsed": 0} for j in JUDGES}
    failed = []

    async def duel(j: str, i: str, flip: bool) -> None:
        first, second = ("abstain", "assert") if flip else ("assert", "abstain")
        user = natural_duel_prompt(items[i]["qtext"], pool[i][first]["text"].strip(), pool[i][second]["text"].strip())
        rec = await cl.ask(j, JUDGE_SYSTEM["default"], user, 16,
                           {"kind": "natural", "variant": "default", "item": i, "pair": "assert-abstain",
                            "first": first, "second": second, "assert_outcome": pool[i]["assert"]["outcome"]})
        if rec is None:
            failed.append((j, i, flip))
            return
        c = counts[j]
        c["calls"] += 1
        ch = parse_letter(rec["text"], "AB")
        if ch is None:
            c["unparsed"] += 1
            return
        c["parsed"] += 1
        c["first"] += ch == "A"
        wins.setdefault((j, i), []).append(float((first if ch == "A" else second) == "assert"))

    await asyncio.gather(*[duel(j, i, f) for i in used for f in (False, True) for j in JUDGES])
    await cl.close()
    if failed:
        raise SystemExit(f"{len(failed)} judge calls failed, rerun to fill them in: {failed[:5]}")

    out: dict = {"pool_questions": len(items), "abstain_style_abstains": len(eligible), "sampled": len(sample),
                 "sample_rule": f"all qualifying questions (at most {MAX_ITEMS}, else a seeded sample)",
                 "left_out_assert_not_an_option": left_out, "used": len(used),
                 "assert_wrong": sum(pool[i]["assert"]["outcome"] == "wrong" for i in used),
                 "assert_correct": sum(pool[i]["assert"]["outcome"] == "correct" for i in used),
                 "bootstrap": a.boot, "natural_step_spend_usd": round(cl.spent, 4), "judges": {}}
    lines = [f"Natural-output duels: the assert-style response against the abstain-style abstention of the same "
             f"model on the same question, both orders, default instruction. {len(eligible)} of {len(items)} pool "
             f"questions have an abstain-style abstention, {len(sample)} were sampled, {len(used)} have an "
             f"assert-style response with a parsed option ({out['assert_wrong']} wrong, {out['assert_correct']} "
             f"correct by the key). Intervals are 95% item bootstraps ({a.boot} resamples).", "",
             "| judge | b_nat, wrong answer beats abstention | 95% CI | items | bootstrap share b_nat <= 0.5 | "
             "a_nat, correct answer beats abstention | 95% CI | items | picks first position | unparsed verdicts |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for k, j in enumerate(JUDGES):
        score = {i: sum(wins[(j, i)]) / len(wins[(j, i)]) for i in used if (j, i) in wins}
        b = rate([score[i] for i in score if pool[i]["assert"]["outcome"] == "wrong"], a.boot, SEED + k)
        aa = rate([score[i] for i in score if pool[i]["assert"]["outcome"] == "correct"], a.boot, SEED + 100 + k)
        c = counts[j]
        out["judges"][j] = {"b_nat": b, "a_nat": aa, "calls": c["calls"], "unparsed": c["unparsed"],
                            "first_position": c["first"] / max(1, c["parsed"]),
                            "items_without_verdict": len(used) - len(score),
                            "p5a_holds": bool(b["n"] and b["rate"] > 0.5 and b["boot_share_le_half"] < 0.05)}
        if b["n"] and aa["n"]:
            lines.append(f"| {j} | {b['rate']:.1%} | {b['lo']:.1%} to {b['hi']:.1%} | {b['n']} | "
                         f"{b['boot_share_le_half']:.4f} | {aa['rate']:.1%} | {aa['lo']:.1%} to {aa['hi']:.1%} | "
                         f"{aa['n']} | {c['first'] / max(1, c['parsed']):.1%} | {c['unparsed']} |")
    held = [j for j in JUDGES if out["judges"][j]["p5a_holds"]]
    out["p5a"] = {"holds_for": held, "holds_for_all_three": len(held) == len(JUDGES)}
    lines += ["", f"P5a (b_nat above 0.5 for each of the three judges, bootstrap share at or below 0.5 under 0.05): "
                  f"{'holds' if len(held) == len(JUDGES) else 'does not hold'}. It holds for {len(held)} of "
                  f"{len(JUDGES)} judges" + (f" ({', '.join(held)})." if held else ".")]
    suffix = "" if not a.limit else f".first{a.limit}"
    (OUT / f"natural_duels{suffix}.json").write_text(json.dumps(out, indent=1))
    (OUT / f"natural_duels{suffix}.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    asyncio.run(main())
