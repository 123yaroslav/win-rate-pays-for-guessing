items 300 (geo, law, medqa), bootstrap draws 10000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 7 of 7 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 91.9% | 85.1% to 97.3% | 37 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 66.7% | 53.3% to 80.0% | 30 | 0.0100 | yes |
| adaption/qwen3.8-27b | 65.0% | 55.0% to 75.0% | 30 | 0.0010 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 82.7% | 79.1% to 86.1% | 237 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.1% | 89.6% to 94.5% | 227 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.8% | 80.0% to 87.2% | 253 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-terra | 68.0% | 57.0% to 78.0% | 50 | 0.0005 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 7 of 7 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 93.5% | 88.0% to 97.8% | 46 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 74.4% | 63.3% to 84.4% | 45 | 0.0000 | yes |
| adaption/qwen3.8-27b | 68.5% | 60.9% to 76.1% | 46 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 84.4% | 81.4% to 87.2% | 298 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 93.1% | 90.9% to 95.1% | 298 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.5% | 82.3% to 88.5% | 300 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-terra | 72.5% | 63.3% to 81.7% | 60 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 4 of 4 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 84.0% | 81.0% to 86.9% | 287 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 90.3% | 87.4% to 93.0% | 207 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.7% | 80.1% to 86.9% | 267 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-terra | 69.4% | 59.3% to 79.6% | 54 | 0.0003 | yes |

## Detection (S1g)

| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |
|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 96.3% | 52.3% | 1 |
| openrouter/mistralai/mistral-small-2603 | 69.7% | 86.7% | 0 |
| openrouter/openai/gpt-5.6-luna | 89.0% | 86.7% | 0 |
| openrouter/openai/gpt-5.6-terra | 90.0% | 85.0% | 0 |

## Verify-then-compare, composed from logged verdicts (exploratory)

| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |
|---|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 98.1% | 84.3% | 51.7% | 3.2% | 0.97 | 0.87 to 1.09 |
| openrouter/mistralai/mistral-small-2603 | 99.8% | 93.1% | 86.6% | 30.4% | 0.35 | 0.28 to 0.41 |
| openrouter/openai/gpt-5.6-luna | 99.8% | 85.5% | 86.7% | 11.0% | 0.52 | 0.49 to 0.54 |
| openrouter/openai/gpt-5.6-terra | 100.0% | 72.5% | 85.0% | 10.0% | 0.53 | 0.46 to 0.61 |

## Two-step account (S1d)

Cells 9, mean absolute error 0.303, Spearman 0.63. Mean predicted 66.5%, mean observed 36.2%.

## adaption/deepseek-v4-flash: own closed-book accuracy 83% on 300 items

### prompt variant default (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 46 | 0 |
| CW-HC | all | 73% | 62% to 83% | 46 | 0 |
| CW-IDK | all | 93% | 88% to 98% | 46 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 37 | 0 |
| CW-HC | judge knows | 66% | 54% to 77% | 37 | 0 |
| CW-IDK | judge knows | 92% | 85% to 97% | 37 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 9 | 0 |
| CW-HC | judge does not know | 100% | 100% to 100% | 9 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 9 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 15 | 0 |
| CW-HC | domain geo | 67% | 47% to 87% | 15 | 0 |
| CW-IDK | domain geo | 90% | 80% to 100% | 15 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 15 | 0 |
| CW-HC | domain law | 77% | 53% to 93% | 15 | 0 |
| CW-IDK | domain law | 97% | 90% to 100% | 15 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 16 | 0 |
| CW-HC | domain medqa | 75% | 62% to 88% | 16 | 0 |
| CW-IDK | domain medqa | 94% | 84% to 100% | 16 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 13 | 0 |
| CW-HC | domain geo, judge knows | 62% | 38% to 85% | 13 | 0 |
| CW-IDK | domain geo, judge knows | 88% | 77% to 100% | 13 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 11 | 0 |
| CW-HC | domain law, judge knows | 68% | 41% to 91% | 11 | 0 |
| CW-IDK | domain law, judge knows | 95% | 86% to 100% | 11 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 13 | 0 |
| CW-HC | domain medqa, judge knows | 69% | 58% to 81% | 13 | 0 |
| CW-IDK | domain medqa, judge knows | 92% | 81% to 100% | 13 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 93% | +0.07 | -6.67 | -22.00 to -3.18 | - | - | - |
| judge knows | 100% | 92% | +0.08 | -5.17 | -17.50 to -2.36 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo | 100% | 90% | +0.10 | -4.00 | -14.00 to -1.50 | - | - | - |
| domain law | 100% | 97% | +0.03 | -14.00 | -14.00 to -4.00 | - | - | - |
| domain medqa | 100% | 94% | +0.06 | -7.00 | -15.00 to -2.20 | - | - | - |
| domain geo, judge knows | 100% | 88% | +0.12 | -3.33 | -12.00 to -1.17 | - | - | - |
| domain law, judge knows | 100% | 95% | +0.05 | -10.00 | -10.00 to -2.67 | - | - | - |
| domain medqa, judge knows | 100% | 92% | +0.08 | -5.50 | -12.00 to -1.60 | - | - | - |

