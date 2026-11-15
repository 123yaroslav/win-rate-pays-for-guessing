items 102 (geo, law, medqa), bootstrap draws 10000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 92.5% | 88.5% to 96.0% | 87 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 63.6% | 54.5% to 72.7% | 77 | 0.0021 | yes |
| adaption/qwen3.8-27b | 65.3% | 59.7% to 70.8% | 72 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 82.2% | 75.7% to 88.2% | 76 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 93.3% | 89.0% to 97.0% | 82 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.5% | 76.5% to 88.6% | 83 | 0.0000 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 93.6% | 90.2% to 96.6% | 102 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 69.7% | 61.6% to 77.3% | 99 | 0.0000 | yes |
| adaption/qwen3.8-27b | 69.6% | 64.7% to 74.5% | 102 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 83.8% | 78.4% to 89.2% | 102 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 94.1% | 90.6% to 97.0% | 101 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.8% | 80.4% to 90.7% | 102 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 90.8% | 85.4% to 95.4% | 65 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 69.4% | 61.2% to 77.6% | 85 | 0.0000 | yes |
| adaption/qwen3.8-27b | 69.6% | 64.7% to 74.5% | 102 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 83.2% | 77.6% to 88.3% | 98 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.0% | 87.3% to 96.0% | 75 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.7% | 78.1% to 89.3% | 89 | 0.0000 | yes |

S1g2: b above 0.5 on group 'judge tells the two answers apart', Holm at 0.05. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 89.7% | 84.5% to 94.8% | 58 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 65.2% | 55.3% to 74.2% | 66 | 0.0016 | yes |
| adaption/qwen3.8-27b | 66.7% | 59.4% to 74.0% | 48 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 82.1% | 72.6% to 90.5% | 42 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 90.9% | 85.6% to 95.5% | 66 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.3% | 76.2% to 88.4% | 82 | 0.0000 | yes |

## Detection (S1g)

| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |
|---|---|---|---|
| adaption/deepseek-v4-flash | 63.7% | 90.2% | 0 |
| adaption/gemma-4-31b-it | 86.3% | 73.5% | 10 |
| adaption/qwen3.8-27b | 100.0% | 47.1% | 0 |
| openrouter/anthropic/claude-haiku-5.5 | 96.1% | 43.1% | 1 |
| openrouter/mistralai/mistral-small-2603 | 74.5% | 86.3% | 0 |
| openrouter/openai/gpt-5.6-luna | 87.3% | 87.3% | 0 |

## Verify-then-compare, composed from logged verdicts (exploratory)

| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |
|---|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 99.5% | 93.6% | 89.7% | 35.8% | 0.26 | 0.11 to 0.38 |
| adaption/gemma-4-31b-it | 98.4% | 72.0% | 76.3% | 8.6% | 0.61 | 0.54 to 0.71 |
| adaption/qwen3.8-27b | 87.3% | 69.6% | 44.1% | 0.0% | 1.13 | 0.94 to 1.44 |
| openrouter/anthropic/claude-haiku-5.5 | 99.0% | 83.7% | 42.6% | 3.0% | 1.19 | 0.95 to 1.58 |
| openrouter/mistralai/mistral-small-2603 | 100.0% | 94.1% | 86.1% | 25.7% | 0.40 | 0.30 to 0.49 |
| openrouter/openai/gpt-5.6-luna | 100.0% | 85.8% | 87.3% | 12.7% | 0.50 | 0.45 to 0.55 |

## Instruction variants (Study 4 criterion)

| judge | variant | a, knows | b, knows | share of resamples with b at or above 0.5 | repaired | a, does not know | b, does not know |
|---|---|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | default | 99% | 93% | 1.000 | no | 100% | 100% |
| adaption/deepseek-v4-flash | mtbench | 99% | 79% | 1.000 | no | 100% | 93% |
| adaption/gemma-4-31b-it | default | 100% | 64% | 0.999 | no | 93% | 91% |
| adaption/gemma-4-31b-it | mtbench | 100% | 14% | 0.000 | yes | 82% | 52% |
| adaption/qwen3.8-27b | default | 91% | 65% | 1.000 | no | 78% | 80% |
| adaption/qwen3.8-27b | mtbench | 100% | 15% | 0.000 | yes | 100% | 100% |
| openrouter/anthropic/claude-haiku-5.5 | default | 99% | 82% | 1.000 | no | 98% | 88% |
| openrouter/anthropic/claude-haiku-5.5 | mtbench | 100% | 27% | 0.000 | yes | 88% | 69% |
| openrouter/mistralai/mistral-small-2603 | default | 100% | 93% | 1.000 | no | 100% | 97% |
| openrouter/mistralai/mistral-small-2603 | mtbench | 99% | 82% | 1.000 | no | 97% | 96% |
| openrouter/openai/gpt-5.6-luna | default | 100% | 83% | 1.000 | no | 100% | 100% |
| openrouter/openai/gpt-5.6-luna | mtbench | 100% | 73% | 1.000 | no | 99% | 96% |

## Two-step account (S1d)

Cells 18, mean absolute error 0.239, Spearman 0.68. Mean predicted 70.5%, mean observed 46.8%.

## adaption/deepseek-v4-flash: own closed-book accuracy 85% on 102 items

