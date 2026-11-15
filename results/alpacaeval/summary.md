# The judge prompt of AlpacaEval 2.0 on 150 fresh questions (Amendment 5)

Known questions only unless marked. b is the rate at which the wrong answer beats "I don't know".

| judge | knows | b, known | 95% CI | wrong beats right, known | 95% CI | b, all questions | no verdict, primary | dropped | b passes | control passes |
|---|---|---|---|---|---|---|---|---|---|---|
| deepseek-v4-flash | 83.3% | 97.2% | 95.2% to 99.2% | 10.0% | 6.0% to 14.4% | 97.3% | 0.0% | no | yes | yes |
| gemma-4-31b-it | 81.3% | 74.4% | 68.2% to 80.6% | 2.5% | 0.4% to 5.4% | 78.5% | 2.7% | no | yes | yes |
| qwen3.8-27b | 79.3% | 91.6% | 87.4% to 95.4% | 3.8% | 1.3% to 7.1% | 92.7% | 0.7% | no | yes | yes |
| claude-haiku-5.5 | 82.7% | 98.8% | 97.2% to 100.0% | 16.1% | 11.4% to 21.6% | 99.0% | 2.0% | no | yes | yes |
| gpt-5.6-luna | 90.0% | 89.6% | 85.9% to 93.3% | 8.1% | 4.8% to 12.2% | 90.7% | 0.0% | no | yes | yes |
| mistral-small-2603 | 79.3% | 87.4% | 83.2% to 91.2% | 18.5% | 13.9% to 23.1% | 89.0% | 0.0% | no | yes | yes |
| qwen3.5-397b | 87.3% | 90.1% | 86.3% to 93.5% | 5.0% | 2.3% to 8.4% | 90.7% | 0.0% | no | yes | yes |
| glm-5.2 | 86.7% | 88.5% | 83.5% to 93.1% | 8.8% | 5.0% to 13.1% | 90.0% | 0.0% | no | yes | yes |

Registered judges kept 6. A1 passes for 6 (holds: True), A2 for 6 (holds: True). Larger judges kept 2, A3 passes for 2 (holds: True).