## adaption/gemma-4-31b-it: own closed-book accuracy 82% on 300 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 98% | 95% to 100% | 46 | 0 |
| CW-HC | all | 32% | 20% to 43% | 46 | 3 |
| CW-IDK | all | 74% | 63% to 84% | 45 | 5 |
| CC-IDK | judge knows | 100% | 100% to 100% | 31 | 0 |
| CW-HC | judge knows | 13% | 5% to 24% | 31 | 3 |
| CW-IDK | judge knows | 67% | 53% to 80% | 30 | 5 |
| CC-IDK | judge does not know | 93% | 83% to 100% | 15 | 0 |
| CW-HC | judge does not know | 70% | 50% to 90% | 15 | 3 |
| CW-IDK | judge does not know | 90% | 73% to 100% | 15 | 5 |
| CC-IDK | domain geo | 93% | 83% to 100% | 15 | 0 |
| CW-HC | domain geo | 20% | 3% to 40% | 15 | 3 |
| CW-IDK | domain geo | 43% | 27% to 60% | 15 | 5 |
| CC-IDK | domain law | 100% | 100% to 100% | 15 | 0 |
| CW-HC | domain law | 33% | 13% to 57% | 15 | 3 |
| CW-IDK | domain law | 100% | 100% to 100% | 15 | 5 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 16 | 0 |
| CW-HC | domain medqa | 41% | 19% to 62% | 16 | 3 |
| CW-IDK | domain medqa | 80% | 63% to 93% | 15 | 5 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-HC | domain geo, judge knows | 8% | 0% to 21% | 12 | 3 |
| CW-IDK | domain geo, judge knows | 38% | 21% to 54% | 12 | 5 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 8 | 0 |
| CW-HC | domain law, judge knows | 0% | 0% to 0% | 8 | 3 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 8 | 5 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 11 | 0 |
| CW-HC | domain medqa, judge knows | 27% | 5% to 50% | 11 | 3 |
| CW-IDK | domain medqa, judge knows | 75% | 50% to 95% | 10 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 74% | +0.23 | -1.05 | -2.58 to -0.42 | - | - | - |
| judge knows | 100% | 67% | +0.33 | -0.50 | -1.50 to -0.07 | - | - | - |
| judge does not know | 93% | 90% | +0.03 | -12.00 | -14.00 to -1.50 | - | - | - |
| domain geo | 93% | 43% | +0.50 | +0.13 | -0.40 to +0.37 | - | - | - |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa | 100% | 80% | +0.20 | -1.50 | -6.50 to -0.36 | - | - | - |
| domain geo, judge knows | 100% | 38% | +0.62 | +0.20 | -0.09 to +0.37 | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 75% | +0.25 | -1.00 | -9.00 to -0.11 | - | - | - |

## adaption/qwen3.8-27b: own closed-book accuracy 77% on 300 items

