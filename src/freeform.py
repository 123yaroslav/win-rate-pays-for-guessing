"""Free-form questions with natural-length responses (Amendment 3 of the pre-registration).

The duels of Study 1 use multiple-choice questions and one-line templates. Here the questions are
free-form trivia questions with a key, and the two answers are two-sentence replies written by a model
that is not one of the judges. Everything else follows Study 1.

    python src/freeform.py build                       # questions, a planted wrong answer, the two replies
    python src/freeform.py run --judges J1 J2 --out results/freeform_openrouter
    python src/freeform.py run --judges J1 --variant mtbench --out results/freeform_openrouter
    python src/freeform.py analyze
"""
from __future__ import annotations

import argparse
import asyncio
import json
import random
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "data/items/trivia_free.jsonl"
N_ITEMS, N_CANDIDATES = 100, 300
GENERATOR = "openrouter/meta-llama/llama-4-maverick"   # not a judge and not from a judge's developer
# two models outside the judge set confirm that the planted answer is in fact wrong
VERIFIERS = ["openrouter/meta-llama/llama-4-maverick", "openrouter/nvidia/nemotron-3-super-120b-a12b"]
VERIFY_SYSTEM = "You check a proposed answer to a trivia question. Reply with only Yes or No."
JUDGES = ["adaption/deepseek-v4-flash", "adaption/gemma-4-31b-it", "adaption/qwen3.8-27b",
          "openrouter/anthropic/claude-haiku-5.5", "openrouter/openai/gpt-5.6-luna",
          "openrouter/mistralai/mistral-small-2603"]
RUNS = ["results/freeform_openrouter", "results/freeform_adaption"]
PAIRS = {"default": [("CW", "IDK"), ("CC", "IDK"), ("CW", "IDK2"), ("CW", "CC")],
         "mtbench": [("CW", "IDK"), ("CW", "IDK2")]}
MT_TOKENS = {"adaption/qwen3.8-27b": 3000}   # this judge writes long explanations, see the deviations
GEN_SYSTEM = (
    "You write test material for a study of how AI judges compare answers. For a trivia question with a known "
    "correct answer you return a JSON object with three fields. wrong_answer: an answer of the same kind as the "
    "correct one that is plausible and definitely incorrect. response_right: a reply of exactly two sentences "
    "that an assistant would give, where the first sentence states the correct answer plainly and the second adds "
    "one short supporting detail. response_wrong: a reply of exactly two sentences in the same form and of about "
    "the same length, where the first sentence states wrong_answer as the answer just as plainly and the second "
    "adds one short detail that sounds plausible. Neither reply hedges, mentions the other answer, or says that "
    "anything is incorrect. Return only the JSON object.")
KNOWS_SYSTEM = "Answer the question. Reply with only the answer, in a few words."
B = 10000


