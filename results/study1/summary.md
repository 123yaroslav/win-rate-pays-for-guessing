items 300 (geo, law, medqa), bootstrap draws 10000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 7 of 7 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 93.8% | 91.3% to 96.0% | 248 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 60.7% | 55.3% to 65.8% | 234 | 0.0001 | yes |
| adaption/qwen3.8-27b | 62.9% | 59.9% to 66.2% | 232 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 82.7% | 79.1% to 86.1% | 237 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.1% | 89.6% to 94.3% | 227 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.8% | 80.2% to 87.2% | 253 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-terra | 68.0% | 57.0% to 78.0% | 50 | 0.0007 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 7 of 7 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 94.8% | 93.0% to 96.7% | 300 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 65.8% | 61.3% to 70.3% | 288 | 0.0000 | yes |
| adaption/qwen3.8-27b | 65.5% | 62.7% to 68.3% | 300 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 84.4% | 81.5% to 87.2% | 298 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 93.1% | 91.1% to 95.1% | 298 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.5% | 82.3% to 88.5% | 300 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-terra | 72.5% | 62.5% to 81.7% | 60 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 7 of 7 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 92.8% | 89.9% to 95.4% | 194 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 63.4% | 58.5% to 68.3% | 254 | 0.0000 | yes |
| adaption/qwen3.8-27b | 65.4% | 62.5% to 68.2% | 299 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 84.0% | 81.0% to 86.9% | 287 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 90.3% | 87.4% to 93.0% | 207 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.7% | 80.1% to 86.9% | 267 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-terra | 69.4% | 59.3% to 79.6% | 54 | 0.0002 | yes |

S1g2: b above 0.5 on group 'judge tells the two answers apart', Holm at 0.05. Passed by 7 of 7 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 92.1% | 89.0% to 94.9% | 177 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 61.2% | 55.8% to 66.5% | 215 | 0.0001 | yes |
| adaption/qwen3.8-27b | 60.7% | 56.9% to 64.8% | 159 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 79.9% | 75.5% to 84.2% | 149 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 89.8% | 86.5% to 92.9% | 182 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.2% | 78.4% to 85.9% | 241 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-terra | 64.9% | 53.2% to 75.5% | 47 | 0.0061 | yes |

## Detection (S1g)

| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |
|---|---|---|---|
| adaption/deepseek-v4-flash | 65.5% | 91.2% | 0 |
| adaption/gemma-4-31b-it | 88.3% | 80.3% | 20 |
| adaption/qwen3.8-27b | 99.7% | 53.0% | 0 |
| openrouter/anthropic/claude-haiku-5.5 | 96.3% | 52.3% | 1 |
| openrouter/mistralai/mistral-small-2603 | 69.7% | 86.7% | 0 |
| openrouter/openai/gpt-5.6-luna | 89.0% | 86.7% | 0 |
| openrouter/openai/gpt-5.6-terra | 90.0% | 85.0% | 0 |

## Verify-then-compare, composed from logged verdicts (exploratory)

| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |
|---|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 99.5% | 94.7% | 90.8% | 34.1% | 0.28 | 0.20 to 0.34 |
| adaption/gemma-4-31b-it | 98.7% | 66.5% | 82.4% | 8.6% | 0.56 | 0.53 to 0.60 |
| adaption/qwen3.8-27b | 87.8% | 65.5% | 48.8% | 0.3% | 1.02 | 0.92 to 1.15 |
| openrouter/anthropic/claude-haiku-5.5 | 98.1% | 84.3% | 51.7% | 3.2% | 0.97 | 0.87 to 1.10 |
| openrouter/mistralai/mistral-small-2603 | 99.8% | 93.1% | 86.6% | 30.4% | 0.35 | 0.28 to 0.41 |
| openrouter/openai/gpt-5.6-luna | 99.8% | 85.5% | 86.7% | 11.0% | 0.52 | 0.49 to 0.55 |
| openrouter/openai/gpt-5.6-terra | 100.0% | 72.5% | 85.0% | 10.0% | 0.53 | 0.46 to 0.61 |

## Two-step account (S1d)

Cells 18, mean absolute error 0.256, Spearman 0.67. Mean predicted 69.3%, mean observed 43.7%.

## adaption/deepseek-v4-flash: own closed-book accuracy 83% on 300 items

