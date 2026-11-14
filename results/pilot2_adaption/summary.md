items 30 (geo, law, medqa), bootstrap draws 1000

## adaption/deepseek-v4-flash: own closed-book accuracy 70% on 30 items

### prompt variant default (picks the first position in 50% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 96% | 88% to 100% | 13 | 0 |
| CW-HC | all | 81% | 58% to 100% | 13 | 0 |
| CW-IDK | all | 92% | 81% to 100% | 13 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 8 | 0 |
| CW-HC | judge knows | 69% | 38% to 100% | 8 | 0 |
| CW-IDK | judge knows | 88% | 69% to 100% | 8 | 0 |
| CC-IDK | judge does not know | 90% | 70% to 100% | 5 | 0 |
| CW-HC | judge does not know | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain geo | 88% | 62% to 100% | 4 | 0 |
| CW-HC | domain geo | 62% | 25% to 100% | 4 | 0 |
| CW-IDK | domain geo | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain law | 75% | 25% to 100% | 4 | 0 |
| CW-IDK | domain law | 100% | 100% to 100% | 4 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain medqa | 100% | 100% to 100% | 5 | 0 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-HC | domain geo, judge knows | 50% | 0% to 100% | 3 | 0 |
| CW-IDK | domain geo, judge knows | 67% | 50% to 100% | 3 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-HC | domain law, judge knows | 67% | 0% to 100% | 3 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 3 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-HC | domain medqa, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 2 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 96% | 92% | +0.04 | -11.00 | -12.00 to -1.60 | - | - | - |
| judge knows | 100% | 88% | +0.12 | -3.00 | -7.00 to -0.60 | - | - | - |
| judge does not know | 90% | 100% | -0.10 | undefined | +nan to +nan | - | - | - |
| domain geo | 88% | 75% | +0.12 | -2.00 | -3.00 to +0.00 | - | - | - |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo, judge knows | 100% | 67% | +0.33 | -0.50 | -2.00 to +0.00 | - | - | - |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |

## adaption/gemma-4-31b-it: own closed-book accuracy 77% on 30 items

### prompt variant default (picks the first position in 57% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 100% | 100% to 100% | 13 | 0 |
| CW-HC | all | 38% | 8% to 69% | 13 | 2 |
| CW-IDK | all | 85% | 73% to 96% | 13 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 9 | 0 |
| CW-HC | judge knows | 11% | 0% to 33% | 9 | 2 |
| CW-IDK | judge knows | 78% | 61% to 94% | 9 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 4 | 0 |
| CW-HC | judge does not know | 100% | 100% to 100% | 4 | 2 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 4 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain geo | 25% | 0% to 75% | 4 | 2 |
| CW-IDK | domain geo | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain law | 25% | 0% to 75% | 4 | 2 |
| CW-IDK | domain law | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain medqa | 60% | 20% to 100% | 5 | 2 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-HC | domain geo, judge knows | 0% | 0% to 0% | 3 | 2 |
| CW-IDK | domain geo, judge knows | 67% | 50% to 100% | 3 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain law, judge knows | 25% | 0% to 75% | 4 | 2 |
| CW-IDK | domain law, judge knows | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-HC | domain medqa, judge knows | 0% | 0% to 0% | 2 | 2 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 2 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 85% | +0.15 | -2.25 | -12.00 to -0.86 | - | - | - |
| judge knows | 100% | 78% | +0.22 | -1.25 | -8.00 to -0.29 | - | - | - |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain law | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |
| domain geo, judge knows | 100% | 67% | +0.33 | -0.50 | -2.00 to +0.00 | - | - | - |
| domain law, judge knows | 100% | 75% | +0.25 | -1.00 | -3.00 to +0.00 | - | - | - |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | - | - | - |

## adaption/qwen3.8-27b: own closed-book accuracy 73% on 30 items

### prompt variant default (picks the first position in 21% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-IDK | all | 88% | 77% to 100% | 13 | 0 |
| CW-HC | all | 42% | 31% to 58% | 13 | 3 |
| CW-IDK | all | 69% | 58% to 81% | 13 | 0 |
| CC-IDK | judge knows | 88% | 75% to 100% | 8 | 0 |
| CW-HC | judge knows | 38% | 19% to 50% | 8 | 3 |
| CW-IDK | judge knows | 62% | 50% to 81% | 8 | 0 |
| CC-IDK | judge does not know | 90% | 70% to 100% | 5 | 0 |
| CW-HC | judge does not know | 50% | 20% to 80% | 5 | 3 |
| CW-IDK | judge does not know | 80% | 60% to 100% | 5 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain geo | 50% | 50% to 50% | 4 | 3 |
| CW-IDK | domain geo | 62% | 50% to 88% | 4 | 0 |
| CC-IDK | domain law | 75% | 50% to 100% | 4 | 0 |
| CW-HC | domain law | 25% | 0% to 50% | 4 | 3 |
| CW-IDK | domain law | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain medqa | 90% | 70% to 100% | 5 | 0 |
| CW-HC | domain medqa | 50% | 20% to 80% | 5 | 3 |
| CW-IDK | domain medqa | 70% | 50% to 90% | 5 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-HC | domain geo, judge knows | 50% | 50% to 50% | 2 | 3 |
| CW-IDK | domain geo, judge knows | 50% | 50% to 50% | 2 | 0 |
| CC-IDK | domain law, judge knows | 75% | 50% to 100% | 4 | 0 |
| CW-HC | domain law, judge knows | 25% | 0% to 50% | 4 | 3 |
| CW-IDK | domain law, judge knows | 75% | 50% to 100% | 4 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 2 | 0 |
| CW-HC | domain medqa, judge knows | 50% | 50% to 50% | 2 | 3 |
| CW-IDK | domain medqa, judge knows | 50% | 50% to 50% | 2 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 88% | 69% | +0.19 | -1.00 | -7.00 to -0.20 | - | - | - |
| judge knows | 88% | 62% | +0.25 | -0.50 | -4.00 to +0.00 | - | - | - |
| judge does not know | 90% | 80% | +0.10 | -3.00 | -4.00 to -0.33 | - | - | - |
| domain geo | 100% | 62% | +0.38 | -0.33 | -3.00 to +0.00 | - | - | - |
| domain law | 75% | 75% | +0.00 | undefined | -3.00 to +0.00 | - | - | - |
| domain medqa | 90% | 70% | +0.20 | -1.00 | -4.00 to +0.00 | - | - | - |
| domain geo, judge knows | 100% | 50% | +0.50 | +0.00 | +0.00 to +0.00 | - | - | - |
| domain law, judge knows | 75% | 75% | +0.00 | undefined | -3.00 to +0.00 | - | - | - |
| domain medqa, judge knows | 100% | 50% | +0.50 | +0.00 | +0.00 to +0.00 | - | - | - |
