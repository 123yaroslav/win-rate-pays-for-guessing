# Paper A. Verified related work

Checked on 14 Nov 2026. This file replaces the unverified table in `idea_A_judge_confidence.md`.

How each source was opened. Metadata (title, authors, dates, venue comment, abstract) came from the arXiv listing record of each id. Numbers came from the full text (arXiv HTML or the PDF), downloaded and searched directly, not from a summary. Published versions were opened on the ACL Anthology or on the publisher page. Every quoted string below was copied from the source. The BibTeX entries are in `paper_A/refs.bib` (45 entries, compiles with `plainnat`, all 45 URLs return HTTP 200).

Our claim, for reference. In duels without a reference answer an LLM judge prefers an assertive wrong answer to "I don't know" in most cases, even on items the judge answers correctly itself. With a = rate at which a right answer beats the abstention and b = rate at which a wrong answer beats it, a policy that always answers with accuracy p wins with probability b + p(a - b). We also test instruction fixes and a selection loop in which fine-tuning on judge-selected answers removes abstention.

## 1. Papers named in the earlier notes

### 1.1 Bibliographic record

| Key | Authors | Exact title | Year and venue | arXiv id and URL |
|---|---|---|---|---|
| `lee2025ember` | Dongryeol Lee, Yerin Hwang, Yongil Kim, Joonsuk Park, Kyomin Jung | Are LLM-Judges Robust to Expressions of Uncertainty? Investigating the effect of Epistemic Markers on LLM-based Evaluation | 2025, NAACL 2025 Long Papers, pages 8962 to 8984 (ACL Anthology record opened) | 2410.20774, https://aclanthology.org/2025.naacl-long.452/ |
| `datta2026tiebreaker` | Rajashik Datta, Sanjan Baitalik | Confidence as a Tie-Breaker: Reassessing Multilingual Hedging Bias in LLM-as-a-Judge Evaluation | 2026, ACL 2026 Student Research Workshop, pages 393 to 402 | no arXiv id, https://aclanthology.org/2026.acl-srw.33/ |
| `yin2026judge` | Youbing Yin, Jingyu Wu, Anoop Kumar, Scott Novotney, Daben Liu, Erin Babinsky | The Judge Can Debias Itself: Awareness and Self-Debiasing for Reliable LLM-as-a-Judge | 2026, arXiv preprint (16 Oct 2026), no venue stated | 2610.24320, https://arxiv.org/abs/2610.24320 |
| `kalai2025hallucinate` | Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, Edwin Zhang | Why Language Models Hallucinate | 2025, arXiv preprint (4 Sep 2025) | 2509.04664, https://arxiv.org/abs/2509.04664 |
| `kalai2026evaluating` | same four authors | Evaluating large language models for accuracy incentivizes hallucinations | 2026, Nature 653, pages 1047 to 1051, online 22 Apr 2026 | doi 10.1038/s41586-026-10549-w, https://www.nature.com/articles/s41586-026-10549-w |
| `zhou2024relying` | Kaitlyn Zhou, Jena D. Hwang, Xiang Ren, Maarten Sap | Relying on the Unreliable: The Impact of Language Models' Reluctance to Express Uncertainty | 2024, ACL 2024 Long Papers, pages 3623 to 3643 | 2401.06730, https://aclanthology.org/2024.acl-long.198/ |
| `leng2024taming` | Jixuan Leng, Chengsong Huang, Banghua Zhu, Jiaxin Huang | Taming Overconfidence in LLMs: Reward Calibration in RLHF | 2024, arXiv preprint. No venue on the arXiv record | 2410.09724, https://arxiv.org/abs/2410.09724 |
| `belem2026may` | Catarina G Belem, Shang Wu, Hongyu Yao, Mark Steyvers, Sameer Singh, Padhraic Smyth | From 'May' to 'Is': Certainty Distortion in Language Model Rewriting | 2026, arXiv comment "Accepted at EMNLP 2026 (Main)" | 2606.07951, https://arxiv.org/abs/2606.07951 |
| `pan2024spontaneous` | Jane Pan, He He, Samuel R. Bowman, Shi Feng | Spontaneous Reward Hacking in Iterative Self-Refinement | 2024, arXiv preprint | 2407.04549, https://arxiv.org/abs/2407.04549 |
| `krumdick2025nofree` | Michael Krumdick, Charles Lovering, Varshini Reddy, Seth Ebner, Chris Tanner | No Free Labels: Limitations of LLM-as-a-Judge Without Human Grounding | 2025, arXiv preprint (v4 of 28 Sep 2026) | 2503.05061, https://arxiv.org/abs/2503.05061 |
| `song2025hallucinationtax` | Linxin Song, Taiwei Shi, Jieyu Zhao | The Hallucination Tax of Reinforcement Finetuning | 2025, arXiv preprint | 2505.13988, https://arxiv.org/abs/2505.13988 |
| `wu2025behaviorally` | Jiayun Wu, Jiashuo Liu, Zhiyuan Zeng, Tianyang Zhan, Tianle Cai, Wenhao Huang | Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning | 2025, arXiv preprint (v3 of 28 Jan 2026) | 2512.19920, https://arxiv.org/abs/2512.19920 |
| `tapwal2026faithful` | Riya Tapwal, Abhishek Kumar, Carsten Maple | Faithful or Fabricated? A Causal Framework for Rationalization Bias in LLM Judges | 2026, arXiv preprint | 2605.23970, https://arxiv.org/abs/2605.23970 |

