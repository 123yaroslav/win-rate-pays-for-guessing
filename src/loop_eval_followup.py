"""Study 5 follow-up: tables for the four models trained directly on the GPU pod (C3, J3, K3, R3).

Reads `results/study5/eval_<model>.jsonl`, written by `src/gpu_eval.py` on the pod for the adapters that
`src/gpu_train_lora.py` trained. Per model: abstention rate, accuracy, wrong-answer rate, unparsed rate and
penalised score with 95% percentile bootstrap intervals over the 300 test questions. The bootstrap is paired,
as in `src/loop_eval_analyze.py`: every resample draws one list of questions and all models are scored on it.

Paired differences C3-J3, C3-K3, J3-K3 and J3-R3 with the bootstrap share on the wrong side of zero. The
follow-up design in `results/study5/deviations.md` predicts two signs for C3-J3 (more abstentions, fewer wrong
answers for C3). There the share counts resamples at zero or with the other sign. Elsewhere no sign is
predicted and the share is taken against the sign of the observed difference, as a description.

The three predictions of the design are evaluated literally, and one more table shows where the abstentions of
C3 fall: on the questions the J3 model gets wrong, or anywhere.

    python src/loop_eval_followup.py       # results/study5/eval_table_followup.md and .json
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from loop_eval_analyze import CODES, METRICS, NAMES, cell, counts, interval, metrics, pct

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261115
MODELS = ["C3", "J3", "K3", "R3"]
ARM = {"C3": "C", "J3": "J", "K3": "K", "R3": "R"}
LABELS = {
    "C3": "C3, cautious style, no selection",
    "J3": "J3, judge, default instruction",
    "K3": "K3, by the key",
    "R3": "R3, random",
    "J": "J, registered run (service, one epoch)",
    "K": "K, registered run (service, one epoch)",
    "R": "R, registered run (service, one epoch)",
    "base_abstain": "base model, abstain instruction (reference)",
}
REFERENCE = ["J", "K", "R", "base_abstain"]
PAIRS = [("C3", "J3"), ("C3", "K3"), ("J3", "K3"), ("J3", "R3")]
PREDICTED = {("C3", "J3"): {"abstention_rate": +1, "wrong_rate": -1}}
DIFF_METRICS = ["abstention_rate", "wrong_rate", "accuracy", "penalised_score"]
OUTCOMES = ["correct", "wrong", "abstain", "unparsed"]


def load(d: Path, name: str) -> list[dict] | None:
    p = d / f"eval_{name}.jsonl"
    return [json.loads(ln) for ln in p.read_text().splitlines() if ln.strip()] if p.exists() else None


def diff_cell(metric: str, v: dict) -> str:
    if metric == "penalised_score":
        body = f"{v['value']:+.3f} ({v['lo']:+.3f} to {v['hi']:+.3f})"
    else:
        body = f"{100 * v['value']:+.1f} pp ({100 * v['lo']:+.1f} to {100 * v['hi']:+.1f})"
    return f"{body}, share {v['share_wrong_side']:.4f}" + (" *" if v["predicted_sign"] else "")


def share(num: int, den: int) -> float | None:
    return num / den if den else None


def show(x: float | None) -> str:
    return "no such question" if x is None else pct(x)


def targeting(c_abstains: list[bool], other_wrong: list[bool], idx) -> dict[str, float | None]:
    """Where the abstentions of one model fall, against the wrong answers of another, on the questions idx."""
    a = [c_abstains[i] for i in idx]
    w = [other_wrong[i] for i in idx]
    both = sum(x and y for x, y in zip(a, w))
    n, na, nw = len(a), sum(a), sum(w)
    out = {
        "wrong_given_abstain": share(both, na),
        "wrong_given_no_abstain": share(nw - both, n - na),
        "abstain_given_wrong": share(both, nw),
        "abstain_given_not_wrong": share(na - both, n - nw),
    }
    for name, x, y in (("wrong_gap", "wrong_given_abstain", "wrong_given_no_abstain"),
                       ("abstain_gap", "abstain_given_wrong", "abstain_given_not_wrong")):
        out[name] = None if out[x] is None or out[y] is None else out[x] - out[y]
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(ROOT / "results" / "study5"))
    ap.add_argument("--boot", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=SEED)
    a = ap.parse_args()
    d = Path(a.dir)

    rows = {m: load(d, m) for m in MODELS + REFERENCE}
    missing = [m for m in MODELS if rows[m] is None]
    if missing:
        raise SystemExit(f"missing output files for {', '.join(missing)}")
    models = MODELS + [m for m in REFERENCE if rows[m] is not None]
    ids = [r["id"] for r in rows["C3"]]
    for m in models:
        assert [r["id"] for r in rows[m]] == ids, f"{m}: other questions or another order than C3"
    n = len(ids)
    codes = {m: [CODES[r["outcome"]] for r in rows[m]] for m in models}

    # targeting: the abstentions of C3 against the errors of each other follow-up model
    c_abs = [r["outcome"] == "abstain" for r in rows["C3"]]
    wrong = {m: [r["outcome"] == "wrong" for r in rows[m]] for m in MODELS[1:]}
    not_right = {m: [r["outcome"] in ("wrong", "unparsed") for r in rows[m]] for m in MODELS[1:]}
    views = {f"{m}_wrong": wrong[m] for m in MODELS[1:]} | {f"{m}_wrong_or_unparsed": not_right[m] for m in MODELS[1:]}

    rng = random.Random(a.seed)
    draws: dict[str, dict[str, list[float]]] = {m: {k: [] for k in METRICS} for m in models}
    t_draws: dict[str, dict[str, list[float]]] = {v: {} for v in views}
    for _ in range(a.boot):
        idx = rng.choices(range(n), k=n)
        for m in models:
            for k, v in metrics(counts(codes[m], idx)).items():
                draws[m][k].append(v)
        for name, flags in views.items():
            for k, v in targeting(c_abs, flags, idx).items():
                if v is not None:
                    t_draws[name].setdefault(k, []).append(v)

    out: dict = {"questions": n, "resamples": a.boot, "seed": a.seed, "models": {}, "differences": {},
                 "predictions": {}, "targeting": {}, "training": {}}
    for m in models:
        point = metrics(counts(codes[m], range(n)))
        out["models"][m] = {"label": LABELS.get(m, m), "file": f"eval_{m}.jsonl", "reference_only": m in REFERENCE,
                            "counts": dict(zip(CODES, counts(codes[m], range(n)))),
                            "hit_token_limit": sum(r.get("finish") == "length" for r in rows[m])}
        for k in METRICS:
            lo, hi = interval(draws[m][k])
            out["models"][m][k] = {"value": point[k], "lo": lo, "hi": hi}

    for x, y in PAIRS:
        out["differences"][f"{x}-{y}"] = {}
        for k in DIFF_METRICS:
            dd = [p - q for p, q in zip(draws[x][k], draws[y][k])]
            value = out["models"][x][k]["value"] - out["models"][y][k]["value"]
            lo, hi = interval(dd)
            le, ge = sum(v <= 0 for v in dd) / len(dd), sum(v >= 0 for v in dd) / len(dd)
            sign = PREDICTED.get((x, y), {}).get(k)
            against = sign if sign else (1 if value > 0 else -1 if value < 0 else 0)
            wrong_side = le if against > 0 else ge if against < 0 else 1.0
            out["differences"][f"{x}-{y}"][k] = {"value": value, "lo": lo, "hi": hi, "share_le_0": le,
                                                  "share_ge_0": ge, "predicted_sign": sign,
                                                  "share_wrong_side": wrong_side}

    md = [f"Follow-up evaluation by the key on {n} MedQA test questions (rows 500 to 799), exploratory. The four "
          "models were trained directly on the rented GPU with `src/gpu_train_lora.py` (three epochs, the same "
          "settings for every arm) and evaluated with `src/gpu_eval.py` as registered: one greedy response per "
          "question, no system prompt. Intervals are 95% percentile bootstraps over questions "
          f"({a.boot} resamples, seed {a.seed}), paired across models. Rates are shares of all questions. "
          "Penalised score: +1 for a right answer, -1 for a wrong or unparsed one, 0 for an abstention, averaged.", "",
          "| model | " + " | ".join(NAMES[k] for k in METRICS) + " |", "|---|" + "---|" * len(METRICS)]
    for m in MODELS:
        md.append(f"| {LABELS[m]} | " + " | ".join(cell(k, out["models"][m][k]) for k in METRICS) + " |")
    refs = [m for m in models if m in REFERENCE]
    if refs:
        md += ["", "For reference, rows of the registered evaluation on the same questions and resamples. They come "
               "from another training (the service, one epoch) or from the base model with an instruction, and they "
               "were run on another pod of the same GPU type.", "",
               "| model | " + " | ".join(NAMES[k] for k in METRICS) + " |", "|---|" + "---|" * len(METRICS)]
        for m in refs:
            md.append(f"| {LABELS[m]} | " + " | ".join(cell(k, out["models"][m][k]) for k in METRICS) + " |")

    md += ["", "Paired differences (first minus second, same resampled questions). The share is the bootstrap share "
           "of resamples on the wrong side of zero. A star marks a cell where the follow-up design predicts a sign "
           "(C3 abstains more than J3 and gives fewer wrong answers). There the share counts resamples at zero or "
           "with the other sign. In the other cells the share is taken against the sign of the observed difference.",
           "", "| difference | " + " | ".join(NAMES[k] for k in DIFF_METRICS) + " |",
           "|---|" + "---|" * len(DIFF_METRICS)]
    for pair, v in out["differences"].items():
        md.append(f"| {pair} | " + " | ".join(diff_cell(k, v[k]) for k in DIFF_METRICS) + " |")
    md.append("")

    # the three predictions, literally
    c3, j3 = out["models"]["C3"], out["models"]["J3"]
    wr = out["differences"]["C3-J3"]["wrong_rate"]
    p1 = c3["abstention_rate"]["value"] >= 0.10
    p2 = j3["abstention_rate"]["value"] <= 0.02
    p3 = wr["value"] < 0 and wr["share_wrong_side"] < 0.05
    out["predictions"] = {
        "C3_abstains_on_at_least_10pct": {"holds": p1, "value": c3["abstention_rate"]["value"],
                                          "count": c3["counts"]["abstain"]},
        "J3_abstains_on_at_most_2pct": {"holds": p2, "value": j3["abstention_rate"]["value"],
                                        "count": j3["counts"]["abstain"]},
        "J3_wrong_rate_above_C3": {"holds": p3, "level": 0.05, "J3_minus_C3": -wr["value"],
                                   "share_wrong_side": wr["share_wrong_side"]},
        "abstention_survives_in_C3": c3["counts"]["abstain"] > 0,
    }
    verdict = lambda ok: "holds" if ok else "does not hold"  # noqa: E731
    md += ["Predictions of the follow-up design, evaluated literally.", "",
           f"1. The C model abstains on at least 10% of the test questions: {verdict(p1)}. C3 abstains on "
           f"{c3['counts']['abstain']} of {n}, {cell('abstention_rate', c3['abstention_rate'])}.",
           f"2. The J model abstains on at most 2%: {verdict(p2)}. J3 abstains on {j3['counts']['abstain']} of {n}, "
           f"{cell('abstention_rate', j3['abstention_rate'])}.",
           f"3. The J model has a higher wrong-answer rate than the C model (paired bootstrap, 0.05): {verdict(p3)}. "
           f"J3 {pct(j3['wrong_rate']['value'])}, C3 {pct(c3['wrong_rate']['value'])}, J3 minus C3 "
           f"{-100 * wr['value']:+.1f} pp ({-100 * wr['hi']:+.1f} to {-100 * wr['lo']:+.1f}), share of resamples "
           f"where J3 is not above C3 {wr['share_wrong_side']:.4f}.", ""]
    if c3["counts"]["abstain"] == 0:
        md += ["The C model does not abstain either. In the words of the design, the follow-up shows that abstention "
               "does not survive this fine-tuning at all.", ""]

    # where the abstentions of C3 fall
    cross = {x: {y: 0 for y in OUTCOMES} for x in OUTCOMES}
    for rc, rj in zip(rows["C3"], rows["J3"]):
        cross[rc["outcome"]][rj["outcome"]] += 1
    out["targeting"]["C3_by_J3_counts"] = cross
    n_abs = sum(c_abs)
    md += ["Where the abstentions of C3 fall. Counts of the 300 questions by the outcome of C3 (rows) and of J3 "
           "(columns).", "", "| C3 \\ J3 | " + " | ".join(OUTCOMES) + " | all |", "|---|" + "---|" * (len(OUTCOMES) + 1)]
    for x in OUTCOMES:
        md.append(f"| {x} | " + " | ".join(str(cross[x][y]) for y in OUTCOMES) + f" | {sum(cross[x].values())} |")
    md.append("| all | " + " | ".join(str(sum(cross[x][y] for x in OUTCOMES)) for y in OUTCOMES) + f" | {n} |")
    md.append("")
    for name, flags in views.items():
        point = targeting(c_abs, flags, range(n))
        block = {"C3_abstains": n_abs, "other_flagged": sum(flags),
                 "both": sum(x and y for x, y in zip(c_abs, flags))}
        for k, v in point.items():
            dr = t_draws[name].get(k, [])
            lo, hi = interval(dr) if dr else (None, None)
            block[k] = {"value": v, "lo": lo, "hi": hi, "resamples_defined": len(dr)}
            if k.endswith("_gap") and dr:
                block[k]["share_le_0"] = sum(x <= 0 for x in dr) / len(dr)
        out["targeting"][name] = block
    if n_abs:
        def rate(v: dict) -> str:
            return "no such question" if v["value"] is None else f"{pct(v['value'])} ({pct(v['lo'])} to {pct(v['hi'])})"

        def gap(v: dict) -> str:
            if v["value"] is None:
                return "not defined"
            return (f"{100 * v['value']:+.1f} pp ({100 * v['lo']:+.1f} to {100 * v['hi']:+.1f}), "
                    f"share at or below zero {v['share_le_0']:.4f}")

        md += [f"C3 abstains on {n_abs} questions. The table asks whether these are the questions another model gets "
               "wrong. First pair of columns: the share of questions the other model gets wrong, among the questions "
               "where C3 abstains and among the rest. Second pair: the share of questions where C3 abstains, among "
               "the questions the other model gets wrong and among the rest. Caution is aimed at the right questions "
               "if the first number of each pair is the larger one. Intervals are bootstraps over questions. No sign "
               "was predicted for these gaps, the share is a description.", "",
               "| other model, its error | wrong where C3 abstains | wrong where C3 answers | gap | "
               "C3 abstains where the other is wrong | C3 abstains where it is not | gap |", "|---|---|---|---|---|---|---|"]
        for name in views:
            b = out["targeting"][name]
            who, _, what = name.partition("_")
            md.append(f"| {who}, {what.replace('_', ' ')} ({b['other_flagged']} questions, {b['both']} of them among "
                      f"the abstentions) | {rate(b['wrong_given_abstain'])} | {rate(b['wrong_given_no_abstain'])} | "
                      f"{gap(b['wrong_gap'])} | {rate(b['abstain_given_wrong'])} | {rate(b['abstain_given_not_wrong'])} | "
                      f"{gap(b['abstain_gap'])} |")
        md.append("")
    else:
        md += ["C3 abstains on no question, so there is nothing to relate to the errors of J3.", ""]

    # training losses, if the logs are here
    logs = {m: d / f"followup_train_log_{ARM[m]}.json" for m in MODELS}
    if all(p.exists() for p in logs.values()):
        md += ["Training (from `followup_train_log_<arm>.json`). Loss is the mean negative log-likelihood per "
               "completion token of a step.", "",
               "| model | steps | first step | mean of epoch 1 | epoch 2 | epoch 3 | mean of the last 10 steps | "
               "final step | longest example, tokens | seconds |", "|---|---|---|---|---|---|---|---|---|---|"]
        for m, p in logs.items():
            s = json.loads(p.read_text())
            e = s["mean_loss_by_epoch"]
            out["training"][m] = {k: s[k] for k in ("steps_done", "first_step_loss", "final_step_loss",
                                                     "mean_loss_last_10_steps", "mean_loss_by_epoch",
                                                     "longest_example_tokens", "seconds", "adapter_sha256",
                                                     "data_sha256", "settings")}
            md.append(f"| {m} | {s['steps_done']} | {s['first_step_loss']:.3f} | {e['1']:.3f} | {e['2']:.3f} | "
                      f"{e['3']:.3f} | {s['mean_loss_last_10_steps']:.3f} | {s['final_step_loss']:.3f} | "
                      f"{s['longest_example_tokens']} | {s['seconds']:.0f} |")
        md.append("")

    noisy = [m for m in MODELS if out["models"][m]["unparsed_rate"]["value"] > 0.05]
    if noisy:
        md += ["Models with more than 5% unparsed responses, three raw responses each (cut at 400 characters).", ""]
        for m in noisy:
            bad = [r for r in rows[m] if r["outcome"] == "unparsed"]
            md.append(f"{LABELS[m]}: {len(bad)} of {n} unparsed, "
                      f"{sum(r.get('finish') == 'length' for r in bad)} of them cut by the token limit.")
            md += ["", *[f"- `{r['id']}`: {json.dumps(r['text'][:400], ensure_ascii=False)}" for r in bad[:3]], ""]
    else:
        md += ["No follow-up model has more than 5% unparsed responses.", ""]

    (d / "eval_table_followup.json").write_text(json.dumps(out, indent=2) + "\n")
    (d / "eval_table_followup.md").write_text("\n".join(md).rstrip() + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