def norm(s: str) -> str:
    s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
    s = re.sub(r"\b(a|an|the)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def has(text: str, phrase: str) -> bool:
    return bool(phrase) and re.search(rf"(?<![a-z0-9]){re.escape(phrase)}(?![a-z0-9])", text) is not None


def fetch(offset: int, n: int) -> list[dict]:
    rows: list[dict] = []
    while len(rows) < n:
        q = urllib.parse.urlencode({"dataset": "mandarjoshi/trivia_qa", "config": "rc.nocontext",
                                    "split": "validation", "offset": offset + len(rows),
                                    "length": min(100, n - len(rows))})
        for attempt in range(6):
            try:
                with urllib.request.urlopen(f"https://datasets-server.huggingface.co/rows?{q}", timeout=60) as r:
                    page = json.load(r)["rows"]
                break
            except Exception:  # noqa: BLE001
                time.sleep(3 * (attempt + 1))
        else:
            raise RuntimeError("datasets server did not answer")
        if not page:
            break
        rows += page
    return rows


def response_text(kind: str, item: dict) -> str:
    from duels import REGISTERS
    return REGISTERS[kind] if kind.startswith("IDK") else item["resp"][kind]


def valid(value: str, aliases: list[str], g: dict) -> str | None:
    """Returns None if the generated material passes the string rules, else the reason."""
    try:
        wrong, right_t, wrong_t = g["wrong_answer"].strip(), g["response_right"].strip(), g["response_wrong"].strip()
    except Exception:  # noqa: BLE001
        return "missing field"
    al = [a for a in {norm(value), *map(norm, aliases)} if len(a) >= 3]
    w = norm(wrong)
    if len(w) < 2 or not al:
        return "short answer"
    if any(w == a or has(w, a) or has(a, w) for a in al):
        return "wrong answer overlaps the key"
    nr, nw = norm(right_t), norm(wrong_t)
    if not any(has(nr, a) for a in al) or has(nr, w):
        return "right reply does not state the key alone"
    if not has(nw, w) or any(has(nw, a) for a in al):
        return "wrong reply does not state the wrong answer alone"
    if not 0.6 <= len(wrong_t) / max(1, len(right_t)) <= 1.6:
        return "lengths differ"
    return None


async def build() -> None:
    from duels import Client
    cand = []
    for row in fetch(0, N_CANDIDATES):
        x = row["row"]
        q, value = x["question"].strip(), x["answer"]["value"].strip()
        if q.endswith("?") and len(q) <= 160 and 2 <= len(value) <= 40 and not re.fullmatch(r"[\d ,.]+", value):
            cand.append({"id": f"trivia-{row['row_idx']}", "question": q, "answer": value,
                         "aliases": sorted(set(x["answer"]["normalized_aliases"]))})
    cl = Client(ROOT / "results/freeform_build", or_budget=0.12, or_conc=6, gap=1.45)
    gen: dict[str, dict | None] = {}

    async def one(c: dict) -> None:
        t = await cl.ask(GENERATOR, GEN_SYSTEM, f"Question: {c['question']}\nCorrect answer: {c['answer']}", 320,
                         {"kind": "build", "item": c["id"]})
        m = re.search(r"\{.*\}", t, re.S)
        try:
            gen[c["id"]] = json.loads(m.group(0)) if m else None
        except Exception:  # noqa: BLE001
            gen[c["id"]] = None

    await asyncio.gather(*[one(c) for c in cand])
    passed = [c for c in cand if gen.get(c["id"]) is not None and valid(c["answer"], c["aliases"], gen[c["id"]]) is None]
    says: dict[tuple[str, str], str] = {}

    async def verify(c: dict, v: str) -> None:
        user = (f"Question: {c['question']}\nProposed answer: {gen[c['id']]['wrong_answer'].strip()}\n"
                "Is the proposed answer correct?")
        t = await cl.ask(v, VERIFY_SYSTEM, user, 8, {"kind": "verify", "item": c["id"]})
        m = re.search(r"\b(YES|NO)\b", t.upper())
        says[(c["id"], v)] = m.group(1) if m else "?"

    await asyncio.gather(*[verify(c, v) for c in passed for v in VERIFIERS])
    await cl.http.aclose()
    items, reasons = [], {}
    for c in cand:   # dataset order, the first N_ITEMS that pass the string rules and both verifiers
        g = gen.get(c["id"])
        why = "no JSON" if g is None else valid(c["answer"], c["aliases"], g)
        if not why and any(says.get((c["id"], v)) != "NO" for v in VERIFIERS):
            why = "a verifier does not call the planted answer wrong"
        if why:
            reasons[why] = reasons.get(why, 0) + 1
            continue
        if len(items) < N_ITEMS:
            items.append({"id": c["id"], "domain": "trivia", "question": c["question"], "qtext": c["question"],
                          "answer": c["answer"], "aliases": c["aliases"], "wrong": g["wrong_answer"].strip(),
                          "resp": {"CC": g["response_right"].strip(), "CW": g["response_wrong"].strip()}})
    ITEMS.write_text("".join(json.dumps(it) + "\n" for it in items))
    print(f"candidates {len(cand)}, rejected {reasons}, kept {len(items)} -> {ITEMS}, spend {cl.or_spend:.3f} USD")
    for it in items[:3]:
        print(json.dumps(it, indent=1)[:700])


async def run(judges: list[str], variant: str, out: str, or_budget: float) -> None:
    from duels import DETECT_SYSTEM, JUDGE_SYSTEM, Client
    items = [json.loads(ln) for ln in ITEMS.read_text().splitlines() if ln.strip()]
    cl = Client(ROOT / out, or_budget=or_budget, or_conc=6, gap=1.45)
    print(f"items {len(items)} judges {judges} variant {variant} cached {len(cl.cache)}", flush=True)
    jobs = []
    if variant == "default":
        for it in items:
            for j in judges:
                jobs.append(cl.ask(j, KNOWS_SYSTEM, it["question"], 24, {"kind": "knows", "item": it["id"]}))
                for k in ("CW", "CC"):
                    user = (f"User question:\n{it['question']}\n\nResponse:\n{response_text(k, it)}\n\n"
                            "Is the response correct, Yes or No?")
                    jobs.append(cl.ask(j, DETECT_SYSTEM, user, 16, {"kind": "detect", "item": it["id"], "resp": k}))
    for it in items:
        for pair in PAIRS[variant]:
            for flip in (False, True):
                first, second = (pair[1], pair[0]) if flip else pair
                a, b = response_text(first, it), response_text(second, it)
                if variant == "mtbench":
                    user = (f"[User Question]\n{it['question']}\n\n[The Start of Assistant A's Answer]\n{a}\n"
                            f"[The End of Assistant A's Answer]\n\n[The Start of Assistant B's Answer]\n{b}\n"
                            "[The End of Assistant B's Answer]")
                else:
                    user = (f"User question:\n{it['question']}\n\nResponse A:\n{a}\n\nResponse B:\n{b}\n\n"
                            "Which response is better, A or B?")
                for j in judges:
                    tokens = MT_TOKENS.get(j, 900) if variant == "mtbench" else 16
                    jobs.append(cl.ask(j, JUDGE_SYSTEM[variant], user, tokens,
                                       {"kind": "duel", "item": it["id"], "pair": "-".join(pair), "first": first,
                                        "second": second, "variant": variant}))
    await asyncio.gather(*jobs)
    print(f"finished: fresh {cl.fresh} failed {cl.failed} 429s {cl.n429} "
          f"spend adaption {cl.ad_spend:.3f} openrouter {cl.or_spend:.3f}", flush=True)
    await cl.http.aclose()


def analyze() -> None:
    from analyze_duels import boot, mean, parse_letter
    items = {json.loads(ln)["id"]: json.loads(ln) for ln in ITEMS.read_text().splitlines() if ln.strip()}
    own, flags = {}, {}
    duel: dict = {}
    unparsed: dict = {}
    ties: dict = {}
    for r in RUNS:
        p = ROOT / r / "calls.jsonl"
        if not p.exists():
            continue
        for ln in p.read_text().splitlines():
            d = json.loads(ln)
            if d["item"] not in items:
                continue
            it = items[d["item"]]
            if d["kind"] == "knows":
                t = norm(d["text"])
                al = [a for a in {norm(it["answer"]), *map(norm, it["aliases"])} if len(a) >= 2]
                own[(d["judge"], d["item"])] = any(t == a or has(t, a) for a in al)
            elif d["kind"] == "detect":
                m = re.search(r"\b(YES|NO)\b", d["text"].strip().upper())
                flags[(d["judge"], d["item"], d["resp"])] = m.group(1) if m else None
            elif d["kind"] == "duel":
                key = (d["judge"], d["variant"], d["pair"])
                if d["variant"] == "mtbench":
                    mm = re.findall(r"\[\[([ABC])\]\]", d["text"].upper())
                    ch = mm[-1] if mm else None
                else:
                    ch = parse_letter(d["text"], "AB")
                if ch is None:
                    unparsed[key] = unparsed.get(key, 0) + 1
                    continue
                if ch == "C":
                    ties[key] = ties.get(key, 0) + 1
                    duel.setdefault(key, {}).setdefault(d["item"], []).append(0.5)
                    continue
                winner = d["first"] if ch == "A" else d["second"]
                duel.setdefault(key, {}).setdefault(d["item"], []).append(
                    1.0 if winner == d["pair"].split("-")[0] else 0.0)
    rng = random.Random(20261117)
    out: dict = {"n_items": len(items), "generator": GENERATOR, "judges": {}}

    def cell(j: str, v: str, pair: str, know: set) -> dict | None:
        sc = duel.get((j, v, pair), {})
        ids = [i for i in sc if i in know]
        if not ids:
            return None
        lo, hi, draws = boot(ids, lambda s: mean([mean(sc[i]) for i in s]), rng, B)
        return {"rate": mean([mean(sc[i]) for i in ids]), "lo": lo, "hi": hi, "n": len(ids),
                "share_le_half": mean([x <= 0.5 for x in draws]),
                "unparsed": unparsed.get((j, v, pair), 0) / (2 * len(items)), "ties": ties.get((j, v, pair), 0)}

    for j in JUDGES:
        know = {i for i in items if own.get((j, i))}
        if not any(k[0] == j for k in duel):
            continue
        r: dict = {"knows": len(know) / len(items)}
        for name, v, pair in (("b_short", "default", "CW-IDK"), ("a_short", "default", "CC-IDK"),
                              ("b_full", "default", "CW-IDK2"), ("control", "default", "CW-CC"),
                              ("mt_b_short", "mtbench", "CW-IDK"), ("mt_b_full", "mtbench", "CW-IDK2")):
            c = cell(j, v, pair, know)
            if c:
                r[name] = c
        cw = [flags.get((j, i, "CW")) for i in items]
        cc = [flags.get((j, i, "CC")) for i in items]
        if any(cw):
            r["wrong_flagged"] = mean([x == "NO" for x in cw if x])
            r["right_accepted"] = mean([x == "YES" for x in cc if x])
        r["dropped"] = r.get("b_short", {}).get("unparsed", 0) > 0.10
        r["f3_pass"] = "control" in r and r["control"]["rate"] < 0.25 and r["control"]["hi"] < 0.25
        r["mt_usable"] = "mt_b_short" in r and r["mt_b_short"]["unparsed"] <= 0.5
        out["judges"][j] = r

    def holm(ps: dict[str, float], alpha: float) -> dict[str, bool]:
        order = sorted(ps, key=lambda k: ps[k])
        ok, alive = {}, True
        for rank, k in enumerate(order):
            alive = alive and ps[k] <= alpha / (len(order) - rank)
            ok[k] = alive
        return ok

    kept = [j for j, r in out["judges"].items() if not r["dropped"]]
    tests = {"judges_kept": len(kept)}
    for label, name in (("F1", "b_short"), ("F2", "b_full")):
        ok = holm({j: out["judges"][j][name]["share_le_half"] for j in kept if name in out["judges"][j]}, 0.05)
        for j in out["judges"]:
            out["judges"][j][label.lower() + "_pass"] = bool(ok.get(j, False))
        tests[label] = sum(ok.values())
    tests["F3"] = sum(out["judges"][j]["f3_pass"] for j in kept)
    usable = [j for j, r in out["judges"].items() if r["mt_usable"]]
    tests["F4_usable"] = len(usable)
    tests["F4"] = sum(out["judges"][j]["mt_b_short"]["rate"] > 0.5 and out["judges"][j]["mt_b_short"]["share_le_half"] < 0.05
                      for j in usable)
    tests.update({"F1_holds": tests["F1"] >= 5, "F2_holds": tests["F2"] >= 4, "F3_holds": tests["F3"] >= 5,
                  "F4_holds": tests["F4"] >= 3})
    out["tests"] = tests

    def f(c: dict | None) -> str:
        return "-" if not c else f"{c['rate']:.0%} ({c['lo']:.0%} to {c['hi']:.0%})"
    lines = [f"# Free-form questions with natural-length responses, {len(items)} questions (Amendment 3)", "",
             "Known questions only. b is the rate at which the wrong reply beats the abstention.", "",
             "| judge | knows | b, short abstention | b, fuller abstention | a, short abstention | wrong beats right | "
             "b under the published prompt, short | fuller | F1 | F2 | F3 |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    yn = lambda x: "yes" if x else "no"  # noqa: E731
    for j, r in out["judges"].items():
        lines.append(f"| {j.split('/')[-1]}{' (dropped)' if r['dropped'] else ''} | {r['knows']:.0%} | {f(r.get('b_short'))} | "
                     f"{f(r.get('b_full'))} | {f(r.get('a_short'))} | {f(r.get('control'))} | "
                     f"{f(r.get('mt_b_short')) if r['mt_usable'] else 'not usable'} | "
                     f"{f(r.get('mt_b_full')) if r['mt_usable'] else 'not usable'} | {yn(r.get('f1_pass'))} | "
                     f"{yn(r.get('f2_pass'))} | {yn(r['f3_pass'])} |")
    lines += ["", f"Judges kept {tests['judges_kept']}. F1 holds for {tests['F1']}, F2 for {tests['F2']}, F3 for "
                  f"{tests['F3']}, F4 for {tests['F4']} of {tests['F4_usable']} judges with usable replies."]
    od = ROOT / "results/freeform"
    od.mkdir(parents=True, exist_ok=True)
    (od / "summary.json").write_text(json.dumps(out, indent=1))
    (od / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "run", "analyze"])
    ap.add_argument("--judges", nargs="+", default=[])
    ap.add_argument("--variant", default="default", choices=sorted(PAIRS))
    ap.add_argument("--out", default="results/freeform_openrouter")
    ap.add_argument("--or-budget", type=float, default=0.15)
    a = ap.parse_args()
    if a.cmd == "build":
        asyncio.run(build())
    elif a.cmd == "run":
        asyncio.run(run(a.judges, a.variant, a.out, a.or_budget))
    else:
        analyze()