### prompt variant default (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 97% | 96% to 98% | 300 | 0 |
| CC-IDK | all | 100% | 99% to 100% | 300 | 0 |
| CW-CC | all | 19% | 16% to 23% | 300 | 0 |
| CW-HC | all | 73% | 69% to 77% | 300 | 0 |
| CW-HW | all | 97% | 95% to 98% | 300 | 0 |
| CW-IDK | all | 95% | 93% to 97% | 300 | 0 |
| HC-IDK | all | 98% | 96% to 99% | 300 | 1 |
| HW-IDK | all | 96% | 95% to 98% | 300 | 0 |
| CC-HC | judge knows | 97% | 96% to 99% | 248 | 0 |
| CC-IDK | judge knows | 100% | 99% to 100% | 248 | 0 |
| CW-CC | judge knows | 15% | 11% to 18% | 248 | 0 |
| CW-HC | judge knows | 70% | 65% to 74% | 248 | 0 |
| CW-HW | judge knows | 96% | 95% to 98% | 248 | 0 |
| CW-IDK | judge knows | 94% | 91% to 96% | 248 | 0 |
| HC-IDK | judge knows | 98% | 97% to 99% | 248 | 1 |
| HW-IDK | judge knows | 96% | 94% to 98% | 248 | 0 |
| CC-HC | judge does not know | 96% | 92% to 99% | 52 | 0 |
| CC-IDK | judge does not know | 99% | 97% to 100% | 52 | 0 |
| CW-CC | judge does not know | 42% | 33% to 52% | 52 | 0 |
| CW-HC | judge does not know | 88% | 81% to 95% | 52 | 0 |
| CW-HW | judge does not know | 99% | 97% to 100% | 52 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 52 | 0 |
| HC-IDK | judge does not know | 95% | 90% to 99% | 52 | 1 |
| HW-IDK | judge does not know | 97% | 93% to 100% | 52 | 0 |
| CC-HC | judge tells the two answers apart | 99% | 97% to 100% | 177 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 99% to 100% | 177 | 0 |
| CW-CC | judge tells the two answers apart | 10% | 7% to 14% | 177 | 0 |
| CW-HC | judge tells the two answers apart | 65% | 60% to 71% | 177 | 0 |
| CW-HW | judge tells the two answers apart | 96% | 94% to 98% | 177 | 0 |
| CW-IDK | judge tells the two answers apart | 92% | 89% to 95% | 177 | 0 |
| HC-IDK | judge tells the two answers apart | 98% | 97% to 99% | 177 | 1 |
| HW-IDK | judge tells the two answers apart | 95% | 93% to 97% | 177 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 98% | 97% to 99% | 194 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 99% to 100% | 194 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 13% | 9% to 16% | 194 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 67% | 62% to 72% | 194 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 96% | 94% to 98% | 194 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 95% | 194 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 98% | 97% to 99% | 194 | 1 |
| HW-IDK | judge flags the wrong answer as incorrect | 96% | 94% to 97% | 194 | 0 |
| CC-HC | judge knows and flags the wrong answer | 98% | 96% to 99% | 169 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 169 | 0 |
| CW-CC | judge knows and flags the wrong answer | 10% | 7% to 13% | 169 | 0 |
| CW-HC | judge knows and flags the wrong answer | 64% | 59% to 70% | 169 | 0 |
| CW-HW | judge knows and flags the wrong answer | 96% | 94% to 98% | 169 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 92% | 88% to 95% | 169 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 99% | 97% to 100% | 169 | 1 |
| HW-IDK | judge knows and flags the wrong answer | 95% | 93% to 97% | 169 | 0 |
| CC-IDK | domain geo | 99% | 98% to 100% | 100 | 0 |
| CW-HC | domain geo | 68% | 60% to 75% | 100 | 0 |
| CW-IDK | domain geo | 88% | 84% to 93% | 100 | 0 |
| CC-IDK | domain law | 100% | 98% to 100% | 100 | 0 |
| CW-HC | domain law | 72% | 64% to 78% | 100 | 0 |
| CW-IDK | domain law | 98% | 96% to 100% | 100 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain medqa | 80% | 74% to 85% | 100 | 0 |
| CW-IDK | domain medqa | 98% | 95% to 100% | 100 | 0 |
| CC-IDK | domain geo, judge knows | 99% | 98% to 100% | 92 | 0 |
| CW-HC | domain geo, judge knows | 66% | 59% to 74% | 92 | 0 |
| CW-IDK | domain geo, judge knows | 88% | 82% to 92% | 92 | 0 |
| CC-IDK | domain law, judge knows | 99% | 98% to 100% | 77 | 0 |
| CW-HC | domain law, judge knows | 68% | 60% to 77% | 77 | 0 |
| CW-IDK | domain law, judge knows | 98% | 95% to 100% | 77 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 79 | 0 |
| CW-HC | domain medqa, judge knows | 75% | 68% to 82% | 79 | 0 |
| CW-IDK | domain medqa, judge knows | 97% | 94% to 99% | 79 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 95% | +0.05 | -9.61 | -16.41 to -6.43 | 97% | 92% | 73% |
| judge knows | 100% | 94% | +0.06 | -7.48 | -12.56 to -5.02 | 96% | 91% | 70% |
| judge does not know | 99% | 100% | -0.01 | undefined | +nan to +nan | 99% | 100% | 88% |
| judge tells the two answers apart | 100% | 92% | +0.08 | -5.52 | -9.35 to -3.63 | 96% | 89% | 65% |
| judge flags the wrong answer as incorrect | 99% | 93% | +0.07 | -6.38 | -11.06 to -4.19 | 96% | 90% | 67% |
| judge knows and flags the wrong answer | 100% | 92% | +0.08 | -5.22 | -8.88 to -3.45 | 96% | 88% | 64% |
| domain geo | 99% | 88% | +0.10 | -3.67 | -7.25 to -2.19 | 95% | 85% | 68% |
| domain law | 100% | 98% | +0.01 | undefined | -24.00 to -11.50 | 96% | 96% | 72% |
| domain medqa | 100% | 98% | +0.03 | -19.00 | -24.00 to -9.00 | 99% | 97% | 80% |
| domain geo, judge knows | 99% | 88% | +0.12 | -3.14 | -6.00 to -1.88 | 95% | 83% | 66% |
| domain law, judge knows | 99% | 98% | +0.01 | undefined | -18.25 to -8.62 | 96% | 95% | 68% |
| domain medqa, judge knows | 100% | 97% | +0.03 | -14.80 | -18.75 to -6.90 | 99% | 96% | 75% |

