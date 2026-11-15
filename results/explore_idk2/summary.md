items 150 (geo, law, medqa), bootstrap draws 10000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 93.3% | 90.2% to 96.1% | 127 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 64.4% | 57.2% to 71.6% | 118 | 0.0000 | yes |
| adaption/qwen3.8-27b | 63.4% | 58.9% to 68.3% | 112 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 82.5% | 77.2% to 87.3% | 114 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 94.2% | 90.9% to 97.1% | 121 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.4% | 77.2% to 87.2% | 125 | 0.0000 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 94.3% | 91.7% to 96.7% | 150 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 69.7% | 63.1% to 75.9% | 145 | 0.0000 | yes |
| adaption/qwen3.8-27b | 67.7% | 63.7% to 72.0% | 150 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 84.3% | 80.3% to 88.3% | 150 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 95.0% | 92.3% to 97.3% | 149 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.3% | 81.0% to 89.3% | 150 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 92.2% | 88.5% to 95.8% | 96 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 68.8% | 61.7% to 75.4% | 128 | 0.0000 | yes |
| adaption/qwen3.8-27b | 67.4% | 63.4% to 71.5% | 149 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 83.7% | 79.5% to 87.8% | 144 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.9% | 89.0% to 96.2% | 105 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.5% | 78.6% to 88.0% | 133 | 0.0000 | yes |

S1g2: b above 0.5 on group 'judge tells the two answers apart', Holm at 0.05. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 91.4% | 87.4% to 95.4% | 87 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 66.0% | 58.5% to 73.1% | 106 | 0.0000 | yes |
| adaption/qwen3.8-27b | 62.8% | 56.8% to 68.9% | 74 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 81.3% | 74.6% to 87.3% | 67 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 91.9% | 87.6% to 95.7% | 93 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 82.0% | 76.6% to 86.9% | 122 | 0.0000 | yes |

## Detection (S1g)

| judge | wrong answers flagged as incorrect | correct answers accepted | unparsed |
|---|---|---|---|
| adaption/deepseek-v4-flash | 64.0% | 90.7% | 0 |
| adaption/gemma-4-31b-it | 88.7% | 78.7% | 10 |
| adaption/qwen3.8-27b | 99.3% | 49.3% | 0 |
| openrouter/anthropic/claude-haiku-5.5 | 96.0% | 46.7% | 1 |
| openrouter/mistralai/mistral-small-2603 | 70.7% | 87.3% | 0 |
| openrouter/openai/gpt-5.6-luna | 88.7% | 88.0% | 0 |

## Verify-then-compare, composed from logged verdicts (exploratory)

| judge | a | b | a with check | b with check | break-even accuracy with check | 95% CI |
|---|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 99.7% | 94.3% | 90.3% | 35.3% | 0.27 | 0.15 to 0.36 |
| adaption/gemma-4-31b-it | 98.9% | 71.2% | 80.6% | 7.9% | 0.58 | 0.53 to 0.64 |
| adaption/qwen3.8-27b | 86.7% | 67.7% | 45.0% | 0.7% | 1.11 | 0.95 to 1.35 |
| openrouter/anthropic/claude-haiku-5.5 | 99.0% | 84.2% | 46.3% | 3.4% | 1.09 | 0.92 to 1.34 |
| openrouter/mistralai/mistral-small-2603 | 100.0% | 95.0% | 87.2% | 29.5% | 0.35 | 0.26 to 0.44 |
| openrouter/openai/gpt-5.6-luna | 100.0% | 85.3% | 88.0% | 11.3% | 0.50 | 0.47 to 0.54 |

## Two-step account (S1d)

Cells 18, mean absolute error 0.249, Spearman 0.66. Mean predicted 70.6%, mean observed 45.8%.

## adaption/deepseek-v4-flash: own closed-book accuracy 85% on 150 items

