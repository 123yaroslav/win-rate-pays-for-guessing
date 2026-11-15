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
| adaption/qwen3.8-27b | 67.7% | 63.3% to 71.7% | 150 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 84.3% | 80.0% to 88.3% | 150 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 95.0% | 92.3% to 97.3% | 149 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 85.3% | 81.0% to 89.3% | 150 | 0.0000 | yes |

S1g: b above 0.5 on group 'judge flags the wrong answer as incorrect', Holm at 0.05. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 92.2% | 88.5% to 95.8% | 96 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 68.8% | 62.1% to 75.4% | 128 | 0.0000 | yes |
| adaption/qwen3.8-27b | 67.4% | 63.4% to 71.5% | 149 | 0.0000 | yes |
| openrouter/anthropic/claude-haiku-5.5 | 83.7% | 79.2% to 87.8% | 144 | 0.0000 | yes |
| openrouter/mistralai/mistral-small-2603 | 92.9% | 89.0% to 96.2% | 105 | 0.0000 | yes |
| openrouter/openai/gpt-5.6-luna | 83.5% | 78.6% to 88.0% | 133 | 0.0000 | yes |

S1g2: b above 0.5 on group 'judge tells the two answers apart', Holm at 0.05. Passed by 6 of 6 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | 91.4% | 87.4% to 95.4% | 87 | 0.0000 | yes |
| adaption/gemma-4-31b-it | 66.0% | 58.5% to 73.6% | 106 | 0.0000 | yes |
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
| openrouter/anthropic/claude-haiku-5.5 | 99.0% | 84.2% | 46.3% | 3.4% | 1.09 | 0.91 to 1.34 |
| openrouter/mistralai/mistral-small-2603 | 100.0% | 95.0% | 87.2% | 29.5% | 0.35 | 0.26 to 0.43 |
| openrouter/openai/gpt-5.6-luna | 100.0% | 85.3% | 88.0% | 11.3% | 0.50 | 0.46 to 0.54 |

## Instruction variants (Study 4 criterion)

| judge | variant | a, knows | b, knows | share of resamples with b at or above 0.5 | repaired | a, does not know | b, does not know |
|---|---|---|---|---|---|---|---|
| adaption/deepseek-v4-flash | default | 100% | 93% | 1.000 | no | 100% | 100% |
| adaption/deepseek-v4-flash | accuracy | 95% | 70% | 1.000 | no | 91% | 98% |
| adaption/deepseek-v4-flash | cot | 93% | 70% | 1.000 | no | 85% | 77% |
| adaption/deepseek-v4-flash | data | 99% | 96% | 1.000 | no | 100% | 98% |
| adaption/deepseek-v4-flash | selfcheck | 98% | 89% | 1.000 | no | 91% | 91% |
| adaption/deepseek-v4-flash | stakes | 87% | 50% | 0.525 | no | 76% | 72% |
| adaption/gemma-4-31b-it | default | 100% | 64% | 1.000 | no | 94% | 93% |
| adaption/gemma-4-31b-it | accuracy | 96% | 13% | 0.000 | yes | 54% | 44% |
| adaption/gemma-4-31b-it | cot | 97% | 22% | 0.000 | yes | 67% | 55% |
| adaption/gemma-4-31b-it | data | 100% | 63% | 1.000 | no | 94% | 88% |
| adaption/gemma-4-31b-it | selfcheck | 100% | 26% | 0.000 | yes | 63% | 67% |
| adaption/gemma-4-31b-it | stakes | 92% | 7% | 0.000 | yes | 39% | 33% |
| adaption/qwen3.8-27b | default | 90% | 63% | 1.000 | no | 78% | 80% |
| adaption/qwen3.8-27b | accuracy | 84% | 53% | 0.960 | no | 72% | 62% |
| adaption/qwen3.8-27b | cot | 100% | 43% | 0.397 | no | 100% | 100% |
| adaption/qwen3.8-27b | data | 99% | 76% | 1.000 | no | 95% | 93% |
| adaption/qwen3.8-27b | selfcheck | 96% | 57% | 1.000 | no | 66% | 72% |
| adaption/qwen3.8-27b | stakes | 74% | 51% | 0.785 | no | 67% | 62% |
| openrouter/anthropic/claude-haiku-5.5 | default | 100% | 82% | 1.000 | no | 97% | 90% |
| openrouter/anthropic/claude-haiku-5.5 | accuracy | 86% | 42% | 0.022 | no | 51% | 53% |
| openrouter/anthropic/claude-haiku-5.5 | cot | 99% | 19% | 0.000 | yes | 78% | 61% |
| openrouter/anthropic/claude-haiku-5.5 | data | 99% | 85% | 1.000 | no | 96% | 96% |
| openrouter/anthropic/claude-haiku-5.5 | selfcheck | 99% | 74% | 1.000 | no | 76% | 86% |
| openrouter/anthropic/claude-haiku-5.5 | stakes | 96% | 58% | 0.989 | no | 83% | 75% |
| openrouter/anthropic/claude-haiku-5.5 | think | 99% | 6% | 0.000 | yes | 70% | 27% |
| openrouter/mistralai/mistral-small-2603 | default | 100% | 94% | 1.000 | no | 100% | 98% |
| openrouter/mistralai/mistral-small-2603 | accuracy | 97% | 89% | 1.000 | no | 95% | 91% |
| openrouter/mistralai/mistral-small-2603 | cot | 97% | 68% | 1.000 | no | 91% | 97% |
| openrouter/mistralai/mistral-small-2603 | data | 100% | 97% | 1.000 | no | 100% | 100% |
| openrouter/mistralai/mistral-small-2603 | selfcheck | 100% | 77% | 1.000 | no | 77% | 83% |
| openrouter/mistralai/mistral-small-2603 | stakes | 98% | 72% | 1.000 | no | 91% | 88% |
| openrouter/mistralai/mistral-small-2603 | think | 100% | 93% | 1.000 | no | 100% | 100% |
| openrouter/openai/gpt-5.6-luna | default | 100% | 82% | 1.000 | no | 100% | 100% |
| openrouter/openai/gpt-5.6-luna | accuracy | 92% | 26% | 0.000 | yes | 72% | 66% |
| openrouter/openai/gpt-5.6-luna | cot | 100% | 85% | 1.000 | no | 100% | 100% |
| openrouter/openai/gpt-5.6-luna | data | 100% | 78% | 1.000 | no | 98% | 98% |
| openrouter/openai/gpt-5.6-luna | selfcheck | 99% | 77% | 1.000 | no | 90% | 100% |
| openrouter/openai/gpt-5.6-luna | stakes | 96% | 38% | 0.001 | yes | 82% | 76% |
| openrouter/openai/gpt-5.6-luna | think | 100% | 52% | 0.718 | no | 100% | 94% |

## Two-step account (S1d)

Cells 12, mean absolute error 0.305, Spearman 0.71. Mean predicted 79.5%, mean observed 49.0%.

## adaption/deepseek-v4-flash: own closed-book accuracy 85% on 150 items

### prompt variant default (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 100% to 100% | 1 | 0 |
| CC-IDK | all | 100% | 99% to 100% | 150 | 0 |
| CW-CC | all | 21% | 16% to 26% | 150 | 0 |
| CW-HC | all | 76% | 70% to 81% | 150 | 0 |
| CW-HW | all | 100% | 100% to 100% | 1 | 0 |
| CW-IDK | all | 94% | 92% to 97% | 150 | 0 |
| HC-IDK | all | 50% | 50% to 50% | 1 | 0 |
| HW-IDK | all | 100% | 100% to 100% | 1 | 0 |
| CC-IDK | judge knows | 100% | 99% to 100% | 127 | 0 |
| CW-CC | judge knows | 16% | 11% to 21% | 127 | 0 |
| CW-HC | judge knows | 72% | 66% to 78% | 127 | 0 |
| CW-IDK | judge knows | 93% | 90% to 96% | 127 | 0 |
| CC-HC | judge does not know | 100% | 100% to 100% | 1 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 23 | 0 |
| CW-CC | judge does not know | 46% | 33% to 59% | 23 | 0 |
| CW-HC | judge does not know | 96% | 89% to 100% | 23 | 0 |
| CW-HW | judge does not know | 100% | 100% to 100% | 1 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 23 | 0 |
| HC-IDK | judge does not know | 50% | 50% to 50% | 1 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 1 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 98% to 100% | 87 | 0 |
| CW-CC | judge tells the two answers apart | 11% | 6% to 16% | 87 | 0 |
| CW-HC | judge tells the two answers apart | 67% | 60% to 75% | 87 | 0 |
| CW-IDK | judge tells the two answers apart | 91% | 87% to 95% | 87 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 96 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 14% | 9% to 19% | 96 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 69% | 62% to 76% | 96 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 92% | 89% to 96% | 96 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 86 | 0 |
| CW-CC | judge knows and flags the wrong answer | 10% | 6% to 15% | 86 | 0 |
| CW-HC | judge knows and flags the wrong answer | 66% | 58% to 73% | 86 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 91% | 87% to 95% | 86 | 0 |
| CC-IDK | domain geo | 99% | 97% to 100% | 50 | 0 |
| CW-HC | domain geo | 68% | 57% to 78% | 50 | 0 |
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
| CW-HC | domain medqa, judge knows | 78% | 68% to 87% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 95% | 90% to 99% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 94% | +0.05 | -8.31 | -15.67 to -5.21 | 100% | 100% | 100% |
| judge knows | 100% | 93% | +0.06 | -6.88 | -13.11 to -4.25 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 100% |
| judge tells the two answers apart | 99% | 91% | +0.08 | -5.14 | -11.29 to -2.95 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 92% | +0.07 | -5.79 | -12.43 to -3.36 | - | - | - |
| judge knows and flags the wrong answer | 99% | 91% | +0.08 | -5.07 | -11.00 to -3.05 | - | - | - |
| domain geo | 99% | 90% | +0.09 | -4.44 | -14.33 to -2.27 | - | - | - |
| domain law | 100% | 97% | +0.03 | -15.67 | -24.00 to -6.14 | - | - | - |
| domain medqa | 100% | 96% | +0.04 | -11.50 | -24.00 to -5.25 | 100% | 100% | 100% |
| domain geo, judge knows | 99% | 89% | +0.10 | -4.00 | -12.67 to -2.00 | - | - | - |
| domain law, judge knows | 100% | 96% | +0.04 | -12.33 | -19.00 to -4.71 | - | - | - |
| domain medqa, judge knows | 100% | 95% | +0.05 | -9.25 | -19.50 to -4.13 | - | - | - |

### prompt variant accuracy (picks the first position in 43% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 95% | 92% to 97% | 150 | 0 |
| CW-IDK | all | 75% | 70% to 79% | 150 | 0 |
| CC-IDK | judge knows | 95% | 93% to 98% | 127 | 0 |
| CW-IDK | judge knows | 70% | 65% to 76% | 127 | 0 |
| CC-IDK | judge does not know | 91% | 83% to 98% | 23 | 0 |
| CW-IDK | judge does not know | 98% | 93% to 100% | 23 | 0 |
| CC-IDK | judge tells the two answers apart | 97% | 94% to 99% | 87 | 0 |
| CW-IDK | judge tells the two answers apart | 66% | 60% to 72% | 87 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 94% | 91% to 97% | 96 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 68% | 62% to 73% | 96 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 95% | 92% to 98% | 86 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 65% | 58% to 71% | 86 | 0 |
| CC-IDK | domain geo | 93% | 88% to 97% | 50 | 0 |
| CW-IDK | domain geo | 63% | 55% to 71% | 50 | 0 |
| CC-IDK | domain law | 95% | 90% to 99% | 50 | 0 |
| CW-IDK | domain law | 84% | 77% to 91% | 50 | 0 |
| CC-IDK | domain medqa | 96% | 92% to 99% | 50 | 0 |
| CW-IDK | domain medqa | 77% | 70% to 84% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 95% | 90% to 99% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 61% | 52% to 70% | 46 | 0 |
| CC-IDK | domain law, judge knows | 95% | 90% to 99% | 40 | 0 |
| CW-IDK | domain law, judge knows | 80% | 71% to 88% | 40 | 0 |
| CC-IDK | domain medqa, judge knows | 96% | 91% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 72% | 63% to 80% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 95% | 75% | +0.20 | -1.23 | -1.91 to -0.81 | - | - | - |
| judge knows | 95% | 70% | +0.25 | -0.83 | -1.29 to -0.52 | - | - | - |
| judge does not know | 91% | 98% | -0.07 | undefined | +nan to +nan | - | - | - |
| judge tells the two answers apart | 97% | 66% | +0.30 | -0.53 | -0.93 to -0.27 | - | - | - |
| judge flags the wrong answer as incorrect | 94% | 68% | +0.27 | -0.67 | -1.13 to -0.37 | - | - | - |
| judge knows and flags the wrong answer | 95% | 65% | +0.31 | -0.47 | -0.82 to -0.23 | - | - | - |
| domain geo | 93% | 63% | +0.30 | -0.43 | -0.95 to -0.13 | - | - | - |
| domain law | 95% | 84% | +0.11 | -3.09 | -9.75 to -1.47 | - | - | - |
| domain medqa | 96% | 77% | +0.19 | -1.42 | -3.20 to -0.74 | - | - | - |
| domain geo, judge knows | 95% | 61% | +0.34 | -0.32 | -0.74 to -0.05 | - | - | - |
| domain law, judge knows | 95% | 80% | +0.15 | -2.00 | -5.60 to -0.90 | - | - | - |
| domain medqa, judge knows | 96% | 72% | +0.24 | -0.90 | -1.92 to -0.41 | - | - | - |

### prompt variant cot (picks the first position in 62% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 92% | 88% to 96% | 90 | 0 |
| CW-IDK | all | 71% | 64% to 78% | 90 | 0 |
| CC-IDK | judge knows | 93% | 89% to 97% | 77 | 0 |
| CW-IDK | judge knows | 70% | 62% to 77% | 77 | 0 |
| CC-IDK | judge does not know | 85% | 73% to 96% | 13 | 0 |
| CW-IDK | judge does not know | 77% | 58% to 92% | 13 | 0 |
| CC-IDK | judge tells the two answers apart | 93% | 88% to 97% | 51 | 0 |
| CW-IDK | judge tells the two answers apart | 63% | 54% to 72% | 51 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 92% | 87% to 96% | 56 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 63% | 54% to 72% | 56 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 93% | 88% to 97% | 50 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 62% | 53% to 71% | 50 | 0 |
| CC-IDK | domain geo | 90% | 82% to 97% | 30 | 0 |
| CW-IDK | domain geo | 58% | 45% to 70% | 30 | 0 |
| CC-IDK | domain law | 90% | 82% to 97% | 30 | 0 |
| CW-IDK | domain law | 82% | 72% to 92% | 30 | 0 |
| CC-IDK | domain medqa | 95% | 88% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 73% | 62% to 85% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 91% | 84% to 98% | 28 | 0 |
| CW-IDK | domain geo, judge knows | 55% | 43% to 68% | 28 | 0 |
| CC-IDK | domain law, judge knows | 89% | 80% to 98% | 23 | 0 |
| CW-IDK | domain law, judge knows | 87% | 78% to 96% | 23 | 0 |
| CC-IDK | domain medqa, judge knows | 98% | 94% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 71% | 58% to 85% | 26 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 92% | 71% | +0.21 | -1.03 | -2.17 to -0.50 | - | - | - |
| judge knows | 93% | 70% | +0.23 | -0.89 | -1.90 to -0.40 | - | - | - |
| judge does not know | 85% | 77% | +0.08 | -3.50 | -9.00 to -0.25 | - | - | - |
| judge tells the two answers apart | 93% | 63% | +0.30 | -0.42 | -1.00 to -0.10 | - | - | - |
| judge flags the wrong answer as incorrect | 92% | 63% | +0.29 | -0.47 | -1.15 to -0.13 | - | - | - |
| judge knows and flags the wrong answer | 93% | 62% | +0.31 | -0.39 | -0.96 to -0.07 | - | - | - |
| domain geo | 90% | 58% | +0.32 | -0.26 | -1.13 to +0.08 | - | - | - |
| domain law | 90% | 82% | +0.08 | -3.80 | -11.00 to -1.00 | - | - | - |
| domain medqa | 95% | 73% | +0.22 | -1.08 | -3.60 to -0.32 | - | - | - |
| domain geo, judge knows | 91% | 55% | +0.36 | -0.15 | -0.79 to +0.15 | - | - | - |
| domain law, judge knows | 89% | 87% | +0.02 | -17.00 | -19.00 to -1.50 | - | - | - |
| domain medqa, judge knows | 98% | 71% | +0.27 | -0.79 | -2.29 to -0.19 | - | - | - |