### prompt variant default (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 97% | 94% to 99% | 102 | 0 |
| CC-IDK | all | 100% | 99% to 100% | 102 | 0 |
| CW-CC | all | 21% | 15% to 27% | 102 | 0 |
| CW-HC | all | 74% | 67% to 80% | 102 | 0 |
| CW-HW | all | 96% | 93% to 99% | 102 | 0 |
| CW-IDK | all | 94% | 90% to 97% | 102 | 0 |
| HC-IDK | all | 97% | 94% to 99% | 102 | 1 |
| HW-IDK | all | 97% | 94% to 99% | 102 | 0 |
| CC-HC | judge knows | 97% | 94% to 99% | 87 | 0 |
| CC-IDK | judge knows | 99% | 98% to 100% | 87 | 0 |
| CW-CC | judge knows | 15% | 10% to 21% | 87 | 0 |
| CW-HC | judge knows | 70% | 63% to 78% | 87 | 0 |
| CW-HW | judge knows | 96% | 93% to 99% | 87 | 0 |
| CW-IDK | judge knows | 93% | 89% to 96% | 87 | 0 |
| HC-IDK | judge knows | 97% | 94% to 99% | 87 | 1 |
| HW-IDK | judge knows | 96% | 93% to 98% | 87 | 0 |
| CC-HC | judge does not know | 97% | 90% to 100% | 15 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 15 | 0 |
| CW-CC | judge does not know | 57% | 40% to 73% | 15 | 0 |
| CW-HC | judge does not know | 93% | 83% to 100% | 15 | 0 |
| CW-HW | judge does not know | 97% | 90% to 100% | 15 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 15 | 0 |
| HC-IDK | judge does not know | 93% | 83% to 100% | 15 | 1 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 15 | 0 |
| CC-HC | judge tells the two answers apart | 97% | 94% to 100% | 58 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 97% to 100% | 58 | 0 |
| CW-CC | judge tells the two answers apart | 9% | 3% to 15% | 58 | 0 |
| CW-HC | judge tells the two answers apart | 62% | 53% to 72% | 58 | 0 |
| CW-HW | judge tells the two answers apart | 95% | 91% to 98% | 58 | 0 |
| CW-IDK | judge tells the two answers apart | 90% | 84% to 95% | 58 | 0 |
| HC-IDK | judge tells the two answers apart | 97% | 94% to 100% | 58 | 1 |
| HW-IDK | judge tells the two answers apart | 95% | 91% to 98% | 58 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 65 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 65 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 12% | 7% to 18% | 65 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 65% | 57% to 74% | 65 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 95% | 92% to 98% | 65 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 91% | 85% to 95% | 65 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 65 | 1 |
| HW-IDK | judge flags the wrong answer as incorrect | 95% | 92% to 98% | 65 | 0 |
| CC-HC | judge knows and flags the wrong answer | 97% | 93% to 99% | 58 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 97% to 100% | 58 | 0 |
| CW-CC | judge knows and flags the wrong answer | 8% | 3% to 13% | 58 | 0 |
| CW-HC | judge knows and flags the wrong answer | 61% | 52% to 71% | 58 | 0 |
| CW-HW | judge knows and flags the wrong answer | 95% | 91% to 98% | 58 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 90% | 84% to 95% | 58 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 97% | 94% to 100% | 58 | 1 |
| HW-IDK | judge knows and flags the wrong answer | 95% | 91% to 98% | 58 | 0 |
| CC-IDK | domain geo | 99% | 96% to 100% | 34 | 0 |
| CW-HC | domain geo | 65% | 51% to 76% | 34 | 0 |
| CW-IDK | domain geo | 88% | 81% to 96% | 34 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain law | 76% | 65% to 87% | 34 | 0 |
| CW-IDK | domain law | 97% | 93% to 100% | 34 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain medqa | 79% | 69% to 88% | 34 | 0 |
| CW-IDK | domain medqa | 96% | 90% to 100% | 34 | 0 |
| CC-IDK | domain geo, judge knows | 98% | 95% to 100% | 31 | 0 |
| CW-HC | domain geo, judge knows | 61% | 48% to 74% | 31 | 0 |
| CW-IDK | domain geo, judge knows | 87% | 79% to 94% | 31 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-HC | domain law, judge knows | 74% | 59% to 87% | 27 | 0 |
| CW-IDK | domain law, judge knows | 96% | 91% to 100% | 27 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 29 | 0 |
| CW-HC | domain medqa, judge knows | 76% | 64% to 86% | 29 | 0 |
| CW-IDK | domain medqa, judge knows | 95% | 90% to 100% | 29 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 94% | +0.06 | -7.42 | -15.83 to -4.26 | 96% | 90% | 74% |
| judge knows | 99% | 93% | +0.07 | -6.17 | -13.50 to -3.53 | 96% | 89% | 70% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 97% | 97% | 93% |
| judge tells the two answers apart | 99% | 90% | +0.09 | -4.18 | -10.40 to -2.22 | 95% | 86% | 62% |
| judge flags the wrong answer as incorrect | 99% | 91% | +0.08 | -4.82 | -11.80 to -2.61 | 95% | 87% | 65% |
| judge knows and flags the wrong answer | 99% | 90% | +0.09 | -4.18 | -10.40 to -2.22 | 95% | 86% | 61% |
| domain geo | 99% | 88% | +0.10 | -3.71 | -14.00 to -1.62 | 93% | 83% | 65% |
| domain law | 100% | 97% | +0.03 | -16.00 | -16.00 to -5.80 | 97% | 94% | 76% |
| domain medqa | 100% | 96% | +0.04 | -10.33 | -16.00 to -3.86 | 99% | 94% | 79% |
| domain geo, judge knows | 98% | 87% | +0.11 | -3.29 | -13.00 to -1.42 | 92% | 82% | 61% |
| domain law, judge knows | 100% | 96% | +0.04 | -12.50 | -12.50 to -4.40 | 98% | 95% | 74% |
| domain medqa, judge knows | 100% | 95% | +0.05 | -8.67 | -13.50 to -3.14 | 98% | 93% | 76% |

### prompt variant mtbench (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 99% to 100% | 102 | 3 |
| CW-IDK | all | 81% | 75% to 86% | 102 | 4 |
| CC-IDK | judge knows | 99% | 98% to 100% | 87 | 3 |
| CW-IDK | judge knows | 79% | 73% to 84% | 87 | 4 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 15 | 3 |
| CW-IDK | judge does not know | 93% | 83% to 100% | 15 | 4 |
| CC-IDK | judge tells the two answers apart | 99% | 97% to 100% | 58 | 3 |
| CW-IDK | judge tells the two answers apart | 72% | 64% to 80% | 58 | 4 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 65 | 3 |
| CW-IDK | judge flags the wrong answer as incorrect | 74% | 67% to 82% | 65 | 4 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 97% to 100% | 58 | 3 |
| CW-IDK | judge knows and flags the wrong answer | 72% | 64% to 80% | 58 | 4 |
| CC-IDK | domain geo | 99% | 96% to 100% | 34 | 3 |
| CW-IDK | domain geo | 66% | 55% to 76% | 34 | 4 |
| CC-IDK | domain law | 100% | 100% to 100% | 34 | 3 |
| CW-IDK | domain law | 90% | 84% to 96% | 34 | 4 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 3 |
| CW-IDK | domain medqa | 86% | 77% to 94% | 34 | 4 |
| CC-IDK | domain geo, judge knows | 98% | 95% to 100% | 31 | 3 |
| CW-IDK | domain geo, judge knows | 63% | 52% to 74% | 31 | 4 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 27 | 3 |
| CW-IDK | domain law, judge knows | 92% | 84% to 98% | 27 | 4 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 29 | 3 |
| CW-IDK | domain medqa, judge knows | 84% | 73% to 93% | 29 | 4 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 81% | +0.19 | -1.66 | -2.67 to -1.04 | - | - | - |
| judge knows | 99% | 79% | +0.21 | -1.39 | -2.37 to -0.85 | - | - | - |
| judge does not know | 100% | 93% | +0.07 | -6.50 | -14.00 to -2.00 | - | - | - |
| judge tells the two answers apart | 99% | 72% | +0.27 | -0.81 | -1.52 to -0.39 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 74% | +0.25 | -0.97 | -1.77 to -0.51 | - | - | - |
| judge knows and flags the wrong answer | 99% | 72% | +0.27 | -0.81 | -1.52 to -0.40 | - | - | - |
| domain geo | 99% | 66% | +0.32 | -0.50 | -1.20 to -0.13 | - | - | - |
| domain law | 100% | 90% | +0.10 | -4.23 | -12.60 to -2.09 | - | - | - |
| domain medqa | 100% | 86% | +0.14 | -2.58 | -6.56 to -1.19 | - | - | - |
| domain geo, judge knows | 98% | 63% | +0.35 | -0.36 | -0.94 to -0.03 | - | - | - |
| domain law, judge knows | 100% | 92% | +0.08 | -5.00 | -17.00 to -2.18 | - | - | - |
| domain medqa, judge knows | 100% | 84% | +0.16 | -2.05 | -5.44 to -0.87 | - | - | - |

## adaption/gemma-4-31b-it: own closed-book accuracy 78% on 102 items

