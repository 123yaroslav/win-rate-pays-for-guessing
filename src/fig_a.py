"""Figures for paper A.

    python src/fig_a.py --style src/paper.mplstyle

fig1_bluff      the bluff rate of each judge next to two rule-based graders, with the equal-wording control
fig2_replicate  the same contrast on the registered study, fresh questions and free-form questions
fig3_guess      what a model gains on a leaderboard by guessing instead of abstaining
fig4_fixes      what lowers the bluff rate, and what each change costs in right answers
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
NAMES = {
    "adaption/deepseek-v4-flash": "DeepSeek V4 Flash",
    "openrouter/mistralai/mistral-small-2603": "Mistral Small 2603",
    "openrouter/openai/gpt-5.6-luna": "GPT-5.6 Luna",
    "openrouter/anthropic/claude-haiku-5.5": "Claude Haiku 5.5",
    "adaption/qwen3.8-27b": "Qwen 3.8 27B",
    "adaption/gemma-4-31b-it": "Gemma 4 31B",
}
LARGE = {"adaption/qwen3.5-397b": "Qwen 3.5 397B", "adaption/glm-5.2": "GLM 5.2"}
SIX = list(NAMES)   # fixed order in every figure: registered bluff rate, highest first
BLUE, ORANGE, GREEN, GREY, INK = "#0072B2", "#D55E00", "#009E73", "#8a8a8a", "#222222"
PAYS = "#fbeee6"    # shade of the region where guessing pays


def cell(summary: dict, judge: str, group: str, pair: str, variant: str = "default") -> dict | None:
    return summary["judges"].get(judge, {}).get("variants", {}).get(variant, {}).get("groups", {}).get(group, {}).get(pair)


def load(p: str) -> dict | None:
    f = ROOT / p
    return json.loads(f.read_text()) if f.exists() else None


def err(c: dict) -> list[list[float]]:
    return [[max(0.0, c["rate"] - c["lo"])], [max(0.0, c["hi"] - c["rate"])]]


def pct_axis(ax, label: str | None = None) -> None:
    ax.set_xlim(-0.02, 1.02)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"])
    if label:
        ax.set_xlabel(label)


def save(fig, out: Path, name: str) -> None:
    for ext in ("pdf", "png"):
        fig.savefig(out / f"{name}.{ext}")
    plt.close(fig)


# ---------------------------------------------------------------------------------------------
def fig1(s1: dict, out: Path) -> None:
    """Bluff rate per judge on the questions it knows, the control, and two rule-based graders."""
    fig, ax = plt.subplots(figsize=(6.5, 2.3))
    rows = [("Penalty grader (+1, \u22121, 0)", "rule0"), ("Accuracy grader (+1, 0, 0)", "rule50")]
    rows += [(NAMES[j], j) for j in SIX]
    n = len(rows)
    ys = {key: n - 1 - i - (0.45 if i >= 2 else 0) for i, (_, key) in enumerate(rows)}
    ax.axvline(0.5, color=GREY, lw=0.8, ls=(0, (2, 2)), zorder=1)
    ax.text(0.76, n + 0.55, "guessing pays", ha="center", va="center", fontsize=8, color=ORANGE, fontweight="bold")
    ax.text(0.25, n + 0.55, "honesty pays", ha="center", va="center", fontsize=8, color="#555555", fontweight="bold")
    # rule-based graders: what a wrong answer gets against an abstention
    for key, x in (("rule0", 0.0), ("rule50", 0.5)):
        ax.plot([x], [ys[key]], marker="D", color=INK, ms=5, zorder=4, clip_on=False)
        ax.text(x + 0.025, ys[key], "0%" if x == 0 else "50% (a tie)", va="center", fontsize=7.5, color=INK)
    # judges
    for j in SIX:
        y = ys[j]
        b, c = cell(s1, j, "judge knows", "CW-IDK"), cell(s1, j, "judge knows", "CW-CC")
        ax.plot([c["rate"], b["rate"]], [y, y], color="#d9d9d9", lw=0.8, ls=(0, (1, 1.5)), zorder=2)
        ax.errorbar(c["rate"], y, xerr=err(c), fmt="o", color=BLUE, ms=5.2, lw=0.9, capsize=0, zorder=3)
        ax.errorbar(b["rate"], y, xerr=err(b), fmt="s", color=ORANGE, ms=5.2, lw=0.9, capsize=0, zorder=3)
        ax.text(b["hi"] + 0.02, y, f"{100 * b['rate']:.0f}%", va="center", fontsize=7.5, color=ORANGE,
                fontweight="bold")
    top = ys[SIX[0]]
    c0, b0 = cell(s1, SIX[0], "judge knows", "CW-CC"), cell(s1, SIX[0], "judge knows", "CW-IDK")
    ax.text(c0["rate"], top + 0.42, "against the right answer", fontsize=7.5, color=BLUE, ha="left", va="bottom")
    ax.text(b0["rate"], top + 0.42, "against \u201cI don't know\u201d", fontsize=7.5, color=ORANGE, ha="right",
            va="bottom")
    ax.axhline(ys["rule50"] - 0.55, color="#dddddd", lw=0.6)
    # leaderboard consequence, same rows: Elo gap from guessing on a fifth of the questions (fig3 numbers)
    for (lab, key), (_, _, e) in zip(rows, guess_stats(s1)):
        ax.text(1.2, ys[key], f"{e:+.0f}".replace("-", "\u2212"), va="center", ha="right", fontsize=8,
                color=ORANGE if key not in ("rule0", "rule50") else INK,
                fontweight="bold" if key not in ("rule0", "rule50") else "normal")
    ax.text(1.2, n + 0.55, "Elo from\nguessing", ha="right", va="center", fontsize=7.2, color="#555555",
            linespacing=1.05)
    ax.set_yticks([ys[k] for _, k in rows])
    ax.set_yticklabels([lab for lab, _ in rows])
    for t in ax.get_yticklabels()[:2]:
        t.set_color("#555555")
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_ylim(-0.75, n + 0.95)
    pct_axis(ax, "Share of duels the wrong answer wins, on questions the judge answers correctly itself")
    ax.set_xlim(-0.02, 1.21)
    ax.spines["bottom"].set_bounds(0, 1)
    ax.axvspan(0.5, 1.0, color=PAYS, lw=0, zorder=0)
    save(fig, out, "fig1_bluff")


# ---------------------------------------------------------------------------------------------
def fig2(s1: dict, confirm: dict, free: dict, large: dict | None, out: Path) -> None:
    """The bluff rate and the control on three registered question sets."""
    judges = SIX + ([j for j in LARGE if large and j in large.get("confirm", {})] if large else [])
    fig, axes = plt.subplots(1, 3, figsize=(6.5, 2.3 + 0.26 * (len(judges) - 6)), sharey=True)
    pos = {j: -i - (0.6 if j in LARGE else 0) for i, j in enumerate(judges)}

    def get(src: str, j: str, kind: str) -> dict | None:
        if j in LARGE:
            r = (large or {}).get("confirm" if src == "fresh" else "free", {}).get(j)
            if src == "s1" or not r:
                return None
            return r["b" if kind == "b" else "control"] if src == "fresh" else r["b_short" if kind == "b" else "control"]
        if src == "s1":
            return cell(s1, j, "judge knows", "CW-IDK" if kind == "b" else "CW-CC")
        if src == "fresh":
            r = confirm["judges"].get(j)
            return r and r["b" if kind == "b" else "control"]
        r = free["judges"].get(j)
        return r and r.get("b_short" if kind == "b" else "control")

    titles = ["$\\mathbf{a}$  Registered study\n300 multiple-choice questions",
              "$\\mathbf{b}$  Registered confirmation\n150 fresh questions",
              "$\\mathbf{c}$  Registered free-form check\n100 questions, two-sentence replies"]
    for ax, src, title in zip(axes, ("s1", "fresh", "free"), titles):
        ax.axvspan(0.5, 1.02, color=PAYS, lw=0, zorder=0)
        ax.axvline(0.5, color=GREY, lw=0.8, ls=(0, (2, 2)), zorder=1)
        for j in judges:
            b, c = get(src, j, "b"), get(src, j, "c")
            y = pos[j]
            if not b:
                ax.text(0.5, y, "not run", ha="center", va="center", fontsize=7, color=GREY)
                continue
            ax.plot([c["rate"], b["rate"]], [y, y], color="#d9d9d9", lw=0.7, ls=(0, (1, 1.5)), zorder=2)
            ax.errorbar(c["rate"], y, xerr=err(c), fmt="o", color=BLUE, ms=4.2, lw=0.8, zorder=3)
            ax.errorbar(b["rate"], y, xerr=err(b), fmt="s", color=ORANGE, ms=4.2, lw=0.8, zorder=3)
        ax.set_title(title, fontsize=7.8, fontweight="normal", linespacing=1.15)
        pct_axis(ax)
        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(["0", "50%", "100%"])
        ax.tick_params(axis="y", length=0)
    axes[0].set_yticks([pos[j] for j in judges])
    axes[0].set_yticklabels([NAMES.get(j) or LARGE[j] + "\u2020" for j in judges])
    axes[0].set_ylim(min(pos.values()) - 0.6, 0.6)
    axes[1].set_xlabel("Share of duels the wrong answer wins, on questions the judge answers correctly itself")
    handles = [Line2D([], [], marker="s", color=ORANGE, ls="", ms=5, label="against \u201cI don't know\u201d"),
               Line2D([], [], marker="o", color=BLUE, ls="", ms=5, label="against the right answer in the same words")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.55, 1.0), ncol=2, frameon=False)
    save(fig, out, "fig2_replicate")


# ---------------------------------------------------------------------------------------------
def guess_stats(s1: dict) -> list[tuple[str, float, float]]:
    """Win rate of a model that guesses among four options against one that says "I don't know", and the Elo
    difference when two models differ only on the fifth of questions that neither knows (ties elsewhere)."""
    def elo(w: float) -> float:
        o = 0.8 * 0.5 + 0.2 * w
        return 400 * math.log10(o / (1 - o))
    rows = [("Penalty grader (+1, \u22121, 0)", 0.25, elo(0.25)),
            ("Accuracy grader (+1, 0, 0)", 0.25 + 0.75 * 0.5, elo(0.625))]
    for j in SIX:
        a, b = cell(s1, j, "all", "CC-IDK")["rate"], cell(s1, j, "all", "CW-IDK")["rate"]
        w = b + 0.25 * (a - b)
        rows.append((NAMES[j], w, elo(w)))
    return rows


def fig3(s1: dict, out: Path) -> None:
    rows = guess_stats(s1)
    fig, ax = plt.subplots(figsize=(6.5, 2.0))
    n = len(rows)
    ys = [n - 1 - i - (0.45 if i >= 2 else 0) for i in range(n)]
    for i, ((lab, w, e), y) in enumerate(zip(rows, ys)):
        col = "#9a9a9a" if i < 2 else ORANGE
        ax.barh(y, w, height=0.62, color=col, lw=0, zorder=2)
        ax.text(w + 0.012, y, "62.5%" if abs(w - 0.625) < 1e-9 else f"{100 * w:.0f}%", va="center", fontsize=7.5,
                color=INK)
        ax.text(1.17, y, f"{e:+.0f}".replace("-", "−"), va="center", ha="right", fontsize=8, color=INK if i < 2 else ORANGE,
                fontweight="bold" if i >= 2 else "normal")
    ax.text(1.17, n - 0.3, "Elo gap if the models differ\nonly on 20% of questions", ha="right", va="bottom",
            fontsize=7.2, color="#555555", linespacing=1.05)
    ax.axvline(0.5, color=INK, lw=0.8, ls=(0, (2, 2)), zorder=3)
    ax.text(0.505, n - 0.3, "even", ha="left", va="bottom", fontsize=7.5, color="#555555")
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows])
    for t in ax.get_yticklabels()[:2]:
        t.set_color("#555555")
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlim(0, 1.18)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"])
    ax.spines["bottom"].set_bounds(0, 1)
    ax.set_ylim(-0.75, n + 0.55)
    ax.set_xlabel("Computed win rate of a model that always guesses (right 1 time in 4) against one that says \u201cI don't know\u201d")
    save(fig, out, "fig3_guess")


# ---------------------------------------------------------------------------------------------
def fixes_rows(s4: dict, reasoning: dict | None, mb: dict | None, idk2: dict | None, confirm: dict) -> list[dict]:
    """One row per change to the judge: b and a per judge (None if not run or not usable)."""
    rep = s4.get("repair", {})

    def variant(v: str, cut_items: int) -> tuple[list, list]:
        bs, as_ = [], []
        for j in SIX:
            r = rep.get(f"{j}|{v}")
            vr = s4["judges"].get(j, {}).get("variants", {}).get(v, {})
            cut = vr.get("unparsed", {}).get("CW-IDK", 0) / (2 * cut_items)
            ok = r is not None and cut <= 0.5
            bs.append(r["b_knows"] if ok else None)
            as_.append(r["a_knows"] if ok else None)
        return bs, as_

    rows = []
    for lab, v, grp in (("Default instruction", "default", "Instruction"), ("Accuracy first", "accuracy", "Instruction"),
                        ("Stakes for the user", "stakes", "Instruction"), ("Judge's own answer shown", "selfcheck", "Instruction"),
                        ("Data-curation framing", "data", "Instruction"), ("Written rationale", "cot", "Explanation")):
        bs, as_ = variant(v, 90 if v == "cot" else 150)
        rows.append({"label": lab, "b": bs, "a": as_, "group": grp})
    if mb:
        bs, as_ = [], []
        for j in SIX:
            c, ca = cell(mb, j, "judge knows", "CW-IDK", "mtbench"), cell(mb, j, "judge knows", "CC-IDK", "mtbench")
            vr = mb["judges"].get(j, {}).get("variants", {}).get("mtbench", {})
            cut = vr.get("unparsed", {}).get("CW-IDK", 0) / (2 * mb["n_items"]) if vr else 0
            bs.append(c["rate"] if c and cut <= 0.5 else None)
            as_.append(ca["rate"] if ca and cut <= 0.5 else None)
        rows.append({"label": "Published judge prompt (MT-Bench)", "b": bs, "a": as_, "group": "Explanation"})
    if reasoning:
        bs, as_ = [], []
        for j in SIX:
            c = ca = None
            for k in ("think|" + j, "reason|" + j):
                x = reasoning.get(k)
                if x and x.get("b_reasoned") and x["share_reasoned"] > 0.2 and c is None:
                    c, ca = x["b_reasoned"]["rate"], (x.get("a_reasoned") or {}).get("rate")
            bs.append(c)
            as_.append(ca)
        rows.append({"label": "Reasoning mode (calls that reasoned)", "b": bs, "a": as_, "group": "Explanation"})
    if idk2:
        rows.append({"label": "Fuller abstention wording", "group": "Abstention",
                     "b": [(cell(idk2, j, "judge knows", "CW-IDK2") or {}).get("rate") for j in SIX],
                     "a": [(cell(idk2, j, "judge knows", "CC-IDK2") or {}).get("rate") for j in SIX]})
    rows.append({"label": "Verify-then-compare", "group": "Verification",
                 "b": [confirm["judges"][j]["rule"]["b"] for j in SIX],
                 "a": [confirm["judges"][j]["rule"]["a"] for j in SIX]})
    return rows


def fig4(rows: list[dict], out: Path) -> None:
    fig, ax = plt.subplots(figsize=(6.5, 2.45))
    n = len(rows)
    ys, y, prev = [], 0.0, None
    for r in rows:
        if prev is not None and r["group"] != prev:
            y -= 0.45
        ys.append(y)
        prev = r["group"]
        y -= 1
    ax.axvspan(0.5, 1.02, color=PAYS, lw=0, zorder=0)
    ax.axvline(0.5, color=GREY, lw=0.8, ls=(0, (2, 2)), zorder=1)
    for r, y in zip(rows, ys):
        vals = [v for v in r["b"] if v is not None]
        if vals:
            ax.plot([min(vals), max(vals)], [y, y], color="#d6d6d6", lw=1.6, zorder=2)
        for v in vals:
            ax.plot(v, y, "o", ms=4.6, color=ORANGE if v >= 0.5 else GREEN, mec="white", mew=0.5, zorder=3)
        below = sum(v < 0.5 for v in vals)
        ax.text(1.09, y, f"{below} of {len(vals)}", va="center", ha="center", fontsize=7.8,
                color=GREEN if below == len(vals) else INK, fontweight="bold" if below == len(vals) else "normal")
        as_ = [v for v in r["a"] if v is not None]
        if as_:
            lo, hi = min(as_), max(as_)
            txt = f"{100 * lo:.0f}%" if round(100 * lo) == round(100 * hi) else f"{100 * lo:.0f}\u2013{100 * hi:.0f}%"
            ax.text(1.34, y, txt, va="center", ha="center", fontsize=7.8, color=INK)
    hy = ys[0] + 0.75
    ax.text(1.09, hy, "judges\nbelow half", ha="center", va="bottom", fontsize=7.2, color="#555555", linespacing=1.05)
    ax.text(1.34, hy, "right answer still\nbeats \u201cI don't know\u201d", ha="center", va="bottom", fontsize=7.2,
            color="#555555", linespacing=1.05)
    ax.plot([0.03], [hy + 0.35], "o", ms=4.6, color=GREEN, mec="white", mew=0.5, clip_on=False)
    ax.text(0.055, hy + 0.35, "below one half", va="center", fontsize=7.2, color="#555555")
    ax.plot([0.53], [hy + 0.35], "o", ms=4.6, color=ORANGE, mec="white", mew=0.5, clip_on=False)
    ax.text(0.555, hy + 0.35, "one half or above", va="center", fontsize=7.2, color="#555555")
    ax.set_yticks(ys)
    ax.set_yticklabels([r["label"] for r in rows])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlim(-0.02, 1.45)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"])
    ax.spines["bottom"].set_bounds(0, 1)
    ax.set_ylim(min(ys) - 0.75, ys[0] + 1.25)
    ax.set_xlabel("Bluff rate: share of duels a wrong answer wins against \u201cI don't know\u201d", x=0.37)
    save(fig, out, "fig4_fixes")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", default="")
    ap.add_argument("--out", default="paper_A/figs")
    a = ap.parse_args()
    if a.style:
        plt.style.use(str(Path(a.style).expanduser()))
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    s1 = load("results/study1/summary.json")
    confirm, free = load("results/confirm2/confirm.json"), load("results/freeform/summary.json")
    large = load("results/large/summary.json")
    fig1(s1, out)
    fig2(s1, confirm, free, large, out)
    fig3(s1, out)
    s4 = load("results/study4/summary.json")
    rows = fixes_rows(s4, load("results/study4/reasoning.json"), load("results/study4/mtbench.json"),
                      load("results/explore_idk2/summary.json"), confirm)
    fig4(rows, out)
    print("figures written to", out)


if __name__ == "__main__":
    main()