### prompt variant data (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| CW-IDK | all | 96% | 94% to 98% | 150 | 0 |
| CC-IDK | judge knows | 99% | 98% to 100% | 127 | 0 |
| CW-IDK | judge knows | 96% | 93% to 98% | 127 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 23 | 0 |
| CW-IDK | judge does not know | 98% | 93% to 100% | 23 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 98% to 100% | 87 | 0 |
| CW-IDK | judge tells the two answers apart | 93% | 89% to 97% | 87 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 96 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 94% | 90% to 97% | 96 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 86 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 94% | 90% to 97% | 86 | 0 |
| CC-IDK | domain geo | 99% | 97% to 100% | 50 | 0 |
| CW-IDK | domain geo | 93% | 88% to 97% | 50 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain law | 99% | 97% to 100% | 50 | 0 |
| CC-IDK | domain medqa | 99% | 97% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 96% | 92% to 99% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 92% | 87% to 97% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 40 | 0 |
| CW-IDK | domain law, judge knows | 99% | 96% to 100% | 40 | 0 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 96% | 91% to 100% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 96% | +0.03 | -13.80 | -23.50 to -7.33 | - | - | - |
| judge knows | 99% | 96% | +0.04 | -12.89 | -20.00 to -6.81 | - | - | - |
| judge does not know | 100% | 98% | +0.02 | -22.00 | -22.00 to -4.75 | - | - | - |
| judge tells the two answers apart | 99% | 93% | +0.06 | -6.82 | -16.00 to -3.83 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 94% | +0.06 | -7.64 | -18.00 to -4.33 | - | - | - |
| judge knows and flags the wrong answer | 99% | 94% | +0.06 | -7.50 | -16.20 to -4.06 | - | - | - |
| domain geo | 99% | 93% | +0.06 | -7.17 | -23.00 to -3.17 | - | - | - |
| domain law | 100% | 99% | +0.01 | undefined | -24.00 to -11.50 | - | - | - |
| domain medqa | 99% | 96% | +0.03 | -15.33 | -24.00 to -5.25 | - | - | - |
| domain geo, judge knows | 99% | 92% | +0.07 | -6.50 | -21.00 to -3.00 | - | - | - |
| domain law, judge knows | 100% | 99% | +0.01 | undefined | -19.00 to -9.00 | - | - | - |
| domain medqa, judge knows | 99% | 96% | +0.02 | -19.00 | -19.50 to -4.86 | - | - | - |

### prompt variant selfcheck (picks the first position in 53% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 97% | 95% to 99% | 150 | 0 |
| CW-IDK | all | 89% | 86% to 93% | 150 | 0 |
| CC-IDK | judge knows | 98% | 97% to 100% | 127 | 0 |
| CW-IDK | judge knows | 89% | 85% to 93% | 127 | 0 |
| CC-IDK | judge does not know | 91% | 83% to 98% | 23 | 0 |
| CW-IDK | judge does not know | 91% | 83% to 98% | 23 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 87 | 0 |
| CW-IDK | judge tells the two answers apart | 90% | 85% to 94% | 87 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 96 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 90% | 85% to 94% | 96 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 86 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 90% | 85% to 94% | 86 | 0 |
| CC-IDK | domain geo | 99% | 97% to 100% | 50 | 0 |
| CW-IDK | domain geo | 91% | 84% to 96% | 50 | 0 |
| CC-IDK | domain law | 95% | 91% to 99% | 50 | 0 |
| CW-IDK | domain law | 84% | 77% to 90% | 50 | 0 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 93% | 88% to 97% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 90% | 84% to 96% | 46 | 0 |
| CC-IDK | domain law, judge knows | 95% | 90% to 99% | 40 | 0 |
| CW-IDK | domain law, judge knows | 84% | 76% to 91% | 40 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 93% | 87% to 98% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 89% | +0.08 | -4.92 | -9.69 to -3.03 | - | - | - |
| judge knows | 98% | 89% | +0.09 | -4.12 | -7.57 to -2.62 | - | - | - |
| judge does not know | 91% | 91% | +0.00 | undefined | -20.00 to -2.17 | - | - | - |
| judge tells the two answers apart | 100% | 90% | +0.10 | -3.83 | -7.70 to -2.35 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 90% | +0.09 | -4.22 | -9.00 to -2.48 | - | - | - |
| judge knows and flags the wrong answer | 100% | 90% | +0.10 | -3.78 | -6.82 to -2.31 | - | - | - |
| domain geo | 99% | 91% | +0.08 | -5.13 | -15.67 to -2.33 | - | - | - |
| domain law | 95% | 84% | +0.11 | -3.09 | -9.75 to -1.53 | - | - | - |
| domain medqa | 98% | 93% | +0.05 | -8.60 | -23.00 to -3.45 | - | - | - |
| domain geo, judge knows | 100% | 90% | +0.10 | -4.11 | -10.50 to -2.07 | - | - | - |
| domain law, judge knows | 95% | 84% | +0.11 | -3.00 | -10.33 to -1.40 | - | - | - |
| domain medqa, judge knows | 100% | 93% | +0.07 | -5.83 | -19.50 to -2.73 | - | - | - |

### prompt variant stakes (picks the first position in 43% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 85% | 81% to 90% | 150 | 0 |
| CW-IDK | all | 53% | 47% to 59% | 150 | 0 |
| CC-IDK | judge knows | 87% | 83% to 91% | 127 | 0 |
| CW-IDK | judge knows | 50% | 44% to 56% | 127 | 0 |
| CC-IDK | judge does not know | 76% | 59% to 91% | 23 | 0 |
| CW-IDK | judge does not know | 72% | 59% to 85% | 23 | 0 |
| CC-IDK | judge tells the two answers apart | 88% | 82% to 93% | 87 | 0 |
| CW-IDK | judge tells the two answers apart | 44% | 37% to 52% | 87 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 85% | 80% to 91% | 96 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 44% | 37% to 51% | 96 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 88% | 83% to 93% | 86 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 41% | 34% to 49% | 86 | 0 |
| CC-IDK | domain geo | 76% | 66% to 85% | 50 | 0 |
| CW-IDK | domain geo | 26% | 18% to 34% | 50 | 0 |
| CC-IDK | domain law | 94% | 89% to 98% | 50 | 0 |
| CW-IDK | domain law | 73% | 64% to 82% | 50 | 0 |
| CC-IDK | domain medqa | 86% | 78% to 93% | 50 | 0 |
| CW-IDK | domain medqa | 61% | 52% to 70% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 79% | 71% to 88% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 24% | 16% to 32% | 46 | 0 |
| CC-IDK | domain law, judge knows | 92% | 86% to 98% | 40 | 0 |
| CW-IDK | domain law, judge knows | 74% | 64% to 84% | 40 | 0 |
| CC-IDK | domain medqa, judge knows | 90% | 83% to 96% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 56% | 46% to 66% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 85% | 53% | +0.32 | -0.10 | -0.35 to +0.08 | - | - | - |
| judge knows | 87% | 50% | +0.37 | +0.00 | -0.21 to +0.15 | - | - | - |
| judge does not know | 76% | 72% | +0.04 | -5.00 | -13.00 to -0.38 | - | - | - |
| judge tells the two answers apart | 88% | 44% | +0.44 | +0.13 | -0.04 to +0.27 | - | - | - |
| judge flags the wrong answer as incorrect | 85% | 44% | +0.41 | +0.14 | -0.04 to +0.28 | - | - | - |
| judge knows and flags the wrong answer | 88% | 41% | +0.47 | +0.19 | +0.04 to +0.31 | - | - | - |
| domain geo | 76% | 26% | +0.50 | +0.48 | +0.35 to +0.62 | - | - | - |
| domain law | 94% | 73% | +0.21 | -1.10 | -2.82 to -0.45 | - | - | - |
| domain medqa | 86% | 61% | +0.25 | -0.44 | -1.33 to -0.04 | - | - | - |
| domain geo, judge knows | 79% | 24% | +0.55 | +0.47 | +0.35 to +0.60 | - | - | - |
| domain law, judge knows | 92% | 74% | +0.19 | -1.27 | -4.17 to -0.46 | - | - | - |
| domain medqa, judge knows | 90% | 56% | +0.34 | -0.18 | -0.67 to +0.10 | - | - | - |

## adaption/gemma-4-31b-it: own closed-book accuracy 82% on 150 items

### prompt variant default (picks the first position in 55% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 100% to 100% | 1 | 0 |
| CC-IDK | all | 99% | 98% to 100% | 150 | 4 |
| CW-CC | all | 10% | 5% to 14% | 147 | 13 |
| CW-HC | all | 28% | 22% to 35% | 147 | 17 |
| CW-HW | all | 100% | 100% to 100% | 1 | 0 |
| CW-IDK | all | 70% | 63% to 76% | 145 | 25 |
| HC-IDK | all | 100% | 100% to 100% | 1 | 0 |
| HW-IDK | all | 100% | 100% to 100% | 1 | 0 |
| CC-HC | judge knows | 100% | 100% to 100% | 1 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 123 | 4 |
| CW-CC | judge knows | 3% | 1% to 6% | 122 | 13 |
| CW-HC | judge knows | 18% | 12% to 24% | 120 | 17 |
| CW-HW | judge knows | 100% | 100% to 100% | 1 | 0 |
| CW-IDK | judge knows | 64% | 57% to 72% | 118 | 25 |
| HC-IDK | judge knows | 100% | 100% to 100% | 1 | 0 |
| HW-IDK | judge knows | 100% | 100% to 100% | 1 | 0 |
| CC-IDK | judge does not know | 94% | 89% to 100% | 27 | 4 |
| CW-CC | judge does not know | 40% | 22% to 58% | 25 | 13 |
| CW-HC | judge does not know | 74% | 61% to 87% | 27 | 17 |
| CW-IDK | judge does not know | 93% | 83% to 100% | 27 | 25 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 111 | 4 |
| CW-CC | judge tells the two answers apart | 3% | 0% to 6% | 108 | 13 |
| CW-HC | judge tells the two answers apart | 19% | 12% to 25% | 108 | 17 |
| CW-IDK | judge tells the two answers apart | 66% | 58% to 74% | 106 | 25 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 133 | 4 |
| CW-CC | judge flags the wrong answer as incorrect | 6% | 3% to 10% | 130 | 13 |
| CW-HC | judge flags the wrong answer as incorrect | 25% | 18% to 32% | 130 | 17 |
| CW-IDK | judge flags the wrong answer as incorrect | 69% | 62% to 75% | 128 | 25 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 111 | 4 |
| CW-CC | judge knows and flags the wrong answer | 1% | 0% to 3% | 110 | 13 |
| CW-HC | judge knows and flags the wrong answer | 16% | 10% to 22% | 108 | 17 |
| CW-IDK | judge knows and flags the wrong answer | 64% | 57% to 71% | 106 | 25 |
| CC-IDK | domain geo | 98% | 95% to 100% | 50 | 4 |
| CW-HC | domain geo | 14% | 6% to 23% | 50 | 17 |
| CW-IDK | domain geo | 44% | 33% to 55% | 49 | 25 |
| CC-IDK | domain law | 99% | 97% to 100% | 50 | 4 |
| CW-HC | domain law | 34% | 22% to 46% | 48 | 17 |
| CW-IDK | domain law | 92% | 84% to 98% | 48 | 25 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 4 |
| CW-HC | domain medqa | 37% | 24% to 49% | 49 | 17 |
| CW-IDK | domain medqa | 74% | 64% to 84% | 48 | 25 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 4 |
| CW-HC | domain geo, judge knows | 10% | 3% to 17% | 46 | 17 |
| CW-IDK | domain geo, judge knows | 42% | 31% to 53% | 45 | 25 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 36 | 4 |
| CW-HC | domain law, judge knows | 16% | 6% to 28% | 34 | 17 |
| CW-IDK | domain law, judge knows | 88% | 78% to 97% | 34 | 25 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 4 |
| CW-HC | domain medqa, judge knows | 29% | 16% to 41% | 40 | 17 |
| CW-IDK | domain medqa, judge knows | 69% | 56% to 81% | 39 | 25 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 70% | +0.29 | -0.67 | -1.13 to -0.37 | 100% | 100% | 100% |
| judge knows | 100% | 64% | +0.36 | -0.40 | -0.76 to -0.17 | 100% | 100% | 100% |
| judge does not know | 94% | 93% | +0.02 | undefined | -12.50 to -2.71 | - | - | - |
| judge tells the two answers apart | 100% | 66% | +0.34 | -0.47 | -0.86 to -0.20 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 69% | +0.30 | -0.62 | -1.06 to -0.31 | - | - | - |
| judge knows and flags the wrong answer | 100% | 64% | +0.36 | -0.39 | -0.77 to -0.15 | - | - | - |
| domain geo | 98% | 44% | +0.54 | +0.11 | -0.10 to +0.26 | - | - | - |
| domain law | 99% | 92% | +0.07 | -5.71 | -22.50 to -2.36 | - | - | - |
| domain medqa | 100% | 74% | +0.26 | -0.92 | -2.20 to -0.33 | 100% | 100% | 100% |
| domain geo, judge knows | 100% | 42% | +0.58 | +0.13 | -0.07 to +0.27 | - | - | - |
| domain law, judge knows | 100% | 88% | +0.12 | -3.25 | -10.33 to -1.27 | - | - | - |
| domain medqa, judge knows | 100% | 69% | +0.31 | -0.62 | -1.60 to -0.15 | 100% | 100% | 100% |

### prompt variant accuracy (picks the first position in 52% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 88% | 83% to 93% | 150 | 2 |
| CW-IDK | all | 18% | 12% to 24% | 148 | 7 |
| CC-IDK | judge knows | 96% | 92% to 99% | 123 | 2 |
| CW-IDK | judge knows | 13% | 8% to 18% | 122 | 7 |
| CC-IDK | judge does not know | 54% | 37% to 70% | 27 | 2 |
| CW-IDK | judge does not know | 44% | 27% to 62% | 26 | 7 |
| CC-IDK | judge tells the two answers apart | 98% | 95% to 100% | 111 | 2 |
| CW-IDK | judge tells the two answers apart | 11% | 6% to 16% | 109 | 7 |
| CC-IDK | judge flags the wrong answer as incorrect | 90% | 85% to 95% | 133 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 12% | 8% to 17% | 131 | 7 |
| CC-IDK | judge knows and flags the wrong answer | 96% | 93% to 99% | 111 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 9% | 5% to 14% | 110 | 7 |
| CC-IDK | domain geo | 88% | 79% to 96% | 50 | 2 |
| CW-IDK | domain geo | 9% | 3% to 17% | 49 | 7 |
| CC-IDK | domain law | 84% | 74% to 93% | 50 | 2 |
| CW-IDK | domain law | 22% | 12% to 34% | 49 | 7 |
| CC-IDK | domain medqa | 93% | 86% to 98% | 50 | 2 |
| CW-IDK | domain medqa | 23% | 13% to 34% | 50 | 7 |
| CC-IDK | domain geo, judge knows | 95% | 88% to 100% | 46 | 2 |
| CW-IDK | domain geo, judge knows | 6% | 1% to 11% | 45 | 7 |
| CC-IDK | domain law, judge knows | 97% | 92% to 100% | 36 | 2 |
| CW-IDK | domain law, judge knows | 15% | 6% to 26% | 36 | 7 |
| CC-IDK | domain medqa, judge knows | 96% | 90% to 100% | 41 | 2 |
| CW-IDK | domain medqa, judge knows | 18% | 9% to 30% | 41 | 7 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 88% | 18% | +0.70 | +0.45 | +0.40 to +0.50 | - | - | - |
| judge knows | 96% | 13% | +0.83 | +0.45 | +0.41 to +0.49 | - | - | - |
| judge does not know | 52% | 44% | +0.08 | +0.75 | -0.50 to +2.33 | - | - | - |
| judge tells the two answers apart | 98% | 11% | +0.88 | +0.45 | +0.41 to +0.48 | - | - | - |
| judge flags the wrong answer as incorrect | 90% | 12% | +0.78 | +0.49 | +0.44 to +0.53 | - | - | - |
| judge knows and flags the wrong answer | 96% | 9% | +0.88 | +0.47 | +0.44 to +0.50 | - | - | - |
| domain geo | 88% | 9% | +0.79 | +0.52 | +0.46 to +0.59 | - | - | - |
| domain law | 84% | 22% | +0.61 | +0.45 | +0.33 to +0.55 | - | - | - |
| domain medqa | 93% | 23% | +0.70 | +0.39 | +0.28 to +0.46 | - | - | - |
| domain geo, judge knows | 94% | 6% | +0.89 | +0.50 | +0.45 to +0.55 | - | - | - |
| domain law, judge knows | 97% | 15% | +0.82 | +0.42 | +0.32 to +0.50 | - | - | - |
| domain medqa, judge knows | 96% | 18% | +0.78 | +0.41 | +0.30 to +0.47 | - | - | - |