## adaption/gemma-4-31b-it: own closed-book accuracy 82% on 300 items

### prompt variant default (picks the first position in 58% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 99% to 100% | 299 | 9 |
| CC-IDK | all | 99% | 98% to 100% | 297 | 12 |
| CW-CC | all | 9% | 6% to 12% | 296 | 19 |
| CW-HC | all | 24% | 20% to 29% | 295 | 35 |
| CW-HW | all | 89% | 85% to 92% | 189 | 263 |
| CW-IDK | all | 66% | 61% to 70% | 288 | 53 |
| HC-IDK | all | 93% | 91% to 95% | 296 | 13 |
| HW-IDK | all | 41% | 37% to 45% | 299 | 16 |
| CC-HC | judge knows | 100% | 99% to 100% | 244 | 9 |
| CC-IDK | judge knows | 100% | 100% to 100% | 243 | 12 |
| CW-CC | judge knows | 2% | 1% to 4% | 243 | 19 |
| CW-HC | judge knows | 14% | 11% to 18% | 241 | 35 |
| CW-HW | judge knows | 86% | 81% to 90% | 138 | 263 |
| CW-IDK | judge knows | 61% | 55% to 66% | 234 | 53 |
| HC-IDK | judge knows | 99% | 97% to 100% | 241 | 13 |
| HW-IDK | judge knows | 36% | 32% to 40% | 244 | 16 |
| CC-HC | judge does not know | 100% | 100% to 100% | 55 | 9 |
| CC-IDK | judge does not know | 94% | 87% to 98% | 54 | 12 |
| CW-CC | judge does not know | 42% | 30% to 54% | 53 | 19 |
| CW-HC | judge does not know | 69% | 58% to 79% | 54 | 35 |
| CW-HW | judge does not know | 96% | 92% to 99% | 51 | 263 |
| CW-IDK | judge does not know | 88% | 81% to 94% | 54 | 53 |
| HC-IDK | judge does not know | 71% | 63% to 79% | 55 | 13 |
| HW-IDK | judge does not know | 64% | 55% to 73% | 55 | 16 |
| CC-HC | judge tells the two answers apart | 100% | 99% to 100% | 225 | 9 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 223 | 12 |
| CW-CC | judge tells the two answers apart | 1% | 0% to 3% | 222 | 19 |
| CW-HC | judge tells the two answers apart | 14% | 10% to 18% | 221 | 35 |
| CW-HW | judge tells the two answers apart | 86% | 82% to 91% | 125 | 263 |
| CW-IDK | judge tells the two answers apart | 61% | 56% to 67% | 215 | 53 |
| HC-IDK | judge tells the two answers apart | 98% | 97% to 99% | 222 | 13 |
| HW-IDK | judge tells the two answers apart | 36% | 31% to 40% | 225 | 16 |
| CC-HC | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 264 | 9 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 262 | 12 |
| CW-CC | judge flags the wrong answer as incorrect | 5% | 3% to 7% | 261 | 19 |
| CW-HC | judge flags the wrong answer as incorrect | 20% | 15% to 24% | 260 | 35 |
| CW-HW | judge flags the wrong answer as incorrect | 87% | 83% to 91% | 161 | 263 |
| CW-IDK | judge flags the wrong answer as incorrect | 63% | 58% to 68% | 254 | 53 |
| HC-IDK | judge flags the wrong answer as incorrect | 94% | 92% to 96% | 261 | 13 |
| HW-IDK | judge flags the wrong answer as incorrect | 37% | 33% to 41% | 264 | 16 |
| CC-HC | judge knows and flags the wrong answer | 100% | 99% to 100% | 223 | 9 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 222 | 12 |
| CW-CC | judge knows and flags the wrong answer | 1% | 0% to 2% | 222 | 19 |
| CW-HC | judge knows and flags the wrong answer | 12% | 9% to 16% | 220 | 35 |
| CW-HW | judge knows and flags the wrong answer | 85% | 80% to 90% | 123 | 263 |
| CW-IDK | judge knows and flags the wrong answer | 60% | 54% to 65% | 214 | 53 |
| HC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 220 | 13 |
| HW-IDK | judge knows and flags the wrong answer | 34% | 30% to 38% | 223 | 16 |
| CC-IDK | domain geo | 99% | 97% to 100% | 99 | 12 |
| CW-HC | domain geo | 13% | 7% to 19% | 99 | 35 |
| CW-IDK | domain geo | 43% | 36% to 51% | 98 | 53 |
| CC-IDK | domain law | 98% | 96% to 100% | 99 | 12 |
| CW-HC | domain law | 32% | 24% to 40% | 97 | 35 |
| CW-IDK | domain law | 86% | 80% to 91% | 96 | 53 |
| CC-IDK | domain medqa | 99% | 97% to 100% | 99 | 12 |
| CW-HC | domain medqa | 28% | 20% to 36% | 99 | 35 |
| CW-IDK | domain medqa | 69% | 61% to 77% | 94 | 53 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 91 | 12 |
| CW-HC | domain geo, judge knows | 8% | 4% to 13% | 91 | 35 |
| CW-IDK | domain geo, judge knows | 41% | 33% to 49% | 90 | 53 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 71 | 12 |
| CW-HC | domain law, judge knows | 15% | 9% to 22% | 69 | 35 |
| CW-IDK | domain law, judge knows | 82% | 74% to 89% | 68 | 53 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 81 | 12 |
| CW-HC | domain medqa, judge knows | 20% | 13% to 28% | 81 | 35 |
| CW-IDK | domain medqa, judge knows | 64% | 55% to 74% | 76 | 53 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 66% | +0.33 | -0.48 | -0.71 to -0.30 | 89% | 73% | 37% |
| judge knows | 100% | 61% | +0.39 | -0.27 | -0.46 to -0.13 | 86% | 67% | 25% |
| judge does not know | 94% | 88% | +0.06 | -6.83 | -15.00 to -2.75 | 96% | 92% | 70% |
| judge tells the two answers apart | 100% | 61% | +0.39 | -0.29 | -0.49 to -0.13 | 86% | 68% | 24% |
| judge flags the wrong answer as incorrect | 99% | 63% | +0.35 | -0.38 | -0.60 to -0.21 | 87% | 70% | 31% |
| judge knows and flags the wrong answer | 100% | 60% | +0.40 | -0.24 | -0.43 to -0.09 | 85% | 65% | 21% |
| domain geo | 99% | 43% | +0.56 | +0.12 | -0.02 to +0.23 | 78% | 46% | 27% |
| domain law | 98% | 86% | +0.12 | -2.88 | -5.92 to -1.66 | 93% | 84% | 36% |
| domain medqa | 99% | 69% | +0.30 | -0.61 | -1.19 to -0.28 | 92% | 83% | 47% |
| domain geo, judge knows | 100% | 41% | +0.59 | +0.15 | +0.02 to +0.25 | 76% | 41% | 20% |
| domain law, judge knows | 100% | 82% | +0.18 | -1.83 | -3.53 to -1.00 | 91% | 78% | 18% |
| domain medqa, judge knows | 100% | 64% | +0.36 | -0.41 | -0.90 to -0.12 | 88% | 78% | 39% |