### prompt variant default (picks the first position in 58% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 100% to 100% | 101 | 6 |
| CC-IDK | all | 99% | 97% to 100% | 102 | 2 |
| CW-CC | all | 12% | 7% to 18% | 99 | 11 |
| CW-HC | all | 30% | 22% to 39% | 100 | 11 |
| CW-HW | all | 90% | 84% to 95% | 65 | 87 |
| CW-IDK | all | 70% | 62% to 77% | 99 | 19 |
| HC-IDK | all | 91% | 86% to 94% | 100 | 8 |
| HW-IDK | all | 42% | 35% to 49% | 101 | 7 |
| CC-HC | judge knows | 100% | 100% to 100% | 79 | 6 |
| CC-IDK | judge knows | 100% | 100% to 100% | 80 | 2 |
| CW-CC | judge knows | 4% | 1% to 8% | 79 | 11 |
| CW-HC | judge knows | 19% | 12% to 26% | 78 | 11 |
| CW-HW | judge knows | 88% | 80% to 94% | 45 | 87 |
| CW-IDK | judge knows | 64% | 55% to 73% | 77 | 19 |
| HC-IDK | judge knows | 99% | 97% to 100% | 78 | 8 |
| HW-IDK | judge knows | 37% | 30% to 45% | 79 | 7 |
| CC-HC | judge does not know | 100% | 100% to 100% | 22 | 6 |
| CC-IDK | judge does not know | 93% | 86% to 100% | 22 | 2 |
| CW-CC | judge does not know | 45% | 25% to 65% | 20 | 11 |
| CW-HC | judge does not know | 73% | 57% to 86% | 22 | 11 |
| CW-HW | judge does not know | 95% | 88% to 100% | 20 | 87 |
| CW-IDK | judge does not know | 91% | 80% to 100% | 22 | 19 |
| HC-IDK | judge does not know | 64% | 52% to 75% | 22 | 8 |
| HW-IDK | judge does not know | 59% | 43% to 73% | 22 | 7 |
| CC-HC | judge tells the two answers apart | 100% | 100% to 100% | 68 | 6 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 69 | 2 |
| CW-CC | judge tells the two answers apart | 5% | 1% to 10% | 66 | 11 |
| CW-HC | judge tells the two answers apart | 19% | 11% to 28% | 67 | 11 |
| CW-HW | judge tells the two answers apart | 89% | 80% to 97% | 38 | 87 |
| CW-IDK | judge tells the two answers apart | 65% | 55% to 74% | 66 | 19 |
| HC-IDK | judge tells the two answers apart | 97% | 94% to 99% | 67 | 8 |
| HW-IDK | judge tells the two answers apart | 35% | 28% to 43% | 68 | 7 |
| CC-HC | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 87 | 6 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 88 | 2 |
| CW-CC | judge flags the wrong answer as incorrect | 9% | 4% to 14% | 85 | 11 |
| CW-HC | judge flags the wrong answer as incorrect | 28% | 20% to 37% | 86 | 11 |
| CW-HW | judge flags the wrong answer as incorrect | 90% | 84% to 95% | 55 | 87 |
| CW-IDK | judge flags the wrong answer as incorrect | 69% | 61% to 78% | 85 | 19 |
| HC-IDK | judge flags the wrong answer as incorrect | 91% | 87% to 95% | 86 | 8 |
| HW-IDK | judge flags the wrong answer as incorrect | 38% | 31% to 45% | 87 | 7 |
| CC-HC | judge knows and flags the wrong answer | 100% | 100% to 100% | 68 | 6 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 69 | 2 |
| CW-CC | judge knows and flags the wrong answer | 2% | 0% to 5% | 68 | 11 |
| CW-HC | judge knows and flags the wrong answer | 16% | 9% to 25% | 67 | 11 |
| CW-HW | judge knows and flags the wrong answer | 88% | 79% to 96% | 38 | 87 |
| CW-IDK | judge knows and flags the wrong answer | 64% | 54% to 73% | 66 | 19 |
| HC-IDK | judge knows and flags the wrong answer | 99% | 96% to 100% | 67 | 8 |
| HW-IDK | judge knows and flags the wrong answer | 34% | 26% to 41% | 68 | 7 |
| CC-IDK | domain geo | 97% | 93% to 100% | 34 | 2 |
| CW-HC | domain geo | 15% | 6% to 25% | 34 | 11 |
| CW-IDK | domain geo | 39% | 27% to 53% | 33 | 19 |
| CC-IDK | domain law | 99% | 96% to 100% | 34 | 2 |
| CW-HC | domain law | 36% | 21% to 52% | 33 | 11 |
| CW-IDK | domain law | 91% | 81% to 99% | 34 | 19 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 2 |
| CW-HC | domain medqa | 41% | 26% to 56% | 33 | 11 |
| CW-IDK | domain medqa | 78% | 66% to 89% | 32 | 19 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 30 | 2 |
| CW-HC | domain geo, judge knows | 8% | 2% to 15% | 30 | 11 |
| CW-IDK | domain geo, judge knows | 36% | 24% to 50% | 29 | 19 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 23 | 2 |
| CW-HC | domain law, judge knows | 16% | 2% to 32% | 22 | 11 |
| CW-IDK | domain law, judge knows | 87% | 74% to 98% | 23 | 19 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 27 | 2 |
| CW-HC | domain medqa, judge knows | 33% | 17% to 50% | 26 | 11 |
| CW-IDK | domain medqa, judge knows | 74% | 60% to 86% | 25 | 19 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 70% | +0.29 | -0.68 | -1.29 to -0.32 | 90% | 75% | 44% |
| judge knows | 100% | 64% | +0.36 | -0.37 | -0.83 to -0.10 | 88% | 67% | 30% |
| judge does not know | 93% | 91% | +0.02 | -18.00 | -20.00 to -2.14 | 95% | 95% | 75% |
| judge tells the two answers apart | 100% | 65% | +0.35 | -0.43 | -0.94 to -0.12 | 89% | 73% | 32% |
| judge flags the wrong answer as incorrect | 99% | 69% | +0.29 | -0.66 | -1.28 to -0.29 | 90% | 75% | 40% |
| judge knows and flags the wrong answer | 100% | 64% | +0.36 | -0.37 | -0.89 to -0.08 | 88% | 68% | 26% |
| domain geo | 97% | 39% | +0.58 | +0.18 | -0.07 to +0.33 | 87% | 48% | 26% |
| domain law | 99% | 91% | +0.07 | -5.60 | -15.50 to -1.75 | 91% | 87% | 41% |
| domain medqa | 100% | 78% | +0.22 | -1.29 | -3.57 to -0.45 | 92% | 87% | 66% |
| domain geo, judge knows | 100% | 36% | +0.64 | +0.22 | +0.00 to +0.36 | 87% | 40% | 17% |
| domain law, judge knows | 100% | 87% | +0.13 | -2.83 | -22.00 to -0.92 | 88% | 80% | 21% |
| domain medqa, judge knows | 100% | 74% | +0.26 | -0.92 | -3.17 to -0.25 | 88% | 82% | 58% |

### prompt variant mtbench (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 92% to 99% | 102 | 0 |
| CW-IDK | all | 23% | 15% to 30% | 102 | 2 |
| CC-IDK | judge knows | 100% | 100% to 100% | 80 | 0 |
| CW-IDK | judge knows | 14% | 8% to 22% | 80 | 2 |
| CC-IDK | judge does not know | 82% | 64% to 95% | 22 | 0 |
| CW-IDK | judge does not know | 52% | 32% to 73% | 22 | 2 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 69 | 0 |
| CW-IDK | judge tells the two answers apart | 17% | 9% to 25% | 69 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 88 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 20% | 12% to 28% | 88 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 69 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 13% | 7% to 21% | 69 | 2 |
| CC-IDK | domain geo | 91% | 79% to 100% | 34 | 0 |
| CW-IDK | domain geo | 12% | 3% to 22% | 34 | 2 |
| CC-IDK | domain law | 97% | 91% to 100% | 34 | 0 |
| CW-IDK | domain law | 37% | 22% to 53% | 34 | 2 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 0 |
| CW-IDK | domain medqa | 19% | 7% to 32% | 34 | 2 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain geo, judge knows | 7% | 2% to 13% | 30 | 2 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 23 | 0 |
| CW-IDK | domain law, judge knows | 24% | 9% to 41% | 23 | 2 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-IDK | domain medqa, judge knows | 15% | 4% to 30% | 27 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 23% | +0.74 | +0.37 | +0.30 to +0.43 | - | - | - |
| judge knows | 100% | 14% | +0.86 | +0.42 | +0.36 to +0.46 | - | - | - |
| judge does not know | 82% | 52% | +0.30 | -0.08 | -3.00 to +0.36 | - | - | - |
| judge tells the two answers apart | 100% | 17% | +0.83 | +0.40 | +0.33 to +0.45 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 20% | +0.79 | +0.38 | +0.31 to +0.44 | - | - | - |
| judge knows and flags the wrong answer | 100% | 13% | +0.87 | +0.42 | +0.37 to +0.47 | - | - | - |
| domain geo | 91% | 12% | +0.79 | +0.48 | +0.43 to +0.54 | - | - | - |
| domain law | 97% | 37% | +0.60 | +0.22 | -0.04 to +0.37 | - | - | - |
| domain medqa | 100% | 19% | +0.81 | +0.38 | +0.26 to +0.46 | - | - | - |
| domain geo, judge knows | 100% | 7% | +0.93 | +0.46 | +0.42 to +0.49 | - | - | - |
| domain law, judge knows | 100% | 24% | +0.76 | +0.34 | +0.15 to +0.45 | - | - | - |
| domain medqa, judge knows | 100% | 15% | +0.85 | +0.41 | +0.29 to +0.48 | - | - | - |

