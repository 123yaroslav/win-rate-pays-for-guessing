items 30 (geo, law, medqa), bootstrap draws 300

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 94.4% | 86.1% to 100.0% | 18 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 97.6% | 92.9% to 100.0% | 21 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 93.8% | 87.5% to 100.0% | 24 | 0.0000 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 94.8% | 87.9% to 100.0% | 29 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 98.3% | 95.0% to 100.0% | 30 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 93.3% | 86.7% to 98.3% | 30 | 0.0000 | yes |

## Two-step account (S1d)

Cells 9, mean absolute error 0.383, Spearman 0.45. Mean predicted 75.1%, mean observed 36.7%.

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 63% on 30 items

### prompt variant default (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 80% | 72% to 88% | 30 | 3 |
| CC-IDK | all | 98% | 95% to 100% | 30 | 0 |
| CW-HC | all | 33% | 20% to 47% | 30 | 2 |
| CW-HW | all | 59% | 47% to 71% | 29 | 7 |
| CW-IDK | all | 95% | 88% to 100% | 29 | 3 |
| HC-IDK | all | 98% | 95% to 100% | 30 | 0 |
| HW-IDK | all | 95% | 90% to 100% | 30 | 2 |
| CC-HC | judge knows | 87% | 76% to 97% | 19 | 3 |
| CC-IDK | judge knows | 100% | 100% to 100% | 19 | 0 |
| CW-HC | judge knows | 24% | 11% to 39% | 19 | 2 |
| CW-HW | judge knows | 53% | 39% to 69% | 18 | 7 |
| CW-IDK | judge knows | 94% | 86% to 100% | 18 | 3 |
| HC-IDK | judge knows | 100% | 100% to 100% | 19 | 0 |
| HW-IDK | judge knows | 95% | 87% to 100% | 19 | 2 |
| CC-HC | judge does not know | 68% | 55% to 82% | 11 | 3 |
| CC-IDK | judge does not know | 95% | 82% to 100% | 11 | 0 |
| CW-HC | judge does not know | 50% | 27% to 68% | 11 | 2 |
| CW-HW | judge does not know | 68% | 55% to 82% | 11 | 7 |
| CW-IDK | judge does not know | 95% | 86% to 100% | 11 | 3 |
| HC-IDK | judge does not know | 95% | 86% to 100% | 11 | 0 |
| HW-IDK | judge does not know | 95% | 86% to 100% | 11 | 2 |
| CC-IDK | domain geo | 100% | 100% to 100% | 8 | 0 |
| CW-HC | domain geo | 31% | 6% to 62% | 8 | 2 |
| CW-IDK | domain geo | 86% | 71% to 100% | 7 | 3 |
| CC-IDK | domain law | 100% | 100% to 100% | 8 | 0 |
| CW-HC | domain law | 31% | 6% to 56% | 8 | 2 |
| CW-IDK | domain law | 100% | 100% to 100% | 8 | 3 |
| CC-IDK | domain medqa | 96% | 89% to 100% | 14 | 0 |
| CW-HC | domain medqa | 36% | 21% to 54% | 14 | 2 |
| CW-IDK | domain medqa | 96% | 89% to 100% | 14 | 3 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 7 | 0 |
| CW-HC | domain geo, judge knows | 21% | 0% to 50% | 7 | 2 |
| CW-IDK | domain geo, judge knows | 92% | 75% to 100% | 6 | 3 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-HC | domain law, judge knows | 33% | 0% to 50% | 3 | 2 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 3 | 3 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 9 | 0 |
| CW-HC | domain medqa, judge knows | 22% | 6% to 39% | 9 | 2 |
| CW-IDK | domain medqa, judge knows | 94% | 83% to 100% | 9 | 3 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 95% | +0.03 | -13.00 | -13.50 to -3.67 | 61% | 59% | 36% |
| judge knows | 100% | 94% | +0.06 | -8.00 | -17.00 to -2.60 | 56% | 53% | 26% |
| judge does not know | 95% | 95% | +0.00 | undefined | -10.00 to -4.00 | 68% | 68% | 50% |
| domain geo | 100% | 86% | +0.14 | -2.50 | -6.00 to -0.75 | 57% | 49% | 36% |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | 62% | 62% | 31% |
| domain medqa | 96% | 96% | +0.00 | undefined | -13.00 to -3.33 | 62% | 62% | 38% |
| domain geo, judge knows | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | 58% | 53% | 25% |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 33% | 33% | 33% |
| domain medqa, judge knows | 100% | 94% | +0.06 | -8.00 | -8.00 to -2.00 | 62% | 59% | 25% |