## adaption/qwen3.8-27b: own closed-book accuracy 77% on 300 items

### prompt variant default (picks the first position in 27% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 89% | 87% to 92% | 300 | 0 |
| CC-IDK | all | 88% | 85% to 90% | 300 | 1 |
| CW-CC | all | 18% | 15% to 21% | 300 | 6 |
| CW-HC | all | 44% | 40% to 47% | 299 | 9 |
| CW-HW | all | 68% | 65% to 71% | 300 | 6 |
| CW-IDK | all | 66% | 63% to 68% | 300 | 6 |
| HC-IDK | all | 81% | 78% to 84% | 300 | 0 |
| HW-IDK | all | 63% | 60% to 66% | 300 | 5 |
| CC-HC | judge knows | 92% | 90% to 94% | 232 | 0 |
| CC-IDK | judge knows | 90% | 88% to 93% | 232 | 1 |
| CW-CC | judge knows | 13% | 10% to 16% | 232 | 6 |
| CW-HC | judge knows | 38% | 34% to 42% | 231 | 9 |
| CW-HW | judge knows | 66% | 63% to 69% | 232 | 6 |
| CW-IDK | judge knows | 63% | 60% to 66% | 232 | 6 |
| HC-IDK | judge knows | 84% | 81% to 87% | 232 | 0 |
| HW-IDK | judge knows | 62% | 59% to 65% | 232 | 5 |
| CC-HC | judge does not know | 80% | 74% to 86% | 68 | 0 |
| CC-IDK | judge does not know | 80% | 74% to 86% | 68 | 1 |
| CW-CC | judge does not know | 37% | 29% to 45% | 68 | 6 |
| CW-HC | judge does not know | 63% | 57% to 70% | 68 | 9 |
| CW-HW | judge does not know | 75% | 69% to 81% | 68 | 6 |
| CW-IDK | judge does not know | 74% | 68% to 81% | 68 | 6 |
| HC-IDK | judge does not know | 71% | 65% to 76% | 68 | 0 |
| HW-IDK | judge does not know | 68% | 61% to 74% | 68 | 5 |
| CC-HC | judge tells the two answers apart | 94% | 92% to 97% | 159 | 0 |
| CC-IDK | judge tells the two answers apart | 92% | 89% to 95% | 159 | 1 |
| CW-CC | judge tells the two answers apart | 10% | 7% to 13% | 159 | 6 |
| CW-HC | judge tells the two answers apart | 33% | 29% to 37% | 158 | 9 |
| CW-HW | judge tells the two answers apart | 64% | 60% to 67% | 159 | 6 |
| CW-IDK | judge tells the two answers apart | 61% | 57% to 65% | 159 | 6 |
| HC-IDK | judge tells the two answers apart | 86% | 83% to 90% | 159 | 0 |
| HW-IDK | judge tells the two answers apart | 58% | 54% to 62% | 159 | 5 |
| CC-HC | judge flags the wrong answer as incorrect | 89% | 87% to 91% | 299 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 88% | 85% to 90% | 299 | 1 |
| CW-CC | judge flags the wrong answer as incorrect | 18% | 15% to 21% | 299 | 6 |
| CW-HC | judge flags the wrong answer as incorrect | 44% | 40% to 47% | 298 | 9 |
| CW-HW | judge flags the wrong answer as incorrect | 68% | 65% to 71% | 299 | 6 |
| CW-IDK | judge flags the wrong answer as incorrect | 65% | 63% to 68% | 299 | 6 |
| HC-IDK | judge flags the wrong answer as incorrect | 81% | 78% to 84% | 299 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 63% | 61% to 66% | 299 | 5 |
| CC-HC | judge knows and flags the wrong answer | 92% | 90% to 94% | 232 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 90% | 88% to 93% | 232 | 1 |
| CW-CC | judge knows and flags the wrong answer | 13% | 10% to 16% | 232 | 6 |
| CW-HC | judge knows and flags the wrong answer | 38% | 34% to 42% | 231 | 9 |
| CW-HW | judge knows and flags the wrong answer | 66% | 63% to 69% | 232 | 6 |
| CW-IDK | judge knows and flags the wrong answer | 63% | 60% to 66% | 232 | 6 |
| HC-IDK | judge knows and flags the wrong answer | 84% | 81% to 88% | 232 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 62% | 59% to 65% | 232 | 5 |
| CC-IDK | domain geo | 96% | 94% to 99% | 100 | 1 |
| CW-HC | domain geo | 36% | 30% to 42% | 100 | 9 |
| CW-IDK | domain geo | 68% | 62% to 72% | 100 | 6 |
| CC-IDK | domain law | 83% | 78% to 88% | 100 | 1 |
| CW-HC | domain law | 47% | 41% to 54% | 99 | 9 |
| CW-IDK | domain law | 66% | 61% to 71% | 100 | 6 |
| CC-IDK | domain medqa | 84% | 80% to 88% | 100 | 1 |
| CW-HC | domain medqa | 48% | 42% to 52% | 100 | 9 |
| CW-IDK | domain medqa | 63% | 58% to 68% | 100 | 6 |
| CC-IDK | domain geo, judge knows | 97% | 95% to 99% | 92 | 1 |
| CW-HC | domain geo, judge knows | 33% | 27% to 39% | 92 | 9 |
| CW-IDK | domain geo, judge knows | 65% | 60% to 71% | 92 | 6 |
| CC-IDK | domain law, judge knows | 85% | 80% to 90% | 71 | 1 |
| CW-HC | domain law, judge knows | 41% | 34% to 49% | 70 | 9 |
| CW-IDK | domain law, judge knows | 63% | 58% to 70% | 71 | 6 |
| CC-IDK | domain medqa, judge knows | 86% | 80% to 91% | 69 | 1 |
| CW-HC | domain medqa, judge knows | 42% | 36% to 48% | 69 | 9 |
| CW-IDK | domain medqa, judge knows | 59% | 54% to 64% | 69 | 6 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 88% | 66% | +0.22 | -0.69 | -0.97 to -0.49 | 68% | 53% | 44% |
| judge knows | 90% | 63% | +0.27 | -0.48 | -0.68 to -0.32 | 66% | 48% | 38% |
| judge does not know | 80% | 74% | +0.06 | -4.12 | -12.00 to -1.33 | 75% | 71% | 63% |
| judge tells the two answers apart | 92% | 61% | +0.31 | -0.34 | -0.53 to -0.19 | 64% | 44% | 33% |
| judge flags the wrong answer as incorrect | 88% | 65% | +0.22 | -0.69 | -0.96 to -0.49 | 68% | 53% | 44% |
| judge knows and flags the wrong answer | 90% | 63% | +0.27 | -0.48 | -0.69 to -0.32 | 66% | 48% | 38% |
| domain geo | 96% | 68% | +0.29 | -0.60 | -0.98 to -0.35 | 68% | 49% | 36% |
| domain law | 83% | 66% | +0.17 | -0.94 | -1.88 to -0.50 | 70% | 59% | 47% |
| domain medqa | 84% | 63% | +0.21 | -0.62 | -1.16 to -0.32 | 66% | 52% | 48% |
| domain geo, judge knows | 97% | 65% | +0.32 | -0.47 | -0.79 to -0.26 | 67% | 46% | 33% |
| domain law, judge knows | 85% | 63% | +0.22 | -0.61 | -1.30 to -0.27 | 67% | 53% | 41% |
| domain medqa, judge knows | 86% | 59% | +0.26 | -0.36 | -0.69 to -0.15 | 64% | 47% | 42% |

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
| CW-CC | judge does not know | 39% | 30% to 48% | 61 | 21 |
| CW-HC | judge does not know | 51% | 42% to 60% | 61 | 36 |
| CW-HW | judge does not know | 58% | 51% to 66% | 61 | 64 |
| CW-IDK | judge does not know | 91% | 86% to 96% | 61 | 11 |
| HC-IDK | judge does not know | 99% | 98% to 100% | 61 | 1 |
| HW-IDK | judge does not know | 94% | 90% to 98% | 61 | 6 |
| CC-HC | judge tells the two answers apart | 90% | 87% to 93% | 151 | 9 |
| CC-IDK | judge tells the two answers apart | 100% | 99% to 100% | 151 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 4% to 10% | 150 | 21 |
| CW-HC | judge tells the two answers apart | 20% | 15% to 25% | 148 | 36 |
| CW-HW | judge tells the two answers apart | 56% | 50% to 62% | 144 | 64 |
| CW-IDK | judge tells the two answers apart | 80% | 76% to 84% | 149 | 11 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 151 | 1 |
| HW-IDK | judge tells the two answers apart | 92% | 89% to 95% | 151 | 6 |
| CC-HC | judge flags the wrong answer as incorrect | 81% | 78% to 84% | 288 | 9 |
| CC-IDK | judge flags the wrong answer as incorrect | 98% | 97% to 99% | 289 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 18% | 15% to 21% | 287 | 21 |
| CW-HC | judge flags the wrong answer as incorrect | 34% | 30% to 39% | 284 | 36 |
| CW-HW | judge flags the wrong answer as incorrect | 58% | 54% to 62% | 279 | 64 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 81% to 87% | 287 | 11 |
| HC-IDK | judge flags the wrong answer as incorrect | 99% | 99% to 100% | 289 | 1 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 91% to 95% | 289 | 6 |
| CC-HC | judge knows and flags the wrong answer | 86% | 83% to 89% | 231 | 9 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 232 | 0 |
| CW-CC | judge knows and flags the wrong answer | 13% | 10% to 17% | 230 | 21 |
| CW-HC | judge knows and flags the wrong answer | 31% | 26% to 36% | 227 | 36 |
| CW-HW | judge knows and flags the wrong answer | 59% | 54% to 63% | 222 | 64 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 79% to 86% | 230 | 11 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 232 | 1 |
| HW-IDK | judge knows and flags the wrong answer | 93% | 91% to 95% | 232 | 6 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 37% | 29% to 45% | 98 | 36 |
| CW-IDK | domain geo | 83% | 78% to 87% | 99 | 11 |
| CC-IDK | domain law | 96% | 94% to 98% | 100 | 0 |
| CW-HC | domain law | 36% | 28% to 44% | 99 | 36 |
| CW-IDK | domain law | 85% | 80% to 90% | 100 | 11 |
| CC-IDK | domain medqa | 98% | 96% to 100% | 100 | 0 |
| CW-HC | domain medqa | 36% | 29% to 43% | 98 | 36 |
| CW-IDK | domain medqa | 85% | 80% to 90% | 99 | 11 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 90 | 0 |
| CW-HC | domain geo, judge knows | 34% | 26% to 43% | 88 | 36 |
| CW-IDK | domain geo, judge knows | 82% | 77% to 87% | 89 | 11 |
| CC-IDK | domain law, judge knows | 98% | 95% to 100% | 67 | 0 |
| CW-HC | domain law, judge knows | 31% | 21% to 41% | 66 | 36 |
| CW-IDK | domain law, judge knows | 83% | 76% to 89% | 67 | 11 |
| CC-IDK | domain medqa, judge knows | 99% | 98% to 100% | 82 | 0 |
| CW-HC | domain medqa, judge knows | 31% | 24% to 39% | 80 | 36 |
| CW-IDK | domain medqa, judge knows | 83% | 77% to 89% | 81 | 11 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 84% | +0.14 | -2.50 | -3.46 to -1.88 | 59% | 51% | 36% |
| judge knows | 99% | 83% | +0.16 | -1.99 | -2.77 to -1.48 | 59% | 49% | 33% |
| judge does not know | 94% | 91% | +0.03 | -12.50 | -17.67 to -3.67 | 58% | 56% | 51% |
| judge tells the two answers apart | 100% | 80% | +0.20 | -1.51 | -2.17 to -1.04 | 56% | 44% | 20% |
| judge flags the wrong answer as incorrect | 98% | 84% | +0.14 | -2.38 | -3.31 to -1.79 | 58% | 50% | 34% |
| judge knows and flags the wrong answer | 99% | 82% | +0.17 | -1.94 | -2.72 to -1.42 | 59% | 49% | 31% |
| domain geo | 100% | 83% | +0.17 | -1.91 | -3.12 to -1.25 | 64% | 53% | 38% |
| domain law | 96% | 85% | +0.11 | -3.04 | -6.08 to -1.82 | 69% | 61% | 36% |
| domain medqa | 98% | 85% | +0.13 | -2.80 | -5.71 to -1.61 | 43% | 38% | 35% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.78 | -2.87 to -1.12 | 64% | 52% | 35% |
| domain law, judge knows | 98% | 83% | +0.15 | -2.20 | -4.55 to -1.21 | 69% | 59% | 32% |
| domain medqa, judge knows | 99% | 83% | +0.16 | -2.08 | -3.94 to -1.22 | 45% | 38% | 30% |

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
| CW-IDK | judge does not know | 96% | 93% to 99% | 71 | 12 |
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
| CW-HW | judge flags the wrong answer as incorrect | 96% | 94% to 98% | 208 | 4 |
| CW-IDK | judge flags the wrong answer as incorrect | 90% | 87% to 93% | 207 | 12 |
| HC-IDK | judge flags the wrong answer as incorrect | 94% | 92% to 96% | 209 | 4 |
| HW-IDK | judge flags the wrong answer as incorrect | 79% | 75% to 82% | 206 | 15 |
| CC-HC | judge knows and flags the wrong answer | 99% | 98% to 100% | 172 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 172 | 0 |
| CW-CC | judge knows and flags the wrong answer | 8% | 5% to 11% | 172 | 3 |
| CW-HC | judge knows and flags the wrong answer | 34% | 28% to 40% | 171 | 5 |
| CW-HW | judge knows and flags the wrong answer | 96% | 94% to 98% | 171 | 4 |
| CW-IDK | judge knows and flags the wrong answer | 90% | 86% to 93% | 170 | 12 |
| HC-IDK | judge knows and flags the wrong answer | 96% | 93% to 98% | 172 | 4 |
| HW-IDK | judge knows and flags the wrong answer | 78% | 74% to 82% | 169 | 15 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 47% | 38% to 56% | 99 | 5 |
| CW-IDK | domain geo | 89% | 84% to 93% | 99 | 12 |
| CC-IDK | domain law | 100% | 98% to 100% | 100 | 0 |
| CW-HC | domain law | 54% | 45% to 62% | 100 | 5 |
| CW-IDK | domain law | 96% | 94% to 98% | 100 | 12 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain medqa | 48% | 40% to 56% | 100 | 5 |
| CW-IDK | domain medqa | 94% | 90% to 97% | 99 | 12 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 90 | 0 |
| CW-HC | domain geo, judge knows | 43% | 34% to 52% | 89 | 5 |
| CW-IDK | domain geo, judge knows | 88% | 83% to 93% | 89 | 12 |
| CC-IDK | domain law, judge knows | 99% | 98% to 100% | 63 | 0 |
| CW-HC | domain law, judge knows | 44% | 33% to 55% | 63 | 5 |
| CW-IDK | domain law, judge knows | 96% | 92% to 99% | 63 | 12 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 76 | 0 |
| CW-HC | domain medqa, judge knows | 40% | 31% to 49% | 76 | 5 |
| CW-IDK | domain medqa, judge knows | 93% | 89% to 97% | 75 | 12 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 93% | +0.07 | -6.42 | -9.57 to -4.62 | 97% | 91% | 50% |
| judge knows | 100% | 92% | +0.08 | -5.46 | -8.42 to -3.83 | 97% | 89% | 43% |
| judge does not know | 100% | 96% | +0.04 | -13.20 | -22.67 to -6.10 | 99% | 95% | 73% |
| judge tells the two answers apart | 100% | 90% | +0.10 | -3.92 | -5.74 to -2.79 | 96% | 86% | 34% |
| judge flags the wrong answer as incorrect | 100% | 90% | +0.10 | -4.18 | -6.14 to -2.98 | 96% | 87% | 39% |
| judge knows and flags the wrong answer | 100% | 90% | +0.10 | -3.86 | -5.80 to -2.70 | 96% | 86% | 34% |
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
| CW-CC | all | 14% | 11% to 18% | 300 | 1 |
| CW-HC | all | 22% | 18% to 26% | 300 | 0 |
| CW-HW | all | 68% | 64% to 71% | 300 | 0 |
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
| CW-CC | judge does not know | 47% | 35% to 60% | 47 | 1 |
| CW-HC | judge does not know | 63% | 51% to 74% | 47 | 0 |
| CW-HW | judge does not know | 76% | 67% to 84% | 47 | 0 |
| CW-IDK | judge does not know | 95% | 88% to 99% | 47 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 47 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 47 | 0 |
| CC-HC | judge tells the two answers apart | 95% | 93% to 97% | 241 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 241 | 0 |
| CW-CC | judge tells the two answers apart | 6% | 4% to 8% | 241 | 1 |
| CW-HC | judge tells the two answers apart | 12% | 9% to 16% | 241 | 0 |
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
| CW-HW | judge knows and flags the wrong answer | 65% | 61% to 69% | 239 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 83% | 79% to 86% | 239 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 239 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 98% | 96% to 99% | 239 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 100 | 0 |
| CW-HC | domain geo | 15% | 10% to 21% | 100 | 0 |
| CW-IDK | domain geo | 84% | 78% to 89% | 100 | 0 |
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
| judge tells the two answers apart | 100% | 82% | +0.18 | -1.80 | -2.54 to -1.32 | 64% | 53% | 12% |
| judge flags the wrong answer as incorrect | 100% | 84% | +0.16 | -2.09 | -2.91 to -1.54 | 66% | 55% | 16% |
| judge knows and flags the wrong answer | 100% | 83% | +0.17 | -1.91 | -2.68 to -1.39 | 65% | 54% | 12% |
| domain geo | 100% | 84% | +0.17 | -2.03 | -3.55 to -1.22 | 72% | 60% | 15% |
| domain law | 100% | 89% | +0.11 | -3.55 | -6.14 to -2.23 | 66% | 59% | 32% |
| domain medqa | 100% | 84% | +0.16 | -2.19 | -3.95 to -1.31 | 65% | 55% | 19% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.76 | -3.14 to -1.02 | 69% | 57% | 10% |
| domain law, judge knows | 100% | 88% | +0.12 | -3.05 | -6.00 to -1.85 | 67% | 59% | 26% |
| domain medqa, judge knows | 100% | 82% | +0.18 | -1.83 | -3.25 to -1.07 | 63% | 52% | 9% |

