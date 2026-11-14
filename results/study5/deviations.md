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

- **The platform win rate is recorded as returned.** `best_win_rate` is 0.0528 (J), 0.0461 (F), 0.0919 (K) and
  0.0915 (R), all far below the platform target of 0.7. The API does not say what the trained model is
  compared with or on which rows, so the number is not interpreted here. The run stops after the one
  iteration that was asked for, whatever the win rate.

- **The training dose is small.** The platform's recommended settings give one epoch of 22 optimiser steps
  on the 1,500 rows (LoRA rank 16, alpha 32, all linear modules, peak learning rate 5e-5, cosine schedule,
  loss on the completion only). The training loss falls from about 1.9 to about 0.5 (`trainer_state.json` in
  every adapter folder). If the trained models differ little, a weak dose is one of the explanations.

- **The adapters name a private base.** `adapter_config.json` has `base_model_name_or_path`
  `togethercomputer/Qwen3.5-9B`. The run was requested on `Qwen/Qwen3.5-9B`, so the evaluation has to load
  the public weights under that name and assumes the two are the same model.

- **One run per rule.** The plan allows a second run per rule if time and credits allow. It was not made, so
  the variation between two trainings of the same set is not known.

## Spend

OpenRouter, from `usage.cost` of every call: generation 0.4693 USD (tuning 0.1603, pool 0.3090), judge round
robins 0.4995 USD, natural-output duels 0.0853 USD. Total 1.0541 USD, under the caps set for these steps
(0.80, 0.80, 0.40 and 2.00 in total).

## Follow-up runs (post hoc)

This part was designed after the registered evaluation was seen (`eval_table.md`). It is exploratory and is
not covered by the pre-registration. The registered runs J, F, K and R, their adapters in `adapters/` and
their results stay as they are and are reported as registered.

What was seen. None of the four trained models abstains on any of the 300 test questions, and 10% to 15% of
their outputs have no final line. The K and R training sets hold only 4.3% and 7.0% abstentions, and one
epoch is 22 optimiser steps, so the registered design could not show a difference in abstention between
the trained models.

What changes in the follow-up.

- **A new rule C, the cautious policy with no selection.** For every one of the 1,500 pool questions the
  abstain-style response is kept as it is, with its abstentions and its unparsed responses. Nothing is
  filtered, and no judge and no key is used. The set is `train_C.jsonl`: 21.9% abstentions (328), 65.1%
  correct (977), 9.8% wrong (147), 3.2% unparsed (48). Its composition next to J and K is in
  `selection_table_followup.md`.
- **Three epochs.** Three runs, C, J and K, on `Qwen/Qwen3.5-9B` with the recommended hyperparameters of the
  registered runs (LoRA rank 16, alpha 32, all linear modules, peak learning rate 5e-5, cosine schedule, loss
  on the completion only) and `n_epochs = 3` in place of 1. One iteration, no augmentation. J and K reuse the
  datasets uploaded for the registered runs.
- **Where things go.** Ledger records of the follow-up carry `"followup": "e3"` in
  `autoscientist_runs.jsonl`. Adapters go to `adapters_e3/{C,J,K}/`, a folder kept out of the repository.

Status. The C set is built and uploaded (dataset `975dd325-e4ad-4a89-8349-18a8eefb2cd3`), and the platform
recommends for it the same hyperparameters as for the other sets. The three runs have not been launched:
the launch command was not permitted in the session that prepared them. Nothing was sent to the training
API beyond the upload and the hyperparameter request, and no run exists. This paragraph is to be replaced
by run ids, win rates, wall times and losses once the runs are made.

## Follow-up on a rented GPU (post hoc, written before any follow-up model was trained)

The follow-up described above was not launched on AutoScientist. It is run instead as direct LoRA training
on the rented GPU that already serves the evaluation, with the same base model and one script for all arms.

Design, fixed on 2026-11-15 at 00:50 local time, after the registered evaluation was seen and before any
follow-up training:

- Arms: C (the cautious style's response to every pool question, no selection), J (judge, default
  instruction), K (by the key), R (random). Training files are the existing `train_{C,J,K,R}.jsonl`.
