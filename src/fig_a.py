"""Figures for paper A from results/study1/summary.json and results/study4/summary.json.

    python src/fig_a.py --style src/paper.mplstyle
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
NAMES = {
    "adaption/deepseek-v4-flash": "DeepSeek V4 Flash",
    "adaption/gemma-4-31b-it": "Gemma 4 31B",
    "adaption/qwen3.8-27b": "Qwen 3.8 27B",
    "openrouter/anthropic/claude-haiku-5.5": "Claude Haiku 5.5",
    "openrouter/openai/gpt-5.6-luna": "GPT-5.6 Luna",
    "openrouter/mistralai/mistral-small-2603": "Mistral Small 2603",
    "openrouter/openai/gpt-5.6-terra": "GPT-5.6 Terra*",
}
BLUE, ORANGE, GREEN, GREY = "#0072B2", "#D55E00", "#009E73", "#777777"


def cell(summary: dict, judge: str, group: str, pair: str, variant: str = "default") -> dict | None:
    return summary["judges"].get(judge, {}).get("variants", {}).get(variant, {}).get("groups", {}).get(group, {}).get(pair)


def fig1(s1: dict, out: Path, confirm: dict | None = None, free: dict | None = None) -> None:
    """The same contrast in three settings, and what it means for win rate.

    Panels a to c: share of duels won by the wrong answer on questions the judge answers correctly itself,
    against the right answer (blue) and against "I don't know" (orange). Panel d: the lines W(p).
    """
    judges = [j for j in NAMES if j in s1["judges"] and "terra" not in j]   # the six registered judges
    fig, axes = plt.subplots(1, 4, figsize=(6.5, 2.55), gridspec_kw={"width_ratios": [1, 1, 1, 1.2], "wspace": 0.12})
    ys = list(range(len(judges)))[::-1]

    def points(ax, get) -> None:
        for y, j in zip(ys, judges):
            for kind, col, mk, dy, hollow in (("right", BLUE, "o", 0.2, False), ("idk", ORANGE, "s", -0.1, False),
                                              ("full", ORANGE, "s", -0.34, True)):
                c = get(j, kind)
                if not c:
                    continue
                ax.errorbar(c["rate"], y + dy, xerr=[[max(0, c["rate"] - c["lo"])], [max(0, c["hi"] - c["rate"])]],
                            fmt=mk, color=col, mfc="white" if hollow else col, ms=3.8, lw=0.9, capsize=1.6)
        ax.axvline(0.5, color=GREY, lw=0.8, ls=":")
        ax.set_xlim(-0.04, 1.04)
        ax.set_ylim(-0.6, len(judges) - 0.4)
        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(["0", "50%", "100%"], fontsize=7.5)
        ax.set_yticks(ys)

    def from_s1(j, kind):
        return None if kind == "full" else cell(s1, j, "judge knows", "CW-CC" if kind == "right" else "CW-IDK")

    def from_confirm(j, kind):
        r = (confirm or {}).get("judges", {}).get(j)
        return None if not r or kind == "full" else r["control" if kind == "right" else "b"]

    def from_free(j, kind):
        r = (free or {}).get("judges", {}).get(j)
        return None if not r else r.get({"right": "control", "idk": "b_short", "full": "b_full"}[kind])

    titles = [("a", "Registered study", "multiple choice, 300"),
              ("b", "Fresh questions", "multiple choice, 150"),
              ("c", "Free-form questions", "two-sentence replies, 100")]
    for ax, get, (letter, t1, t2) in zip(axes[:3], (from_s1, from_confirm, from_free), titles):
        points(ax, get)
        ax.set_title(f"$\\mathbf{{{letter}}}$  {t1}\n{t2}", loc="left", fontsize=6.8, fontweight="normal",
                     linespacing=1.2)
    axes[0].set_yticklabels([NAMES[j] for j in judges], fontsize=7.5)
    for ax in axes[1:3]:
        ax.set_yticklabels([])
        ax.tick_params(axis="y", length=0)
    axes[1].set_xlabel("Duels won by the wrong answer, on questions the judge answers correctly itself", fontsize=7.5)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], marker="o", color=BLUE, ls="", ms=4, label="against the right answer"),
               Line2D([], [], marker="s", color=ORANGE, ls="", ms=4, label="against \"I don't know\"")]
    if free:
        handles.append(Line2D([], [], marker="s", color=ORANGE, mfc="white", ls="", ms=4,
                              label="against a fuller abstention"))
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.115, -0.115), ncol=3, fontsize=7, frameon=False,
               handletextpad=0.2, columnspacing=1.2)

    # panel d: win rate of a policy that always answers, against one that abstains
    bx = axes[3]
    xs = [0, 1]
    bx.fill_between(xs, 0.5, 1.0, color="#f3f3f3", lw=0)
    bx.plot(xs, [0, 1], color="black", lw=1, ls="--", label="right +1, wrong $-$1")
    bx.plot(xs, [0.5, 1], color="black", lw=1, ls=":", label="accuracy grading")
    lows = []
    for j in judges:
        a, b = cell(s1, j, "all", "CC-IDK"), cell(s1, j, "all", "CW-IDK")
        if not a or not b:
            continue
        bx.plot(xs, [b["rate"], a["rate"]], color=ORANGE, lw=1.1, alpha=0.85)
        lows.append(b["rate"])
    bx.axhline(0.5, color=GREY, lw=0.8)
    bx.set_xlim(0, 1)
    bx.set_ylim(0, 1.02)
    bx.set_xticks([0, 0.5, 1])
    bx.set_xticklabels(["0", "50%", "100%"], fontsize=7.5)
    bx.set_yticks([0, 0.5, 1])
    bx.set_yticklabels(["0%", "50%", "100%"], fontsize=7.5)
    bx.yaxis.tick_right()
    bx.yaxis.set_label_position("right")
    bx.set_xlabel("Accuracy of a policy\nthat always answers", fontsize=7.5)
    bx.set_ylabel("Its win rate against\na policy that abstains", fontsize=7.5)
    if lows:
        bx.annotate("LLM judges", xy=(0.10, min(lows) + 0.02), xytext=(0.47, 0.30), color=ORANGE, fontsize=7,
                    ha="left", va="center", arrowprops={"arrowstyle": "-", "color": ORANGE, "lw": 0.7})
    bx.legend(loc="lower right", fontsize=6, frameon=False, handlelength=1.6, borderaxespad=0.2)
    bx.set_title("$\\mathbf{d}$  What the two rates\nmean for win rate", loc="left", fontsize=6.8,
                 fontweight="normal", linespacing=1.2)
    for ext in ("pdf", "png"):
        fig.savefig(out / f"fig1_core.{ext}")
    plt.close(fig)


def fig_fix(s4: dict, s1: dict, out: Path) -> None:
    variants = [("default", "default"), ("data", "data curation"), ("selfcheck", "own answer shown"),
                ("stakes", "stakes"), ("accuracy", "accuracy first"), ("cot", "written reasoning"),
                ("think", "reasoning mode")]
    judges = [j for j in NAMES if j in s4["judges"]]
    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.6), sharey=True)
    cols = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#000000"]
    for ax, group, title in ((axes[0], "judge knows", "Questions the judge answers correctly"),
                             (axes[1], "judge does not know", "Questions the judge answers wrongly")):
        for k, j in enumerate(judges):
            xs, bs = [], []
            for x, (v, _) in enumerate(variants):
                src = s1 if v == "default" else s4
                c = cell(src, j, group, "CW-IDK", v)
                if c:
                    xs.append(x)
                    bs.append(c["rate"])
            ax.plot(xs, bs, marker="o", ms=3.5, lw=0.9, color=cols[k % len(cols)], label=NAMES[j], alpha=0.9)
        ax.axhline(0.5, color=GREY, lw=0.8, ls=":")
        ax.set_xticks(range(len(variants)))
        ax.set_xticklabels([n for _, n in variants], rotation=30, ha="right")
        ax.set_ylim(0, 1.02)
        ax.set_yticks([0, 0.5, 1])
        ax.set_yticklabels(["0%", "50%", "100%"])
        ax.set_title(title, loc="left", fontsize=8.5, fontweight="normal")
    axes[0].set_ylabel("Wrong answer beats\n\"I don't know\" (b)")
    axes[1].legend(loc="lower left", fontsize=7, ncol=1)
    for ext in ("pdf", "png"):
        fig.savefig(out / f"fig_fix.{ext}")
    plt.close(fig)


def fig_map(s4: dict, reasoning: dict | None, idk2: dict | None, out: Path) -> None:
    """b on questions the judge knows, for every judge and condition. Darker means the wrong answer wins more."""
    judges = [j for j in NAMES if j in s4["judges"] and "terra" not in j]
    rep = s4.get("repair", {})
    rows = [("Default instruction", "default"), ("Data-curation framing", "data"), ("Own answer shown", "selfcheck"),
            ("Stakes", "stakes"), ("Accuracy first", "accuracy"), ("Written rationale", "cot")]
    grid, marks, labels = [], [], []
    for lab, v in rows:
        vals, mk = [], []
        for j in judges:
            r = rep.get(f"{j}|{v}")
            vr = s4["judges"][j]["variants"].get(v, {})
            cut = vr.get("unparsed", {}).get("CW-IDK", 0) / (2 * (90 if v == "cot" else 150))
            vals.append(None if not r else ("cut" if cut > 0.5 else r["b_knows"]))
            mk.append(bool(r and r["repaired"] and v not in ("default", "data") and cut <= 0.5))
        grid.append(vals)
        marks.append(mk)
        labels.append(lab)
    if reasoning:
        vals = []
        for j in judges:
            c = None
            for key_ in ("think|" + j, "reason|" + j):
                x = reasoning.get(key_)
                if x and x.get("b_reasoned") and x["share_reasoned"] > 0.2 and c is None:
                    c = x["b_reasoned"]["rate"]
            vals.append(c)
        grid.append(vals)
        marks.append([False] * len(judges))
        labels.append("Reasoning mode, calls that reasoned")
    mp = ROOT / "results/study4/mtbench.json"
    if mp.exists():
        mb = json.loads(mp.read_text())
        vals = []
        for j in judges:
            c = cell(mb, j, "judge knows", "CW-IDK", "mtbench")
            vr = mb["judges"].get(j, {}).get("variants", {}).get("mtbench", {})
            cut = vr.get("unparsed", {}).get("CW-IDK", 0) / (2 * mb["n_items"]) if vr else 0
            vals.append(None if not c else ("cut" if cut > 0.5 else c["rate"]))
        grid.append(vals)
        marks.append([False] * len(judges))
        labels.append("Published judge prompt (MT-Bench)")
    if idk2:
        vals = []
        for j in judges:
            c = cell(idk2, j, "judge knows", "CW-IDK2")
            vals.append(None if not c else c["rate"])
        grid.append(vals)
        marks.append([False] * len(judges))
        labels.append("Fuller abstention")
    fig, ax = plt.subplots(figsize=(6.5, 2.8))
    cmap = plt.get_cmap("Oranges")
    for y, vals in enumerate(grid):
        for x, v in enumerate(vals):
            if v is None or v == "cut":
                ax.text(x, y, "not run" if v is None else "replies cut", ha="center", va="center", fontsize=6.5,
                        color="#999999")
                continue
            ax.add_patch(plt.Rectangle((x - 0.5, y - 0.5), 1, 1, color=cmap(0.08 + 0.72 * v), lw=0))
            ax.text(x, y, f"{100 * v:.0f}", ha="center", va="center", fontsize=8,
                    color="white" if v > 0.62 else "#222222", fontweight="bold" if marks[y][x] else "normal")
            if marks[y][x]:
                ax.add_patch(plt.Rectangle((x - 0.47, y - 0.44), 0.94, 0.88, fill=False, ec="#0072B2", lw=1.3))
    ax.set_xlim(-0.5, len(judges) - 0.5)
    ax.set_ylim(len(grid) - 0.5, -0.5)
    ax.set_xticks(range(len(judges)))
    ax.set_xticklabels([NAMES[j].replace(" V4 Flash", "\nV4 Flash").replace(" 4 31B", "\n4 31B").replace(" 3.8 27B", "\n3.8 27B")
                        .replace(" Haiku 5.5", "\nHaiku 5.5").replace(" Luna", "\nLuna").replace(" Small 2603", "\nSmall 2603")
                        for j in judges], fontsize=7.5)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(grid)))
    ax.set_yticklabels(labels, fontsize=8)
    ax.tick_params(length=0)
    for sp in ax.spines.values():
        sp.set_visible(False)
    for ext in ("pdf", "png"):
        fig.savefig(out / f"fig2_map.{ext}")
    plt.close(fig)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", default="")
    ap.add_argument("--s1", default="results/study1/summary.json")
    ap.add_argument("--s4", default="results/study4/summary.json")
    ap.add_argument("--out", default="paper_A/figs")
    a = ap.parse_args()
    if a.style:
        plt.style.use(str(Path(a.style).expanduser()))
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    s1 = json.loads((ROOT / a.s1).read_text())
    tp = ROOT / "results/study4/reasoning.json"
    cp, fp = ROOT / "results/confirm2/confirm.json", ROOT / "results/freeform/summary.json"
    fig1(s1, out, json.loads(cp.read_text()) if cp.exists() else None,
         json.loads(fp.read_text()) if fp.exists() else None)
    if (ROOT / a.s4).exists():
        s4 = json.loads((ROOT / a.s4).read_text())
        fig_fix(s4, s1, out)
        ip = ROOT / "results/explore_idk2/summary.json"
        fig_map(s4, json.loads(tp.read_text()) if tp.exists() else None,
                json.loads(ip.read_text()) if ip.exists() else None, out)
    print("figures written to", out)


if __name__ == "__main__":
    main()
