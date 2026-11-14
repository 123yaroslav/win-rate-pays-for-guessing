items 150 (geo, law, medqa), bootstrap draws 4000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 83.0% | 78.3% to 87.8% | 115 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 94.3% | 91.1% to 97.2% | 123 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.1% | 76.8% to 87.0% | 123 | 0.0000 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 84.3% | 80.0% to 88.3% | 150 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 95.0% | 92.3% to 97.3% | 149 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.3% | 80.7% to 89.7% | 150 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 83.7% | 79.2% to 87.8% | 144 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.9% | 89.0% to 96.2% | 105 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.5% | 78.6% to 88.0% | 133 | 0.0000 | yes |

## Detection (S1g)

| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |
|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 96.0% | 46.7% | 1 |
| openrouter/mistralai/mistral-small-2603 | 70.7% | 87.3% | 0 |
| openrouter/openai/gpt-5.6-luna | 88.7% | 88.0% | 0 |

## Verify-then-compare, composed from logged verdicts (exploratory)

| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |
|---|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 99.0% | 84.2% | 46.3% | 3.4% | 1.09 | 0.91 to 1.32 |
| openrouter/mistralai/mistral-small-2603 | 100.0% | 95.0% | 87.2% | 29.5% | 0.35 | 0.26 to 0.44 |
| openrouter/openai/gpt-5.6-luna | 100.0% | 85.3% | 88.0% | 11.3% | 0.50 | 0.46 to 0.54 |

## Instruction variants (Study 4 criterion)

| judge | variant | a, knows | b, knows | share of resamples with b at or above 0.5 | repaired | a, does not know | b, does not know |
|---|---|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | default | 100% | 83% | 1.000 | no | 97% | 89% |
| openrouter/anthropic/claude-haiku-5.5 | accuracy | 87% | 43% | 0.040 | no | 49% | 50% |
| openrouter/anthropic/claude-haiku-5.5 | cot | 99% | 19% | 0.000 | yes | 78% | 65% |
| openrouter/anthropic/claude-haiku-5.5 | data | 100% | 85% | 1.000 | no | 94% | 96% |
| openrouter/anthropic/claude-haiku-5.5 | selfcheck | 100% | 74% | 1.000 | no | 73% | 84% |
| openrouter/anthropic/claude-haiku-5.5 | stakes | 96% | 58% | 0.987 | no | 81% | 76% |
| openrouter/anthropic/claude-haiku-5.5 | think | 99% | 6% | 0.000 | yes | 70% | 27% |
| openrouter/mistralai/mistral-small-2603 | default | 100% | 94% | 1.000 | no | 100% | 98% |
| openrouter/mistralai/mistral-small-2603 | accuracy | 96% | 90% | 1.000 | no | 96% | 90% |
| openrouter/mistralai/mistral-small-2603 | cot | 97% | 68% | 1.000 | no | 91% | 97% |
| openrouter/mistralai/mistral-small-2603 | data | 100% | 97% | 1.000 | no | 100% | 100% |
| openrouter/mistralai/mistral-small-2603 | selfcheck | 100% | 77% | 1.000 | no | 75% | 86% |
| openrouter/mistralai/mistral-small-2603 | stakes | 98% | 72% | 1.000 | no | 90% | 87% |
| openrouter/mistralai/mistral-small-2603 | think | 100% | 93% | 1.000 | no | 100% | 100% |
| openrouter/openai/gpt-5.6-luna | default | 100% | 82% | 1.000 | no | 100% | 100% |
| openrouter/openai/gpt-5.6-luna | accuracy | 94% | 26% | 0.000 | yes | 65% | 59% |
| openrouter/openai/gpt-5.6-luna | cot | 100% | 85% | 1.000 | no | 100% | 100% |
| openrouter/openai/gpt-5.6-luna | data | 100% | 78% | 1.000 | no | 98% | 100% |
| openrouter/openai/gpt-5.6-luna | selfcheck | 100% | 77% | 1.000 | no | 87% | 96% |
| openrouter/openai/gpt-5.6-luna | stakes | 98% | 38% | 0.001 | yes | 76% | 72% |
| openrouter/openai/gpt-5.6-luna | think | 100% | 52% | 0.701 | no | 100% | 91% |

## Two-step account (S1d)

Cells 9, mean absolute error 0.295, Spearman 0.48. Mean predicted 67.1%, mean observed 37.6%.

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 77% on 150 items

### prompt variant default (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 83% | 79% to 87% | 150 | 5 |
| CC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| CW-HC | all | 39% | 32% to 45% | 148 | 18 |
| CW-HW | all | 58% | 53% to 64% | 146 | 34 |
| CW-IDK | all | 84% | 80% to 88% | 150 | 5 |
| HC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| HW-IDK | all | 94% | 91% to 96% | 150 | 3 |
| CC-HC | judge knows | 87% | 83% to 91% | 115 | 5 |
| CC-IDK | judge knows | 100% | 99% to 100% | 115 | 0 |
| CW-HC | judge knows | 32% | 25% to 39% | 113 | 18 |
| CW-HW | judge knows | 59% | 53% to 66% | 111 | 34 |
| CW-IDK | judge knows | 83% | 78% to 88% | 115 | 5 |
| HC-IDK | judge knows | 100% | 99% to 100% | 115 | 0 |
| HW-IDK | judge knows | 94% | 91% to 97% | 115 | 3 |
| CC-HC | judge does not know | 71% | 61% to 80% | 35 | 5 |
| CC-IDK | judge does not know | 97% | 93% to 100% | 35 | 0 |
| CW-HC | judge does not know | 60% | 47% to 73% | 35 | 18 |
| CW-HW | judge does not know | 54% | 43% to 66% | 35 | 34 |
| CW-IDK | judge does not know | 89% | 81% to 96% | 35 | 5 |
| HC-IDK | judge does not know | 97% | 93% to 100% | 35 | 0 |
| HW-IDK | judge does not know | 93% | 87% to 99% | 35 | 3 |
| CC-HC | judge flags the wrong answer as incorrect | 83% | 79% to 88% | 144 | 5 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 36% | 30% to 43% | 142 | 18 |
| CW-HW | judge flags the wrong answer as incorrect | 57% | 52% to 63% | 140 | 34 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 79% to 88% | 144 | 5 |
| HC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 96% | 144 | 3 |
| CC-HC | judge knows and flags the wrong answer | 87% | 83% to 91% | 112 | 5 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 112 | 0 |
| CW-HC | judge knows and flags the wrong answer | 30% | 24% to 37% | 110 | 18 |
| CW-HW | judge knows and flags the wrong answer | 59% | 53% to 66% | 108 | 34 |
| CW-IDK | judge knows and flags the wrong answer | 83% | 77% to 88% | 112 | 5 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 112 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 94% | 91% to 97% | 112 | 3 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 40% | 30% to 51% | 49 | 18 |
| CW-IDK | domain geo | 84% | 77% to 91% | 50 | 5 |
| CC-IDK | domain law | 99% | 97% to 100% | 50 | 0 |
| CW-HC | domain law | 43% | 32% to 54% | 50 | 18 |
| CW-IDK | domain law | 85% | 78% to 92% | 50 | 5 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 0 |
| CW-HC | domain medqa | 33% | 22% to 43% | 49 | 18 |
| CW-IDK | domain medqa | 84% | 76% to 91% | 50 | 5 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 43 | 0 |
| CW-HC | domain geo, judge knows | 35% | 24% to 46% | 42 | 18 |
| CW-IDK | domain geo, judge knows | 84% | 76% to 91% | 43 | 5 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 31 | 0 |
| CW-HC | domain law, judge knows | 34% | 21% to 48% | 31 | 18 |
| CW-IDK | domain law, judge knows | 85% | 76% to 94% | 31 | 5 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-HC | domain medqa, judge knows | 28% | 18% to 39% | 40 | 18 |
| CW-IDK | domain medqa, judge knows | 80% | 71% to 89% | 41 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 84% | +0.15 | -2.34 | -3.59 to -1.60 | 59% | 50% | 39% |
| judge knows | 100% | 83% | +0.17 | -2.00 | -3.35 to -1.30 | 60% | 50% | 32% |
| judge does not know | 97% | 89% | +0.09 | -4.50 | -15.00 to -2.00 | 54% | 50% | 60% |
| judge flags the wrong answer as incorrect | 99% | 84% | +0.15 | -2.20 | -3.45 to -1.49 | 58% | 49% | 37% |
| judge knows and flags the wrong answer | 100% | 83% | +0.17 | -1.92 | -3.11 to -1.22 | 60% | 50% | 31% |
| domain geo | 100% | 84% | +0.16 | -2.12 | -4.56 to -1.17 | 64% | 54% | 40% |
| domain law | 99% | 85% | +0.14 | -2.50 | -5.25 to -1.29 | 68% | 58% | 43% |
| domain medqa | 98% | 84% | +0.14 | -2.43 | -6.83 to -1.18 | 42% | 37% | 34% |
| domain geo, judge knows | 100% | 84% | +0.16 | -2.07 | -4.37 to -1.05 | 64% | 54% | 35% |
| domain law, judge knows | 100% | 85% | +0.15 | -2.44 | -6.75 to -1.07 | 71% | 61% | 34% |
| domain medqa, judge knows | 99% | 80% | +0.18 | -1.67 | -4.13 to -0.74 | 46% | 38% | 28% |

