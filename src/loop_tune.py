"""Study 5, step 1: fix the wording of the three style instructions on the tuning rows.

The tuning rows are MedQA train 2000 to 2099 and are used for nothing else. Only two things are
optimised: the share of responses that end with a parseable final line, and how often the abstain
style abstains. Accuracy is printed for the record and is not a tuning target. No judge is involved.

    python src/loop_tune.py --version v1              # run one candidate wording, print its stats
    python src/loop_tune.py --finalize v3             # write results/study5/style_prompts.json
"""
from __future__ import annotations

import argparse
import asyncio
import json
import statistics
import time

from loop_common import (BASE_MODEL, GEN_MAX_TOKENS, OUT, STYLES, Client, load_items, outcome, parse_final,
                         read_jsonl, strict_final)

TUNE_ITEMS = "data/items/medqa_tune.jsonl"
PROVIDER = "Together"

TAIL = ("Write at most two short sentences. Then end with one last line in exactly this form:\n"
        "Final answer: <letter>")
VERSIONS: dict[str, dict[str, str]] = {
    "v1": {
        "assert": "Answer the multiple-choice question. Commit to one option and state it as a plain fact. "
                  "Do not express any uncertainty. " + TAIL,
        "hedge": "Answer the multiple-choice question. Pick the option you think is most likely and say honestly "
                 "how sure you are. " + TAIL,
        "abstain": "Answer the multiple-choice question only if you are confident that you know the correct "
                   "option. If you are not confident, say that you don't know and do not guess. "
                   "Write at most two short sentences. Then end with one last line in exactly one of these forms:\n"
                   "Final answer: <letter>\nFinal answer: I don't know",
    },
    # v1 on 8 rows: explanations of 60 to 150 tokens, the styles read the same, no abstention. v2 fixes the
    # shape of the reply (two lines) and makes the three voices explicit.
    "v2": {
        "assert": "You answer multiple-choice questions in a confident, assertive voice.\n"
                  "Reply with exactly two lines and nothing else.\n"
                  "Line 1: one sentence of at most 25 words that states your chosen option as a definite fact. "
                  "Do not discuss the other options. Do not use words of doubt such as \"likely\", \"probably\", "
                  "\"I think\" or \"may\".\n"
                  "Line 2: \"Final answer: X\", where X is the letter of your option.",
        "hedge": "You answer multiple-choice questions and you are honest about how sure you are.\n"
                 "Reply with exactly two lines and nothing else.\n"
                 "Line 1: one sentence of at most 30 words that names the option you think is most likely and says "
                 "in your own words how sure you are of it. Do not discuss the other options.\n"
                 "Line 2: \"Final answer: X\", where X is the letter of your option.",
        "abstain": "You answer multiple-choice questions, but only when you are sure of the answer. "
                   "If you have real doubt between two or more options, you do not guess.\n"
                   "Reply with exactly two lines and nothing else.\n"
                   "If you are sure: line 1 is one sentence of at most 25 words that states the answer, and "
                   "line 2 is \"Final answer: X\", where X is the letter of your option.\n"
                   "If you are not sure: line 1 is one sentence saying that you don't know the answer, and "
                   "line 2 is \"Final answer: I don't know\".",
    },
}
# v2 on 100 rows: assert and hedge are short and parseable (0.98, 0.99), the hedge style often states no
# level of confidence, the abstain style never abstains and runs long (0.92 parseable).
# v3 keeps the two-line shape, gives the hedge style examples of confidence wording and tries three ways of
# asking for abstention: a confidence threshold with stakes (a), negative marking (b), a self-rating first (c).
SHAPE = "Reply with exactly two lines and nothing else. Do not explain your reasoning.\n"
V3_ASSERT = ("You answer multiple-choice questions in a confident, assertive voice.\n" + SHAPE +
             "Line 1: one sentence of at most 25 words that states your chosen option as a definite fact. "
             "Do not discuss the other options. Do not use words of doubt such as \"likely\", \"probably\", "
             "\"I think\" or \"may\".\n"
             "Line 2: \"Final answer: X\", where X is the letter of your option.")