### prompt variant default (picks the first position in 29% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 88% | 82% to 93% | 46 | 0 |
| CW-HC | all | 42% | 34% to 51% | 46 | 1 |
| CW-IDK | all | 68% | 61% to 76% | 46 | 2 |
| CC-IDK | judge knows | 93% | 87% to 98% | 30 | 0 |
| CW-HC | judge knows | 32% | 23% to 40% | 30 | 1 |
| CW-IDK | judge knows | 65% | 55% to 75% | 30 | 2 |
| CC-IDK | judge does not know | 78% | 66% to 91% | 16 | 0 |
| CW-HC | judge does not know | 62% | 47% to 78% | 16 | 1 |
| CW-IDK | judge does not know | 75% | 62% to 88% | 16 | 2 |
| CC-IDK | domain geo | 97% | 90% to 100% | 15 | 0 |
| CW-HC | domain geo | 47% | 30% to 63% | 15 | 1 |
| CW-IDK | domain geo | 73% | 57% to 87% | 15 | 2 |
| CC-IDK | domain law | 83% | 70% to 93% | 15 | 0 |
| CW-HC | domain law | 37% | 20% to 53% | 15 | 1 |
| CW-IDK | domain law | 67% | 57% to 80% | 15 | 2 |
| CC-IDK | domain medqa | 84% | 72% to 94% | 16 | 0 |
| CW-HC | domain medqa | 44% | 31% to 56% | 16 | 1 |
| CW-IDK | domain medqa | 66% | 56% to 78% | 16 | 2 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-HC | domain geo, judge knows | 33% | 21% to 46% | 12 | 1 |
| CW-IDK | domain geo, judge knows | 67% | 50% to 83% | 12 | 2 |
| CC-IDK | domain law, judge knows | 85% | 70% to 100% | 10 | 0 |
| CW-HC | domain law, judge knows | 25% | 10% to 40% | 10 | 1 |
| CW-IDK | domain law, judge knows | 65% | 50% to 80% | 10 | 2 |
| CC-IDK | domain medqa, judge knows | 94% | 81% to 100% | 8 | 0 |
| CW-HC | domain medqa, judge knows | 38% | 19% to 50% | 8 | 1 |
| CW-IDK | domain medqa, judge knows | 62% | 50% to 81% | 8 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 88% | 68% | +0.20 | -0.94 | -2.40 to -0.39 | - | - | - |
| judge knows | 93% | 65% | +0.28 | -0.53 | -1.27 to -0.16 | - | - | - |
| judge does not know | 78% | 75% | +0.03 | -8.00 | -10.00 to -0.67 | - | - | - |
| domain geo | 97% | 73% | +0.23 | -1.00 | -5.50 to -0.17 | - | - | - |
| domain law | 83% | 67% | +0.17 | -1.00 | -4.00 to -0.22 | - | - | - |
| domain medqa | 84% | 66% | +0.19 | -0.83 | -6.00 to -0.17 | - | - | - |
| domain geo, judge knows | 100% | 67% | +0.33 | -0.50 | -2.00 to +0.00 | - | - | - |
| domain law, judge knows | 85% | 65% | +0.20 | -0.75 | -4.00 to +0.00 | - | - | - |
| domain medqa, judge knows | 94% | 62% | +0.31 | -0.40 | -2.00 to +0.00 | - | - | - |

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 80% on 300 items

