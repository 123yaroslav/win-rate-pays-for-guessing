items 300 (geo, law, medqa), bootstrap draws 4000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 82.7% | 79.3% to 86.1% | 237 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.1% | 89.6% to 94.5% | 227 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.8% | 80.4% to 87.2% | 253 | 0.0000 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 84.4% | 81.5% to 87.2% | 298 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 93.1% | 91.1% to 95.0% | 298 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.5% | 82.3% to 88.5% | 300 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 84.0% | 80.8% to 86.9% | 287 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 90.3% | 87.4% to 93.0% | 207 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.7% | 80.3% to 87.1% | 267 | 0.0000 | yes |

S1g2: b above 0.5 on group 'judge tells the two answers apart', Holm at 0.05. Passed by 3 of 3 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 79.9% | 75.5% to 84.2% | 149 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 89.8% | 86.8% to 92.9% | 182 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.2% | 78.2% to 85.7% | 241 | 0.0000 | yes |

## Detection (S1g)

| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |
|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 96.3% | 52.3% | 1 |
| openrouter/mistralai/mistral-small-2603 | 69.7% | 86.7% | 0 |
| openrouter/openai/gpt-5.6-luna | 89.0% | 86.7% | 0 |

## Verify-then-compare, composed from logged verdicts (exploratory)

| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |
|---|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | 98.1% | 84.3% | 51.7% | 3.2% | 0.97 | 0.86 to 1.10 |
| openrouter/mistralai/mistral-small-2603 | 99.8% | 93.1% | 86.6% | 30.4% | 0.35 | 0.28 to 0.41 |
| openrouter/openai/gpt-5.6-luna | 99.8% | 85.5% | 86.7% | 11.0% | 0.52 | 0.49 to 0.55 |

## Instruction variants (Study 4 criterion)

| judge | variant | a, knows | b, knows | share of resamples with b at or above 0.5 | repaired | a, does not know | b, does not know |
|---|---|---|---|---|---|---|---|
| openrouter/anthropic/claude-haiku-5.5 | default | 99% | 83% | 1.000 | no | 94% | 91% |
| openrouter/anthropic/claude-haiku-5.5 | think | 99% | 6% | 0.000 | yes | 70% | 32% |
| openrouter/mistralai/mistral-small-2603 | default | 100% | 92% | 1.000 | no | 100% | 96% |
| openrouter/openai/gpt-5.6-luna | default | 100% | 84% | 1.000 | no | 99% | 95% |
| openrouter/openai/gpt-5.6-luna | think | 100% | 56% | 0.994 | no | 94% | 85% |

## Two-step account (S1d)

Cells 9, mean absolute error 0.303, Spearman 0.63. Mean predicted 66.5%, mean observed 36.2%.

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 80% on 300 items