## adaption/qwen3.8-27b: own closed-book accuracy 71% on 102 items

### prompt variant default (picks the first position in 29% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 89% | 84% to 93% | 102 | 0 |
| CC-IDK | all | 87% | 83% to 91% | 102 | 0 |
| CW-CC | all | 22% | 16% to 27% | 102 | 3 |
| CW-HC | all | 46% | 40% to 51% | 102 | 3 |
| CW-HW | all | 71% | 66% to 75% | 102 | 3 |
| CW-IDK | all | 70% | 65% to 75% | 102 | 2 |
| HC-IDK | all | 85% | 81% to 90% | 102 | 0 |
| HW-IDK | all | 65% | 59% to 70% | 102 | 0 |
| CC-HC | judge knows | 92% | 88% to 97% | 72 | 0 |
| CC-IDK | judge knows | 91% | 86% to 95% | 72 | 0 |
| CW-CC | judge knows | 14% | 9% to 19% | 72 | 3 |
| CW-HC | judge knows | 39% | 33% to 45% | 72 | 3 |
| CW-HW | judge knows | 70% | 64% to 76% | 72 | 3 |
| CW-IDK | judge knows | 65% | 60% to 71% | 72 | 2 |
| HC-IDK | judge knows | 90% | 85% to 94% | 72 | 0 |
| HW-IDK | judge knows | 64% | 58% to 70% | 72 | 0 |
| CC-HC | judge does not know | 80% | 72% to 88% | 30 | 0 |
| CC-IDK | judge does not know | 78% | 70% to 87% | 30 | 0 |
| CW-CC | judge does not know | 40% | 28% to 52% | 30 | 3 |
| CW-HC | judge does not know | 62% | 52% to 73% | 30 | 3 |
| CW-HW | judge does not know | 72% | 63% to 80% | 30 | 3 |
| CW-IDK | judge does not know | 80% | 72% to 88% | 30 | 2 |
| HC-IDK | judge does not know | 73% | 65% to 82% | 30 | 0 |
| HW-IDK | judge does not know | 67% | 57% to 77% | 30 | 0 |
| CC-HC | judge tells the two answers apart | 95% | 91% to 99% | 48 | 0 |
| CC-IDK | judge tells the two answers apart | 94% | 89% to 98% | 48 | 0 |
| CW-CC | judge tells the two answers apart | 10% | 5% to 17% | 48 | 3 |
| CW-HC | judge tells the two answers apart | 33% | 27% to 40% | 48 | 3 |
| CW-HW | judge tells the two answers apart | 66% | 59% to 72% | 48 | 3 |
| CW-IDK | judge tells the two answers apart | 67% | 59% to 74% | 48 | 2 |
| HC-IDK | judge tells the two answers apart | 93% | 88% to 97% | 48 | 0 |
| HW-IDK | judge tells the two answers apart | 60% | 53% to 68% | 48 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 89% | 84% to 93% | 102 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 87% | 83% to 91% | 102 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 22% | 16% to 27% | 102 | 3 |
| CW-HC | judge flags the wrong answer as incorrect | 46% | 40% to 51% | 102 | 3 |
| CW-HW | judge flags the wrong answer as incorrect | 71% | 66% to 75% | 102 | 3 |
| CW-IDK | judge flags the wrong answer as incorrect | 70% | 65% to 75% | 102 | 2 |
| HC-IDK | judge flags the wrong answer as incorrect | 85% | 81% to 90% | 102 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 65% | 60% to 70% | 102 | 0 |
| CC-HC | judge knows and flags the wrong answer | 92% | 88% to 97% | 72 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 91% | 86% to 95% | 72 | 0 |
| CW-CC | judge knows and flags the wrong answer | 14% | 9% to 19% | 72 | 3 |
| CW-HC | judge knows and flags the wrong answer | 39% | 33% to 45% | 72 | 3 |
| CW-HW | judge knows and flags the wrong answer | 70% | 64% to 76% | 72 | 3 |
| CW-IDK | judge knows and flags the wrong answer | 65% | 60% to 71% | 72 | 2 |
| HC-IDK | judge knows and flags the wrong answer | 90% | 85% to 94% | 72 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 64% | 58% to 70% | 72 | 0 |
| CC-IDK | domain geo | 96% | 91% to 100% | 34 | 0 |
| CW-HC | domain geo | 40% | 29% to 50% | 34 | 3 |
| CW-IDK | domain geo | 66% | 57% to 75% | 34 | 2 |
| CC-IDK | domain law | 79% | 71% to 87% | 34 | 0 |
| CW-HC | domain law | 50% | 40% to 60% | 34 | 3 |
| CW-IDK | domain law | 74% | 65% to 82% | 34 | 2 |
| CC-IDK | domain medqa | 87% | 79% to 94% | 34 | 0 |
| CW-HC | domain medqa | 47% | 40% to 54% | 34 | 3 |
| CW-IDK | domain medqa | 69% | 60% to 78% | 34 | 2 |
| CC-IDK | domain geo, judge knows | 97% | 92% to 100% | 30 | 0 |
| CW-HC | domain geo, judge knows | 32% | 23% to 40% | 30 | 3 |
| CW-IDK | domain geo, judge knows | 62% | 53% to 70% | 30 | 2 |
| CC-IDK | domain law, judge knows | 83% | 74% to 93% | 21 | 0 |
| CW-HC | domain law, judge knows | 43% | 31% to 55% | 21 | 3 |
| CW-IDK | domain law, judge knows | 71% | 62% to 81% | 21 | 2 |
| CC-IDK | domain medqa, judge knows | 90% | 81% to 98% | 21 | 0 |
| CW-HC | domain medqa, judge knows | 45% | 33% to 57% | 21 | 3 |
| CW-IDK | domain medqa, judge knows | 64% | 55% to 74% | 21 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 87% | 70% | +0.18 | -1.11 | -2.09 to -0.65 | 71% | 58% | 46% |
| judge knows | 91% | 65% | +0.26 | -0.59 | -1.07 to -0.31 | 70% | 52% | 39% |
| judge does not know | 78% | 80% | -0.02 | undefined | -10.00 to -1.71 | 72% | 73% | 62% |
| judge tells the two answers apart | 94% | 67% | +0.27 | -0.62 | -1.29 to -0.27 | 66% | 48% | 33% |
| judge flags the wrong answer as incorrect | 87% | 70% | +0.18 | -1.11 | -2.08 to -0.63 | 71% | 58% | 46% |
| judge knows and flags the wrong answer | 91% | 65% | +0.26 | -0.59 | -1.07 to -0.30 | 70% | 52% | 39% |
| domain geo | 96% | 66% | +0.29 | -0.55 | -1.31 to -0.19 | 68% | 48% | 40% |
| domain law | 79% | 74% | +0.06 | -4.00 | -9.50 to -1.00 | 74% | 69% | 50% |
| domain medqa | 87% | 69% | +0.18 | -1.08 | -3.60 to -0.41 | 71% | 58% | 47% |
| domain geo, judge knows | 97% | 62% | +0.35 | -0.33 | -0.79 to -0.07 | 67% | 43% | 32% |
| domain law, judge knows | 83% | 71% | +0.12 | -1.80 | -11.00 to -0.45 | 71% | 63% | 43% |
| domain medqa, judge knows | 90% | 64% | +0.26 | -0.55 | -1.43 to -0.14 | 74% | 54% | 45% |