### prompt variant default (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 81% | 78% to 84% | 299 | 9 |
| CC-IDK | all | 98% | 97% to 99% | 300 | 0 |
| CW-HC | all | 36% | 32% to 41% | 295 | 36 |
| CW-HW | all | 59% | 55% to 63% | 290 | 64 |
| CW-IDK | all | 84% | 81% to 87% | 298 | 11 |
| HC-IDK | all | 100% | 99% to 100% | 300 | 1 |
| HW-IDK | all | 93% | 91% to 95% | 300 | 6 |
| CC-HC | judge knows | 86% | 83% to 89% | 238 | 9 |
| CC-IDK | judge knows | 99% | 98% to 100% | 239 | 0 |
| CW-HC | judge knows | 32% | 27% to 37% | 234 | 36 |
| CW-HW | judge knows | 59% | 55% to 64% | 229 | 64 |
| CW-IDK | judge knows | 83% | 79% to 86% | 237 | 11 |
| HC-IDK | judge knows | 100% | 99% to 100% | 239 | 1 |
| HW-IDK | judge knows | 93% | 91% to 95% | 239 | 6 |
| CC-HC | judge does not know | 65% | 57% to 72% | 61 | 9 |
| CC-IDK | judge does not know | 94% | 90% to 98% | 61 | 0 |
| CW-HC | judge does not know | 51% | 42% to 60% | 61 | 36 |
| CW-HW | judge does not know | 58% | 51% to 66% | 61 | 64 |
| CW-IDK | judge does not know | 91% | 86% to 96% | 61 | 11 |
| HC-IDK | judge does not know | 99% | 98% to 100% | 61 | 1 |
| HW-IDK | judge does not know | 94% | 90% to 98% | 61 | 6 |
| CC-HC | judge flags the wrong answer as incorrect | 81% | 78% to 84% | 288 | 9 |
| CC-IDK | judge flags the wrong answer as incorrect | 98% | 97% to 99% | 289 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 34% | 29% to 38% | 284 | 36 |
| CW-HW | judge flags the wrong answer as incorrect | 58% | 54% to 62% | 279 | 64 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 81% to 87% | 287 | 11 |
| HC-IDK | judge flags the wrong answer as incorrect | 99% | 99% to 100% | 289 | 1 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 91% to 95% | 289 | 6 |
| CC-HC | judge knows and flags the wrong answer | 86% | 82% to 89% | 231 | 9 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 232 | 0 |
| CW-HC | judge knows and flags the wrong answer | 31% | 26% to 36% | 227 | 36 |
| CW-HW | judge knows and flags the wrong answer | 59% | 54% to 64% | 222 | 64 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 79% to 86% | 230 | 11 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 232 | 1 |
| HW-IDK | judge knows and flags the wrong answer | 93% | 91% to 95% | 232 | 6 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 37% | 29% to 45% | 98 | 36 |
| CW-IDK | domain geo | 83% | 78% to 87% | 99 | 11 |
| CC-IDK | domain law | 96% | 94% to 99% | 100 | 0 |
| CW-HC | domain law | 36% | 28% to 44% | 99 | 36 |
| CW-IDK | domain law | 85% | 80% to 90% | 100 | 11 |
| CC-IDK | domain medqa | 98% | 96% to 100% | 100 | 0 |
| CW-HC | domain medqa | 36% | 29% to 43% | 98 | 36 |
| CW-IDK | domain medqa | 85% | 80% to 90% | 99 | 11 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 90 | 0 |
| CW-HC | domain geo, judge knows | 34% | 26% to 43% | 88 | 36 |
| CW-IDK | domain geo, judge knows | 82% | 76% to 87% | 89 | 11 |
| CC-IDK | domain law, judge knows | 98% | 95% to 100% | 67 | 0 |
| CW-HC | domain law, judge knows | 31% | 21% to 41% | 66 | 36 |
| CW-IDK | domain law, judge knows | 83% | 76% to 89% | 67 | 11 |
| CC-IDK | domain medqa, judge knows | 99% | 98% to 100% | 82 | 0 |
| CW-HC | domain medqa, judge knows | 31% | 23% to 39% | 80 | 36 |
| CW-IDK | domain medqa, judge knows | 83% | 77% to 90% | 81 | 11 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 84% | +0.14 | -2.50 | -3.48 to -1.89 | 59% | 51% | 36% |
| judge knows | 99% | 83% | +0.16 | -1.99 | -2.75 to -1.47 | 59% | 49% | 33% |
| judge does not know | 94% | 91% | +0.03 | -12.50 | -17.67 to -3.75 | 58% | 56% | 51% |
| judge flags the wrong answer as incorrect | 98% | 84% | +0.14 | -2.38 | -3.26 to -1.77 | 58% | 50% | 34% |
| judge knows and flags the wrong answer | 99% | 82% | +0.17 | -1.94 | -2.69 to -1.42 | 59% | 49% | 31% |
| domain geo | 100% | 83% | +0.17 | -1.91 | -2.96 to -1.25 | 64% | 53% | 38% |
| domain law | 96% | 85% | +0.11 | -3.04 | -6.08 to -1.79 | 69% | 61% | 36% |
| domain medqa | 98% | 85% | +0.13 | -2.80 | -5.71 to -1.64 | 43% | 38% | 35% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.78 | -2.87 to -1.12 | 64% | 52% | 35% |
| domain law, judge knows | 98% | 83% | +0.15 | -2.20 | -4.36 to -1.23 | 69% | 59% | 32% |
| domain medqa, judge knows | 99% | 83% | +0.16 | -2.08 | -4.00 to -1.19 | 45% | 38% | 30% |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 76% on 300 items