### prompt variant default (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 81% | 78% to 84% | 299 | 9 |
| CC-IDK | all | 98% | 97% to 99% | 300 | 0 |
| CW-CC | all | 19% | 16% to 23% | 298 | 21 |
| CW-HC | all | 36% | 32% to 41% | 295 | 36 |
| CW-HW | all | 59% | 55% to 63% | 290 | 64 |
| CW-IDK | all | 84% | 82% to 87% | 298 | 11 |
| HC-IDK | all | 100% | 99% to 100% | 300 | 1 |
| HW-IDK | all | 93% | 91% to 95% | 300 | 6 |
| CC-HC | judge knows | 86% | 83% to 89% | 238 | 9 |
| CC-IDK | judge knows | 99% | 98% to 100% | 239 | 0 |
| CW-CC | judge knows | 14% | 11% to 18% | 237 | 21 |
| CW-HC | judge knows | 32% | 27% to 37% | 234 | 36 |
| CW-HW | judge knows | 59% | 55% to 64% | 229 | 64 |
| CW-IDK | judge knows | 83% | 79% to 86% | 237 | 11 |
| HC-IDK | judge knows | 100% | 99% to 100% | 239 | 1 |
| HW-IDK | judge knows | 93% | 91% to 95% | 239 | 6 |
| CC-HC | judge does not know | 65% | 57% to 72% | 61 | 9 |
| CC-IDK | judge does not know | 94% | 90% to 98% | 61 | 0 |
| CW-CC | judge does not know | 39% | 31% to 48% | 61 | 21 |
| CW-HC | judge does not know | 51% | 42% to 60% | 61 | 36 |
| CW-HW | judge does not know | 58% | 51% to 66% | 61 | 64 |
| CW-IDK | judge does not know | 91% | 86% to 95% | 61 | 11 |
| HC-IDK | judge does not know | 99% | 98% to 100% | 61 | 1 |
| HW-IDK | judge does not know | 94% | 90% to 98% | 61 | 6 |
| CC-HC | judge tells the two answers apart | 90% | 87% to 93% | 151 | 9 |
| CC-IDK | judge tells the two answers apart | 100% | 99% to 100% | 151 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 4% to 10% | 150 | 21 |
| CW-HC | judge tells the two answers apart | 20% | 15% to 26% | 148 | 36 |
| CW-HW | judge tells the two answers apart | 56% | 50% to 61% | 144 | 64 |
| CW-IDK | judge tells the two answers apart | 80% | 76% to 84% | 149 | 11 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 151 | 1 |
| HW-IDK | judge tells the two answers apart | 92% | 89% to 95% | 151 | 6 |
| CC-HC | judge flags the wrong answer as incorrect | 81% | 78% to 84% | 288 | 9 |
| CC-IDK | judge flags the wrong answer as incorrect | 98% | 97% to 99% | 289 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 18% | 15% to 21% | 287 | 21 |
| CW-HC | judge flags the wrong answer as incorrect | 34% | 30% to 39% | 284 | 36 |
| CW-HW | judge flags the wrong answer as incorrect | 58% | 54% to 63% | 279 | 64 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 81% to 87% | 287 | 11 |
| HC-IDK | judge flags the wrong answer as incorrect | 99% | 99% to 100% | 289 | 1 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 91% to 95% | 289 | 6 |
| CC-HC | judge knows and flags the wrong answer | 86% | 83% to 89% | 231 | 9 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 232 | 0 |
| CW-CC | judge knows and flags the wrong answer | 13% | 10% to 17% | 230 | 21 |
| CW-HC | judge knows and flags the wrong answer | 31% | 26% to 36% | 227 | 36 |
| CW-HW | judge knows and flags the wrong answer | 59% | 54% to 64% | 222 | 64 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 79% to 86% | 230 | 11 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 232 | 1 |
| HW-IDK | judge knows and flags the wrong answer | 93% | 90% to 95% | 232 | 6 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 37% | 29% to 45% | 98 | 36 |
| CW-IDK | domain geo | 83% | 78% to 87% | 99 | 11 |
| CC-IDK | domain law | 96% | 94% to 99% | 100 | 0 |
| CW-HC | domain law | 36% | 28% to 44% | 99 | 36 |
| CW-IDK | domain law | 85% | 80% to 90% | 100 | 11 |
| CC-IDK | domain medqa | 98% | 96% to 100% | 100 | 0 |
| CW-HC | domain medqa | 36% | 29% to 43% | 98 | 36 |
| CW-IDK | domain medqa | 85% | 80% to 91% | 99 | 11 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 90 | 0 |
| CW-HC | domain geo, judge knows | 34% | 26% to 43% | 88 | 36 |
| CW-IDK | domain geo, judge knows | 82% | 77% to 87% | 89 | 11 |
| CC-IDK | domain law, judge knows | 98% | 95% to 100% | 67 | 0 |
| CW-HC | domain law, judge knows | 31% | 22% to 41% | 66 | 36 |
| CW-IDK | domain law, judge knows | 83% | 76% to 89% | 67 | 11 |
| CC-IDK | domain medqa, judge knows | 99% | 98% to 100% | 82 | 0 |
| CW-HC | domain medqa, judge knows | 31% | 24% to 39% | 80 | 36 |
| CW-IDK | domain medqa, judge knows | 83% | 77% to 90% | 81 | 11 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 84% | +0.14 | -2.50 | -3.47 to -1.85 | 59% | 51% | 36% |
| judge knows | 99% | 83% | +0.16 | -1.99 | -2.76 to -1.46 | 59% | 49% | 33% |
| judge does not know | 94% | 91% | +0.03 | -12.50 | -17.67 to -3.75 | 58% | 56% | 51% |
| judge tells the two answers apart | 100% | 80% | +0.20 | -1.51 | -2.22 to -1.04 | 56% | 44% | 20% |
| judge flags the wrong answer as incorrect | 98% | 84% | +0.14 | -2.38 | -3.29 to -1.77 | 58% | 50% | 34% |
| judge knows and flags the wrong answer | 99% | 82% | +0.17 | -1.94 | -2.70 to -1.41 | 59% | 49% | 31% |
| domain geo | 100% | 83% | +0.17 | -1.91 | -3.12 to -1.25 | 64% | 53% | 38% |
| domain law | 96% | 85% | +0.11 | -3.04 | -6.23 to -1.79 | 69% | 61% | 36% |
| domain medqa | 98% | 85% | +0.13 | -2.80 | -5.79 to -1.64 | 43% | 38% | 35% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.78 | -2.87 to -1.17 | 64% | 52% | 35% |
| domain law, judge knows | 98% | 83% | +0.15 | -2.20 | -4.64 to -1.20 | 69% | 59% | 32% |
| domain medqa, judge knows | 99% | 83% | +0.16 | -2.08 | -3.94 to -1.19 | 45% | 38% | 30% |