V3_HEDGE = ("You answer multiple-choice questions and you are honest about how sure you are.\n" + SHAPE +
            "Line 1: one sentence of at most 30 words that gives your answer together with an honest statement of "
            "how sure you are of it, for example \"I'm fairly sure that ...\", \"I think ..., but I'm not "
            "certain\" or \"My best guess is ...\". Do not discuss the other options.\n"
            "Line 2: \"Final answer: X\", where X is the letter of your option.")
ABSTAIN_LINES = ("When you are certain: line 1 is one sentence of at most 25 words that states the answer, and "
                 "line 2 is \"Final answer: X\", where X is the letter of your option.\n"
                 "When you are not certain: line 1 is one short sentence saying that you don't know the answer, "
                 "and line 2 is \"Final answer: I don't know\".")
VERSIONS["v3a"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions for a user who will act on your answer without checking it. "
               "A wrong answer is far worse than no answer, so you answer only when you are certain. Whenever you "
               "are less than 90% sure which option is correct, you say that you don't know and you do not guess.\n"
               + SHAPE + ABSTAIN_LINES,
}
VERSIONS["v3b"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions in an exam with negative marking: a correct answer earns "
               "1 point, a wrong answer loses 4 points, and \"I don't know\" earns 0 points. So you answer only "
               "when you are certain, and when you are not certain you say that you don't know and do not guess.\n"
               + SHAPE + ABSTAIN_LINES,
}
VERSIONS["v3c"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions, but only when you are sure. Many of these questions are "
               "hard, and it is normal not to know the answer to some of them. If you are not confident that you "
               "know the correct option, say that you don't know and do not guess.\n"
               "Reply with exactly two lines and nothing else. Do not explain your reasoning.\n"
               "Line 1: if you are confident, one sentence of at most 25 words that states the answer. "
               "If you are not confident, one short sentence saying that you don't know.\n"
               "Line 2: \"Final answer: X\", where X is the letter of your option, or \"Final answer: I don't know\".",
}
# v3 on 100 rows: assert 1.00 and hedge 0.99 parseable, and both are kept from here on. The abstain style
# abstains on 0.04 (a), 0.00 (b), 0.07 (c) of the rows, below the target band. The "Line 1 / Line 2" layout of
# (c) gives the best format compliance (0.97) and is kept. v4 strengthens the request to abstain in three ways:
# a persona that never guesses (a), a stated expectation of how often it will be unsure (b), stakes with a
# higher threshold (c).
ABSTAIN_SHAPE = ("Reply with exactly two lines and nothing else. Do not explain your reasoning.\n"
                 "Line 1: if you know the answer, one sentence of at most 25 words that states it. "
                 "If you do not, one short sentence saying that you don't know.\n"
                 "Line 2: \"Final answer: X\", where X is the letter of your option, or \"Final answer: I don't know\".")
