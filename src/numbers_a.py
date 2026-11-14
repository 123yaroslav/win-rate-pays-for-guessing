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
    p2 = ROOT / "results/study3b/summary.json"
    if p2.exists():
        b = json.loads(p2.read_text())
        for reg, name in (("IDK", "privIdk"), ("FACT", "privFact")):
            c = b.get(reg, {})
            put(f"{name}Rows", str(c.get("n", 0)))
            put(f"{name}Different", str(c.get("DIFFERENT", 0)))
            put(f"{name}Same", str(c.get("SAME", 0)))
            put(f"{name}Abstain", str(c.get("ABSTAIN", 0)))
            put(f"{name}Disagree", str(c.get("disagree", 0)))
        ev = ROOT / "results/study3b/evaluation.json"
        if ev.exists():
            q2 = json.loads(ev.read_text()).get("quality", {})
            if q2.get("grade_before"):
                put("privGradeBefore", str(q2["grade_before"]))
                put("privGradeAfter", str(q2["grade_after"]))
                put("privScoreBefore", f"{q2['score_before']:.1f}")
                put("privScoreAfter", f"{q2['score_after']:.1f}")


def main() -> None:
    study1()
    study3()
    lines = [f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in sorted(macros.items())]
    (OUT / "numbers.tex").write_text("% generated by src/numbers_a.py, do not edit\n" + "\n".join(lines) + "\n")
    print(f"{len(lines)} macros written")


if __name__ == "__main__":
    main()