### prompt variant cot (picks the first position in 61% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 90% | 84% to 95% | 87 | 7 |
| CW-IDK | all | 30% | 22% to 37% | 86 | 12 |
| CC-IDK | judge knows | 97% | 94% to 99% | 66 | 7 |
| CW-IDK | judge knows | 22% | 15% to 30% | 66 | 12 |
| CC-IDK | judge does not know | 67% | 50% to 83% | 21 | 7 |
| CW-IDK | judge does not know | 55% | 38% to 72% | 20 | 12 |
| CC-IDK | judge tells the two answers apart | 98% | 96% to 100% | 58 | 7 |
| CW-IDK | judge tells the two answers apart | 23% | 15% to 31% | 57 | 12 |
| CC-IDK | judge flags the wrong answer as incorrect | 91% | 86% to 96% | 76 | 7 |
| CW-IDK | judge flags the wrong answer as incorrect | 27% | 20% to 35% | 75 | 12 |
| CC-IDK | judge knows and flags the wrong answer | 97% | 93% to 99% | 58 | 7 |
| CW-IDK | judge knows and flags the wrong answer | 22% | 15% to 28% | 58 | 12 |
| CC-IDK | domain geo | 87% | 75% to 95% | 30 | 7 |
| CW-IDK | domain geo | 18% | 8% to 30% | 30 | 12 |
| CC-IDK | domain law | 88% | 76% to 97% | 29 | 7 |
| CW-IDK | domain law | 48% | 34% to 62% | 29 | 12 |
| CC-IDK | domain medqa | 95% | 89% to 100% | 28 | 7 |
| CW-IDK | domain medqa | 22% | 11% to 35% | 27 | 12 |
| CC-IDK | domain geo, judge knows | 94% | 88% to 100% | 26 | 7 |
| CW-IDK | domain geo, judge knows | 13% | 6% to 21% | 26 | 12 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 19 | 7 |
| CW-IDK | domain law, judge knows | 39% | 24% to 55% | 19 | 12 |
| CC-IDK | domain medqa, judge knows | 98% | 93% to 100% | 21 | 7 |
| CW-IDK | domain medqa, judge knows | 17% | 5% to 29% | 21 | 12 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 90% | 30% | +0.60 | +0.34 | +0.24 to +0.42 | - | - | - |
| judge knows | 97% | 22% | +0.75 | +0.37 | +0.30 to +0.43 | - | - | - |
| judge does not know | 65% | 55% | +0.10 | -0.50 | -5.00 to +0.67 | - | - | - |
| judge tells the two answers apart | 98% | 23% | +0.75 | +0.36 | +0.29 to +0.42 | - | - | - |
| judge flags the wrong answer as incorrect | 91% | 27% | +0.63 | +0.36 | +0.27 to +0.43 | - | - | - |
| judge knows and flags the wrong answer | 97% | 22% | +0.75 | +0.38 | +0.31 to +0.44 | - | - | - |
| domain geo | 87% | 18% | +0.68 | +0.46 | +0.37 to +0.55 | - | - | - |
| domain law | 88% | 48% | +0.40 | +0.04 | -0.53 to +0.30 | - | - | - |
| domain medqa | 94% | 22% | +0.72 | +0.38 | +0.26 to +0.47 | - | - | - |
| domain geo, judge knows | 94% | 13% | +0.81 | +0.45 | +0.38 to +0.51 | - | - | - |
| domain law, judge knows | 100% | 39% | +0.61 | +0.17 | -0.12 to +0.34 | - | - | - |
| domain medqa, judge knows | 98% | 17% | +0.81 | +0.41 | +0.30 to +0.49 | - | - | - |

### prompt variant data (picks the first position in 54% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 99% | 97% to 100% | 150 | 0 |
| CW-IDK | all | 67% | 60% to 74% | 148 | 17 |
| CC-IDK | judge knows | 100% | 100% to 100% | 123 | 0 |
| CW-IDK | judge knows | 63% | 55% to 70% | 122 | 17 |
| CC-IDK | judge does not know | 94% | 85% to 100% | 27 | 0 |
| CW-IDK | judge does not know | 88% | 77% to 98% | 26 | 17 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 111 | 0 |
| CW-IDK | judge tells the two answers apart | 65% | 58% to 73% | 110 | 17 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 66% | 60% to 73% | 131 | 17 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 111 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 63% | 55% to 70% | 110 | 17 |
| CC-IDK | domain geo | 98% | 94% to 100% | 50 | 0 |
| CW-IDK | domain geo | 46% | 35% to 57% | 49 | 17 |
| CC-IDK | domain law | 99% | 97% to 100% | 50 | 0 |
| CW-IDK | domain law | 91% | 84% to 97% | 49 | 17 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 65% | 53% to 77% | 50 | 17 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 46% | 34% to 58% | 45 | 17 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 36 | 0 |
| CW-IDK | domain law, judge knows | 89% | 79% to 97% | 36 | 17 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 59% | 45% to 72% | 41 | 17 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 67% | +0.32 | -0.54 | -0.95 to -0.27 | - | - | - |
| judge knows | 100% | 63% | +0.37 | -0.34 | -0.67 to -0.11 | - | - | - |
| judge does not know | 94% | 88% | +0.06 | -6.67 | -12.00 to -1.56 | - | - | - |
| judge tells the two answers apart | 100% | 65% | +0.35 | -0.45 | -0.86 to -0.18 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 66% | +0.32 | -0.51 | -0.91 to -0.23 | - | - | - |
| judge knows and flags the wrong answer | 100% | 63% | +0.37 | -0.34 | -0.69 to -0.10 | - | - | - |
| domain geo | 98% | 46% | +0.52 | +0.08 | -0.17 to +0.25 | - | - | - |
| domain law | 99% | 91% | +0.08 | -5.00 | -21.00 to -2.06 | - | - | - |
| domain medqa | 100% | 65% | +0.35 | -0.43 | -1.17 to -0.06 | - | - | - |
| domain geo, judge knows | 100% | 46% | +0.54 | +0.08 | -0.18 to +0.24 | - | - | - |
| domain law, judge knows | 100% | 89% | +0.11 | -3.50 | -11.00 to -1.40 | - | - | - |
| domain medqa, judge knows | 100% | 59% | +0.41 | -0.21 | -0.78 to +0.09 | - | - | - |

### prompt variant selfcheck (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 93% | 89% to 97% | 149 | 6 |
| CW-IDK | all | 33% | 27% to 41% | 148 | 7 |
| CC-IDK | judge knows | 100% | 100% to 100% | 122 | 6 |
| CW-IDK | judge knows | 26% | 19% to 33% | 121 | 7 |
| CC-IDK | judge does not know | 63% | 46% to 80% | 27 | 6 |
| CW-IDK | judge does not know | 67% | 50% to 83% | 27 | 7 |
| CC-IDK | judge tells the two answers apart | 99% | 97% to 100% | 110 | 6 |
| CW-IDK | judge tells the two answers apart | 28% | 21% to 36% | 109 | 7 |
| CC-IDK | judge flags the wrong answer as incorrect | 94% | 91% to 98% | 132 | 6 |
| CW-IDK | judge flags the wrong answer as incorrect | 31% | 24% to 38% | 131 | 7 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 110 | 6 |
| CW-IDK | judge knows and flags the wrong answer | 24% | 17% to 31% | 109 | 7 |
| CC-IDK | domain geo | 92% | 84% to 98% | 49 | 6 |
| CW-IDK | domain geo | 5% | 1% to 11% | 49 | 7 |
| CC-IDK | domain law | 93% | 86% to 98% | 50 | 6 |
| CW-IDK | domain law | 57% | 46% to 69% | 49 | 7 |
| CC-IDK | domain medqa | 95% | 89% to 100% | 50 | 6 |
| CW-IDK | domain medqa | 38% | 26% to 51% | 50 | 7 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 45 | 6 |
| CW-IDK | domain geo, judge knows | 3% | 0% to 8% | 45 | 7 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 36 | 6 |
| CW-IDK | domain law, judge knows | 50% | 37% to 63% | 35 | 7 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 6 |
| CW-IDK | domain medqa, judge knows | 30% | 17% to 44% | 41 | 7 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 93% | 33% | +0.60 | +0.28 | +0.18 to +0.35 | - | - | - |
| judge knows | 100% | 26% | +0.74 | +0.32 | +0.25 to +0.38 | - | - | - |
| judge does not know | 63% | 67% | -0.04 | undefined | -5.50 to +0.40 | - | - | - |
| judge tells the two answers apart | 99% | 28% | +0.71 | +0.31 | +0.22 to +0.37 | - | - | - |
| judge flags the wrong answer as incorrect | 94% | 31% | +0.63 | +0.30 | +0.21 to +0.37 | - | - | - |
| judge knows and flags the wrong answer | 100% | 24% | +0.76 | +0.34 | +0.27 to +0.39 | - | - | - |
| domain geo | 92% | 5% | +0.87 | +0.52 | +0.48 to +0.57 | - | - | - |
| domain law | 93% | 57% | +0.36 | -0.20 | -0.88 to +0.09 | - | - | - |
| domain medqa | 95% | 38% | +0.57 | +0.21 | -0.02 to +0.35 | - | - | - |
| domain geo, judge knows | 100% | 3% | +0.97 | +0.48 | +0.46 to +0.50 | - | - | - |
| domain law, judge knows | 100% | 50% | +0.50 | +0.00 | -0.35 to +0.20 | - | - | - |
| domain medqa, judge knows | 100% | 30% | +0.70 | +0.28 | +0.11 to +0.39 | - | - | - |

### prompt variant stakes (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 82% | 76% to 88% | 148 | 4 |
| CW-IDK | all | 12% | 7% to 17% | 148 | 7 |
| CC-IDK | judge knows | 92% | 87% to 96% | 121 | 4 |
| CW-IDK | judge knows | 7% | 3% to 11% | 121 | 7 |
| CC-IDK | judge does not know | 39% | 24% to 56% | 27 | 4 |
| CW-IDK | judge does not know | 33% | 19% to 48% | 27 | 7 |
| CC-IDK | judge tells the two answers apart | 94% | 89% to 97% | 109 | 4 |
| CW-IDK | judge tells the two answers apart | 6% | 3% to 10% | 109 | 7 |
| CC-IDK | judge flags the wrong answer as incorrect | 84% | 77% to 89% | 131 | 4 |
| CW-IDK | judge flags the wrong answer as incorrect | 7% | 4% to 11% | 131 | 7 |
| CC-IDK | judge knows and flags the wrong answer | 92% | 87% to 96% | 109 | 4 |
| CW-IDK | judge knows and flags the wrong answer | 5% | 1% to 8% | 109 | 7 |
| CC-IDK | domain geo | 82% | 70% to 92% | 49 | 4 |
| CW-IDK | domain geo | 8% | 2% to 17% | 48 | 7 |
| CC-IDK | domain law | 78% | 66% to 87% | 49 | 4 |
| CW-IDK | domain law | 15% | 7% to 24% | 50 | 7 |
| CC-IDK | domain medqa | 87% | 78% to 95% | 50 | 4 |
| CW-IDK | domain medqa | 12% | 5% to 21% | 50 | 7 |
| CC-IDK | domain geo, judge knows | 89% | 80% to 97% | 45 | 4 |
| CW-IDK | domain geo, judge knows | 5% | 0% to 10% | 44 | 7 |
| CC-IDK | domain law, judge knows | 94% | 87% to 100% | 35 | 4 |
| CW-IDK | domain law, judge knows | 10% | 3% to 19% | 36 | 7 |
| CC-IDK | domain medqa, judge knows | 93% | 84% to 99% | 41 | 4 |
| CW-IDK | domain medqa, judge knows | 7% | 1% to 16% | 41 | 7 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 83% | 12% | +0.71 | +0.54 | +0.49 to +0.59 | - | - | - |
| judge knows | 92% | 7% | +0.85 | +0.50 | +0.46 to +0.54 | - | - | - |
| judge does not know | 39% | 33% | +0.06 | +3.00 | +0.67 to +5.50 | - | - | - |
| judge tells the two answers apart | 94% | 6% | +0.88 | +0.50 | +0.47 to +0.53 | - | - | - |
| judge flags the wrong answer as incorrect | 84% | 7% | +0.77 | +0.56 | +0.51 to +0.61 | - | - | - |
| judge knows and flags the wrong answer | 93% | 5% | +0.88 | +0.52 | +0.48 to +0.55 | - | - | - |
| domain geo | 83% | 9% | +0.74 | +0.56 | +0.49 to +0.65 | - | - | - |
| domain law | 78% | 15% | +0.62 | +0.56 | +0.47 to +0.67 | - | - | - |
| domain medqa | 87% | 12% | +0.75 | +0.51 | +0.42 to +0.59 | - | - | - |
| domain geo, judge knows | 91% | 5% | +0.86 | +0.53 | +0.47 to +0.59 | - | - | - |
| domain law, judge knows | 94% | 10% | +0.84 | +0.47 | +0.40 to +0.54 | - | - | - |
| domain medqa, judge knows | 93% | 7% | +0.85 | +0.50 | +0.44 to +0.57 | - | - | - |

## adaption/qwen3.8-27b: own closed-book accuracy 75% on 150 items

### prompt variant default (picks the first position in 28% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 50% | 50% to 50% | 1 | 0 |
| CC-IDK | all | 87% | 83% to 90% | 150 | 0 |
| CW-CC | all | 23% | 18% to 28% | 150 | 3 |
| CW-HC | all | 45% | 40% to 50% | 149 | 6 |
| CW-HW | all | 100% | 100% to 100% | 1 | 0 |
| CW-IDK | all | 68% | 63% to 72% | 150 | 2 |
| HC-IDK | all | 50% | 50% to 50% | 1 | 0 |
| CC-IDK | judge knows | 90% | 86% to 93% | 112 | 0 |
| CW-CC | judge knows | 16% | 12% to 21% | 112 | 3 |
| CW-HC | judge knows | 38% | 33% to 44% | 111 | 6 |
| CW-IDK | judge knows | 63% | 59% to 68% | 112 | 2 |
| CC-HC | judge does not know | 50% | 50% to 50% | 1 | 0 |
| CC-IDK | judge does not know | 78% | 70% to 86% | 38 | 0 |
| CW-CC | judge does not know | 43% | 33% to 54% | 38 | 3 |
| CW-HC | judge does not know | 63% | 54% to 72% | 38 | 6 |
| CW-HW | judge does not know | 100% | 100% to 100% | 1 | 0 |
| CW-IDK | judge does not know | 80% | 72% to 88% | 38 | 2 |
| HC-IDK | judge does not know | 50% | 50% to 50% | 1 | 0 |
| CC-IDK | judge tells the two answers apart | 91% | 86% to 95% | 74 | 0 |
| CW-CC | judge tells the two answers apart | 12% | 7% to 17% | 74 | 3 |
| CW-HC | judge tells the two answers apart | 33% | 27% to 38% | 73 | 6 |
| CW-IDK | judge tells the two answers apart | 63% | 57% to 69% | 74 | 2 |
| CC-HC | judge flags the wrong answer as incorrect | 50% | 50% to 50% | 1 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 87% | 83% to 90% | 149 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 23% | 18% to 28% | 149 | 3 |
| CW-HC | judge flags the wrong answer as incorrect | 44% | 39% to 49% | 148 | 6 |
| CW-HW | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 1 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 67% | 63% to 71% | 149 | 2 |
| HC-IDK | judge flags the wrong answer as incorrect | 50% | 50% to 50% | 1 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 90% | 86% to 93% | 112 | 0 |
| CW-CC | judge knows and flags the wrong answer | 16% | 12% to 21% | 112 | 3 |
| CW-HC | judge knows and flags the wrong answer | 38% | 33% to 44% | 111 | 6 |
| CW-IDK | judge knows and flags the wrong answer | 63% | 59% to 68% | 112 | 2 |
| CC-IDK | domain geo | 95% | 90% to 99% | 50 | 0 |
| CW-HC | domain geo | 39% | 30% to 48% | 50 | 6 |
| CW-IDK | domain geo | 66% | 58% to 73% | 50 | 2 |
| CC-IDK | domain law | 83% | 76% to 89% | 50 | 0 |
| CW-HC | domain law | 51% | 42% to 60% | 49 | 6 |
| CW-IDK | domain law | 71% | 63% to 78% | 50 | 2 |
| CC-IDK | domain medqa | 82% | 75% to 88% | 50 | 0 |
| CW-HC | domain medqa | 44% | 37% to 51% | 50 | 6 |
| CW-IDK | domain medqa | 66% | 60% to 72% | 50 | 2 |
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
| all | 87% | 68% | +0.19 | -0.93 | -1.57 to -0.58 | 100% | 150% | 50% |
| judge knows | 90% | 63% | +0.26 | -0.51 | -0.85 to -0.28 | - | - | - |
| judge does not know | 78% | 80% | -0.03 | undefined | -12.00 to -2.38 | 100% | 150% | 50% |
| judge tells the two answers apart | 91% | 63% | +0.28 | -0.45 | -0.87 to -0.20 | - | - | - |
| judge flags the wrong answer as incorrect | 87% | 67% | +0.19 | -0.91 | -1.55 to -0.57 | 100% | 150% | 50% |
| judge knows and flags the wrong answer | 90% | 63% | +0.26 | -0.51 | -0.86 to -0.28 | - | - | - |
| domain geo | 95% | 66% | +0.29 | -0.55 | -1.20 to -0.23 | - | - | - |
| domain law | 83% | 71% | +0.12 | -1.75 | -7.00 to -0.68 | - | - | - |
| domain medqa | 82% | 66% | +0.16 | -1.00 | -3.00 to -0.43 | 100% | 150% | 50% |
| domain geo, judge knows | 96% | 62% | +0.33 | -0.37 | -0.81 to -0.11 | - | - | - |
| domain law, judge knows | 87% | 69% | +0.18 | -1.08 | -4.25 to -0.35 | - | - | - |
| domain medqa, judge knows | 85% | 59% | +0.26 | -0.35 | -0.83 to -0.10 | - | - | - |