### 1.2 What each did and did not do

"Did not" is relative to our three claims: a wrong answer against an abstention under a pairwise LLM judge, a break-even accuracy, and a selection loop.

| Key | What they did (at most one quoted number) | What they did not do |
|---|---|---|
| `lee2025ember` | Built EMBER (2,000 reference-guided QA items and 823 pairwise instruction-following items) and showed that five judges penalise outputs carrying uncertainty markers. In the pairwise split with no reference in the prompt, when the correct output carries a weakener and the incorrect one a strengthener, Llama-3-8B-Instruct still picks the correct output in "52.2" percent of pairs (Table 3, GPT-4o "90.3"). | The marked response always states an answer. There is no abstention. Even in the worst cell the judge prefers the correct output. No break-even analysis, no training. |
| `datta2026tiebreaker` | One judge (GPT-4o-mini) with a reference answer in the prompt, 5,120 short factual items in four language varieties. When both answers are correct "the judge prefers the assertive answer in 1,276 of 1,280 cases". | Reference always given. When the hedged answer is correct and the assertive one wrong, the assertive one wins only 2 of 1,280 times. No abstention, no theory, no training. |
| `yin2026judge` | Three judges, seven bias types, 500 items each. Their confidence-bias set rewrites TruthfulQA pairs so that the incorrect answer is assertive and the correct one hedged. Under standard prompting gpt-oss-120b picks the correct answer with accuracy ".924" (Claude Opus 4.6 .990, Gemma 4 26B A4B .928) and self-debiasing raises it to .962. | The correct answer is hedged, not withheld. Judges pick the correct answer in 92 to 99 percent of pairs. No abstention, no break-even, no training. |
| `kalai2025hallucinate` | Argue that "Under binary grading, abstaining is strictly sub-optimal" (Observation 1) and propose explicit confidence targets in the instructions, where "mistakes are penalized t/(1−t) points". | The grader is a fixed scoring rule. No pairwise or win-rate grading and no measurement of an LLM grader. Two remarks point our way without data. A table footnote says "Grading is performed using language models, hence incorrect bluffs may occasionally be scored as correct", and the appendix reads the WildBench rubric and conjectures that an IDK response "may be scored (3-4), lower than a fair response with factual errors or hallucinations (5-6)". |
| `kalai2026evaluating` | Journal version of the same argument with an experiment on SimpleQA, "which comprises 4,326 factual questions", under closed and open rubrics. | Same limits. Grading uses the standard SimpleQA grader with ground truth. |
| `zhou2024relying` | Show that deployed models rarely express uncertainty, that human preference datasets disfavour weakeners, and that the OpenAssistant reward model gives weakeners an "average rewards score of -1.86" (plain statements 4.03, strengtheners 0.82). | Human annotators and a reward model trained on them, not an LLM judge. Hedged answers, not abstention against a wrong answer. No controlled training run. |
| `leng2024taming` | Show that reward models used for PPO "exhibit inherent biases towards high-confidence scores regardless of the actual quality of responses" and propose two calibrated PPO variants, one of which "reduces ECE by 6.44 points" on GSM8K. | A numeric confidence score appended to the response, judged by reward models. No abstention, no pairwise LLM judge. |
| `belem2026may` | Measure how rewriting by language models changes expressed certainty and find that "certainty distortion affects up to 75% of LM outputs", more often upward. | The LLM judge is only the measuring instrument. No link to judge preferences, win rate or training data. |
| `pan2024spontaneous` | On essay editing, iterative refinement against an LLM evaluator raises the evaluator's ratings while quality by human judgment "remains stagnant or even decreases" (no single headline number). | Essays, in-context refinement. Nothing on correctness, confidence or abstention, and no fine-tuning. |
| `krumdick2025nofree` | Collect expert correctness labels for "1,200 responses" and show that without a reference "judges show high agreement with human experts only on questions the judges were able to correctly answer themselves". | Does not ask which response a judge prefers when it cannot verify. No abstention. Our result holds even on items the judge answers correctly, which this paper does not test for abstentions. |
| `song2025hallucinationtax` | Show that reinforcement fine-tuning "could reduce model refusal rates by more than 80%" on unanswerable questions, and that mixing in 10% unanswerable problems restores refusal. | The reward is rule-based ("we implement a rule-based reward function"), not an LLM judge. No pairwise comparison. |
| `wu2025behaviorally` | Train Qwen3-4B-Instruct with strictly proper scoring rules so that it abstains or flags uncertain claims, with a "log-scale Accuracy-to-Hallucination Ratio gain (0.806)" against GPT-5's 0.207 on BeyondAIME. | A training reward computed against ground truth, not a judging protocol. No pairwise judge. |
| `tapwal2026faithful` | Five open-weight judges of 7 to 9 billion parameters rank pairs of summaries from "a new dataset of 1,000 summaries" under cue interventions, one of which rewrites a summary to sound more assertive. | Summarisation, not question answering. No abstention, no break-even, no training. |