### prompt variant accuracy (picks the first position in 47% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 78% | 72% to 84% | 149 | 11 |
| CW-IDK | all | 45% | 38% to 51% | 142 | 34 |
| CC-IDK | judge knows | 87% | 82% to 92% | 115 | 11 |
| CW-IDK | judge knows | 43% | 36% to 50% | 107 | 34 |
| CC-IDK | judge does not know | 49% | 35% to 60% | 34 | 11 |
| CW-IDK | judge does not know | 50% | 37% to 63% | 35 | 34 |
| CC-IDK | judge flags the wrong answer as incorrect | 79% | 73% to 84% | 143 | 11 |
| CW-IDK | judge flags the wrong answer as incorrect | 43% | 36% to 50% | 136 | 34 |
| CC-IDK | judge knows and flags the wrong answer | 88% | 82% to 92% | 112 | 11 |
| CW-IDK | judge knows and flags the wrong answer | 42% | 35% to 50% | 104 | 34 |
| CC-IDK | domain geo | 85% | 76% to 93% | 50 | 11 |
| CW-IDK | domain geo | 41% | 28% to 52% | 48 | 34 |
| CC-IDK | domain law | 65% | 54% to 75% | 50 | 11 |
| CW-IDK | domain law | 46% | 35% to 57% | 50 | 34 |
| CC-IDK | domain medqa | 85% | 76% to 93% | 49 | 11 |
| CW-IDK | domain medqa | 48% | 35% to 59% | 44 | 34 |
| CC-IDK | domain geo, judge knows | 93% | 85% to 99% | 43 | 11 |
| CW-IDK | domain geo, judge knows | 38% | 26% to 51% | 41 | 34 |
| CC-IDK | domain law, judge knows | 76% | 65% to 87% | 31 | 11 |
| CW-IDK | domain law, judge knows | 45% | 31% to 58% | 31 | 34 |
| CC-IDK | domain medqa, judge knows | 89% | 80% to 96% | 41 | 11 |
| CW-IDK | domain medqa, judge knows | 47% | 34% to 61% | 35 | 34 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 78% | 44% | +0.33 | +0.17 | -0.05 to +0.31 | - | - | - |
| judge knows | 87% | 43% | +0.44 | +0.16 | -0.01 to +0.28 | - | - | - |
| judge does not know | 49% | 49% | +0.00 | undefined | -1.00 to +3.00 | - | - | - |
| judge flags the wrong answer as incorrect | 78% | 43% | +0.36 | +0.21 | +0.03 to +0.33 | - | - | - |
| judge knows and flags the wrong answer | 88% | 42% | +0.45 | +0.17 | +0.00 to +0.29 | - | - | - |
| domain geo | 86% | 41% | +0.46 | +0.20 | -0.07 to +0.39 | - | - | - |
| domain law | 65% | 46% | +0.19 | +0.21 | -0.86 to +0.58 | - | - | - |
| domain medqa | 83% | 47% | +0.36 | +0.10 | -0.38 to +0.32 | - | - | - |
| domain geo, judge knows | 95% | 38% | +0.57 | +0.21 | -0.03 to +0.36 | - | - | - |
| domain law, judge knows | 76% | 45% | +0.31 | +0.16 | -0.67 to +0.44 | - | - | - |
| domain medqa, judge knows | 87% | 47% | +0.40 | +0.07 | -0.40 to +0.30 | - | - | - |

### prompt variant cot (picks the first position in 46% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 89% to 98% | 88 | 20 |
| CW-IDK | all | 29% | 19% to 38% | 80 | 42 |
| CC-IDK | judge knows | 99% | 96% to 100% | 68 | 20 |
| CW-IDK | judge knows | 19% | 10% to 29% | 63 | 42 |
| CC-IDK | judge does not know | 78% | 57% to 92% | 20 | 20 |
| CW-IDK | judge does not know | 65% | 44% to 85% | 17 | 42 |
| CC-IDK | judge flags the wrong answer as incorrect | 95% | 90% to 99% | 85 | 20 |
| CW-IDK | judge flags the wrong answer as incorrect | 27% | 18% to 37% | 77 | 42 |
| CC-IDK | judge knows and flags the wrong answer | 98% | 96% to 100% | 66 | 20 |
| CW-IDK | judge knows and flags the wrong answer | 18% | 8% to 28% | 61 | 42 |
| CC-IDK | domain geo | 92% | 82% to 100% | 30 | 20 |
| CW-IDK | domain geo | 17% | 5% to 31% | 29 | 42 |
| CC-IDK | domain law | 90% | 80% to 98% | 30 | 20 |
| CW-IDK | domain law | 42% | 25% to 62% | 26 | 42 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 28 | 20 |
| CW-IDK | domain medqa | 28% | 12% to 44% | 25 | 42 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 25 | 20 |
| CW-IDK | domain geo, judge knows | 12% | 0% to 24% | 25 | 42 |
| CC-IDK | domain law, judge knows | 95% | 87% to 100% | 19 | 20 |
| CW-IDK | domain law, judge knows | 25% | 6% to 50% | 16 | 42 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 24 | 20 |
| CW-IDK | domain medqa, judge knows | 23% | 5% to 41% | 22 | 42 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 93% | 28% | +0.65 | +0.34 | +0.23 to +0.43 | - | - | - |
| judge knows | 98% | 19% | +0.79 | +0.39 | +0.30 to +0.46 | - | - | - |
| judge does not know | 72% | 62% | +0.09 | -1.33 | -7.00 to +0.38 | - | - | - |
| judge flags the wrong answer as incorrect | 94% | 26% | +0.68 | +0.35 | +0.24 to +0.43 | - | - | - |
| judge knows and flags the wrong answer | 98% | 18% | +0.80 | +0.40 | +0.31 to +0.46 | - | - | - |
| domain geo | 91% | 17% | +0.74 | +0.44 | +0.31 to +0.54 | - | - | - |
| domain law | 88% | 42% | +0.46 | +0.17 | -0.45 to +0.39 | - | - | - |
| domain medqa | 100% | 25% | +0.75 | +0.33 | +0.14 to +0.45 | - | - | - |
| domain geo, judge knows | 100% | 12% | +0.88 | +0.43 | +0.34 to +0.50 | - | - | - |
| domain law, judge knows | 94% | 25% | +0.69 | +0.36 | +0.00 to +0.53 | - | - | - |
| domain medqa, judge knows | 100% | 23% | +0.77 | +0.35 | +0.15 to +0.45 | - | - | - |