### prompt variant default (picks the first position in 46% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 99% | 98% to 100% | 300 | 2 |
| CC-IDK | all | 100% | 100% to 100% | 300 | 0 |
| CW-HC | all | 50% | 45% to 55% | 299 | 5 |
| CW-HW | all | 97% | 96% to 98% | 299 | 4 |
| CW-IDK | all | 93% | 91% to 95% | 298 | 12 |
| HC-IDK | all | 94% | 92% to 96% | 299 | 4 |
| HW-IDK | all | 83% | 80% to 86% | 295 | 15 |
| CC-HC | judge knows | 99% | 98% to 100% | 229 | 2 |
| CC-IDK | judge knows | 100% | 99% to 100% | 229 | 0 |
| CW-HC | judge knows | 42% | 37% to 48% | 228 | 5 |
| CW-HW | judge knows | 97% | 95% to 98% | 228 | 4 |
| CW-IDK | judge knows | 92% | 90% to 94% | 227 | 12 |
| HC-IDK | judge knows | 95% | 93% to 97% | 228 | 4 |
| HW-IDK | judge knows | 81% | 78% to 85% | 224 | 15 |
| CC-HC | judge does not know | 100% | 100% to 100% | 71 | 2 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 71 | 0 |
| CW-HC | judge does not know | 73% | 64% to 82% | 71 | 5 |
| CW-HW | judge does not know | 99% | 96% to 100% | 71 | 4 |
| CW-IDK | judge does not know | 96% | 94% to 99% | 71 | 12 |
| HC-IDK | judge does not know | 91% | 86% to 95% | 71 | 4 |
| HW-IDK | judge does not know | 88% | 83% to 93% | 71 | 15 |
| CC-HC | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 209 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 209 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 39% | 33% to 44% | 208 | 5 |
| CW-HW | judge flags the wrong answer as incorrect | 96% | 94% to 98% | 208 | 4 |
| CW-IDK | judge flags the wrong answer as incorrect | 90% | 87% to 93% | 207 | 12 |
| HC-IDK | judge flags the wrong answer as incorrect | 94% | 92% to 96% | 209 | 4 |
| HW-IDK | judge flags the wrong answer as incorrect | 79% | 75% to 83% | 206 | 15 |
| CC-HC | judge knows and flags the wrong answer | 99% | 98% to 100% | 172 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 172 | 0 |
| CW-HC | judge knows and flags the wrong answer | 34% | 29% to 40% | 171 | 5 |
| CW-HW | judge knows and flags the wrong answer | 96% | 94% to 98% | 171 | 4 |
| CW-IDK | judge knows and flags the wrong answer | 90% | 86% to 93% | 170 | 12 |
| HC-IDK | judge knows and flags the wrong answer | 96% | 93% to 98% | 172 | 4 |
| HW-IDK | judge knows and flags the wrong answer | 78% | 74% to 82% | 169 | 15 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 47% | 38% to 55% | 99 | 5 |
| CW-IDK | domain geo | 89% | 84% to 93% | 99 | 12 |
| CC-IDK | domain law | 100% | 98% to 100% | 100 | 0 |
| CW-HC | domain law | 54% | 46% to 62% | 100 | 5 |
| CW-IDK | domain law | 96% | 94% to 99% | 100 | 12 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain medqa | 48% | 40% to 56% | 100 | 5 |
| CW-IDK | domain medqa | 94% | 90% to 97% | 99 | 12 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 90 | 0 |
| CW-HC | domain geo, judge knows | 43% | 34% to 52% | 89 | 5 |
| CW-IDK | domain geo, judge knows | 88% | 83% to 93% | 89 | 12 |
| CC-IDK | domain law, judge knows | 99% | 98% to 100% | 63 | 0 |
| CW-HC | domain law, judge knows | 44% | 34% to 56% | 63 | 5 |
| CW-IDK | domain law, judge knows | 96% | 92% to 99% | 63 | 12 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 76 | 0 |
| CW-HC | domain medqa, judge knows | 40% | 31% to 49% | 76 | 5 |
| CW-IDK | domain medqa, judge knows | 93% | 89% to 97% | 75 | 12 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 93% | +0.07 | -6.42 | -9.61 to -4.69 | 97% | 91% | 50% |
| judge knows | 100% | 92% | +0.08 | -5.46 | -8.38 to -3.83 | 97% | 89% | 43% |
| judge does not know | 100% | 96% | +0.04 | -13.20 | -22.67 to -6.10 | 99% | 95% | 73% |
| judge flags the wrong answer as incorrect | 100% | 90% | +0.10 | -4.18 | -6.14 to -2.98 | 96% | 87% | 39% |
| judge knows and flags the wrong answer | 100% | 90% | +0.10 | -3.86 | -6.08 to -2.70 | 96% | 86% | 34% |
| domain geo | 100% | 89% | +0.11 | -3.50 | -6.07 to -2.19 | 95% | 85% | 47% |
| domain law | 100% | 96% | +0.03 | -15.50 | -24.00 to -7.33 | 98% | 96% | 54% |
| domain medqa | 100% | 94% | +0.06 | -7.25 | -15.50 to -4.21 | 98% | 92% | 48% |
| domain geo, judge knows | 100% | 88% | +0.12 | -3.24 | -5.85 to -1.97 | 95% | 84% | 43% |
| domain law, judge knows | 99% | 96% | +0.03 | -14.50 | -20.00 to -5.89 | 99% | 96% | 44% |
| domain medqa, judge knows | 100% | 93% | +0.07 | -6.50 | -14.00 to -3.69 | 97% | 91% | 41% |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 84% on 300 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 93% | 91% to 95% | 300 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 300 | 0 |
| CW-HC | all | 22% | 18% to 26% | 300 | 0 |
| CW-HW | all | 68% | 64% to 71% | 300 | 0 |
| CW-IDK | all | 86% | 82% to 88% | 300 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 300 | 0 |
| HW-IDK | all | 98% | 97% to 99% | 300 | 0 |
| CC-HC | judge knows | 95% | 93% to 97% | 253 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 253 | 0 |
| CW-HC | judge knows | 15% | 11% to 18% | 253 | 0 |
| CW-HW | judge knows | 66% | 62% to 70% | 253 | 0 |
| CW-IDK | judge knows | 84% | 80% to 87% | 253 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 253 | 0 |
| HW-IDK | judge knows | 98% | 97% to 99% | 253 | 0 |
| CC-HC | judge does not know | 84% | 77% to 90% | 47 | 0 |
| CC-IDK | judge does not know | 99% | 97% to 100% | 47 | 0 |
| CW-HC | judge does not know | 63% | 51% to 74% | 47 | 0 |
| CW-HW | judge does not know | 76% | 66% to 84% | 47 | 0 |
| CW-IDK | judge does not know | 95% | 88% to 99% | 47 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 47 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 47 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 94% | 92% to 96% | 267 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 267 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 16% | 13% to 19% | 267 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 66% | 62% to 70% | 267 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 80% to 87% | 267 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 267 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 98% | 97% to 99% | 267 | 0 |
| CC-HC | judge knows and flags the wrong answer | 95% | 93% to 97% | 239 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 239 | 0 |
| CW-HC | judge knows and flags the wrong answer | 12% | 9% to 15% | 239 | 0 |
| CW-HW | judge knows and flags the wrong answer | 65% | 61% to 70% | 239 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 83% | 79% to 86% | 239 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 239 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 98% | 96% to 99% | 239 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 15% | 10% to 21% | 100 | 0 |
| CW-IDK | domain geo | 84% | 77% to 89% | 100 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain law | 32% | 26% to 40% | 100 | 0 |
| CW-IDK | domain law | 89% | 84% to 93% | 100 | 0 |
| CC-IDK | domain medqa | 100% | 98% to 100% | 100 | 0 |
| CW-HC | domain medqa | 19% | 12% to 26% | 100 | 0 |
| CW-IDK | domain medqa | 84% | 78% to 90% | 100 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 91 | 0 |
| CW-HC | domain geo, judge knows | 10% | 5% to 15% | 91 | 0 |
| CW-IDK | domain geo, judge knows | 82% | 75% to 88% | 91 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 77 | 0 |
| CW-HC | domain law, judge knows | 26% | 19% to 34% | 77 | 0 |
| CW-IDK | domain law, judge knows | 88% | 82% to 93% | 77 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 85 | 0 |
| CW-HC | domain medqa, judge knows | 9% | 5% to 15% | 85 | 0 |
| CW-IDK | domain medqa, judge knows | 82% | 76% to 88% | 85 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 86% | +0.14 | -2.48 | -3.40 to -1.85 | 68% | 58% | 22% |
| judge knows | 100% | 84% | +0.16 | -2.09 | -2.89 to -1.53 | 66% | 56% | 15% |
| judge does not know | 99% | 95% | +0.04 | -10.50 | -22.50 to -3.60 | 76% | 72% | 63% |
| judge flags the wrong answer as incorrect | 100% | 84% | +0.16 | -2.09 | -2.91 to -1.54 | 66% | 55% | 16% |
| judge knows and flags the wrong answer | 100% | 83% | +0.17 | -1.91 | -2.68 to -1.39 | 65% | 54% | 12% |
| domain geo | 100% | 84% | +0.17 | -2.03 | -3.55 to -1.22 | 72% | 60% | 15% |
| domain law | 100% | 89% | +0.11 | -3.55 | -6.14 to -2.23 | 66% | 59% | 32% |
| domain medqa | 100% | 84% | +0.16 | -2.19 | -4.00 to -1.30 | 65% | 55% | 19% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.76 | -3.14 to -1.02 | 69% | 57% | 10% |
| domain law, judge knows | 100% | 88% | +0.12 | -3.05 | -5.42 to -1.85 | 67% | 59% | 26% |
| domain medqa, judge knows | 100% | 82% | +0.18 | -1.83 | -3.25 to -1.07 | 63% | 52% | 9% |