### prompt variant mtbench (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 93 | 32 |
| CW-IDK | all | 39% | 21% to 57% | 28 | 164 |
| CC-IDK | judge knows | 100% | 100% to 100% | 69 | 32 |
| CW-IDK | judge knows | 15% | 0% to 30% | 20 | 164 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 24 | 32 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 8 | 164 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 48 | 32 |
| CW-IDK | judge tells the two answers apart | 0% | 0% to 0% | 15 | 164 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 93 | 32 |
| CW-IDK | judge flags the wrong answer as incorrect | 39% | 21% to 57% | 28 | 164 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 69 | 32 |
| CW-IDK | judge knows and flags the wrong answer | 15% | 0% to 30% | 20 | 164 |
| CC-IDK | domain geo | 100% | 100% to 100% | 33 | 32 |
| CW-IDK | domain geo | 12% | 0% to 31% | 16 | 164 |
| CC-IDK | domain law | 100% | 100% to 100% | 28 | 32 |
| CW-IDK | domain law | 75% | 38% to 100% | 8 | 164 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 32 | 32 |
| CW-IDK | domain medqa | 75% | 25% to 100% | 4 | 164 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 30 | 32 |
| CW-IDK | domain geo, judge knows | 7% | 0% to 20% | 15 | 164 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 19 | 32 |
| CW-IDK | domain law, judge knows | 33% | 0% to 100% | 3 | 164 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 20 | 32 |
| CW-IDK | domain medqa, judge knows | 50% | 0% to 100% | 2 | 164 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 35% | +0.65 | +0.24 | -0.08 to +0.41 | - | - | - |
| judge knows | 100% | 15% | +0.85 | +0.41 | +0.29 to +0.50 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge tells the two answers apart | 100% | 0% | +1.00 | +0.50 | +0.50 to +0.50 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 35% | +0.65 | +0.24 | -0.08 to +0.41 | - | - | - |
| judge knows and flags the wrong answer | 100% | 15% | +0.85 | +0.41 | +0.29 to +0.50 | - | - | - |
| domain geo | 100% | 7% | +0.93 | +0.46 | +0.37 to +0.50 | - | - | - |
| domain law | 100% | 71% | +0.29 | -0.75 | -2.50 to +0.30 | - | - | - |
| domain medqa | 100% | 75% | +0.25 | -1.00 | -1.00 to +0.33 | - | - | - |
| domain geo, judge knows | 100% | 7% | +0.93 | +0.46 | +0.37 to +0.50 | - | - | - |
| domain law, judge knows | 100% | 33% | +0.67 | +0.25 | -0.50 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 50% | +0.50 | +0.00 | +0.00 to +0.50 | - | - | - |

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 75% on 102 items

### prompt variant default (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 82% | 77% to 87% | 102 | 4 |
| CC-IDK | all | 99% | 98% to 100% | 102 | 0 |
| CW-CC | all | 20% | 14% to 26% | 102 | 5 |
| CW-HC | all | 42% | 34% to 50% | 101 | 11 |
| CW-HW | all | 57% | 50% to 64% | 99 | 24 |
| CW-IDK | all | 84% | 78% to 89% | 102 | 3 |
| HC-IDK | all | 99% | 97% to 100% | 102 | 0 |
| HW-IDK | all | 94% | 90% to 97% | 102 | 2 |
| CC-HC | judge knows | 86% | 80% to 91% | 76 | 4 |
| CC-IDK | judge knows | 99% | 98% to 100% | 76 | 0 |
| CW-CC | judge knows | 15% | 9% to 22% | 76 | 5 |
| CW-HC | judge knows | 36% | 27% to 45% | 75 | 11 |
| CW-HW | judge knows | 59% | 51% to 67% | 73 | 24 |
| CW-IDK | judge knows | 82% | 76% to 88% | 76 | 3 |
| HC-IDK | judge knows | 99% | 97% to 100% | 76 | 0 |
| HW-IDK | judge knows | 93% | 89% to 97% | 76 | 2 |
| CC-HC | judge does not know | 73% | 62% to 83% | 26 | 4 |
| CC-IDK | judge does not know | 98% | 94% to 100% | 26 | 0 |
| CW-CC | judge does not know | 33% | 19% to 48% | 26 | 5 |
| CW-HC | judge does not know | 60% | 46% to 73% | 26 | 11 |
| CW-HW | judge does not know | 52% | 40% to 63% | 26 | 24 |
| CW-IDK | judge does not know | 88% | 81% to 96% | 26 | 3 |
| HC-IDK | judge does not know | 98% | 94% to 100% | 26 | 0 |
| HW-IDK | judge does not know | 94% | 88% to 100% | 26 | 2 |
| CC-HC | judge tells the two answers apart | 86% | 79% to 93% | 42 | 4 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 42 | 0 |
| CW-CC | judge tells the two answers apart | 11% | 4% to 19% | 42 | 5 |
| CW-HC | judge tells the two answers apart | 26% | 16% to 37% | 41 | 11 |
| CW-HW | judge tells the two answers apart | 54% | 42% to 65% | 40 | 24 |
| CW-IDK | judge tells the two answers apart | 82% | 73% to 90% | 42 | 3 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 42 | 0 |
| HW-IDK | judge tells the two answers apart | 96% | 92% to 100% | 42 | 2 |
| CC-HC | judge flags the wrong answer as incorrect | 82% | 77% to 87% | 98 | 4 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 98 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 18% | 12% to 24% | 98 | 5 |
| CW-HC | judge flags the wrong answer as incorrect | 40% | 32% to 48% | 97 | 11 |
| CW-HW | judge flags the wrong answer as incorrect | 56% | 49% to 63% | 95 | 24 |
| CW-IDK | judge flags the wrong answer as incorrect | 83% | 78% to 88% | 98 | 3 |
| HC-IDK | judge flags the wrong answer as incorrect | 98% | 96% to 100% | 98 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 96% | 98 | 2 |
| CC-HC | judge knows and flags the wrong answer | 86% | 80% to 90% | 73 | 4 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 73 | 0 |
| CW-CC | judge knows and flags the wrong answer | 14% | 8% to 21% | 73 | 5 |
| CW-HC | judge knows and flags the wrong answer | 34% | 25% to 43% | 72 | 11 |
| CW-HW | judge knows and flags the wrong answer | 59% | 50% to 67% | 70 | 24 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 75% to 88% | 73 | 3 |
| HC-IDK | judge knows and flags the wrong answer | 99% | 97% to 100% | 73 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 93% | 89% to 97% | 73 | 2 |
| CC-IDK | domain geo | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain geo | 41% | 28% to 54% | 34 | 11 |
| CW-IDK | domain geo | 85% | 76% to 93% | 34 | 3 |
| CC-IDK | domain law | 99% | 96% to 100% | 34 | 0 |
| CW-HC | domain law | 47% | 32% to 60% | 34 | 11 |
| CW-IDK | domain law | 82% | 74% to 91% | 34 | 3 |
| CC-IDK | domain medqa | 99% | 96% to 100% | 34 | 0 |
| CW-HC | domain medqa | 38% | 24% to 52% | 33 | 11 |
| CW-IDK | domain medqa | 84% | 74% to 93% | 34 | 3 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-HC | domain geo, judge knows | 35% | 20% to 52% | 27 | 11 |
| CW-IDK | domain geo, judge knows | 85% | 74% to 94% | 27 | 3 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 21 | 0 |
| CW-HC | domain law, judge knows | 40% | 24% to 60% | 21 | 11 |
| CW-IDK | domain law, judge knows | 81% | 69% to 93% | 21 | 3 |
| CC-IDK | domain medqa, judge knows | 98% | 95% to 100% | 28 | 0 |
| CW-HC | domain medqa, judge knows | 33% | 19% to 48% | 27 | 11 |
| CW-IDK | domain medqa, judge knows | 80% | 68% to 91% | 28 | 3 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 84% | +0.15 | -2.23 | -3.86 to -1.37 | 58% | 49% | 43% |
| judge knows | 99% | 82% | +0.17 | -1.88 | -3.56 to -1.06 | 60% | 50% | 37% |
| judge does not know | 98% | 88% | +0.10 | -4.00 | -11.50 to -1.67 | 52% | 47% | 60% |
| judge tells the two answers apart | 100% | 82% | +0.18 | -1.80 | -4.25 to -0.83 | 55% | 45% | 26% |
| judge flags the wrong answer as incorrect | 99% | 83% | +0.16 | -2.10 | -3.67 to -1.29 | 57% | 48% | 41% |
| judge knows and flags the wrong answer | 99% | 82% | +0.18 | -1.77 | -3.44 to -0.97 | 59% | 50% | 35% |
| domain geo | 100% | 85% | +0.15 | -2.40 | -5.80 to -1.12 | 63% | 54% | 41% |
| domain law | 99% | 82% | +0.16 | -2.00 | -5.40 to -0.89 | 65% | 54% | 47% |
| domain medqa | 99% | 84% | +0.15 | -2.30 | -7.50 to -0.94 | 43% | 38% | 40% |
| domain geo, judge knows | 100% | 85% | +0.15 | -2.38 | -8.00 to -0.93 | 63% | 54% | 35% |
| domain law, judge knows | 100% | 81% | +0.19 | -1.63 | -6.00 to -0.50 | 69% | 56% | 40% |
| domain medqa, judge knows | 98% | 80% | +0.18 | -1.70 | -6.00 to -0.59 | 48% | 41% | 35% |

