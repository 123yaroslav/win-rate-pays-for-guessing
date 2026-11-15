# Free-form questions with natural-length responses, 100 questions (Amendment 3)

Known questions only. b is the rate at which the wrong reply beats the abstention.

| judge | knows | b, short abstention | b, fuller abstention | a, short abstention | wrong beats right | b under the published prompt, short | fuller | F1 | F2 | F3 |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-haiku-5.5 | 75% | 73% (67% to 80%) | 59% (52% to 67%) | 99% (98% to 100%) | 3% (1% to 5%) | 10% (4% to 17%) | 8% (3% to 14%) | yes | yes | yes |
| gpt-5.6-luna | 81% | 63% (54% to 72%) | 36% (28% to 45%) | 100% (100% to 100%) | 0% (0% to 0%) | 41% (33% to 50%) | 14% (9% to 19%) | yes | no | yes |
| mistral-small-2603 | 79% | 97% (94% to 99%) | 75% (69% to 80%) | 100% (100% to 100%) | 4% (2% to 8%) | 85% (80% to 90%) | 73% (66% to 81%) | yes | yes | yes |

Judges kept 3. F1 holds for 3, F2 for 2, F3 for 3, F4 for 1 of 3 judges with usable replies.