### prompt variant think (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 93% | 90% to 95% | 300 | 1 |
| CW-IDK | all | 11% | 8% to 15% | 300 | 0 |
| CC-IDK | judge knows | 99% | 97% to 100% | 239 | 1 |
| CW-IDK | judge knows | 6% | 3% to 9% | 239 | 0 |
| CC-IDK | judge does not know | 70% | 59% to 81% | 61 | 1 |
| CW-IDK | judge does not know | 32% | 22% to 43% | 61 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 98% to 100% | 151 | 1 |
| CW-IDK | judge tells the two answers apart | 2% | 0% to 5% | 151 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 94% | 91% to 96% | 289 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 9% | 6% to 12% | 289 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 232 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 5% | 2% to 8% | 232 | 0 |
| CC-IDK | domain geo | 94% | 90% to 98% | 100 | 1 |
| CW-IDK | domain geo | 9% | 4% to 14% | 100 | 0 |
| CC-IDK | domain law | 88% | 82% to 94% | 100 | 1 |
| CW-IDK | domain law | 16% | 10% to 23% | 100 | 0 |
| CC-IDK | domain medqa | 96% | 91% to 99% | 100 | 1 |
| CW-IDK | domain medqa | 9% | 4% to 15% | 100 | 0 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 90 | 1 |
| CW-IDK | domain geo, judge knows | 6% | 2% to 11% | 90 | 0 |
| CC-IDK | domain law, judge knows | 97% | 93% to 100% | 67 | 1 |
| CW-IDK | domain law, judge knows | 10% | 3% to 16% | 67 | 0 |
| CC-IDK | domain medqa, judge knows | 99% | 98% to 100% | 82 | 1 |
| CW-IDK | domain medqa, judge knows | 3% | 0% to 7% | 82 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 93% | 11% | +0.82 | +0.47 | +0.45 to +0.50 | - | - | - |
| judge knows | 99% | 6% | +0.92 | +0.48 | +0.46 to +0.49 | - | - | - |
| judge does not know | 70% | 32% | +0.39 | +0.47 | +0.27 to +0.65 | - | - | - |
| judge tells the two answers apart | 99% | 2% | +0.97 | +0.49 | +0.48 to +0.50 | - | - | - |
| judge flags the wrong answer as incorrect | 94% | 9% | +0.84 | +0.48 | +0.46 to +0.50 | - | - | - |
| judge knows and flags the wrong answer | 99% | 5% | +0.94 | +0.48 | +0.47 to +0.49 | - | - | - |
| domain geo | 94% | 9% | +0.85 | +0.48 | +0.45 to +0.51 | - | - | - |
| domain law | 88% | 16% | +0.72 | +0.47 | +0.41 to +0.52 | - | - | - |
| domain medqa | 96% | 9% | +0.86 | +0.47 | +0.44 to +0.50 | - | - | - |
| domain geo, judge knows | 99% | 6% | +0.93 | +0.47 | +0.45 to +0.49 | - | - | - |
| domain law, judge knows | 97% | 10% | +0.87 | +0.46 | +0.41 to +0.50 | - | - | - |
| domain medqa, judge knows | 99% | 3% | +0.96 | +0.49 | +0.46 to +0.50 | - | - | - |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 76% on 300 items