### prompt variant accuracy (picks the first position in 20% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 81% | 77% to 85% | 150 | 1 |
| CW-IDK | all | 55% | 52% to 59% | 150 | 2 |
| CC-IDK | judge knows | 84% | 79% to 88% | 112 | 1 |
| CW-IDK | judge knows | 53% | 50% to 57% | 112 | 2 |
| CC-IDK | judge does not know | 72% | 64% to 80% | 38 | 1 |
| CW-IDK | judge does not know | 62% | 55% to 68% | 38 | 2 |
| CC-IDK | judge tells the two answers apart | 88% | 82% to 93% | 74 | 1 |
| CW-IDK | judge tells the two answers apart | 52% | 47% to 57% | 74 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 81% | 77% to 85% | 149 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 55% | 52% to 59% | 149 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 84% | 79% to 88% | 112 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 53% | 50% to 57% | 112 | 2 |
| CC-IDK | domain geo | 85% | 78% to 91% | 50 | 1 |
| CW-IDK | domain geo | 48% | 42% to 53% | 50 | 2 |
| CC-IDK | domain law | 74% | 67% to 81% | 50 | 1 |
| CW-IDK | domain law | 61% | 56% to 67% | 50 | 2 |
| CC-IDK | domain medqa | 84% | 77% to 90% | 50 | 1 |
| CW-IDK | domain medqa | 57% | 52% to 63% | 50 | 2 |
| CC-IDK | domain geo, judge knows | 87% | 80% to 93% | 45 | 1 |
| CW-IDK | domain geo, judge knows | 47% | 41% to 52% | 45 | 2 |
| CC-IDK | domain law, judge knows | 78% | 69% to 85% | 34 | 1 |
| CW-IDK | domain law, judge knows | 65% | 57% to 72% | 34 | 2 |
| CC-IDK | domain medqa, judge knows | 86% | 79% to 94% | 33 | 1 |
| CW-IDK | domain medqa, judge knows | 50% | 45% to 55% | 33 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 81% | 55% | +0.26 | -0.21 | -0.41 to -0.07 | - | - | - |
| judge knows | 84% | 53% | +0.31 | -0.10 | -0.27 to +0.01 | - | - | - |
| judge does not know | 72% | 62% | +0.11 | -1.13 | -5.00 to -0.29 | - | - | - |
| judge tells the two answers apart | 88% | 52% | +0.36 | -0.06 | -0.22 to +0.07 | - | - | - |
| judge flags the wrong answer as incorrect | 81% | 55% | +0.26 | -0.21 | -0.42 to -0.07 | - | - | - |
| judge knows and flags the wrong answer | 84% | 53% | +0.31 | -0.10 | -0.27 to +0.01 | - | - | - |
| domain geo | 85% | 48% | +0.37 | +0.05 | -0.13 to +0.17 | - | - | - |
| domain law | 74% | 61% | +0.13 | -0.85 | -2.80 to -0.32 | - | - | - |
| domain medqa | 84% | 57% | +0.27 | -0.26 | -0.70 to -0.05 | - | - | - |
| domain geo, judge knows | 87% | 47% | +0.40 | +0.08 | -0.07 to +0.20 | - | - | - |
| domain law, judge knows | 78% | 65% | +0.13 | -1.11 | -4.67 to -0.36 | - | - | - |
| domain medqa, judge knows | 86% | 50% | +0.36 | +0.00 | -0.15 to +0.10 | - | - | - |

### prompt variant cot (picks the first position in 52% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 60 | 77 |
| CW-IDK | all | 56% | 33% to 78% | 18 | 157 |
| CC-IDK | judge knows | 100% | 100% to 100% | 50 | 77 |
| CW-IDK | judge knows | 43% | 14% to 71% | 14 | 157 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 10 | 77 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 4 | 157 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 39 | 77 |
| CW-IDK | judge tells the two answers apart | 30% | 0% to 60% | 10 | 157 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 60 | 77 |
| CW-IDK | judge flags the wrong answer as incorrect | 56% | 33% to 78% | 18 | 157 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 50 | 77 |
| CW-IDK | judge knows and flags the wrong answer | 43% | 14% to 71% | 14 | 157 |
| CC-IDK | domain geo | 100% | 100% to 100% | 25 | 77 |
| CW-IDK | domain geo | 46% | 23% to 77% | 13 | 157 |
| CC-IDK | domain law | 100% | 100% to 100% | 11 | 77 |
| CW-IDK | domain law | 75% | 25% to 100% | 4 | 157 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 24 | 77 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 1 | 157 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 24 | 77 |
| CW-IDK | domain geo, judge knows | 36% | 9% to 64% | 11 | 157 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 9 | 77 |
| CW-IDK | domain law, judge knows | 50% | 0% to 100% | 2 | 157 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 17 | 77 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 1 | 157 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 43% | +0.57 | +0.13 | -0.75 to +0.36 | - | - | - |
| judge knows | 100% | 38% | +0.62 | +0.19 | -0.62 to +0.41 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge tells the two answers apart | 100% | 22% | +0.78 | +0.36 | -0.13 to +0.50 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 43% | +0.57 | +0.13 | -0.75 to +0.36 | - | - | - |
| judge knows and flags the wrong answer | 100% | 38% | +0.62 | +0.19 | -0.62 to +0.41 | - | - | - |
| domain geo | 100% | 42% | +0.58 | +0.14 | -0.50 to +0.40 | - | - | - |
| domain law | 100% | 0% | +1.00 | +0.50 | +0.50 to +0.50 | - | - | - |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo, judge knows | 100% | 36% | +0.64 | +0.21 | -0.37 to +0.45 | - | - | - |
| domain law, judge knows | 100% | 0% | +1.00 | +0.50 | +0.50 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |

### prompt variant data (picks the first position in 52% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 98% | 96% to 99% | 150 | 0 |
| CW-IDK | all | 80% | 76% to 85% | 150 | 0 |
| CC-IDK | judge knows | 99% | 98% to 100% | 112 | 0 |
| CW-IDK | judge knows | 76% | 70% to 82% | 112 | 0 |
| CC-IDK | judge does not know | 95% | 89% to 99% | 38 | 0 |
| CW-IDK | judge does not know | 93% | 88% to 99% | 38 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 98% to 100% | 74 | 0 |
| CW-IDK | judge tells the two answers apart | 73% | 66% to 80% | 74 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 98% | 96% to 99% | 149 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 80% | 76% to 85% | 149 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 112 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 76% | 70% to 82% | 112 | 0 |
| CC-IDK | domain geo | 98% | 95% to 100% | 50 | 0 |
| CW-IDK | domain geo | 65% | 55% to 74% | 50 | 0 |
| CC-IDK | domain law | 96% | 92% to 99% | 50 | 0 |
| CW-IDK | domain law | 92% | 87% to 97% | 50 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 84% | 77% to 90% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 45 | 0 |
| CW-IDK | domain geo, judge knows | 63% | 52% to 73% | 45 | 0 |
| CC-IDK | domain law, judge knows | 97% | 93% to 100% | 34 | 0 |
| CW-IDK | domain law, judge knows | 88% | 81% to 96% | 34 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 33 | 0 |
| CW-IDK | domain medqa, judge knows | 80% | 71% to 88% | 33 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 80% | +0.18 | -1.72 | -2.69 to -1.14 | - | - | - |
| judge knows | 99% | 76% | +0.23 | -1.12 | -1.77 to -0.69 | - | - | - |
| judge does not know | 95% | 93% | +0.01 | undefined | -17.50 to -4.14 | - | - | - |
| judge tells the two answers apart | 99% | 73% | +0.26 | -0.87 | -1.57 to -0.45 | - | - | - |
| judge flags the wrong answer as incorrect | 98% | 80% | +0.18 | -1.70 | -2.68 to -1.12 | - | - | - |
| judge knows and flags the wrong answer | 99% | 76% | +0.23 | -1.12 | -1.79 to -0.69 | - | - | - |
| domain geo | 98% | 65% | +0.33 | -0.45 | -1.05 to -0.12 | - | - | - |
| domain law | 96% | 92% | +0.04 | -10.50 | -22.50 to -3.45 | - | - | - |
| domain medqa | 100% | 84% | +0.16 | -2.12 | -4.00 to -1.17 | - | - | - |
| domain geo, judge knows | 100% | 63% | +0.37 | -0.36 | -0.87 to -0.07 | - | - | - |
| domain law, judge knows | 97% | 88% | +0.09 | -4.33 | -14.50 to -1.91 | - | - | - |
| domain medqa, judge knows | 100% | 80% | +0.20 | -1.54 | -3.12 to -0.83 | - | - | - |

### prompt variant selfcheck (picks the first position in 26% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 89% | 85% to 92% | 149 | 7 |
| CW-IDK | all | 61% | 57% to 65% | 149 | 12 |
| CC-IDK | judge knows | 96% | 93% to 98% | 112 | 7 |
| CW-IDK | judge knows | 57% | 53% to 61% | 111 | 12 |
| CC-IDK | judge does not know | 66% | 58% to 74% | 37 | 7 |
| CW-IDK | judge does not know | 72% | 64% to 82% | 38 | 12 |
| CC-IDK | judge tells the two answers apart | 96% | 93% to 99% | 74 | 7 |
| CW-IDK | judge tells the two answers apart | 57% | 52% to 61% | 74 | 12 |
| CC-IDK | judge flags the wrong answer as incorrect | 89% | 85% to 92% | 148 | 7 |
| CW-IDK | judge flags the wrong answer as incorrect | 61% | 57% to 65% | 148 | 12 |
| CC-IDK | judge knows and flags the wrong answer | 96% | 93% to 98% | 112 | 7 |
| CW-IDK | judge knows and flags the wrong answer | 57% | 53% to 61% | 111 | 12 |
| CC-IDK | domain geo | 94% | 89% to 98% | 50 | 7 |
| CW-IDK | domain geo | 58% | 53% to 64% | 49 | 12 |
| CC-IDK | domain law | 86% | 80% to 92% | 49 | 7 |
| CW-IDK | domain law | 63% | 56% to 70% | 50 | 12 |
| CC-IDK | domain medqa | 86% | 79% to 92% | 50 | 7 |
| CW-IDK | domain medqa | 62% | 55% to 69% | 50 | 12 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 45 | 7 |
| CW-IDK | domain geo, judge knows | 56% | 50% to 61% | 44 | 12 |
| CC-IDK | domain law, judge knows | 96% | 91% to 100% | 34 | 7 |
| CW-IDK | domain law, judge knows | 60% | 53% to 68% | 34 | 12 |
| CC-IDK | domain medqa, judge knows | 92% | 86% to 98% | 33 | 7 |
| CW-IDK | domain medqa, judge knows | 56% | 48% to 64% | 33 | 12 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 89% | 61% | +0.27 | -0.41 | -0.68 to -0.23 | - | - | - |
| judge knows | 96% | 57% | +0.39 | -0.19 | -0.33 to -0.07 | - | - | - |
| judge does not know | 66% | 73% | -0.07 | undefined | -8.50 to -1.17 | - | - | - |
| judge tells the two answers apart | 96% | 57% | +0.39 | -0.17 | -0.35 to -0.04 | - | - | - |
| judge flags the wrong answer as incorrect | 89% | 61% | +0.28 | -0.39 | -0.65 to -0.21 | - | - | - |
| judge knows and flags the wrong answer | 96% | 57% | +0.39 | -0.19 | -0.33 to -0.07 | - | - | - |
| domain geo | 94% | 58% | +0.36 | -0.23 | -0.52 to -0.05 | - | - | - |
| domain law | 86% | 63% | +0.22 | -0.59 | -1.54 to -0.19 | - | - | - |
| domain medqa | 86% | 62% | +0.24 | -0.50 | -1.42 to -0.16 | - | - | - |
| domain geo, judge knows | 99% | 56% | +0.43 | -0.13 | -0.30 to +0.00 | - | - | - |
| domain law, judge knows | 96% | 60% | +0.35 | -0.29 | -0.71 to -0.06 | - | - | - |
| domain medqa, judge knows | 92% | 56% | +0.36 | -0.17 | -0.53 to +0.04 | - | - | - |

### prompt variant stakes (picks the first position in 13% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 72% | 68% to 76% | 150 | 5 |
| CW-IDK | all | 54% | 51% to 57% | 150 | 2 |
| CC-IDK | judge knows | 74% | 69% to 78% | 112 | 5 |
| CW-IDK | judge knows | 51% | 48% to 54% | 112 | 2 |
| CC-IDK | judge does not know | 67% | 59% to 75% | 38 | 5 |
| CW-IDK | judge does not know | 62% | 55% to 68% | 38 | 2 |
| CC-IDK | judge tells the two answers apart | 78% | 72% to 84% | 74 | 5 |
| CW-IDK | judge tells the two answers apart | 51% | 47% to 54% | 74 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 72% | 68% to 76% | 149 | 5 |
| CW-IDK | judge flags the wrong answer as incorrect | 54% | 51% to 56% | 149 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 74% | 69% to 79% | 112 | 5 |
| CW-IDK | judge knows and flags the wrong answer | 51% | 48% to 54% | 112 | 2 |
| CC-IDK | domain geo | 75% | 68% to 82% | 50 | 5 |
| CW-IDK | domain geo | 53% | 49% to 58% | 50 | 2 |
| CC-IDK | domain law | 69% | 62% to 76% | 50 | 5 |
| CW-IDK | domain law | 57% | 52% to 63% | 50 | 2 |
| CC-IDK | domain medqa | 72% | 65% to 79% | 50 | 5 |
| CW-IDK | domain medqa | 51% | 47% to 55% | 50 | 2 |
| CC-IDK | domain geo, judge knows | 77% | 69% to 83% | 45 | 5 |
| CW-IDK | domain geo, judge knows | 51% | 48% to 56% | 45 | 2 |
| CC-IDK | domain law, judge knows | 74% | 65% to 82% | 34 | 5 |
| CW-IDK | domain law, judge knows | 53% | 47% to 59% | 34 | 2 |
| CC-IDK | domain medqa, judge knows | 70% | 62% to 79% | 33 | 5 |
| CW-IDK | domain medqa, judge knows | 48% | 44% to 53% | 33 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 72% | 54% | +0.18 | -0.20 | -0.45 to -0.04 | - | - | - |
| judge knows | 74% | 51% | +0.23 | -0.04 | -0.19 to +0.07 | - | - | - |
| judge does not know | 67% | 62% | +0.05 | -2.25 | -6.00 to -0.40 | - | - | - |
| judge tells the two answers apart | 78% | 51% | +0.28 | -0.02 | -0.18 to +0.09 | - | - | - |
| judge flags the wrong answer as incorrect | 72% | 54% | +0.18 | -0.20 | -0.44 to -0.05 | - | - | - |
| judge knows and flags the wrong answer | 74% | 51% | +0.23 | -0.04 | -0.19 to +0.07 | - | - | - |
| domain geo | 75% | 53% | +0.22 | -0.14 | -0.47 to +0.04 | - | - | - |
| domain law | 69% | 57% | +0.12 | -0.58 | -2.40 to -0.10 | - | - | - |
| domain medqa | 72% | 51% | +0.21 | -0.05 | -0.38 to +0.13 | - | - | - |
| domain geo, judge knows | 77% | 51% | +0.26 | -0.04 | -0.25 to +0.08 | - | - | - |
| domain law, judge knows | 74% | 53% | +0.21 | -0.14 | -0.60 to +0.11 | - | - | - |
| domain medqa, judge knows | 70% | 48% | +0.21 | +0.07 | -0.29 to +0.25 | - | - | - |

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 76% on 150 items

