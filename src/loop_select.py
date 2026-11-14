"""Study 5, step 3: keep one response per pool question by four rules, and describe the four selected sets.

  J  round robin of the three candidates (assert, hedge, abstain style), judged by Claude Haiku 5.5 with the
     default instruction of src/duels.py. Three duels per question, the presentation order of every duel is
     drawn with a fixed seed, the candidate with most wins is kept, ties are broken with the seed.
  F  the same with the `accuracy` instruction (same presentation orders).
  K  by the key: a correct response if there is one (seeded choice among them), else an abstention if there
     is one, else a seeded random candidate.
  R  a seeded random candidate.

The judge sees the question with its options and the two full responses, in the format of duel_prompt.
Outputs in results/study5: train_{J,F,K,R}.jsonl, selection_table.json, selection_table.md.

    python src/loop_select.py
"""
from __future__ import annotations

import argparse
import asyncio
import json
import random
from collections import Counter

import numpy as np

from duels import JUDGE_SYSTEM, parse_letter
from loop_common import OUT, SEED, STYLES, Client, boot_means, interval, load_items, read_jsonl

POOL_ITEMS = "data/items/medqa_pool.jsonl"
JUDGE = "anthropic/claude-haiku-5.5"
PAIRS = [("assert", "hedge"), ("assert", "abstain"), ("hedge", "abstain")]
RULE_VARIANT = {"J": "default", "F": "accuracy"}
OUTCOMES = ["abstain", "correct", "wrong", "unparsed"]
B = 10000


def natural_duel_prompt(qtext: str, first: str, second: str) -> str:
    """The user message of duel_prompt (src/duels.py) with real responses and no selfcheck note."""
    return (f"User question:\n{qtext}\n\nResponse A:\n{first}\n\n"
            f"Response B:\n{second}\n\nWhich response is better, A or B?")


def flipped(qid: str, pair: tuple[str, str]) -> bool:
    return random.Random(f"{SEED}:order:{qid}:{pair[0]}-{pair[1]}").random() < 0.5


def pick(rule: str, qid: str, candidates: list[str]) -> str:
    return random.Random(f"{SEED}:{rule}:{qid}").choice(sorted(candidates))


def select_by_key(qid: str, cand: dict[str, dict]) -> tuple[str, str]:
    correct = [s for s in STYLES if cand[s]["outcome"] == "correct"]
    if correct:
        return pick("K", qid, correct), "correct"
    abst = [s for s in STYLES if cand[s]["outcome"] == "abstain"]
    if abst:
        return pick("K", qid, abst), "abstention"
    return pick("K", qid, STYLES), "random"


def table(sets: dict[str, list[dict]], boot: int) -> dict:
    """Composition of every selected set with question-bootstrap intervals, and paired differences of rules."""
    n = len(next(iter(sets.values())))
    cols = [("outcome", o) for o in OUTCOMES] + [("style", s) for s in STYLES]
    rules = list(sets)
    mat = np.array([[float(sets[r][i][c[0]] == c[1]) for r in rules for c in cols] for i in range(n)])
    draws = boot_means(mat, boot)                       # the same resampled questions for every rule
    col = {(r, c): j for j, (r, c) in enumerate((r, c) for r in rules for c in cols)}
    out: dict = {"n_questions": n, "bootstrap": boot, "rules": {}, "differences": {}}
    for r in rules:
        out["rules"][r] = {}
        for c in cols:
            j = col[(r, c)]
            lo, hi = interval(draws[:, j])
            out["rules"][r][f"{c[0]}:{c[1]}"] = {"share": float(mat[:, j].mean()), "count": int(mat[:, j].sum()),
                                                 "lo": lo, "hi": hi}
    for a, b in [("J", "K"), ("F", "K"), ("J", "F"), ("J", "R"), ("K", "R")]:
        out["differences"][f"{a}-{b}"] = {}
        for c in cols:
            d = draws[:, col[(a, c)]] - draws[:, col[(b, c)]]
            lo, hi = interval(d)
            out["differences"][f"{a}-{b}"][f"{c[0]}:{c[1]}"] = {
                "diff": float(mat[:, col[(a, c)]].mean() - mat[:, col[(b, c)]].mean()), "lo": lo, "hi": hi,
                "boot_share_le_0": float((d <= 0).mean()), "boot_share_ge_0": float((d >= 0).mean())}
    return out