### prompt variant default (picks the first position in 46% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 99% | 98% to 100% | 300 | 2 |
| CC-IDK | all | 100% | 100% to 100% | 300 | 0 |
| CW-CC | all | 19% | 15% to 22% | 300 | 3 |
| CW-HC | all | 50% | 45% to 55% | 299 | 5 |
| CW-HW | all | 97% | 96% to 98% | 299 | 4 |
| CW-IDK | all | 93% | 91% to 95% | 298 | 12 |
| HC-IDK | all | 94% | 92% to 96% | 299 | 4 |
| HW-IDK | all | 83% | 80% to 86% | 295 | 15 |
| CC-HC | judge knows | 99% | 98% to 100% | 229 | 2 |
| CC-IDK | judge knows | 100% | 99% to 100% | 229 | 0 |
| CW-CC | judge knows | 10% | 7% to 13% | 229 | 3 |
| CW-HC | judge knows | 42% | 37% to 48% | 228 | 5 |
| CW-HW | judge knows | 97% | 95% to 98% | 228 | 4 |
| CW-IDK | judge knows | 92% | 90% to 94% | 227 | 12 |
| HC-IDK | judge knows | 95% | 93% to 97% | 228 | 4 |
| HW-IDK | judge knows | 81% | 78% to 85% | 224 | 15 |
| CC-HC | judge does not know | 100% | 100% to 100% | 71 | 2 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 71 | 0 |
| CW-CC | judge does not know | 47% | 37% to 57% | 71 | 3 |
| CW-HC | judge does not know | 73% | 64% to 82% | 71 | 5 |
| CW-HW | judge does not know | 99% | 96% to 100% | 71 | 4 |
| CW-IDK | judge does not know | 96% | 94% to 99% | 71 | 12 |
| HC-IDK | judge does not know | 91% | 86% to 95% | 71 | 4 |
| HW-IDK | judge does not know | 88% | 83% to 93% | 71 | 15 |
| CC-HC | judge tells the two answers apart | 99% | 98% to 100% | 184 | 2 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 184 | 0 |
| CW-CC | judge tells the two answers apart | 8% | 5% to 12% | 184 | 3 |
| CW-HC | judge tells the two answers apart | 33% | 28% to 39% | 183 | 5 |
| CW-HW | judge tells the two answers apart | 96% | 94% to 98% | 183 | 4 |
| CW-IDK | judge tells the two answers apart | 90% | 87% to 93% | 182 | 12 |
| HC-IDK | judge tells the two answers apart | 96% | 95% to 98% | 184 | 4 |
| HW-IDK | judge tells the two answers apart | 79% | 75% to 83% | 181 | 15 |
| CC-HC | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 209 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 209 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 13% | 10% to 17% | 209 | 3 |
| CW-HC | judge flags the wrong answer as incorrect | 39% | 33% to 44% | 208 | 5 |
| CW-HW | judge flags the wrong answer as incorrect | 96% | 95% to 98% | 208 | 4 |
| CW-IDK | judge flags the wrong answer as incorrect | 90% | 87% to 93% | 207 | 12 |
| HC-IDK | judge flags the wrong answer as incorrect | 94% | 92% to 96% | 209 | 4 |
| HW-IDK | judge flags the wrong answer as incorrect | 79% | 75% to 83% | 206 | 15 |
| CC-HC | judge knows and flags the wrong answer | 99% | 98% to 100% | 172 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 172 | 0 |
| CW-CC | judge knows and flags the wrong answer | 8% | 5% to 11% | 172 | 3 |
| CW-HC | judge knows and flags the wrong answer | 34% | 28% to 40% | 171 | 5 |
| CW-HW | judge knows and flags the wrong answer | 96% | 94% to 98% | 171 | 4 |
| CW-IDK | judge knows and flags the wrong answer | 90% | 86% to 93% | 170 | 12 |
| HC-IDK | judge knows and flags the wrong answer | 96% | 93% to 98% | 172 | 4 |
| HW-IDK | judge knows and flags the wrong answer | 78% | 74% to 82% | 169 | 15 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 47% | 39% to 56% | 99 | 5 |
| CW-IDK | domain geo | 89% | 84% to 93% | 99 | 12 |
| CC-IDK | domain law | 100% | 98% to 100% | 100 | 0 |
| CW-HC | domain law | 54% | 45% to 62% | 100 | 5 |
| CW-IDK | domain law | 96% | 94% to 98% | 100 | 12 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain medqa | 48% | 40% to 57% | 100 | 5 |
| CW-IDK | domain medqa | 94% | 90% to 97% | 99 | 12 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 90 | 0 |
| CW-HC | domain geo, judge knows | 43% | 34% to 51% | 89 | 5 |
| CW-IDK | domain geo, judge knows | 88% | 83% to 93% | 89 | 12 |
| CC-IDK | domain law, judge knows | 99% | 98% to 100% | 63 | 0 |
| CW-HC | domain law, judge knows | 44% | 33% to 56% | 63 | 5 |
| CW-IDK | domain law, judge knows | 96% | 92% to 99% | 63 | 12 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 76 | 0 |
| CW-HC | domain medqa, judge knows | 40% | 31% to 50% | 76 | 5 |
| CW-IDK | domain medqa, judge knows | 93% | 89% to 97% | 75 | 12 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 93% | +0.07 | -6.42 | -9.61 to -4.62 | 97% | 91% | 50% |
| judge knows | 100% | 92% | +0.08 | -5.46 | -8.33 to -3.83 | 97% | 89% | 43% |
| judge does not know | 100% | 96% | +0.04 | -13.20 | -22.67 to -6.10 | 99% | 95% | 73% |
| judge tells the two answers apart | 100% | 90% | +0.10 | -3.92 | -6.00 to -2.87 | 96% | 86% | 34% |
| judge flags the wrong answer as incorrect | 100% | 90% | +0.10 | -4.18 | -6.14 to -2.98 | 96% | 87% | 39% |
| judge knows and flags the wrong answer | 100% | 90% | +0.10 | -3.86 | -5.80 to -2.70 | 96% | 86% | 34% |
| domain geo | 100% | 89% | +0.11 | -3.50 | -6.07 to -2.19 | 95% | 85% | 47% |
| domain law | 100% | 96% | +0.03 | -15.50 | -24.00 to -7.33 | 98% | 96% | 54% |
| domain medqa | 100% | 94% | +0.06 | -7.25 | -15.50 to -4.21 | 98% | 92% | 48% |
| domain geo, judge knows | 100% | 88% | +0.12 | -3.24 | -5.85 to -1.97 | 95% | 84% | 43% |
| domain law, judge knows | 99% | 96% | +0.03 | -14.50 | -20.00 to -6.00 | 99% | 96% | 44% |
| domain medqa, judge knows | 100% | 93% | +0.07 | -6.50 | -14.00 to -3.69 | 97% | 91% | 41% |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 84% on 300 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 93% | 92% to 95% | 300 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 300 | 0 |
| CW-CC | all | 14% | 11% to 18% | 300 | 1 |
| CW-HC | all | 22% | 18% to 26% | 300 | 0 |
| CW-HW | all | 68% | 64% to 72% | 300 | 0 |
| CW-IDK | all | 86% | 82% to 88% | 300 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 300 | 0 |
| HW-IDK | all | 98% | 97% to 99% | 300 | 0 |
| CC-HC | judge knows | 95% | 93% to 97% | 253 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 253 | 0 |
| CW-CC | judge knows | 8% | 6% to 11% | 253 | 1 |
| CW-HC | judge knows | 15% | 11% to 18% | 253 | 0 |
| CW-HW | judge knows | 66% | 62% to 70% | 253 | 0 |
| CW-IDK | judge knows | 84% | 80% to 87% | 253 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 253 | 0 |
| HW-IDK | judge knows | 98% | 97% to 99% | 253 | 0 |
| CC-HC | judge does not know | 84% | 78% to 90% | 47 | 0 |
| CC-IDK | judge does not know | 99% | 97% to 100% | 47 | 0 |
| CW-CC | judge does not know | 47% | 34% to 60% | 47 | 1 |
| CW-HC | judge does not know | 63% | 51% to 74% | 47 | 0 |
| CW-HW | judge does not know | 76% | 67% to 84% | 47 | 0 |
| CW-IDK | judge does not know | 95% | 88% to 99% | 47 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 47 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 47 | 0 |
| CC-HC | judge tells the two answers apart | 95% | 93% to 97% | 241 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 241 | 0 |
| CW-CC | judge tells the two answers apart | 6% | 4% to 9% | 241 | 1 |
| CW-HC | judge tells the two answers apart | 12% | 10% to 16% | 241 | 0 |
| CW-HW | judge tells the two answers apart | 64% | 60% to 68% | 241 | 0 |
| CW-IDK | judge tells the two answers apart | 82% | 78% to 86% | 241 | 0 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 241 | 0 |
| HW-IDK | judge tells the two answers apart | 98% | 96% to 99% | 241 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 94% | 92% to 96% | 267 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 267 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 9% | 6% to 12% | 267 | 1 |
| CW-HC | judge flags the wrong answer as incorrect | 16% | 13% to 19% | 267 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 66% | 62% to 70% | 267 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 80% to 87% | 267 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 267 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 98% | 97% to 99% | 267 | 0 |
| CC-HC | judge knows and flags the wrong answer | 95% | 93% to 97% | 239 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 239 | 0 |
| CW-CC | judge knows and flags the wrong answer | 6% | 4% to 9% | 239 | 1 |
| CW-HC | judge knows and flags the wrong answer | 12% | 9% to 15% | 239 | 0 |
| CW-HW | judge knows and flags the wrong answer | 65% | 61% to 70% | 239 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 83% | 79% to 86% | 239 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 239 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 98% | 96% to 99% | 239 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 15% | 10% to 21% | 100 | 0 |
| CW-IDK | domain geo | 84% | 78% to 90% | 100 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain law | 32% | 25% to 40% | 100 | 0 |
| CW-IDK | domain law | 89% | 84% to 93% | 100 | 0 |
| CC-IDK | domain medqa | 100% | 98% to 100% | 100 | 0 |
| CW-HC | domain medqa | 19% | 12% to 26% | 100 | 0 |
| CW-IDK | domain medqa | 84% | 78% to 90% | 100 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 91 | 0 |
| CW-HC | domain geo, judge knows | 10% | 5% to 15% | 91 | 0 |
| CW-IDK | domain geo, judge knows | 82% | 75% to 88% | 91 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 77 | 0 |
| CW-HC | domain law, judge knows | 26% | 19% to 34% | 77 | 0 |
| CW-IDK | domain law, judge knows | 88% | 82% to 92% | 77 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 85 | 0 |
| CW-HC | domain medqa, judge knows | 9% | 5% to 14% | 85 | 0 |
| CW-IDK | domain medqa, judge knows | 82% | 76% to 88% | 85 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 86% | +0.14 | -2.48 | -3.43 to -1.83 | 68% | 58% | 22% |
| judge knows | 100% | 84% | +0.16 | -2.09 | -2.89 to -1.53 | 66% | 56% | 15% |
| judge does not know | 99% | 95% | +0.04 | -10.50 | -22.50 to -3.40 | 76% | 72% | 63% |
| judge tells the two answers apart | 100% | 82% | +0.18 | -1.80 | -2.54 to -1.32 | 64% | 53% | 12% |
| judge flags the wrong answer as incorrect | 100% | 84% | +0.16 | -2.09 | -2.91 to -1.54 | 66% | 55% | 16% |
| judge knows and flags the wrong answer | 100% | 83% | +0.17 | -1.91 | -2.68 to -1.41 | 65% | 54% | 12% |
| domain geo | 100% | 84% | +0.17 | -2.03 | -3.55 to -1.22 | 72% | 60% | 15% |
| domain law | 100% | 89% | +0.11 | -3.55 | -6.14 to -2.23 | 66% | 59% | 32% |
| domain medqa | 100% | 84% | +0.16 | -2.19 | -4.05 to -1.33 | 65% | 55% | 19% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.76 | -3.14 to -1.02 | 69% | 57% | 10% |
| domain law, judge knows | 100% | 88% | +0.12 | -3.05 | -5.42 to -1.85 | 67% | 59% | 26% |
| domain medqa, judge knows | 100% | 82% | +0.18 | -1.83 | -3.25 to -1.07 | 63% | 52% | 9% |

