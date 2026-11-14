# Study 5, deviations from the pre-registration and notes on trust

Steps covered here: style instructions, pool, selection rules, natural-output duels, AutoScientist training.
The evaluation of the trained models (P5c to P5e) is a separate step and is not covered.

## Deviations

1. **The abstain instruction makes "I don't know" the default reply.** The plan says the third style is
   "abstain if not confident" and that its wording is tuned on train rows 2000 to 2099 for format compliance
   and abstention frequency. Instructions that only ask the model to abstain when unsure (confidence
   threshold, stakes, negative marking, a stated share of hard questions) gave 0% to 7% abstention on the
   tuning rows, below the target band of 15% to 45%. The wording that was fixed tells the model that its
   default reply is "I don't know" and that it answers only when it can name the option with confidence.
   It gives 22% abstention on the tuning rows and 21.9% on the pool. No abstention is forced by a rule, the
   model decides on every question. All 22 wordings that were tried and their statistics are in
   `style_prompts.json`.

2. **Two wordings were tied on the tuning targets.** v7c (22% abstention, 97% parseable) and v7d (23%, 97%)
   both met the targets on all 100 rows. v7c was taken because its criterion word is the one in the plan
   ("confident") and it adds no statement about how much the model knows. Accuracy was printed next to the
   targets during tuning. It was not a criterion, but v7c also has the higher accuracy when answering on the
   tuning rows (0.85 against 0.81), so the choice cannot be shown to be blind to it.

3. **No price quote exists for a training run.** The Adaption API (SDK 0.19, the latest release) has no
   endpoint that prices an AutoScientist run and none that returns the credit balance. The only call before
   launch is `recommend_hyperparams`. The runs were launched without a quote. The run records returned by the
   API carry no cost field, so credits used are not known from the API.

4. **The K and R runs were launched about 19 minutes before the J and F runs.** K and R need no judge call,
   so their sets were written and uploaded while the judge round robins were still running. The files were
   written by the functions of `src/loop_select.py` and are byte-identical to the ones the full script wrote
   at its end (checked by hash). All four runs use the same model, settings and recommended hyperparameters.

5. **Natural-output duels reuse 328 judge calls of rule J.** For Claude Haiku 5.5, one of the two orders of
   every assert-against-abstain duel is the same request (model, instruction, prompt, token cap) as a duel of
   the J round robin. Those verdicts were copied from `judge_calls.jsonl` and not requested again. They are
   marked `reused_from` in `natural_calls.jsonl`.

## Notes that limit what the numbers mean

- **Base model and provider.** `qwen/qwen3.5-9b` on OpenRouter, provider pinned to Together (no fallback),
  temperature 0, reasoning off, at most 200 output tokens. All 4,500 pool responses came from Together.
  OpenRouter lists the quantisation of this endpoint as unknown.

- **Format compliance of the abstain style is 96.8% on the pool** (97% on the tuning rows, the target was at
  least 97%). 48 abstain-style responses are long explanations cut by the token cap, with no final line.
  They stay in the pool as candidates, as the plan keeps one of the three responses per question. The judge
  likes them: 35 of the J set and 29 of the F set are such cut responses (K 7, R 21). A model trained on J or F
  therefore sees about 2% of completions that end mid-sentence without a final line.

- **The three styles differ in length, not only in register.** Median words when the response answers:
  assert 20, hedge 27, abstain style 30 (mean 37). J keeps the longest of the three candidates on 857 of
  1,500 questions and takes 55.5% of its set from the abstain style. So J is not a pure test of tone.

- **The abstention is a bare "I don't know."** 305 of the 328 abstentions are exactly
  "I don't know.\nFinal answer: I don't know", against a one-sentence answer with a reason. b_nat and a_nat
  therefore measure a short non-answer against an explained answer. They do not show how a judge treats a
  fuller, more helpful abstention.

- **The hedge style is a fixed phrase.** 94% of hedge-style responses open with "I am fairly sure" or
  "I'm fairly sure". It marks a register and is not a calibrated confidence.

- **Abstention is only weakly tied to not knowing.** On the 328 questions where the abstain style abstains,
  the assert style is correct on 72.3%, against 81.6% on the other questions.

- **Rule F has many unparsed verdicts.** With the `accuracy` instruction Claude Haiku 5.5 does not reply with
  a letter in 622 of 4,500 duels (13.8%, against 126 or 2.8% with the default instruction). In 486 of the 622
  both responses name the same option, and the reply starts "Both responses give the same answer" and is cut
  at 16 tokens. As in the common setup, an unparsed verdict is dropped: it gives no win to either side. Rule
  F then has a tie for most wins on 361 questions (J on 164), and those are settled by the seed. Instruction
  and token cap were not changed after this was seen.

- **21 questions have the same text in two styles.** Their duel is between identical responses.

- **The platform win rate is recorded as returned.** The API does not say what the trained model is compared
  with or on which rows, so `best_win_rate` is not interpreted here.

## Spend

OpenRouter, from `usage.cost` of every call: generation 0.4693 USD (tuning 0.1603, pool 0.3090), judge round
robins 0.4995 USD, natural-output duels 0.0853 USD. Total 1.0541 USD, under the caps set for these steps
(0.80, 0.80, 0.40 and 2.00 in total).