### prompt variant default (picks the first position in 48% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 96% | 94% to 98% | 150 | 0 |
| CC-IDK | all | 100% | 99% to 100% | 150 | 0 |
| CC-IDK2 | all | 94% | 91% to 97% | 150 | 0 |
| CW-CC | all | 21% | 16% to 26% | 150 | 0 |
| CW-HC | all | 76% | 70% to 81% | 150 | 0 |
| CW-HW | all | 97% | 95% to 99% | 150 | 0 |
| CW-IDK | all | 94% | 92% to 97% | 150 | 0 |
| CW-IDK2 | all | 72% | 66% to 77% | 150 | 0 |
| HC-IDK | all | 97% | 95% to 99% | 150 | 1 |
| HW-IDK | all | 96% | 94% to 98% | 150 | 0 |
| CC-HC | judge knows | 96% | 94% to 98% | 127 | 0 |
| CC-IDK | judge knows | 100% | 99% to 100% | 127 | 0 |
| CC-IDK2 | judge knows | 94% | 91% to 97% | 127 | 0 |
| CW-CC | judge knows | 16% | 11% to 21% | 127 | 0 |
| CW-HC | judge knows | 72% | 66% to 78% | 127 | 0 |
| CW-HW | judge knows | 96% | 94% to 98% | 127 | 0 |
| CW-IDK | judge knows | 93% | 90% to 96% | 127 | 0 |
| CW-IDK2 | judge knows | 69% | 63% to 75% | 127 | 0 |
| HC-IDK | judge knows | 98% | 96% to 100% | 127 | 1 |
| HW-IDK | judge knows | 96% | 94% to 98% | 127 | 0 |
| CC-HC | judge does not know | 98% | 93% to 100% | 23 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 23 | 0 |
| CC-IDK2 | judge does not know | 91% | 83% to 98% | 23 | 0 |
| CW-CC | judge does not know | 46% | 33% to 59% | 23 | 0 |
| CW-HC | judge does not know | 96% | 89% to 100% | 23 | 0 |
| CW-HW | judge does not know | 98% | 93% to 100% | 23 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 23 | 0 |
| CW-IDK2 | judge does not know | 87% | 78% to 96% | 23 | 0 |
| HC-IDK | judge does not know | 93% | 87% to 100% | 23 | 1 |
| HW-IDK | judge does not know | 96% | 89% to 100% | 23 | 0 |
| CC-HC | judge tells the two answers apart | 98% | 96% to 100% | 87 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 98% to 100% | 87 | 0 |
| CC-IDK2 | judge tells the two answers apart | 97% | 94% to 99% | 87 | 0 |
| CW-CC | judge tells the two answers apart | 11% | 6% to 16% | 87 | 0 |
| CW-HC | judge tells the two answers apart | 67% | 60% to 75% | 87 | 0 |
| CW-HW | judge tells the two answers apart | 96% | 93% to 99% | 87 | 0 |
| CW-IDK | judge tells the two answers apart | 91% | 87% to 95% | 87 | 0 |
| CW-IDK2 | judge tells the two answers apart | 64% | 56% to 72% | 87 | 0 |
| HC-IDK | judge tells the two answers apart | 98% | 95% to 99% | 87 | 1 |
| HW-IDK | judge tells the two answers apart | 95% | 91% to 98% | 87 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 97% | 95% to 99% | 96 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 96 | 0 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 95% | 92% to 98% | 96 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 14% | 9% to 19% | 96 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 69% | 62% to 76% | 96 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 96% | 94% to 99% | 96 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 92% | 89% to 96% | 96 | 0 |
| CW-IDK2 | judge flags the wrong answer as incorrect | 66% | 58% to 73% | 96 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 97% | 95% to 99% | 96 | 1 |
| HW-IDK | judge flags the wrong answer as incorrect | 95% | 92% to 98% | 96 | 0 |
| CC-HC | judge knows and flags the wrong answer | 97% | 94% to 99% | 86 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 86 | 0 |
| CC-IDK2 | judge knows and flags the wrong answer | 96% | 92% to 99% | 86 | 0 |
| CW-CC | judge knows and flags the wrong answer | 10% | 6% to 16% | 86 | 0 |
| CW-HC | judge knows and flags the wrong answer | 66% | 58% to 73% | 86 | 0 |
| CW-HW | judge knows and flags the wrong answer | 96% | 93% to 99% | 86 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 91% | 87% to 95% | 86 | 0 |
| CW-IDK2 | judge knows and flags the wrong answer | 62% | 54% to 70% | 86 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 98% | 96% to 100% | 86 | 1 |
| HW-IDK | judge knows and flags the wrong answer | 95% | 91% to 98% | 86 | 0 |
| CC-IDK | domain geo | 99% | 97% to 100% | 50 | 0 |
| CW-HC | domain geo | 68% | 58% to 78% | 50 | 0 |
| CW-IDK | domain geo | 90% | 84% to 95% | 50 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain law | 77% | 67% to 86% | 50 | 0 |
| CW-IDK | domain law | 97% | 93% to 100% | 50 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain medqa | 82% | 74% to 89% | 50 | 0 |
| CW-IDK | domain medqa | 96% | 92% to 99% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 46 | 0 |
| CW-HC | domain geo, judge knows | 65% | 54% to 76% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 89% | 83% to 95% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 40 | 0 |
| CW-HC | domain law, judge knows | 74% | 62% to 85% | 40 | 0 |
| CW-IDK | domain law, judge knows | 96% | 91% to 100% | 40 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 0 |
| CW-HC | domain medqa, judge knows | 78% | 70% to 87% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 95% | 90% to 99% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 94% | +0.05 | -8.31 | -15.67 to -5.25 | 97% | 92% | 76% |
| judge knows | 100% | 93% | +0.06 | -6.88 | -13.11 to -4.29 | 96% | 90% | 72% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 98% | 98% | 96% |
| judge tells the two answers apart | 99% | 91% | +0.08 | -5.14 | -11.14 to -2.95 | 96% | 88% | 67% |
| judge flags the wrong answer as incorrect | 99% | 92% | +0.07 | -5.79 | -12.43 to -3.43 | 96% | 89% | 69% |
| judge knows and flags the wrong answer | 99% | 91% | +0.08 | -5.07 | -11.14 to -3.00 | 96% | 88% | 66% |
| domain geo | 99% | 90% | +0.09 | -4.44 | -14.33 to -2.27 | 94% | 86% | 68% |
| domain law | 100% | 97% | +0.03 | -15.67 | -24.00 to -6.14 | 97% | 94% | 77% |
| domain medqa | 100% | 96% | +0.04 | -11.50 | -24.00 to -5.25 | 99% | 95% | 82% |
| domain geo, judge knows | 99% | 89% | +0.10 | -4.00 | -13.33 to -2.00 | 93% | 84% | 65% |
| domain law, judge knows | 100% | 96% | +0.04 | -12.33 | -19.00 to -4.71 | 98% | 94% | 74% |
| domain medqa, judge knows | 100% | 95% | +0.05 | -9.25 | -19.50 to -4.13 | 99% | 94% | 78% |

