items 30 (geo, law, medqa), bootstrap draws 500

## openrouter/anthropic/claude-haiku-5.5: own closed-book accuracy 63% on 30 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 83% | 70% to 93% | 15 | 3 |
| CC-IDK | all | 97% | 91% to 100% | 16 | 0 |
| CW-HC | all | 31% | 12% to 47% | 16 | 0 |
| CW-HW | all | 62% | 44% to 78% | 16 | 3 |
| CW-IDK | all | 94% | 84% to 100% | 16 | 1 |
| HC-IDK | all | 97% | 90% to 100% | 15 | 0 |
| HW-IDK | all | 90% | 80% to 100% | 15 | 0 |
| CC-HC | judge knows | 93% | 79% to 100% | 7 | 3 |
| CC-IDK | judge knows | 100% | 100% to 100% | 8 | 0 |
| CW-HC | judge knows | 25% | 6% to 50% | 8 | 0 |
| CW-HW | judge knows | 50% | 25% to 75% | 8 | 3 |
| CW-IDK | judge knows | 94% | 81% to 100% | 8 | 1 |
| HC-IDK | judge knows | 100% | 100% to 100% | 7 | 0 |
| HW-IDK | judge knows | 86% | 71% to 100% | 7 | 0 |
| CC-HC | judge does not know | 75% | 56% to 94% | 8 | 3 |
| CC-IDK | judge does not know | 94% | 81% to 100% | 8 | 0 |
| CW-HC | judge does not know | 38% | 12% to 62% | 8 | 0 |
| CW-HW | judge does not know | 75% | 62% to 94% | 8 | 3 |
| CW-IDK | judge does not know | 94% | 81% to 100% | 8 | 1 |
| HC-IDK | judge does not know | 94% | 81% to 100% | 8 | 0 |
| HW-IDK | judge does not know | 94% | 81% to 100% | 8 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain geo | 40% | 0% to 80% | 5 | 0 |
| CW-IDK | domain geo | 90% | 70% to 100% | 5 | 1 |
| CC-IDK | domain law | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain law | 10% | 0% to 30% | 5 | 0 |
| CW-IDK | domain law | 100% | 100% to 100% | 5 | 1 |
| CC-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CW-HC | domain medqa | 42% | 25% to 50% | 6 | 0 |
| CW-IDK | domain medqa | 92% | 75% to 100% | 6 | 1 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain geo, judge knows | 25% | 0% to 75% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 1 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 1 | 0 |
| CW-HC | domain law, judge knows | 0% | 0% to 0% | 1 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 1 | 1 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-HC | domain medqa, judge knows | 33% | 0% to 50% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 83% | 67% to 100% | 3 | 1 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 94% | +0.03 | -14.00 | -15.00 to -2.20 | 62% | 61% | 31% |
| judge knows | 100% | 94% | +0.06 | -7.00 | -7.00 to -1.00 | 50% | 47% | 25% |
| judge does not know | 94% | 94% | +0.00 | undefined | -7.00 to -1.33 | 75% | 75% | 38% |
| domain geo | 100% | 90% | +0.10 | -4.00 | -4.00 to -0.67 | 60% | 54% | 40% |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | 70% | 70% | 10% |
| domain medqa | 92% | 92% | +0.00 | undefined | -5.00 to -0.50 | 58% | 58% | 42% |
| domain geo, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 62% | 62% | 25% |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 0% | 0% | 0% |
| domain medqa, judge knows | 100% | 83% | +0.17 | -2.00 | -2.00 to +0.00 | 50% | 42% | 33% |

## openrouter/mistralai/mistral-small-2603: own closed-book accuracy 70% on 30 items

### prompt variant default (picks the first position in 49% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 97% | 91% to 100% | 16 | 0 |
| CC-IDK | all | 100% | 100% to 100% | 16 | 0 |
| CW-HC | all | 53% | 31% to 75% | 16 | 0 |
| CW-HW | all | 100% | 100% to 100% | 16 | 0 |
| CW-IDK | all | 100% | 100% to 100% | 16 | 0 |
| HC-IDK | all | 97% | 90% to 100% | 15 | 0 |
| HW-IDK | all | 97% | 90% to 100% | 15 | 0 |
| CC-HC | judge knows | 95% | 85% to 100% | 10 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 10 | 0 |
| CW-HC | judge knows | 35% | 10% to 65% | 10 | 0 |
| CW-HW | judge knows | 100% | 100% to 100% | 10 | 0 |
| CW-IDK | judge knows | 100% | 100% to 100% | 10 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 9 | 0 |
| HW-IDK | judge knows | 100% | 100% to 100% | 9 | 0 |
| CC-HC | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CW-HC | judge does not know | 83% | 67% to 100% | 6 | 0 |
| CW-HW | judge does not know | 100% | 100% to 100% | 6 | 0 |
| CW-IDK | judge does not know | 100% | 100% to 100% | 6 | 0 |
| HC-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| HW-IDK | judge does not know | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain geo | 50% | 10% to 90% | 5 | 0 |
| CW-IDK | domain geo | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain law | 40% | 10% to 70% | 5 | 0 |
| CW-IDK | domain law | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CW-HC | domain medqa | 67% | 33% to 100% | 6 | 0 |
| CW-IDK | domain medqa | 100% | 100% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-HC | domain geo, judge knows | 33% | 0% to 100% | 3 | 0 |
| CW-IDK | domain geo, judge knows | 100% | 100% to 100% | 3 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain law, judge knows | 38% | 0% to 75% | 4 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 4 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |
| CW-HC | domain medqa, judge knows | 33% | 0% to 100% | 3 | 0 |
| CW-IDK | domain medqa, judge knows | 100% | 100% to 100% | 3 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 53% |
| judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 35% |
| judge does not know | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 83% |
| domain geo | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 50% |
| domain law | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 40% |
| domain medqa | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 67% |
| domain geo, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 33% |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 38% |
| domain medqa, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 100% | 100% | 33% |