### 1.3 Where the sources differ from the earlier notes

1. arXiv 2605.23970 is not titled "Confidence Attack". Its title is "Faithful or Fabricated? A Causal Framework for Rationalization Bias in LLM Judges". "Robustness to a Confidence Attack" is the heading of its Section V-I.
2. Belem et al. The notes say 30 to 75% of paraphrases change certainty. The paper says "up to 75%". The figure of 30% in the paper refers to prior work on human science communication ("around 30% of human-written scientific findings are inflated").
3. Li et al., "Gaming AI-Assisted Peer Reviews" (arXiv 2606.10159, `li2026gaming`). The notes say success above 60%. The abstract says "an attack-success-rate of about 38%" and "more than 50%" when the original review suggests reject.
4. Yin et al. report accuracies (.990, .924, .928). The wrong-pick rates in the notes (1.0%, 7.6%, 7.2%) are one minus those accuracies. That arithmetic is ours, not the paper's.
5. EMBER. The numbers in the notes are correct (Table 3, drops of 3.0 and 24.8 points, and a drop of 19.0 points for GPT-4o in reference-guided QA). The largest pairwise drop is in a different cell, a weakener on the correct output against a plain incorrect output (30.2 points for Llama-3-8B-Instruct, 5.0 for GPT-4o).
6. Ye et al. (CALM, `ye2024justice`). Its 12 biases are position, verbosity, compassion-fade, bandwagon, distraction, fallacy-oversight, authority, sentiment, diversity, chain-of-thought, self-enhancement and refinement-aware. None concerns hedging, confidence or abstention. Its authority bias is a fake citation.
7. Everything else in rows 1 to 12 of the earlier table matched the sources.