### prompt variant default (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 83% | 79% to 87% | 150 | 5 |
| CC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| CW-CC | all | 20% | 15% to 25% | 150 | 11 |
| CW-HC | all | 39% | 32% to 45% | 148 | 18 |
| CW-HW | all | 58% | 53% to 64% | 146 | 34 |
| CW-IDK | all | 84% | 80% to 88% | 150 | 5 |
| HC-IDK | all | 99% | 98% to 100% | 150 | 0 |
| HW-IDK | all | 94% | 91% to 96% | 150 | 3 |
| CC-HC | judge knows | 87% | 82% to 91% | 114 | 5 |
| CC-IDK | judge knows | 100% | 99% to 100% | 114 | 0 |
| CW-CC | judge knows | 14% | 10% to 19% | 114 | 11 |
| CW-HC | judge knows | 33% | 26% to 40% | 112 | 18 |
| CW-HW | judge knows | 59% | 52% to 65% | 110 | 34 |
| CW-IDK | judge knows | 82% | 77% to 87% | 114 | 5 |
| HC-IDK | judge knows | 99% | 98% to 100% | 114 | 0 |
| HW-IDK | judge knows | 93% | 90% to 96% | 114 | 3 |
| CC-HC | judge does not know | 72% | 62% to 81% | 36 | 5 |
| CC-IDK | judge does not know | 97% | 93% to 100% | 36 | 0 |
| CW-CC | judge does not know | 38% | 25% to 50% | 36 | 11 |
| CW-HC | judge does not know | 56% | 43% to 68% | 36 | 18 |
| CW-HW | judge does not know | 57% | 47% to 67% | 36 | 34 |
| CW-IDK | judge does not know | 90% | 83% to 96% | 36 | 5 |
| HC-IDK | judge does not know | 99% | 96% to 100% | 36 | 0 |
| HW-IDK | judge does not know | 94% | 89% to 99% | 36 | 3 |
| CC-HC | judge tells the two answers apart | 90% | 84% to 94% | 67 | 5 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 67 | 0 |
| CW-CC | judge tells the two answers apart | 10% | 4% to 16% | 67 | 11 |
| CW-HC | judge tells the two answers apart | 22% | 14% to 30% | 66 | 18 |
| CW-HW | judge tells the two answers apart | 54% | 45% to 62% | 65 | 34 |
| CW-IDK | judge tells the two answers apart | 81% | 75% to 87% | 67 | 5 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 67 | 0 |
| HW-IDK | judge tells the two answers apart | 95% | 91% to 98% | 67 | 3 |
| CC-HC | judge flags the wrong answer as incorrect | 83% | 79% to 88% | 144 | 5 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 18% | 14% to 23% | 144 | 11 |
| CW-HC | judge flags the wrong answer as incorrect | 36% | 30% to 43% | 142 | 18 |
| CW-HW | judge flags the wrong answer as incorrect | 57% | 52% to 63% | 140 | 34 |
| CW-IDK | judge flags the wrong answer as incorrect | 84% | 79% to 88% | 144 | 5 |
| HC-IDK | judge flags the wrong answer as incorrect | 99% | 98% to 100% | 144 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 93% | 91% to 96% | 144 | 3 |
| CC-HC | judge knows and flags the wrong answer | 87% | 82% to 91% | 111 | 5 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 99% to 100% | 111 | 0 |
| CW-CC | judge knows and flags the wrong answer | 14% | 9% to 19% | 111 | 11 |
| CW-HC | judge knows and flags the wrong answer | 32% | 25% to 39% | 109 | 18 |
| CW-HW | judge knows and flags the wrong answer | 58% | 52% to 65% | 107 | 34 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 77% to 87% | 111 | 5 |
| HC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 111 | 0 |
| HW-IDK | judge knows and flags the wrong answer | 93% | 90% to 96% | 111 | 3 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-HC | domain geo | 40% | 29% to 51% | 49 | 18 |
| CW-IDK | domain geo | 84% | 77% to 91% | 50 | 5 |
| CC-IDK | domain law | 99% | 97% to 100% | 50 | 0 |
| CW-HC | domain law | 43% | 32% to 54% | 50 | 18 |
| CW-IDK | domain law | 85% | 78% to 92% | 50 | 5 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 0 |
| CW-HC | domain medqa | 33% | 23% to 43% | 49 | 18 |
| CW-IDK | domain medqa | 84% | 76% to 91% | 50 | 5 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 42 | 0 |
| CW-HC | domain geo, judge knows | 34% | 22% to 46% | 41 | 18 |
| CW-IDK | domain geo, judge knows | 83% | 75% to 90% | 42 | 5 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 31 | 0 |
| CW-HC | domain law, judge knows | 37% | 24% to 52% | 31 | 18 |
| CW-IDK | domain law, judge knows | 84% | 74% to 92% | 31 | 5 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-HC | domain medqa, judge knows | 29% | 18% to 40% | 40 | 18 |
| CW-IDK | domain medqa, judge knows | 80% | 71% to 89% | 41 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 99% | 84% | +0.15 | -2.34 | -3.63 to -1.59 | 59% | 50% | 39% |
| judge knows | 100% | 82% | +0.17 | -1.90 | -3.04 to -1.24 | 59% | 49% | 33% |
| judge does not know | 97% | 90% | +0.07 | -5.80 | -16.00 to -2.40 | 57% | 53% | 56% |
| judge tells the two answers apart | 100% | 81% | +0.19 | -1.68 | -2.94 to -0.97 | 55% | 44% | 22% |
| judge flags the wrong answer as incorrect | 99% | 84% | +0.15 | -2.20 | -3.45 to -1.49 | 58% | 49% | 37% |
| judge knows and flags the wrong answer | 100% | 82% | +0.18 | -1.82 | -2.96 to -1.18 | 59% | 49% | 32% |
| domain geo | 100% | 84% | +0.16 | -2.12 | -4.56 to -1.17 | 64% | 54% | 40% |
| domain law | 99% | 85% | +0.14 | -2.50 | -5.71 to -1.33 | 68% | 58% | 43% |
| domain medqa | 98% | 84% | +0.14 | -2.43 | -6.83 to -1.17 | 42% | 37% | 34% |
| domain geo, judge knows | 100% | 83% | +0.17 | -2.00 | -4.25 to -1.00 | 63% | 53% | 34% |
| domain law, judge knows | 100% | 84% | +0.16 | -2.10 | -5.20 to -0.94 | 69% | 58% | 37% |
| domain medqa, judge knows | 99% | 80% | +0.18 | -1.67 | -4.43 to -0.78 | 46% | 38% | 30% |

### prompt variant accuracy (picks the first position in 47% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 78% | 72% to 84% | 149 | 11 |
| CW-IDK | all | 45% | 38% to 51% | 142 | 34 |
| CC-IDK | judge knows | 86% | 81% to 91% | 114 | 11 |
| CW-IDK | judge knows | 42% | 34% to 50% | 106 | 34 |
| CC-IDK | judge does not know | 51% | 39% to 64% | 35 | 11 |
| CW-IDK | judge does not know | 53% | 40% to 65% | 36 | 34 |
| CC-IDK | judge tells the two answers apart | 95% | 90% to 99% | 67 | 11 |
| CW-IDK | judge tells the two answers apart | 44% | 34% to 53% | 63 | 34 |
| CC-IDK | judge flags the wrong answer as incorrect | 79% | 73% to 84% | 143 | 11 |
| CW-IDK | judge flags the wrong answer as incorrect | 43% | 36% to 50% | 136 | 34 |
| CC-IDK | judge knows and flags the wrong answer | 87% | 82% to 92% | 111 | 11 |
| CW-IDK | judge knows and flags the wrong answer | 41% | 33% to 49% | 103 | 34 |
| CC-IDK | domain geo | 85% | 76% to 93% | 50 | 11 |
| CW-IDK | domain geo | 41% | 29% to 52% | 48 | 34 |
| CC-IDK | domain law | 65% | 55% to 75% | 50 | 11 |
| CW-IDK | domain law | 46% | 35% to 57% | 50 | 34 |
| CC-IDK | domain medqa | 85% | 76% to 93% | 49 | 11 |
| CW-IDK | domain medqa | 48% | 36% to 59% | 44 | 34 |
| CC-IDK | domain geo, judge knows | 94% | 87% to 100% | 42 | 11 |
| CW-IDK | domain geo, judge knows | 38% | 25% to 51% | 40 | 34 |
| CC-IDK | domain law, judge knows | 73% | 60% to 84% | 31 | 11 |
| CW-IDK | domain law, judge knows | 45% | 32% to 58% | 31 | 34 |
| CC-IDK | domain medqa, judge knows | 89% | 80% to 96% | 41 | 11 |
| CW-IDK | domain medqa, judge knows | 44% | 31% to 57% | 35 | 34 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 78% | 44% | +0.33 | +0.17 | -0.03 to +0.31 | - | - | - |
| judge knows | 86% | 42% | +0.44 | +0.18 | +0.00 to +0.30 | - | - | - |
| judge does not know | 51% | 51% | +0.00 | undefined | -1.75 to +2.00 | - | - | - |
| judge tells the two answers apart | 94% | 44% | +0.51 | +0.12 | -0.08 to +0.26 | - | - | - |
| judge flags the wrong answer as incorrect | 78% | 43% | +0.36 | +0.21 | +0.03 to +0.34 | - | - | - |
| judge knows and flags the wrong answer | 87% | 41% | +0.46 | +0.19 | +0.03 to +0.31 | - | - | - |
| domain geo | 86% | 41% | +0.46 | +0.20 | -0.07 to +0.38 | - | - | - |
| domain law | 65% | 46% | +0.19 | +0.21 | -0.90 to +0.57 | - | - | - |
| domain medqa | 83% | 47% | +0.36 | +0.10 | -0.39 to +0.33 | - | - | - |
| domain geo, judge knows | 96% | 38% | +0.59 | +0.21 | +0.00 to +0.36 | - | - | - |
| domain law, judge knows | 73% | 45% | +0.27 | +0.18 | -0.71 to +0.50 | - | - | - |
| domain medqa, judge knows | 87% | 44% | +0.43 | +0.13 | -0.27 to +0.33 | - | - | - |

### prompt variant cot (picks the first position in 46% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 89% to 98% | 88 | 20 |
| CW-IDK | all | 29% | 19% to 39% | 80 | 42 |
| CC-IDK | judge knows | 99% | 96% to 100% | 68 | 20 |
| CW-IDK | judge knows | 19% | 10% to 29% | 62 | 42 |
| CC-IDK | judge does not know | 78% | 60% to 95% | 20 | 20 |
| CW-IDK | judge does not know | 61% | 42% to 81% | 18 | 42 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 36 | 20 |
| CW-IDK | judge tells the two answers apart | 12% | 3% to 24% | 33 | 42 |
| CC-IDK | judge flags the wrong answer as incorrect | 95% | 90% to 99% | 85 | 20 |
| CW-IDK | judge flags the wrong answer as incorrect | 27% | 18% to 37% | 77 | 42 |
| CC-IDK | judge knows and flags the wrong answer | 98% | 96% to 100% | 66 | 20 |
| CW-IDK | judge knows and flags the wrong answer | 18% | 8% to 28% | 60 | 42 |
| CC-IDK | domain geo | 92% | 82% to 100% | 30 | 20 |
| CW-IDK | domain geo | 17% | 5% to 31% | 29 | 42 |
| CC-IDK | domain law | 90% | 80% to 98% | 30 | 20 |
| CW-IDK | domain law | 42% | 25% to 60% | 26 | 42 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 28 | 20 |
| CW-IDK | domain medqa | 28% | 12% to 48% | 25 | 42 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 24 | 20 |
| CW-IDK | domain geo, judge knows | 12% | 0% to 25% | 24 | 42 |
| CC-IDK | domain law, judge knows | 95% | 87% to 100% | 19 | 20 |
| CW-IDK | domain law, judge knows | 25% | 6% to 50% | 16 | 42 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 25 | 20 |
| CW-IDK | domain medqa, judge knows | 23% | 9% to 41% | 22 | 42 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 93% | 28% | +0.65 | +0.34 | +0.23 to +0.42 | - | - | - |
| judge knows | 98% | 19% | +0.79 | +0.39 | +0.30 to +0.45 | - | - | - |
| judge does not know | 74% | 59% | +0.15 | -0.60 | -6.00 to +0.40 | - | - | - |
| judge tells the two answers apart | 100% | 12% | +0.88 | +0.43 | +0.34 to +0.48 | - | - | - |
| judge flags the wrong answer as incorrect | 94% | 26% | +0.68 | +0.35 | +0.24 to +0.43 | - | - | - |
| judge knows and flags the wrong answer | 98% | 18% | +0.80 | +0.40 | +0.31 to +0.46 | - | - | - |
| domain geo | 91% | 17% | +0.74 | +0.44 | +0.31 to +0.54 | - | - | - |
| domain law | 88% | 42% | +0.46 | +0.17 | -0.42 to +0.40 | - | - | - |
| domain medqa | 100% | 25% | +0.75 | +0.33 | +0.14 to +0.45 | - | - | - |
| domain geo, judge knows | 100% | 12% | +0.88 | +0.43 | +0.33 to +0.50 | - | - | - |
| domain law, judge knows | 94% | 25% | +0.69 | +0.36 | +0.00 to +0.52 | - | - | - |
| domain medqa, judge knows | 100% | 23% | +0.77 | +0.35 | +0.15 to +0.48 | - | - | - |

### prompt variant data (picks the first position in 52% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 98% | 97% to 100% | 150 | 1 |
| CW-IDK | all | 88% | 84% to 91% | 150 | 1 |
| CC-IDK | judge knows | 99% | 98% to 100% | 114 | 1 |
| CW-IDK | judge knows | 85% | 80% to 90% | 114 | 1 |
| CC-IDK | judge does not know | 96% | 90% to 100% | 36 | 1 |
| CW-IDK | judge does not know | 96% | 90% to 100% | 36 | 1 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 67 | 1 |
| CW-IDK | judge tells the two answers apart | 81% | 73% to 87% | 67 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 99% | 97% to 100% | 144 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 87% | 83% to 91% | 144 | 1 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 111 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 85% | 80% to 90% | 111 | 1 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain geo | 85% | 76% to 93% | 50 | 1 |
| CC-IDK | domain law | 97% | 93% to 100% | 50 | 1 |
| CW-IDK | domain law | 94% | 88% to 99% | 50 | 1 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 1 |
| CW-IDK | domain medqa | 84% | 77% to 90% | 50 | 1 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 42 | 1 |
| CW-IDK | domain geo, judge knows | 83% | 74% to 92% | 42 | 1 |
| CC-IDK | domain law, judge knows | 98% | 95% to 100% | 31 | 1 |
| CW-IDK | domain law, judge knows | 90% | 81% to 98% | 31 | 1 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 1 |
| CW-IDK | domain medqa, judge knows | 83% | 76% to 90% | 41 | 1 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 88% | +0.11 | -3.53 | -6.25 to -2.24 | - | - | - |
| judge knows | 99% | 85% | +0.14 | -2.50 | -4.33 to -1.55 | - | - | - |
| judge does not know | 96% | 96% | +0.00 | undefined | -17.00 to -4.83 | - | - | - |
| judge tells the two answers apart | 100% | 81% | +0.19 | -1.58 | -2.94 to -0.86 | - | - | - |
| judge flags the wrong answer as incorrect | 99% | 87% | +0.11 | -3.24 | -5.80 to -2.07 | - | - | - |
| judge knows and flags the wrong answer | 99% | 85% | +0.14 | -2.41 | -4.19 to -1.50 | - | - | - |
| domain geo | 100% | 85% | +0.15 | -2.33 | -5.25 to -1.17 | - | - | - |
| domain law | 97% | 94% | +0.03 | -14.67 | -23.00 to -3.45 | - | - | - |
| domain medqa | 98% | 84% | +0.14 | -2.43 | -5.86 to -1.29 | - | - | - |
| domain geo, judge knows | 100% | 83% | +0.17 | -2.00 | -5.00 to -0.91 | - | - | - |
| domain law, judge knows | 98% | 90% | +0.08 | -5.00 | -14.00 to -1.73 | - | - | - |
| domain medqa, judge knows | 99% | 83% | +0.16 | -2.08 | -5.00 to -1.05 | - | - | - |

