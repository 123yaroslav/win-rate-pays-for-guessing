items 150 (geo, law, medqa), bootstrap draws 10000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 82.5% | 77.2% to 87.3% | 114 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 94.2% | 90.9% to 97.1% | 121 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.4% | 77.2% to 87.2% | 125 | 0.0000 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 84.3% | 80.0% to 88.3% | 150 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 95.0% | 92.3% to 97.3% | 149 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.3% | 81.0% to 89.3% | 150 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 83.7% | 79.5% to 87.8% | 144 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.9% | 89.0% to 96.2% | 105 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.5% | 78.6% to 88.0% | 133 | 0.0000 | yes |

S1g2: b above 0.5 on group 'judge tells the two answers apart', Holm at 0.05. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 81.3% | 74.6% to 87.3% | 67 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 91.9% | 87.6% to 95.7% | 93 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.0% | 76.6% to 86.9% | 122 | 0.0000 | yes |

## Detection (S1g)

| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |
|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 96.0% | 46.7% | 1 |
| openrouter/mistralai/mistral-small-2603 | 70.7% | 87.3% | 0 |
| openrouter/openai/gpt-5.6-luna | 88.7% | 88.0% | 0 |

## Verify-then-compare, composed from logged verdicts (exploratory)

| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |
|---|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 99.0% | 84.2% | 46.3% | 3.4% | 1.09 | 0.92 to 1.34 |
| openrouter/mistralai/mistral-small-2603 | 100.0% | 95.0% | 87.2% | 29.5% | 0.35 | 0.26 to 0.43 |
| openrouter/openai/gpt-5.6-luna | 100.0% | 85.3% | 88.0% | 11.3% | 0.50 | 0.46 to 0.54 |

## Two-step account (S1d)

Cells 9, mean absolute error 0.295, Spearman 0.48. Mean predicted 67.1%, mean observed 37.6%.

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 76% on 150 items