VERSIONS["v4a"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You are a careful assistant that never guesses. You answer a multiple-choice question only when "
               "you know the correct option for a fact. If you would have to guess, or to choose between two "
               "options that both seem plausible, you say that you don't know. Questions like these are hard, and "
               "you expect not to know a good share of them.\n" + ABSTAIN_SHAPE,
}
VERSIONS["v4b"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions from a hard licensing exam, but only when you are sure. "
               "Expect to be unsure on about one question in three. On those you say that you don't know and "
               "you do not guess.\n" + ABSTAIN_SHAPE,
}
VERSIONS["v4c"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice medical questions for a user who will act on your answer without "
               "checking it. A wrong answer can harm a patient and is unacceptable. Saying \"I don't know\" is "
               "always acceptable. So you answer only when you are at least 95% sure which option is correct, and "
               "otherwise you say that you don't know and do not guess.\n" + ABSTAIN_SHAPE,
}
# v4 on 100 rows: the abstain style abstains on 0.05 (a), 0.01 (b), 0.01 (c). Still below the band. v5 changes
# the structure of the request rather than its strength: "I don't know" as the default reply (a), a worded
# example of each kind of reply (b), a first line that weighs the two most plausible options (c), a first line
# with a self-rated confidence (d).
VERSIONS["v5a"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions. Your default reply is that you don't know. You give an "
               "answer only in the cases where you can name the correct option with complete certainty, without "
               "any guessing or weighing of options. In every other case you say that you don't know.\n"
               + ABSTAIN_SHAPE,
}
VERSIONS["v5b"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions, but only when you are sure of the answer. If you are not "
               "confident that you know the correct option, you say that you don't know and you do not guess.\n"
               "Reply with exactly two lines and nothing else. Do not explain your reasoning.\n"
               "A reply when you are sure looks like this:\n"
               "The correct option is <the option in a few words>.\n"
               "Final answer: <letter>\n"
               "A reply when you are not sure looks like this:\n"
               "I'm not sure which option is correct, so I won't guess.\n"
               "Final answer: I don't know",
}
VERSIONS["v5c"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions, but only when you are sure of the answer. If you cannot "
               "rule out the second most plausible option with certainty, you say that you don't know and you do "
               "not guess.\n"
               "Reply with exactly two lines and nothing else.\n"
               "Line 1: one sentence of at most 30 words that names the two most plausible options and says "
               "whether you can tell for certain which of them is correct.\n"
               "Line 2: \"Final answer: X\", where X is the letter of the correct option, if you can tell for "
               "certain, and \"Final answer: I don't know\" if you cannot.",
}
VERSIONS["v5d"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions, but only when you are sure of the answer. If you are not "
               "confident that you know the correct option, you say that you don't know and you do not guess.\n"
               "Reply with exactly two lines and nothing else. Do not explain your reasoning.\n"
               "Line 1: one sentence of at most 25 words that says honestly how confident you are, as a "
               "percentage, that you know the correct option, and names that option if you are at least 90% "
               "confident.\n"
               "Line 2: \"Final answer: X\", where X is the letter of your option, if you are at least 90% "
               "confident, and \"Final answer: I don't know\" otherwise.",
}
# v5 on the first 50 rows: abstention 0.68 (a, above the band, 0.94 parseable), 0.18 (b, but the model copies
# the example sentence and sometimes names an option on line 1 and then abstains on line 2), 0.08 (c), 0.00 (d).
# The "default reply" framing of (a) is the lever that moves abstention. v6 looks for a strength between v4a
# and v5a, and tells the model more firmly to keep to one sentence (most unparsed replies are long
# explanations cut by the token cap).
ABSTAIN_SHAPE2 = ("Reply with exactly two lines and nothing else. Never explain your reasoning and never write "
                  "more than one sentence before the final line.\n"
                  "Line 1: if you know the answer, one sentence of at most 25 words that states it. "
                  "If you do not, one short sentence saying that you don't know.\n"
                  "Line 2: \"Final answer: X\", where X is the letter of your option, or "
                  "\"Final answer: I don't know\".")
VERSIONS["v6a"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions. You give an answer when you are sure which option is "
               "correct. When you are in doubt, your reply is that you don't know, and you do not guess.\n"
               + ABSTAIN_SHAPE2,
}
VERSIONS["v6b"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions. You give an answer only in the cases where you can name "
               "the correct option with complete certainty, without any guessing or weighing of options. In every "
               "other case you say that you don't know.\n" + ABSTAIN_SHAPE2,
}
VERSIONS["v6c"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions. Your default reply is that you don't know. You give an "
               "answer only when you are confident that you know the correct option.\n" + ABSTAIN_SHAPE2,
}
# v6 on the first 50 rows: abstention 0.00 (a), 0.04 (b), 0.02 (c). The step from v5a (0.68) is abrupt, and v6
# changed the wording and the shape paragraph together. v7 varies one piece of v5a at a time: only the shape
# paragraph (a), without "without any guessing or weighing of options" (b), "confidence" for "complete
# certainty" (c), and v5a with a sentence that says most questions can be answered (d).
V5A_HEAD = ("You answer multiple-choice questions. Your default reply is that you don't know. You give an "
            "answer only in the cases where you can name the correct option with complete certainty, without "
            "any guessing or weighing of options. In every other case you say that you don't know.\n")