### prompt variant selfcheck (picks the first position in 40% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 91% to 96% | 150 | 0 |
| CW-IDK | all | 77% | 72% to 81% | 150 | 0 |
| CC-IDK | judge knows | 99% | 98% to 100% | 114 | 0 |
| CW-IDK | judge knows | 74% | 68% to 79% | 114 | 0 |
| CC-IDK | judge does not know | 76% | 68% to 85% | 36 | 0 |
| CW-IDK | judge does not know | 86% | 78% to 93% | 36 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 67 | 0 |
| CW-IDK | judge tells the two answers apart | 72% | 66% to 79% | 67 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 94% | 91% to 97% | 144 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 76% | 71% to 80% | 144 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 111 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 73% | 68% to 78% | 111 | 0 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 0 |
| CW-IDK | domain geo | 76% | 68% to 84% | 50 | 0 |
| CC-IDK | domain law | 90% | 84% to 95% | 50 | 0 |
| CW-IDK | domain law | 83% | 76% to 90% | 50 | 0 |
| CC-IDK | domain medqa | 95% | 91% to 99% | 50 | 0 |
| CW-IDK | domain medqa | 71% | 63% to 79% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 42 | 0 |
| CW-IDK | domain geo, judge knows | 75% | 67% to 83% | 42 | 0 |
| CC-IDK | domain law, judge knows | 98% | 95% to 100% | 31 | 0 |
| CW-IDK | domain law, judge knows | 79% | 71% to 87% | 31 | 0 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 68% | 59% to 78% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 94% | 77% | +0.17 | -1.57 | -2.65 to -1.01 | - | - | - |
| judge knows | 99% | 74% | +0.25 | -0.93 | -1.41 to -0.61 | - | - | - |
| judge does not know | 76% | 86% | -0.10 | undefined | -12.50 to -2.11 | - | - | - |
| judge tells the two answers apart | 100% | 72% | +0.28 | -0.81 | -1.39 to -0.46 | - | - | - |
| judge flags the wrong answer as incorrect | 94% | 76% | +0.18 | -1.40 | -2.29 to -0.90 | - | - | - |
| judge knows and flags the wrong answer | 99% | 73% | +0.26 | -0.88 | -1.36 to -0.57 | - | - | - |
| domain geo | 96% | 76% | +0.20 | -1.30 | -2.67 to -0.67 | - | - | - |
| domain law | 90% | 83% | +0.07 | -4.71 | -18.00 to -1.59 | - | - | - |
| domain medqa | 95% | 71% | +0.24 | -0.87 | -2.00 to -0.37 | - | - | - |
| domain geo, judge knows | 100% | 75% | +0.25 | -1.00 | -2.00 to -0.50 | - | - | - |
| domain law, judge knows | 98% | 79% | +0.19 | -1.50 | -3.43 to -0.72 | - | - | - |
| domain medqa, judge knows | 99% | 68% | +0.30 | -0.60 | -1.31 to -0.21 | - | - | - |

### prompt variant stakes (picks the first position in 46% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 93% | 89% to 96% | 149 | 2 |
| CW-IDK | all | 62% | 56% to 68% | 148 | 12 |
| CC-IDK | judge knows | 96% | 93% to 98% | 113 | 2 |
| CW-IDK | judge knows | 58% | 51% to 65% | 112 | 12 |
| CC-IDK | judge does not know | 83% | 74% to 92% | 36 | 2 |
| CW-IDK | judge does not know | 75% | 64% to 86% | 36 | 12 |
| CC-IDK | judge tells the two answers apart | 98% | 96% to 100% | 66 | 2 |
| CW-IDK | judge tells the two answers apart | 57% | 48% to 65% | 66 | 12 |
| CC-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 96% | 143 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 61% | 55% to 68% | 142 | 12 |
| CC-IDK | judge knows and flags the wrong answer | 96% | 93% to 98% | 110 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 58% | 50% to 65% | 109 | 12 |
| CC-IDK | domain geo | 92% | 86% to 97% | 50 | 2 |
| CW-IDK | domain geo | 48% | 37% to 59% | 50 | 12 |
| CC-IDK | domain law | 90% | 83% to 96% | 49 | 2 |
| CW-IDK | domain law | 70% | 60% to 81% | 49 | 12 |
| CC-IDK | domain medqa | 96% | 92% to 99% | 50 | 2 |
| CW-IDK | domain medqa | 68% | 58% to 78% | 49 | 12 |
| CC-IDK | domain geo, judge knows | 95% | 90% to 99% | 42 | 2 |
| CW-IDK | domain geo, judge knows | 45% | 33% to 57% | 42 | 12 |
| CC-IDK | domain law, judge knows | 95% | 90% to 100% | 30 | 2 |
| CW-IDK | domain law, judge knows | 63% | 50% to 77% | 30 | 12 |
| CC-IDK | domain medqa, judge knows | 96% | 91% to 100% | 41 | 2 |
| CW-IDK | domain medqa, judge knows | 68% | 56% to 78% | 40 | 12 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 93% | 62% | +0.31 | -0.39 | -0.74 to -0.15 | - | - | - |
| judge knows | 95% | 58% | +0.38 | -0.20 | -0.49 to -0.01 | - | - | - |
| judge does not know | 83% | 75% | +0.08 | -3.00 | -10.50 to -0.59 | - | - | - |
| judge tells the two answers apart | 98% | 56% | +0.42 | -0.15 | -0.42 to +0.05 | - | - | - |
| judge flags the wrong answer as incorrect | 93% | 61% | +0.32 | -0.34 | -0.67 to -0.12 | - | - | - |
| judge knows and flags the wrong answer | 96% | 57% | +0.38 | -0.19 | -0.46 to +0.00 | - | - | - |
| domain geo | 92% | 48% | +0.44 | +0.05 | -0.28 to +0.24 | - | - | - |
| domain law | 90% | 70% | +0.20 | -1.00 | -4.14 to -0.28 | - | - | - |
| domain medqa | 96% | 68% | +0.28 | -0.67 | -1.50 to -0.23 | - | - | - |
| domain geo, judge knows | 95% | 45% | +0.50 | +0.10 | -0.19 to +0.27 | - | - | - |
| domain law, judge knows | 95% | 62% | +0.33 | -0.37 | -1.45 to +0.04 | - | - | - |
| domain medqa, judge knows | 96% | 68% | +0.29 | -0.61 | -1.50 to -0.16 | - | - | - |

### prompt variant think (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 92% | 86% to 97% | 90 | 0 |
| CW-IDK | all | 11% | 6% to 18% | 90 | 0 |
| CC-IDK | judge knows | 99% | 96% to 100% | 68 | 0 |
| CW-IDK | judge knows | 6% | 1% to 12% | 68 | 0 |
| CC-IDK | judge does not know | 70% | 50% to 89% | 22 | 0 |
| CW-IDK | judge does not know | 27% | 11% to 45% | 22 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 96% to 100% | 36 | 0 |
| CW-IDK | judge tells the two answers apart | 4% | 0% to 11% | 36 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 93% | 88% to 98% | 87 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 9% | 4% to 15% | 87 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 66 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 5% | 1% to 10% | 66 | 0 |
| CC-IDK | domain geo | 87% | 75% to 97% | 30 | 0 |
| CW-IDK | domain geo | 10% | 2% to 20% | 30 | 0 |
| CC-IDK | domain law | 92% | 82% to 100% | 30 | 0 |
| CW-IDK | domain law | 12% | 2% to 23% | 30 | 0 |
| CC-IDK | domain medqa | 97% | 90% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 12% | 2% to 23% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 98% | 94% to 100% | 24 | 0 |
| CW-IDK | domain geo, judge knows | 6% | 0% to 17% | 24 | 0 |
| CC-IDK | domain law, judge knows | 97% | 92% to 100% | 19 | 0 |
| CW-IDK | domain law, judge knows | 5% | 0% to 16% | 19 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 25 | 0 |
| CW-IDK | domain medqa, judge knows | 6% | 0% to 16% | 25 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 92% | 11% | +0.81 | +0.48 | +0.44 to +0.52 | - | - | - |
| judge knows | 99% | 6% | +0.93 | +0.48 | +0.44 to +0.50 | - | - | - |
| judge does not know | 70% | 27% | +0.43 | +0.53 | +0.23 to +0.90 | - | - | - |
| judge tells the two answers apart | 99% | 4% | +0.94 | +0.49 | +0.44 to +0.51 | - | - | - |
| judge flags the wrong answer as incorrect | 93% | 9% | +0.84 | +0.49 | +0.45 to +0.52 | - | - | - |
| judge knows and flags the wrong answer | 99% | 5% | +0.95 | +0.48 | +0.45 to +0.50 | - | - | - |
| domain geo | 87% | 10% | +0.77 | +0.52 | +0.44 to +0.61 | - | - | - |
| domain law | 92% | 12% | +0.80 | +0.48 | +0.40 to +0.55 | - | - | - |
| domain medqa | 97% | 12% | +0.85 | +0.45 | +0.37 to +0.50 | - | - | - |
| domain geo, judge knows | 98% | 6% | +0.92 | +0.48 | +0.41 to +0.52 | - | - | - |
| domain law, judge knows | 97% | 5% | +0.92 | +0.49 | +0.45 to +0.50 | - | - | - |
| domain medqa, judge knows | 100% | 6% | +0.94 | +0.47 | +0.40 to +0.50 | - | - | - |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 81% on 150 items

### prompt variant default (picks the first position in 45% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 100% | 99% to 100% | 150 | 1 |
| CC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| CW-CC | all | 16% | 11% to 21% | 150 | 2 |
| CW-HC | all | 51% | 45% to 58% | 150 | 2 |
| CW-HW | all | 98% | 96% to 99% | 150 | 2 |
| CW-IDK | all | 95% | 92% to 97% | 149 | 7 |
| HC-IDK | all | 94% | 91% to 96% | 149 | 2 |
| HW-IDK | all | 84% | 80% to 88% | 148 | 7 |
| CC-HC | judge knows | 100% | 99% to 100% | 122 | 1 |
| CC-IDK | judge knows | 100% | 100% to 100% | 122 | 0 |
| CW-CC | judge knows | 7% | 4% to 11% | 122 | 2 |
| CW-HC | judge knows | 45% | 37% to 52% | 122 | 2 |
| CW-HW | judge knows | 98% | 95% to 99% | 122 | 2 |
| CW-IDK | judge knows | 94% | 91% to 97% | 121 | 7 |
| HC-IDK | judge knows | 95% | 92% to 98% | 121 | 2 |
| HW-IDK | judge knows | 82% | 78% to 87% | 120 | 7 |
| CC-HC | judge does not know | 100% | 100% to 100% | 28 | 1 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 28 | 0 |
| CW-CC | judge does not know | 55% | 41% to 70% | 28 | 2 |
| CW-HC | judge does not know | 80% | 66% to 91% | 28 | 2 |
| CW-HW | judge does not know | 98% | 95% to 100% | 28 | 2 |
| CW-IDK | judge does not know | 98% | 95% to 100% | 28 | 7 |
| HC-IDK | judge does not know | 89% | 80% to 96% | 28 | 2 |
| HW-IDK | judge does not know | 91% | 84% to 98% | 28 | 7 |
| CC-HC | judge tells the two answers apart | 99% | 98% to 100% | 94 | 1 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 94 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 4% to 12% | 94 | 2 |
| CW-HC | judge tells the two answers apart | 35% | 27% to 42% | 94 | 2 |
| CW-HW | judge tells the two answers apart | 96% | 94% to 99% | 94 | 2 |
| CW-IDK | judge tells the two answers apart | 92% | 88% to 96% | 93 | 7 |
| HC-IDK | judge tells the two answers apart | 95% | 92% to 98% | 94 | 2 |
| HW-IDK | judge tells the two answers apart | 80% | 74% to 85% | 93 | 7 |
| CC-HC | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 106 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 106 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 12% | 7% to 17% | 106 | 2 |
| CW-HC | judge flags the wrong answer as incorrect | 40% | 33% to 48% | 106 | 2 |
| CW-HW | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 106 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 93% | 89% to 96% | 105 | 7 |
| HC-IDK | judge flags the wrong answer as incorrect | 93% | 90% to 97% | 106 | 2 |
| HW-IDK | judge flags the wrong answer as incorrect | 80% | 76% to 85% | 105 | 7 |
| CC-HC | judge knows and flags the wrong answer | 99% | 98% to 100% | 94 | 1 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 94 | 0 |
| CW-CC | judge knows and flags the wrong answer | 7% | 4% to 12% | 94 | 2 |
| CW-HC | judge knows and flags the wrong answer | 37% | 29% to 45% | 94 | 2 |
| CW-HW | judge knows and flags the wrong answer | 97% | 94% to 99% | 94 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 92% | 88% to 96% | 93 | 7 |
| HC-IDK | judge knows and flags the wrong answer | 94% | 91% to 97% | 94 | 2 |
| HW-IDK | judge knows and flags the wrong answer | 80% | 74% to 85% | 93 | 7 |
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
| domain law | 100% | 98% | +0.02 | -24.00 | -24.00 to -7.33 | 99% | 97% | 60% |
| domain medqa | 100% | 95% | +0.05 | -8.80 | -23.50 to -3.90 | 97% | 92% | 53% |
| domain geo, judge knows | 100% | 91% | +0.09 | -4.75 | -14.33 to -2.29 | 97% | 88% | 39% |
| domain law, judge knows | 100% | 98% | +0.02 | undefined | -15.50 to -7.25 | 100% | 98% | 50% |
| domain medqa, judge knows | 100% | 94% | +0.06 | -7.40 | -20.00 to -3.67 | 96% | 91% | 48% |

### prompt variant accuracy (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 94% to 98% | 150 | 2 |
| CW-IDK | all | 90% | 86% to 93% | 150 | 2 |
| CC-IDK | judge knows | 97% | 94% to 99% | 122 | 2 |
| CW-IDK | judge knows | 89% | 85% to 93% | 122 | 2 |
| CC-IDK | judge does not know | 95% | 88% to 100% | 28 | 2 |
| CW-IDK | judge does not know | 91% | 84% to 98% | 28 | 2 |
| CC-IDK | judge tells the two answers apart | 97% | 95% to 99% | 94 | 2 |
| CW-IDK | judge tells the two answers apart | 86% | 81% to 91% | 94 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 97% | 95% to 99% | 106 | 2 |
| CW-IDK | judge flags the wrong answer as incorrect | 87% | 83% to 92% | 106 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 97% | 95% to 99% | 94 | 2 |
| CW-IDK | judge knows and flags the wrong answer | 87% | 82% to 91% | 94 | 2 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 2 |
| CW-IDK | domain geo | 89% | 83% to 94% | 50 | 2 |
| CC-IDK | domain law | 94% | 89% to 98% | 50 | 2 |
| CW-IDK | domain law | 89% | 82% to 95% | 50 | 2 |
| CC-IDK | domain medqa | 99% | 97% to 100% | 50 | 2 |
| CW-IDK | domain medqa | 91% | 85% to 96% | 50 | 2 |
| CC-IDK | domain geo, judge knows | 97% | 92% to 100% | 46 | 2 |
| CW-IDK | domain geo, judge knows | 88% | 82% to 93% | 46 | 2 |
| CC-IDK | domain law, judge knows | 92% | 86% to 98% | 33 | 2 |
| CW-IDK | domain law, judge knows | 89% | 80% to 97% | 33 | 2 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 43 | 2 |
| CW-IDK | domain medqa, judge knows | 91% | 85% to 97% | 43 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 90% | +0.07 | -5.95 | -13.67 to -3.47 | - | - | - |
| judge knows | 97% | 89% | +0.07 | -5.33 | -12.62 to -3.04 | - | - | - |
| judge does not know | 95% | 91% | +0.04 | -11.50 | -12.50 to -2.57 | - | - | - |
| judge tells the two answers apart | 97% | 86% | +0.11 | -3.24 | -6.50 to -1.93 | - | - | - |
| judge flags the wrong answer as incorrect | 97% | 87% | +0.10 | -3.76 | -7.91 to -2.26 | - | - | - |
| judge knows and flags the wrong answer | 97% | 87% | +0.10 | -3.68 | -7.80 to -2.14 | - | - | - |
| domain geo | 96% | 89% | +0.07 | -5.57 | -15.00 to -2.43 | - | - | - |
| domain law | 94% | 89% | +0.05 | -7.80 | -20.50 to -2.62 | - | - | - |
| domain medqa | 99% | 91% | +0.08 | -5.13 | -15.33 to -2.57 | - | - | - |
| domain geo, judge knows | 97% | 88% | +0.09 | -4.38 | -13.67 to -2.00 | - | - | - |
| domain law, judge knows | 92% | 89% | +0.03 | -13.00 | -14.00 to -2.22 | - | - | - |
| domain medqa, judge knows | 100% | 91% | +0.09 | -4.37 | -13.33 to -2.31 | - | - | - |