### prompt variant default (picks the first position in 48% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 83% | 79% to 87% | 150 | 5 |
| CC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| CC-IDK2 | all | 97% | 94% to 99% | 150 | 4 |
| CW-CC | all | 20% | 15% to 25% | 150 | 11 |
| CW-HC | all | 39% | 32% to 45% | 148 | 18 |
| CW-HW | all | 58% | 53% to 64% | 146 | 34 |
| CW-IDK | all | 84% | 80% to 88% | 150 | 5 |
| CW-IDK2 | all | 74% | 70% to 79% | 149 | 4 |
| HC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| HW-IDK | all | 94% | 91% to 96% | 150 | 3 |
| CC-HC | judge knows | 87% | 82% to 91% | 114 | 5 |
| CC-IDK | judge knows | 100% | 99% to 100% | 114 | 0 |
| CC-IDK2 | judge knows | 97% | 95% to 100% | 114 | 4 |
| CW-CC | judge knows | 14% | 10% to 19% | 114 | 11 |
| CW-HC | judge knows | 33% | 26% to 40% | 112 | 18 |
| CW-HW | judge knows | 59% | 52% to 65% | 110 | 34 |
| CW-IDK | judge knows | 82% | 77% to 87% | 114 | 5 |
| CW-IDK2 | judge knows | 71% | 66% to 76% | 113 | 4 |
| HC-IDK | judge knows | 99% | 98% to 100% | 114 | 0 |
| HW-IDK | judge knows | 93% | 90% to 96% | 114 | 3 |
| CC-HC | judge does not know | 72% | 64% to 81% | 36 | 5 |
| CC-IDK | judge does not know | 97% | 93% to 100% | 36 | 0 |
| CC-IDK2 | judge does not know | 94% | 89% to 99% | 36 | 4 |
| CW-CC | judge does not know | 38% | 25% to 50% | 36 | 11 |
| CW-HC | judge does not know | 56% | 43% to 68% | 36 | 18 |
| CW-HW | judge does not know | 57% | 46% to 67% | 36 | 34 |
| CW-IDK | judge does not know | 90% | 83% to 96% | 36 | 5 |
| CW-IDK2 | judge does not know | 85% | 75% to 93% | 36 | 4 |
| HC-IDK | judge does not know | 99% | 96% to 100% | 36 | 0 |
| HW-IDK | judge does not know | 94% | 89% to 99% | 36 | 3 |
| CC-HC | judge tells the two answers apart | 90% | 84% to 94% | 67 | 5 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 67 | 0 |
| CC-IDK2 | judge tells the two answers apart | 99% | 98% to 100% | 67 | 4 |
| CW-CC | judge tells the two answers apart | 10% | 4% to 16% | 67 | 11 |
| CW-HC | judge tells the two answers apart | 22% | 14% to 30% | 66 | 18 |
| CW-HW | judge tells the two answers apart | 54% | 45% to 62% | 65 | 34 |
| CW-IDK | judge tells the two answers apart | 81% | 75% to 87% | 67 | 5 |
| CW-IDK2 | judge tells the two answers apart | 67% | 60% to 73% | 66 | 4 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 67 | 0 |
| HW-IDK | judge tells the two answers apart | 95% | 91% to 98% | 67 | 3 |
| CC-HC | judge flags the wrong answer as incorrect | 83% | 79% to 87% | 144 | 5 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 97% | 95% to 99% | 144 | 4 |
| CW-CC | judge flags the wrong answer as incorrect | 18% | 14% to 23% | 144 | 11 |
| CW-HC | judge flags the wrong answer as incorrect | 36% | 30% to 43% | 142 | 18 |
| CW-HW | judge flags the wrong answer as incorrect | 57% | 52% to 63% | 140 | 34 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 80% to 88% | 144 | 5 |
| CW-IDK2 | judge flags the wrong answer as incorrect | 74% | 70% to 79% | 143 | 4 |
| HC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 91% to 96% | 144 | 3 |
| CC-HC | judge knows and flags the wrong answer | 87% | 82% to 91% | 111 | 5 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 111 | 0 |
| CC-IDK2 | judge knows and flags the wrong answer | 98% | 95% to 100% | 111 | 4 |
| CW-CC | judge knows and flags the wrong answer | 14% | 9% to 19% | 111 | 11 |
| CW-HC | judge knows and flags the wrong answer | 32% | 25% to 39% | 109 | 18 |
| CW-HW | judge knows and flags the wrong answer | 58% | 51% to 65% | 107 | 34 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 77% to 87% | 111 | 5 |
| CW-IDK2 | judge knows and flags the wrong answer | 71% | 66% to 76% | 110 | 4 |
| HC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 111 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 93% | 90% to 96% | 111 | 3 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 40% | 29% to 51% | 49 | 18 |
| CW-IDK | domain geo | 84% | 77% to 91% | 50 | 5 |
| CC-IDK | domain law | 99% | 97% to 100% | 50 | 0 |
| CW-HC | domain law | 43% | 32% to 54% | 50 | 18 |
| CW-IDK | domain law | 85% | 78% to 92% | 50 | 5 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 0 |
| CW-HC | domain medqa | 33% | 22% to 43% | 49 | 18 |
| CW-IDK | domain medqa | 84% | 76% to 91% | 50 | 5 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 42 | 0 |
| CW-HC | domain geo, judge knows | 34% | 23% to 46% | 41 | 18 |
| CW-IDK | domain geo, judge knows | 83% | 75% to 90% | 42 | 5 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 31 | 0 |
| CW-HC | domain law, judge knows | 37% | 23% to 52% | 31 | 18 |
| CW-IDK | domain law, judge knows | 84% | 74% to 92% | 31 | 5 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-HC | domain medqa, judge knows | 29% | 19% to 40% | 40 | 18 |
| CW-IDK | domain medqa, judge knows | 80% | 71% to 89% | 41 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 84% | +0.15 | -2.34 | -3.63 to -1.60 | 59% | 50% | 39% |
| judge knows | 100% | 82% | +0.17 | -1.90 | -3.11 to -1.24 | 59% | 49% | 33% |
| judge does not know | 97% | 90% | +0.07 | -5.80 | -16.00 to -2.40 | 57% | 53% | 56% |
| judge tells the two answers apart | 100% | 81% | +0.19 | -1.68 | -2.94 to -0.97 | 55% | 44% | 22% |
| judge flags the wrong answer as incorrect | 99% | 84% | +0.15 | -2.20 | -3.48 to -1.49 | 58% | 49% | 37% |
| judge knows and flags the wrong answer | 100% | 82% | +0.18 | -1.82 | -2.93 to -1.16 | 59% | 49% | 32% |
| domain geo | 100% | 84% | +0.16 | -2.12 | -4.56 to -1.17 | 64% | 54% | 40% |
| domain law | 99% | 85% | +0.14 | -2.50 | -5.25 to -1.33 | 68% | 58% | 43% |
| domain medqa | 98% | 84% | +0.14 | -2.43 | -6.83 to -1.17 | 42% | 37% | 34% |
| domain geo, judge knows | 100% | 83% | +0.17 | -2.00 | -4.25 to -1.00 | 63% | 53% | 34% |
| domain law, judge knows | 100% | 84% | +0.16 | -2.10 | -5.20 to -0.94 | 69% | 58% | 37% |
| domain medqa, judge knows | 99% | 80% | +0.18 | -1.67 | -4.13 to -0.78 | 46% | 38% | 30% |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 81% on 150 items

