"""Write every number used in paper A as LaTeX macros and tables, from the result files.

    python src/numbers_a.py

Outputs paper_A/numbers.tex (macros) and paper_A/tab_*.tex (tables). Nothing in the report is typed by hand.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "paper_A"
SIX = ["adaption/deepseek-v4-flash", "adaption/gemma-4-31b-it", "adaption/qwen3.8-27b",
       "openrouter/anthropic/claude-haiku-5.5", "openrouter/openai/gpt-5.6-luna",
       "openrouter/mistralai/mistral-small-2603"]
TERRA = "openrouter/openai/gpt-5.6-terra"
NAMES = {SIX[0]: "DeepSeek V4 Flash", SIX[1]: "Gemma 4 31B", SIX[2]: "Qwen 3.8 27B", SIX[3]: "Claude Haiku 5.5",
         SIX[4]: "GPT-5.6 Luna", SIX[5]: "Mistral Small 2603", TERRA: "GPT-5.6 Terra"}
KEY = {SIX[0]: "Deepseek", SIX[1]: "Gemma", SIX[2]: "Qwen", SIX[3]: "Haiku", SIX[4]: "Luna", SIX[5]: "Mistral",
       TERRA: "Terra"}
macros: dict[str, str] = {}


def pct(x: float, digits: int = 0) -> str:
    if digits == 0 and (0.995 <= x < 1 or 0 < x < 0.005):
        digits = 1   # do not round 99.7% up to 100% or 0.3% down to 0%
    return f"{100 * x:.{digits}f}\\%"


def put(name: str, value: str) -> None:
    assert name.isalpha(), name
    macros[name] = value


def cell(s: dict, j: str, group: str, pair: str, variant: str = "default") -> dict | None:
    return s["judges"].get(j, {}).get("variants", {}).get(variant, {}).get("groups", {}).get(group, {}).get(pair)


def ci(c: dict | None) -> str:
    return "--" if not c else f"{100 * c['rate']:.0f} ({100 * c['lo']:.0f}--{100 * c['hi']:.0f})"


def study1() -> None:
    p = ROOT / "results/study1/summary.json"
    if not p.exists():
        return
    s = json.loads(p.read_text())
    rows = []
    bk, ba, wh, tone, acc, hedged_all, flagged_only, a_all = [], [], [], [], [], [], [], []
    for j in SIX + [TERRA]:
        if j not in s["judges"]:
            continue
        jr = s["judges"][j]
        c_bk, c_ba = cell(s, j, "judge knows", "CW-IDK"), cell(s, j, "all", "CW-IDK")
        c_ak = cell(s, j, "judge knows", "CC-IDK")
        c_hedged = cell(s, j, "judge knows", "CW-HC")
        c_wh = cell(s, j, "judge knows", "CW-CC")   # equal-tone control, added after the registered runs
        c_bu = cell(s, j, "judge does not know", "CW-IDK")
        c_hw = cell(s, j, "all", "HW-IDK")
        det = s.get("detection", {}).get(j)
        c_bf = cell(s, j, "judge tells the two answers apart", "CW-IDK")
        c_bflag = cell(s, j, "judge flags the wrong answer as incorrect", "CW-IDK")
        star = "$^{*}$" if j == TERRA else ""
        det_txt = f"{100 * det['tells_apart']:.0f}" if det and "tells_apart" in det else "--"
        rows.append(f"{NAMES[j]}{star} & {100 * jr['own_accuracy']:.0f} & {ci(c_ak)} & {ci(c_bk)} & {ci(c_bu)} & "
                    f"{ci(c_wh)} & {det_txt} & {ci(c_bf)} \\\\")
        k = KEY[j]
        if c_bk:
            put(f"bKnows{k}", pct(c_bk["rate"]))
            put(f"bKnowsLo{k}", pct(c_bk["lo"]))
            put(f"bKnowsHi{k}", pct(c_bk["hi"]))
            put(f"nKnows{k}", str(c_bk["n"]))
        if c_ba:
            put(f"bAll{k}", pct(c_ba["rate"]))
        if c_wh:
            put(f"wrongOverRight{k}", pct(c_wh["rate"]))
        if c_hedged:
            put(f"wrongOverHedged{k}", pct(c_hedged["rate"]))
            if j in SIX:
                hedged_all.append(c_hedged["rate"])
        if c_bu:
            put(f"bUnknown{k}", pct(c_bu["rate"]))
        if det:
            put(f"flagged{k}", pct(det["cw_flagged"]))
            put(f"accepted{k}", pct(det["cc_accepted"]))
            put(f"tellsApart{k}", pct(det.get("tells_apart", float("nan"))))
        if c_bflag:
            put(f"bFlaggedOnly{k}", pct(c_bflag["rate"]))
            if j in SIX:
                flagged_only.append(c_bflag["rate"])
        if c_bf:
            put(f"bFlagged{k}", pct(c_bf["rate"]))
            put(f"nFlagged{k}", str(c_bf["n"]))
        if j in SIX:
            acc.append(jr["own_accuracy"])
            if c_bk:
                bk.append(c_bk["rate"])
            if c_ba:
                ba.append(c_ba["rate"])
            c_aa = cell(s, j, "all", "CC-IDK")
            if c_aa:
                a_all.append(c_aa["rate"])
            if c_wh:
                wh.append(c_wh["rate"])
            t = cell(s, j, "all", "CW-HW")
            if t:
                tone.append(t["rate"])
            if c_hw:
                put(f"hedgedWrongOverIdk{k}", pct(c_hw["rate"]))
    if bk:
        put("bKnowsMin", pct(min(bk)))
        put("bKnowsMax", pct(max(bk)))
        put("bAllMin", pct(min(ba)))
        put("bAllMax", pct(max(ba)))
        put("wrongOverRightMin", pct(min(wh)))
        put("wrongOverRightMax", pct(max(wh)))
        put("wrongOverHedgedMin", pct(min(hedged_all)))
        put("wrongOverHedgedMax", pct(max(hedged_all)))
        put("equalToneJudges", str(sum(1 for j in SIX if cell(s, j, "judge knows", "CW-CC"))))
        if flagged_only:
            put("bFlaggedOnlyMin", pct(min(flagged_only)))
            put("bFlaggedOnlyMax", pct(max(flagged_only)))
        put("aAllMin", pct(min(a_all)))
        put("aAllMax", pct(max(a_all)))
        gaps = {j: cell(s, j, "judge knows", "CW-IDK")["rate"] - cell(s, j, "judge knows", "CW-CC")["rate"]
                for j in SIX if cell(s, j, "judge knows", "CW-CC")}
        if gaps:
            put("gapMin", f"{100 * min(gaps.values()):.0f}")
            put("gapMax", f"{100 * max(gaps.values()):.0f}")
        # unparsed replies and position
        un, tot = [], []
        for j in SIX:
            v = s["judges"][j]["variants"]["default"]
            if "unparsed" in v:
                n_items = cell(s, j, "all", "CW-IDK")["n"]
                un.append(v["unparsed"].get("CW-IDK", 0) / 600)
        if un:
            put("unparsedPrimaryMax", pct(max(un), 1))
        pos = {j: s["judges"][j]["variants"]["default"]["picks_first_position"] for j in SIX}
        put("posFirstMin", pct(min(pos.values())))
        put("posFirstMax", pct(max(pos.values())))
        put("accMin", pct(min(acc)))
        put("accMax", pct(max(acc)))
    if tone:
        put("toneMin", pct(min(tone)))
        put("toneMax", pct(max(tone)))
    dom, hw, fl, bf, ta, acp = [], [], [], [], [], []
    for j in SIX:
        for d in ("medqa", "law", "geo"):
            c = cell(s, j, f"domain {d}", "CW-IDK")
            if c:
                dom.append(c["rate"])
        c = cell(s, j, "all", "HW-IDK")
        if c:
            hw.append(c["rate"])
        det = s.get("detection", {}).get(j)
        if det:
            fl.append(det["cw_flagged"])
            acp.append(det["cc_accepted"])
            if "tells_apart" in det:
                ta.append(det["tells_apart"])
        c = cell(s, j, "judge tells the two answers apart", "CW-IDK")
        if c:
            bf.append(c["rate"])
    hw_above = [x for x in hw if x > 0.5]
    put("hwIdkAbove", ["no", "one", "two", "three", "four", "five", "six"][len(hw_above)])
    if hw_above:
        put("hwIdkAboveMin", pct(min(hw_above)))
        put("hwIdkAboveMax", pct(max(hw_above)))
    hw_below = [x for x in hw if x <= 0.5]
    if hw_below:
        put("hwIdkBelow", pct(min(hw_below)))
    put("tellsApartMajority", ["No", "One", "Two", "Three", "Four", "Five", "Six"][sum(x > 0.5 for x in ta)] if ta else "--")
    put("domainCells", str(len(dom)))
    put("domainCellsAbove", str(sum(x > 0.5 for x in dom)))
    for name, xs in (("bDomain", dom), ("hwIdk", hw), ("flagged", fl), ("bFlagged", bf), ("tellsApart", ta),
                     ("accepted", acp)):
        if xs:
            put(f"{name}Min", pct(min(xs)))
            put(f"{name}Max", pct(max(xs)))
    # a sized example: two models that differ only on the questions neither knows
    hk = SIX[3]
    a_h, b_h = cell(s, hk, "all", "CC-IDK"), cell(s, hk, "all", "CW-IDK")
    if a_h and b_h:
        import math
        w = b_h["rate"] + 0.25 * (a_h["rate"] - b_h["rate"])
        overall = 0.8 * 0.5 + 0.2 * w
        put("exampleW", pct(w))
        put("exampleOverall", pct(overall, 1))
        put("exampleElo", f"{400 * math.log10(overall / (1 - overall)):.0f}")
    sp_ = ROOT / "results/study1/strict_parse.json"
    if sp_.exists():
        x = json.loads(sp_.read_text())[SIX[1]]
        put("strictGemmaShare", pct(x["strict"]["share_no_verdict"]))
        put("strictGemmaB", pct(x["strict"]["b_knows"]))
        put("strictGemmaQ", str(x["strict"]["known_questions"]))
        put("looseGemmaShare", pct(x["loose"]["share_no_verdict"], 1))
    gm = s["judges"][SIX[1]]["variants"]["default"]
    put("gemmaToneUnparsed", str(gm["unparsed"]["CW-HW"]))
    put("gemmaToneItems", str(gm["parsed_items"]["CW-HW"]))
    for lab in ("H1", "H1F", "S1g", "S1g2"):
        t = s.get("tests", {}).get(lab)
        if t:
            six = [j for j in SIX if j in t["holm_pass"]]
            name = {"H1": "hOne", "H1F": "hOneF", "S1g": "sOneG", "S1g2": "sOneGApart"}[lab]
            put(f"{name}Pass", str(sum(t["holm_pass"][j] for j in six)))
            put(f"{name}Judges", str(len(six)))
            put(f"{name}PassWord", WORDS[sum(t["holm_pass"][j] for j in six)])
    ts = s.get("two_step_check")
    if ts:
        put("twoStepMae", f"{ts['mae']:.2f}")
        put("twoStepRho", f"{ts['spearman']:.2f}")
        put("twoStepPred", pct(sum(c[2] for c in ts["cells"]) / len(ts["cells"])))
        put("twoStepObs", pct(sum(c[3] for c in ts["cells"]) / len(ts["cells"])))
        put("twoStepCells", str(len(ts["cells"])))
    (OUT / "tab_main.tex").write_text("\n".join(rows) + "\n")


def study3() -> None:
    p = ROOT / "results/study3/summary.json"
    if not p.exists():
        return
    s = json.loads(p.read_text())
    r, tot, q = s["registers"], s["total"], s["platform"]
    put("adaptRows", str(tot["n"]))
    put("adaptAbstainAfter", str(tot.get("abstain", 0)))
    put("adaptHedgedAfter", str(tot.get("hedged", 0)))
    put("adaptCommit", str(tot["commit"]))
    put("adaptLeak", str(tot.get("leak", 0)))
    put("adaptIdkCommit", str(r["IDK"]["commit"]))
    put("adaptIdkRows", str(r["IDK"]["n"]))
    put("adaptIdkWrong", str(r["IDK"].get("wrong", 0)))
    put("adaptIdkCorrect", str(r["IDK"].get("correct", 0)))
    put("adaptCwCommit", str(r["CW"]["commit"]))
    put("adaptCwCorrected", str(r["CW"].get("correct", 0)))
    put("adaptRightCommit", str(r["CC"]["commit"] + r["HC"]["commit"]))
    put("adaptRightBroken", str(r["CC"].get("wrong", 0) + r["HC"].get("wrong", 0)))
    put("adaptHcHedged", str(r["HC"].get("hedged", 0)))
    put("adaptGradeBefore", q["grade_before"])
    put("adaptGradeAfter", q["grade_after"])
    put("adaptScoreBefore", f"{q['score_before']:.1f}")
    put("adaptScoreAfter", f"{q['score_after']:.1f}")
    names = {"CC": "Assertive, correct", "HC": "Hedged, correct", "IDK": "Abstention", "CW": "Assertive, wrong"}
    rows = []
    for k in ("CC", "HC", "IDK", "CW"):
        c = r[k]
        rows.append(f"{names[k]} & {c['n']} & {c['commit']} & {c.get('correct', 0)} & {c.get('wrong', 0)} & "
                    f"{c.get('abstain', 0)} & {c.get('hedged', 0)} & {c.get('disagree', 0)} \\\\")
    (OUT / "tab_adapt.tex").write_text("\n".join(rows) + "\n")
    p2 = ROOT / "results/study3c/summary.json"
    if p2.exists():
        b = json.loads(p2.read_text())
        for reg, name in (("IDK", "privIdk"), ("FACT", "privFact")):
            c = b.get(reg, {})
            put(f"{name}Rows", str(c.get("n", 0)))
            put(f"{name}Different", str(c.get("DIFFERENT", 0)))
            put(f"{name}Same", str(c.get("SAME", 0)))
            put(f"{name}Abstain", str(c.get("ABSTAIN", 0)))
            put(f"{name}Disagree", str(c.get("disagree", 0)))
        ev = ROOT / "results/study3c/evaluation.json"
        if ev.exists():
            q2 = json.loads(ev.read_text()).get("quality", {})
            if q2.get("grade_before"):
                put("privGradeBefore", str(q2["grade_before"]))
                put("privGradeAfter", str(q2["grade_after"]))
                put("privScoreBefore", f"{q2['score_before']:.1f}")
                put("privScoreAfter", f"{q2['score_after']:.1f}")


VARIANTS = [("default", "Default"), ("data", "Data curation"), ("selfcheck", "Own answer shown"),
            ("stakes", "Stakes"), ("accuracy", "Accuracy first"), ("cot", "Written rationale")]


def study4() -> None:
    p = ROOT / "results/study4/summary.json"
    if not p.exists():
        return
    s = json.loads(p.read_text())
    rep = s.get("repair", {})
    judges = [j for j in SIX if j in s["judges"]]

    def cut_share(j: str, v: str) -> float:
        vr = s["judges"][j]["variants"].get(v, {})
        n_q = 90 if v in ("cot", "think") else 150
        return vr.get("unparsed", {}).get("CW-IDK", 0) / (2 * n_q)

    flagged = []
    rows, repaired_by = [], {}
    for v, name in VARIANTS:
        cells = []
        for j in judges:
            r = rep.get(f"{j}|{v}")
            if not r:
                cells.append("--")
                continue
            cs = cut_share(j, v)
            if cs > 0.5:
                cells.append("n/e")
                flagged.append((j, v, cs, r["n_knows"]))
                continue
            mark = "$^{\\dagger}$" if r["repaired"] and v != "default" else ""
            if cs > 0.10:
                mark += "$^{\\ddagger}$"
                flagged.append((j, v, cs, r["n_knows"]))
            cells.append(f"{100 * r['b_knows']:.0f}{mark}")
            if r["repaired"] and v not in ("default", "data"):
                repaired_by.setdefault(v, []).append(j)
        rows.append(f"{name} & " + " & ".join(cells) + " \\\\")
    rows.append("\\midrule")
    for v, name in (("default", "Default"), ("accuracy", "Accuracy first")):
        cells = []
        for j in judges:
            r = rep.get(f"{j}|{v}")
            cells.append("--" if not r or r["a_unknown"] is None else
                         f"{100 * r['a_unknown']:.0f} / {100 * r['b_unknown']:.0f}")
        rows.append(f"{name}, $a$ / $b$ & " + " & ".join(cells) + " \\\\")
    short = {SIX[0]: "DeepSeek", SIX[1]: "Gemma", SIX[2]: "Qwen", SIX[3]: "Haiku", SIX[4]: "Luna", SIX[5]: "Mistral"}
    n_main = len(VARIANTS)
    full = ["\\begin{tabular}{@{}l" + "r" * len(judges) + "@{}}", "\\toprule",
            " & ".join(["Instruction"] + [short[j] for j in judges]) + " \\\\", "\\midrule",
            "\\multicolumn{" + str(len(judges) + 1) + "}{@{}l}{\\emph{Questions the judge knows, $b$}} \\\\"]
    full += rows[:n_main]
    full += ["\\midrule", "\\multicolumn{" + str(len(judges) + 1) +
             "}{@{}l}{\\emph{Questions the judge does not know, $a$ / $b$}} \\\\"]
    full += [r.replace(", $a$ / $b$", "") for r in rows[n_main + 1:]]
    full += ["\\bottomrule", "\\end{tabular}"]
    (OUT / "tab_fix_full.tex").write_text("\n".join(full) + "\n")
    (OUT / "tab_fix.tex").write_text("\n".join(rows) + "\n")
    (OUT / "tab_fix_head.tex").write_text(" & ".join(["Instruction"] + [NAMES[j].replace(" ", "~", 1) if False else NAMES[j] for j in judges]) + " \\\\\n")
    put("fixJudges", str(len(judges)))
    # a cell with more than half of the replies cut is not evaluated, so it cannot count as repaired
    per_variant = {v: len(repaired_by.get(v, [])) for v, _ in VARIANTS if v not in ("default", "data", "think")}
    put("fixMaxSingle", str(max(per_variant.values()) if per_variant else 0))
    put("fixMaxSingleWord", WORDS[max(per_variant.values()) if per_variant else 0])
    put("fixRepairedUnknown", str(sum(1 for k_, r_ in rep.items() if r_.get("repaired_unknown")
                                      and k_.split("|")[1] not in ("default", "data", "think"))))
    put("fixRepairedAccuracy", str(len(repaired_by.get("accuracy", []))))
    put("fixRepairedStakes", str(len(repaired_by.get("stakes", []))))
    put("fixRepairedSelfcheck", str(len(repaired_by.get("selfcheck", []))))
    put("fixRepairedCot", str(len(repaired_by.get("cot", []))))
    anyrep = {j for js in repaired_by.values() for j in js}
    put("fixRepairedAny", str(len(anyrep)))
    for v, key in (("accuracy", "Accuracy"), ("data", "Data"), ("selfcheck", "Selfcheck"), ("stakes", "Stakes")):
        bs = [rep[f"{j}|{v}"]["b_knows"] for j in judges if f"{j}|{v}" in rep]
        if bs:
            put(f"fix{key}BMin", pct(min(bs)))
            put(f"fix{key}BMax", pct(max(bs)))
    au = [rep[f"{j}|accuracy"]["a_unknown"] for j in judges if rep.get(f"{j}|accuracy", {}).get("a_unknown") is not None]
    bu = [rep[f"{j}|accuracy"]["b_unknown"] for j in judges if rep.get(f"{j}|accuracy", {}).get("b_unknown") is not None]
    if au:
        put("fixAccuracyAUnknownMin", pct(min(au)))
        put("fixAccuracyAUnknownMax", pct(max(au)))
        put("fixAccuracyBUnknownMin", pct(min(bu)))
        put("fixAccuracyBUnknownMax", pct(max(bu)))
    for j in judges:
        for v, key in (("cot", "Cot"), ("think", "Think"), ("accuracy", "Accuracy"), ("stakes", "Stakes")):
            r = rep.get(f"{j}|{v}")
            if r:
                put(f"fix{key}B{KEY[j]}", pct(r["b_knows"]))
    vn = dict(VARIANTS)
    put("fixFlagged", ", ".join(f"{NAMES[j]} under {vn[v].lower()} ({100 * cs_:.0f}\\%)" for j, v, cs_, _ in flagged))
    for j in (SIX[3], SIX[4], SIX[5]):
        r_ = rep.get(f"{j}|think")
        if r_:
            put(f"thinkReg{KEY[j]}", pct(r_["b_knows"]))
    put("thinkRegRepaired", ["no", "one", "two", "three"][sum(1 for j in (SIX[3], SIX[4], SIX[5]) if rep.get(f"{j}|think", {}).get("repaired"))])
    cot = {j: rep[f"{j}|cot"] for j in judges if f"{j}|cot" in rep and cut_share(j, "cot") <= 0.5}
    if cot:
        left = [r_["b_knows"] for r_ in cot.values() if not r_["repaired"]]
        put("cotJudges", ["no", "one", "two", "three", "four", "five", "six"][len(cot)])
        above = [r_["b_knows"] for r_ in cot.values() if r_["b_knows"] > 0.5]
        put("cotAboveHalf", ["no", "one", "two", "three", "four", "five", "six"][len(above)])
        if above:
            put("cotAboveBMin", pct(min(above)))
            put("cotAboveBMax", pct(max(above)))
        put("cotNotRepaired", ["no", "one", "two", "three", "four", "five", "six"][len(left)])
        if left:
            put("cotLeftBMin", pct(min(left)))
            put("cotLeftBMax", pct(max(left)))
    mp = ROOT / "results/study4/mtbench.json"
    if mp.exists():
        mb = json.loads(mp.read_text())
        rows_m, above = [], []
        ran = 0
        for j in SIX:
            vr = mb["judges"].get(j, {}).get("variants", {}).get("mtbench")
            if not vr or "CW-IDK" not in vr["groups"]["judge knows"]:
                continue
            a_, b_ = vr["groups"]["judge knows"]["CC-IDK"], vr["groups"]["judge knows"]["CW-IDK"]
            cut = vr["unparsed"]["CW-IDK"] / (2 * mb["n_items"])
            if cut > 0.5:   # replies cut before the verdict
                rows_m.append(f"{NAMES[j]} & {b_['n']} & n/e & n/e & {vr['ties']['CW-IDK']} & {vr['unparsed']['CW-IDK']} \\\\")
                put("mtCutJudge", NAMES[j])
                put("mtCutShare", pct(cut))
                continue
            ran += 1
            put(f"mtB{KEY[j]}", pct(b_["rate"]))
            if b_["rate"] > 0.5:
                above.append(b_["rate"])
            calls = 2 * vr["parsed_items"]["CW-IDK"] if "parsed_items" in vr else 0
            rows_m.append(f"{NAMES[j]} & {b_['n']} & {100 * a_['rate']:.0f} ({100 * a_['lo']:.0f}--{100 * a_['hi']:.0f}) & "
                          f"{100 * b_['rate']:.0f} ({100 * b_['lo']:.0f}--{100 * b_['hi']:.0f}) & {vr['ties']['CW-IDK']} & "
                          f"{vr['unparsed']['CW-IDK']} \\\\")
        (OUT / "tab_mtbench.tex").write_text("\n".join(rows_m) + "\n")
        put("mtAbove", ["no", "one", "two", "three", "four", "five", "six"][len(above)])
        put("mtJudges", ["no", "one", "two", "three", "four", "five", "six"][ran])
        if above:
            put("mtAboveMin", pct(min(above)))
            put("mtAboveMax", pct(max(above)))
        put("mtQuestions", str(mb["n_items"]))
    ls = ROOT / "results/study4/luna_selection.json"
    if ls.exists():
        x = json.loads(ls.read_text())
        put("lunaSelReasoned", pct(x["default_b_reasoned_any"]))
        put("lunaSelNot", pct(x["default_b_reasoned_none"]))
    rp = ROOT / "results/study4/reasoning.json"
    if rp.exists():
        r = json.loads(rp.read_text())
        rows_r = []
        for key_, name, lab in (("think|" + SIX[3], "Haiku", "Claude Haiku 5.5, reasoning mode on"),
                                ("think|" + SIX[4], "Luna", "GPT-5.6 Luna, reasoning mode on"),
                                ("reason|" + SIX[5], "Mistral", "Mistral Small 2603, reasoning effort requested")):
            x = r.get(key_)
            if not x:
                continue
            br, bn = x["b_reasoned"], x["b_not"]
            n_r, n_n = (br["calls"] if br else 0), (bn["calls"] if bn else 0)
            put(f"reasonedShare{name}", pct(n_r / (n_r + n_n)))
            if br:
                put(f"reasonedB{name}", pct(br["rate"]))
            if bn:
                put(f"notReasonedB{name}", pct(bn["rate"]))
            put(f"reasonedQuestions{name}", str(x["questions"]))
            def c(v):
                return "--" if not v else f"{100 * v['rate']:.0f} ({100 * v['lo']:.0f}--{100 * v['hi']:.0f})"
            rows_r.append(f"{lab} & {x['questions']} & {100 * n_r / (n_r + n_n):.0f} & {c(br)} & {c(bn)} \\\\")
        (OUT / "tab_reasoning.tex").write_text("\n".join(rows_r) + "\n")
    s1 = json.loads((ROOT / "results/study1/summary.json").read_text())
    vtc = s1.get("verify_then_compare", {})
    ps = [v["p_star_check"] for j, v in vtc.items() if j in SIX and v["p_star_check"] == v["p_star_check"]]
    if ps:
        put("vtcMin", f"{min(ps):.2f}")
        put("vtcMax", f"{max(ps):.2f}")
        put("vtcJudges", str(len(ps)))
        put("vtcInBand", str(sum(0.25 <= x <= 0.75 for x in ps)))
        for j, v in vtc.items():
            put(f"vtc{KEY[j]}", f"{v['p_star_check']:.2f}")
            put(f"vtcA{KEY[j]}", pct(v["a_check"]))
            put(f"vtcB{KEY[j]}", pct(v["b_check"]))


def study5() -> None:
    d = ROOT / "results/study5"
    if (d / "natural_duels.json").exists():
        n = json.loads((d / "natural_duels.json").read_text())
        bs = [v["b_nat"]["rate"] for v in n["judges"].values()]
        as_ = [v["a_nat"]["rate"] for v in n["judges"].values()]
        put("natBMin", pct(min(bs), 1))
        put("natBMax", pct(max(bs), 1))
        put("natAMin", pct(min(as_)))
        put("natQuestions", str(n["used"]))
        put("natWrong", str(n["assert_wrong"]))
        put("natWrongMin", str(min(v["b_nat"]["n"] for v in n["judges"].values())))
        put("natPool", f"{n['pool_questions']:,}".replace(",", "{,}"))
    if (d / "selection_table.json").exists():
        s = json.loads((d / "selection_table.json").read_text())
        rows = []
        names = {"J": "J, judge, default instruction", "F": "F, judge, accuracy first", "K": "K, by the key",
                 "R": "R, random"}
        for r in ("J", "F", "K", "R"):
            x = s["rules"][r]
            put(f"selAbstain{r}", pct(x["outcome:abstain"]["share"], 1))
            put(f"selWrong{r}", pct(x["outcome:wrong"]["share"], 1))
            put(f"selCorrect{r}", pct(x["outcome:correct"]["share"], 1))
        (OUT / "sel_names.json").write_text(json.dumps(names))
    if (d / "pool_summary.json").exists():
        ps = json.loads((d / "pool_summary.json").read_text())
        put("poolAbstainShare", pct(ps["abstain"]["abstain"]["share"], 1))
        put("poolAssertWrong", pct(ps["assert"]["wrong"]["share"], 1))
    runs = d / "autoscientist_runs.jsonl"
    if runs.exists():
        for ln in runs.read_text().splitlines():
            r = json.loads(ln)
            if r.get("op") == "final" and r.get("status") == "succeeded" and r.get("best_win_rate") is not None:
                put(f"platformWin{r['rule']}", pct(r["best_win_rate"], 1))
    et = d / "eval_table.json"
    if et.exists():
        e = json.loads(et.read_text())
        sel = json.loads((d / "selection_table.json").read_text())["rules"] if (d / "selection_table.json").exists() else {}
        labels = {"J": "J, judge, default instruction", "F": "F, judge, accuracy first", "K": "K, by the key",
                  "R": "R, random"}
        rows = []
        for r in ("J", "F", "K", "R"):
            m = e["models"].get(r)
            if not m:
                continue
            key = r
            put(f"evalAbstain{key}", pct(m["abstention_rate"]["value"], 1))
            put(f"evalWrong{key}", pct(m["wrong_rate"]["value"], 1))
            put(f"evalCorrect{key}", pct(m["accuracy"]["value"], 1))
            put(f"evalUnparsed{key}", pct(m["unparsed_rate"]["value"], 1))
            put(f"evalScore{key}", f"{m['penalised_score']['value']:.2f}")
            s_ab = sel.get(r, {}).get("outcome:abstain", {}).get("share")
            s_wr = sel.get(r, {}).get("outcome:wrong", {}).get("share")
            rows.append(f"{labels[r]} & {100 * s_ab:.1f} & {100 * s_wr:.1f} & {100 * m['abstention_rate']['value']:.1f} & "
                        f"{100 * m['wrong_rate']['value']:.1f} & {100 * m['accuracy']['value']:.1f} & "
                        f"{100 * m['unparsed_rate']['value']:.1f} & {m['penalised_score']['value']:.2f} \\\\")
        rows.append("\\midrule")
        dj = e["differences"]["J-K"]["penalised_score"]
        put("scoreDiffJK", f"{dj['value']:.2f}")
        put("scoreDiffJKLo", f"{dj['lo']:.2f}")
        put("scoreDiffJKHi", f"{dj['hi']:.2f}")
        for k, lab in (("base_assert", "Base model, assert instruction"), ("base_abstain", "Base model, cautious instruction")):
            m = e["models"].get(k)
            if m:
                nm = "BaseAssert" if k == "base_assert" else "BaseCautious"
                put(f"evalAbstain{nm}", pct(m["abstention_rate"]["value"], 1))
                put(f"evalWrong{nm}", pct(m["wrong_rate"]["value"], 1))
                put(f"evalCorrect{nm}", pct(m["accuracy"]["value"], 1))
                rows.append(f"{lab} & -- & -- & {100 * m['abstention_rate']['value']:.1f} & "
                            f"{100 * m['wrong_rate']['value']:.1f} & {100 * m['accuracy']['value']:.1f} & "
                            f"{100 * m['unparsed_rate']['value']:.1f} & {m['penalised_score']['value']:.2f} \\\\")
        (OUT / "tab_loop.tex").write_text("\n".join(rows) + "\n")
        put("evalQuestions", str(e["questions"]))
    n2 = d / "natural2.json"
    if n2.exists():
        x = json.loads(n2.read_text())
        bs = [v["b"]["rate"] for v in x["judges"].values()]
        as_ = [v["a"]["rate"] for v in x["judges"].values()]
        put("natTwoBMin", pct(min(bs)))
        put("natTwoBMax", pct(max(bs)))
        put("natTwoAMin", pct(min(as_)))
        put("natTwoQuestions", str(x["wrong_questions"]))
        nm = {"openrouter/anthropic/claude-haiku-5.5": "Claude Haiku 5.5", "openrouter/openai/gpt-5.6-luna": "GPT-5.6 Luna",
              "openrouter/mistralai/mistral-small-2603": "Mistral Small 2603"}
        rows_n = []
        for j, v in x["judges"].items():
            b, a_ = v["b"], v["a"]
            rows_n.append(f"{nm.get(j, j)} & {100 * b['rate']:.0f} ({100 * b['lo']:.0f}--{100 * b['hi']:.0f}) & {b['n']} & "
                          f"{100 * a_['rate']:.0f} ({100 * a_['lo']:.0f}--{100 * a_['hi']:.0f}) & {a_['n']} \\\\")
        (OUT / "tab_natural2.tex").write_text("\n".join(rows_n) + "\n")
    fu = d / "eval_table_followup.json"
    if fu.exists():
        f = json.loads(fu.read_text())
        shares = {}
        st1 = d / "selection_table.json"
        st2 = d / "selection_table_followup.json"
        if st1.exists():
            for r_, x_ in json.loads(st1.read_text())["rules"].items():
                shares[r_] = x_["outcome:abstain"]["share"]
        if st2.exists():
            x2 = json.loads(st2.read_text())
            for r_, x_ in (x2.get("rules") or x2).items():
                if isinstance(x_, dict) and ("outcome:abstain" in x_ or "abstain" in x_):
                    shares.setdefault(r_, (x_.get("outcome:abstain") or x_["abstain"])["share"])
        dose = []
        for k_, lab in (("C", "C, cautious responses, no selection"), ("R", "R, random pick"), ("K", "K, pick by the key"),
                        ("J", "J, pick by the judge")):
            m = f["models"].get(k_ + "3")
            if m and k_ in shares:
                dose.append(f"{lab} & {100 * shares[k_]:.1f} & {100 * m['abstention_rate']['value']:.1f} & "
                            f"{100 * m['wrong_rate']['value']:.1f} & {100 * m['accuracy']['value']:.1f} \\\\")
                put(f"trainAbstain{k_}", pct(shares[k_], 1))
        (OUT / "tab_dose.tex").write_text("\n".join(dose) + "\n")
        labels = {"C3": "C, cautious style, no selection", "R3": "R, random", "K3": "K, by the key (oracle)",
                  "J3": "J, judge, default instruction"}
        train_share = {}
        for fn in ("selection_table.json", "selection_table_followup.json"):
            if (d / fn).exists():
                for r_, x_ in json.loads((d / fn).read_text())["rules"].items():
                    v_ = x_.get("outcome:abstain") or x_.get("abstain")
                    if v_:
                        train_share.setdefault(r_, v_["share"])
        rows_f = []
        for k_, lab in labels.items():
            m = f["models"].get(k_)
            if not m:
                continue
            nm = k_[0]
            put(f"fuAbstain{nm}", pct(m["abstention_rate"]["value"], 1))
            put(f"fuWrong{nm}", pct(m["wrong_rate"]["value"], 1))
            put(f"fuCorrect{nm}", pct(m["accuracy"]["value"], 1))
            put(f"fuScore{nm}", f"{m['penalised_score']['value']:.2f}")
            def c(x):
                return f"{100 * x['value']:.1f} ({100 * x['lo']:.1f}--{100 * x['hi']:.1f})"
            rows_f.append(f"{lab} & {100 * train_share.get(nm, float('nan')):.1f} & {c(m['abstention_rate'])} & {c(m['wrong_rate'])} & {c(m['accuracy'])} & "
                          f"{100 * m['unparsed_rate']['value']:.1f} & {m['penalised_score']['value']:.2f} \\\\")
        (OUT / "tab_followup.tex").write_text("\n".join(rows_f) + "\n")
        dw = f["differences"]["C3-J3"]["wrong_rate"]
        put("fuWrongDiff", f"{abs(100 * dw['value']):.1f}")
        put("fuWrongDiffLo", f"{abs(100 * dw['hi']):.1f}")
        put("fuWrongDiffHi", f"{abs(100 * dw['lo']):.1f}")
        jr_ = f["differences"]["J3-R3"]["abstention_rate"]
        put("fuJRDiff", f"{abs(100 * jr_['value']):.1f}")
        put("fuJRDiffLo", f"{abs(100 * jr_['hi']):.1f}")
        put("fuJRDiffHi", f"{abs(100 * jr_['lo']):.1f}")
        ds_ = f["differences"]["C3-J3"]["penalised_score"]
        put("fuScoreDiffLo", f"{ds_['lo']:.2f}".replace("-", "$-$"))
        put("fuScoreDiffHi", f"{ds_['hi']:.2f}")
    pool = d / "pool.jsonl"
    tj = d / "train_J.jsonl"
    if pool.exists() and tj.exists():
        rows_p = [json.loads(l) for l in pool.read_text().splitlines() if l.strip()]
        by = {}
        for r_ in rows_p:
            by.setdefault(r_["id"], {})[r_["style"]] = r_
        abst = [q for q in by.values() if q.get("abstain", {}).get("outcome") == "abstain"]
        bare = sum(1 for q in abst if len(q["abstain"]["text"].split()) <= 8)
        put("bareAbstentions", str(bare))
        longest = 0
        for l in tj.read_text().splitlines():
            r_ = json.loads(l)
            q = by[r_["id"]]
            lens = {k_: len(v_["text"].split()) for k_, v_ in q.items()}
            if lens[r_["style"]] == max(lens.values()):
                longest += 1
        put("jLongest", str(longest))
    pd = d / "p5d_J_K.json"
    if pd.exists():
        x = json.loads(pd.read_text())
        rs = [v["rate"] for v in x["judges"].values()]
        put("pFiveDMin", pct(min(rs)))
        put("pFiveDMax", pct(max(rs)))
        put("pFiveDQuestions", str(x["questions_that_differ"]))
    p = ROOT / "results/explore_idk2/summary.json"
    if p.exists():
        s = json.loads(p.read_text())
        b2 = [cell(s, j, "judge knows", "CW-IDK2") for j in SIX]
        b2 = [c["rate"] for c in b2 if c]
        if b2:
            words = ["no", "one", "two", "three", "four", "five", "six"]
            put("idkTwoMin", pct(min(b2)))
            put("idkTwoMax", pct(max(b2)))
            put("idkTwoJudges", words[len(b2)])
            ab = [x for x in b2 if x > 0.5]
            put("idkTwoAbove", words[len(ab)])
            if ab:
                put("idkTwoAboveMin", pct(min(ab)))
                put("idkTwoAboveMax", pct(max(ab)))
            be = [x for x in b2 if x <= 0.5]
            if be:
                put("idkTwoBelow", pct(min(be)))


WORDS = ["no", "one", "two", "three", "four", "five", "six"]


def rng_put(name: str, xs: list[float]) -> None:
    if xs:
        put(name + "Min", pct(min(xs)))
        put(name + "Max", pct(max(xs)))


def reruns() -> None:
    """Replies of one judge that were cut by the reply limit, and the reruns with a higher limit."""
    import re

    def count(run: str, variant: str, judge: str) -> tuple[int, int] | None:
        p = ROOT / run / "calls.jsonl"
        if not p.exists():
            return None
        n_, cut = 0, 0
        for ln in p.read_text().splitlines():
            d = json.loads(ln) if ln.strip() else {}
            if d.get("kind") == "duel" and d.get("variant") == variant and d["judge"] == judge and d["pair"] == "CW-IDK":
                n_ += 1
                up = d["text"].upper()
                ok = re.findall(r"\[\[([ABC])\]\]", up) if variant == "mtbench" else re.findall(r"VERDICT\W*([AB])\b", up)
                cut += not ok
        return (cut, n_) if n_ else None

    for lab, variant, first, again in (("Cot", "cot", "results/study4_adaption", "results/study4_adaption_cot_rerun"),
                                       ("Mt", "mtbench", "results/study4_adaption_mtbench",
                                        "results/study4_adaption_mtbench_rerun")):
        a, b = count(first, variant, SIX[2]), count(again, variant, SIX[2])
        if a:
            put(f"qwen{lab}Cut", str(a[0]))
            put(f"qwen{lab}Total", str(a[1]))
        put(f"qwen{lab}RerunCut", str(b[0]) if b else "?")
        put(f"qwen{lab}RerunTotal", str(b[1]) if b else "?")


def confirm2() -> None:
    """Registered confirmation on fresh questions (Amendment 2)."""
    p = ROOT / "results/confirm2/confirm.json"
    if not p.exists():
        return
    s = json.loads(p.read_text())
    js = [j for j in SIX if j in s["judges"]]
    kept = [j for j in js if not s["judges"][j]["dropped"]]
    t_ = s["tests"]
    put("cfQuestions", str(s["n_items"]))
    put("cfJudges", WORDS[len(js)])
    put("cfKept", WORDS[len(kept)])
    put("cfDropped", WORDS[len(js) - len(kept)])
    rng_put("cfB", [s["judges"][j]["b"]["rate"] for j in kept])
    rng_put("cfCtrl", [s["judges"][j]["control"]["rate"] for j in kept])
    gaps = [s["judges"][j]["gap"]["value"] for j in kept]
    if gaps:
        put("cfGapMin", f"{100 * min(gaps):.0f}")
        put("cfGapMax", f"{100 * max(gaps):.0f}")
    for lab, key in (("One", "C1"), ("Two", "C2"), ("Three", "C3"), ("Four", "C4_b"), ("FourA", "C4_a")):
        put("cfC" + lab + "Pass", WORDS[t_[key]])
    for lab, key in (("One", "C1_holds"), ("Two", "C2_holds"), ("Three", "C3_holds"), ("Four", "C4_holds")):
        put("cfC" + lab + "Outcome", "holds" if t_[key] else "fails")
    put("cfAllHold", "yes" if t_["C1_holds"] and t_["C2_holds"] and t_["C3_holds"] else "no")
    put("cfAllPass", WORDS[sum(s["judges"][j]["c1_pass"] and s["judges"][j]["c2_pass"] and s["judges"][j]["c3_pass"]
                               for j in kept)])
    rule = [j for j in kept if "rule" in s["judges"][j]]
    rng_put("cfRuleB", [s["judges"][j]["rule"]["b"] for j in rule])
    rng_put("cfRuleBBefore", [s["judges"][j]["rule"]["b_before"] for j in rule])
    rng_put("cfRuleA", [s["judges"][j]["rule"]["a"] for j in rule])
    put("cfRuleBelowHalf", WORDS[sum(s["judges"][j]["rule"]["b"] < 0.5 for j in rule)])
    fails = [j for j in rule if not s["judges"][j]["rule"]["share_ge_half"] < 0.05]
    put("cfCFourFailNames", " and ".join(NAMES[j] for j in fails) or "none")
    put("cfCFourFailB", ", ".join(pct(s["judges"][j]["rule"]["b"]) for j in fails) or "--")
    low =[j for j in rule if s["judges"][j]["rule"]["a"] < 0.6]
    put("cfRuleUnusable", WORDS[len(low)])
    put("cfRuleUnusableNames", " and ".join(NAMES[j] for j in low) or "none")
    ps = [s["judges"][j]["rule"]["p_star"] for j in rule]
    if ps:
        put("cfRulePstarMin", f"{min(ps):.2f}")
        put("cfRulePstarMax", f"{max(ps):.2f}")
    put("cfUnparsedMax", pct(max([s["judges"][j]["unparsed_primary"] for j in js] or [0]), 1))
    put("cfAboveHalf", WORDS[sum(s["judges"][j]["b"]["rate"] > 0.5 for j in kept)])
    fl = [s["judges"][j]["rule"]["wrong_flagged"] for j in rule]
    rng_put("cfFlagged", fl)
    rng_put("cfAccepted", [s["judges"][j]["rule"]["right_accepted"] for j in rule])
    rows = []
    for j in js:
        r = s["judges"][j]
        ru = r.get("rule")
        rows.append(f"{NAMES[j]}{'$^{\\ddagger}$' if r['dropped'] else ''} & {100 * r['own_accuracy']:.0f} & {ci(r['a'])} & {ci(r['b'])} & "
                    f"{ci(r['control'])} & "
                    + (f"{100 * ru['b']:.0f} ({100 * ru['b_lo']:.0f}--{100 * ru['b_hi']:.0f}) & "
                       f"{100 * ru['a']:.0f} ({100 * ru['a_lo']:.0f}--{100 * ru['a_hi']:.0f})" if ru else "-- & --")
                    + " \\\\")
    (OUT / "tab_confirm.tex").write_text("\n".join(rows) + "\n")


def freeform() -> None:
    """Free-form questions with natural-length replies (Amendment 3)."""
    p = ROOT / "results/freeform/summary.json"
    if not p.exists():
        return
    s = json.loads(p.read_text())
    js = [j for j in SIX if j in s["judges"]]
    kept = [j for j in js if not s["judges"][j]["dropped"]]
    t_ = s["tests"]
    put("ffQuestions", str(s["n_items"]))
    put("ffJudges", WORDS[len(js)])
    put("ffKept", WORDS[len(kept)])
    rng_put("ffKnows", [s["judges"][j]["knows"] for j in js])
    for lab, key in (("ffB", "b_short"), ("ffFull", "b_full"), ("ffCtrl", "control"), ("ffA", "a_short")):
        rng_put(lab, [s["judges"][j][key]["rate"] for j in kept if key in s["judges"][j]])
    for lab, key in (("One", "F1"), ("Two", "F2"), ("Three", "F3"), ("Four", "F4")):
        put("ffF" + lab + "Pass", WORDS[t_[key]])
        put("ffF" + lab + "Outcome", "holds" if t_[key + "_holds"] else "fails")
    put("ffMtUsable", WORDS[t_["F4_usable"]])
    usable = [j for j in js if s["judges"][j]["mt_usable"]]
    rng_put("ffMt", [s["judges"][j]["mt_b_short"]["rate"] for j in usable])
    above = [s["judges"][j]["mt_b_short"]["rate"] for j in usable if s["judges"][j]["mt_b_short"]["rate"] > 0.5]
    put("ffMtAbove", WORDS[len(above)])
    rng_put("ffMtAboveB", above)
    rng_put("ffMtFull", [s["judges"][j]["mt_b_full"]["rate"] for j in usable if "mt_b_full" in s["judges"][j]])
    fl = [s["judges"][j]["wrong_flagged"] for j in js if "wrong_flagged" in s["judges"][j]]
    rng_put("ffFlagged", fl)
    put("ffAboveHalf", WORDS[sum(s["judges"][j]["b_short"]["rate"] > 0.5 for j in kept if "b_short" in s["judges"][j])])
    put("ffFullAboveHalf", WORDS[sum(s["judges"][j]["b_full"]["rate"] > 0.5 for j in kept if "b_full" in s["judges"][j])])
    below = [j for j in kept if "b_short" in s["judges"][j] and s["judges"][j]["b_short"]["rate"] <= 0.5]
    put("ffBelowNames", " and ".join(NAMES[j] for j in below) or "none")
    put("ffBelowB", ", ".join(f"{100 * s['judges'][j]['b_short']['rate']:.0f}\\%" for j in below) or "--")
    put("ffBelowKnows", ", ".join(f"{100 * s['judges'][j]['knows']:.0f}\\%" for j in below) or "--")
    cp = ROOT / "results/confirm2/confirm.json"
    cf = json.loads(cp.read_text())["judges"] if cp.exists() else {}
    rows = []
    for j in SIX:
        r, c = s["judges"].get(j), cf.get(j)
        g = lambda d, k: "--" if not d or k not in d else f"{100 * d[k]['rate']:.0f}"  # noqa: E731
        mt = "--" if not r or "mt_b_short" not in r else ("n/e" if not r["mt_usable"] else f"{100 * r['mt_b_short']['rate']:.0f}")
        rows.append(f"{NAMES[j]} & {g(c, 'b')} & {g(c, 'control')} & {g(r, 'b_short')} & {g(r, 'b_full')} & "
                    f"{g(r, 'control')} & {mt} \\\\")
    (OUT / "tab_replicate.tex").write_text("\n".join(rows) + "\n")
    rows = []
    for j in js:
        r = s["judges"][j]
        mt = (lambda k: ci(r.get(k)) if r["mt_usable"] else "n/e")
        rows.append(f"{NAMES[j]}{'$^{\\ddagger}$' if r['dropped'] else ''} & {100 * r['knows']:.0f} & {ci(r.get('a_short'))} & "
                    f"{ci(r.get('b_short'))} & {ci(r.get('b_full'))} & {ci(r.get('control'))} & {mt('mt_b_short')} & "
                    f"{mt('mt_b_full')} \\\\")
    (OUT / "tab_freeform.tex").write_text("\n".join(rows) + "\n")
    items = [json.loads(ln) for ln in (ROOT / "data/items/trivia_free.jsonl").read_text().splitlines() if ln.strip()]
    ex = items[0]   # the first question of the set
    put("ffExampleQ", tex(ex["question"]))
    put("ffExampleWrong", tex(ex["resp"]["CW"]))
    put("ffExampleKey", tex(ex["answer"]))


def tex(s: str) -> str:
    rep = {"\\": "\\textbackslash{}", "&": "\\&", "%": "\\%", "$": "\\$", "#": "\\#", "_": "\\_", "{": "\\{",
           "}": "\\}", "~": "\\textasciitilde{}", "^": "\\textasciicircum{}", "<": "\\textless{}",
           ">": "\\textgreater{}"}
    out = "".join(rep.get(ch, ch) for ch in s)
    out = out.replace(' "', " ``").replace('"', "''")
    return out.replace("\n", " \\\\{} ")


def appendix() -> None:
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    import duels
    blocks = [("Judge instruction, default", duels.JUDGE_SYSTEM["default"]),
              ("Judge instruction, accuracy first", duels.JUDGE_SYSTEM["accuracy"]),
              ("Judge instruction, stakes", duels.JUDGE_SYSTEM["stakes"]),
              ("Judge instruction, written rationale", duels.JUDGE_SYSTEM["cot"]),
              ("Published judge prompt (MT-Bench pairwise prompt, entry pair-v2 of the file judge_prompts.jsonl in the FastChat repository), system part", duels.JUDGE_SYSTEM["mtbench"]),
              ("Published judge prompt, user part", "[User Question]\n<question with options>\n\n[The Start of Assistant A's Answer]\n<first response>\n[The End of Assistant A's Answer]\n\n[The Start of Assistant B's Answer]\n<second response>\n[The End of Assistant B's Answer]"),
              ("Judge instruction, data curation", duels.JUDGE_SYSTEM["data"]),
              ("Own answer shown (line added to the duel prompt, default instruction)",
               "Your own answer when you solved this question yourself: <letter>. <option text>"),
              ("Duel prompt", "User question:\n<question with options>\n\nResponse A:\n<first response>\n\n"
                              "Response B:\n<second response>\n\nWhich response is better, A or B?"),
              ("Closed-book answer of the judge", duels.KNOWS_SYSTEM),
              ("Detection", duels.DETECT_SYSTEM + " The prompt ends with: Is the response correct, Yes or No?"),
              ("Responses", " / ".join(f"{k}: {v}" for k, v in duels.REGISTERS.items()).replace("{x}", "X"))]
    sp = ROOT / "results/study5/style_prompts.json"
    if sp.exists():
        d = json.loads(sp.read_text())
        final = d.get("prompts") or d.get("final") or {}
        for k in ("assert", "hedge", "abstain"):
            if k in final:
                blocks.append((f"Loop, style instruction {'cautious' if k == 'abstain' else k}", final[k]))
    import adapt_analyze
    import freeform as ff
    blocks.append(("Free-form check, writer of the replies (Llama 4 Maverick)", ff.GEN_SYSTEM))
    blocks.append(("Free-form check, check of the planted answer", ff.VERIFY_SYSTEM
                   + " The prompt gives the question and the proposed answer and ends with: Is the proposed answer correct?"))
    blocks.append(("Free-form check, the judge's own answer", ff.KNOWS_SYSTEM))
    blocks.append(("Extractor, first audit", adapt_analyze.SYS1))
    blocks.append(("Extractor, second audit", adapt_analyze.SYS2))
    lines = []
    for name, text in blocks:
        lines.append(f"\\textbf{{{tex(name)}.}} {tex(text)}\n")
    (OUT / "app_prompts.tex").write_text("\n".join(lines))

    # all seven pairs per judge, all questions
    p = ROOT / "results/study1/summary.json"
    if p.exists():
        s = json.loads(p.read_text())
        pairs = ["CC-IDK", "CW-IDK", "HC-IDK", "HW-IDK", "CW-HC", "CW-HW", "CC-HC", "CW-CC"]
        rows = []
        for j in SIX:
            if j not in s["judges"]:
                continue
            cs = [cell(s, j, "all", pr) for pr in pairs]
            rows.append(f"{NAMES[j]} & " + " & ".join("--" if not c else f"{100 * c['rate']:.0f}" for c in cs) + " \\\\")
        (OUT / "tab_pairs.tex").write_text("\n".join(rows) + "\n")
        rows = []
        for j in SIX:
            if j not in s["judges"]:
                continue
            cs = [cell(s, j, f"domain {d}", pr) for d in ("medqa", "law", "geo") for pr in ("CC-IDK", "CW-IDK", "CW-HC")]
            rows.append(f"{NAMES[j]} & " + " & ".join("--" if not c else f"{100 * c['rate']:.0f}" for c in cs) + " \\\\")
        (OUT / "tab_domains.tex").write_text("\n".join(rows) + "\n")
        vt = s.get("verify_then_compare", {})
        rows = []
        for j in SIX + [TERRA]:
            v = vt.get(j)
            if v:
                star = "$^{*}$" if j == TERRA else ""
                rows.append(f"{NAMES[j]}{star} & {100 * v['a']:.0f} & {100 * v['b']:.0f} & {100 * v['a_check']:.0f} & "
                            f"{100 * v['b_check']:.0f} & {v['p_star_check']:.2f} ({v['lo']:.2f}--{v['hi']:.2f}) \\\\")
        (OUT / "tab_vtc.tex").write_text("\n".join(rows) + "\n")
        det = s.get("detection", {})
        rows = []
        for j in SIX + [TERRA]:
            v = det.get(j)
            if v:
                star = "$^{*}$" if j == TERRA else ""
                rows.append(f"{NAMES[j]}{star} & {100 * v['cw_flagged']:.0f} & {100 * v['cc_accepted']:.0f} & "
                            f"{100 * v.get('tells_apart', float('nan')):.0f} \\\\")
        (OUT / "tab_detect.tex").write_text("\n".join(rows) + "\n")
        vs = [s["judges"][j]["variants"]["default"]["groups"]["all"].get("derived", {}).get("v_eff") for j in SIX
              if j in s["judges"]]
        vs = [v for v in vs if v is not None]
        if vs:
            put("vEffMin", f"{min(vs):.2f}")
            put("vEffMax", f"{max(vs):.2f}")
    nd = ROOT / "results/study5/natural_duels.json"
    if nd.exists():
        n = json.loads(nd.read_text())
        nm = {"anthropic/claude-haiku-5.5": "Claude Haiku 5.5", "openai/gpt-5.6-luna": "GPT-5.6 Luna",
              "mistralai/mistral-small-2603": "Mistral Small 2603"}
        rows = []
        for j, v in n["judges"].items():
            b, a = v["b_nat"], v["a_nat"]
            rows.append(f"{nm.get(j, j)} & {100 * b['rate']:.1f} ({100 * b['lo']:.1f}--{100 * b['hi']:.1f}) & {b['n']} & "
                        f"{100 * a['rate']:.1f} ({100 * a['lo']:.1f}--{100 * a['hi']:.1f}) & {a['n']} \\\\")
        (OUT / "tab_natural.tex").write_text("\n".join(rows) + "\n")
    st = ROOT / "results/study5/selection_table.json"
    if st.exists():
        s5 = json.loads(st.read_text())
        names = {"J": "J, judge, default", "F": "F, judge, accuracy first", "K": "K, by the key", "R": "R, random"}
        rows = []
        for r in ("J", "F", "K", "R"):
            x = s5["rules"][r]
            def f(k, x=x):
                c = x[k]
                return f"{100 * c['share']:.1f} ({100 * c['lo']:.1f}--{100 * c['hi']:.1f})"
            rows.append(f"{names[r]} & {f('outcome:abstain')} & {f('outcome:correct')} & {f('outcome:wrong')} & "
                        f"{100 * x['outcome:unparsed']['share']:.1f} \\\\")
        (OUT / "tab_selection.tex").write_text("\n".join(rows) + "\n")
    p = ROOT / "results/explore_idk2/summary.json"
    if p.exists():
        s = json.loads(p.read_text())
        rows = []
        for j in SIX:
            cs = [cell(s, j, "judge knows", pr) for pr in ("CW-IDK", "CW-IDK2", "CC-IDK", "CC-IDK2")]
            if all(cs):
                rows.append(f"{NAMES[j]} & " + " & ".join(f"{100 * c['rate']:.0f} ({100 * c['lo']:.0f}--{100 * c['hi']:.0f})" for c in cs) + " \\\\")
        (OUT / "tab_idk2.tex").write_text("\n".join(rows) + "\n")


def form_abstract() -> None:
    """The abstract of main.tex as plain text with the macros filled in, for the submission form."""
    import re
    src = (OUT / "main.tex").read_text()
    m = re.search(r"\\begin\{apartabstract\}(.*?)\\end\{apartabstract\}", src, re.S)
    if not m:
        return
    txt = m.group(1).strip()
    for k in sorted(macros, key=len, reverse=True):
        txt = txt.replace("\\" + k + "{}", macros[k]).replace("\\" + k, macros[k])
    txt = txt.replace("\\%", "%").replace("``", '"').replace("\'\'", '"').replace("{,}", ",")
    txt = re.sub(r"\\(?:emph|textit|textbf)\{([^{}]*)\}", r"\1", txt)   # plain text for the form
    txt = re.sub(r"\$([^$]*)\$", r"\1", txt).replace("\\,", " ")
    assert "\\" not in txt and "{" not in txt, txt
    txt = re.sub(r"\s+", " ", txt)
    (OUT / "abstract_for_form.txt").write_text(txt + "\n")
    readme = ROOT / "README.md"   # the summary in the README is the same text
    if readme.exists():
        r = readme.read_text()
        a, b = "<!-- abstract:start -->", "<!-- abstract:end -->"
        if a in r and b in r:
            readme.write_text(r[:r.index(a) + len(a)] + "\n" + txt + "\n" + r[r.index(b):])
    put("abstractWords", str(len(txt.split())))


def large() -> None:
    """Amendment 4, part A: two larger judges (results/large/summary.json from src/large_judges.py)."""
    f = ROOT / "results/large/summary.json"
    if not f.exists():
        return
    s = json.loads(f.read_text())
    names = {"adaption/qwen3.5-397b": "Qwen 3.5 397B", "adaption/glm-5.2": "GLM 5.2"}
    c, fr, t = s["confirm"], s["free"], s["tests"]
    put("lgNames", " and ".join(names[j] for j in names if j in c))
    for key, src, fld in (("lgB", c, "b"), ("lgCtrl", c, "control"), ("lgFfB", fr, "b_short"),
                          ("lgFfCtrl", fr, "control"), ("lgFfFull", fr, "b_full")):
        xs = [src[j][fld]["rate"] for j in names if j in src and fld in src[j]]
        if xs:
            rng_put(key, xs)
    for j, k in names.items():
        if j in c:
            put("lgB" + k.split()[0].replace(".", ""), pct(c[j]["b"]["rate"]))
        if j in fr and "b_short" in fr[j]:
            put("lgFfB" + k.split()[0].replace(".", ""), pct(fr[j]["b_short"]["rate"]))
    rng_put("lgAcc", [c[j]["own_accuracy"] for j in names if j in c])
    rule = [c[j]["rule"]["b"] for j in names if j in c and "rule" in c[j]]
    if rule:
        rng_put("lgRuleB", rule)
        rng_put("lgRuleA", [c[j]["rule"]["a"] for j in names if j in c and "rule" in c[j]])
    for lab in ("One", "Two", "Three"):
        k = {"One": "L1", "Two": "L2", "Three": "L3"}[lab]
        put(f"lgL{lab}Outcome", "holds" if t[k + "_holds"] else "fails")
        put(f"lgL{lab}Pass", WORDS[t[k + "_pass"]])
    put("lgFfAbove", WORDS[sum(fr[j]["b_short"]["rate"] > 0.5 for j in names if j in fr and "b_short" in fr[j])])


def reward_models() -> None:
    """Amendment 4, part B: three reward models (results/reward_models/summary.json from src/rm_analyze.py)."""
    f = ROOT / "results/reward_models/summary.json"
    if not f.exists():
        return
    s = json.loads(f.read_text())
    short = {"Skywork/Skywork-Reward-V2-Llama-3.1-8B": "Skywork V2 Llama 8B",
             "Skywork/Skywork-Reward-V2-Qwen3-8B": "Skywork V2 Qwen3 8B",
             "allenai/Llama-3.1-Tulu-3-8B-RM": "Tulu 3 8B RM"}
    ms = s["models"]
    for st, key in (("mcq", "rmMc"), ("free", "rmFf")):
        for fld, k2 in (("b", "B"), ("b_separated", "BSep"), ("control", "Ctrl"), ("separated", "Sep"), ("a", "A"),
                        ("b_full", "Full")):
            xs = [ms[m][st][fld]["rate"] if isinstance(ms[m][st][fld], dict) else ms[m][st][fld] for m in ms]
            rng_put(key + k2, xs)
        put(key + "Above", WORDS[sum(ms[m][st]["b_separated"]["rate"] > 0.5 for m in ms)])
    t = s["tests"]
    for k, lab in (("R1", "rmROne"), ("R2", "rmRTwo")):
        put(lab + "Outcome", "holds" if t[k]["holds"] else "fails")
        put(lab + "Pass", WORDS[t[k]["passes"]])
    put("rmCount", WORDS[len(ms)])
    sens = ROOT / "results/reward_models/sensitivity_tulu_bos.jsonl"   # unregistered check, start token added
    if sens.exists():
        from collections import defaultdict
        d: dict = defaultdict(dict)
        for ln in sens.read_text().splitlines():
            r = json.loads(ln)
            d[(r["set"], r["item"])][r["resp"]] = r["score"]
        for st, key in (("mcq", "Mc"), ("free", "Ff")):
            sep = [v for (s_, _), v in d.items() if s_ == st and v["CC"] > v["CW"]]
            put("rmBos" + key, pct(sum((v["CW"] > v["IDK"]) + 0.5 * (v["CW"] == v["IDK"]) for v in sep) / len(sep)))
        tulu = ms.get("allenai/Llama-3.1-Tulu-3-8B-RM")
        if tulu:
            put("rmTuluMc", pct(tulu["mcq"]["b_separated"]["rate"]))
            put("rmTuluFf", pct(tulu["free"]["b_separated"]["rate"]))
    rows = []
    for m in ms:
        cells = [short.get(m, m)]
        for st in ("mcq", "free"):
            r = ms[m][st]
            for fld in ("b", "b_separated", "control"):
                c = r[fld]
                cells.append(f"{100 * c['rate']:.0f} ({100 * c['lo']:.0f}--{100 * c['hi']:.0f})")
        rows.append(" & ".join(cells) + " \\\\")
    (OUT / "tab_rm.tex").write_text("\n".join(rows) + "\n")


def figure_numbers() -> None:
    """Numbers shown in figures 3 and 4, computed by the same functions that draw them."""
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from fig_a import fixes_rows, guess_stats  # noqa: E402

    def load(rel: str):
        f = ROOT / rel
        return json.loads(f.read_text()) if f.exists() else None

    s1 = load("results/study1/summary.json")
    g = guess_stats(s1)
    judges = g[2:]
    put("guessWMin", pct(min(w for _, w, _ in judges)))
    put("guessWMax", pct(max(w for _, w, _ in judges)))
    put("guessEloMin", f"{min(e for _, _, e in judges):.0f}")
    put("guessEloMax", f"{max(e for _, _, e in judges):.0f}")
    put("guessEloRule", f"{abs(g[0][2]):.0f}")
    put("guessEloAcc", f"{g[1][2]:.0f}")
    confirm = load("results/confirm2/confirm.json")
    s4 = load("results/study4/summary.json")
    if not (confirm and s4):
        return
    rows = fixes_rows(s4, load("results/study4/reasoning.json"), load("results/study4/mtbench.json"),
                      load("results/explore_idk2/summary.json"), confirm)
    instr = [r for r in rows if r["group"] == "Instruction" and r["label"] != "Default instruction"]
    put("instrBelowMax", WORDS[max(sum(v < 0.5 for v in r["b"] if v is not None) for r in instr)])
    vtc = rows[-1]
    put("vtcBelow", WORDS[sum(v < 0.5 for v in vtc["b"])])


def main() -> None:
    study1()
    study3()
    study4()
    study5()
    reruns()
    confirm2()
    freeform()
    figure_numbers()
    large()
    reward_models()
    appendix()
    form_abstract()
    lines = [f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in sorted(macros.items())]
    (OUT / "numbers.tex").write_text("% generated by src/numbers_a.py, do not edit\n" + "\n".join(lines) + "\n")
    print(f"{len(lines)} macros written")


if __name__ == "__main__":
    main()
