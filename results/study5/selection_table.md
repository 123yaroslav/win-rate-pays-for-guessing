Composition of the selected training sets, 1500 questions each. Intervals are 95% percentile bootstraps over questions (10000 resamples).

| rule | abstentions | correct | wrong | unparsed | assert style | hedge style | abstain style |
|---|---|---|---|---|---|---|---|
| J, judge, default instruction | 0.3% (0.1% to 0.7%) | 81.7% (79.7% to 83.7%) | 15.6% (13.7% to 17.5%) | 2.3% (1.6% to 3.1%) | 26.5% (24.4% to 28.7%) | 18.0% (16.1% to 19.9%) | 55.5% (52.9% to 57.9%) |
| F, judge, accuracy instruction | 1.7% (1.1% to 2.3%) | 82.1% (80.1% to 84.1%) | 14.3% (12.6% to 16.1%) | 1.9% (1.3% to 2.7%) | 25.5% (23.4% to 27.7%) | 24.9% (22.8% to 27.1%) | 49.5% (47.0% to 52.1%) |
| K, by the key | 4.3% (3.3% to 5.3%) | 87.5% (85.9% to 89.2%) | 7.7% (6.4% to 9.1%) | 0.5% (0.1% to 0.9%) | 36.4% (34.0% to 38.8%) | 33.1% (30.8% to 35.5%) | 30.5% (28.2% to 32.8%) |
| R, random | 7.0% (5.7% to 8.3%) | 74.7% (72.5% to 76.9%) | 16.9% (15.0% to 18.8%) | 1.4% (0.9% to 2.0%) | 34.3% (31.9% to 36.7%) | 32.3% (29.9% to 34.6%) | 33.4% (31.1% to 35.7%) |

Paired differences between rules (same resampled questions).

| difference | abstentions | correct | wrong |
|---|---|---|---|
| J-K | -3.9 pp (-5.0 to -2.9) | -5.8 pp (-7.0 to -4.7) | +7.9 pp (+6.4 to +9.4) |
| F-K | -2.6 pp (-3.7 to -1.5) | -5.5 pp (-6.7 to -4.3) | +6.6 pp (+5.3 to +8.0) |
| J-F | -1.3 pp (-2.0 to -0.7) | -0.3 pp (-1.4 to +0.7) | +1.3 pp (+0.3 to +2.3) |
| J-R | -6.7 pp (-8.0 to -5.4) | +7.0 pp (+5.3 to +8.7) | -1.3 pp (-2.7 to +0.2) |
| K-R | -2.7 pp (-4.3 to -1.2) | +12.8 pp (+11.1 to +14.5) | -9.1 pp (-10.7 to -7.7) |

P5b (J has a lower share of abstentions and a higher share of wrong answers than K): holds. Abstentions -3.9 pp (-5.0 to -2.9), bootstrap share of resamples with a difference at or above zero 0.0000. Wrong answers +7.9 pp (+6.4 to +9.4), bootstrap share at or below zero 0.0000.

Judge duels behind J and F (Claude Haiku 5.5, three per question).

| rule | duels | unparsed verdicts | picks the first position | questions with a tie for most wins | assert beats abstain style | hedge beats abstain style | assert beats hedge |
|---|---|---|---|---|---|---|---|
| J | 4500 | 126 | 59.0% | 164 | 38.9% | 33.1% | 58.4% |
| F | 4500 | 622 | 63.0% | 361 | 40.2% | 37.4% | 54.4% |

Pair rates are over all pool questions, whatever the abstain-style response says (it abstains on a minority of them). The rates on abstentions only are in natural_duels.md.
