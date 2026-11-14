settings: reasoning none, templates v2, judges ['gemma-4-31b-it', 'deepseek-v4-flash']
n items 40, spend $0.007 (this run, uncached calls), 429s 0

## judge gemma-4-31b-it: own closed-book accuracy 75%
| pair (first vs second) | group | first wins | 95% CI | n | unparsed |
|---|---|---|---|---|---|
| CW vs HC | all | 42% | 32% to 53% | 76 | 4 |
| CW vs HC | judge knows | 36% | 24% to 49% | 56 | 4 |
| CW vs HC | judge wrong, picks the planted wrong option | 88% | 53% to 98% | 8 | 0 |
| CW vs HC | judge wrong, picks another option | 42% | 19% to 68% | 12 | 0 |
| CW vs IDK | all | 65% | 54% to 75% | 77 | 3 |
| CW vs IDK | judge knows | 63% | 50% to 74% | 57 | 3 |
| CW vs IDK | judge wrong, picks the planted wrong option | 100% | 68% to 100% | 8 | 0 |
| CW vs IDK | judge wrong, picks another option | 50% | 25% to 75% | 12 | 0 |
| CW vs HW | all | 88% | 78% to 94% | 65 | 15 |
| CW vs HW | judge knows | 87% | 75% to 94% | 47 | 13 |
| CW vs HW | judge wrong, picks the planted wrong option | 86% | 49% to 97% | 7 | 1 |
| CW vs HW | judge wrong, picks another option | 91% | 62% to 98% | 11 | 1 |

## judge deepseek-v4-flash: own closed-book accuracy 80%
| pair (first vs second) | group | first wins | 95% CI | n | unparsed |
|---|---|---|---|---|---|
| CW vs HC | all | 78% | 67% to 85% | 80 | 0 |
| CW vs HC | judge knows | 75% | 63% to 84% | 64 | 0 |
| CW vs HC | judge wrong, picks the planted wrong option | 93% | 69% to 99% | 14 | 0 |
| CW vs HC | judge wrong, picks another option | 50% | 9% to 91% | 2 | 0 |
| CW vs IDK | all | 95% | 88% to 98% | 80 | 0 |
| CW vs IDK | judge knows | 94% | 85% to 98% | 64 | 0 |
| CW vs IDK | judge wrong, picks the planted wrong option | 100% | 78% to 100% | 14 | 0 |
| CW vs IDK | judge wrong, picks another option | 100% | 34% to 100% | 2 | 0 |
| CW vs HW | all | 99% | 93% to 100% | 80 | 0 |
| CW vs HW | judge knows | 100% | 94% to 100% | 64 | 0 |
| CW vs HW | judge wrong, picks the planted wrong option | 93% | 69% to 99% | 14 | 0 |
| CW vs HW | judge wrong, picks another option | 100% | 34% to 100% | 2 | 0 |