### prompt variant accuracy (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 81% | 64% to 92% | 18 | 0 |
| CW-IDK | all | 50% | 31% to 67% | 18 | 4 |
| CC-IDK | judge knows | 90% | 75% to 100% | 10 | 0 |
| CW-IDK | judge knows | 45% | 20% to 70% | 10 | 4 |
| CC-IDK | judge does not know | 69% | 44% to 94% | 8 | 0 |
| CW-IDK | judge does not know | 56% | 31% to 81% | 8 | 4 |
| CC-IDK | domain geo | 67% | 33% to 92% | 6 | 0 |
| CW-IDK | domain geo | 50% | 17% to 83% | 6 | 4 |
| CC-IDK | domain law | 83% | 67% to 100% | 6 | 0 |
| CW-IDK | domain law | 33% | 8% to 67% | 6 | 4 |
| CC-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 67% | 33% to 92% | 6 | 4 |
| CC-IDK | domain geo, judge knows | 80% | 60% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 40% | 10% to 80% | 5 | 4 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-IDK | domain law, judge knows | 50% | 0% to 100% | 2 | 4 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 50% | 0% to 100% | 3 | 4 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 81% | 50% | +0.31 | +0.00 | -2.00 to +0.42 | - | - | - |
| judge knows | 90% | 45% | +0.45 | +0.11 | -1.00 to +0.46 | - | - | - |
| judge does not know | 69% | 56% | +0.12 | -0.50 | -3.00 to +0.71 | - | - | - |
| domain geo | 67% | 50% | +0.17 | +0.00 | -2.00 to +1.00 | - | - | - |
| domain law | 83% | 33% | +0.50 | +0.33 | -1.00 to +0.67 | - | - | - |
| domain medqa | 92% | 67% | +0.25 | -0.67 | -4.00 to +0.29 | - | - | - |
| domain geo, judge knows | 80% | 40% | +0.40 | +0.25 | -1.00 to +0.67 | - | - | - |
| domain law, judge knows | 100% | 50% | +0.50 | +0.00 | +0.00 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 50% | +0.50 | +0.00 | -2.00 to +0.50 | - | - | - |

### prompt variant cot (picks the first position in 42% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 88% | 75% to 100% | 16 | 6 |
| CW-IDK | all | 36% | 14% to 57% | 14 | 11 |
| CC-IDK | judge knows | 100% | 100% to 100% | 10 | 6 |
| CW-IDK | judge knows | 28% | 0% to 56% | 9 | 11 |
| CC-IDK | judge does not know | 67% | 42% to 92% | 6 | 6 |
| CW-IDK | judge does not know | 50% | 10% to 90% | 5 | 11 |
| CC-IDK | domain geo | 83% | 50% to 100% | 6 | 6 |
| CW-IDK | domain geo | 33% | 0% to 83% | 6 | 11 |
| CC-IDK | domain law | 83% | 58% to 100% | 6 | 6 |
| CW-IDK | domain law | 50% | 10% to 90% | 5 | 11 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 4 | 6 |
| CW-IDK | domain medqa | 17% | 0% to 50% | 3 | 11 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 6 |
| CW-IDK | domain geo, judge knows | 40% | 0% to 80% | 5 | 11 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 2 | 6 |
| CW-IDK | domain law, judge knows | 0% | 0% to 0% | 2 | 11 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 6 |
| CW-IDK | domain medqa, judge knows | 25% | 0% to 50% | 2 | 11 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 88% | 38% | +0.50 | +0.23 | -0.38 to +0.54 | - | - | - |
| judge knows | 100% | 28% | +0.72 | +0.31 | -0.29 to +0.50 | - | - | - |
| judge does not know | 62% | 62% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo | 83% | 33% | +0.50 | +0.33 | -1.00 to +1.00 | - | - | - |
| domain law | 90% | 50% | +0.40 | +0.00 | -1.50 to +0.50 | - | - | - |
| domain medqa | 100% | 25% | +0.75 | +0.33 | +0.00 to +0.50 | - | - | - |
| domain geo, judge knows | 100% | 40% | +0.60 | +0.17 | -1.50 to +0.50 | - | - | - |
| domain law, judge knows | 100% | 0% | +1.00 | +0.50 | +0.50 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 25% | +0.75 | +0.33 | +0.00 to +0.50 | - | - | - |