## openrouter/openai/gpt-5.6-luna: own closed-book accuracy 80% on 30 items

### prompt variant default (picks the first position in 56% of duels)

| pair, first vs second | group | first wins | 95% CI | items | unparsed calls |
|---|---|---|---|---|---|
| CC-HC | all | 97% | 91% to 100% | 16 | 0 |
| CC-IDK | all | 97% | 91% to 100% | 16 | 0 |
| CW-HC | all | 22% | 9% to 38% | 16 | 0 |
| CW-HW | all | 69% | 50% to 84% | 16 | 0 |
| CW-IDK | all | 94% | 84% to 100% | 16 | 0 |
| HC-IDK | all | 100% | 100% to 100% | 15 | 0 |
| HW-IDK | all | 100% | 100% to 100% | 15 | 0 |
| CC-HC | judge knows | 100% | 100% to 100% | 12 | 0 |
| CC-IDK | judge knows | 100% | 100% to 100% | 12 | 0 |
| CW-HC | judge knows | 12% | 0% to 25% | 12 | 0 |
| CW-HW | judge knows | 67% | 46% to 83% | 12 | 0 |
| CW-IDK | judge knows | 96% | 88% to 100% | 12 | 0 |
| HC-IDK | judge knows | 100% | 100% to 100% | 11 | 0 |
| HW-IDK | judge knows | 100% | 100% to 100% | 11 | 0 |
| CC-HC | judge does not know | 88% | 62% to 100% | 4 | 0 |
| CC-IDK | judge does not know | 88% | 62% to 100% | 4 | 0 |
| CW-HC | judge does not know | 50% | 12% to 88% | 4 | 0 |
| CW-HW | judge does not know | 75% | 50% to 100% | 4 | 0 |
| CW-IDK | judge does not know | 88% | 62% to 100% | 4 | 0 |
| HC-IDK | judge does not know | 100% | 100% to 100% | 4 | 0 |
| HW-IDK | judge does not know | 100% | 100% to 100% | 4 | 0 |
| CC-IDK | domain geo | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain geo | 20% | 0% to 40% | 5 | 0 |
| CW-IDK | domain geo | 100% | 100% to 100% | 5 | 0 |
| CC-IDK | domain law | 100% | 100% to 100% | 5 | 0 |
| CW-HC | domain law | 10% | 0% to 30% | 5 | 0 |
| CW-IDK | domain law | 90% | 70% to 100% | 5 | 0 |
| CC-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CW-HC | domain medqa | 33% | 8% to 58% | 6 | 0 |
| CW-IDK | domain medqa | 92% | 75% to 100% | 6 | 0 |
| CC-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain geo, judge knows | 12% | 0% to 38% | 4 | 0 |
| CW-IDK | domain geo, judge knows | 100% | 100% to 100% | 4 | 0 |
| CC-IDK | domain law, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain law, judge knows | 12% | 0% to 38% | 4 | 0 |
| CW-IDK | domain law, judge knows | 100% | 100% to 100% | 4 | 0 |
| CC-IDK | domain medqa, judge knows | 100% | 100% to 100% | 4 | 0 |
| CW-HC | domain medqa, judge knows | 12% | 0% to 38% | 4 | 0 |
| CW-IDK | domain medqa, judge knows | 88% | 62% to 100% | 4 | 0 |

| group | a = CC beats IDK | b = CW beats IDK | a - b | break-even accuracy p* | 95% CI | tone, CW beats HW | CW beats HC predicted | observed |
|---|---|---|---|---|---|---|---|---|
| all | 97% | 94% | +0.03 | -14.00 | -15.00 to -2.00 | 69% | 67% | 22% |
| judge knows | 100% | 96% | +0.04 | -11.00 | -11.00 to -2.00 | 67% | 64% | 12% |
| judge does not know | 88% | 88% | +0.00 | undefined | -3.00 to -0.33 | 75% | 75% | 50% |
| domain geo | 100% | 100% | +0.00 | undefined | +nan to +nan | 70% | 70% | 20% |
| domain law | 100% | 90% | +0.10 | -4.00 | -4.00 to -0.67 | 70% | 63% | 10% |
| domain medqa | 92% | 92% | +0.00 | undefined | -5.00 to -1.00 | 67% | 67% | 33% |
| domain geo, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 62% | 62% | 12% |
| domain law, judge knows | 100% | 100% | +0.00 | undefined | +nan to +nan | 75% | 75% | 12% |
| domain medqa, judge knows | 100% | 88% | +0.12 | -3.00 | -3.00 to -0.33 | 62% | 55% | 12% |
