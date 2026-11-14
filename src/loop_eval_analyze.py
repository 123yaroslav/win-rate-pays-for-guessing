"""Study 5, evaluation by the key: tables for the trained models (predictions P5c and P5e).

Reads `results/study5/eval_<model>.jsonl`, written by `src/gpu_eval.py` on the GPU pod. Per model: abstention
rate, accuracy, wrong-answer rate, unparsed rate and penalised score (+1 right, -1 wrong or unparsed,
0 abstention), each with a 95% percentile bootstrap interval over the test questions. The bootstrap is paired:
every resample draws one list of questions and all models are scored on it. For the pairs J-K, F-K, J-F and J-R
it gives the difference, its interval and the share of resamples on the wrong side of zero.

Wrong side: where the pre-registration predicts a sign (P5c, P5e), the share of resamples in which the
difference is zero or has the other sign. Elsewhere no sign is predicted and the share is taken against the
sign of the observed difference, as a description.

    python src/loop_eval_analyze.py        # results/study5/eval_table.md and eval_table.json
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261115
CODES = {"correct": 0, "wrong": 1, "abstain": 2, "unparsed": 3}
LABELS = {
    "J": "J, judge, default instruction",
    "F": "F, judge, accuracy instruction",
    "K": "K, by the key",
    "R": "R, random",
    "base": "base model, no system prompt",
    "base_assert": "base model, assert instruction (reference)",
    "base_hedge": "base model, hedge instruction (reference)",
    "base_abstain": "base model, abstain instruction (reference)",
}
ORDER = list(LABELS)
METRICS = ["abstention_rate", "accuracy", "wrong_rate", "unparsed_rate", "penalised_score"]
DIFF_METRICS = ["abstention_rate", "wrong_rate", "accuracy", "penalised_score"]
NAMES = {"abstention_rate": "abstentions", "accuracy": "correct", "wrong_rate": "wrong",
         "unparsed_rate": "unparsed", "penalised_score": "penalised score"}
PHRASE = {"abstention_rate": "Abstention rate", "wrong_rate": "Wrong-answer rate", "penalised_score": "Penalised score"}
PAIRS = [("J", "K"), ("F", "K"), ("J", "F"), ("J", "R")]
# predicted sign of the difference first minus second: P5c for J-K, P5e (F between J and K) for F-K and J-F
PREDICTED = {
    ("J", "K"): {"abstention_rate": -1, "wrong_rate": +1, "penalised_score": -1},
    ("F", "K"): {"abstention_rate": -1, "penalised_score": -1},
    ("J", "F"): {"abstention_rate": -1, "penalised_score": -1},
}


def metrics(c: list[int]) -> dict[str, float]:
    """From the counts of correct, wrong, abstain, unparsed."""
    n = sum(c)
    return {"abstention_rate": c[2] / n, "accuracy": c[0] / n, "wrong_rate": c[1] / n,
            "unparsed_rate": c[3] / n, "penalised_score": (c[0] - c[1] - c[3]) / n}


def counts(codes: list[int], idx) -> list[int]:
    c = [0, 0, 0, 0]
    for i in idx:
        c[codes[i]] += 1
    return c


def interval(draws: list[float]) -> tuple[float, float]:
    s = sorted(draws)
    return s[int(0.025 * len(s))], s[min(len(s) - 1, int(0.975 * len(s)))]


def pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def cell(metric: str, v: dict) -> str:
    if metric == "penalised_score":
        return f"{v['value']:+.3f} ({v['lo']:+.3f} to {v['hi']:+.3f})"
    return f"{pct(v['value'])} ({pct(v['lo'])} to {pct(v['hi'])})"


def diff_cell(metric: str, v: dict) -> str:
    if metric == "penalised_score":
        body = f"{v['value']:+.3f} ({v['lo']:+.3f} to {v['hi']:+.3f})"
    else:
        body = f"{100 * v['value']:+.1f} pp ({100 * v['lo']:+.1f} to {100 * v['hi']:+.1f})"
    return f"{body}, share {v['share_wrong_side']:.4f}" + (" *" if v["predicted_sign"] else "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(ROOT / "results" / "study5"))
    ap.add_argument("--boot", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=SEED)
    a = ap.parse_args()
    d = Path(a.dir)

    found = {p.name[len("eval_"):-len(".jsonl")]: p for p in d.glob("eval_*.jsonl")}
    models = [m for m in ORDER if m in found] + sorted(m for m in found if m not in ORDER)
    missing = [m for m in ORDER if m not in found]
    rows = {m: [json.loads(ln) for ln in found[m].read_text().splitlines() if ln.strip()] for m in models}
    ids = [r["id"] for r in rows[models[0]]]
    for m in models:
        assert [r["id"] for r in rows[m]] == ids, f"{m}: other questions or another order than {models[0]}"
    n = len(ids)
    codes = {m: [CODES[r["outcome"]] for r in rows[m]] for m in models}

    rng = random.Random(a.seed)
    draws: dict[str, dict[str, list[float]]] = {m: {k: [] for k in METRICS} for m in models}
    for _ in range(a.boot):
        idx = rng.choices(range(n), k=n)
        for m in models:
            for k, v in metrics(counts(codes[m], idx)).items():
                draws[m][k].append(v)

    out: dict = {"questions": n, "resamples": a.boot, "seed": a.seed, "missing_models": missing,
                 "models": {}, "differences": {}, "predictions": {}}
    for m in models:
        point = metrics(counts(codes[m], range(n)))
        out["models"][m] = {"label": LABELS.get(m, m), "file": found[m].name,
                            "counts": dict(zip(CODES, counts(codes[m], range(n)))),
                            "hit_token_limit": sum(r.get("finish") == "length" for r in rows[m])}
        for k in METRICS:
            lo, hi = interval(draws[m][k])
            out["models"][m][k] = {"value": point[k], "lo": lo, "hi": hi}

    for x, y in PAIRS:
        if x not in codes or y not in codes:
            continue
        out["differences"][f"{x}-{y}"] = {}
        for k in DIFF_METRICS:
            dd = [p - q for p, q in zip(draws[x][k], draws[y][k])]
            value = out["models"][x][k]["value"] - out["models"][y][k]["value"]
            lo, hi = interval(dd)
            le, ge = sum(v <= 0 for v in dd) / len(dd), sum(v >= 0 for v in dd) / len(dd)
            sign = PREDICTED.get((x, y), {}).get(k)
            against = sign if sign else (1 if value > 0 else -1 if value < 0 else 0)
            wrong = le if against > 0 else ge if against < 0 else 1.0
            out["differences"][f"{x}-{y}"][k] = {"value": value, "lo": lo, "hi": hi, "share_le_0": le, "share_ge_0": ge,
                                                  "predicted_sign": sign, "share_wrong_side": wrong}

    md = [f"Evaluation by the key on {n} MedQA test questions (rows 500 to 799). One greedy response per question, "
          "no system prompt for the trained models. Intervals are 95% percentile bootstraps over questions "
          f"({a.boot} resamples, seed {a.seed}), paired across models. Rates are shares of all questions. "
          "Penalised score: +1 for a right answer, -1 for a wrong or unparsed one, 0 for an abstention, averaged.", ""]
    if missing:
        md += [f"Missing output files: {', '.join(missing)}.", ""]
    md += ["| model | " + " | ".join(NAMES[k] for k in METRICS) + " |", "|---|" + "---|" * len(METRICS)]
    for m in models:
        md.append(f"| {LABELS.get(m, m)} | " + " | ".join(cell(k, out["models"][m][k]) for k in METRICS) + " |")
    md += ["", "The three reference rows run the base model with the style instruction as system prompt, the way "
           "the training pool was generated. They are not part of the registered evaluation.", ""]

    if out["differences"]:
        md += ["Paired differences (first minus second, same resampled questions). The share is the bootstrap share "
               "of resamples on the wrong side of zero. A star marks a cell with a registered sign (P5c, P5e), where "
               "the share counts resamples at zero or with the other sign. In the other cells the share is taken "
               "against the sign of the observed difference.", "",
               "| difference | " + " | ".join(NAMES[k] for k in DIFF_METRICS) + " |", "|---|" + "---|" * len(DIFF_METRICS)]
        for pair, v in out["differences"].items():
            md.append(f"| {pair} | " + " | ".join(diff_cell(k, v[k]) for k in DIFF_METRICS) + " |")
        md.append("")

    jk = out["differences"].get("J-K")
    if jk:
        parts = {k: jk[k] for k in ("abstention_rate", "wrong_rate", "penalised_score")}
        holds = all(v["share_wrong_side"] < 0.05 for v in parts.values())
        out["predictions"]["P5c"] = {"holds": holds, "level": 0.05,
                                     "shares": {k: v["share_wrong_side"] for k, v in parts.items()}}
        md += ["P5c (the J model has a lower abstention rate, a higher wrong-answer rate and a lower penalised score "
               f"than the K model, each at 0.05): {'holds' if holds else 'does not hold'}. "
               + ". ".join(f"{PHRASE[k]} {diff_cell(k, v).rstrip(' *')}" for k, v in parts.items()) + ".", ""]
    fk, jf = out["differences"].get("F-K"), out["differences"].get("J-F")
    if fk and jf:
        between = {}
        for k in ("abstention_rate", "penalised_score"):
            j, f, kk = (out["models"][m][k]["value"] for m in ("J", "F", "K"))
            inside = sum(min(p, q) <= r <= max(p, q) for p, r, q in
                         zip(draws["J"][k], draws["F"][k], draws["K"][k])) / a.boot
            between[k] = {"J": j, "F": f, "K": kk, "all_equal": j == f == kk,
                          "F_between_J_and_K": min(j, kk) <= f <= max(j, kk),
                          "predicted_order_J_F_K": j < f < kk, "share_resamples_F_between": inside}
        out["predictions"]["P5e"] = between
        md += ["P5e (the F model sits between J and K on abstention rate and penalised score). "
               + " ".join(f"{PHRASE[k]}: J {cell(k, out['models']['J'][k]).split(' (')[0]}, "
                          f"F {cell(k, out['models']['F'][k]).split(' (')[0]}, K {cell(k, out['models']['K'][k]).split(' (')[0]}, "
                          + ("the three are equal, so there is no order to test."
                             if v["all_equal"] else
                             f"F between J and K: {'yes' if v['F_between_J_and_K'] else 'no'}, "
                             f"in the predicted order J below F below K: {'yes' if v['predicted_order_J_F_K'] else 'no'}, "
                             f"F between them in {v['share_resamples_F_between']:.4f} of the resamples.")
                          for k, v in between.items()), ""]

    noisy = [m for m in models if out["models"][m]["unparsed_rate"]["value"] > 0.05]
    if noisy:
        md += ["Models with more than 5% unparsed responses, three raw responses each (cut at 400 characters).", ""]
        for m in noisy:
            bad = [r for r in rows[m] if r["outcome"] == "unparsed"]
            md.append(f"{LABELS.get(m, m)}: {len(bad)} of {n} unparsed, "
                      f"{sum(r.get('finish') == 'length' for r in bad)} of them cut by the token limit.")
            md += ["", *[f"- `{r['id']}`: {json.dumps(r['text'][:400], ensure_ascii=False)}" for r in bad[:3]], ""]

    (d / "eval_table.json").write_text(json.dumps(out, indent=2) + "\n")
    (d / "eval_table.md").write_text("\n".join(md).rstrip() + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
