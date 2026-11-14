"""Tables for the duel runs (src/duels.py).

For every judge, prompt variant and pair the score of an item is the share of its two orders won by
the first-named response of the pair (0, 0.5 or 1). Rates are means of item scores, intervals are
item bootstraps. Groups: all items, items the judge answers correctly itself ("knows"), the rest.

Derived numbers per judge:
  a = rate(CC beats IDK), b = rate(CW beats IDK)
  break-even accuracy p* = (0.5 - b) / (a - b): the accuracy above which answering beats abstaining
  under this judge. p* <= 0 means a guess beats "I don't know" even if it is always wrong.

    python src/analyze_duels.py --runs results/study1 --items data/items/*_confirm.jsonl --out results/study1/summary
"""
from __future__ import annotations

import argparse
import json
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = 10000


def parse_letter(text: str, allowed: str, cot: bool = False) -> str | None:
    t = text.strip().upper()
    if cot:
        m = re.findall(rf"VERDICT\W*([{allowed}])\b", t)
        return m[-1] if m else None
    m = re.search(rf"\b([{allowed}])\b", t)
    return m.group(1) if m else None


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def boot(ids: list[str], stat, rng: random.Random, n: int = B) -> tuple[float, float, list[float]]:
    """Item bootstrap of stat(list of ids). Returns the 2.5 and 97.5 percentiles and the draws."""
    if not ids:
        return float("nan"), float("nan"), []
    draws = []
    for _ in range(n):
        s = stat([ids[rng.randrange(len(ids))] for _ in ids])
        if s == s:
            draws.append(s)
    draws.sort()
    if not draws:
        return float("nan"), float("nan"), []
    return draws[int(0.025 * len(draws))], draws[min(len(draws) - 1, int(0.975 * len(draws)))], draws