def markdown(t: dict, extra: dict) -> str:
    def cell(x: dict) -> str:
        return f"{x['share']:.1%} ({x['lo']:.1%} to {x['hi']:.1%})"

    def dcell(x: dict) -> str:
        return f"{x['diff'] * 100:+.1f} pp ({x['lo'] * 100:+.1f} to {x['hi'] * 100:+.1f})"

    names = {"J": "J, judge, default instruction", "F": "F, judge, accuracy instruction",
             "K": "K, by the key", "R": "R, random"}
    lines = [f"Composition of the selected training sets, {t['n_questions']} questions each. "
             f"Intervals are 95% percentile bootstraps over questions ({t['bootstrap']} resamples).", "",
             "| rule | abstentions | correct | wrong | unparsed | assert style | hedge style | abstain style |",
             "|---|---|---|---|---|---|---|---|"]
    for r, row in t["rules"].items():
        lines.append(f"| {names[r]} | " + " | ".join(
            cell(row[k]) for k in [f"outcome:{o}" for o in OUTCOMES] + [f"style:{s}" for s in STYLES]) + " |")
    lines += ["", "Paired differences between rules (same resampled questions).", "",
              "| difference | abstentions | correct | wrong |", "|---|---|---|---|"]
    for k, row in t["differences"].items():
        lines.append(f"| {k} | " + " | ".join(dcell(row[f"outcome:{o}"]) for o in ["abstain", "correct", "wrong"]) + " |")
    jk = t["differences"].get("J-K")
    if jk:
        a, w = jk["outcome:abstain"], jk["outcome:wrong"]
        ok = a["diff"] < 0 and w["diff"] > 0
        lines += ["", f"P5b (J has a lower share of abstentions and a higher share of wrong answers than K): "
                      f"{'holds' if ok else 'does not hold'}. Abstentions {dcell(a)}, bootstrap share of "
                      f"resamples with a difference at or above zero {a['boot_share_ge_0']:.4f}. Wrong answers "
                      f"{dcell(w)}, bootstrap share at or below zero {w['boot_share_le_0']:.4f}."]
    lines += ["", "Judge duels behind J and F (Claude Haiku 5.5, three per question).", "",
              "| rule | duels | unparsed verdicts | picks the first position | questions with a tie for most wins | "
              "assert beats abstain style | hedge beats abstain style | assert beats hedge |", "|---|---|---|---|---|---|---|---|"]
    for r, e in extra.items():
        lines.append(f"| {r} | {e['duels']} | {e['unparsed']} | {e['first_position']:.1%} | {e['ties']} | "
                     f"{e['pair_first_wins']['assert-abstain']:.1%} | {e['pair_first_wins']['hedge-abstain']:.1%} | "
                     f"{e['pair_first_wins']['assert-hedge']:.1%} |")
    lines += ["", "Pair rates are over all pool questions, whatever the abstain-style response says "
                  "(it abstains on a minority of them). The rates on abstentions only are in natural_duels.md."]
    return "\n".join(lines) + "\n"


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--conc", type=int, default=6)
    ap.add_argument("--boot", type=int, default=B)
    a = ap.parse_args()
    items = load_items(POOL_ITEMS)[:a.limit or None]
    pool: dict[str, dict[str, dict]] = {}
    for r in read_jsonl(OUT / "pool.jsonl"):
        pool.setdefault(r["id"], {})[r["style"]] = r
    assert all(set(pool.get(it["id"], {})) == set(STYLES) for it in items), "pool.jsonl is incomplete"

    cl = Client("select", a.conc)
    verdict: dict[tuple[str, str, tuple[str, str]], str | None] = {}    # (rule, qid, pair) -> winning style
    stats = {r: {"duels": 0, "unparsed": 0, "first": 0, "parsed": 0, "pair": Counter(), "pair_n": Counter()}
             for r in RULE_VARIANT}
    failed = []

    async def duel(rule: str, it: dict, pair: tuple[str, str]) -> None:
        first, second = (pair[1], pair[0]) if flipped(it["id"], pair) else pair
        user = natural_duel_prompt(it["qtext"], pool[it["id"]][first]["text"].strip(),
                                   pool[it["id"]][second]["text"].strip())
        rec = await cl.ask(JUDGE, JUDGE_SYSTEM[RULE_VARIANT[rule]], user, 16,
                           {"kind": "select", "rule": rule, "variant": RULE_VARIANT[rule], "item": it["id"],
                            "pair": "-".join(pair), "first": first, "second": second})
        if rec is None:
            failed.append((rule, it["id"], pair))
            return
        ch = parse_letter(rec["text"], "AB")
        st = stats[rule]
        st["duels"] += 1
        if ch is None:
            st["unparsed"] += 1
            verdict[(rule, it["id"], pair)] = None
            return
        st["parsed"] += 1
        st["first"] += ch == "A"
        win = first if ch == "A" else second
        verdict[(rule, it["id"], pair)] = win
        st["pair"]["-".join(pair)] += win == pair[0]
        st["pair_n"]["-".join(pair)] += 1

    await asyncio.gather(*[duel(r, it, p) for it in items for p in PAIRS for r in RULE_VARIANT])
    await cl.close()
    if failed:
        raise SystemExit(f"{len(failed)} judge calls failed, rerun to fill them in: {failed[:5]}")

    sets: dict[str, list[dict]] = {r: [] for r in ["J", "F", "K", "R"]}
    extra = {}
    for rule in RULE_VARIANT:
        ties = 0
        for it in items:
            wins = Counter({s: 0 for s in STYLES})
            for p in PAIRS:
                w = verdict[(rule, it["id"], p)]
                if w:
                    wins[w] += 1
            top = [s for s in STYLES if wins[s] == max(wins.values())]
            ties += len(top) > 1
            s = pick(rule, it["id"], top)
            sets[rule].append({"how": {"wins": dict(wins), "tie": len(top) > 1}, "style": s, "id": it["id"]})
        st = stats[rule]
        extra[rule] = {"duels": st["duels"], "unparsed": st["unparsed"], "ties": ties,
                       "first_position": st["first"] / max(1, st["parsed"]),
                       "pair_first_wins": {k: st["pair"][k] / max(1, st["pair_n"][k]) for k in
                                           ["-".join(p) for p in PAIRS]}}
    for it in items:
        s, why = select_by_key(it["id"], pool[it["id"]])
        sets["K"].append({"how": {"by": why}, "style": s, "id": it["id"]})
        sets["R"].append({"how": {"by": "random"}, "style": pick("R", it["id"], STYLES), "id": it["id"]})

    qtext = {it["id"]: it["qtext"] for it in items}
    for rule, rows in sets.items():
        for row in rows:
            c = pool[row["id"]][row["style"]]
            row.update({"rule": rule, "prompt": qtext[row["id"]], "completion": c["text"].strip(),
                        "parsed": c["parsed"], "outcome": c["outcome"], "key": c["key"]})
        suffix = "" if not a.limit else f".first{a.limit}"
        (OUT / f"train_{rule}{suffix}.jsonl").write_text("".join(json.dumps(
            {k: row[k] for k in ["id", "rule", "style", "prompt", "completion", "parsed", "outcome", "key", "how"]})
            + "\n" for row in rows))

    t = table(sets, a.boot)
    t["judge"] = {"model": JUDGE, "duel_stats": extra, "select_step_spend_usd": round(cl.spent, 4)}
    suffix = "" if not a.limit else f".first{a.limit}"
    (OUT / f"selection_table{suffix}.json").write_text(json.dumps(t, indent=1))
    md = markdown(t, extra)
    (OUT / f"selection_table{suffix}.md").write_text(md)
    print(md)


if __name__ == "__main__":
    asyncio.run(main())