## 2. Fresh novelty search

### 2.1 Web queries

| # | Query | Closest hits | Opened |
|---|---|---|---|
| 1 | "LLM judge" abstention "I don't know" pairwise preference wrong answer | SCOPE, cascaded selective evaluation. Both concern a judge that abstains, not an answer that abstains | SCOPE abstract |
| 2 | LLM-as-a-judge penalizes abstention prefers confident incorrect answer over "I don't know" | Datta and Baitalik, I-CALM, Burns, a practitioner blog | all four |
| 3 | judge prefers incorrect answer over refusal LLM evaluator abstain bias arXiv 2026 | Zhang et al. (Diverging Preferences), Pasch (2505.15365), Wagner (2607.08456) | first two in full, third abstract |
| 4 | "win rate" abstention hallucination evaluation LLM judge pairwise guessing incentive | Mohsin et al., Kalai et al. in Nature, PhantomBench | first two in full |
| 5 | Chatbot Arena LMArena refusal penalty votes users penalize refusals | Pasch (2501.03266) | full text |
| 6 | AbstentionBench LLM judge abstention evaluation reasoning models | Kirichenko et al. | full text |
| 7 | "abstain" "LLM evaluator" bias uncertain answers scored lower than incorrect answers | nothing new | abstracts |
| 8 | preference optimization RLAIF LLM judge feedback reduces abstention increases hallucination | CATTO, nothing direct | CATTO abstract |
| 9 | synthetic data filtering by LLM judge removes "I don't know" responses fine-tuning | nothing direct | none |
| 10 | proper scoring rule pairwise LLM judging abstention incentive-compatible win rate | SCOPE. Two other hits (arXiv 2510.00263, 2508.05469) were not opened and are not cited | SCOPE abstract |
| 11 | LLM judge "abstention" versus "incorrect answer" head-to-head "break-even" accuracy | Ravikumar (2609.17686), a threshold analysis for benchmark scoring rules | full text |
| 12 | sycophancy overconfidence emerges from optimizing against LLM judge or user preferences | Shapira et al., Sharma et al. | abstracts |
| 13 | LLM judge pairwise "I don't know" loses to hallucinated answer unanswerable questions | Remeli and Hardt, Tu et al. | first in full, second abstract |
| 14 | "abstention" "wrong answer" preferred "even when the judge knows the answer" pairwise 2026 | judge-side abstention only | abstracts |
| 15 | Arena-Hard OR AlpacaEval OR MT-Bench LLM judge refusal "I don't know" penalized | Zheng et al. (null models). Nothing on abstention | abstract |
| 16 | reward model OR "LLM judge" selects training data, abstention removed | the same blog, Mohamadi et al. | both |
| 17 | LLM judge rates "I don't know" lower than incorrect answer experiment (extended search) | nothing direct | none |
| 18 | best-of-N selection by LLM judge, fine-tuning eliminates refusals | Landesberg (2603.12520). Nothing on abstention | abstract |
| 19 | site:lesswrong.com OR site:alignmentforum.org, same topic | no forum posts returned | none |
| 20 | "judges" "prefer" hallucinated answers over abstentions, medical, 2026 (extended search) | Afrasyab (2607.18828), MedAbstain (2601.12471). Neither compares an abstention with a wrong answer in a duel | abstracts |
| 21 | LLM-as-a-judge "epistemic humility" OR "admitting ignorance" scored lower than "incorrect" | Tripathi et al. | full text |
| 22 | "IDK" "pairwise" "judge" "win rate" abstaining model loses arena-style evaluation | nothing direct | none |