### prompt variant data (picks the first position in 52% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 98% | 97% to 100% | 150 | 1 |
| CW-IDK | all | 88% | 83% to 91% | 150 | 1 |
| CC-IDK | judge knows | 100% | 99% to 100% | 115 | 1 |
| CW-IDK | judge knows | 85% | 80% to 90% | 115 | 1 |
| CC-IDK | judge does not know | 94% | 89% to 99% | 35 | 1 |
| CW-IDK | judge does not know | 96% | 90% to 100% | 35 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 144 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 87% | 83% to 91% | 144 | 1 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 112 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 85% | 80% to 90% | 112 | 1 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain geo | 85% | 77% to 93% | 50 | 1 |
| CC-IDK | domain law | 97% | 93% to 100% | 50 | 1 |
| CW-IDK | domain law | 94% | 88% to 99% | 50 | 1 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 1 |
| CW-IDK | domain medqa | 84% | 77% to 90% | 50 | 1 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 43 | 1 |
| CW-IDK | domain geo, judge knows | 84% | 74% to 92% | 43 | 1 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 31 | 1 |
| CW-IDK | domain law, judge knows | 90% | 81% to 98% | 31 | 1 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 1 |
| CW-IDK | domain medqa, judge knows | 83% | 76% to 90% | 41 | 1 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 88% | +0.11 | -3.53 | -6.37 to -2.20 | - | - | - |
| judge knows | 100% | 85% | +0.14 | -2.45 | -4.18 to -1.58 | - | - | - |
| judge does not know | 94% | 96% | -0.01 | undefined | -16.00 to -4.83 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 87% | +0.11 | -3.24 | -5.70 to -2.07 | - | - | - |
| judge knows and flags the wrong answer | 100% | 85% | +0.15 | -2.36 | -4.05 to -1.47 | - | - | - |
| domain geo | 100% | 85% | +0.15 | -2.33 | -5.25 to -1.08 | - | - | - |
| domain law | 97% | 94% | +0.03 | -14.67 | -23.00 to -3.55 | - | - | - |
| domain medqa | 98% | 84% | +0.14 | -2.43 | -5.86 to -1.29 | - | - | - |
| domain geo, judge knows | 100% | 84% | +0.16 | -2.07 | -5.14 to -0.95 | - | - | - |
| domain law, judge knows | 100% | 90% | +0.10 | -4.17 | -14.50 to -1.58 | - | - | - |
| domain medqa, judge knows | 99% | 83% | +0.16 | -2.08 | -4.71 to -1.05 | - | - | - |

### prompt variant selfcheck (picks the first position in 40% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 91% to 96% | 150 | 0 |
| CW-IDK | all | 77% | 72% to 81% | 150 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 115 | 0 |
| CW-IDK | judge knows | 74% | 69% to 80% | 115 | 0 |
| CC-IDK | judge does not know | 73% | 64% to 81% | 35 | 0 |
| CW-IDK | judge does not know | 84% | 76% to 93% | 35 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 94% | 91% to 97% | 144 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 76% | 71% to 80% | 144 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 112 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 74% | 68% to 79% | 112 | 0 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 0 |
| CW-IDK | domain geo | 76% | 68% to 83% | 50 | 0 |
| CC-IDK | domain law | 90% | 84% to 95% | 50 | 0 |
| CW-IDK | domain law | 83% | 76% to 90% | 50 | 0 |
| CC-IDK | domain medqa | 95% | 90% to 99% | 50 | 0 |
| CW-IDK | domain medqa | 71% | 62% to 79% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 43 | 0 |
| CW-IDK | domain geo, judge knows | 76% | 67% to 84% | 43 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 31 | 0 |
| CW-IDK | domain law, judge knows | 81% | 73% to 89% | 31 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 68% | 60% to 78% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 94% | 77% | +0.17 | -1.57 | -2.63 to -1.00 | - | - | - |
| judge knows | 100% | 74% | +0.26 | -0.95 | -1.45 to -0.62 | - | - | - |
| judge does not know | 73% | 84% | -0.11 | undefined | -11.50 to -2.67 | - | - | - |
| judge flags the wrong answer as incorrect | 94% | 76% | +0.18 | -1.40 | -2.31 to -0.91 | - | - | - |
| judge knows and flags the wrong answer | 100% | 74% | +0.26 | -0.90 | -1.33 to -0.58 | - | - | - |
| domain geo | 96% | 76% | +0.20 | -1.30 | -2.67 to -0.69 | - | - | - |
| domain law | 90% | 83% | +0.07 | -4.71 | -18.50 to -1.59 | - | - | - |
| domain medqa | 95% | 71% | +0.24 | -0.87 | -2.07 to -0.36 | - | - | - |
| domain geo, judge knows | 100% | 76% | +0.24 | -1.05 | -2.07 to -0.54 | - | - | - |
| domain law, judge knows | 100% | 81% | +0.19 | -1.58 | -3.43 to -0.82 | - | - | - |
| domain medqa, judge knows | 100% | 68% | +0.32 | -0.58 | -1.28 to -0.24 | - | - | - |

### prompt variant stakes (picks the first position in 46% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 93% | 90% to 96% | 149 | 2 |
| CW-IDK | all | 62% | 56% to 69% | 148 | 12 |
| CC-IDK | judge knows | 96% | 93% to 98% | 114 | 2 |
| CW-IDK | judge knows | 58% | 51% to 65% | 113 | 12 |
| CC-IDK | judge does not know | 81% | 71% to 90% | 35 | 2 |
| CW-IDK | judge does not know | 76% | 64% to 87% | 35 | 12 |
| CC-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 96% | 143 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 61% | 55% to 68% | 142 | 12 |
| CC-IDK | judge knows and flags the wrong answer | 96% | 94% to 99% | 111 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 58% | 50% to 65% | 110 | 12 |
| CC-IDK | domain geo | 92% | 86% to 97% | 50 | 2 |
| CW-IDK | domain geo | 48% | 37% to 59% | 50 | 12 |
| CC-IDK | domain law | 90% | 83% to 96% | 49 | 2 |
| CW-IDK | domain law | 70% | 60% to 81% | 49 | 12 |
| CC-IDK | domain medqa | 96% | 92% to 99% | 50 | 2 |
| CW-IDK | domain medqa | 68% | 58% to 79% | 49 | 12 |
| CC-IDK | domain geo, judge knows | 95% | 91% to 99% | 43 | 2 |
| CW-IDK | domain geo, judge knows | 45% | 34% to 57% | 43 | 12 |
| CC-IDK | domain law, judge knows | 97% | 92% to 100% | 30 | 2 |
| CW-IDK | domain law, judge knows | 63% | 48% to 77% | 30 | 12 |
| CC-IDK | domain medqa, judge knows | 96% | 91% to 100% | 41 | 2 |
| CW-IDK | domain medqa, judge knows | 68% | 56% to 78% | 40 | 12 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 93% | 62% | +0.31 | -0.39 | -0.74 to -0.16 | - | - | - |
| judge knows | 96% | 58% | +0.38 | -0.20 | -0.47 to -0.01 | - | - | - |
| judge does not know | 81% | 76% | +0.06 | -4.50 | -11.00 to -0.67 | - | - | - |
| judge flags the wrong answer as incorrect | 93% | 61% | +0.32 | -0.34 | -0.67 to -0.12 | - | - | - |
| judge knows and flags the wrong answer | 96% | 57% | +0.39 | -0.19 | -0.44 to -0.01 | - | - | - |
| domain geo | 92% | 48% | +0.44 | +0.05 | -0.29 to +0.24 | - | - | - |
| domain law | 90% | 70% | +0.20 | -1.00 | -4.00 to -0.30 | - | - | - |
| domain medqa | 96% | 68% | +0.28 | -0.67 | -1.50 to -0.22 | - | - | - |
| domain geo, judge knows | 95% | 45% | +0.50 | +0.09 | -0.19 to +0.26 | - | - | - |
| domain law, judge knows | 97% | 62% | +0.34 | -0.35 | -1.25 to +0.04 | - | - | - |
| domain medqa, judge knows | 96% | 68% | +0.29 | -0.61 | -1.53 to -0.17 | - | - | - |