### prompt variant data (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 18 | 0 |
| CW-IDK | all | 92% | 83% to 100% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 10 | 0 |
| CW-IDK | judge knows | 90% | 75% to 100% | 10 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 8 | 0 |
| CW-IDK | judge does not know | 94% | 81% to 100% | 8 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 90% | 70% to 100% | 5 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 2 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 83% | 50% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 92% | +0.08 | -5.00 | -17.00 to -2.00 | - | - | - |
| judge knows | 100% | 90% | +0.10 | -4.00 | -9.00 to -1.00 | - | - | - |
| judge does not know | 100% | 94% | +0.06 | -7.00 | -7.00 to -1.00 | - | - | - |
| domain geo | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain law | 100% | 92% | +0.08 | -5.00 | -5.00 to -0.50 | - | - | - |
| domain medqa | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain geo, judge knows | 100% | 90% | +0.10 | -4.00 | -4.00 to -0.67 | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | - | - | - |

### prompt variant selfcheck (picks the first position in 38% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 86% | 75% to 94% | 18 | 0 |
| CW-IDK | all | 78% | 64% to 92% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 10 | 0 |
| CW-IDK | judge knows | 80% | 65% to 95% | 10 | 0 |
| CC-IDK | judge does not know | 69% | 50% to 88% | 8 | 0 |
| CW-IDK | judge does not know | 75% | 50% to 100% | 8 | 0 |
| CC-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain geo | 67% | 33% to 92% | 6 | 0 |
| CC-IDK | domain law | 83% | 67% to 100% | 6 | 0 |
| CW-IDK | domain law | 83% | 58% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 83% | 67% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 80% | 60% to 100% | 5 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-IDK | domain law, judge knows | 75% | 50% to 100% | 2 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 83% | 50% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 86% | 78% | +0.08 | -3.33 | -13.00 to -0.62 | - | - | - |
| judge knows | 100% | 80% | +0.20 | -1.50 | -9.00 to -0.43 | - | - | - |
| judge does not know | 69% | 75% | -0.06 | undefined | -4.00 to +0.67 | - | - | - |
| domain geo | 92% | 67% | +0.25 | -0.67 | -5.00 to +0.25 | - | - | - |
| domain law | 83% | 83% | +0.00 | undefined | -5.00 to -0.50 | - | - | - |
| domain medqa | 83% | 83% | +0.00 | undefined | -5.00 to -0.67 | - | - | - |
| domain geo, judge knows | 100% | 80% | +0.20 | -1.50 | -4.00 to -0.25 | - | - | - |
| domain law, judge knows | 100% | 75% | +0.25 | -1.00 | -1.00 to +0.00 | - | - | - |
| domain medqa, judge knows | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | - | - | - |

### prompt variant stakes (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 92% | 81% to 100% | 18 | 0 |
| CW-IDK | all | 72% | 58% to 86% | 18 | 0 |
| CC-IDK | judge knows | 90% | 70% to 100% | 10 | 0 |
| CW-IDK | judge knows | 60% | 40% to 75% | 10 | 0 |
| CC-IDK | judge does not know | 94% | 81% to 100% | 8 | 0 |
| CW-IDK | judge does not know | 88% | 69% to 100% | 8 | 0 |
| CC-IDK | domain geo | 83% | 50% to 100% | 6 | 0 |
| CW-IDK | domain geo | 67% | 50% to 83% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 75% | 42% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 75% | 58% to 92% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 80% | 40% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 60% | 50% to 80% | 5 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-IDK | domain law, judge knows | 50% | 0% to 100% | 2 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 67% | 50% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 92% | 72% | +0.19 | -1.14 | -9.00 to -0.25 | - | - | - |
| judge knows | 90% | 60% | +0.30 | -0.33 | -5.00 to +0.17 | - | - | - |
| judge does not know | 94% | 88% | +0.06 | -6.00 | -7.00 to -1.33 | - | - | - |
| domain geo | 83% | 67% | +0.17 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain law | 100% | 75% | +0.25 | -1.00 | -5.00 to +0.14 | - | - | - |
| domain medqa | 92% | 75% | +0.17 | -1.50 | -5.00 to -0.25 | - | - | - |
| domain geo, judge knows | 80% | 60% | +0.20 | -0.50 | -0.50 to +0.00 | - | - | - |
| domain law, judge knows | 100% | 50% | +0.50 | +0.00 | +0.00 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 67% | +0.33 | -0.50 | -2.00 to +0.00 | - | - | - |