## adaption/gemma-4-31b-it: own closed-book accuracy 82% on 150 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 99% to 100% | 149 | 7 |
| CC-IDK | all | 99% | 98% to 100% | 150 | 4 |
| CC-IDK2 | all | 96% | 92% to 98% | 145 | 18 |
| CW-CC | all | 10% | 5% to 14% | 147 | 13 |
| CW-HC | all | 28% | 22% to 35% | 147 | 17 |
| CW-HW | all | 90% | 85% to 94% | 98 | 124 |
| CW-IDK | all | 70% | 63% to 76% | 145 | 25 |
| CW-IDK2 | all | 45% | 38% to 52% | 144 | 27 |
| HC-IDK | all | 93% | 90% to 96% | 147 | 10 |
| HW-IDK | all | 42% | 36% to 47% | 149 | 8 |
| CC-HC | judge knows | 100% | 99% to 100% | 122 | 7 |
| CC-IDK | judge knows | 100% | 100% to 100% | 123 | 4 |
| CC-IDK2 | judge knows | 99% | 97% to 100% | 118 | 18 |
| CW-CC | judge knows | 3% | 1% to 6% | 122 | 13 |
| CW-HC | judge knows | 18% | 12% to 24% | 120 | 17 |
| CW-HW | judge knows | 88% | 82% to 93% | 73 | 124 |
| CW-IDK | judge knows | 64% | 57% to 72% | 118 | 25 |
| CW-IDK2 | judge knows | 38% | 29% to 46% | 117 | 27 |
| HC-IDK | judge knows | 99% | 97% to 100% | 120 | 10 |
| HW-IDK | judge knows | 37% | 31% to 43% | 122 | 8 |
| CC-HC | judge does not know | 100% | 100% to 100% | 27 | 7 |
| CC-IDK | judge does not know | 94% | 87% to 100% | 27 | 4 |
| CC-IDK2 | judge does not know | 81% | 67% to 94% | 27 | 18 |
| CW-CC | judge does not know | 40% | 22% to 58% | 25 | 13 |
| CW-HC | judge does not know | 74% | 61% to 87% | 27 | 17 |
| CW-HW | judge does not know | 96% | 90% to 100% | 25 | 124 |
| CW-IDK | judge does not know | 93% | 83% to 100% | 27 | 25 |
| CW-IDK2 | judge does not know | 78% | 63% to 91% | 27 | 27 |
| HC-IDK | judge does not know | 69% | 57% to 80% | 27 | 10 |
| HW-IDK | judge does not know | 63% | 50% to 76% | 27 | 8 |
| CC-HC | judge tells the two answers apart | 100% | 99% to 100% | 110 | 7 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 111 | 4 |
| CC-IDK2 | judge tells the two answers apart | 99% | 96% to 100% | 106 | 18 |
| CW-CC | judge tells the two answers apart | 3% | 0% to 6% | 108 | 13 |
| CW-HC | judge tells the two answers apart | 19% | 12% to 25% | 108 | 17 |
| CW-HW | judge tells the two answers apart | 90% | 84% to 95% | 65 | 124 |
| CW-IDK | judge tells the two answers apart | 66% | 58% to 73% | 106 | 25 |
| CW-IDK2 | judge tells the two answers apart | 38% | 30% to 47% | 106 | 27 |
| HC-IDK | judge tells the two answers apart | 98% | 95% to 100% | 108 | 10 |
| HW-IDK | judge tells the two answers apart | 36% | 30% to 42% | 110 | 8 |
| CC-HC | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 132 | 7 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 133 | 4 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 96% | 93% to 99% | 128 | 18 |
| CW-CC | judge flags the wrong answer as incorrect | 6% | 3% to 10% | 130 | 13 |
| CW-HC | judge flags the wrong answer as incorrect | 25% | 18% to 32% | 130 | 17 |
| CW-HW | judge flags the wrong answer as incorrect | 89% | 84% to 94% | 85 | 124 |
| CW-IDK | judge flags the wrong answer as incorrect | 69% | 62% to 75% | 128 | 25 |
| CW-IDK2 | judge flags the wrong answer as incorrect | 43% | 35% to 50% | 128 | 27 |
| HC-IDK | judge flags the wrong answer as incorrect | 94% | 91% to 97% | 130 | 10 |
| HW-IDK | judge flags the wrong answer as incorrect | 38% | 32% to 43% | 132 | 8 |
| CC-HC | judge knows and flags the wrong answer | 100% | 99% to 100% | 110 | 7 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 111 | 4 |
| CC-IDK2 | judge knows and flags the wrong answer | 99% | 96% to 100% | 106 | 18 |
| CW-CC | judge knows and flags the wrong answer | 1% | 0% to 3% | 110 | 13 |
| CW-HC | judge knows and flags the wrong answer | 16% | 10% to 22% | 108 | 17 |
| CW-HW | judge knows and flags the wrong answer | 88% | 81% to 94% | 65 | 124 |
| CW-IDK | judge knows and flags the wrong answer | 64% | 57% to 72% | 106 | 25 |
| CW-IDK2 | judge knows and flags the wrong answer | 36% | 28% to 45% | 106 | 27 |
| HC-IDK | judge knows and flags the wrong answer | 99% | 97% to 100% | 108 | 10 |
| HW-IDK | judge knows and flags the wrong answer | 34% | 28% to 40% | 110 | 8 |
| CC-IDK | domain geo | 98% | 95% to 100% | 50 | 4 |
| CW-HC | domain geo | 14% | 6% to 23% | 50 | 17 |
| CW-IDK | domain geo | 44% | 34% to 55% | 49 | 25 |
| CC-IDK | domain law | 99% | 97% to 100% | 50 | 4 |
| CW-HC | domain law | 34% | 23% to 47% | 48 | 17 |
| CW-IDK | domain law | 92% | 84% to 98% | 48 | 25 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 4 |
| CW-HC | domain medqa | 37% | 26% to 49% | 49 | 17 |
| CW-IDK | domain medqa | 74% | 64% to 83% | 48 | 25 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 4 |
| CW-HC | domain geo, judge knows | 10% | 3% to 17% | 46 | 17 |
| CW-IDK | domain geo, judge knows | 42% | 31% to 53% | 45 | 25 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 36 | 4 |
| CW-HC | domain law, judge knows | 16% | 6% to 26% | 34 | 17 |
| CW-IDK | domain law, judge knows | 88% | 78% to 97% | 34 | 25 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 4 |
| CW-HC | domain medqa, judge knows | 29% | 16% to 41% | 40 | 17 |
| CW-IDK | domain medqa, judge knows | 69% | 56% to 81% | 39 | 25 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 70% | +0.29 | -0.67 | -1.12 to -0.38 | 90% | 75% | 41% |
| judge knows | 100% | 64% | +0.36 | -0.40 | -0.76 to -0.16 | 88% | 68% | 29% |
| judge does not know | 94% | 93% | +0.02 | undefined | -12.50 to -2.83 | 96% | 96% | 76% |
| judge tells the two answers apart | 100% | 66% | +0.34 | -0.47 | -0.89 to -0.20 | 90% | 74% | 30% |
| judge flags the wrong answer as incorrect | 99% | 69% | +0.30 | -0.62 | -1.07 to -0.31 | 90% | 74% | 37% |
| judge knows and flags the wrong answer | 100% | 64% | +0.36 | -0.39 | -0.77 to -0.15 | 88% | 69% | 25% |
| domain geo | 98% | 44% | +0.54 | +0.11 | -0.12 to +0.26 | 83% | 48% | 26% |
| domain law | 99% | 92% | +0.07 | -5.71 | -22.00 to -2.36 | 93% | 88% | 38% |
| domain medqa | 100% | 74% | +0.26 | -0.92 | -2.20 to -0.37 | 93% | 85% | 61% |
| domain geo, judge knows | 100% | 42% | +0.58 | +0.13 | -0.07 to +0.27 | 83% | 43% | 20% |
| domain law, judge knows | 100% | 88% | +0.12 | -3.25 | -10.33 to -1.27 | 91% | 83% | 20% |
| domain medqa, judge knows | 100% | 69% | +0.31 | -0.62 | -1.60 to -0.15 | 90% | 79% | 52% |

