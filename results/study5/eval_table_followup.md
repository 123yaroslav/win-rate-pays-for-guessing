Follow-up evaluation by the key on 300 MedQA test questions (rows 500 to 799), exploratory. The four models were trained directly on the rented GPU with `src/gpu_train_lora.py` (three epochs, the same settings for every arm) and evaluated with `src/gpu_eval.py` as registered: one greedy response per question, no system prompt. Intervals are 95% percentile bootstraps over questions (10000 resamples, seed 20261115), paired across models. Rates are shares of all questions. Penalised score: +1 for a right answer, -1 for a wrong or unparsed one, 0 for an abstention, averaged.

| model | abstentions | correct | wrong | unparsed | penalised score |
|---|---|---|---|---|---|
| C3, cautious style, no selection | 17.3% (13.3% to 21.7%) | 69.7% (64.3% to 75.0%) | 10.3% (7.0% to 14.0%) | 2.7% (1.0% to 4.7%) | +0.567 (+0.483 to +0.647) |
| J3, judge, default instruction | 0.0% (0.0% to 0.0%) | 80.3% (75.7% to 84.7%) | 17.0% (13.0% to 21.3%) | 2.7% (1.0% to 4.7%) | +0.607 (+0.513 to +0.693) |
| K3, by the key | 0.3% (0.0% to 1.0%) | 81.3% (76.7% to 85.7%) | 17.3% (13.0% to 21.7%) | 1.0% (0.0% to 2.3%) | +0.630 (+0.540 to +0.713) |
| R3, random | 2.3% (0.7% to 4.3%) | 80.7% (76.0% to 85.0%) | 16.7% (12.7% to 21.0%) | 0.3% (0.0% to 1.0%) | +0.637 (+0.550 to +0.720) |

For reference, rows of the registered evaluation on the same questions and resamples. They come from another training (the service, one epoch) or from the base model with an instruction, and they were run on another pod of the same GPU type.

| model | abstentions | correct | wrong | unparsed | penalised score |
|---|---|---|---|---|---|
| J, registered run (service, one epoch) | 0.0% (0.0% to 0.0%) | 73.0% (68.0% to 78.0%) | 17.0% (13.0% to 21.3%) | 10.0% (6.7% to 13.7%) | +0.460 (+0.360 to +0.560) |
| K, registered run (service, one epoch) | 0.0% (0.0% to 0.0%) | 67.7% (62.3% to 73.0%) | 17.0% (12.7% to 21.3%) | 15.3% (11.3% to 19.7%) | +0.353 (+0.247 to +0.460) |
| R, registered run (service, one epoch) | 0.0% (0.0% to 0.0%) | 68.3% (63.0% to 73.3%) | 17.7% (13.7% to 22.0%) | 14.0% (10.3% to 18.0%) | +0.367 (+0.260 to +0.467) |
| base model, abstain instruction (reference) | 31.7% (26.3% to 37.0%) | 58.0% (52.3% to 63.7%) | 9.0% (6.0% to 12.3%) | 1.3% (0.3% to 2.7%) | +0.477 (+0.400 to +0.553) |

Paired differences (first minus second, same resampled questions). The share is the bootstrap share of resamples on the wrong side of zero. A star marks a cell where the follow-up design predicts a sign (C3 abstains more than J3 and gives fewer wrong answers). There the share counts resamples at zero or with the other sign. In the other cells the share is taken against the sign of the observed difference.

| difference | abstentions | wrong | correct | penalised score |
|---|---|---|---|---|
| C3-J3 | +17.3 pp (+13.3 to +21.7), share 0.0000 * | -6.7 pp (-10.3 to -3.0), share 0.0002 * | -10.7 pp (-15.3 to -6.3), share 0.0000 | -0.040 (-0.113 to +0.033), share 0.1475 |
| C3-K3 | +17.0 pp (+13.0 to +21.3), share 0.0000 | -7.0 pp (-10.7 to -3.3), share 0.0002 | -11.7 pp (-16.7 to -6.7), share 0.0000 | -0.063 (-0.143 to +0.017), share 0.0726 |
| J3-K3 | -0.3 pp (-1.0 to +0.0), share 0.3598 | -0.3 pp (-4.3 to +3.7), share 0.4608 | -1.0 pp (-5.0 to +2.7), share 0.3506 | -0.023 (-0.100 to +0.053), share 0.3087 |
| J3-R3 | -2.3 pp (-4.3 to -0.7), share 0.0009 | +0.3 pp (-3.7 to +4.3), share 0.4579 | -0.3 pp (-4.3 to +3.7), share 0.4664 | -0.030 (-0.110 to +0.050), share 0.2415 |

Predictions of the follow-up design, evaluated literally.