- Training: LoRA rank 16, alpha 32, all linear projection modules, three epochs, batch size 16, learning rate
  1e-4 with 10% warm-up and cosine decay, loss on the completion only, the chat format of the evaluation with
  no system prompt, one fixed seed. Identical for all arms.
- Evaluation: the registered one (300 MedQA test questions, no system prompt, greedy decoding, final line).
- Predictions: the C model abstains on at least 10% of the test questions, the J model on at most 2%, and
  the J model has a higher wrong-answer rate than the C model (paired bootstrap, 0.05). If the C model does
  not abstain either, the follow-up shows that abstention does not survive this fine-tuning at all, and the
  report says so.

The registered runs and their results stay as they are. The follow-up is reported as exploratory.

### Outcome of the follow-up on the rented GPU (added after the run, the design text above is unchanged)

What was run, on 14 November 19:50 to 22:13 UTC (15 November local time). `src/gpu_train_lora.py` trained four
adapters on the pod, C3, J3, K3 and R3, from `train_{C,J,K,R}.jsonl`. `src/gpu_eval.py` evaluated them as
registered: the 300 test questions, no system prompt, greedy decoding, batch 16, at most 300 new tokens.
`src/loop_eval_followup.py` wrote `eval_table_followup.md` and `eval_table_followup.json`. The loss of every step
is in `followup_train_log_<arm>.json`, the log of the pod is `followup_run.log`, times and money are in
`runpod_log.md` (step 3, about 1.45 USD).

Settings actually used, identical for the four arms.

- Base `Qwen/Qwen3.5-9B` at revision `c202236235762e1c871ad0ccb60c8ee5ba337b9a`, the text tower in bfloat16, the
  class the evaluation loads. The base weights were read from disk again for every arm.
- LoRA rank 16, alpha 32, dropout 0, on the q, k, v, o, gate, up and down projections: 256 tensors, 29.1 million
  parameters, the same modules as in the service adapters.
- Three epochs over the 1,500 rows, 16 examples per optimiser step, 282 steps (the last step of an epoch has
  12 examples). AdamW, peak learning rate 1e-4, 29 warm-up steps (10%), cosine decay to zero.
- Loss on the completion and the closing `<|im_end|>` token only, averaged over the tokens of a step.
- Format: the prompt that `gpu_eval.py` builds (one user turn with the question text, no system prompt, thinking
  off), then the completion, then `<|im_end|>`. The script compares its prompts with `gpu_eval.render` and prints
  one training example and one evaluation prompt (`followup_run.log`). The chat template renders the two turns to
  the same text.
- Seed 20261115 for the initial adapter weights and for the data order. All files hold the same questions in the
  same row order, so every step shows the same 16 questions to every arm.
- Nothing is truncated. The longest example has 846 tokens in C, 764 in J and 755 in K and R.

Choices the design left open, made before training: weight decay 0, AdamW betas 0.9 and 0.999, gradient clipping
at norm 1, adapter weights in float32 under bfloat16 autocast, and a warm-up that starts at learning rate 0, so
the first step does not move the weights.

Departures from the fixed design.

1. **A step of 16 examples is computed in several forward passes.** One pass over 16 examples does not fit in the
   48 GB of the card. The backward pass takes about 14.5 MB per token: two examples with 1,692 padded tokens peak
   at 41.3 GB, and four examples run out of memory. The script packs the 16 examples of a step, longest first,
   into passes of at most 1,500 padded tokens (about four passes per step) and adds up the gradients. The loss of
   a step is the sum over all completion tokens of its 16 examples divided by their number, so the optimiser step
   is the one a single batch of 16 gives, up to rounding. Batch size, number of steps and schedule are as designed.
   No step ran out of memory during training.
2. **Another pod.** The stopped pod `o9m5gie80kmn40` (EU-SE-1) could not be started. A new pod of the same GPU type
   (A40, CA-MTL-1) was built with the same image and package versions. On it the base model gives the same 300
   responses as in the registered evaluation (same file checksum). The old pod was deleted.