### prompt variant think (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 99% | 98% to 100% | 300 | 0 |
| CW-IDK | all | 61% | 56% to 65% | 300 | 0 |
| CC-IDK | judge knows | 100% | 99% to 100% | 253 | 0 |
| CW-IDK | judge knows | 56% | 51% to 61% | 253 | 0 |
| CC-IDK | judge does not know | 94% | 86% to 99% | 47 | 0 |
| CW-IDK | judge does not know | 85% | 76% to 94% | 47 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 99% to 100% | 241 | 0 |
| CW-IDK | judge tells the two answers apart | 53% | 48% to 58% | 241 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 267 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 56% | 51% to 61% | 267 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 239 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 54% | 49% to 59% | 239 | 0 |
| CC-IDK | domain geo | 99% | 97% to 100% | 100 | 0 |
| CW-IDK | domain geo | 39% | 31% to 47% | 100 | 0 |
| CC-IDK | domain law | 98% | 96% to 100% | 100 | 0 |
| CW-IDK | domain law | 84% | 78% to 88% | 100 | 0 |
| CC-IDK | domain medqa | 98% | 96% to 100% | 100 | 0 |
| CW-IDK | domain medqa | 60% | 52% to 67% | 100 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 91 | 0 |
| CW-IDK | domain geo, judge knows | 35% | 27% to 43% | 91 | 0 |
| CC-IDK | domain law, judge knows | 99% | 97% to 100% | 77 | 0 |
| CW-IDK | domain law, judge knows | 81% | 74% to 88% | 77 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 85 | 0 |
| CW-IDK | domain medqa, judge knows | 56% | 48% to 64% | 85 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 61% | +0.38 | -0.28 | -0.45 to -0.14 | - | - | - |
| judge knows | 100% | 56% | +0.43 | -0.14 | -0.28 to -0.02 | - | - | - |
| judge does not know | 94% | 85% | +0.09 | -4.12 | -18.50 to -1.44 | - | - | - |
| judge tells the two answers apart | 100% | 53% | +0.47 | -0.07 | -0.19 to +0.04 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 56% | +0.43 | -0.15 | -0.29 to -0.03 | - | - | - |
| judge knows and flags the wrong answer | 100% | 54% | +0.46 | -0.09 | -0.22 to +0.02 | - | - | - |
| domain geo | 99% | 39% | +0.60 | +0.18 | +0.07 to +0.28 | - | - | - |
| domain law | 98% | 84% | +0.15 | -2.23 | -3.85 to -1.37 | - | - | - |
| domain medqa | 98% | 60% | +0.39 | -0.24 | -0.54 to -0.04 | - | - | - |
| domain geo, judge knows | 100% | 35% | +0.65 | +0.23 | +0.12 to +0.31 | - | - | - |
| domain law, judge knows | 99% | 81% | +0.18 | -1.78 | -3.24 to -1.00 | - | - | - |
| domain medqa, judge knows | 100% | 56% | +0.44 | -0.13 | -0.37 to +0.03 | - | - | - |