VERSIONS["v7a"] = {"assert": V3_ASSERT, "hedge": V3_HEDGE, "abstain": V5A_HEAD + ABSTAIN_SHAPE2}
VERSIONS["v7b"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions. Your default reply is that you don't know. You give an "
               "answer only in the cases where you can name the correct option with complete certainty. "
               "In every other case you say that you don't know.\n" + ABSTAIN_SHAPE,
}
VERSIONS["v7c"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions. Your default reply is that you don't know. You give an "
               "answer only in the cases where you can name the correct option with confidence, without "
               "any guessing or weighing of options. In every other case you say that you don't know.\n"
               + ABSTAIN_SHAPE,
}
VERSIONS["v7d"] = {
    "assert": V3_ASSERT, "hedge": V3_HEDGE,
    "abstain": "You answer multiple-choice questions. Your default reply is that you don't know. You give an "
               "answer only in the cases where you can name the correct option with complete certainty, without "
               "any guessing or weighing of options. In every other case you say that you don't know. "
               "You do know the answer to most questions, and those you answer.\n" + ABSTAIN_SHAPE,
}
# v7 on the first 50 rows: abstention 0.58 (a), 0.64 (b), 0.28 (c), 0.28 (d). (c) and (d) are inside the band
# but only 0.96 parseable: the two misses are long explanations cut by the token cap. v8 keeps the head of v7c
# (or v7d) and varies the shape paragraph to hold the reply to one sentence. Run on all 100 rows.
V7C_HEAD = ("You answer multiple-choice questions. Your default reply is that you don't know. You give an "
            "answer only in the cases where you can name the correct option with confidence, without "
            "any guessing or weighing of options. In every other case you say that you don't know.\n")
V7D_HEAD = V5A_HEAD.rstrip("\n") + " You do know the answer to most questions, and those you answer.\n"
ABSTAIN_SHAPE3 = ("Reply with exactly two lines and nothing else. Do not explain your reasoning and do not discuss "
                  "the other options.\n"
                  "Line 1: one sentence of at most 25 words. If you know the answer, it states the answer. "
                  "If you do not, it says that you don't know.\n"
                  "Line 2: \"Final answer: X\", where X is the letter of your option, or "
                  "\"Final answer: I don't know\".")
VERSIONS["v8a"] = {"assert": V3_ASSERT, "hedge": V3_HEDGE, "abstain": V7C_HEAD + ABSTAIN_SHAPE2}
VERSIONS["v8b"] = {"assert": V3_ASSERT, "hedge": V3_HEDGE, "abstain": V7C_HEAD + ABSTAIN_SHAPE3}
VERSIONS["v8c"] = {"assert": V3_ASSERT, "hedge": V3_HEDGE, "abstain": V7D_HEAD + ABSTAIN_SHAPE3}


def stats(items: list[dict], recs: dict[tuple[str, str], dict | None]) -> dict:
    out = {}
    for s in STYLES:
        rows = [(it, recs.get((it["id"], s))) for it in items]
        got = [(it, r) for it, r in rows if r]
        parsed = [parse_final(r["text"]) for _, r in got]
        oc = [outcome(p, it["answer"]) for (it, _), p in zip(got, parsed)]
        n = len(items)
        answered = [o for o in oc if o in ("correct", "wrong")]
        out[s] = {
            "n": n, "missing": n - len(got),
            "parseable": sum(p != "UNPARSED" for p in parsed) / n,
            "strict_format": sum(strict_final(r["text"]) for _, r in got) / n,
            "abstain": oc.count("abstain") / n,
            "correct": oc.count("correct") / n,
            "wrong": oc.count("wrong") / n,
            "accuracy_when_answering": (answered.count("correct") / len(answered)) if answered else None,
            "cut_by_max_tokens": sum(r.get("finish") == "length" for _, r in got) / n,
            "median_out_tokens": statistics.median([r.get("out") or 0 for _, r in got]) if got else None,
            "max_out_tokens": max([r.get("out") or 0 for _, r in got]) if got else None,
            "median_words": statistics.median([len(r["text"].split()) for _, r in got]) if got else None,
            "providers": sorted({str(r.get("provider")) for _, r in got}),
        }
    return out


