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
    bk, ba, wh, tone, acc = [], [], [], [], []
    for j in SIX + [TERRA]:
        if j not in s["judges"]:
            continue
        jr = s["judges"][j]
        c_bk, c_ba = cell(s, j, "judge knows", "CW-IDK"), cell(s, j, "all", "CW-IDK")
        c_ak = cell(s, j, "judge knows", "CC-IDK")
        c_wh = cell(s, j, "judge knows", "CW-HC")
        c_bu = cell(s, j, "judge does not know", "CW-IDK")
        c_hw = cell(s, j, "all", "HW-IDK")
        det = s.get("detection", {}).get(j)
        c_bf = cell(s, j, "judge flags the wrong answer as incorrect", "CW-IDK")
        star = "$^{*}$" if j == TERRA else ""
        det_txt = f"{100 * det['cw_flagged']:.0f}" if det else "--"
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
        if c_bu:
            put(f"bUnknown{k}", pct(c_bu["rate"]))
        if det:
            put(f"flagged{k}", pct(det["cw_flagged"]))
            put(f"accepted{k}", pct(det["cc_accepted"]))
        if c_bf:
            put(f"bFlagged{k}", pct(c_bf["rate"]))
            put(f"nFlagged{k}", str(c_bf["n"]))
        if j in SIX:
            acc.append(jr["own_accuracy"])
            if c_bk:
                bk.append(c_bk["rate"])
            if c_ba:
                ba.append(c_ba["rate"])
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
        put("accMin", pct(min(acc)))
        put("accMax", pct(max(acc)))
    if tone:
        put("toneMin", pct(min(tone)))
        put("toneMax", pct(max(tone)))
    dom, hw, fl, bf = [], [], [], []
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
        c = cell(s, j, "judge flags the wrong answer as incorrect", "CW-IDK")
        if c:
            bf.append(c["rate"])
    for name, xs in (("bDomain", dom), ("hwIdk", hw), ("flagged", fl), ("bFlagged", bf)):
        if xs:
            put(f"{name}Min", pct(min(xs)))
            put(f"{name}Max", pct(max(xs)))
    for lab in ("H1", "H1F", "S1g"):
        t = s.get("tests", {}).get(lab)
        if t:
            six = [j for j in SIX if j in t["holm_pass"]]
            name = {"H1": "hOne", "H1F": "hOneF", "S1g": "sOneG"}[lab]
            put(f"{name}Pass", str(sum(t["holm_pass"][j] for j in six)))
            put(f"{name}Judges", str(len(six)))
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
                    f"{c.get('abstain', 0)} & {c.get('hedged', 0)} \\\\")
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
            ("stakes", "Stakes"), ("accuracy", "Accuracy first"), ("cot", "Written reasoning"),
            ("think", "Reasoning mode")]


def study4() -> None:
    p = ROOT / "results/study4/summary.json"
    if not p.exists():
        return
    s = json.loads(p.read_text())
    rep = s.get("repair", {})
    judges = [j for j in SIX if j in s["judges"]]
    rows, repaired_by = [], {}
    for v, name in VARIANTS:
        cells = []
        for j in judges:
            r = rep.get(f"{j}|{v}")
            if not r:
                cells.append("--")
                continue
            mark = "$^{\\dagger}$" if r["repaired"] and v != "default" else ""
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
        put("natBMin", pct(min(bs)))
        put("natBMax", pct(max(bs)))
        put("natAMin", pct(min(as_)))
        put("natQuestions", str(n["used"]))
        put("natWrong", str(n["assert_wrong"]))
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
        (OUT / "eval_table_seen.txt").write_text("present")
    p = ROOT / "results/explore_idk2/summary.json"
    if p.exists():
        s = json.loads(p.read_text())
        b2 = [cell(s, j, "judge knows", "CW-IDK2") for j in SIX]
        b2 = [c["rate"] for c in b2 if c]
        if b2:
            put("idkTwoMin", pct(min(b2)))
            put("idkTwoMax", pct(max(b2)))
            put("idkTwoJudges", str(len(b2)))


def tex(s: str) -> str:
    rep = {"\\": "\\textbackslash{}", "&": "\\&", "%": "\\%", "$": "\\$", "#": "\\#", "_": "\\_", "{": "\\{",
           "}": "\\}", "~": "\\textasciitilde{}", "^": "\\textasciicircum{}", "<": "\\textless{}",
           ">": "\\textgreater{}"}
    out = "".join(rep.get(ch, ch) for ch in s)
    out = out.replace(' "', " ``").replace('"', "''")
    return out.replace("\n", " \\\\ ")


def appendix() -> None:
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    import duels
    blocks = [("Judge instruction, default", duels.JUDGE_SYSTEM["default"]),
              ("Judge instruction, accuracy first", duels.JUDGE_SYSTEM["accuracy"]),
              ("Judge instruction, stakes", duels.JUDGE_SYSTEM["stakes"]),
              ("Judge instruction, written reasoning", duels.JUDGE_SYSTEM["cot"]),
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
                blocks.append((f"Loop, style instruction {k}", final[k]))
    import adapt_analyze
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
        pairs = ["CC-IDK", "CW-IDK", "HC-IDK", "HW-IDK", "CW-HC", "CW-HW", "CC-HC"]
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
                rows.append(f"{NAMES[j]}{star} & {100 * v['cw_flagged']:.0f} & {100 * v['cc_accepted']:.0f} \\\\")
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


def main() -> None:
    study1()
    study3()
    study4()
    study5()
    appendix()
    lines = [f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in sorted(macros.items())]
    (OUT / "numbers.tex").write_text("% generated by src/numbers_a.py, do not edit\n" + "\n".join(lines) + "\n")
    print(f"{len(lines)} macros written")


if __name__ == "__main__":
    main()