## openrouter/openai/gpt-5.6-terra: own closed-book accuracy 83% on 60 items

### prompt variant default (picks the first position in 53% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 60 | 0 |
| CW-CC | all | 10% | 3% to 18% | 60 | 0 |
| CW-HC | all | 11% | 4% to 18% | 60 | 0 |
| CW-IDK | all | 72% | 62% to 82% | 60 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 50 | 0 |
| CW-CC | judge knows | 4% | 0% to 9% | 50 | 0 |
| CW-HC | judge knows | 3% | 0% to 7% | 50 | 0 |
| CW-IDK | judge knows | 68% | 57% to 78% | 50 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 10 | 0 |
| CW-CC | judge does not know | 40% | 15% to 70% | 10 | 0 |
| CW-HC | judge does not know | 50% | 25% to 80% | 10 | 0 |
| CW-IDK | judge does not know | 95% | 85% to 100% | 10 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 47 | 0 |
| CW-CC | judge tells the two answers apart | 1% | 0% to 3% | 47 | 0 |
| CW-HC | judge tells the two answers apart | 1% | 0% to 3% | 47 | 0 |
| CW-IDK | judge tells the two answers apart | 65% | 53% to 76% | 47 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 54 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 6% | 1% to 12% | 54 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 5% | 1% to 10% | 54 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 69% | 59% to 80% | 54 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 48 | 0 |
| CW-CC | judge knows and flags the wrong answer | 3% | 0% to 8% | 48 | 0 |
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
| judge tells the two answers apart | 100% | 65% | +0.35 | -0.42 | -1.04 to -0.07 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 69% | +0.31 | -0.64 | -1.45 to -0.23 | - | - | - |
| judge knows and flags the wrong answer | 100% | 67% | +0.33 | -0.50 | -1.18 to -0.12 | - | - | - |
| domain geo | 100% | 65% | +0.35 | -0.43 | -1.86 to +0.09 | - | - | - |
| domain law | 100% | 88% | +0.12 | -3.00 | -19.00 to -1.00 | - | - | - |
| domain medqa | 100% | 65% | +0.35 | -0.43 | -1.50 to +0.00 | - | - | - |
| domain geo, judge knows | 100% | 61% | +0.39 | -0.29 | -1.57 to +0.14 | - | - | - |
| domain law, judge knows | 100% | 87% | +0.13 | -2.75 | -14.00 to -0.67 | - | - | - |
| domain medqa, judge knows | 100% | 59% | +0.41 | -0.21 | -1.12 to +0.15 | - | - | - |