def load(runs: list[str], item_files: list[str]):
    items = {}
    for f in item_files:
        for ln in Path(f).read_text().splitlines():
            if ln.strip():
                it = json.loads(ln)
                items[it["id"]] = it
    own, duel = {}, defaultdict(dict)          # duel[(judge, variant, pair)][item] = [outcomes]
    first_pick = defaultdict(lambda: [0, 0])   # (judge, variant) -> [picked A, parsed]
    unparsed = defaultdict(int)
    for run in runs:
        p = ROOT / run / "calls.jsonl"
        for ln in p.read_text().splitlines():
            if not ln.strip():
                continue
            d = json.loads(ln)
            if d["item"] not in items:
                continue
            if d["kind"] == "knows":
                own[(d["judge"], d["item"])] = parse_letter(d["text"], "ABCD")
                continue
            ch = parse_letter(d["text"], "AB", cot=d["variant"] == "cot")
            key = (d["judge"], d["variant"], d["pair"])
            if ch is None:
                unparsed[key] += 1
                continue
            winner = d["first"] if ch == "A" else d["second"]
            duel[key].setdefault(d["item"], []).append(1.0 if winner == d["pair"].split("-")[0] else 0.0)
            fp = first_pick[(d["judge"], d["variant"])]
            fp[0] += ch == "A"
            fp[1] += 1
    return items, own, duel, first_pick, unparsed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--items", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--boot", type=int, default=B)
    a = ap.parse_args()
    items, own, duel, first_pick, unparsed = load(a.runs, a.items)
    rng = random.Random(20261115)
    judges = sorted({k[0] for k in duel})
    variants = sorted({k[1] for k in duel}, key=lambda v: (v != "default", v))
    pairs = sorted({k[2] for k in duel})
    domains = sorted({it["domain"] for it in items.values()})
    out: dict = {"judges": {}, "n_items": len(items)}
    lines = [f"items {len(items)} ({', '.join(domains)}), bootstrap draws {a.boot}", ""]

    for j in judges:
        ids_all = [i for i in items if (j, i) in own]
        know = {i: own[(j, i)] == items[i]["answer"] for i in ids_all}
        acc = mean([know[i] for i in ids_all])
        jr: dict = {"own_accuracy": acc, "n_knows_items": len(ids_all), "variants": {}}
        lines += [f"## {j}: own closed-book accuracy {acc:.0%} on {len(ids_all)} items", ""]
        for v in variants:
            fp = first_pick.get((j, v))
            if not fp or not fp[1]:
                continue
            vr: dict = {"picks_first_position": fp[0] / fp[1], "groups": {}}
            lines += [f"### prompt variant {v} (picks the first position in {fp[0] / fp[1]:.0%} of duels)", "",
                      "| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |",
                      "|---|---|---|---|---|---|"]
            groups = [("all", lambda i: True), ("judge knows", lambda i: know.get(i, False)),
                      ("judge does not know", lambda i: i in know and not know[i])]
            groups += [(f"domain {d}", lambda i, d=d: items[i]["domain"] == d) for d in domains]
            groups += [(f"domain {d}, judge knows", lambda i, d=d: items[i]["domain"] == d and know.get(i, False))
                       for d in domains]
            for gname, gf in groups:
                gr: dict = {}
                for p in pairs:
                    sc = duel.get((j, v, p), {})
                    ids = [i for i in sc if gf(i)]
                    if not ids:
                        continue
                    score = {i: mean(sc[i]) for i in ids}
                    m = mean([score[i] for i in ids])
                    lo, hi, draws = boot(ids, lambda s: mean([score[i] for i in s]), rng, a.boot)
                    p_le_half = mean([d <= 0.5 for d in draws]) if draws else float("nan")
                    gr[p] = {"rate": m, "lo": lo, "hi": hi, "n": len(ids), "p_boot_le_half": p_le_half}
                    if not gname.startswith("domain") or p in ("CW-IDK", "CC-IDK", "CW-HC"):
                        lines.append(f"| {p} | {gname} | {m:.0%} | {lo:.0%} to {hi:.0%} | {len(ids)} | "
                                     f"{unparsed.get((j, v, p), 0)} |")
                # break-even accuracy from the two abstention pairs, bootstrapped jointly over items
                sa, sb = duel.get((j, v, "CC-IDK"), {}), duel.get((j, v, "CW-IDK"), {})
                ids = [i for i in sa if i in sb and gf(i)]
                if ids:
                    def pstar(s):
                        aa, bb = mean([mean(sa[i]) for i in s]), mean([mean(sb[i]) for i in s])
                        return (0.5 - bb) / (aa - bb) if aa - bb > 0.02 else float("nan")
                    aa, bb = mean([mean(sa[i]) for i in ids]), mean([mean(sb[i]) for i in ids])
                    lo, hi, draws = boot(ids, pstar, rng, a.boot)
                    gr["derived"] = {"a": aa, "b": bb, "v_eff": aa - bb, "p_star": pstar(ids), "p_star_lo": lo,
                                     "p_star_hi": hi, "n": len(ids), "boot_defined": len(draws) / a.boot}
                    sh, st = duel.get((j, v, "CW-HC"), {}), duel.get((j, v, "CW-HW"), {})
                    ids2 = [i for i in ids if i in sh and i in st]
                    if ids2:
                        tone = mean([mean(st[i]) for i in ids2])
                        a2, b2 = mean([mean(sa[i]) for i in ids2]), mean([mean(sb[i]) for i in ids2])
                        gr["derived"].update({"tone": tone, "pred_CW_HC": (1 - (a2 - b2)) * tone,
                                              "obs_CW_HC": mean([mean(sh[i]) for i in ids2]), "n_pred": len(ids2)})
                vr["groups"][gname] = gr
            lines += ["", "| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | "
                          "tone, CW beats HW | CW beats HC predicted | observed |", "|---|---|---|---|---|---|---|---|---|"]
            for gname, gr in vr["groups"].items():
                d = gr.get("derived")
                if not d:
                    continue
                ps = "undefined" if d["p_star"] != d["p_star"] else f"{d['p_star']:+.2f}"
                extra = (f"{d['tone']:.0%} | {d['pred_CW_HC']:.0%} | {d['obs_CW_HC']:.0%}" if "tone" in d else "- | - | -")
                lines.append(f"| {gname} | {d['a']:.0%} | {d['b']:.0%} | {d['a'] - d['b']:+.2f} | {ps} | "
                             f"{d['p_star_lo']:+.2f} to {d['p_star_hi']:+.2f} | {extra} |")
            lines.append("")
            jr["variants"][v] = vr
        out["judges"][j] = jr
    o = ROOT / a.out
    o.parent.mkdir(parents=True, exist_ok=True)
    o.with_suffix(".md").write_text("\n".join(lines))
    o.with_suffix(".json").write_text(json.dumps(out, indent=1))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