### prompt variant think (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 92% | 86% to 97% | 90 | 0 |
| CW-IDK | all | 11% | 6% to 18% | 90 | 0 |
| CC-IDK | judge knows | 99% | 96% to 100% | 68 | 0 |
| CW-IDK | judge knows | 6% | 1% to 12% | 68 | 0 |
| CC-IDK | judge does not know | 70% | 50% to 89% | 22 | 0 |
| CW-IDK | judge does not know | 27% | 11% to 45% | 22 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 93% | 88% to 98% | 87 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 9% | 4% to 15% | 87 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 66 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 5% | 1% to 9% | 66 | 0 |
| CC-IDK | domain geo | 87% | 75% to 97% | 30 | 0 |
| CW-IDK | domain geo | 10% | 2% to 22% | 30 | 0 |
| CC-IDK | domain law | 92% | 82% to 100% | 30 | 0 |
| CW-IDK | domain law | 12% | 2% to 23% | 30 | 0 |
| CC-IDK | domain medqa | 97% | 90% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 12% | 2% to 23% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 98% | 94% to 100% | 25 | 0 |
| CW-IDK | domain geo, judge knows | 6% | 0% to 16% | 25 | 0 |
| CC-IDK | domain law, judge knows | 97% | 92% to 100% | 19 | 0 |
| CW-IDK | domain law, judge knows | 5% | 0% to 16% | 19 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 24 | 0 |
| CW-IDK | domain medqa, judge knows | 6% | 0% to 17% | 24 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 92% | 11% | +0.81 | +0.48 | +0.44 to +0.52 | - | - | - |
| judge knows | 99% | 6% | +0.93 | +0.48 | +0.44 to +0.50 | - | - | - |
| judge does not know | 70% | 27% | +0.43 | +0.53 | +0.22 to +0.91 | - | - | - |
| judge flags the wrong answer as incorrect | 93% | 9% | +0.84 | +0.49 | +0.45 to +0.52 | - | - | - |
| judge knows and flags the wrong answer | 99% | 5% | +0.95 | +0.48 | +0.45 to +0.50 | - | - | - |
| domain geo | 87% | 10% | +0.77 | +0.52 | +0.45 to +0.61 | - | - | - |
| domain law | 92% | 12% | +0.80 | +0.48 | +0.40 to +0.54 | - | - | - |
| domain medqa | 97% | 12% | +0.85 | +0.45 | +0.37 to +0.50 | - | - | - |
| domain geo, judge knows | 98% | 6% | +0.92 | +0.48 | +0.41 to +0.52 | - | - | - |
| domain law, judge knows | 97% | 5% | +0.92 | +0.49 | +0.45 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 6% | +0.94 | +0.47 | +0.40 to +0.50 | - | - | - |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 83% on 150 items

### prompt variant default (picks the first position in 46% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 99% to 100% | 150 | 1 |
| CC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| CW-HC | all | 51% | 45% to 58% | 150 | 2 |
| CW-HW | all | 98% | 96% to 99% | 150 | 2 |
| CW-IDK | all | 95% | 92% to 97% | 149 | 7 |
| HC-IDK | all | 94% | 91% to 96% | 149 | 2 |
| HW-IDK | all | 84% | 80% to 88% | 148 | 7 |
| CC-HC | judge knows | 100% | 99% to 100% | 124 | 1 |
| CC-IDK | judge knows | 100% | 100% to 100% | 124 | 0 |
| CW-HC | judge knows | 46% | 38% to 53% | 124 | 2 |
| CW-HW | judge knows | 98% | 96% to 99% | 124 | 2 |
| CW-IDK | judge knows | 94% | 91% to 97% | 123 | 7 |
| HC-IDK | judge knows | 95% | 92% to 98% | 123 | 2 |
| HW-IDK | judge knows | 83% | 78% to 87% | 122 | 7 |
| CC-HC | judge does not know | 100% | 100% to 100% | 26 | 1 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 26 | 0 |
| CW-HC | judge does not know | 79% | 65% to 92% | 26 | 2 |
| CW-HW | judge does not know | 98% | 94% to 100% | 26 | 2 |
| CW-IDK | judge does not know | 98% | 94% to 100% | 26 | 7 |
| HC-IDK | judge does not know | 88% | 81% to 96% | 26 | 2 |
| HW-IDK | judge does not know | 90% | 83% to 98% | 26 | 7 |
| CC-HC | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 106 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 106 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 40% | 33% to 48% | 106 | 2 |
| CW-HW | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 106 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 93% | 89% to 96% | 105 | 7 |
| HC-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 96% | 106 | 2 |
| HW-IDK | judge flags the wrong answer as incorrect | 80% | 76% to 85% | 105 | 7 |
| CC-HC | judge knows and flags the wrong answer | 99% | 98% to 100% | 95 | 1 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 95 | 0 |
| CW-HC | judge knows and flags the wrong answer | 37% | 29% to 46% | 95 | 2 |
| CW-HW | judge knows and flags the wrong answer | 97% | 94% to 99% | 95 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 93% | 88% to 96% | 94 | 7 |
| HC-IDK | judge knows and flags the wrong answer | 94% | 91% to 97% | 95 | 2 |
| HW-IDK | judge knows and flags the wrong answer | 80% | 74% to 85% | 94 | 7 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 42% | 31% to 54% | 50 | 2 |
| CW-IDK | domain geo | 92% | 86% to 97% | 50 | 7 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain law | 60% | 48% to 72% | 50 | 2 |
| CW-IDK | domain law | 98% | 95% to 100% | 50 | 7 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain medqa | 52% | 40% to 64% | 50 | 2 |
| CW-IDK | domain medqa | 95% | 90% to 99% | 49 | 7 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-HC | domain geo, judge knows | 39% | 28% to 51% | 46 | 2 |
| CW-IDK | domain geo, judge knows | 91% | 85% to 97% | 46 | 7 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 34 | 0 |
| CW-HC | domain law, judge knows | 51% | 37% to 66% | 34 | 2 |
| CW-IDK | domain law, judge knows | 99% | 96% to 100% | 34 | 7 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 44 | 0 |
| CW-HC | domain medqa, judge knows | 48% | 35% to 60% | 44 | 2 |
| CW-IDK | domain medqa, judge knows | 94% | 90% to 99% | 43 | 7 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 95% | +0.05 | -8.93 | -17.63 to -5.48 | 98% | 93% | 52% |
| judge knows | 100% | 94% | +0.06 | -7.79 | -16.57 to -4.59 | 98% | 92% | 46% |
| judge does not know | 100% | 98% | +0.02 | undefined | -12.00 to -5.50 | 98% | 96% | 79% |
| judge flags the wrong answer as incorrect | 100% | 93% | +0.07 | -6.00 | -12.13 to -3.57 | 97% | 90% | 40% |
| judge knows and flags the wrong answer | 100% | 93% | +0.07 | -5.71 | -12.43 to -3.27 | 97% | 90% | 38% |
| domain geo | 100% | 92% | +0.08 | -5.25 | -15.67 to -2.57 | 97% | 89% | 42% |
| domain law | 100% | 98% | +0.02 | -24.00 | -24.00 to -7.33 | 99% | 97% | 60% |
| domain medqa | 100% | 95% | +0.05 | -8.80 | -23.50 to -4.44 | 97% | 92% | 53% |
| domain geo, judge knows | 100% | 91% | +0.09 | -4.75 | -14.33 to -2.29 | 97% | 88% | 39% |
| domain law, judge knows | 100% | 99% | +0.01 | undefined | -16.00 to -7.50 | 100% | 99% | 51% |
| domain medqa, judge knows | 100% | 94% | +0.06 | -7.60 | -20.50 to -3.30 | 97% | 91% | 49% |

