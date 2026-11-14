items 300 (geo, law, medqa), bootstrap draws 2000

## Registered tests (default instruction)

H1: b above 0.5 on group 'judge knows', Holm at 0.04. Passed by 1 of 1 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/openai/gpt-5.6-terra | 68.0% | 57.0% to 79.0% | 50 | 0.0005 | yes |

H1F: b above 0.5 on group 'all', Holm at 0.01. Passed by 1 of 1 judges.

| judge | b | 95% CI | items | bootstrap share at or below 0.5 | passes |
|---|---|---|---|---|---|
| openrouter/openai/gpt-5.6-terra | 72.5% | 62.5% to 81.7% | 60 | 0.0000 | yes |

## openrouter/openai/gpt-5.6-terra: own closed-book accuracy 83% on 60 items

### prompt variant default (picks the first position in 54% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 60 | 0 |
| CW-HC | all | 11% | 4% to 18% | 60 | 0 |
| CW-IDK | all | 72% | 62% to 82% | 60 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 50 | 0 |
| CW-HC | judge knows | 3% | 0% to 7% | 50 | 0 |
| CW-IDK | judge knows | 68% | 57% to 79% | 50 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 10 | 0 |
| CW-HC | judge does not know | 50% | 20% to 80% | 10 | 0 |
| CW-IDK | judge does not know | 95% | 85% to 100% | 10 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 20 | 0 |
| CW-HC | domain geo | 10% | 0% to 25% | 20 | 0 |
| CW-IDK | domain geo | 65% | 48% to 82% | 20 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 20 | 0 |
| CW-HC | domain law | 12% | 2% to 25% | 20 | 0 |
| CW-IDK | domain law | 88% | 72% to 98% | 20 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 20 | 0 |
| CW-HC | domain medqa | 10% | 0% to 22% | 20 | 0 |
| CW-IDK | domain medqa | 65% | 48% to 80% | 20 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 18 | 0 |
| CW-HC | domain geo, judge knows | 0% | 0% to 0% | 18 | 0 |
| CW-IDK | domain geo, judge knows | 61% | 42% to 81% | 18 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 15 | 0 |
| CW-HC | domain law, judge knows | 7% | 0% to 17% | 15 | 0 |
| CW-IDK | domain law, judge knows | 87% | 70% to 100% | 15 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 17 | 0 |
| CW-HC | domain medqa, judge knows | 3% | 0% to 9% | 17 | 0 |
| CW-IDK | domain medqa, judge knows | 59% | 44% to 76% | 17 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 72% | +0.28 | -0.82 | -1.73 to -0.36 | - | - | - |
| judge knows | 100% | 68% | +0.32 | -0.56 | -1.38 to -0.16 | - | - | - |
| judge does not know | 100% | 95% | +0.05 | -9.00 | -9.00 to -2.33 | - | - | - |
| domain geo | 100% | 65% | +0.35 | -0.43 | -1.86 to +0.09 | - | - | - |
| domain law | 100% | 88% | +0.12 | -3.00 | -19.00 to -1.00 | - | - | - |
| domain medqa | 100% | 65% | +0.35 | -0.43 | -1.50 to +0.00 | - | - | - |
| domain geo, judge knows | 100% | 61% | +0.39 | -0.29 | -1.57 to +0.14 | - | - | - |
| domain law, judge knows | 100% | 87% | +0.13 | -2.75 | -14.00 to -0.67 | - | - | - |
| domain medqa, judge knows | 100% | 59% | +0.41 | -0.21 | -1.12 to +0.15 | - | - | - |