### prompt variant mtbench (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 97% | 93% to 100% | 102 | 0 |
| CW-IDK | all | 38% | 30% to 46% | 102 | 0 |
| CC-IDK | judge knows | 100% | 99% to 100% | 76 | 0 |
| CW-IDK | judge knows | 27% | 19% to 35% | 76 | 0 |
| CC-IDK | judge does not know | 88% | 77% to 98% | 26 | 0 |
| CW-IDK | judge does not know | 69% | 53% to 85% | 26 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 42 | 0 |
| CW-IDK | judge tells the two answers apart | 18% | 11% to 27% | 42 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 97% | 94% to 100% | 98 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 35% | 27% to 43% | 98 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 73 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 24% | 16% to 32% | 73 | 0 |
| CC-IDK | domain geo | 93% | 84% to 100% | 34 | 0 |
| CW-IDK | domain geo | 26% | 15% to 38% | 34 | 0 |
| CC-IDK | domain law | 98% | 94% to 100% | 34 | 0 |
| CW-IDK | domain law | 57% | 43% to 71% | 34 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 0 |
| CW-IDK | domain medqa | 29% | 17% to 43% | 34 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-IDK | domain geo, judge knows | 18% | 7% to 30% | 27 | 0 |
| CC-IDK | domain law, judge knows | 99% | 96% to 100% | 21 | 0 |
| CW-IDK | domain law, judge knows | 42% | 25% to 58% | 21 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 28 | 0 |
| CW-IDK | domain medqa, judge knows | 24% | 11% to 38% | 28 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 38% | +0.59 | +0.21 | +0.08 to +0.30 | - | - | - |
| judge knows | 100% | 27% | +0.73 | +0.32 | +0.23 to +0.39 | - | - | - |
| judge does not know | 88% | 69% | +0.19 | -1.00 | -6.20 to -0.07 | - | - | - |
| judge tells the two answers apart | 100% | 18% | +0.82 | +0.39 | +0.31 to +0.44 | - | - | - |
| judge flags the wrong answer as incorrect | 97% | 35% | +0.62 | +0.24 | +0.13 to +0.33 | - | - | - |
| judge knows and flags the wrong answer | 100% | 24% | +0.76 | +0.35 | +0.27 to +0.41 | - | - | - |
| domain geo | 93% | 26% | +0.67 | +0.36 | +0.22 to +0.45 | - | - | - |
| domain law | 98% | 57% | +0.40 | -0.18 | -0.83 to +0.13 | - | - | - |
| domain medqa | 100% | 29% | +0.71 | +0.29 | +0.12 to +0.40 | - | - | - |
| domain geo, judge knows | 100% | 18% | +0.82 | +0.39 | +0.29 to +0.46 | - | - | - |
| domain law, judge knows | 99% | 42% | +0.57 | +0.15 | -0.20 to +0.33 | - | - | - |
| domain medqa, judge knows | 100% | 24% | +0.76 | +0.34 | +0.19 to +0.44 | - | - | - |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 81% on 102 items