### prompt variant accuracy (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 94% to 98% | 150 | 2 |
| CW-IDK | all | 90% | 86% to 93% | 150 | 2 |
| CC-IDK | judge knows | 96% | 94% to 98% | 124 | 2 |
| CW-IDK | judge knows | 90% | 85% to 93% | 124 | 2 |
| CC-IDK | judge does not know | 96% | 90% to 100% | 26 | 2 |
| CW-IDK | judge does not know | 90% | 83% to 98% | 26 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 97% | 95% to 99% | 106 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 87% | 83% to 92% | 106 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 97% | 94% to 99% | 95 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 87% | 83% to 92% | 95 | 2 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 2 |
| CW-IDK | domain geo | 89% | 83% to 94% | 50 | 2 |
| CC-IDK | domain law | 94% | 89% to 98% | 50 | 2 |
| CW-IDK | domain law | 89% | 82% to 95% | 50 | 2 |
| CC-IDK | domain medqa | 99% | 97% to 100% | 50 | 2 |
| CW-IDK | domain medqa | 91% | 86% to 96% | 50 | 2 |
| CC-IDK | domain geo, judge knows | 97% | 92% to 100% | 46 | 2 |
| CW-IDK | domain geo, judge knows | 88% | 82% to 93% | 46 | 2 |
| CC-IDK | domain law, judge knows | 93% | 87% to 99% | 34 | 2 |
| CW-IDK | domain law, judge knows | 90% | 81% to 97% | 34 | 2 |
| CC-IDK | domain medqa, judge knows | 99% | 97% to 100% | 44 | 2 |
| CW-IDK | domain medqa, judge knows | 91% | 85% to 97% | 44 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 90% | +0.07 | -5.95 | -14.11 to -3.48 | - | - | - |
| judge knows | 96% | 90% | +0.07 | -5.76 | -14.29 to -3.14 | - | - | - |
| judge does not know | 96% | 90% | +0.06 | -7.00 | -11.50 to -2.25 | - | - | - |
| judge flags the wrong answer as incorrect | 97% | 87% | +0.10 | -3.76 | -7.82 to -2.26 | - | - | - |
| judge knows and flags the wrong answer | 97% | 87% | +0.09 | -3.94 | -9.63 to -2.25 | - | - | - |
| domain geo | 96% | 89% | +0.07 | -5.57 | -20.00 to -2.43 | - | - | - |
| domain law | 94% | 89% | +0.05 | -7.80 | -20.50 to -2.58 | - | - | - |
| domain medqa | 99% | 91% | +0.08 | -5.13 | -15.00 to -2.57 | - | - | - |
| domain geo, judge knows | 97% | 88% | +0.09 | -4.38 | -17.50 to -2.00 | - | - | - |
| domain law, judge knows | 93% | 90% | +0.03 | -13.50 | -14.50 to -2.11 | - | - | - |
| domain medqa, judge knows | 99% | 91% | +0.08 | -5.14 | -19.50 to -2.38 | - | - | - |

### prompt variant cot (picks the first position in 61% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 92% to 98% | 90 | 0 |
| CW-IDK | all | 73% | 67% to 80% | 90 | 0 |
| CC-IDK | judge knows | 97% | 93% to 99% | 74 | 0 |
| CW-IDK | judge knows | 68% | 60% to 76% | 74 | 0 |
| CC-IDK | judge does not know | 91% | 81% to 100% | 16 | 0 |
| CW-IDK | judge does not know | 97% | 91% to 100% | 16 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 96% | 92% to 99% | 67 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 65% | 57% to 73% | 67 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 96% | 92% to 99% | 59 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 61% | 53% to 69% | 59 | 0 |
| CC-IDK | domain geo | 92% | 85% to 98% | 30 | 0 |
| CW-IDK | domain geo | 48% | 37% to 60% | 30 | 0 |
| CC-IDK | domain law | 97% | 92% to 100% | 30 | 0 |
| CW-IDK | domain law | 88% | 78% to 97% | 30 | 0 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 83% | 75% to 92% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 93% | 86% to 98% | 28 | 0 |
| CW-IDK | domain geo, judge knows | 45% | 34% to 55% | 28 | 0 |
| CC-IDK | domain law, judge knows | 98% | 92% to 100% | 20 | 0 |
| CW-IDK | domain law, judge knows | 85% | 72% to 95% | 20 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 81% | 71% to 90% | 26 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 73% | +0.22 | -1.05 | -1.93 to -0.57 | - | - | - |
| judge knows | 97% | 68% | +0.28 | -0.64 | -1.19 to -0.29 | - | - | - |
| judge does not know | 91% | 97% | -0.06 | undefined | -15.00 to -4.00 | - | - | - |
| judge flags the wrong answer as incorrect | 96% | 65% | +0.31 | -0.49 | -1.00 to -0.17 | - | - | - |
| judge knows and flags the wrong answer | 96% | 61% | +0.35 | -0.32 | -0.73 to -0.06 | - | - | - |
| domain geo | 92% | 48% | +0.43 | +0.04 | -0.33 to +0.24 | - | - | - |
| domain law | 97% | 88% | +0.08 | -4.60 | -13.00 to -1.55 | - | - | - |
| domain medqa | 98% | 83% | +0.15 | -2.22 | -6.25 to -1.00 | - | - | - |
| domain geo, judge knows | 93% | 45% | +0.48 | +0.11 | -0.17 to +0.29 | - | - | - |
| domain law, judge knows | 98% | 85% | +0.12 | -2.80 | -18.00 to -0.89 | - | - | - |
| domain medqa, judge knows | 100% | 81% | +0.19 | -1.60 | -4.20 to -0.73 | - | - | - |

### prompt variant data (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 150 | 1 |
| CW-IDK | all | 98% | 96% to 99% | 149 | 2 |
| CC-IDK | judge knows | 100% | 100% to 100% | 124 | 1 |
| CW-IDK | judge knows | 97% | 95% to 99% | 123 | 2 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 26 | 1 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 26 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 106 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 105 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 95 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 96% | 94% to 99% | 94 | 2 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain geo | 95% | 91% to 99% | 50 | 2 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain law | 99% | 97% to 100% | 50 | 2 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain medqa | 99% | 97% to 100% | 49 | 2 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 1 |
| CW-IDK | domain geo, judge knows | 95% | 90% to 99% | 46 | 2 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 34 | 1 |
| CW-IDK | domain law, judge knows | 99% | 96% to 100% | 34 | 2 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 44 | 1 |
| CW-IDK | domain medqa, judge knows | 99% | 97% to 100% | 43 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 98% | +0.02 | -20.29 | -23.83 to -10.46 | - | - | - |
| judge knows | 100% | 97% | +0.03 | -16.57 | -23.60 to -8.46 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 97% | +0.03 | -14.00 | -20.00 to -7.75 | - | - | - |
| judge knows and flags the wrong answer | 100% | 96% | +0.04 | -12.43 | -22.50 to -6.83 | - | - | - |
| domain geo | 100% | 95% | +0.05 | -9.00 | -24.00 to -4.00 | - | - | - |
| domain law | 100% | 99% | +0.01 | undefined | -24.00 to -11.50 | - | - | - |
| domain medqa | 100% | 99% | +0.01 | undefined | -23.50 to -11.25 | - | - | - |
| domain geo, judge knows | 100% | 95% | +0.05 | -8.20 | -22.00 to -4.11 | - | - | - |
| domain law, judge knows | 100% | 99% | +0.01 | undefined | -16.00 to -7.50 | - | - | - |
| domain medqa, judge knows | 100% | 99% | +0.01 | undefined | -20.50 to -9.75 | - | - | - |