### 2.2 arXiv listing search (abstract field, sorted by date)

| Query | Results | Relevant |
|---|---|---|
| "judge" AND "abstention" AND "pairwise" | 6 | none on answer-side abstention |
| "LLM-as-a-judge" AND "abstention" | 11 | none |
| "judge" AND "I don't know" AND "incorrect" | 1 | LACIE |
| "judge" AND "abstain" AND "win rate" | 0 | |
| "LLM judges" AND "refusal" AND "prefer" | 5 | Wedgwood et al. (2603.03319) on refusal of sensitive requests |
| "judge" AND "abstention" AND "hallucination" AND "prefer" | 0 | |
| "judges" AND "penalize" AND "abstention" | 1 | unrelated |
| "evaluator" AND "abstention" AND "confident" AND "wrong" AND "prefer" | 1 | LACIE |
| "judge" AND "refusal" AND "incorrect answer" AND "pairwise" | 0 | |
| "Chatbot Arena" AND "refusal" | 3 | the two Pasch papers |
| "LLM-as-a-judge" AND "I don't know" | 1 | unrelated |
| "judge" AND "epistemic markers" | 1 | EMBER |
| "judge" AND "overconfidence" AND "reward" AND "abstain" | 0 | |
| "preference" AND "abstention" AND "fine-tuning" AND "judge" | 1 | unrelated |
| "LLM judge" AND "uncertainty expression" | 0 | |

### 2.3 Closest prior work and how it overlaps

No source found shows that a wrong answer beats an abstention under an LLM judge with the truth known. The nearest results, in order of closeness:

| Key | Setup and number | Overlap | Difference |
|---|---|---|---|
| `pasch2025aivshuman` (arXiv 2505.15365) | 49,938 single-turn Chatbot Arena pairs re-judged pairwise by GPT-4o and Llama 3 70B with the prompt format of Zheng et al. (2023). Table 1 gives technical refusals a win rate of 0.27 and a loss rate of 0.59 under GPT-4o (0.24 and 0.66 under Llama 3 70B), against 0.46 and 0.50 wins for normal responses. | Pairwise LLM judges penalise responses that decline for lack of ability. This is the closest precedent and must be cited. | Observational. The correctness of the opposing response is unknown, so a penalty for declining is not separated from a reward for being right. Open-domain prompts, not keyed questions. No break-even, no training. The paper's own headline is the opposite direction for ethical refusals, which judges rate more favourably than users do. |
| `kalai2025hallucinate` | Reading of the WildBench rubric (quoted in 1.2). | States the hypothesis that an LLM-graded rubric may score IDK below a response with errors. | A conjecture from the rubric text. No judge was run. Pointwise rubric, not pairwise. |
| `lee2025ember`, `datta2026tiebreaker`, `yin2026judge` | Hedged correct answer against assertive wrong answer (numbers in 1.2). | Judges dislike uncertainty markers and use assertiveness as a tie-breaker. | The hedged response still answers. In all three the correct hedged answer beats the wrong assertive one in most pairs, from 52.2 percent for the weakest judge in EMBER to 1,277 of 1,280 in Datta and Baitalik. An abstention removes the answer, and that case is untested. |
| `tripathi2025pairwise` (arXiv 2504.14716, COLM 2025) | Adds assertiveness, prolixity or sycophancy to the weaker response. "Pairwise preferences flip in about 35% of the cases, compared to only 9% for absolute scores." | Pairwise protocols are more exposed to assertive style than pointwise scores. Supports our pointwise check. | Instruction following only. The limitations say "this can be extended to other aces of evaluation like factuality or reasoning" (wording as in the source). No abstention. |
| `zhang2025diverging` (arXiv 2410.14632, ICML 2025) | On comply against refuse pairs with diverging human preferences, "WildBench's LLM-as-Judge method for scoring completions consistently prefers the complying response 100% of the time" (21 examples). | LLM judges favour compliance over refusal. | Safety and capability refusals on contested prompts. No correctness key. |
| `remeli2026correct` (arXiv 2606.09409, ICML 2026) | Pairwise judging without a reference on five benchmarks with ground truth. "Elo rankings achieve a Spearman correlation above 0.9 with accuracy rankings". | The positive counterpart to our result. It agrees with our finding that judges rarely prefer a wrong answer to a right one. | It does not analyse pairs where one response declines. Its only remark on unattempted answers concerns a pointwise judge that "labels 76.7% of ground-truth not_attempted responses as incorrect". |
| `lmsys2023leaderboard`, `pasch2025refusals` | Human voters. "casual users are more likely to penalize abstention over subtly inaccurate responses" (LMSYS, a rough estimate for PaLM 2). Ethical refusals: "win rate drops to 8%, compared to 36% for normal responses" (Pasch). | Human pairwise votes penalise refusals. | Human voters, not LLM judges. Correctness uncontrolled. |
| `mohsin2025limits` | Survey text: benchmarks and reward models "penalize abstention and reward guessing" and "This phenomenon is exacerbated by LM-as-judge evaluation". | States the direction. | An assertion with a citation on length bias. No measurement. |
| A practitioner blog (tianpan.co, 27 Apr 2026, not in the .bib) | Says judges "systematically score confident wrong answers higher than honest hedging" and cites "one widely-cited result" without naming it. It also describes the authority bias of CALM as confident outputs beating hedged ones, which is not what CALM measures (see 1.3 item 6). | Same intuition in public. | No data and no checkable source. |