### prompt variant default (picks the first position in 45% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 99% to 100% | 102 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 102 | 0 |
| CW-CC | all | 19% | 13% to 25% | 102 | 1 |
| CW-HC | all | 50% | 41% to 58% | 102 | 1 |
| CW-HW | all | 98% | 96% to 100% | 102 | 2 |
| CW-IDK | all | 94% | 91% to 97% | 101 | 5 |
| HC-IDK | all | 93% | 89% to 96% | 102 | 0 |
| HW-IDK | all | 85% | 80% to 90% | 100 | 5 |
| CC-HC | judge knows | 99% | 98% to 100% | 83 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 83 | 0 |
| CW-CC | judge knows | 10% | 5% to 14% | 83 | 1 |
| CW-HC | judge knows | 42% | 33% to 51% | 83 | 1 |
| CW-HW | judge knows | 98% | 96% to 100% | 83 | 2 |
| CW-IDK | judge knows | 93% | 89% to 97% | 82 | 5 |
| HC-IDK | judge knows | 94% | 90% to 97% | 83 | 0 |
| HW-IDK | judge knows | 83% | 78% to 88% | 81 | 5 |
| CC-HC | judge does not know | 100% | 100% to 100% | 19 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 19 | 0 |
| CW-CC | judge does not know | 58% | 42% to 74% | 19 | 1 |
| CW-HC | judge does not know | 82% | 66% to 95% | 19 | 1 |
| CW-HW | judge does not know | 97% | 92% to 100% | 19 | 2 |
| CW-IDK | judge does not know | 97% | 92% to 100% | 19 | 5 |
| HC-IDK | judge does not know | 87% | 76% to 97% | 19 | 0 |
| HW-IDK | judge does not know | 92% | 84% to 100% | 19 | 5 |
| CC-HC | judge tells the two answers apart | 99% | 98% to 100% | 67 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 67 | 0 |
| CW-CC | judge tells the two answers apart | 9% | 4% to 15% | 67 | 1 |
| CW-HC | judge tells the two answers apart | 36% | 27% to 45% | 67 | 1 |
| CW-HW | judge tells the two answers apart | 97% | 94% to 99% | 67 | 2 |
| CW-IDK | judge tells the two answers apart | 91% | 86% to 95% | 66 | 5 |
| HC-IDK | judge tells the two answers apart | 95% | 91% to 98% | 67 | 0 |
| HW-IDK | judge tells the two answers apart | 82% | 76% to 88% | 66 | 5 |
| CC-HC | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 76 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 76 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 14% | 8% to 20% | 76 | 1 |
| CW-HC | judge flags the wrong answer as incorrect | 41% | 32% to 51% | 76 | 1 |
| CW-HW | judge flags the wrong answer as incorrect | 97% | 95% to 99% | 76 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 92% | 87% to 96% | 75 | 5 |
| HC-IDK | judge flags the wrong answer as incorrect | 92% | 88% to 96% | 76 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 83% | 77% to 88% | 75 | 5 |
| CC-HC | judge knows and flags the wrong answer | 99% | 98% to 100% | 67 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 67 | 0 |
| CW-CC | judge knows and flags the wrong answer | 9% | 4% to 15% | 67 | 1 |
| CW-HC | judge knows and flags the wrong answer | 37% | 28% to 47% | 67 | 1 |
| CW-HW | judge knows and flags the wrong answer | 98% | 95% to 100% | 67 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 92% | 86% to 96% | 66 | 5 |
| HC-IDK | judge knows and flags the wrong answer | 93% | 89% to 97% | 67 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 82% | 76% to 87% | 66 | 5 |
| CC-IDK | domain geo | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain geo | 41% | 28% to 56% | 34 | 1 |
| CW-IDK | domain geo | 90% | 81% to 97% | 34 | 5 |
| CC-IDK | domain law | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain law | 53% | 38% to 68% | 34 | 1 |
| CW-IDK | domain law | 97% | 93% to 100% | 34 | 5 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain medqa | 54% | 40% to 69% | 34 | 1 |
| CW-IDK | domain medqa | 95% | 89% to 100% | 33 | 5 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 31 | 0 |
| CW-HC | domain geo, judge knows | 35% | 23% to 50% | 31 | 1 |
| CW-IDK | domain geo, judge knows | 89% | 79% to 97% | 31 | 5 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 22 | 0 |
| CW-HC | domain law, judge knows | 41% | 23% to 59% | 22 | 1 |
| CW-IDK | domain law, judge knows | 98% | 93% to 100% | 22 | 5 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 30 | 0 |
| CW-HC | domain medqa, judge knows | 50% | 35% to 65% | 30 | 1 |
| CW-IDK | domain medqa, judge knows | 95% | 88% to 100% | 29 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 94% | +0.06 | -7.42 | -15.83 to -4.32 | 98% | 92% | 50% |
| judge knows | 100% | 93% | +0.07 | -6.45 | -15.40 to -3.56 | 98% | 92% | 43% |
| judge does not know | 100% | 97% | +0.03 | -18.00 | -18.00 to -5.33 | 97% | 95% | 82% |
| judge tells the two answers apart | 100% | 91% | +0.09 | -4.50 | -10.00 to -2.47 | 97% | 88% | 36% |
| judge flags the wrong answer as incorrect | 100% | 92% | +0.08 | -5.25 | -11.50 to -2.95 | 97% | 90% | 42% |
| judge knows and flags the wrong answer | 100% | 92% | +0.08 | -5.00 | -12.20 to -2.67 | 98% | 90% | 38% |
| domain geo | 100% | 90% | +0.10 | -3.86 | -16.00 to -1.62 | 99% | 88% | 41% |
| domain law | 100% | 97% | +0.03 | -16.00 | -16.00 to -5.80 | 99% | 96% | 53% |
| domain medqa | 100% | 95% | +0.05 | -10.00 | -15.50 to -3.71 | 97% | 93% | 56% |
| domain geo, judge knows | 100% | 89% | +0.11 | -3.43 | -14.50 to -1.38 | 98% | 87% | 35% |
| domain law, judge knows | 100% | 98% | +0.02 | -21.00 | -21.00 to -4.50 | 100% | 98% | 41% |
| domain medqa, judge knows | 100% | 95% | +0.05 | -8.67 | -13.50 to -3.14 | 97% | 92% | 52% |