### prompt variant selfcheck (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 95% | 93% to 98% | 150 | 3 |
| CW-IDK | all | 79% | 74% to 83% | 131 | 51 |
| CC-IDK | judge knows | 100% | 99% to 100% | 124 | 3 |
| CW-IDK | judge knows | 77% | 72% to 82% | 106 | 51 |
| CC-IDK | judge does not know | 75% | 65% to 85% | 26 | 3 |
| CW-IDK | judge does not know | 86% | 78% to 94% | 25 | 51 |
| CC-IDK | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 106 | 3 |
| CW-IDK | judge flags the wrong answer as incorrect | 75% | 70% to 81% | 91 | 51 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 95 | 3 |
| CW-IDK | judge knows and flags the wrong answer | 74% | 68% to 80% | 81 | 51 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 3 |
| CW-IDK | domain geo | 81% | 74% to 88% | 45 | 51 |
| CC-IDK | domain law | 92% | 86% to 97% | 50 | 3 |
| CW-IDK | domain law | 76% | 68% to 84% | 44 | 51 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 3 |
| CW-IDK | domain medqa | 79% | 71% to 86% | 42 | 51 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 46 | 3 |
| CW-IDK | domain geo, judge knows | 79% | 72% to 87% | 41 | 51 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 34 | 3 |
| CW-IDK | domain law, judge knows | 74% | 64% to 84% | 29 | 51 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 44 | 3 |
| CW-IDK | domain medqa, judge knows | 76% | 68% to 85% | 36 | 51 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 95% | 79% | +0.16 | -1.79 | -2.87 to -1.18 | - | - | - |
| judge knows | 100% | 77% | +0.23 | -1.19 | -1.78 to -0.80 | - | - | - |
| judge does not know | 74% | 86% | -0.12 | undefined | +nan to +nan | - | - | - |
| judge flags the wrong answer as incorrect | 96% | 75% | +0.21 | -1.21 | -2.00 to -0.74 | - | - | - |
| judge knows and flags the wrong answer | 99% | 74% | +0.25 | -0.95 | -1.50 to -0.59 | - | - | - |
| domain geo | 96% | 81% | +0.14 | -2.15 | -6.00 to -1.05 | - | - | - |
| domain law | 91% | 76% | +0.15 | -1.77 | -5.00 to -0.81 | - | - | - |
| domain medqa | 98% | 79% | +0.19 | -1.50 | -3.22 to -0.78 | - | - | - |
| domain geo, judge knows | 99% | 79% | +0.20 | -1.50 | -3.00 to -0.78 | - | - | - |
| domain law, judge knows | 100% | 74% | +0.26 | -0.93 | -2.22 to -0.38 | - | - | - |
| domain medqa, judge knows | 100% | 76% | +0.24 | -1.12 | -2.27 to -0.57 | - | - | - |

### prompt variant stakes (picks the first position in 37% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 94% to 98% | 150 | 1 |
| CW-IDK | all | 75% | 70% to 79% | 149 | 5 |
| CC-IDK | judge knows | 98% | 96% to 99% | 124 | 1 |
| CW-IDK | judge knows | 72% | 68% to 77% | 123 | 5 |
| CC-IDK | judge does not know | 90% | 83% to 98% | 26 | 1 |
| CW-IDK | judge does not know | 87% | 77% to 94% | 26 | 5 |
| CC-IDK | judge flags the wrong answer as incorrect | 96% | 93% to 98% | 106 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 67% | 63% to 73% | 106 | 5 |
| CC-IDK | judge knows and flags the wrong answer | 97% | 95% to 99% | 95 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 66% | 61% to 72% | 95 | 5 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 1 |
| CW-IDK | domain geo | 60% | 53% to 67% | 50 | 5 |
| CC-IDK | domain law | 95% | 90% to 99% | 50 | 1 |
| CW-IDK | domain law | 89% | 83% to 95% | 49 | 5 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 1 |
| CW-IDK | domain medqa | 76% | 69% to 83% | 50 | 5 |
| CC-IDK | domain geo, judge knows | 97% | 92% to 100% | 46 | 1 |
| CW-IDK | domain geo, judge knows | 59% | 52% to 65% | 46 | 5 |
| CC-IDK | domain law, judge knows | 96% | 90% to 100% | 34 | 1 |
| CW-IDK | domain law, judge knows | 88% | 80% to 95% | 33 | 5 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 44 | 1 |
| CW-IDK | domain medqa, judge knows | 75% | 68% to 83% | 44 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 75% | +0.21 | -1.16 | -1.70 to -0.78 | - | - | - |
| judge knows | 98% | 72% | +0.25 | -0.89 | -1.33 to -0.59 | - | - | - |
| judge does not know | 90% | 87% | +0.04 | -9.50 | -10.50 to -1.86 | - | - | - |
| judge flags the wrong answer as incorrect | 96% | 67% | +0.28 | -0.62 | -0.98 to -0.37 | - | - | - |
| judge knows and flags the wrong answer | 97% | 66% | +0.31 | -0.53 | -0.85 to -0.31 | - | - | - |
| domain geo | 96% | 60% | +0.36 | -0.28 | -0.58 to -0.09 | - | - | - |
| domain law | 95% | 89% | +0.06 | -6.33 | -21.00 to -2.46 | - | - | - |
| domain medqa | 98% | 76% | +0.22 | -1.18 | -2.29 to -0.66 | - | - | - |
| domain geo, judge knows | 97% | 59% | +0.38 | -0.23 | -0.52 to -0.05 | - | - | - |
| domain law, judge knows | 95% | 88% | +0.08 | -5.00 | -14.00 to -1.90 | - | - | - |
| domain medqa, judge knows | 100% | 75% | +0.25 | -1.00 | -1.93 to -0.57 | - | - | - |

### prompt variant think (picks the first position in 47% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 90 | 0 |
| CW-IDK | all | 94% | 91% to 97% | 88 | 5 |
| CC-IDK | judge knows | 100% | 100% to 100% | 74 | 0 |
| CW-IDK | judge knows | 93% | 89% to 97% | 72 | 5 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 16 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 16 | 5 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 67 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 93% | 89% to 97% | 66 | 5 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 59 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 92% | 87% to 97% | 58 | 5 |
| CC-IDK | domain geo | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain geo | 88% | 80% to 95% | 30 | 5 |
| CC-IDK | domain law | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain law | 97% | 91% to 100% | 29 | 5 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 98% | 95% to 100% | 29 | 5 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 28 | 0 |
| CW-IDK | domain geo, judge knows | 88% | 79% to 95% | 28 | 5 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 20 | 0 |
| CW-IDK | domain law, judge knows | 95% | 87% to 100% | 19 | 5 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 98% | 94% to 100% | 25 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 94% | +0.06 | -7.80 | -16.60 to -4.50 | - | - | - |
| judge knows | 100% | 93% | +0.07 | -6.20 | -13.40 to -3.50 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 93% | +0.07 | -6.33 | -15.50 to -3.40 | - | - | - |
| judge knows and flags the wrong answer | 100% | 92% | +0.08 | -5.44 | -13.50 to -2.87 | - | - | - |
| domain geo | 100% | 88% | +0.12 | -3.29 | -9.00 to -1.50 | - | - | - |
| domain law | 100% | 97% | +0.03 | -13.50 | -13.50 to -4.80 | - | - | - |
| domain medqa | 100% | 98% | +0.02 | undefined | -13.50 to -6.25 | - | - | - |
| domain geo, judge knows | 100% | 88% | +0.12 | -3.00 | -8.33 to -1.33 | - | - | - |
| domain law, judge knows | 100% | 95% | +0.05 | -8.50 | -18.00 to -2.80 | - | - | - |
| domain medqa, judge knows | 100% | 98% | +0.02 | -24.00 | -24.00 to -5.25 | - | - | - |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 82% on 150 items