### prompt variant think (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 83% | 67% to 94% | 18 | 0 |
| CW-IDK | all | 17% | 0% to 33% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 10 | 0 |
| CW-IDK | judge knows | 10% | 0% to 30% | 10 | 0 |
| CC-IDK | judge does not know | 62% | 31% to 94% | 8 | 0 |
| CW-IDK | judge does not know | 25% | 0% to 62% | 8 | 0 |
| CC-IDK | domain geo | 83% | 50% to 100% | 6 | 0 |
| CW-IDK | domain geo | 17% | 0% to 50% | 6 | 0 |
| CC-IDK | domain law | 67% | 33% to 92% | 6 | 0 |
| CW-IDK | domain law | 33% | 0% to 67% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 0% | 0% to 0% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 20% | 0% to 60% | 5 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-IDK | domain law, judge knows | 0% | 0% to 0% | 2 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 0% | 0% to 0% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 83% | 17% | +0.67 | +0.50 | +0.32 to +0.67 | - | - | - |
| judge knows | 100% | 10% | +0.90 | +0.44 | +0.29 to +0.50 | - | - | - |
| judge does not know | 62% | 25% | +0.38 | +0.67 | +0.00 to +2.00 | - | - | - |
| domain geo | 83% | 17% | +0.67 | +0.50 | +0.00 to +1.00 | - | - | - |
| domain law | 67% | 33% | +0.33 | +0.50 | +0.00 to +1.00 | - | - | - |
| domain medqa | 100% | 0% | +1.00 | +0.50 | +0.50 to +0.50 | - | - | - |
| domain geo, judge knows | 100% | 20% | +0.80 | +0.37 | -0.25 to +0.50 | - | - | - |
| domain law, judge knows | 100% | 0% | +1.00 | +0.50 | +0.50 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 0% | +1.00 | +0.50 | +0.50 to +0.50 | - | - | - |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 70% on 30 items

### prompt variant default (picks the first position in 47% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 98% | 95% to 100% | 30 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 30 | 0 |
| CW-HC | all | 57% | 40% to 73% | 30 | 0 |
| CW-HW | all | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | all | 98% | 95% to 100% | 30 | 0 |
| HC-IDK | all | 95% | 90% to 100% | 30 | 0 |
| HW-IDK | all | 90% | 82% to 97% | 30 | 0 |
| CC-HC | judge knows | 98% | 93% to 100% | 21 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 21 | 0 |
| CW-HC | judge knows | 45% | 26% to 62% | 21 | 0 |
| CW-HW | judge knows | 100% | 100% to 100% | 21 | 0 |
| CW-IDK | judge knows | 98% | 93% to 100% | 21 | 0 |
| HC-IDK | judge knows | 95% | 90% to 100% | 21 | 0 |
| HW-IDK | judge knows | 90% | 81% to 98% | 21 | 0 |
| CC-HC | judge does not know | 100% | 100% to 100% | 9 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 9 | 0 |
| CW-HC | judge does not know | 83% | 67% to 100% | 9 | 0 |
| CW-HW | judge does not know | 100% | 100% to 100% | 9 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 9 | 0 |
| HC-IDK | judge does not know | 94% | 83% to 100% | 9 | 0 |
| HW-IDK | judge does not know | 89% | 72% to 100% | 9 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 8 | 0 |
| CW-HC | domain geo | 56% | 31% to 81% | 8 | 0 |
| CW-IDK | domain geo | 94% | 81% to 100% | 8 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 8 | 0 |
| CW-HC | domain law | 50% | 19% to 75% | 8 | 0 |
| CW-IDK | domain law | 100% | 100% to 100% | 8 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 14 | 0 |
| CW-HC | domain medqa | 61% | 36% to 82% | 14 | 0 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 14 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 6 | 0 |
| CW-HC | domain geo, judge knows | 50% | 25% to 83% | 6 | 0 |
| CW-IDK | domain geo, judge knows | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 6 | 0 |
| CW-HC | domain law, judge knows | 42% | 8% to 75% | 6 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 9 | 0 |
| CW-HC | domain medqa, judge knows | 44% | 17% to 72% | 9 | 0 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 9 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 98% | +0.02 | undefined | -14.00 to -6.50 | 100% | 98% | 57% |
| judge knows | 100% | 98% | +0.02 | -20.00 | -20.00 to -4.25 | 100% | 98% | 45% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 83% |
| domain geo | 100% | 94% | +0.06 | -7.00 | -7.00 to -1.67 | 100% | 94% | 56% |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 50% |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 61% |
| domain geo, judge knows | 100% | 92% | +0.08 | -5.00 | -5.00 to -0.50 | 100% | 92% | 50% |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 42% |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 44% |