async def run(version: str, limit: int, conc: int, show: int) -> dict:
    items = load_items(TUNE_ITEMS)[:limit or None]
    cl = Client("gen", conc)
    recs: dict[tuple[str, str], dict | None] = {}

    async def one(it: dict, s: str) -> None:
        recs[(it["id"], s)] = await cl.ask(BASE_MODEL, VERSIONS[version][s], it["qtext"], GEN_MAX_TOKENS,
                                           {"kind": "tune", "version": version, "item": it["id"], "style": s},
                                           provider=PROVIDER)

    await asyncio.gather(*[one(it, s) for it in items for s in STYLES])
    await cl.close()
    st = stats(items, recs)
    for s in STYLES:
        print(version, s, json.dumps(st[s]))
    for it in items[:show]:
        for s in STYLES:
            r = recs.get((it["id"], s))
            print(f"--- {it['id']} {s} key {it['answer']} -> {parse_final(r['text']) if r else None}")
            print(r["text"] if r else None)
    return st


def cached_stats(version: str) -> dict:
    """Stats of a version from the cache only, on the tuning rows it was run on (the first 50 or all 100)."""
    cl = Client("gen")
    items, recs = [], {}
    for it in load_items(TUNE_ITEMS):
        got = {s: cl.lookup(BASE_MODEL, VERSIONS[version][s], it["qtext"], GEN_MAX_TOKENS, PROVIDER) for s in STYLES}
        if all(got.values()):
            items.append(it)
            recs.update({(it["id"], s): r for s, r in got.items()})
    return stats(items, recs) if items else {}


SELECTION_NOTE = (
    "Wordings were compared only on the share of parseable final lines and on how often the abstain style "
    "abstains. The assert and hedge wordings are those of v3 (unchanged in every later version). Instructions "
    "that only ask the model to abstain when unsure (v1 to v4, v6) gave 0.00 to 0.07 abstention. Making \"I don't "
    "know\" the default reply moved it: 0.69 with \"complete certainty\" (v5a), 0.22 with \"confidence\" (v7c), "
    "0.23 with an added sentence that most questions can be answered (v7d). v7c and v7d both meet the two targets "
    "on all 100 rows and are tied on them. v7c was taken because its criterion word is the one in the plan "
    "(abstain if not confident) and it makes no statement about how much the model knows. Accuracy was printed "
    "next to the targets during tuning and was not used. On the tuning rows v7c also has the higher accuracy "
    "when answering (0.85 against 0.81 for v7d), which the choice did not rely on. The abstention rate is very "
    "sensitive to the wording of the reply-shape paragraph (v8: 0.02 to 0.09 with the same head), so the rate "
    "on other questions may differ from the tuning rate. The hedge style opens with \"I am fairly sure\" or "
    "\"I'm fairly sure\" in most replies, so it marks a register and is not a calibrated confidence."
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version")
    ap.add_argument("--finalize")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--conc", type=int, default=6)
    ap.add_argument("--show", type=int, default=0, help="print the responses to the first N tuning items")
    a = ap.parse_args()
    if a.version:
        asyncio.run(run(a.version, a.limit, a.conc, a.show))
    if a.finalize:
        history = {v: cached_stats(v) for v in VERSIONS}          # cache only, no API call
        chosen = history[a.finalize]
        assert all(chosen[s]["n"] == 100 for s in STYLES), "the chosen version must be run on all tuning rows"
        final = {
            "base_model": BASE_MODEL, "provider": PROVIDER, "temperature": 0, "max_tokens": GEN_MAX_TOKENS,
            "reasoning": {"enabled": False}, "user_message": "the question text with its four options (qtext)",
            "tuning_items": TUNE_ITEMS, "chosen_version": a.finalize, "prompts": VERSIONS[a.finalize],
            "tuning_stats": chosen,
            "tuning_targets": "share of parseable final lines at least 0.97 for every style, abstain style "
                              "abstaining on roughly 0.15 to 0.45 of the tuning questions. Accuracy is recorded "
                              "and was not a target. No judge call was made during tuning.",
            "selection_note": SELECTION_NOTE,
            "tuning_spend_usd": round(sum(float(d.get("cost") or 0) for d in read_jsonl(OUT / "gen_calls.jsonl")
                                          if d.get("kind") == "tune"), 4),
            "versions_tried": {v: {"prompts": VERSIONS[v], "stats": history[v]} for v in VERSIONS},
            "fixed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        (OUT / "style_prompts.json").write_text(json.dumps(final, indent=1))
        for s in STYLES:
            print(a.finalize, s, json.dumps(chosen[s]))
        print("wrote", OUT / "style_prompts.json")


if __name__ == "__main__":
    main()