## adaption/qwen3.8-27b: own closed-book accuracy 75% on 150 items

### prompt variant default (picks the first position in 27% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 89% | 86% to 93% | 150 | 0 |
| CC-IDK | all | 87% | 83% to 90% | 150 | 0 |
| CC-IDK2 | all | 87% | 84% to 91% | 150 | 3 |
| CW-CC | all | 23% | 18% to 28% | 150 | 3 |
| CW-HC | all | 45% | 40% to 50% | 149 | 6 |
| CW-HW | all | 70% | 66% to 74% | 150 | 4 |
| CW-IDK | all | 68% | 64% to 72% | 150 | 2 |
| CW-IDK2 | all | 61% | 57% to 64% | 150 | 7 |
| HC-IDK | all | 83% | 80% to 87% | 150 | 0 |
| HW-IDK | all | 65% | 61% to 69% | 150 | 2 |
| CC-HC | judge knows | 92% | 89% to 96% | 112 | 0 |
| CC-IDK | judge knows | 90% | 86% to 93% | 112 | 0 |
| CC-IDK2 | judge knows | 90% | 86% to 93% | 112 | 3 |
| CW-CC | judge knows | 16% | 12% to 21% | 112 | 3 |
| CW-HC | judge knows | 38% | 33% to 44% | 111 | 6 |
| CW-HW | judge knows | 70% | 65% to 75% | 112 | 4 |
| CW-IDK | judge knows | 63% | 59% to 68% | 112 | 2 |
| CW-IDK2 | judge knows | 60% | 56% to 64% | 112 | 7 |
| HC-IDK | judge knows | 87% | 83% to 91% | 112 | 0 |
| HW-IDK | judge knows | 64% | 59% to 69% | 112 | 2 |
| CC-HC | judge does not know | 80% | 72% to 88% | 38 | 0 |
| CC-IDK | judge does not know | 78% | 70% to 86% | 38 | 0 |
| CC-IDK2 | judge does not know | 80% | 72% to 88% | 38 | 3 |
| CW-CC | judge does not know | 43% | 33% to 54% | 38 | 3 |
| CW-HC | judge does not know | 63% | 54% to 72% | 38 | 6 |
| CW-HW | judge does not know | 72% | 64% to 80% | 38 | 4 |
| CW-IDK | judge does not know | 80% | 72% to 88% | 38 | 2 |
| CW-IDK2 | judge does not know | 63% | 57% to 71% | 38 | 7 |
| HC-IDK | judge does not know | 72% | 64% to 80% | 38 | 0 |
| HW-IDK | judge does not know | 67% | 59% to 75% | 38 | 2 |
| CC-HC | judge tells the two answers apart | 95% | 91% to 98% | 74 | 0 |
| CC-IDK | judge tells the two answers apart | 91% | 86% to 95% | 74 | 0 |
| CC-IDK2 | judge tells the two answers apart | 91% | 86% to 95% | 74 | 3 |
| CW-CC | judge tells the two answers apart | 12% | 7% to 17% | 74 | 3 |
| CW-HC | judge tells the two answers apart | 33% | 27% to 38% | 73 | 6 |
| CW-HW | judge tells the two answers apart | 66% | 61% to 72% | 74 | 4 |
| CW-IDK | judge tells the two answers apart | 63% | 57% to 69% | 74 | 2 |
| CW-IDK2 | judge tells the two answers apart | 57% | 53% to 62% | 74 | 7 |
| HC-IDK | judge tells the two answers apart | 89% | 84% to 94% | 74 | 0 |
| HW-IDK | judge tells the two answers apart | 59% | 53% to 65% | 74 | 2 |
| CC-HC | judge flags the wrong answer as incorrect | 89% | 86% to 92% | 149 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 87% | 83% to 90% | 149 | 0 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 88% | 84% to 91% | 149 | 3 |
| CW-CC | judge flags the wrong answer as incorrect | 23% | 18% to 28% | 149 | 3 |
| CW-HC | judge flags the wrong answer as incorrect | 44% | 40% to 49% | 148 | 6 |
| CW-HW | judge flags the wrong answer as incorrect | 70% | 66% to 75% | 149 | 4 |
| CW-IDK | judge flags the wrong answer as incorrect | 67% | 63% to 71% | 149 | 2 |
| CW-IDK2 | judge flags the wrong answer as incorrect | 60% | 57% to 64% | 149 | 7 |
| HC-IDK | judge flags the wrong answer as incorrect | 83% | 80% to 87% | 149 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 65% | 60% to 69% | 149 | 2 |
| CC-HC | judge knows and flags the wrong answer | 92% | 89% to 96% | 112 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 90% | 86% to 93% | 112 | 0 |
| CC-IDK2 | judge knows and flags the wrong answer | 90% | 86% to 93% | 112 | 3 |
| CW-CC | judge knows and flags the wrong answer | 16% | 12% to 21% | 112 | 3 |
| CW-HC | judge knows and flags the wrong answer | 38% | 33% to 44% | 111 | 6 |
| CW-HW | judge knows and flags the wrong answer | 70% | 65% to 74% | 112 | 4 |
| CW-IDK | judge knows and flags the wrong answer | 63% | 59% to 68% | 112 | 2 |
| CW-IDK2 | judge knows and flags the wrong answer | 60% | 56% to 64% | 112 | 7 |
| HC-IDK | judge knows and flags the wrong answer | 87% | 83% to 91% | 112 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 64% | 59% to 69% | 112 | 2 |
| CC-IDK | domain geo | 95% | 91% to 99% | 50 | 0 |
| CW-HC | domain geo | 39% | 30% to 48% | 50 | 6 |
| CW-IDK | domain geo | 66% | 58% to 74% | 50 | 2 |
| CC-IDK | domain law | 83% | 76% to 89% | 50 | 0 |
| CW-HC | domain law | 51% | 42% to 60% | 49 | 6 |
| CW-IDK | domain law | 71% | 64% to 78% | 50 | 2 |
| CC-IDK | domain medqa | 82% | 75% to 88% | 50 | 0 |
| CW-HC | domain medqa | 44% | 37% to 51% | 50 | 6 |
| CW-IDK | domain medqa | 66% | 60% to 73% | 50 | 2 |
| CC-IDK | domain geo, judge knows | 96% | 91% to 99% | 45 | 0 |
| CW-HC | domain geo, judge knows | 32% | 24% to 40% | 45 | 6 |
| CW-IDK | domain geo, judge knows | 62% | 54% to 70% | 45 | 2 |
| CC-IDK | domain law, judge knows | 87% | 79% to 94% | 34 | 0 |
| CW-HC | domain law, judge knows | 45% | 35% to 56% | 33 | 6 |
| CW-IDK | domain law, judge knows | 69% | 60% to 78% | 34 | 2 |
| CC-IDK | domain medqa, judge knows | 85% | 77% to 92% | 33 | 0 |
| CW-HC | domain medqa, judge knows | 39% | 30% to 48% | 33 | 6 |
| CW-IDK | domain medqa, judge knows | 59% | 53% to 67% | 33 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 87% | 68% | +0.19 | -0.93 | -1.55 to -0.57 | 70% | 57% | 45% |
| judge knows | 90% | 63% | +0.26 | -0.51 | -0.85 to -0.28 | 70% | 52% | 38% |
| judge does not know | 78% | 80% | -0.03 | undefined | -12.00 to -2.25 | 72% | 74% | 63% |
| judge tells the two answers apart | 91% | 63% | +0.28 | -0.45 | -0.88 to -0.20 | 66% | 48% | 33% |
| judge flags the wrong answer as incorrect | 87% | 67% | +0.19 | -0.91 | -1.52 to -0.56 | 71% | 57% | 44% |
| judge knows and flags the wrong answer | 90% | 63% | +0.26 | -0.51 | -0.87 to -0.28 | 70% | 52% | 38% |
| domain geo | 95% | 66% | +0.29 | -0.55 | -1.16 to -0.23 | 69% | 49% | 39% |
| domain law | 83% | 71% | +0.12 | -1.75 | -7.00 to -0.70 | 74% | 66% | 51% |
| domain medqa | 82% | 66% | +0.16 | -1.00 | -3.00 to -0.43 | 68% | 57% | 44% |
| domain geo, judge knows | 96% | 62% | +0.33 | -0.37 | -0.81 to -0.11 | 69% | 46% | 32% |
| domain law, judge knows | 87% | 69% | +0.18 | -1.08 | -4.25 to -0.36 | 71% | 59% | 45% |
| domain medqa, judge knows | 85% | 59% | +0.26 | -0.35 | -0.80 to -0.10 | 70% | 52% | 39% |

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 76% on 150 items