### prompt variant default (picks the first position in 44% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 99% to 100% | 150 | 1 |
| CC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| CC-IDK2 | all | 87% | 83% to 91% | 150 | 0 |
| CW-CC | all | 16% | 11% to 22% | 150 | 2 |
| CW-HC | all | 51% | 44% to 58% | 150 | 2 |
| CW-HW | all | 98% | 96% to 99% | 150 | 2 |
| CW-IDK | all | 95% | 92% to 97% | 149 | 7 |
| CW-IDK2 | all | 64% | 58% to 70% | 150 | 5 |
| HC-IDK | all | 94% | 91% to 96% | 149 | 2 |
| HW-IDK | all | 84% | 80% to 88% | 148 | 7 |
| CC-HC | judge knows | 100% | 99% to 100% | 122 | 1 |
| CC-IDK | judge knows | 100% | 100% to 100% | 122 | 0 |
| CC-IDK2 | judge knows | 90% | 85% to 93% | 122 | 0 |
| CW-CC | judge knows | 7% | 4% to 11% | 122 | 2 |
| CW-HC | judge knows | 45% | 37% to 52% | 122 | 2 |
| CW-HW | judge knows | 98% | 95% to 99% | 122 | 2 |
| CW-IDK | judge knows | 94% | 91% to 97% | 121 | 7 |
| CW-IDK2 | judge knows | 61% | 54% to 67% | 122 | 5 |
| HC-IDK | judge knows | 95% | 92% to 98% | 121 | 2 |
| HW-IDK | judge knows | 82% | 78% to 87% | 120 | 7 |
| CC-HC | judge does not know | 100% | 100% to 100% | 28 | 1 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 28 | 0 |
| CC-IDK2 | judge does not know | 75% | 64% to 86% | 28 | 0 |
| CW-CC | judge does not know | 55% | 41% to 70% | 28 | 2 |
| CW-HC | judge does not know | 80% | 68% to 91% | 28 | 2 |
| CW-HW | judge does not know | 98% | 95% to 100% | 28 | 2 |
| CW-IDK | judge does not know | 98% | 95% to 100% | 28 | 7 |
| CW-IDK2 | judge does not know | 80% | 66% to 91% | 28 | 5 |
| HC-IDK | judge does not know | 89% | 82% to 96% | 28 | 2 |
| HW-IDK | judge does not know | 91% | 84% to 98% | 28 | 7 |
| CC-HC | judge tells the two answers apart | 99% | 98% to 100% | 94 | 1 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 94 | 0 |
| CC-IDK2 | judge tells the two answers apart | 88% | 84% to 93% | 94 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 4% to 12% | 94 | 2 |
| CW-HC | judge tells the two answers apart | 35% | 27% to 43% | 94 | 2 |
| CW-HW | judge tells the two answers apart | 96% | 94% to 98% | 94 | 2 |
| CW-IDK | judge tells the two answers apart | 92% | 88% to 96% | 93 | 7 |
| CW-IDK2 | judge tells the two answers apart | 55% | 47% to 62% | 94 | 5 |
| HC-IDK | judge tells the two answers apart | 95% | 92% to 98% | 94 | 2 |
| HW-IDK | judge tells the two answers apart | 80% | 74% to 84% | 93 | 7 |
| CC-HC | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 106 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 106 | 0 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 86% | 82% to 91% | 106 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 12% | 7% to 17% | 106 | 2 |
| CW-HC | judge flags the wrong answer as incorrect | 40% | 33% to 48% | 106 | 2 |
| CW-HW | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 106 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 93% | 89% to 96% | 105 | 7 |
| CW-IDK2 | judge flags the wrong answer as incorrect | 57% | 50% to 64% | 106 | 5 |
| HC-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 96% | 106 | 2 |
| HW-IDK | judge flags the wrong answer as incorrect | 80% | 76% to 85% | 105 | 7 |
| CC-HC | judge knows and flags the wrong answer | 99% | 98% to 100% | 94 | 1 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 94 | 0 |
| CC-IDK2 | judge knows and flags the wrong answer | 88% | 82% to 93% | 94 | 0 |
| CW-CC | judge knows and flags the wrong answer | 7% | 4% to 12% | 94 | 2 |
| CW-HC | judge knows and flags the wrong answer | 37% | 29% to 45% | 94 | 2 |
| CW-HW | judge knows and flags the wrong answer | 97% | 94% to 99% | 94 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 92% | 88% to 96% | 93 | 7 |
| CW-IDK2 | judge knows and flags the wrong answer | 54% | 47% to 62% | 94 | 5 |
| HC-IDK | judge knows and flags the wrong answer | 94% | 91% to 97% | 94 | 2 |
| HW-IDK | judge knows and flags the wrong answer | 80% | 74% to 85% | 93 | 7 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 42% | 31% to 54% | 50 | 2 |
| CW-IDK | domain geo | 92% | 86% to 97% | 50 | 7 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain law | 60% | 47% to 72% | 50 | 2 |
| CW-IDK | domain law | 98% | 95% to 100% | 50 | 7 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain medqa | 52% | 40% to 64% | 50 | 2 |
| CW-IDK | domain medqa | 95% | 91% to 99% | 49 | 7 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-HC | domain geo, judge knows | 39% | 27% to 51% | 46 | 2 |
| CW-IDK | domain geo, judge knows | 91% | 85% to 97% | 46 | 7 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 33 | 0 |
| CW-HC | domain law, judge knows | 50% | 35% to 65% | 33 | 2 |
| CW-IDK | domain law, judge knows | 98% | 95% to 100% | 33 | 7 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 43 | 0 |
| CW-HC | domain medqa, judge knows | 47% | 34% to 59% | 43 | 2 |
| CW-IDK | domain medqa, judge knows | 94% | 89% to 99% | 42 | 7 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 95% | +0.05 | -8.93 | -17.63 to -5.48 | 98% | 93% | 52% |
| judge knows | 100% | 94% | +0.06 | -7.64 | -16.29 to -4.50 | 98% | 92% | 45% |
| judge does not know | 100% | 98% | +0.02 | undefined | -13.00 to -6.00 | 98% | 96% | 80% |
| judge tells the two answers apart | 100% | 92% | +0.08 | -5.20 | -10.63 to -3.04 | 96% | 88% | 35% |
| judge flags the wrong answer as incorrect | 100% | 93% | +0.07 | -6.00 | -12.13 to -3.57 | 97% | 90% | 40% |
| judge knows and flags the wrong answer | 100% | 92% | +0.08 | -5.64 | -12.29 to -3.23 | 97% | 89% | 37% |
| domain geo | 100% | 92% | +0.08 | -5.25 | -15.67 to -2.57 | 97% | 89% | 42% |
| domain law | 100% | 98% | +0.02 | -24.00 | -24.00 to -9.00 | 99% | 97% | 60% |
| domain medqa | 100% | 95% | +0.05 | -8.80 | -23.50 to -3.90 | 97% | 92% | 53% |
| domain geo, judge knows | 100% | 91% | +0.09 | -4.75 | -14.33 to -2.29 | 97% | 88% | 39% |
| domain law, judge knows | 100% | 98% | +0.02 | undefined | -15.50 to -7.25 | 100% | 98% | 50% |
| domain medqa, judge knows | 100% | 94% | +0.06 | -7.40 | -20.00 to -3.67 | 96% | 91% | 48% |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 83% on 150 items