1. The C model abstains on at least 10% of the test questions: holds. C3 abstains on 52 of 300, 17.3% (13.3% to 21.7%).
2. The J model abstains on at most 2%: holds. J3 abstains on 0 of 300, 0.0% (0.0% to 0.0%).
3. The J model has a higher wrong-answer rate than the C model (paired bootstrap, 0.05): holds. J3 17.0%, C3 10.3%, J3 minus C3 +6.7 pp (+3.0 to +10.3), share of resamples where J3 is not above C3 0.0002.

Where the abstentions of C3 fall. Counts of the 300 questions by the outcome of C3 (rows) and of J3 (columns).

| C3 \ J3 | correct | wrong | abstain | unparsed | all |
|---|---|---|---|---|---|
| correct | 199 | 8 | 0 | 2 | 209 |
| wrong | 5 | 25 | 0 | 1 | 31 |
| abstain | 34 | 16 | 0 | 2 | 52 |
| unparsed | 3 | 2 | 0 | 3 | 8 |
| all | 241 | 51 | 0 | 8 | 300 |

C3 abstains on 52 questions. The table asks whether these are the questions another model gets wrong. First pair of columns: the share of questions the other model gets wrong, among the questions where C3 abstains and among the rest. Second pair: the share of questions where C3 abstains, among the questions the other model gets wrong and among the rest. Caution is aimed at the right questions if the first number of each pair is the larger one. Intervals are bootstraps over questions. No sign was predicted for these gaps, the share is a description.

| other model, its error | wrong where C3 abstains | wrong where C3 answers | gap | C3 abstains where the other is wrong | C3 abstains where it is not | gap |
|---|---|---|---|---|---|---|
| J3, wrong (51 questions, 16 of them among the abstentions) | 30.8% (18.4% to 43.9%) | 14.1% (9.9% to 18.6%) | +16.7 pp (+3.5 to +30.4), share at or below zero 0.0066 | 31.4% (18.8% to 44.4%) | 14.5% (10.2% to 18.9%) | +16.9 pp (+3.6 to +30.6), share at or below zero 0.0066 |
| K3, wrong (52 questions, 14 of them among the abstentions) | 26.9% (15.2% to 39.6%) | 15.3% (11.0% to 20.0%) | +11.6 pp (-1.2 to +25.1), share at or below zero 0.0371 | 26.9% (15.1% to 39.5%) | 15.3% (11.0% to 19.9%) | +11.6 pp (-1.1 to +25.0), share at or below zero 0.0371 |
| R3, wrong (50 questions, 14 of them among the abstentions) | 26.9% (15.5% to 39.6%) | 14.5% (10.3% to 19.0%) | +12.4 pp (-0.3 to +25.7), share at or below zero 0.0281 | 28.0% (15.8% to 40.9%) | 15.2% (10.9% to 19.8%) | +12.8 pp (-0.2 to +26.6), share at or below zero 0.0281 |
| J3, wrong or unparsed (59 questions, 18 of them among the abstentions) | 34.6% (21.7% to 48.0%) | 16.5% (12.0% to 21.3%) | +18.1 pp (+4.3 to +32.3), share at or below zero 0.0037 | 30.5% (18.9% to 42.6%) | 14.1% (9.9% to 18.6%) | +16.4 pp (+3.8 to +29.1), share at or below zero 0.0037 |
| K3, wrong or unparsed (55 questions, 15 of them among the abstentions) | 28.8% (17.0% to 41.7%) | 16.1% (11.7% to 20.9%) | +12.7 pp (-0.4 to +26.3), share at or below zero 0.0288 | 27.3% (15.7% to 39.6%) | 15.1% (10.8% to 19.7%) | +12.2 pp (-0.4 to +25.5), share at or below zero 0.0288 |
| R3, wrong or unparsed (51 questions, 14 of them among the abstentions) | 26.9% (15.5% to 39.6%) | 14.9% (10.6% to 19.5%) | +12.0 pp (-0.6 to +25.3), share at or below zero 0.0321 | 27.5% (15.6% to 40.0%) | 15.3% (11.0% to 19.9%) | +12.2 pp (-0.6 to +25.6), share at or below zero 0.0321 |

Training (from `followup_train_log_<arm>.json`). Loss is the mean negative log-likelihood per completion token of a step.

| model | steps | first step | mean of epoch 1 | epoch 2 | epoch 3 | mean of the last 10 steps | final step | longest example, tokens | seconds |
|---|---|---|---|---|---|---|---|---|---|
| C3 | 282 | 1.564 | 0.408 | 0.105 | 0.046 | 0.045 | 0.041 | 846 | 1428 |
| J3 | 282 | 1.569 | 0.458 | 0.140 | 0.069 | 0.065 | 0.063 | 764 | 1423 |
| K3 | 282 | 2.140 | 0.551 | 0.159 | 0.082 | 0.081 | 0.074 | 755 | 1359 |
| R3 | 282 | 2.194 | 0.568 | 0.161 | 0.084 | 0.086 | 0.081 | 755 | 1365 |

No follow-up model has more than 5% unparsed responses.
