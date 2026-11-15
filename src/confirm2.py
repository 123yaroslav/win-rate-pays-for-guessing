"""Registered confirmation on fresh questions (Amendment 2 of the pre-registration).

Tests C1 to C4 on the 150 fresh questions, from the calls in results/confirm2_openrouter and
results/confirm2_adaption. "Known" questions are those the judge answers correctly itself.

    python src/confirm2.py
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze_duels import B, boot, load, mean  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RUNS = ["results/confirm2_openrouter", "results/confirm2_adaption"]
ITEMS = [str(ROOT / f"data/items/{d}_fresh.jsonl") for d in ("medqa", "law", "geo")]
JUDGES = ["adaption/deepseek-v4-flash", "adaption/gemma-4-31b-it", "adaption/qwen3.8-27b",
          "openrouter/anthropic/claude-haiku-5.5", "openrouter/openai/gpt-5.6-luna",
          "openrouter/mistralai/mistral-small-2603"]
ALPHA = 0.05
MAX_UNPARSED = 0.10


def holm(ps: dict[str, float], alpha: float) -> dict[str, bool]:
    order = sorted(ps, key=lambda k: ps[k])
    ok, alive = {}, True
    for rank, k in enumerate(order):
        alive = alive and ps[k] <= alpha / (len(order) - rank)
        ok[k] = alive
    return ok


def main() -> None:
    runs = [r for r in RUNS if (ROOT / r / "calls.jsonl").exists()]
    items, own, duel, _, unparsed, flags = load(runs, ITEMS)
    rng = random.Random(20261116)
    out: dict = {"n_items": len(items), "judges": {}}
    for j in JUDGES:
        sb, sa, sx = (duel.get((j, "default", p), {}) for p in ("CW-IDK", "CC-IDK", "CW-CC"))
        if not sb:
            continue
        know = {i for i in items if own.get((j, i)) == items[i]["answer"]}
        r: dict = {"own_accuracy": len(know) / len(items),
                   "unparsed_primary": unparsed.get((j, "default", "CW-IDK"), 0) / (2 * len(items)),
                   "unparsed_control": unparsed.get((j, "default", "CW-CC"), 0) / (2 * len(items))}
        r["dropped"] = r["unparsed_primary"] > MAX_UNPARSED
        # C1: b on known questions
        ids = [i for i in sb if i in know]
        lo, hi, draws = boot(ids, lambda s: mean([mean(sb[i]) for i in s]), rng, B)
        r["b"] = {"rate": mean([mean(sb[i]) for i in ids]), "lo": lo, "hi": hi, "n": len(ids),
                  "share_le_half": mean([d <= 0.5 for d in draws])}
        ida = [i for i in sa if i in know]
        lo, hi, _ = boot(ida, lambda s: mean([mean(sa[i]) for i in s]), rng, B)
        r["a"] = {"rate": mean([mean(sa[i]) for i in ida]), "lo": lo, "hi": hi, "n": len(ida)}
        # C2: the wrong answer against the right answer in the same words, known questions
        idx = [i for i in sx if i in know]
        lo, hi, _ = boot(idx, lambda s: mean([mean(sx[i]) for i in s]), rng, B)
        r["control"] = {"rate": mean([mean(sx[i]) for i in idx]), "lo": lo, "hi": hi, "n": len(idx)}
        r["c2_pass"] = bool(idx) and r["control"]["rate"] < 0.25 and hi < 0.25
        # C3: gap between the two rates on the same questions
        idd = [i for i in sb if i in sx and i in know]
        gap = lambda s: mean([mean(sb[i]) for i in s]) - mean([mean(sx[i]) for i in s])  # noqa: E731
        lo, hi, _ = boot(idd, gap, rng, B)
        r["gap"] = {"value": gap(idd), "lo": lo, "hi": hi, "n": len(idd)}
        r["c3_pass"] = bool(idd) and r["gap"]["value"] >= 0.30 and lo > 0
        # C4: verify-then-compare on all questions with a parsed reply to both checks and both duels
        idv = [i for i in sa if i in sb and flags.get((j, i, "CW")) and flags.get((j, i, "CC"))]
        if idv:
            ga = {i: 0.0 if flags[(j, i, "CC")] == "NO" else mean(sa[i]) for i in idv}
            gb = {i: 0.0 if flags[(j, i, "CW")] == "NO" else mean(sb[i]) for i in idv}
            lo, hi, draws = boot(idv, lambda s: mean([gb[i] for i in s]), rng, B)
            alo, ahi, _ = boot(idv, lambda s: mean([ga[i] for i in s]), rng, B)

            def pstar(s, ga=ga, gb=gb):
                aa, bb = mean([ga[i] for i in s]), mean([gb[i] for i in s])
                return (0.5 - bb) / (aa - bb) if aa - bb > 0.02 else float("nan")
            plo, phi, _ = boot(idv, pstar, rng, B)
            r["rule"] = {"n": len(idv), "a_before": mean([mean(sa[i]) for i in idv]),
                         "b_before": mean([mean(sb[i]) for i in idv]),
                         "a": mean(list(ga.values())), "a_lo": alo, "a_hi": ahi,
                         "b": mean(list(gb.values())), "b_lo": lo, "b_hi": hi,
                         "share_ge_half": mean([d >= 0.5 for d in draws]),
                         "p_star": pstar(idv), "p_star_lo": plo, "p_star_hi": phi,
                         "wrong_flagged": mean([flags[(j, i, "CW")] == "NO" for i in idv]),
                         "right_accepted": mean([flags[(j, i, "CC")] == "YES" for i in idv])}
            r["c4_b_pass"] = r["rule"]["b"] < 0.5 and r["rule"]["share_ge_half"] < ALPHA
            r["c4_a_pass"] = r["rule"]["a"] >= 0.80
        out["judges"][j] = r
    kept = [j for j in out["judges"] if not out["judges"][j]["dropped"]]
    ok = holm({j: out["judges"][j]["b"]["share_le_half"] for j in kept}, ALPHA)
    for j in out["judges"]:
        out["judges"][j]["c1_pass"] = bool(ok.get(j, False))
    out["tests"] = {
        "judges_kept": len(kept),
        "C1": sum(out["judges"][j]["c1_pass"] for j in kept),
        "C2": sum(out["judges"][j]["c2_pass"] for j in kept),
        "C3": sum(out["judges"][j]["c3_pass"] for j in kept),
        "C4_b": sum(out["judges"][j].get("c4_b_pass", False) for j in kept),
        "C4_a": sum(out["judges"][j].get("c4_a_pass", False) for j in kept),
    }
    t = out["tests"]
    out["tests"]["C1_holds"] = t["C1"] >= 5
    out["tests"]["C2_holds"] = t["C2"] >= 5
    out["tests"]["C3_holds"] = t["C3"] >= 5
    out["tests"]["C4_holds"] = t["C4_b"] >= 5
    lines = [f"# Confirmation on {len(items)} fresh questions (Amendment 2)", "",
             "| judge | knows | b, known | 95% CI | wrong beats right, known | 95% CI | gap | "
             "b with rule | a with rule | no verdict, primary pair | C1 | C2 | C3 | C4 |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    yn = lambda x: "yes" if x else "no"  # noqa: E731
    for j, r in out["judges"].items():
        ru = r.get("rule", {})
        lines.append(
            f"| {j.split('/')[-1]}{' (dropped)' if r['dropped'] else ''} | {r['own_accuracy']:.0%} | "
            f"{r['b']['rate']:.1%} | {r['b']['lo']:.1%} to {r['b']['hi']:.1%} | {r['control']['rate']:.1%} | "
            f"{r['control']['lo']:.1%} to {r['control']['hi']:.1%} | {r['gap']['value']:+.2f} | "
            + (f"{ru['b']:.1%} | {ru['a']:.1%}" if ru else "- | -")
            + f" | {r['unparsed_primary']:.1%} | {yn(r['c1_pass'])} | {yn(r['c2_pass'])} | {yn(r['c3_pass'])} | "
            f"{yn(r.get('c4_b_pass'))} |")
    lines += ["", f"Judges kept {t['judges_kept']}. C1 holds for {t['C1']}, C2 for {t['C2']}, C3 for {t['C3']}, "
                  f"C4 (b below 0.5 with the rule) for {t['C4_b']}, a with the rule at or above 0.80 for {t['C4_a']}."]
    od = ROOT / "results/confirm2"
    od.mkdir(parents=True, exist_ok=True)
    (od / "confirm.json").write_text(json.dumps(out, indent=1))
    (od / "confirm.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