### prompt variant default (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 93% | 90% to 96% | 150 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| CW-HC | all | 22% | 17% to 28% | 150 | 0 |
| CW-HW | all | 69% | 64% to 74% | 150 | 0 |
| CW-IDK | all | 85% | 81% to 90% | 150 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| HW-IDK | all | 98% | 96% to 100% | 150 | 0 |
| CC-HC | judge knows | 96% | 93% to 98% | 123 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 123 | 0 |
| CW-HC | judge knows | 13% | 9% to 18% | 123 | 0 |
| CW-HW | judge knows | 66% | 61% to 72% | 123 | 0 |
| CW-IDK | judge knows | 82% | 77% to 87% | 123 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 123 | 0 |
| HW-IDK | judge knows | 98% | 95% to 100% | 123 | 0 |
| CC-HC | judge does not know | 81% | 72% to 91% | 27 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 27 | 0 |
| CW-HC | judge does not know | 65% | 50% to 80% | 27 | 0 |
| CW-HW | judge does not know | 81% | 72% to 91% | 27 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 27 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 27 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 27 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 94% | 91% to 97% | 133 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 133 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 15% | 11% to 20% | 133 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 68% | 62% to 73% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 83% | 79% to 88% | 133 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 133 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 98% | 95% to 100% | 133 | 0 |
| CC-HC | judge knows and flags the wrong answer | 96% | 93% to 98% | 118 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 118 | 0 |
| CW-HC | judge knows and flags the wrong answer | 10% | 6% to 14% | 118 | 0 |
| CW-HW | judge knows and flags the wrong answer | 66% | 60% to 72% | 118 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 81% | 76% to 86% | 118 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 118 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 97% | 95% to 100% | 118 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 14% | 7% to 22% | 50 | 0 |
| CW-IDK | domain geo | 83% | 74% to 91% | 50 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain law | 33% | 23% to 43% | 50 | 0 |
| CW-IDK | domain law | 90% | 84% to 95% | 50 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain medqa | 20% | 10% to 31% | 50 | 0 |
| CW-IDK | domain medqa | 83% | 74% to 91% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-HC | domain geo, judge knows | 8% | 3% to 13% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 82% | 73% to 90% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 35 | 0 |
| CW-HC | domain law, judge knows | 27% | 17% to 39% | 35 | 0 |
| CW-IDK | domain law, judge knows | 86% | 77% to 93% | 35 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 42 | 0 |
| CW-HC | domain medqa, judge knows | 7% | 1% to 14% | 42 | 0 |
| CW-IDK | domain medqa, judge knows | 80% | 70% to 88% | 42 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 85% | +0.15 | -2.41 | -3.69 to -1.63 | 69% | 59% | 22% |
| judge knows | 100% | 82% | +0.18 | -1.80 | -2.84 to -1.16 | 66% | 54% | 13% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 81% | 81% | 65% |
| judge flags the wrong answer as incorrect | 100% | 83% | +0.17 | -2.02 | -3.16 to -1.33 | 68% | 56% | 15% |
| judge knows and flags the wrong answer | 100% | 81% | +0.19 | -1.68 | -2.69 to -1.11 | 66% | 54% | 10% |
| domain geo | 100% | 83% | +0.17 | -1.94 | -4.56 to -0.92 | 72% | 60% | 14% |
| domain law | 100% | 90% | +0.10 | -4.00 | -9.00 to -2.12 | 64% | 58% | 33% |
| domain medqa | 100% | 83% | +0.17 | -1.94 | -4.56 to -0.92 | 71% | 59% | 20% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.71 | -4.11 to -0.84 | 71% | 58% | 8% |
| domain law, judge knows | 100% | 86% | +0.14 | -2.50 | -6.00 to -1.33 | 60% | 51% | 27% |
| domain medqa, judge knows | 100% | 80% | +0.20 | -1.47 | -3.20 to -0.68 | 67% | 53% | 7% |

### prompt variant accuracy (picks the first position in 58% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 89% | 84% to 93% | 150 | 0 |
| CW-IDK | all | 32% | 26% to 39% | 150 | 0 |
| CC-IDK | judge knows | 94% | 91% to 97% | 123 | 0 |
| CW-IDK | judge knows | 26% | 20% to 33% | 123 | 0 |
| CC-IDK | judge does not know | 65% | 48% to 80% | 27 | 0 |
| CW-IDK | judge does not know | 59% | 44% to 74% | 27 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 92% | 88% to 95% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 26% | 20% to 32% | 133 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 95% | 92% to 98% | 118 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 24% | 18% to 31% | 118 | 0 |
| CC-IDK | domain geo | 98% | 95% to 100% | 50 | 0 |
| CW-IDK | domain geo | 20% | 11% to 30% | 50 | 0 |
| CC-IDK | domain law | 76% | 66% to 85% | 50 | 0 |
| CW-IDK | domain law | 41% | 31% to 51% | 50 | 0 |
| CC-IDK | domain medqa | 93% | 86% to 99% | 50 | 0 |
| CW-IDK | domain medqa | 36% | 25% to 48% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 16% | 8% to 26% | 46 | 0 |
| CC-IDK | domain law, judge knows | 84% | 76% to 93% | 35 | 0 |
| CW-IDK | domain law, judge knows | 39% | 26% to 51% | 35 | 0 |
| CC-IDK | domain medqa, judge knows | 98% | 93% to 100% | 42 | 0 |
| CW-IDK | domain medqa, judge knows | 27% | 17% to 39% | 42 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 89% | 32% | +0.57 | +0.31 | +0.23 to +0.38 | - | - | - |
| judge knows | 94% | 26% | +0.68 | +0.35 | +0.28 to +0.40 | - | - | - |
| judge does not know | 65% | 59% | +0.06 | -1.67 | -4.00 to +0.40 | - | - | - |
| judge flags the wrong answer as incorrect | 92% | 26% | +0.66 | +0.37 | +0.30 to +0.42 | - | - | - |
| judge knows and flags the wrong answer | 95% | 24% | +0.71 | +0.37 | +0.30 to +0.42 | - | - | - |
| domain geo | 98% | 20% | +0.78 | +0.38 | +0.29 to +0.45 | - | - | - |
| domain law | 76% | 41% | +0.35 | +0.26 | -0.05 to +0.44 | - | - | - |
| domain medqa | 93% | 36% | +0.57 | +0.25 | +0.04 to +0.38 | - | - | - |
| domain geo, judge knows | 99% | 16% | +0.83 | +0.41 | +0.33 to +0.46 | - | - | - |
| domain law, judge knows | 84% | 39% | +0.46 | +0.25 | -0.04 to +0.42 | - | - | - |
| domain medqa, judge knows | 98% | 27% | +0.70 | +0.32 | +0.19 to +0.42 | - | - | - |

### prompt variant cot (picks the first position in 54% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 90 | 0 |
| CW-IDK | all | 88% | 82% to 93% | 90 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 73 | 0 |
| CW-IDK | judge knows | 85% | 78% to 90% | 73 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 17 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 17 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 79 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 86% | 80% to 92% | 79 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 71 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 85% | 77% to 91% | 71 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain geo | 87% | 77% to 95% | 30 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain law | 95% | 90% to 100% | 30 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 82% | 72% to 92% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-IDK | domain geo, judge knows | 85% | 74% to 94% | 27 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 20 | 0 |
| CW-IDK | domain law, judge knows | 92% | 85% to 100% | 20 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 79% | 67% to 88% | 26 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 88% | +0.12 | -3.09 | -5.92 to -1.81 | - | - | - |
| judge knows | 100% | 85% | +0.15 | -2.32 | -4.62 to -1.28 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 86% | +0.14 | -2.59 | -5.08 to -1.47 | - | - | - |
| judge knows and flags the wrong answer | 100% | 85% | +0.15 | -2.23 | -4.46 to -1.29 | - | - | - |
| domain geo | 100% | 87% | +0.13 | -2.75 | -9.00 to -1.14 | - | - | - |
| domain law | 100% | 95% | +0.05 | -9.00 | -14.00 to -3.29 | - | - | - |
| domain medqa | 100% | 82% | +0.18 | -1.73 | -5.00 to -0.76 | - | - | - |
| domain geo, judge knows | 100% | 85% | +0.15 | -2.38 | -8.00 to -0.93 | - | - | - |
| domain law, judge knows | 100% | 92% | +0.07 | -5.67 | -19.00 to -2.33 | - | - | - |
| domain medqa, judge knows | 100% | 79% | +0.21 | -1.36 | -3.33 to -0.53 | - | - | - |

### prompt variant data (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 99% to 100% | 150 | 0 |
| CW-IDK | all | 82% | 77% to 86% | 150 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 123 | 0 |
| CW-IDK | judge knows | 78% | 72% to 83% | 123 | 0 |
| CC-IDK | judge does not know | 98% | 94% to 100% | 27 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 27 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 79% | 74% to 84% | 133 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 118 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 77% | 71% to 82% | 118 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain geo | 77% | 68% to 86% | 50 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain law | 88% | 82% to 94% | 50 | 0 |
| CC-IDK | domain medqa | 99% | 97% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 80% | 71% to 88% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 75% | 65% to 84% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 35 | 0 |
| CW-IDK | domain law, judge knows | 83% | 74% to 90% | 35 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 42 | 0 |
| CW-IDK | domain medqa, judge knows | 76% | 65% to 86% | 42 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 82% | +0.18 | -1.76 | -2.70 to -1.17 | - | - | - |
| judge knows | 100% | 78% | +0.22 | -1.24 | -1.93 to -0.81 | - | - | - |
| judge does not know | 98% | 100% | -0.02 | undefined | +nan to +nan | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 79% | +0.20 | -1.44 | -2.25 to -0.94 | - | - | - |
| judge knows and flags the wrong answer | 100% | 77% | +0.23 | -1.15 | -1.81 to -0.71 | - | - | - |
| domain geo | 100% | 77% | +0.23 | -1.17 | -2.33 to -0.56 | - | - | - |
| domain law | 100% | 88% | +0.12 | -3.17 | -7.33 to -1.78 | - | - | - |
| domain medqa | 99% | 80% | +0.19 | -1.58 | -3.90 to -0.75 | - | - | - |
| domain geo, judge knows | 100% | 75% | +0.25 | -1.00 | -2.07 to -0.44 | - | - | - |
| domain law, judge knows | 100% | 83% | +0.17 | -1.92 | -4.00 to -1.06 | - | - | - |
| domain medqa, judge knows | 100% | 76% | +0.24 | -1.10 | -2.50 to -0.45 | - | - | - |