### prompt variant default (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 93% | 90% to 96% | 150 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| CC-IDK2 | all | 98% | 96% to 99% | 150 | 0 |
| CW-CC | all | 15% | 11% to 20% | 150 | 0 |
| CW-HC | all | 22% | 17% to 28% | 150 | 0 |
| CW-HW | all | 69% | 64% to 74% | 150 | 0 |
| CW-IDK | all | 85% | 81% to 89% | 150 | 0 |
| CW-IDK2 | all | 69% | 64% to 74% | 150 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| HW-IDK | all | 98% | 96% to 100% | 150 | 0 |
| CC-HC | judge knows | 95% | 92% to 97% | 125 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 125 | 0 |
| CC-IDK2 | judge knows | 99% | 97% to 100% | 125 | 0 |
| CW-CC | judge knows | 8% | 5% to 12% | 125 | 0 |
| CW-HC | judge knows | 13% | 9% to 18% | 125 | 0 |
| CW-HW | judge knows | 68% | 62% to 73% | 125 | 0 |
| CW-IDK | judge knows | 82% | 77% to 87% | 125 | 0 |
| CW-IDK2 | judge knows | 64% | 59% to 69% | 125 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 125 | 0 |
| HW-IDK | judge knows | 98% | 95% to 100% | 125 | 0 |
| CC-HC | judge does not know | 86% | 76% to 94% | 25 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| CC-IDK2 | judge does not know | 94% | 86% to 100% | 25 | 0 |
| CW-CC | judge does not know | 50% | 32% to 68% | 25 | 0 |
| CW-HC | judge does not know | 68% | 52% to 84% | 25 | 0 |
| CW-HW | judge does not know | 76% | 64% to 86% | 25 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| CW-IDK2 | judge does not know | 94% | 86% to 100% | 25 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| CC-HC | judge tells the two answers apart | 95% | 92% to 98% | 122 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 122 | 0 |
| CC-IDK2 | judge tells the two answers apart | 99% | 98% to 100% | 122 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 4% to 11% | 122 | 0 |
| CW-HC | judge tells the two answers apart | 13% | 9% to 18% | 122 | 0 |
| CW-HW | judge tells the two answers apart | 67% | 61% to 73% | 122 | 0 |
| CW-IDK | judge tells the two answers apart | 82% | 77% to 87% | 122 | 0 |
| CW-IDK2 | judge tells the two answers apart | 64% | 59% to 70% | 122 | 0 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 122 | 0 |
| HW-IDK | judge tells the two answers apart | 98% | 95% to 100% | 122 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 94% | 91% to 97% | 133 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 133 | 0 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 98% | 97% to 100% | 133 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 9% | 5% to 13% | 133 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 15% | 11% to 20% | 133 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 68% | 62% to 73% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 83% | 79% to 88% | 133 | 0 |
| CW-IDK2 | judge flags the wrong answer as incorrect | 66% | 61% to 71% | 133 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 133 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 98% | 95% to 100% | 133 | 0 |
| CC-HC | judge knows and flags the wrong answer | 95% | 92% to 97% | 121 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 121 | 0 |
| CC-IDK2 | judge knows and flags the wrong answer | 99% | 98% to 100% | 121 | 0 |
| CW-CC | judge knows and flags the wrong answer | 7% | 4% to 11% | 121 | 0 |
| CW-HC | judge knows and flags the wrong answer | 11% | 7% to 15% | 121 | 0 |
| CW-HW | judge knows and flags the wrong answer | 67% | 62% to 73% | 121 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 76% to 87% | 121 | 0 |
| CW-IDK2 | judge knows and flags the wrong answer | 63% | 58% to 68% | 121 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 121 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 98% | 95% to 100% | 121 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 14% | 7% to 22% | 50 | 0 |
| CW-IDK | domain geo | 83% | 75% to 91% | 50 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain law | 33% | 23% to 43% | 50 | 0 |
| CW-IDK | domain law | 90% | 84% to 95% | 50 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain medqa | 20% | 10% to 31% | 50 | 0 |
| CW-IDK | domain medqa | 83% | 74% to 91% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-HC | domain geo, judge knows | 9% | 3% to 14% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 82% | 73% to 89% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 38 | 0 |
| CW-HC | domain law, judge knows | 25% | 14% to 36% | 38 | 0 |
| CW-IDK | domain law, judge knows | 87% | 80% to 93% | 38 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 0 |
| CW-HC | domain medqa, judge knows | 7% | 1% to 15% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 79% | 70% to 88% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 85% | +0.15 | -2.41 | -3.69 to -1.63 | 69% | 59% | 22% |
| judge knows | 100% | 82% | +0.18 | -1.84 | -2.91 to -1.19 | 68% | 56% | 13% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 76% | 76% | 68% |
| judge tells the two answers apart | 100% | 82% | +0.18 | -1.77 | -2.81 to -1.14 | 67% | 55% | 13% |
| judge flags the wrong answer as incorrect | 100% | 83% | +0.17 | -2.02 | -3.16 to -1.33 | 68% | 56% | 15% |
| judge knows and flags the wrong answer | 100% | 82% | +0.18 | -1.75 | -2.78 to -1.12 | 67% | 55% | 11% |
| domain geo | 100% | 83% | +0.17 | -1.94 | -4.56 to -0.92 | 72% | 60% | 14% |
| domain law | 100% | 90% | +0.10 | -4.00 | -9.00 to -2.12 | 64% | 58% | 33% |
| domain medqa | 100% | 83% | +0.17 | -1.94 | -4.56 to -0.92 | 71% | 59% | 20% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.71 | -4.11 to -0.84 | 70% | 57% | 9% |
| domain law, judge knows | 100% | 87% | +0.13 | -2.80 | -6.60 to -1.38 | 63% | 55% | 25% |
| domain medqa, judge knows | 100% | 79% | +0.21 | -1.41 | -3.10 to -0.64 | 70% | 55% | 7% |