### prompt variant mtbench (picks the first position in 48% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 99% | 97% to 100% | 102 | 1 |
| CW-IDK | all | 84% | 79% to 89% | 102 | 6 |
| CC-IDK | judge knows | 99% | 97% to 100% | 83 | 1 |
| CW-IDK | judge knows | 82% | 76% to 87% | 83 | 6 |
| CC-IDK | judge does not know | 97% | 92% to 100% | 19 | 1 |
| CW-IDK | judge does not know | 96% | 92% to 100% | 19 | 6 |
| CC-IDK | judge tells the two answers apart | 100% | 99% to 100% | 67 | 1 |
| CW-IDK | judge tells the two answers apart | 78% | 71% to 84% | 67 | 6 |
| CC-IDK | judge flags the wrong answer as incorrect | 98% | 96% to 100% | 76 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 80% | 74% to 85% | 76 | 6 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 97% to 100% | 67 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 78% | 71% to 84% | 67 | 6 |
| CC-IDK | domain geo | 99% | 96% to 100% | 34 | 1 |
| CW-IDK | domain geo | 83% | 74% to 91% | 34 | 6 |
| CC-IDK | domain law | 100% | 100% to 100% | 34 | 1 |
| CW-IDK | domain law | 93% | 87% to 98% | 34 | 6 |
| CC-IDK | domain medqa | 97% | 93% to 100% | 34 | 1 |
| CW-IDK | domain medqa | 77% | 68% to 85% | 34 | 6 |
| CC-IDK | domain geo, judge knows | 98% | 95% to 100% | 31 | 1 |
| CW-IDK | domain geo, judge knows | 81% | 72% to 90% | 31 | 6 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 22 | 1 |
| CW-IDK | domain law, judge knows | 91% | 82% to 98% | 22 | 6 |
| CC-IDK | domain medqa, judge knows | 98% | 96% to 100% | 30 | 1 |
| CW-IDK | domain medqa, judge knows | 75% | 65% to 84% | 30 | 6 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 84% | +0.14 | -2.41 | -4.10 to -1.54 | - | - | - |
| judge knows | 99% | 82% | +0.17 | -1.84 | -3.15 to -1.14 | - | - | - |
| judge does not know | 97% | 96% | +0.01 | undefined | -18.00 to -6.60 | - | - | - |
| judge tells the two answers apart | 100% | 78% | +0.22 | -1.25 | -2.12 to -0.74 | - | - | - |
| judge flags the wrong answer as incorrect | 98% | 80% | +0.19 | -1.58 | -2.70 to -0.95 | - | - | - |
| judge knows and flags the wrong answer | 99% | 78% | +0.21 | -1.30 | -2.31 to -0.76 | - | - | - |
| domain geo | 99% | 83% | +0.15 | -2.14 | -6.11 to -1.00 | - | - | - |
| domain law | 100% | 93% | +0.07 | -5.80 | -16.00 to -2.78 | - | - | - |
| domain medqa | 97% | 77% | +0.20 | -1.37 | -3.36 to -0.61 | - | - | - |
| domain geo, judge knows | 98% | 81% | +0.17 | -1.86 | -5.22 to -0.82 | - | - | - |
| domain law, judge knows | 100% | 91% | +0.09 | -4.50 | -21.00 to -1.75 | - | - | - |
| domain medqa, judge knows | 98% | 75% | +0.23 | -1.07 | -2.50 to -0.44 | - | - | - |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 81% on 102 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 92% | 89% to 96% | 102 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 102 | 0 |
| CW-CC | all | 15% | 10% to 22% | 102 | 0 |
| CW-HC | all | 25% | 17% to 32% | 102 | 0 |
| CW-HW | all | 69% | 63% to 75% | 102 | 0 |
| CW-IDK | all | 86% | 80% to 91% | 102 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 102 | 0 |
| HW-IDK | all | 99% | 98% to 100% | 102 | 0 |
| CC-HC | judge knows | 95% | 91% to 98% | 83 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 83 | 0 |
| CW-CC | judge knows | 7% | 3% to 11% | 83 | 0 |
| CW-HC | judge knows | 13% | 8% to 19% | 83 | 0 |
| CW-HW | judge knows | 67% | 60% to 73% | 83 | 0 |
| CW-IDK | judge knows | 83% | 77% to 89% | 83 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 83 | 0 |
| HW-IDK | judge knows | 99% | 97% to 100% | 83 | 0 |
| CC-HC | judge does not know | 82% | 71% to 92% | 19 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 19 | 0 |
| CW-CC | judge does not know | 53% | 34% to 74% | 19 | 0 |
| CW-HC | judge does not know | 74% | 55% to 89% | 19 | 0 |
| CW-HW | judge does not know | 76% | 66% to 87% | 19 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 19 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 19 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 19 | 0 |
| CC-HC | judge tells the two answers apart | 95% | 91% to 98% | 82 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 82 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 3% to 11% | 82 | 0 |
| CW-HC | judge tells the two answers apart | 15% | 9% to 21% | 82 | 0 |
| CW-HW | judge tells the two answers apart | 66% | 60% to 73% | 82 | 0 |
| CW-IDK | judge tells the two answers apart | 82% | 76% to 88% | 82 | 0 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 82 | 0 |
| HW-IDK | judge tells the two answers apart | 99% | 97% to 100% | 82 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 93% | 90% to 97% | 89 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 89 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 8% | 4% to 12% | 89 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 16% | 10% to 22% | 89 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 67% | 61% to 74% | 89 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 78% to 89% | 89 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 89 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 89 | 0 |
| CC-HC | judge knows and flags the wrong answer | 94% | 91% to 98% | 81 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 81 | 0 |
| CW-CC | judge knows and flags the wrong answer | 6% | 2% to 10% | 81 | 0 |
| CW-HC | judge knows and flags the wrong answer | 12% | 7% to 17% | 81 | 0 |
| CW-HW | judge knows and flags the wrong answer | 67% | 60% to 73% | 81 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 76% to 88% | 81 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 81 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 99% | 97% to 100% | 81 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain geo | 15% | 6% to 25% | 34 | 0 |
| CW-IDK | domain geo | 85% | 76% to 94% | 34 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain law | 35% | 22% to 49% | 34 | 0 |
| CW-IDK | domain law | 90% | 82% to 96% | 34 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain medqa | 24% | 12% to 37% | 34 | 0 |
| CW-IDK | domain medqa | 82% | 71% to 93% | 34 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 30 | 0 |
| CW-HC | domain geo, judge knows | 7% | 2% to 13% | 30 | 0 |
| CW-IDK | domain geo, judge knows | 83% | 73% to 92% | 30 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 24 | 0 |
| CW-HC | domain law, judge knows | 25% | 12% to 38% | 24 | 0 |
| CW-IDK | domain law, judge knows | 85% | 77% to 94% | 24 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 29 | 0 |
| CW-HC | domain medqa, judge knows | 10% | 3% to 21% | 29 | 0 |
| CW-IDK | domain medqa, judge knows | 79% | 66% to 91% | 29 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 86% | +0.14 | -2.52 | -4.37 to -1.55 | 69% | 59% | 25% |
| judge knows | 100% | 83% | +0.17 | -1.86 | -3.37 to -1.07 | 67% | 55% | 13% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 76% | 76% | 74% |
| judge tells the two answers apart | 100% | 82% | +0.18 | -1.83 | -3.32 to -1.05 | 66% | 55% | 15% |
| judge flags the wrong answer as incorrect | 100% | 84% | +0.16 | -2.07 | -3.68 to -1.23 | 67% | 56% | 16% |
| judge knows and flags the wrong answer | 100% | 82% | +0.18 | -1.79 | -3.26 to -1.08 | 67% | 55% | 12% |
| domain geo | 100% | 85% | +0.15 | -2.40 | -5.80 to -1.12 | 75% | 64% | 15% |
| domain law | 100% | 90% | +0.10 | -3.86 | -10.33 to -1.83 | 60% | 54% | 35% |
| domain medqa | 100% | 82% | +0.18 | -1.83 | -5.80 to -0.70 | 71% | 58% | 24% |
| domain geo, judge knows | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.87 | 72% | 60% | 7% |
| domain law, judge knows | 100% | 85% | +0.15 | -2.43 | -7.00 to -1.00 | 58% | 50% | 25% |
| domain medqa, judge knows | 100% | 79% | +0.21 | -1.42 | -4.80 to -0.53 | 69% | 55% | 10% |

### prompt variant mtbench (picks the first position in 52% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 99% to 100% | 102 | 0 |
| CW-IDK | all | 78% | 72% to 83% | 102 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 83 | 0 |
| CW-IDK | judge knows | 73% | 67% to 80% | 83 | 0 |
| CC-IDK | judge does not know | 99% | 96% to 100% | 19 | 0 |
| CW-IDK | judge does not know | 96% | 92% to 100% | 19 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 82 | 0 |
| CW-IDK | judge tells the two answers apart | 73% | 66% to 80% | 82 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 89 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 75% | 68% to 81% | 89 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 81 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 73% | 66% to 79% | 81 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 34 | 0 |
| CW-IDK | domain geo | 74% | 61% to 85% | 34 | 0 |
| CC-IDK | domain law | 99% | 98% to 100% | 34 | 0 |
| CW-IDK | domain law | 90% | 85% to 94% | 34 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 34 | 0 |
| CW-IDK | domain medqa | 70% | 60% to 79% | 34 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain geo, judge knows | 70% | 57% to 82% | 30 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 24 | 0 |
| CW-IDK | domain law, judge knows | 88% | 80% to 94% | 24 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 29 | 0 |
| CW-IDK | domain medqa, judge knows | 66% | 54% to 76% | 29 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 78% | +0.22 | -1.26 | -2.01 to -0.77 | - | - | - |
| judge knows | 100% | 73% | +0.27 | -0.89 | -1.48 to -0.50 | - | - | - |
| judge does not know | 99% | 96% | +0.03 | -17.50 | -18.00 to -5.17 | - | - | - |
| judge tells the two answers apart | 100% | 73% | +0.27 | -0.86 | -1.45 to -0.48 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 75% | +0.25 | -0.98 | -1.58 to -0.58 | - | - | - |
| judge knows and flags the wrong answer | 100% | 73% | +0.27 | -0.84 | -1.42 to -0.47 | - | - | - |
| domain geo | 100% | 74% | +0.26 | -0.89 | -2.24 to -0.28 | - | - | - |
| domain law | 99% | 90% | +0.10 | -4.15 | -10.00 to -2.24 | - | - | - |
| domain medqa | 100% | 70% | +0.30 | -0.66 | -1.34 to -0.26 | - | - | - |
| domain geo, judge knows | 100% | 70% | +0.30 | -0.67 | -1.86 to -0.15 | - | - | - |
| domain law, judge knows | 100% | 88% | +0.12 | -3.00 | -7.00 to -1.67 | - | - | - |
| domain medqa, judge knows | 100% | 66% | +0.34 | -0.45 | -1.07 to -0.12 | - | - | - |