### prompt variant selfcheck (picks the first position in 58% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 98% | 96% to 99% | 150 | 0 |
| CW-IDK | all | 81% | 76% to 85% | 150 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 123 | 0 |
| CW-IDK | judge knows | 77% | 72% to 82% | 123 | 0 |
| CC-IDK | judge does not know | 87% | 78% to 94% | 27 | 0 |
| CW-IDK | judge does not know | 96% | 91% to 100% | 27 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 98% | 96% to 100% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 78% | 73% to 83% | 133 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 118 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 76% | 71% to 81% | 118 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain geo | 75% | 66% to 83% | 50 | 0 |
| CC-IDK | domain law | 97% | 93% to 100% | 50 | 0 |
| CW-IDK | domain law | 87% | 81% to 93% | 50 | 0 |
| CC-IDK | domain medqa | 96% | 92% to 99% | 50 | 0 |
| CW-IDK | domain medqa | 80% | 72% to 87% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 73% | 64% to 82% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 35 | 0 |
| CW-IDK | domain law, judge knows | 84% | 77% to 91% | 35 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 42 | 0 |
| CW-IDK | domain medqa, judge knows | 76% | 67% to 85% | 42 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 81% | +0.17 | -1.80 | -2.82 to -1.19 | - | - | - |
| judge knows | 100% | 77% | +0.23 | -1.20 | -1.86 to -0.81 | - | - | - |
| judge does not know | 87% | 96% | -0.09 | undefined | -12.00 to -7.33 | - | - | - |
| judge flags the wrong answer as incorrect | 98% | 78% | +0.20 | -1.42 | -2.23 to -0.93 | - | - | - |
| judge knows and flags the wrong answer | 100% | 76% | +0.24 | -1.11 | -1.68 to -0.74 | - | - | - |
| domain geo | 100% | 75% | +0.25 | -1.00 | -1.94 to -0.47 | - | - | - |
| domain law | 97% | 87% | +0.10 | -3.70 | -10.50 to -1.82 | - | - | - |
| domain medqa | 96% | 80% | +0.16 | -1.88 | -5.57 to -0.88 | - | - | - |
| domain geo, judge knows | 100% | 73% | +0.27 | -0.84 | -1.71 to -0.35 | - | - | - |
| domain law, judge knows | 100% | 84% | +0.16 | -2.18 | -4.83 to -1.06 | - | - | - |
| domain medqa, judge knows | 100% | 76% | +0.24 | -1.10 | -2.23 to -0.50 | - | - | - |

### prompt variant stakes (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 90% to 96% | 150 | 0 |
| CW-IDK | all | 44% | 37% to 51% | 150 | 1 |
| CC-IDK | judge knows | 98% | 96% to 99% | 123 | 0 |
| CW-IDK | judge knows | 38% | 30% to 46% | 123 | 1 |
| CC-IDK | judge does not know | 76% | 63% to 87% | 27 | 0 |
| CW-IDK | judge does not know | 72% | 57% to 85% | 27 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 95% | 92% to 97% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 38% | 32% to 45% | 133 | 1 |
| CC-IDK | judge knows and flags the wrong answer | 98% | 96% to 100% | 118 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 36% | 29% to 44% | 118 | 1 |
| CC-IDK | domain geo | 97% | 93% to 100% | 50 | 0 |
| CW-IDK | domain geo | 27% | 17% to 38% | 50 | 1 |
| CC-IDK | domain law | 88% | 81% to 94% | 50 | 0 |
| CW-IDK | domain law | 59% | 48% to 70% | 50 | 1 |
| CC-IDK | domain medqa | 96% | 91% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 46% | 34% to 58% | 50 | 1 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 25% | 15% to 36% | 46 | 1 |
| CC-IDK | domain law, judge knows | 94% | 89% to 99% | 35 | 0 |
| CW-IDK | domain law, judge knows | 54% | 40% to 67% | 35 | 1 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 42 | 0 |
| CW-IDK | domain medqa, judge knows | 38% | 25% to 52% | 42 | 1 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 94% | 44% | +0.50 | +0.12 | -0.02 to +0.23 | - | - | - |
| judge knows | 98% | 38% | +0.60 | +0.20 | +0.09 to +0.29 | - | - | - |
| judge does not know | 76% | 72% | +0.04 | -6.00 | -7.50 to -0.33 | - | - | - |
| judge flags the wrong answer as incorrect | 95% | 38% | +0.56 | +0.21 | +0.10 to +0.29 | - | - | - |
| judge knows and flags the wrong answer | 98% | 36% | +0.62 | +0.23 | +0.12 to +0.31 | - | - | - |
| domain geo | 97% | 27% | +0.70 | +0.33 | +0.21 to +0.42 | - | - | - |
| domain law | 88% | 59% | +0.29 | -0.31 | -1.18 to +0.06 | - | - | - |
| domain medqa | 96% | 46% | +0.50 | +0.08 | -0.22 to +0.26 | - | - | - |
| domain geo, judge knows | 99% | 25% | +0.74 | +0.34 | +0.23 to +0.42 | - | - | - |
| domain law, judge knows | 94% | 54% | +0.40 | -0.11 | -0.67 to +0.17 | - | - | - |
| domain medqa, judge knows | 99% | 38% | +0.61 | +0.20 | -0.02 to +0.34 | - | - | - |

### prompt variant think (picks the first position in 60% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 90 | 0 |
| CW-IDK | all | 59% | 52% to 67% | 90 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 73 | 0 |
| CW-IDK | judge knows | 52% | 45% to 60% | 73 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 17 | 0 |
| CW-IDK | judge does not know | 91% | 76% to 100% | 17 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 79 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 54% | 46% to 61% | 79 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 71 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 51% | 42% to 59% | 71 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain geo | 37% | 23% to 50% | 30 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain law | 80% | 72% to 88% | 30 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 62% | 50% to 73% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-IDK | domain geo, judge knows | 33% | 20% to 48% | 27 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 20 | 0 |
| CW-IDK | domain law, judge knows | 72% | 62% to 82% | 20 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 56% | 44% to 69% | 26 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 59% | +0.41 | -0.23 | -0.50 to -0.03 | - | - | - |
| judge knows | 100% | 52% | +0.48 | -0.04 | -0.26 to +0.11 | - | - | - |
| judge does not know | 100% | 91% | +0.09 | -4.67 | -16.00 to -1.12 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 54% | +0.46 | -0.08 | -0.32 to +0.07 | - | - | - |
| judge knows and flags the wrong answer | 100% | 51% | +0.49 | -0.01 | -0.20 to +0.13 | - | - | - |
| domain geo | 100% | 37% | +0.63 | +0.21 | +0.00 to +0.35 | - | - | - |
| domain law | 100% | 80% | +0.20 | -1.50 | -3.29 to -0.76 | - | - | - |
| domain medqa | 100% | 62% | +0.38 | -0.30 | -0.87 to +0.00 | - | - | - |
| domain geo, judge knows | 100% | 33% | +0.67 | +0.25 | +0.04 to +0.37 | - | - | - |
| domain law, judge knows | 100% | 72% | +0.28 | -0.82 | -1.86 to -0.33 | - | - | - |
| domain medqa, judge knows | 100% | 56% | +0.44 | -0.13 | -0.53 to +0.13 | - | - | - |
