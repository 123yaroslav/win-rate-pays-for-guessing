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
ties: dict = {}


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


def load(runs: list[str], item_files: list[str], limit: int = 0):
    items = {}
    for f in item_files:
        rows = [json.loads(ln) for ln in Path(f).read_text().splitlines() if ln.strip()]
        for it in rows[:limit] if limit else rows:
            items[it["id"]] = it
    own, duel, flags = {}, defaultdict(dict), {}   # duel[(judge, variant, pair)][item] = [outcomes]
    first_pick = defaultdict(lambda: [0, 0])   # (judge, variant) -> [picked A, parsed]
    unparsed = defaultdict(int)
    global ties
    ties = defaultdict(int)
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
            if d["kind"] == "detect":
                m = re.search(r"\b(YES|NO)\b", d["text"].strip().upper())
                flags[(d["judge"], d["item"], d["resp"])] = m.group(1) if m else None
                continue
            key = (d["judge"], d["variant"], d["pair"])
            if d["variant"] == "mtbench":   # verdict in double brackets, [[C]] is a tie
                mm = re.findall(r"\[\[([ABC])\]\]", d["text"].upper())
                ch = mm[-1] if mm else None
            else:
                ch = parse_letter(d["text"], "AB", cot=d["variant"] == "cot")
            if ch is None:
                unparsed[key] += 1
                continue
            if ch == "C":
                duel[key].setdefault(d["item"], []).append(0.5)
                ties[key] += 1
                continue
            winner = d["first"] if ch == "A" else d["second"]
            duel[key].setdefault(d["item"], []).append(1.0 if winner == d["pair"].split("-")[0] else 0.0)
            fp = first_pick[(d["judge"], d["variant"])]
            fp[0] += ch == "A"
            fp[1] += 1
    return items, own, duel, first_pick, unparsed, flags


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--items", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--boot", type=int, default=B)
    ap.add_argument("--limit", type=int, default=0, help="use only the first N items of every file")
    a = ap.parse_args()
    items, own, duel, first_pick, unparsed, flags = load(a.runs, a.items, a.limit)
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
            if any(k[0] == j for k in flags):
                groups += [("judge tells the two answers apart", lambda i: flags.get((j, i, "CW")) == "NO"
                            and flags.get((j, i, "CC")) == "YES"),
                           ("judge flags the wrong answer as incorrect", lambda i: flags.get((j, i, "CW")) == "NO"),
                           ("judge knows and flags the wrong answer", lambda i: know.get(i, False)
                            and flags.get((j, i, "CW")) == "NO")]
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
                    p_ge_half = mean([d >= 0.5 for d in draws]) if draws else float("nan")
                    gr[p] = {"rate": m, "lo": lo, "hi": hi, "n": len(ids), "p_boot_le_half": p_le_half,
                             "p_boot_ge_half": p_ge_half}
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
            vr["unparsed"] = {p_: unparsed.get((j, v, p_), 0) for p_ in pairs}
            vr["ties"] = {p_: ties.get((j, v, p_), 0) for p_ in pairs}
            vr["parsed_items"] = {p_: len(duel.get((j, v, p_), {})) for p_ in pairs}
            jr["variants"][v] = vr
        out["judges"][j] = jr
    def holm(ps: dict[str, float], alpha: float) -> dict[str, bool]:
        order = sorted(ps, key=lambda k: ps[k])
        ok, alive = {}, True
        for rank, k in enumerate(order):
            alive = alive and ps[k] <= alpha / (len(order) - rank)
            ok[k] = alive
        return ok

    head = ["## Registered tests (default instruction)", ""]
    tests: dict = {}
    for gname, alpha, label in (("judge knows", 0.04, "H1"), ("all", 0.01, "H1F"),
                                ("judge flags the wrong answer as incorrect", 0.05, "S1g"),
                                ("judge tells the two answers apart", 0.05, "S1g2")):
        ps = {}
        for j in judges:
            g = out["judges"][j]["variants"].get("default", {}).get("groups", {}).get(gname, {}).get("CW-IDK")
            if g:
                ps[j] = g["p_boot_le_half"]
        if not ps:
            continue
        # the Holm family is the six registered judges; the stronger judge of S1f is tested on its own
        fam = {j: v for j, v in ps.items() if "gpt-5.6-terra" not in j}
        ok = holm(fam, alpha) if fam else {}
        for j in ps:
            if j not in ok:
                ok[j] = ps[j] <= alpha
        tests[label] = {"group": gname, "alpha": alpha, "p": ps, "holm_pass": ok, "n_pass": sum(ok.values()),
                        "n_judges": len(ps)}
        head += [f"{label}: b above 0.5 on group '{gname}', Holm at {alpha}. Passed by {sum(ok.values())} of {len(ps)} judges.", "",
                 "| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |", "|---|---|---|---|---|---|"]
        for j in judges:
            g = out["judges"][j]["variants"].get("default", {}).get("groups", {}).get(gname, {}).get("CW-IDK")
            if g:
                head.append(f"| {j} | {g['rate']:.1%} | {g['lo']:.1%} to {g['hi']:.1%} | {g['n']} | "
                            f"{g['p_boot_le_half']:.4f} | {'yes' if ok[j] else 'no'} |")
        head.append("")
    out["tests"] = tests

    if flags:
        head += ["## Detection (S1g)", "", "| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |",
                 "|---|---|---|---|"]
        det = {}
        for j in judges:
            cw = [flags[k] for k in flags if k[0] == j and k[2] == "CW"]
            cc = [flags[k] for k in flags if k[0] == j and k[2] == "CC"]
            if not cw:
                continue
            both = [i for (jj, i, r) in flags if jj == j and r == "CW" and (j, i, "CC") in flags]
            det[j] = {"cw_flagged": mean([x == "NO" for x in cw]), "cc_accepted": mean([x == "YES" for x in cc]),
                      "tells_apart": mean([flags[(j, i, "CW")] == "NO" and flags[(j, i, "CC")] == "YES" for i in both]),
                      "unparsed": sum(x is None for x in cw + cc), "n": len(cw)}
            head.append(f"| {j} | {det[j]['cw_flagged']:.1%} | {det[j]['cc_accepted']:.1%} | {det[j]['unparsed']} |")
        head.append("")
        out["detection"] = det

    # Exploratory: a verify-then-compare protocol composed from logged verdicts. An answer that the judge
    # itself calls incorrect loses to the abstention, otherwise the duel verdict stands.
    if flags:
        vtc = {}
        head += ["## Verify-then-compare, composed from logged verdicts (exploratory)", "",
                 "| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |",
                 "|---|---|---|---|---|---|---|"]
        for j in judges:
            sa, sb = duel.get((j, "default", "CC-IDK"), {}), duel.get((j, "default", "CW-IDK"), {})
            ids = [i for i in sa if i in sb and flags.get((j, i, "CW")) and flags.get((j, i, "CC"))]
            if not ids:
                continue
            ga = {i: 0.0 if flags[(j, i, "CC")] == "NO" else mean(sa[i]) for i in ids}
            gb = {i: 0.0 if flags[(j, i, "CW")] == "NO" else mean(sb[i]) for i in ids}

            def pstar2(sample, ga=ga, gb=gb):
                aa, bb = mean([ga[i] for i in sample]), mean([gb[i] for i in sample])
                return (0.5 - bb) / (aa - bb) if aa - bb > 0.02 else float("nan")
            lo, hi, _ = boot(ids, pstar2, rng, a.boot)
            vtc[j] = {"a": mean([mean(sa[i]) for i in ids]), "b": mean([mean(sb[i]) for i in ids]),
                      "a_check": mean(list(ga.values())), "b_check": mean(list(gb.values())),
                      "p_star_check": pstar2(ids), "lo": lo, "hi": hi, "n": len(ids)}
            v = vtc[j]
            head.append(f"| {j} | {v['a']:.1%} | {v['b']:.1%} | {v['a_check']:.1%} | {v['b_check']:.1%} | "
                        f"{v['p_star_check']:.2f} | {lo:.2f} to {hi:.2f} |")
        head.append("")
        out["verify_then_compare"] = vtc

    # Study 4 criterion: a variant repairs a judge if, on items the judge knows, b is below 0.5
    # (bootstrap share at or above 0.5 under 0.05) while a stays at or above 0.9.
    if len(variants) > 1:
        head += ["## Instruction variants (Study 4 criterion)", "",
                 "| judge | variant | a, knows | b, knows | share of resamples with b at or above 0.5 | repaired | "
                 "a, does not know | b, does not know |", "|---|---|---|---|---|---|---|---|"]
        rep = {}
        for j in judges:
            for v in variants:
                gs = out["judges"][j]["variants"].get(v, {}).get("groups", {})
                ak, bk = gs.get("judge knows", {}).get("CC-IDK"), gs.get("judge knows", {}).get("CW-IDK")
                au, bu = gs.get("judge does not know", {}).get("CC-IDK"), gs.get("judge does not know", {}).get("CW-IDK")
                if not ak or not bk:
                    continue
                ok = bk["p_boot_ge_half"] < 0.05 and ak["rate"] >= 0.9
                ok_u = bool(au and bu and bu["p_boot_ge_half"] < 0.05 and au["rate"] >= 0.9)
                rep[f"{j}|{v}"] = {"a_knows": ak["rate"], "b_knows": bk["rate"], "p_ge_half": bk["p_boot_ge_half"],
                                   "repaired": ok, "repaired_unknown": ok_u, "n_knows": bk["n"],
                                   "n_unknown": bu["n"] if bu else 0,
                                   "a_unknown": au["rate"] if au else None, "b_unknown": bu["rate"] if bu else None}
                head.append(f"| {j} | {v} | {ak['rate']:.0%} | {bk['rate']:.0%} | {bk['p_boot_ge_half']:.3f} | "
                            f"{'yes' if ok else 'no'} | {'-' if not au else format(au['rate'], '.0%')} | "
                            f"{'-' if not bu else format(bu['rate'], '.0%')} |")
        head.append("")
        out["repair"] = rep

    cells = []
    for j in judges:
        gs = out["judges"][j]["variants"].get("default", {}).get("groups", {})
        for d in domains:
            dd = gs.get(f"domain {d}", {}).get("derived", {})
            if "pred_CW_HC" in dd:
                cells.append((j, d, dd["pred_CW_HC"], dd["obs_CW_HC"]))
    if len(cells) >= 3:
        def ranks(xs):
            order = sorted(range(len(xs)), key=lambda i: xs[i])
            r = [0.0] * len(xs)
            i = 0
            while i < len(order):
                k = i
                while k + 1 < len(order) and xs[order[k + 1]] == xs[order[i]]:
                    k += 1
                for m in range(i, k + 1):
                    r[order[m]] = (i + k) / 2 + 1
                i = k + 1
            return r
        pr, ob = ranks([c[2] for c in cells]), ranks([c[3] for c in cells])
        mp, mo = mean(pr), mean(ob)
        den = (sum((x - mp) ** 2 for x in pr) * sum((y - mo) ** 2 for y in ob)) ** 0.5
        rho = sum((x - mp) * (y - mo) for x, y in zip(pr, ob)) / den if den else float("nan")
        mae = mean([abs(c[2] - c[3]) for c in cells])
        out["two_step_check"] = {"cells": cells, "mae": mae, "spearman": rho}
        head += ["## Two-step account (S1d)", "",
                 f"Cells {len(cells)}, mean absolute error {mae:.3f}, Spearman {rho:.2f}. "
                 f"Mean predicted {mean([c[2] for c in cells]):.1%}, mean observed {mean([c[3] for c in cells]):.1%}.", ""]
    lines = lines[:2] + head + lines[2:]

    o = ROOT / a.out
    o.parent.mkdir(parents=True, exist_ok=True)
    o.with_suffix(".md").write_text("\n".join(lines))
    o.with_suffix(".json").write_text(json.dumps(out, indent=1))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
