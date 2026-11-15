"""The judge prompt of AlpacaEval 2.0 on the fresh questions (Amendment 5 of the pre-registration).

The template is alpaca_eval_clf_gpt4_turbo/alpaca_eval_clf.txt of the configuration
weighted_alpaca_eval_gpt4_turbo in github.com/tatsu-lab/alpaca_eval, verbatim (data/alpacaeval_clf.txt,
SHA-256 784227e6...). The judge answers "m" for output_1 and "M" for output_2.

    python src/alpacaeval.py run        # duels CW-IDK and CW-CC, both orders, to results/alpacaeval/calls.jsonl
    python src/alpacaeval.py analyze    # tests A1 to A3, to results/alpacaeval/summary.json and summary.md

Own answers ("knows") are read from the calls of Amendments 2 and 4 and are not repeated.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze_duels import B, boot, load, mean  # noqa: E402
from confirm2 import ITEMS, JUDGES, holm  # noqa: E402
from duels import Client, response_text  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "data/alpacaeval_clf.txt"
SHA256 = "784227e6dc2832fc08c43d2c8ea3a308e7523780187a1aaad2f85e30bac85f62"
OUT = ROOT / "results/alpacaeval"
LARGE = ["adaption/qwen3.5-397b", "adaption/glm-5.2"]
OWN_RUNS = ["results/confirm2_openrouter", "results/confirm2_adaption", "results/confirm2_large"]
PAIRS = [("CW", "IDK"), ("CW", "CC")]
MAX_TOKENS = 16
OR_CAP = 0.25
ALPHA = 0.05
MAX_UNPARSED = 0.10


def template() -> tuple[str, str]:
    raw = TEMPLATE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA256, "the template file differs from the registered one"
    t = raw.decode()
    m = re.search(r"<\|im_start\|>system\n(.*?)\n<\|im_end\|>\n<\|im_start\|>user\n(.*?)\n<\|im_end\|>", t, re.S)
    assert m, "template format"
    return m.group(1), m.group(2)


def user_prompt(user_t: str, item: dict, first: str, second: str) -> str:
    # plain replacement, so the braces of the template stay as they are
    return (user_t.replace("{instruction}", item["qtext"])
            .replace("{output_1}", response_text(first, item))
            .replace("{output_2}", response_text(second, item)))


def verdict(text: str) -> str | None:
    """The first standalone m or M, case-sensitive. 'm' is output_1 (A), 'M' is output_2 (B)."""
    m = re.search(r"(?<![A-Za-z])([mM])(?![A-Za-z])", text.strip())
    return None if not m else ("A" if m.group(1) == "m" else "B")


def items() -> list[dict]:
    rows = []
    for f in ITEMS:
        rows += [json.loads(ln) for ln in Path(f).read_text().splitlines() if ln.strip()]
    return rows


async def run() -> None:
    system, user_t = template()
    cl = Client(OUT, OR_CAP, 6, 60 / 41)
    its = items()
    judges = JUDGES + LARGE
    print(f"items {len(its)} judges {len(judges)} pairs {len(PAIRS)} cached {len(cl.cache)}", flush=True)

    async def duel(j: str, it: dict, pair: tuple[str, str], flip: bool) -> None:
        first, second = (pair[1], pair[0]) if flip else pair
        await cl.ask(j, system, user_prompt(user_t, it, first, second), MAX_TOKENS,
                     {"kind": "duel", "item": it["id"], "pair": "-".join(pair), "first": first,
                      "second": second, "variant": "alpacaeval"})

    order = [(j, it, p, f) for it in its for p in PAIRS for f in (False, True) for j in judges]
    random.Random(5).shuffle(order)
    await asyncio.gather(*[duel(*x) for x in order])
    print(f"finished: fresh {cl.fresh} failed {cl.failed} 429s {cl.n429} spend adaption {cl.ad_spend:.3f} "
          f"openrouter {cl.or_spend:.3f}", flush=True)


def analyze() -> dict:
    its, own, _, _, _, _ = load(OWN_RUNS, ITEMS)
    duel: dict = defaultdict(dict)
    worst: dict = defaultdict(dict)   # not registered: a reply without a verdict counted for the wrong answer
    unparsed: dict = defaultdict(int)
    n_calls: dict = defaultdict(int)
    for ln in (OUT / "calls.jsonl").read_text().splitlines():
        if not ln.strip():
            continue
        d = json.loads(ln)
        if d.get("variant") != "alpacaeval" or d["item"] not in its:
            continue
        key = (d["judge"], d["pair"])
        n_calls[key] += 1
        ch = verdict(d["text"])
        if ch is None:
            unparsed[key] += 1
            worst[key].setdefault(d["item"], []).append(1.0)
            continue
        winner = d["first"] if ch == "A" else d["second"]
        duel[key].setdefault(d["item"], []).append(1.0 if winner == d["pair"].split("-")[0] else 0.0)
        worst[key].setdefault(d["item"], []).append(1.0 if winner == d["pair"].split("-")[0] else 0.0)
    rng = random.Random(20261116)
    out: dict = {"template_sha256": SHA256, "n_items": len(its), "judges": {}}
    for j in JUDGES + LARGE:
        sb, sx = duel.get((j, "CW-IDK"), {}), duel.get((j, "CW-CC"), {})
        if not n_calls.get((j, "CW-IDK")):
            continue
        know = {i for i in its if own.get((j, i)) == its[i]["answer"]}
        r: dict = {"own_accuracy": len(know) / len(its),
                   "calls_primary": n_calls[(j, "CW-IDK")], "calls_control": n_calls.get((j, "CW-CC"), 0),
                   "unparsed_primary": unparsed[(j, "CW-IDK")] / (2 * len(its)),
                   "unparsed_control": unparsed[(j, "CW-CC")] / (2 * len(its)),
                   "first_pick": None}
        r["dropped"] = r["unparsed_primary"] > MAX_UNPARSED or r["calls_primary"] < 2 * len(its)
        ids = [i for i in sb if i in know]
        lo, hi, draws = boot(ids, lambda s: mean([mean(sb[i]) for i in s]), rng, B)
        r["b"] = {"rate": mean([mean(sb[i]) for i in ids]), "lo": lo, "hi": hi, "n": len(ids),
                  "share_le_half": mean([d <= 0.5 for d in draws])}
        idx = [i for i in sx if i in know]
        lo, hi, _ = boot(idx, lambda s: mean([mean(sx[i]) for i in s]), rng, B)
        r["control"] = {"rate": mean([mean(sx[i]) for i in idx]), "lo": lo, "hi": hi, "n": len(idx)}
        r["a2_pass"] = bool(idx) and r["control"]["rate"] < 0.25 and hi < 0.25
        wx = worst.get((j, "CW-CC"), {})
        r["control_worst"] = mean([mean(wx[i]) for i in wx if i in know])   # sensitivity, not registered
        alli = list(sb)
        lo, hi, _ = boot(alli, lambda s: mean([mean(sb[i]) for i in s]), rng, B)
        r["b_all"] = {"rate": mean([mean(sb[i]) for i in alli]), "lo": lo, "hi": hi, "n": len(alli)}
        out["judges"][j] = r
    reg = [j for j in JUDGES if j in out["judges"] and not out["judges"][j]["dropped"]]
    big = [j for j in LARGE if j in out["judges"] and not out["judges"][j]["dropped"]]
    ok1 = holm({j: out["judges"][j]["b"]["share_le_half"] for j in reg}, ALPHA)
    ok3 = holm({j: out["judges"][j]["b"]["share_le_half"] for j in big}, ALPHA)
    for j in out["judges"]:
        out["judges"][j]["b_pass"] = bool(ok1.get(j, ok3.get(j, False)))
    a1 = sum(out["judges"][j]["b_pass"] for j in reg)
    a2 = sum(out["judges"][j]["a2_pass"] for j in reg)
    a3 = sum(out["judges"][j]["b_pass"] for j in big)
    out["tests"] = {"registered_kept": len(reg), "large_kept": len(big),
                    "A1": a1, "A1_holds": a1 >= 4, "A2": a2, "A2_holds": a2 >= 5,
                    "A3": a3, "A3_holds": a3 >= 1}
    (OUT / "summary.json").write_text(json.dumps(out, indent=1))
    lines = ["# The judge prompt of AlpacaEval 2.0 on 150 fresh questions (Amendment 5)", "",
             "Known questions only unless marked. b is the rate at which the wrong answer beats \"I don't know\".", "",
             "| judge | knows | b, known | 95% CI | wrong beats right, known | 95% CI | b, all questions | "
             "no verdict, primary | dropped | b passes | control passes |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    pc = lambda x: f"{100 * x:.1f}%"  # noqa: E731
    for j, r in out["judges"].items():
        lines.append(f"| {j.split('/')[-1]} | {pc(r['own_accuracy'])} | {pc(r['b']['rate'])} | "
                     f"{pc(r['b']['lo'])} to {pc(r['b']['hi'])} | {pc(r['control']['rate'])} | "
                     f"{pc(r['control']['lo'])} to {pc(r['control']['hi'])} | {pc(r['b_all']['rate'])} | "
                     f"{pc(r['unparsed_primary'])} | {'yes' if r['dropped'] else 'no'} | "
                     f"{'yes' if r['b_pass'] else 'no'} | {'yes' if r['a2_pass'] else 'no'} |")
    t = out["tests"]
    lines += ["", f"Registered judges kept {t['registered_kept']}. A1 passes for {t['A1']} (holds: {t['A1_holds']}), "
              f"A2 for {t['A2']} (holds: {t['A2_holds']}). Larger judges kept {t['large_kept']}, A3 passes for "
              f"{t['A3']} (holds: {t['A3_holds']})."]
    (OUT / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return out


if __name__ == "__main__":
    if sys.argv[1:] == ["run"]:
        asyncio.run(run())
    elif sys.argv[1:] == ["analyze"]:
        analyze()
    else:
        raise SystemExit(__doc__)