### prompt variant default (picks the first position in 48% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 83% | 79% to 87% | 150 | 5 |
| CC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| CC-IDK2 | all | 97% | 94% to 99% | 150 | 4 |
| CW-CC | all | 20% | 15% to 25% | 150 | 11 |
| CW-HC | all | 39% | 32% to 45% | 148 | 18 |
| CW-HW | all | 58% | 52% to 64% | 146 | 34 |
| CW-IDK | all | 84% | 80% to 88% | 150 | 5 |
| CW-IDK2 | all | 74% | 70% to 79% | 149 | 4 |
| HC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| HW-IDK | all | 94% | 91% to 96% | 150 | 3 |
| CC-HC | judge knows | 87% | 82% to 91% | 114 | 5 |
| CC-IDK | judge knows | 100% | 99% to 100% | 114 | 0 |
| CC-IDK2 | judge knows | 97% | 95% to 100% | 114 | 4 |
| CW-CC | judge knows | 14% | 10% to 20% | 114 | 11 |
| CW-HC | judge knows | 33% | 26% to 40% | 112 | 18 |
| CW-HW | judge knows | 59% | 52% to 65% | 110 | 34 |
| CW-IDK | judge knows | 82% | 77% to 87% | 114 | 5 |
| CW-IDK2 | judge knows | 71% | 66% to 76% | 113 | 4 |
| HC-IDK | judge knows | 99% | 98% to 100% | 114 | 0 |
| HW-IDK | judge knows | 93% | 90% to 96% | 114 | 3 |
| CC-HC | judge does not know | 72% | 62% to 81% | 36 | 5 |
| CC-IDK | judge does not know | 97% | 93% to 100% | 36 | 0 |
| CC-IDK2 | judge does not know | 94% | 89% to 99% | 36 | 4 |
| CW-CC | judge does not know | 38% | 25% to 50% | 36 | 11 |
| CW-HC | judge does not know | 56% | 43% to 67% | 36 | 18 |
| CW-HW | judge does not know | 57% | 47% to 67% | 36 | 34 |
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
| CC-HC | judge flags the wrong answer as incorrect | 83% | 79% to 88% | 144 | 5 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 97% | 95% to 99% | 144 | 4 |
| CW-CC | judge flags the wrong answer as incorrect | 18% | 14% to 23% | 144 | 11 |
| CW-HC | judge flags the wrong answer as incorrect | 36% | 30% to 43% | 142 | 18 |
| CW-HW | judge flags the wrong answer as incorrect | 57% | 52% to 63% | 140 | 34 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 80% to 88% | 144 | 5 |
| CW-IDK2 | judge flags the wrong answer as incorrect | 74% | 69% to 79% | 143 | 4 |
| HC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 91% to 96% | 144 | 3 |
| CC-HC | judge knows and flags the wrong answer | 87% | 82% to 91% | 111 | 5 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 111 | 0 |
| CC-IDK2 | judge knows and flags the wrong answer | 98% | 95% to 100% | 111 | 4 |
| CW-CC | judge knows and flags the wrong answer | 14% | 9% to 19% | 111 | 11 |
| CW-HC | judge knows and flags the wrong answer | 32% | 25% to 39% | 109 | 18 |
| CW-HW | judge knows and flags the wrong answer | 58% | 52% to 65% | 107 | 34 |
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
| CW-HC | domain law, judge knows | 37% | 24% to 52% | 31 | 18 |
| CW-IDK | domain law, judge knows | 84% | 74% to 94% | 31 | 5 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-HC | domain medqa, judge knows | 29% | 19% to 40% | 40 | 18 |
| CW-IDK | domain medqa, judge knows | 80% | 71% to 89% | 41 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 84% | +0.15 | -2.34 | -3.66 to -1.59 | 59% | 50% | 39% |
| judge knows | 100% | 82% | +0.17 | -1.90 | -3.07 to -1.22 | 59% | 49% | 33% |
| judge does not know | 97% | 90% | +0.07 | -5.80 | -16.00 to -2.40 | 57% | 53% | 56% |
| judge tells the two answers apart | 100% | 81% | +0.19 | -1.68 | -2.94 to -0.97 | 55% | 44% | 22% |
| judge flags the wrong answer as incorrect | 99% | 84% | +0.15 | -2.20 | -3.45 to -1.48 | 58% | 49% | 37% |
| judge knows and flags the wrong answer | 100% | 82% | +0.18 | -1.82 | -2.96 to -1.18 | 59% | 49% | 32% |
| domain geo | 100% | 84% | +0.16 | -2.12 | -4.56 to -1.17 | 64% | 54% | 40% |
| domain law | 99% | 85% | +0.14 | -2.50 | -5.25 to -1.33 | 68% | 58% | 43% |
| domain medqa | 98% | 84% | +0.14 | -2.43 | -6.67 to -1.17 | 42% | 37% | 34% |
| domain geo, judge knows | 100% | 83% | +0.17 | -2.00 | -4.25 to -1.00 | 63% | 53% | 34% |
| domain law, judge knows | 100% | 84% | +0.16 | -2.10 | -5.20 to -0.94 | 69% | 58% | 37% |
| domain medqa, judge knows | 99% | 80% | +0.18 | -1.67 | -4.13 to -0.77 | 46% | 38% | 30% |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 81% on 150 items