For the selection loop the neighbours are `song2025hallucinationtax` (rule-based reward erodes refusal), `stengeleskin2024lacie` (preference optimisation on data from a game between a speaker and a simulated listener, which leads to "an emergent increase in model abstention", the opposite direction to ours because its preferences use ground-truth correctness together with the listener's acceptance), `pan2024spontaneous`, `sharma2023sycophancy` ("Optimizing model outputs against PMs also sometimes sacrifices truthfulness in favor of sycophancy"), `hosking2024human`, `wen2024mislead`, `williams2025targeted` and `shapira2026rlhf`. None fine-tunes on answers selected by a pairwise LLM judge and measures abstention.

For instruction fixes on the answering model the neighbours are `mohamadi2025honesty` (on GSM8K, MedQA and GPQA "frontier models almost never abstain despite explicit warnings of severe penalties") and `zong2026icalm`. For fixes on the judge they are `yin2026judge` and Appendix D of `lee2025ember`, where task-specific prompts help but "neither approach is entirely successful".

Verdict. No part of the three claims is scooped. Two wordings need care. Do not write that nobody has shown LLM judges penalising refusals, because Pasch shows it in Arena data. Do not present the incentive to guess under LLM grading as a new idea, because Kalai et al. state it as a conjecture. The new result is the controlled measurement with a key (a and b), the break-even reading of win rate, and the loop.

## 3. Suggested related-work paragraph

Ready for `paper_A/main.tex`. The one number is from Table 3 of EMBER.

> \citet{kalai2025hallucinate,kalai2026evaluating} show that accuracy grading gives a wrong answer and an abstention the same score, so guessing is never worse, but their graders are fixed scoring rules, and for rubrics graded by a language model they only conjecture that ``I don't know'' may score below a flawed answer. Studies of epistemic markers put hedged and assertive answers before LLM judges \citep{lee2025ember,datta2026tiebreaker,yin2026judge} and find that judges penalise uncertainty markers and use assertiveness as a tie-breaker, but the hedged response still names an answer, and the correct hedged answer keeps beating the assertive wrong one (GPT-4o picks it in 90.3\% of such pairs in EMBER). \citet{tripathi2025pairwise} find that pairwise protocols are swayed by assertive style far more than absolute scores, but they test instruction following, not correctness or abstention. Chatbot Arena data show that refusals lose pairwise comparisons, with human voters \citep{lmsys2023leaderboard,pasch2025refusals} and with GPT-4o and Llama~3 as judges \citep{pasch2025aivshuman}, but the correctness of the competing response is unknown there, so a penalty for declining cannot be separated from a reward for being right. \citet{remeli2026correct} report that rankings from pairwise LLM judging agree with accuracy rankings on benchmarks with ground truth, but they do not examine pairs in which one response declines to answer. On the training side, human preference data, reward models and reinforcement fine-tuning are known to push models away from expressed uncertainty and refusal \citep{zhou2024relying,leng2024taming,hosking2024human,sharma2023sycophancy,song2025hallucinationtax}, and refinement against an LLM evaluator drifts from human judgment \citep{pan2024spontaneous}, but none of these selects training data with a pairwise LLM judge and measures abstention afterwards. To our knowledge no prior work measures how often an LLM judge prefers a wrong answer to an explicit abstention when the key is known, derives the accuracy at which answering starts to pay under win rate, or shows that fine-tuning on judge-selected answers removes abstention.

## 4. Datasets

| Key | Record | Checked on |
|---|---|---|
| `jin2021medqa` | Di Jin, Eileen Pan, Nassim Oufattole, Wei-Hung Weng, Hanyi Fang, Peter Szolovits. "What Disease Does This Patient Have? A Large-Scale Open Domain Question Answering Dataset from Medical Exams". Applied Sciences 11(14), 6421, 2021. doi 10.3390/app11146421. arXiv 2009.13081. The abstract calls MedQA a dataset "collected from the professional medical board exams" with 12,723 English questions. | arXiv record and Crossref record of the journal article |
| `hendrycks2021mmlu` | Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, Jacob Steinhardt. "Measuring Massive Multitask Language Understanding". arXiv 2009.03300, arXiv comment "ICLR 2021". "The test covers 57 tasks". | arXiv record |

## 5. Other verified entries in the .bib

All opened as arXiv records unless stated. `zheng2023judging` (MT-Bench and Chatbot Arena, NeurIPS 2023 Datasets and Benchmarks per arXiv comment), `chiang2024chatbotarena`, `zheng2025cheating` (a constant response reaches "an 86.5% LC win rate on AlpacaEval 2.0"), `badshah2026scope` (the judge abstains, not the answer), `tu2026reasoning` (ACL 2026, weak judges accept incorrect answers that come with fluent reasoning), `wen2024knowlimits` (survey of abstention), `kirichenko2025abstentionbench` ("reasoning fine-tuning degrades abstention (by 24% on average)"), `wei2024simpleqa` (answers graded "correct, incorrect, or not attempted"), `burns2025guessing`, `ravikumar2026missing` (break-even threshold for scoring rules with an abstain reward), `ye2024justice`, `wahi2026optimizing`, `landesberg2026bestofn`, `parikh2026catto`, `li2026gaming`.

## 6. Not verified, left out of the .bib

- Chow (1970), the classical reject-option threshold that Ravikumar cites. The IEEE page returned an empty response, so it was not opened.
- Peters and Chin-Yee, Xiao et al., and the OpenAI sycophancy postmortem from the "search only" list of the earlier notes. Not opened.
- ICLR 2025 as the venue of Leng et al. Not stated on the arXiv record, so the entry is an arXiv preprint.
- arXiv 2510.00263 and 2508.05469 (proper scoring rules for judges). Seen in search results only.

## 7. Note for the draft

The Related Work section of `paper_A/main.tex` still cites `todo_placeholder`, which is no longer in the .bib. It prints as an undefined citation until the paragraph in section 3 replaces the TODO.