### prompt variant accuracy (picks the first position in 47% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 97% | 92% to 100% | 18 | 0 |
| CW-IDK | all | 92% | 83% to 100% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-IDK | judge knows | 88% | 75% to 100% | 12 | 0 |
| CC-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 88% | 62% to 100% | 4 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 80% | 60% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 92% | +0.06 | -7.50 | -17.00 to -2.00 | - | - | - |
| judge knows | 100% | 88% | +0.12 | -3.00 | -11.00 to -1.00 | - | - | - |
| judge does not know | 92% | 100% | -0.08 | undefined | +nan to +nan | - | - | - |
| domain geo | 92% | 92% | +0.00 | undefined | -5.00 to -1.00 | - | - | - |
| domain law | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.50 | - | - | - |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo, judge knows | 100% | 88% | +0.12 | -3.00 | -3.00 to -0.33 | - | - | - |
| domain law, judge knows | 100% | 80% | +0.20 | -1.50 | -4.00 to -0.25 | - | - | - |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |

### prompt variant cot (picks the first position in 58% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 97% | 92% to 100% | 18 | 0 |
| CW-IDK | all | 81% | 64% to 92% | 18 | 0 |
| CC-IDK | judge knows | 96% | 88% to 100% | 12 | 0 |
| CW-IDK | judge knows | 71% | 50% to 88% | 12 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain geo | 58% | 33% to 92% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 88% | 62% to 100% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 38% | 12% to 50% | 4 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 90% | 70% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 83% | 50% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 81% | +0.17 | -1.83 | -8.00 to -0.60 | - | - | - |
| judge knows | 96% | 71% | +0.25 | -0.83 | -3.00 to -0.11 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo | 92% | 58% | +0.33 | -0.25 | -2.00 to +0.50 | - | - | - |
| domain law | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain medqa | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain geo, judge knows | 88% | 38% | +0.50 | +0.25 | +0.00 to +0.75 | - | - | - |
| domain law, judge knows | 100% | 90% | +0.10 | -4.00 | -4.00 to -0.67 | - | - | - |
| domain medqa, judge knows | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | - | - | - |

### prompt variant data (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 18 | 0 |
| CW-IDK | all | 100% | 100% to 100% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-IDK | judge knows | 100% | 100% to 100% | 12 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |

### prompt variant selfcheck (picks the first position in 52% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 97% | 92% to 100% | 18 | 0 |
| CW-IDK | all | 84% | 75% to 94% | 16 | 5 |
| CC-IDK | judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-IDK | judge knows | 80% | 65% to 95% | 10 | 5 |
| CC-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | judge does not know | 92% | 75% to 100% | 6 | 5 |
| CC-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain geo | 83% | 67% to 100% | 6 | 5 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 75% | 50% to 100% | 4 | 5 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 92% | 75% to 100% | 6 | 5 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 75% | 50% to 100% | 4 | 5 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 83% | 50% to 100% | 3 | 5 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 83% | 50% to 100% | 3 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 84% | +0.12 | -2.75 | -13.00 to -0.78 | - | - | - |
| judge knows | 100% | 80% | +0.20 | -1.50 | -9.00 to -0.43 | - | - | - |
| judge does not know | 92% | 92% | +0.00 | undefined | -5.00 to -0.50 | - | - | - |
| domain geo | 92% | 83% | +0.08 | -4.00 | -5.00 to -0.50 | - | - | - |
| domain law | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain medqa | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain geo, judge knows | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain law, judge knows | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | - | - | - |
| domain medqa, judge knows | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | - | - | - |

### prompt variant stakes (picks the first position in 36% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 86% to 100% | 18 | 0 |
| CW-IDK | all | 78% | 67% to 92% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-IDK | judge knows | 71% | 58% to 83% | 12 | 0 |
| CC-IDK | judge does not know | 83% | 67% to 100% | 6 | 0 |
| CW-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain geo | 58% | 50% to 75% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 50% | 50% to 50% | 4 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 80% | 60% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 83% | 50% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 94% | 78% | +0.17 | -1.67 | -8.00 to -0.50 | - | - | - |
| judge knows | 100% | 71% | +0.29 | -0.71 | -3.00 to -0.20 | - | - | - |
| judge does not know | 83% | 92% | -0.08 | undefined | +nan to +nan | - | - | - |
| domain geo | 92% | 58% | +0.33 | -0.25 | -1.50 to +0.00 | - | - | - |
| domain law | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.50 | - | - | - |
| domain medqa | 92% | 92% | +0.00 | undefined | -5.00 to -0.50 | - | - | - |
| domain geo, judge knows | 100% | 50% | +0.50 | +0.00 | +0.00 to +0.00 | - | - | - |
| domain law, judge knows | 100% | 80% | +0.20 | -1.50 | -4.00 to -0.25 | - | - | - |
| domain medqa, judge knows | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | - | - | - |

### prompt variant think (picks the first position in 44% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 97% | 89% to 100% | 18 | 0 |
| CW-IDK | all | 92% | 83% to 100% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-IDK | judge knows | 92% | 79% to 100% | 12 | 0 |
| CC-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain geo | 75% | 58% to 92% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 92% | +0.06 | -7.50 | -17.00 to -2.20 | - | - | - |
| judge knows | 100% | 92% | +0.08 | -5.00 | -11.00 to -1.40 | - | - | - |
| judge does not know | 92% | 92% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo | 92% | 75% | +0.17 | -1.50 | -5.00 to -0.20 | - | - | - |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo, judge knows | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 80% on 30 items

### prompt variant default (picks the first position in 55% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 97% | 92% to 100% | 30 | 0 |
| CC-IDK | all | 98% | 95% to 100% | 30 | 0 |
| CW-HC | all | 18% | 8% to 28% | 30 | 0 |
| CW-HW | all | 72% | 58% to 83% | 30 | 0 |
| CW-IDK | all | 93% | 87% to 98% | 30 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 30 | 0 |
| HW-IDK | all | 98% | 95% to 100% | 30 | 0 |
| CC-HC | judge knows | 100% | 100% to 100% | 24 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 24 | 0 |
| CW-HC | judge knows | 10% | 4% to 19% | 24 | 0 |
| CW-HW | judge knows | 71% | 54% to 85% | 24 | 0 |
| CW-IDK | judge knows | 94% | 88% to 100% | 24 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 24 | 0 |
| HW-IDK | judge knows | 98% | 94% to 100% | 24 | 0 |
| CC-HC | judge does not know | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| CW-HC | judge does not know | 50% | 17% to 83% | 6 | 0 |
| CW-HW | judge does not know | 75% | 58% to 92% | 6 | 0 |
| CW-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 8 | 0 |
| CW-HC | domain geo | 19% | 6% to 31% | 8 | 0 |
| CW-IDK | domain geo | 100% | 100% to 100% | 8 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 8 | 0 |
| CW-HC | domain law | 25% | 6% to 50% | 8 | 0 |
| CW-IDK | domain law | 94% | 81% to 100% | 8 | 0 |
| CC-IDK | domain medqa | 96% | 89% to 100% | 14 | 0 |
| CW-HC | domain medqa | 14% | 0% to 29% | 14 | 0 |
| CW-IDK | domain medqa | 89% | 79% to 96% | 14 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 7 | 0 |
| CW-HC | domain geo, judge knows | 14% | 0% to 29% | 7 | 0 |
| CW-IDK | domain geo, judge knows | 100% | 100% to 100% | 7 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 6 | 0 |
| CW-HC | domain law, judge knows | 17% | 0% to 33% | 6 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 11 | 0 |
| CW-HC | domain medqa, judge knows | 5% | 0% to 14% | 11 | 0 |
| CW-IDK | domain medqa, judge knows | 86% | 77% to 100% | 11 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 93% | +0.05 | -8.67 | -14.00 to -2.75 | 72% | 68% | 18% |
| judge knows | 100% | 94% | +0.06 | -7.00 | -23.00 to -2.43 | 71% | 66% | 10% |
| judge does not know | 92% | 92% | +0.00 | undefined | -5.00 to -1.00 | 75% | 75% | 50% |
| domain geo | 100% | 100% | +0.00 | undefined | +nan to +nan | 81% | 81% | 19% |
| domain law | 100% | 94% | +0.06 | -7.00 | -7.00 to -1.00 | 69% | 64% | 25% |
| domain medqa | 96% | 89% | +0.07 | -5.50 | -13.00 to -1.17 | 68% | 63% | 14% |
| domain geo, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 79% | 79% | 14% |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 75% | 75% | 17% |
| domain medqa, judge knows | 100% | 86% | +0.14 | -2.67 | -10.00 to -0.83 | 64% | 55% | 5% |