### prompt variant cot (picks the first position in 61% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 93% to 98% | 90 | 0 |
| CW-IDK | all | 73% | 66% to 80% | 90 | 0 |
| CC-IDK | judge knows | 97% | 93% to 99% | 73 | 0 |
| CW-IDK | judge knows | 68% | 60% to 75% | 73 | 0 |
| CC-IDK | judge does not know | 91% | 82% to 100% | 17 | 0 |
| CW-IDK | judge does not know | 97% | 91% to 100% | 17 | 0 |
| CC-IDK | judge tells the two answers apart | 97% | 93% to 99% | 60 | 0 |
| CW-IDK | judge tells the two answers apart | 62% | 53% to 70% | 60 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 96% | 92% to 99% | 67 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 65% | 57% to 72% | 67 | 0 |
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
| CC-IDK | domain law, judge knows | 97% | 92% to 100% | 19 | 0 |
| CW-IDK | domain law, judge knows | 84% | 71% to 95% | 19 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 81% | 71% to 90% | 26 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 73% | +0.22 | -1.05 | -1.96 to -0.57 | - | - | - |
| judge knows | 97% | 68% | +0.29 | -0.62 | -1.16 to -0.27 | - | - | - |
| judge does not know | 91% | 97% | -0.06 | undefined | -16.00 to -4.00 | - | - | - |
| judge tells the two answers apart | 97% | 62% | +0.35 | -0.33 | -0.75 to -0.07 | - | - | - |
| judge flags the wrong answer as incorrect | 96% | 65% | +0.31 | -0.49 | -1.00 to -0.17 | - | - | - |
| judge knows and flags the wrong answer | 96% | 61% | +0.35 | -0.32 | -0.74 to -0.06 | - | - | - |
| domain geo | 92% | 48% | +0.43 | +0.04 | -0.33 to +0.24 | - | - | - |
| domain law | 97% | 88% | +0.08 | -4.60 | -13.00 to -1.60 | - | - | - |
| domain medqa | 98% | 83% | +0.15 | -2.22 | -6.50 to -1.00 | - | - | - |
| domain geo, judge knows | 93% | 45% | +0.48 | +0.11 | -0.17 to +0.28 | - | - | - |
| domain law, judge knows | 97% | 84% | +0.13 | -2.60 | -17.00 to -0.80 | - | - | - |
| domain medqa, judge knows | 100% | 81% | +0.19 | -1.60 | -4.20 to -0.73 | - | - | - |

### prompt variant data (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 150 | 1 |
| CW-IDK | all | 98% | 96% to 99% | 149 | 2 |
| CC-IDK | judge knows | 100% | 100% to 100% | 122 | 1 |
| CW-IDK | judge knows | 97% | 95% to 99% | 121 | 2 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 28 | 1 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 28 | 2 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 94 | 1 |
| CW-IDK | judge tells the two answers apart | 96% | 94% to 99% | 93 | 2 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 106 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 105 | 2 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 94 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 96% | 94% to 98% | 93 | 2 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain geo | 95% | 91% to 99% | 50 | 2 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain law | 99% | 97% to 100% | 50 | 2 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 50 | 1 |
| CW-IDK | domain medqa | 99% | 97% to 100% | 49 | 2 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 1 |
| CW-IDK | domain geo, judge knows | 95% | 90% to 99% | 46 | 2 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 33 | 1 |
| CW-IDK | domain law, judge knows | 98% | 95% to 100% | 33 | 2 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 43 | 1 |
| CW-IDK | domain medqa, judge knows | 99% | 96% to 100% | 42 | 2 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 98% | +0.02 | -20.29 | -23.83 to -10.46 | - | - | - |
| judge knows | 100% | 97% | +0.03 | -16.29 | -23.20 to -8.31 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge tells the two answers apart | 100% | 96% | +0.04 | -12.29 | -22.25 to -6.75 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 97% | +0.03 | -14.00 | -20.00 to -7.08 | - | - | - |
| judge knows and flags the wrong answer | 100% | 96% | +0.04 | -12.29 | -22.25 to -6.15 | - | - | - |
| domain geo | 100% | 95% | +0.05 | -9.00 | -24.00 to -4.56 | - | - | - |
| domain law | 100% | 99% | +0.01 | undefined | -24.00 to -11.50 | - | - | - |
| domain medqa | 100% | 99% | +0.01 | undefined | -23.50 to -11.25 | - | - | - |
| domain geo, judge knows | 100% | 95% | +0.05 | -8.20 | -22.00 to -3.60 | - | - | - |
| domain law, judge knows | 100% | 98% | +0.02 | undefined | -15.50 to -7.25 | - | - | - |
| domain medqa, judge knows | 100% | 99% | +0.01 | undefined | -20.00 to -9.50 | - | - | - |

### prompt variant selfcheck (picks the first position in 51% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 95% | 93% to 97% | 150 | 3 |
| CW-IDK | all | 79% | 74% to 83% | 131 | 51 |
| CC-IDK | judge knows | 100% | 99% to 100% | 122 | 3 |
| CW-IDK | judge knows | 77% | 73% to 82% | 104 | 51 |
| CC-IDK | judge does not know | 77% | 68% to 86% | 28 | 3 |
| CW-IDK | judge does not know | 83% | 74% to 93% | 27 | 51 |
| CC-IDK | judge tells the two answers apart | 98% | 96% to 99% | 94 | 3 |
| CW-IDK | judge tells the two answers apart | 74% | 68% to 79% | 80 | 51 |
| CC-IDK | judge flags the wrong answer as incorrect | 97% | 94% to 99% | 106 | 3 |
| CW-IDK | judge flags the wrong answer as incorrect | 75% | 70% to 80% | 91 | 51 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 94 | 3 |
| CW-IDK | judge knows and flags the wrong answer | 74% | 69% to 80% | 80 | 51 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 3 |
| CW-IDK | domain geo | 81% | 74% to 88% | 45 | 51 |
| CC-IDK | domain law | 92% | 87% to 97% | 50 | 3 |
| CW-IDK | domain law | 76% | 68% to 84% | 44 | 51 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 3 |
| CW-IDK | domain medqa | 79% | 71% to 86% | 42 | 51 |
| CC-IDK | domain geo, judge knows | 99% | 97% to 100% | 46 | 3 |
| CW-IDK | domain geo, judge knows | 79% | 72% to 87% | 41 | 51 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 33 | 3 |
| CW-IDK | domain law, judge knows | 75% | 64% to 86% | 28 | 51 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 43 | 3 |
| CW-IDK | domain medqa, judge knows | 77% | 69% to 86% | 35 | 51 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 95% | 79% | +0.16 | -1.79 | -2.93 to -1.18 | - | - | - |
| judge knows | 100% | 77% | +0.22 | -1.24 | -1.89 to -0.82 | - | - | - |
| judge does not know | 76% | 83% | -0.07 | undefined | -9.50 to -2.60 | - | - | - |
| judge tells the two answers apart | 98% | 74% | +0.24 | -1.00 | -1.66 to -0.61 | - | - | - |
| judge flags the wrong answer as incorrect | 96% | 75% | +0.21 | -1.21 | -2.00 to -0.75 | - | - | - |
| judge knows and flags the wrong answer | 99% | 74% | +0.25 | -0.98 | -1.57 to -0.60 | - | - | - |
| domain geo | 96% | 81% | +0.14 | -2.15 | -6.40 to -1.05 | - | - | - |
| domain law | 91% | 76% | +0.15 | -1.77 | -5.33 to -0.80 | - | - | - |
| domain medqa | 98% | 79% | +0.19 | -1.50 | -3.20 to -0.78 | - | - | - |
| domain geo, judge knows | 99% | 79% | +0.20 | -1.50 | -3.00 to -0.82 | - | - | - |
| domain law, judge knows | 100% | 75% | +0.25 | -1.00 | -2.50 to -0.40 | - | - | - |
| domain medqa, judge knows | 100% | 77% | +0.23 | -1.19 | -2.50 to -0.59 | - | - | - |

### prompt variant stakes (picks the first position in 37% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 94% to 98% | 150 | 1 |
| CW-IDK | all | 75% | 71% to 79% | 149 | 5 |
| CC-IDK | judge knows | 98% | 95% to 99% | 122 | 1 |
| CW-IDK | judge knows | 72% | 67% to 77% | 121 | 5 |
| CC-IDK | judge does not know | 91% | 84% to 98% | 28 | 1 |
| CW-IDK | judge does not know | 88% | 79% to 95% | 28 | 5 |
| CC-IDK | judge tells the two answers apart | 98% | 96% to 99% | 94 | 1 |
| CW-IDK | judge tells the two answers apart | 67% | 62% to 72% | 94 | 5 |
| CC-IDK | judge flags the wrong answer as incorrect | 96% | 93% to 98% | 106 | 1 |
| CW-IDK | judge flags the wrong answer as incorrect | 67% | 62% to 72% | 106 | 5 |
| CC-IDK | judge knows and flags the wrong answer | 97% | 95% to 99% | 94 | 1 |
| CW-IDK | judge knows and flags the wrong answer | 66% | 61% to 71% | 94 | 5 |
| CC-IDK | domain geo | 96% | 92% to 99% | 50 | 1 |
| CW-IDK | domain geo | 60% | 53% to 67% | 50 | 5 |
| CC-IDK | domain law | 95% | 91% to 99% | 50 | 1 |
| CW-IDK | domain law | 89% | 83% to 94% | 49 | 5 |
| CC-IDK | domain medqa | 98% | 95% to 100% | 50 | 1 |
| CW-IDK | domain medqa | 76% | 69% to 83% | 50 | 5 |
| CC-IDK | domain geo, judge knows | 97% | 92% to 100% | 46 | 1 |
| CW-IDK | domain geo, judge knows | 59% | 52% to 65% | 46 | 5 |
| CC-IDK | domain law, judge knows | 95% | 89% to 100% | 33 | 1 |
| CW-IDK | domain law, judge knows | 88% | 80% to 95% | 32 | 5 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 43 | 1 |
| CW-IDK | domain medqa, judge knows | 74% | 67% to 81% | 43 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 75% | +0.21 | -1.16 | -1.73 to -0.80 | - | - | - |
| judge knows | 98% | 72% | +0.26 | -0.85 | -1.29 to -0.56 | - | - | - |
| judge does not know | 91% | 88% | +0.04 | -10.50 | -11.50 to -2.00 | - | - | - |
| judge tells the two answers apart | 98% | 67% | +0.31 | -0.55 | -0.88 to -0.33 | - | - | - |
| judge flags the wrong answer as incorrect | 96% | 67% | +0.28 | -0.62 | -0.98 to -0.38 | - | - | - |
| judge knows and flags the wrong answer | 97% | 66% | +0.31 | -0.51 | -0.82 to -0.29 | - | - | - |
| domain geo | 96% | 60% | +0.36 | -0.28 | -0.59 to -0.08 | - | - | - |
| domain law | 95% | 89% | +0.06 | -6.33 | -20.50 to -2.54 | - | - | - |
| domain medqa | 98% | 76% | +0.22 | -1.18 | -2.36 to -0.63 | - | - | - |
| domain geo, judge knows | 97% | 59% | +0.38 | -0.23 | -0.52 to -0.05 | - | - | - |
| domain law, judge knows | 95% | 88% | +0.08 | -4.80 | -13.50 to -1.80 | - | - | - |
| domain medqa, judge knows | 100% | 74% | +0.26 | -0.95 | -1.69 to -0.54 | - | - | - |

### prompt variant think (picks the first position in 47% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 90 | 0 |
| CW-IDK | all | 94% | 91% to 97% | 88 | 5 |
| CC-IDK | judge knows | 100% | 100% to 100% | 73 | 0 |
| CW-IDK | judge knows | 93% | 89% to 96% | 71 | 5 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 17 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 17 | 5 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 60 | 0 |
| CW-IDK | judge tells the two answers apart | 92% | 87% to 97% | 59 | 5 |
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
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 19 | 0 |
| CW-IDK | domain law, judge knows | 94% | 86% to 100% | 18 | 5 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 98% | 94% to 100% | 25 | 5 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 94% | +0.06 | -7.80 | -16.60 to -4.50 | - | - | - |
| judge knows | 100% | 93% | +0.07 | -6.10 | -13.20 to -3.44 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge tells the two answers apart | 100% | 92% | +0.08 | -5.56 | -13.75 to -2.93 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 93% | +0.07 | -6.33 | -15.50 to -3.40 | - | - | - |
| judge knows and flags the wrong answer | 100% | 92% | +0.08 | -5.44 | -13.50 to -2.87 | - | - | - |
| domain geo | 100% | 88% | +0.12 | -3.29 | -9.00 to -1.50 | - | - | - |
| domain law | 100% | 97% | +0.03 | -13.50 | -13.50 to -4.80 | - | - | - |
| domain medqa | 100% | 98% | +0.02 | undefined | -13.50 to -6.25 | - | - | - |
| domain geo, judge knows | 100% | 88% | +0.12 | -3.00 | -8.33 to -1.33 | - | - | - |
| domain law, judge knows | 100% | 94% | +0.06 | -8.00 | -17.00 to -2.60 | - | - | - |
| domain medqa, judge knows | 100% | 98% | +0.02 | -24.00 | -24.00 to -5.25 | - | - | - |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 83% on 150 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 93% | 91% to 96% | 150 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| CW-CC | all | 15% | 11% to 21% | 150 | 0 |
| CW-HC | all | 22% | 17% to 28% | 150 | 0 |
| CW-HW | all | 69% | 64% to 74% | 150 | 0 |
| CW-IDK | all | 85% | 81% to 89% | 150 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 150 | 0 |
| HW-IDK | all | 98% | 96% to 100% | 150 | 0 |
| CC-HC | judge knows | 95% | 92% to 97% | 125 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 125 | 0 |
| CW-CC | judge knows | 8% | 5% to 12% | 125 | 0 |
| CW-HC | judge knows | 13% | 9% to 18% | 125 | 0 |
| CW-HW | judge knows | 68% | 62% to 73% | 125 | 0 |
| CW-IDK | judge knows | 82% | 77% to 87% | 125 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 125 | 0 |
| HW-IDK | judge knows | 98% | 95% to 100% | 125 | 0 |
| CC-HC | judge does not know | 86% | 76% to 94% | 25 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| CW-CC | judge does not know | 50% | 32% to 68% | 25 | 0 |
| CW-HC | judge does not know | 68% | 50% to 84% | 25 | 0 |
| CW-HW | judge does not know | 76% | 64% to 86% | 25 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| CC-HC | judge tells the two answers apart | 95% | 92% to 98% | 122 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 122 | 0 |
| CW-CC | judge tells the two answers apart | 7% | 4% to 11% | 122 | 0 |
| CW-HC | judge tells the two answers apart | 13% | 9% to 18% | 122 | 0 |
| CW-HW | judge tells the two answers apart | 67% | 61% to 72% | 122 | 0 |
| CW-IDK | judge tells the two answers apart | 82% | 77% to 87% | 122 | 0 |
| HC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 122 | 0 |
| HW-IDK | judge tells the two answers apart | 98% | 95% to 100% | 122 | 0 |
| CC-HC | judge flags the wrong answer as incorrect | 94% | 91% to 97% | 133 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 133 | 0 |
| CW-CC | judge flags the wrong answer as incorrect | 9% | 5% to 13% | 133 | 0 |
| CW-HC | judge flags the wrong answer as incorrect | 15% | 11% to 20% | 133 | 0 |
| CW-HW | judge flags the wrong answer as incorrect | 68% | 62% to 73% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 83% | 79% to 88% | 133 | 0 |
| HC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 133 | 0 |
| HW-IDK | judge flags the wrong answer as incorrect | 98% | 95% to 100% | 133 | 0 |
| CC-HC | judge knows and flags the wrong answer | 95% | 92% to 97% | 121 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 121 | 0 |
| CW-CC | judge knows and flags the wrong answer | 7% | 4% to 11% | 121 | 0 |
| CW-HC | judge knows and flags the wrong answer | 11% | 7% to 15% | 121 | 0 |
| CW-HW | judge knows and flags the wrong answer | 67% | 62% to 73% | 121 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 82% | 77% to 87% | 121 | 0 |
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
| CW-IDK | domain geo, judge knows | 82% | 72% to 90% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 38 | 0 |
| CW-HC | domain law, judge knows | 25% | 16% to 36% | 38 | 0 |
| CW-IDK | domain law, judge knows | 87% | 80% to 93% | 38 | 0 |
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

