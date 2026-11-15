"""Reward models, Amendment 4, part B: rates, intervals and the tests R1 and R2.

A model prefers response X to response Y on a question if X gets the higher score, and an exact tie
counts as half. A model "separates" a question if it scores CC above CW. Rates are means over
questions with an item bootstrap (10,000 resamples). R1 (multiple-choice) and R2 (free-form) use b on
separated questions, the bootstrap share at or below 0.5 as the p-value, Holm over the three models at
0.05, and hold if at least two of the three models pass.

    python src/rm_analyze.py     # results/reward_models/scores.jsonl -> summary.json, summary.md
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze_duels import B, boot, mean  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "results/reward_models"
MODELS = ["Skywork/Skywork-Reward-V2-Llama-3.1-8B", "Skywork/Skywork-Reward-V2-Qwen3-8B",
          "allenai/Llama-3.1-Tulu-3-8B-RM"]
SETS = {"mcq": "150 fresh multiple-choice questions", "free": "100 free-form questions"}
TESTS = {"mcq": "R1", "free": "R2"}
ALPHA = 0.05
PAIRS = {"a": ("CC", "IDK"), "b": ("CW", "IDK"), "control": ("CW", "CC"), "b_full": ("CW", "IDK2"),
         "a_full": ("CC", "IDK2")}


def win(x: float, y: float) -> float:
    return 1.0 if x > y else 0.5 if x == y else 0.0


def holm(ps: dict[str, float], alpha: float) -> dict[str, bool]:
    order = sorted(ps, key=lambda k: ps[k])
    ok, alive = {}, True
    for rank, k in enumerate(order):
        alive = alive and ps[k] <= alpha / (len(order) - rank)
        ok[k] = alive
    return ok


def main() -> None:
    sc: dict = {}
    for ln in (RES / "scores.jsonl").read_text().splitlines():
        if ln.strip():
            d = json.loads(ln)
            sc.setdefault(d["model"], {}).setdefault(d["set"], {}).setdefault(d["item"], {})[d["resp"]] = d["score"]
    models = [m for m in MODELS if m in sc] + [m for m in sc if m not in MODELS]
    rng = random.Random(20261118)
    out: dict = {"models": {}, "bootstrap": B, "seed": 20261118}

    def cell(vals: dict[str, float], ids: list[str]) -> dict:
        lo, hi, draws = boot(ids, lambda s: mean([vals[i] for i in s]), rng, B)
        return {"rate": mean([vals[i] for i in ids]), "lo": lo, "hi": hi, "n": len(ids),
                "share_le_half": mean([x <= 0.5 for x in draws])}

    for m in models:
        out["models"][m] = {}
        for s in SETS:
            items = sc[m].get(s, {})
            ids = sorted(i for i, r in items.items() if all(k in r for k in ("CC", "CW", "IDK", "IDK2")))
            if not ids:
                continue
            r: dict = {"n_items": len(ids)}
            for name, (x, y) in PAIRS.items():
                vals = {i: win(items[i][x], items[i][y]) for i in ids}
                r[name] = cell(vals, ids)
                r[name]["ties"] = sum(v == 0.5 for v in vals.values())
            sep = {i: float(items[i]["CC"] > items[i]["CW"]) for i in ids}
            r["separated"] = cell(sep, ids)
            sids = [i for i in ids if sep[i]]
            for name in ("b", "a", "b_full", "a_full"):
                x, y = PAIRS[name]
                vals = {i: win(items[i][x], items[i][y]) for i in sids}
                r[name + "_separated"] = cell(vals, sids)
            for ids_, tag in ((ids, "all"), (sids, "separated")):
                diff = {i: items[i]["CW"] - items[i]["IDK"] for i in ids_}
                lo, hi, _ = boot(ids_, lambda q: mean([diff[i] for i in q]), rng, B)
                r[f"mean_cw_minus_idk_{tag}"] = {"mean": mean(list(diff.values())), "lo": lo, "hi": hi, "n": len(ids_)}
            allv = [items[i][k] for i in ids for k in ("CC", "CW", "IDK", "IDK2")]
            r["score_range"] = {"min": min(allv), "max": max(allv),
                                **{f"mean_{k}": mean([items[i][k] for i in ids]) for k in ("CC", "CW", "IDK", "IDK2")}}
            out["models"][m][s] = r

    tests: dict = {}
    for s, label in TESTS.items():
        ps = {m: out["models"][m][s]["b_separated"]["share_le_half"] for m in models if s in out["models"][m]}
        ok = holm(ps, ALPHA)
        for m in ps:
            out["models"][m][s]["test_pass"] = bool(ok[m])
        tests[label] = {"set": s, "passes": sum(ok.values()), "of": len(ps), "holds": sum(ok.values()) >= 2,
                        "p": ps}
    out["tests"] = tests
    (RES / "summary.json").write_text(json.dumps(out, indent=1))

    def f(c: dict) -> str:
        return f"{c['rate']:.0%} ({c['lo']:.0%} to {c['hi']:.0%})"
    lines = ["# Reward models (Amendment 4, part B)", "",
             "Each response scored alone. X beats Y on a question if X gets the higher score, an exact tie counts "
             "half. The model separates a question if it scores CC above CW. Rates are over all questions of the "
             "set except where marked separated. Intervals are 95% item bootstraps with 10,000 resamples.", ""]
    for s, title in SETS.items():
        lines += [f"## {title}", "",
                  "| model | a, CC beats IDK | b, CW beats IDK | control, CW beats CC | CW beats IDK2 | CC beats IDK2 "
                  "| separated share | b on separated (n) | bootstrap share at or below 0.5 | "
                  f"{TESTS[s]} after Holm | mean score CW minus IDK |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
        for m in models:
            r = out["models"][m].get(s)
            if not r:
                continue
            d = r["mean_cw_minus_idk_all"]
            lines.append(f"| {m.split('/')[-1]} | {f(r['a'])} | {f(r['b'])} | {f(r['control'])} | {f(r['b_full'])} | "
                         f"{f(r['a_full'])} | {f(r['separated'])} | {f(r['b_separated'])} ({r['b_separated']['n']}) | "
                         f"{r['b_separated']['share_le_half']:.4f} | {'pass' if r['test_pass'] else 'fail'} | "
                         f"{d['mean']:+.2f} ({d['lo']:+.2f} to {d['hi']:+.2f}) |")
        t = tests[TESTS[s]]
        lines += ["", f"{TESTS[s]}: passes for {t['passes']} of {t['of']} models, "
                      f"{'holds' if t['holds'] else 'does not hold'} (needs at least two).", ""]
    lines += ["## Score scales", "", "| model | set | min | max | mean CC | mean CW | mean IDK | mean IDK2 | ties in b |",
              "|---|---|---|---|---|---|---|---|---|"]
    for m in models:
        for s in SETS:
            r = out["models"][m].get(s)
            if r:
                g = r["score_range"]
                lines.append(f"| {m.split('/')[-1]} | {s} | {g['min']:.2f} | {g['max']:.2f} | {g['mean_CC']:.2f} | "
                             f"{g['mean_CW']:.2f} | {g['mean_IDK']:.2f} | {g['mean_IDK2']:.2f} | {r['b']['ties']} |")
    (RES / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
