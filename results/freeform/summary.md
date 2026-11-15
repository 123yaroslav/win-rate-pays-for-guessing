# Free-form questions with natural-length responses, 100 questions (Amendment 3)

Known questions only. b is the rate at which the wrong reply beats the abstention.

| judge | knows | b, short abstention | b, fuller abstention | a, short abstention | wrong beats right | b under the published prompt, short | fuller | F1 | F2 | F3 |
|---|---|---|---|---|---|---|---|---|---|---|
| deepseek-v4-flash | 83% | 73% (66% to 81%) | 52% (45% to 58%) | 99% (98% to 100%) | 2% (1% to 5%) | 56% (48% to 64%) | 24% (18% to 31%) | yes | no | yes |
| gemma-4-31b-it | 58% | 32% (21% to 43%) | 24% (14% to 35%) | 100% (100% to 100%) | 0% (0% to 0%) | 19% (10% to 28%) | 14% (6% to 23%) | no | no | yes |
| qwen3.8-27b | 50% | 65% (58% to 72%) | 66% (60% to 73%) | 96% (92% to 99%) | 3% (0% to 7%) | 17% (8% to 27%) | 16% (8% to 26%) | yes | yes | yes |
| claude-haiku-5.5 | 75% | 73% (67% to 80%) | 59% (51% to 67%) | 99% (98% to 100%) | 3% (1% to 5%) | 10% (5% to 17%) | 8% (3% to 14%) | yes | yes | yes |
| gpt-5.6-luna | 81% | 63% (54% to 72%) | 36% (28% to 45%) | 100% (100% to 100%) | 0% (0% to 0%) | 41% (33% to 50%) | 14% (8% to 19%) | yes | no | yes |
| mistral-small-2603 | 79% | 97% (94% to 99%) | 75% (69% to 80%) | 100% (100% to 100%) | 4% (1% to 8%) | 85% (80% to 90%) | 73% (66% to 81%) | yes | yes | yes |

Judges kept 6. F1 holds for 5, F2 for 3, F3 for 6, F4 for 1 of 6 judges with usable replies.