### prompt variant accuracy (picks the first position in 58% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 89% | 85% to 93% | 150 | 0 |
| CW-IDK | all | 32% | 26% to 39% | 150 | 0 |
| CC-IDK | judge knows | 92% | 88% to 96% | 125 | 0 |
| CW-IDK | judge knows | 26% | 20% to 32% | 125 | 0 |
| CC-IDK | judge does not know | 72% | 54% to 88% | 25 | 0 |
| CW-IDK | judge does not know | 66% | 50% to 80% | 25 | 0 |
| CC-IDK | judge tells the two answers apart | 95% | 91% to 98% | 122 | 0 |
| CW-IDK | judge tells the two answers apart | 25% | 19% to 31% | 122 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 92% | 88% to 95% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 26% | 20% to 32% | 133 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 93% | 89% to 96% | 121 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 24% | 18% to 30% | 121 | 0 |
| CC-IDK | domain geo | 98% | 95% to 100% | 50 | 0 |
| CW-IDK | domain geo | 20% | 11% to 30% | 50 | 0 |
| CC-IDK | domain law | 76% | 66% to 86% | 50 | 0 |
| CW-IDK | domain law | 41% | 31% to 51% | 50 | 0 |
| CC-IDK | domain medqa | 93% | 85% to 99% | 50 | 0 |
| CW-IDK | domain medqa | 36% | 25% to 48% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 98% | 95% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 16% | 8% to 26% | 46 | 0 |
| CC-IDK | domain law, judge knows | 80% | 71% to 89% | 38 | 0 |
| CW-IDK | domain law, judge knows | 34% | 24% to 45% | 38 | 0 |
| CC-IDK | domain medqa, judge knows | 98% | 93% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 28% | 17% to 40% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 89% | 32% | +0.57 | +0.31 | +0.23 to +0.38 | - | - | - |
| judge knows | 92% | 26% | +0.67 | +0.37 | +0.30 to +0.42 | - | - | - |
| judge does not know | 72% | 66% | +0.06 | -2.67 | -11.00 to +0.07 | - | - | - |
| judge tells the two answers apart | 95% | 25% | +0.70 | +0.36 | +0.30 to +0.41 | - | - | - |
| judge flags the wrong answer as incorrect | 92% | 26% | +0.66 | +0.37 | +0.30 to +0.42 | - | - | - |
| judge knows and flags the wrong answer | 93% | 24% | +0.69 | +0.38 | +0.31 to +0.43 | - | - | - |
| domain geo | 98% | 20% | +0.78 | +0.38 | +0.29 to +0.45 | - | - | - |
| domain law | 76% | 41% | +0.35 | +0.26 | -0.08 to +0.44 | - | - | - |
| domain medqa | 93% | 36% | +0.57 | +0.25 | +0.04 to +0.38 | - | - | - |
| domain geo, judge knows | 98% | 16% | +0.82 | +0.41 | +0.33 to +0.47 | - | - | - |
| domain law, judge knows | 80% | 34% | +0.46 | +0.34 | +0.13 to +0.49 | - | - | - |
| domain medqa, judge knows | 98% | 28% | +0.70 | +0.32 | +0.16 to +0.42 | - | - | - |

### prompt variant cot (picks the first position in 54% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 90 | 0 |
| CW-IDK | all | 88% | 82% to 93% | 90 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 74 | 0 |
| CW-IDK | judge knows | 85% | 78% to 91% | 74 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 16 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 16 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 73 | 0 |
| CW-IDK | judge tells the two answers apart | 86% | 79% to 92% | 73 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 79 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 86% | 80% to 92% | 79 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 72 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 85% | 78% to 90% | 72 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain geo | 87% | 75% to 97% | 30 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain law | 95% | 88% to 100% | 30 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 82% | 72% to 92% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-IDK | domain geo, judge knows | 85% | 72% to 96% | 27 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 21 | 0 |
| CW-IDK | domain law, judge knows | 93% | 86% to 100% | 21 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 79% | 67% to 88% | 26 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 88% | +0.12 | -3.09 | -5.92 to -1.90 | - | - | - |
| judge knows | 100% | 85% | +0.15 | -2.36 | -4.69 to -1.39 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| judge tells the two answers apart | 100% | 86% | +0.14 | -2.48 | -4.62 to -1.43 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 86% | +0.14 | -2.59 | -5.08 to -1.55 | - | - | - |
| judge knows and flags the wrong answer | 100% | 85% | +0.15 | -2.27 | -4.54 to -1.32 | - | - | - |
| domain geo | 100% | 87% | +0.13 | -2.75 | -9.00 to -1.00 | - | - | - |
| domain law | 100% | 95% | +0.05 | -9.00 | -14.00 to -3.29 | - | - | - |
| domain medqa | 100% | 82% | +0.18 | -1.73 | -5.00 to -0.76 | - | - | - |
| domain geo, judge knows | 100% | 85% | +0.15 | -2.38 | -8.00 to -0.80 | - | - | - |
| domain law, judge knows | 100% | 93% | +0.07 | -6.00 | -20.00 to -2.50 | - | - | - |
| domain medqa, judge knows | 100% | 79% | +0.21 | -1.36 | -3.33 to -0.53 | - | - | - |

### prompt variant data (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 99% to 100% | 150 | 0 |
| CW-IDK | all | 82% | 77% to 86% | 150 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 125 | 0 |
| CW-IDK | judge knows | 78% | 73% to 84% | 125 | 0 |
| CC-IDK | judge does not know | 98% | 94% to 100% | 25 | 0 |
| CW-IDK | judge does not know | 98% | 94% to 100% | 25 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 122 | 0 |
| CW-IDK | judge tells the two answers apart | 78% | 72% to 83% | 122 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 99% to 100% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 79% | 74% to 84% | 133 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 121 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 78% | 72% to 83% | 121 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain geo | 77% | 68% to 86% | 50 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain law | 88% | 82% to 94% | 50 | 0 |
| CC-IDK | domain medqa | 99% | 97% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 80% | 71% to 88% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 75% | 65% to 84% | 46 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 38 | 0 |
| CW-IDK | domain law, judge knows | 84% | 76% to 91% | 38 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 77% | 66% to 87% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 82% | +0.18 | -1.76 | -2.65 to -1.17 | - | - | - |
| judge knows | 100% | 78% | +0.22 | -1.31 | -2.05 to -0.84 | - | - | - |
| judge does not know | 98% | 98% | +0.00 | undefined | -24.00 to -6.67 | - | - | - |
| judge tells the two answers apart | 100% | 78% | +0.22 | -1.26 | -1.98 to -0.79 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 79% | +0.20 | -1.44 | -2.25 to -0.96 | - | - | - |
| judge knows and flags the wrong answer | 100% | 78% | +0.22 | -1.24 | -1.95 to -0.78 | - | - | - |
| domain geo | 100% | 77% | +0.23 | -1.17 | -2.33 to -0.56 | - | - | - |
| domain law | 100% | 88% | +0.12 | -3.17 | -7.33 to -1.78 | - | - | - |
| domain medqa | 99% | 80% | +0.19 | -1.58 | -3.80 to -0.75 | - | - | - |
| domain geo, judge knows | 100% | 75% | +0.25 | -1.00 | -2.07 to -0.44 | - | - | - |
| domain law, judge knows | 100% | 84% | +0.16 | -2.17 | -4.43 to -1.11 | - | - | - |
| domain medqa, judge knows | 100% | 77% | +0.23 | -1.16 | -2.73 to -0.46 | - | - | - |

### prompt variant selfcheck (picks the first position in 58% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 98% | 96% to 99% | 150 | 0 |
| CW-IDK | all | 81% | 76% to 85% | 150 | 0 |
| CC-IDK | judge knows | 99% | 98% to 100% | 125 | 0 |
| CW-IDK | judge knows | 77% | 72% to 82% | 125 | 0 |
| CC-IDK | judge does not know | 90% | 82% to 98% | 25 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 25 | 0 |
| CC-IDK | judge tells the two answers apart | 99% | 97% to 100% | 122 | 0 |
| CW-IDK | judge tells the two answers apart | 77% | 72% to 82% | 122 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 98% | 96% to 100% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 78% | 73% to 83% | 133 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 99% | 98% to 100% | 121 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 76% | 71% to 81% | 121 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 50 | 0 |
| CW-IDK | domain geo | 75% | 66% to 83% | 50 | 0 |
| CC-IDK | domain law | 97% | 93% to 100% | 50 | 0 |
| CW-IDK | domain law | 87% | 81% to 93% | 50 | 0 |
| CC-IDK | domain medqa | 96% | 92% to 99% | 50 | 0 |
| CW-IDK | domain medqa | 80% | 72% to 87% | 50 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 73% | 64% to 82% | 46 | 0 |
| CC-IDK | domain law, judge knows | 99% | 96% to 100% | 38 | 0 |
| CW-IDK | domain law, judge knows | 83% | 75% to 89% | 38 | 0 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 76% | 67% to 84% | 41 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 98% | 81% | +0.17 | -1.80 | -2.86 to -1.19 | - | - | - |
| judge knows | 99% | 77% | +0.22 | -1.20 | -1.82 to -0.77 | - | - | - |
| judge does not know | 90% | 100% | -0.10 | undefined | +nan to +nan | - | - | - |
| judge tells the two answers apart | 99% | 77% | +0.22 | -1.25 | -1.93 to -0.80 | - | - | - |
| judge flags the wrong answer as incorrect | 98% | 78% | +0.20 | -1.42 | -2.23 to -0.93 | - | - | - |
| judge knows and flags the wrong answer | 99% | 76% | +0.23 | -1.12 | -1.73 to -0.74 | - | - | - |
| domain geo | 100% | 75% | +0.25 | -1.00 | -1.94 to -0.47 | - | - | - |
| domain law | 97% | 87% | +0.10 | -3.70 | -10.75 to -1.82 | - | - | - |
| domain medqa | 96% | 80% | +0.16 | -1.88 | -5.43 to -0.85 | - | - | - |
| domain geo, judge knows | 100% | 73% | +0.27 | -0.84 | -1.71 to -0.39 | - | - | - |
| domain law, judge knows | 99% | 83% | +0.16 | -2.08 | -4.43 to -1.06 | - | - | - |
| domain medqa, judge knows | 99% | 76% | +0.23 | -1.11 | -2.45 to -0.48 | - | - | - |

### prompt variant stakes (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 94% | 91% to 96% | 150 | 0 |
| CW-IDK | all | 44% | 37% to 51% | 150 | 1 |
| CC-IDK | judge knows | 96% | 94% to 98% | 125 | 0 |
| CW-IDK | judge knows | 38% | 30% to 45% | 125 | 1 |
| CC-IDK | judge does not know | 82% | 68% to 94% | 25 | 0 |
| CW-IDK | judge does not know | 76% | 60% to 90% | 25 | 1 |
| CC-IDK | judge tells the two answers apart | 97% | 95% to 99% | 122 | 0 |
| CW-IDK | judge tells the two answers apart | 37% | 30% to 44% | 122 | 1 |
| CC-IDK | judge flags the wrong answer as incorrect | 95% | 91% to 97% | 133 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 38% | 32% to 45% | 133 | 1 |
| CC-IDK | judge knows and flags the wrong answer | 96% | 94% to 98% | 121 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 36% | 29% to 43% | 121 | 1 |
| CC-IDK | domain geo | 97% | 93% to 100% | 50 | 0 |
| CW-IDK | domain geo | 27% | 17% to 38% | 50 | 1 |
| CC-IDK | domain law | 88% | 81% to 94% | 50 | 0 |
| CW-IDK | domain law | 59% | 48% to 70% | 50 | 1 |
| CC-IDK | domain medqa | 96% | 91% to 100% | 50 | 0 |
| CW-IDK | domain medqa | 46% | 34% to 58% | 50 | 1 |
| CC-IDK | domain geo, judge knows | 98% | 95% to 100% | 46 | 0 |
| CW-IDK | domain geo, judge knows | 25% | 15% to 36% | 46 | 1 |
| CC-IDK | domain law, judge knows | 91% | 84% to 96% | 38 | 0 |
| CW-IDK | domain law, judge knows | 51% | 39% to 63% | 38 | 1 |
| CC-IDK | domain medqa, judge knows | 99% | 96% to 100% | 41 | 0 |
| CW-IDK | domain medqa, judge knows | 39% | 26% to 52% | 41 | 1 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 94% | 44% | +0.50 | +0.12 | -0.02 to +0.23 | - | - | - |
| judge knows | 96% | 38% | +0.58 | +0.21 | +0.10 to +0.30 | - | - | - |
| judge does not know | 82% | 76% | +0.06 | -4.33 | -17.00 to -0.42 | - | - | - |
| judge tells the two answers apart | 97% | 37% | +0.60 | +0.21 | +0.10 to +0.30 | - | - | - |
| judge flags the wrong answer as incorrect | 95% | 38% | +0.56 | +0.21 | +0.09 to +0.30 | - | - | - |
| judge knows and flags the wrong answer | 96% | 36% | +0.60 | +0.23 | +0.12 to +0.31 | - | - | - |
| domain geo | 97% | 27% | +0.70 | +0.33 | +0.21 to +0.42 | - | - | - |
| domain law | 88% | 59% | +0.29 | -0.31 | -1.19 to +0.05 | - | - | - |
| domain medqa | 96% | 46% | +0.50 | +0.08 | -0.22 to +0.26 | - | - | - |
| domain geo, judge knows | 98% | 25% | +0.73 | +0.34 | +0.23 to +0.42 | - | - | - |
| domain law, judge knows | 91% | 51% | +0.39 | -0.03 | -0.50 to +0.21 | - | - | - |
| domain medqa, judge knows | 99% | 39% | +0.60 | +0.18 | -0.05 to +0.33 | - | - | - |

### prompt variant think (picks the first position in 60% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 90 | 0 |
| CW-IDK | all | 59% | 52% to 67% | 90 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 74 | 0 |
| CW-IDK | judge knows | 52% | 44% to 60% | 74 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 16 | 0 |
| CW-IDK | judge does not know | 94% | 84% to 100% | 16 | 0 |
| CC-IDK | judge tells the two answers apart | 100% | 100% to 100% | 73 | 0 |
| CW-IDK | judge tells the two answers apart | 51% | 43% to 60% | 73 | 0 |
| CC-IDK | judge flags the wrong answer as incorrect | 100% | 100% to 100% | 79 | 0 |
| CW-IDK | judge flags the wrong answer as incorrect | 54% | 46% to 62% | 79 | 0 |
| CC-IDK | judge knows and flags the wrong answer | 100% | 100% to 100% | 72 | 0 |
| CW-IDK | judge knows and flags the wrong answer | 51% | 42% to 59% | 72 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain geo | 37% | 23% to 52% | 30 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain law | 80% | 72% to 88% | 30 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 30 | 0 |
| CW-IDK | domain medqa | 62% | 50% to 73% | 30 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 27 | 0 |
| CW-IDK | domain geo, judge knows | 30% | 17% to 43% | 27 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 21 | 0 |
| CW-IDK | domain law, judge knows | 76% | 64% to 86% | 21 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 26 | 0 |
| CW-IDK | domain medqa, judge knows | 56% | 44% to 67% | 26 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 59% | +0.41 | -0.23 | -0.50 to -0.05 | - | - | - |
| judge knows | 100% | 52% | +0.48 | -0.04 | -0.25 to +0.11 | - | - | - |
| judge does not know | 100% | 94% | +0.06 | -7.00 | -15.00 to -2.20 | - | - | - |
| judge tells the two answers apart | 100% | 51% | +0.49 | -0.03 | -0.24 to +0.12 | - | - | - |
| judge flags the wrong answer as incorrect | 100% | 54% | +0.46 | -0.08 | -0.32 to +0.08 | - | - | - |
| judge knows and flags the wrong answer | 100% | 51% | +0.49 | -0.01 | -0.22 to +0.13 | - | - | - |
| domain geo | 100% | 37% | +0.63 | +0.21 | +0.00 to +0.35 | - | - | - |
| domain law | 100% | 80% | +0.20 | -1.50 | -3.29 to -0.76 | - | - | - |
| domain medqa | 100% | 62% | +0.38 | -0.30 | -0.87 to +0.00 | - | - | - |
| domain geo, judge knows | 100% | 30% | +0.70 | +0.29 | +0.13 to +0.40 | - | - | - |
| domain law, judge knows | 100% | 76% | +0.24 | -1.10 | -2.50 to -0.50 | - | - | - |
| domain medqa, judge knows | 100% | 56% | +0.44 | -0.13 | -0.53 to +0.10 | - | - | - |