### prompt variant default (picks the first position in 44% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 99% to 100% | 150 | 1 |
| CC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| CC-IDK2 | all | 87% | 83% to 91% | 150 | 0 |
| CW-CC | all | 16% | 12% to 21% | 150 | 2 |
| CW-HC | all | 51% | 44% to 58% | 150 | 2 |
| CW-HW | all | 98% | 96% to 99% | 150 | 2 |
| CW-IDK | all | 95% | 92% to 97% | 149 | 7 |
| CW-IDK2 | all | 64% | 58% to 70% | 150 | 5 |
| HC-IDK | all | 94% | 91% to 96% | 149 | 2 |
| HW-IDK | all | 84% | 80% to 88% | 148 | 7 |
| CC-HC | judge knows | 100% | 99% to 100% | 122 | 1 |
| CC-IDK | judge knows | 100% | 100% to 100% | 122 | 0 |
| CC-IDK2 | judge knows | 90% | 86% to 93% | 122 | 0 |
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
| CW-IDK2 | judge does not know | 80% | 68% to 91% | 28 | 5 |
| HC-IDK | judge does not know | 89% | 82% to 96% | 28 | 2 |
| HW-IDK | judge does not know | 91% | 84% to 98% | 28 | 7 |
| CC-HC | judge tells the two answers apart | 99% | 98% to 100% | 94 | 1 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 94 | 0 |
| CC-IDK2 | judge tells the two answers apart | 88% | 83% to 93% | 94 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 4% to 12% | 94 | 2 |
| CW-HC | judge tells the two answers apart | 35% | 27% to 43% | 94 | 2 |
| CW-HW | judge tells the two answers apart | 96% | 94% to 99% | 94 | 2 |
| CW-IDK | judge tells the two answers apart | 92% | 88% to 96% | 93 | 7 |
| CW-IDK2 | judge tells the two answers apart | 55% | 47% to 62% | 94 | 5 |
| HC-IDK | judge tells the two answers apart | 95% | 92% to 98% | 94 | 2 |
| HW-IDK | judge tells the two answers apart | 80% | 74% to 85% | 93 | 7 |
| CC-HC | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 106 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 106 | 0 |
| CC-IDK2 | judge flags the wrong answer as incorrect | 86% | 81% to 91% | 106 | 0 |
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
| HW-IDK | judge knows and flags the wrong answer | 80% | 74% to 84% | 93 | 7 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 42% | 30% to 54% | 50 | 2 |
| CW-IDK | domain geo | 92% | 86% to 97% | 50 | 7 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain law | 60% | 48% to 72% | 50 | 2 |
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
| CC-IDK2 | judge does not know | 94% | 88% to 100% | 25 | 0 |
| CW-CC | judge does not know | 50% | 32% to 68% | 25 | 0 |
| CW-HC | judge does not know | 68% | 52% to 84% | 25 | 0 |
| CW-HW | judge does not know | 76% | 64% to 86% | 25 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| CW-IDK2 | judge does not know | 94% | 88% to 100% | 25 | 0 |
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
| CW-IDK2 | judge knows and flags the wrong answer | 63% | 58% to 69% | 121 | 0 |
| HC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 121 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 98% | 95% to 100% | 121 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 14% | 7% to 22% | 50 | 0 |
| CW-IDK | domain geo | 83% | 74% to 91% | 50 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain law | 33% | 23% to 43% | 50 | 0 |
| CW-IDK | domain law | 90% | 84% to 95% | 50 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain medqa | 20% | 10% to 31% | 50 | 0 |
| CW-IDK | domain medqa | 83% | 75% to 91% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-HC | domain geo, judge knows | 9% | 3% to 14% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 82% | 73% to 90% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 38 | 0 |
| CW-HC | domain law, judge knows | 25% | 16% to 36% | 38 | 0 |
| CW-IDK | domain law, judge knows | 87% | 79% to 93% | 38 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 0 |
| CW-HC | domain medqa, judge knows | 7% | 1% to 15% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 79% | 70% to 88% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 85% | +0.15 | -2.41 | -3.84 to -1.63 | 69% | 59% | 22% |
| judge knows | 100% | 82% | +0.18 | -1.84 | -2.91 to -1.19 | 68% | 56% | 13% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 76% | 76% | 68% |
| judge tells the two answers apart | 100% | 82% | +0.18 | -1.77 | -2.81 to -1.14 | 67% | 55% | 13% |
| judge flags the wrong answer as incorrect | 100% | 83% | +0.17 | -2.02 | -3.16 to -1.33 | 68% | 56% | 15% |
| judge knows and flags the wrong answer | 100% | 82% | +0.18 | -1.75 | -2.78 to -1.12 | 67% | 55% | 11% |
| domain geo | 100% | 83% | +0.17 | -1.94 | -4.56 to -0.92 | 72% | 60% | 14% |
| domain law | 100% | 90% | +0.10 | -4.00 | -9.00 to -2.12 | 64% | 58% | 33% |
| domain medqa | 100% | 83% | +0.17 | -1.94 | -4.56 to -0.92 | 71% | 59% | 20% |
| domain geo, judge knows | 100% | 82% | +0.18 | -1.71 | -4.11 to -0.84 | 70% | 57% | 9% |
| domain law, judge knows | 100% | 87% | +0.13 | -2.80 | -6.60 to -1.53 | 63% | 55% | 25% |
| domain medqa, judge knows | 100% | 79% | +0.21 | -1.41 | -3.10 to -0.64 | 70% | 55% | 7% |