### prompt variant accuracy (picks the first position in 64% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 89% | 72% to 100% | 18 | 0 |
| CW-IDK | all | 44% | 31% to 58% | 18 | 0 |
| CC-IDK | judge knows | 93% | 71% to 100% | 14 | 0 |
| CW-IDK | judge knows | 43% | 25% to 61% | 14 | 0 |
| CC-IDK | judge does not know | 75% | 25% to 100% | 4 | 0 |
| CW-IDK | judge does not know | 50% | 12% to 88% | 4 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 50% | 33% to 67% | 6 | 0 |
| CC-IDK | domain law | 83% | 50% to 100% | 6 | 0 |
| CW-IDK | domain law | 42% | 25% to 50% | 6 | 0 |
| CC-IDK | domain medqa | 83% | 50% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 42% | 17% to 75% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 50% | 20% to 80% | 5 | 0 |
| CC-IDK | domain law, judge knows | 80% | 40% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 40% | 20% to 50% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain medqa, judge knows | 38% | 0% to 75% | 4 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 89% | 44% | +0.44 | +0.13 | -0.33 to +0.41 | - | - | - |
| judge knows | 93% | 43% | +0.50 | +0.14 | -0.27 to +0.43 | - | - | - |
| judge does not know | 75% | 50% | +0.25 | +0.00 | -1.00 to +3.00 | - | - | - |
| domain geo | 100% | 50% | +0.50 | +0.00 | -1.00 to +0.25 | - | - | - |
| domain law | 83% | 42% | +0.42 | +0.20 | +0.00 to +1.00 | - | - | - |
| domain medqa | 83% | 42% | +0.42 | +0.20 | -1.00 to +1.00 | - | - | - |
| domain geo, judge knows | 100% | 50% | +0.50 | +0.00 | -1.50 to +0.37 | - | - | - |
| domain law, judge knows | 80% | 40% | +0.40 | +0.25 | +0.00 to +1.50 | - | - | - |
| domain medqa, judge knows | 100% | 38% | +0.62 | +0.20 | -1.00 to +0.50 | - | - | - |

### prompt variant cot (picks the first position in 54% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 18 | 0 |
| CW-IDK | all | 83% | 72% to 94% | 18 | 1 |
| CC-IDK | judge knows | 100% | 100% to 100% | 14 | 0 |
| CW-IDK | judge knows | 89% | 79% to 100% | 14 | 1 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | judge does not know | 62% | 50% to 88% | 4 | 1 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 83% | 67% to 100% | 6 | 1 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 92% | 75% to 100% | 6 | 1 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 75% | 58% to 100% | 6 | 1 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 90% | 70% to 100% | 5 | 1 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 1 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain medqa, judge knows | 75% | 50% to 100% | 4 | 1 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.64 | - | - | - |
| judge knows | 100% | 89% | +0.11 | -3.67 | -13.00 to -1.33 | - | - | - |
| judge does not know | 100% | 62% | +0.38 | -0.33 | -3.00 to +0.00 | - | - | - |
| domain geo | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.50 | - | - | - |
| domain law | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain medqa | 100% | 75% | +0.25 | -1.00 | -5.00 to -0.20 | - | - | - |
| domain geo, judge knows | 100% | 90% | +0.10 | -4.00 | -4.00 to -0.67 | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |

### prompt variant data (picks the first position in 54% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 18 | 0 |
| CW-IDK | all | 92% | 81% to 100% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 14 | 0 |
| CW-IDK | judge knows | 96% | 89% to 100% | 14 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | judge does not know | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 90% | 70% to 100% | 5 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 92% | +0.08 | -5.00 | -17.00 to -2.00 | - | - | - |
| judge knows | 100% | 96% | +0.04 | -13.00 | -13.00 to -3.67 | - | - | - |
| judge does not know | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain geo | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain law | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain medqa | 100% | 92% | +0.08 | -5.00 | -5.00 to -1.00 | - | - | - |
| domain geo, judge knows | 100% | 90% | +0.10 | -4.00 | -4.00 to -0.67 | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |

### prompt variant selfcheck (picks the first position in 60% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 92% | 83% to 100% | 18 | 0 |
| CW-IDK | all | 83% | 72% to 94% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 14 | 0 |
| CW-IDK | judge knows | 82% | 71% to 93% | 14 | 0 |
| CC-IDK | judge does not know | 62% | 50% to 88% | 4 | 0 |
| CW-IDK | judge does not know | 88% | 62% to 100% | 4 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | domain law | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain law | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 83% | 67% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 80% | 60% to 100% | 5 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 80% | 60% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain medqa, judge knows | 88% | 62% to 100% | 4 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 92% | 83% | +0.08 | -4.00 | -14.00 to -1.12 | - | - | - |
| judge knows | 100% | 82% | +0.18 | -1.80 | -13.00 to -0.56 | - | - | - |
| judge does not know | 62% | 88% | -0.25 | undefined | +nan to +nan | - | - | - |
| domain geo | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.20 | - | - | - |
| domain law | 92% | 83% | +0.08 | -4.00 | -5.00 to -0.20 | - | - | - |
| domain medqa | 83% | 83% | +0.00 | undefined | -5.00 to -0.25 | - | - | - |
| domain geo, judge knows | 100% | 80% | +0.20 | -1.50 | -4.00 to -0.25 | - | - | - |
| domain law, judge knows | 100% | 80% | +0.20 | -1.50 | -4.00 to -0.25 | - | - | - |
| domain medqa, judge knows | 100% | 88% | +0.12 | -3.00 | -3.00 to -0.33 | - | - | - |

### prompt variant stakes (picks the first position in 61% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 86% to 100% | 18 | 0 |
| CW-IDK | all | 56% | 36% to 72% | 18 | 0 |
| CC-IDK | judge knows | 96% | 89% to 100% | 14 | 0 |
| CW-IDK | judge knows | 61% | 43% to 79% | 14 | 0 |
| CC-IDK | judge does not know | 88% | 62% to 100% | 4 | 0 |
| CW-IDK | judge does not know | 38% | 0% to 75% | 4 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 50% | 25% to 67% | 6 | 0 |
| CC-IDK | domain law | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain law | 58% | 33% to 83% | 6 | 0 |
| CC-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 58% | 25% to 92% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 50% | 20% to 80% | 5 | 0 |
| CC-IDK | domain law, judge knows | 90% | 70% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 70% | 50% to 90% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain medqa, judge knows | 62% | 12% to 100% | 4 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 94% | 56% | +0.39 | -0.14 | -0.86 to +0.16 | - | - | - |
| judge knows | 96% | 61% | +0.36 | -0.30 | -1.60 to +0.14 | - | - | - |
| judge does not know | 88% | 38% | +0.50 | +0.25 | -1.00 to +0.75 | - | - | - |
| domain geo | 100% | 50% | +0.50 | +0.00 | -1.00 to +0.33 | - | - | - |
| domain law | 92% | 58% | +0.33 | -0.25 | -3.00 to +0.29 | - | - | - |
| domain medqa | 92% | 58% | +0.33 | -0.25 | -5.00 to +0.50 | - | - | - |
| domain geo, judge knows | 100% | 50% | +0.50 | +0.00 | -1.50 to +0.29 | - | - | - |
| domain law, judge knows | 90% | 70% | +0.20 | -1.00 | -4.00 to +0.00 | - | - | - |
| domain medqa, judge knows | 100% | 62% | +0.38 | -0.33 | -3.00 to +0.33 | - | - | - |

### prompt variant think (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 18 | 0 |
| CW-IDK | all | 75% | 61% to 89% | 18 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 14 | 0 |
| CW-IDK | judge knows | 79% | 61% to 93% | 14 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | judge does not know | 62% | 25% to 100% | 4 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain geo | 83% | 67% to 100% | 6 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain law | 83% | 50% to 100% | 6 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 58% | 33% to 83% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain geo, judge knows | 80% | 60% to 100% | 5 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-IDK | domain medqa, judge knows | 50% | 25% to 88% | 4 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 75% | +0.25 | -1.00 | -3.50 to -0.20 | - | - | - |
| judge knows | 100% | 79% | +0.21 | -1.33 | -6.00 to -0.27 | - | - | - |
| judge does not know | 100% | 62% | +0.38 | -0.33 | -3.00 to +0.33 | - | - | - |
| domain geo | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.50 | - | - | - |
| domain law | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | - | - | - |
| domain medqa | 100% | 58% | +0.42 | -0.20 | -2.00 to +0.25 | - | - | - |
| domain geo, judge knows | 100% | 80% | +0.20 | -1.50 | -4.00 to -0.25 | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 50% | +0.50 | +0.00 | -3.00 to +0.43 | - | - | - |