3. **A look at C3 before the other arms were trained.** To test the file layout, `gpu_eval.py` loaded the first
   adapter on 16 test questions (256 of 256 tensors placed, 2 abstentions among the 16 responses). Arms J, K and R
   were then trained by the same command with no setting changed.

Training loss, mean per completion token. First step, means of epochs 1, 2 and 3, last step. C: 1.56, 0.41, 0.11,
0.05, 0.04. J: 1.57, 0.46, 0.14, 0.07, 0.06. K: 2.14, 0.55, 0.16, 0.08, 0.07. R: 2.19, 0.57, 0.16, 0.08, 0.08. No
loss was NaN. The loss of the third epoch is close to zero, so each adapter has largely memorised its 1,500
completions.

Result on the 300 test questions. Rates are shares of all questions, 95% paired bootstrap intervals in brackets.

| model | abstentions | correct | wrong | unparsed |
|---|---|---|---|---|
| C3, cautious style, no selection | 17.3% (13.3% to 21.7%) | 69.7% (64.3% to 75.0%) | 10.3% (7.0% to 14.0%) | 2.7% (1.0% to 4.7%) |
| J3, judge, default instruction | 0.0% (0.0% to 0.0%) | 80.3% (75.7% to 84.7%) | 17.0% (13.0% to 21.3%) | 2.7% (1.0% to 4.7%) |
| K3, by the key | 0.3% (0.0% to 1.0%) | 81.3% (76.7% to 85.7%) | 17.3% (13.0% to 21.7%) | 1.0% (0.0% to 2.3%) |
| R3, random | 2.3% (0.7% to 4.3%) | 80.7% (76.0% to 85.0%) | 16.7% (12.7% to 21.0%) | 0.3% (0.0% to 1.0%) |

The three predictions, read literally.

1. The C model abstains on at least 10% of the test questions: holds. C3 abstains on 52 of 300, 17.3%.
2. The J model abstains on at most 2%: holds. J3 abstains on none of the 300.
3. The J model has a higher wrong-answer rate than the C model: holds. J3 17.0%, C3 10.3%, difference 6.7 points
   (3.0 to 10.3). J3 is not above C3 in 0.0002 of the bootstrap resamples, below 0.05.

Abstention survives this fine-tuning when the training set keeps it (21.9% abstentions in `train_C`), and it is
absent after training on the judge's choice (0.3% abstentions in `train_J`).

What limits the result.

- **C3 gives up correct answers too.** It has 10.7 points fewer correct answers than J3 (6.3 to 15.3). Of its 52
  abstentions, 34 fall on questions J3 answers correctly, 16 on questions J3 gets wrong and 2 on questions where J3
  has no final line. The penalised score of C3 is +0.567 against +0.607 for J3, difference -0.040 (-0.113 to +0.033),
  so C3 is not better on that score.
- **The caution is aimed at harder questions, but loosely.** J3 is wrong on 30.8% of the questions where C3
  abstains and on 14.1% of the questions where C3 answers (gap 16.7 points, 3.5 to 30.4). Read the other way, C3
  abstains on 31.4% of the questions J3 gets wrong and on 14.5% of the others. With K3 or R3 in the place of J3 the
  gap is 11.6 and 12.4 points and its interval reaches zero. No sign was predicted for these gaps.
- **J against K shows no difference here either.** J3 and K3 differ by 0.3 points in abstentions and 0.3 points in
  wrong answers. K3 abstains on 1 question and R3 on 7, though their training sets hold 4.3% and 7.0% abstentions.
  The follow-up separates C from the other three arms, not the judge from the key.
- **One run per arm and one seed.** The variation between two trainings of the same set is not known.
- **The abstention is the bare one.** 49 of the 52 abstentions of C3 are exactly "I don't know." with the final
  line, as in the training set.
- **The follow-up models differ from the registered ones in several things at once**: the trainer, three epochs
  and 282 steps in place of one epoch and 22 steps, and twice the peak learning rate. The lower share of responses
  without a final line (0.3% to 2.7%, against 10% to 15%) cannot be assigned to one of them.
- The follow-up was designed after the registered evaluation was seen. It is exploratory.