## openrouter/openai/gpt-5.6-terra: own closed-book accuracy 83% on 60 items

### prompt variant default (picks the first position in 54% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 60 | 0 |
| CW-HC | all | 11% | 4% to 18% | 60 | 0 |
| CW-IDK | all | 72% | 63% to 82% | 60 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 50 | 0 |
| CW-HC | judge knows | 3% | 0% to 7% | 50 | 0 |
| CW-IDK | judge knows | 68% | 57% to 78% | 50 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 10 | 0 |
| CW-HC | judge does not know | 50% | 20% to 80% | 10 | 0 |
| CW-IDK | judge does not know | 95% | 85% to 100% | 10 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 54 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 5% | 1% to 10% | 54 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 69% | 59% to 80% | 54 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 48 | 0 |
| CW-HC | judge knows and flags the wrong answer | 2% | 0% to 5% | 48 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 67% | 55% to 77% | 48 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 20 | 0 |
| CW-HC | domain geo | 10% | 0% to 25% | 20 | 0 |
| CW-IDK | domain geo | 65% | 45% to 82% | 20 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 20 | 0 |
| CW-HC | domain law | 12% | 2% to 25% | 20 | 0 |
| CW-IDK | domain law | 88% | 75% to 98% | 20 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 20 | 0 |
| CW-HC | domain medqa | 10% | 0% to 22% | 20 | 0 |
| CW-IDK | domain medqa | 65% | 50% to 80% | 20 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 18 | 0 |
| CW-HC | domain geo, judge knows | 0% | 0% to 0% | 18 | 0 |
| CW-IDK | domain geo, judge knows | 61% | 42% to 81% | 18 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 15 | 0 |
| CW-HC | domain law, judge knows | 7% | 0% to 17% | 15 | 0 |
| CW-IDK | domain law, judge knows | 87% | 70% to 100% | 15 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 17 | 0 |
| CW-HC | domain medqa, judge knows | 3% | 0% to 9% | 17 | 0 |
| CW-IDK | domain medqa, judge knows | 59% | 41% to 76% | 17 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 72% | +0.28 | -0.82 | -1.73 to -0.36 | - | - | - |
| judge knows | 100% | 68% | +0.32 | -0.56 | -1.27 to -0.16 | - | - | - |
| judge does not know | 100% | 95% | +0.05 | -9.00 | -9.00 to -2.33 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 69% | +0.31 | -0.64 | -1.35 to -0.23 | - | - | - |
| judge knows and flags the wrong answer | 100% | 67% | +0.33 | -0.50 | -1.18 to -0.12 | - | - | - |
| domain geo | 100% | 65% | +0.35 | -0.43 | -1.86 to +0.09 | - | - | - |
| domain law | 100% | 88% | +0.12 | -3.00 | -19.00 to -1.00 | - | - | - |
| domain medqa | 100% | 65% | +0.35 | -0.43 | -1.50 to +0.00 | - | - | - |
| domain geo, judge knows | 100% | 61% | +0.39 | -0.29 | -1.57 to +0.14 | - | - | - |
| domain law, judge knows | 100% | 87% | +0.13 | -2.75 | -14.00 to -0.67 | - | - | - |
| domain medqa, judge knows | 100% | 59% | +0.41 | -0.21 | -1.12 to +0.15 | - | - | - |
