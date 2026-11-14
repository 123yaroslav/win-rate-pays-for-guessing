# Adaptive Data on 400 rows with known truth

Platform evaluation of the run: grade C to A, score 5.0 to 9.1, completion quality 1.78 to 9.72 (the platform scores a sample of 100 rows).

| source completion | rows | commits to an option | of those correct | of those wrong | abstains | hedged | extractors disagree | internal trace in output |
|---|---|---|---|---|---|---|---|---|
| assertive correct | 100 | 99/100 = 99% (95% to 100%) | 95/99 = 96% (90% to 98%) | 4/99 = 4% (2% to 10%) | 0/100 = 0% (0% to 4%) | 0/100 = 0% (0% to 4%) | 1 | 1 |
| hedged correct | 100 | 100/100 = 100% (96% to 100%) | 96/100 = 96% (90% to 98%) | 4/100 = 4% (2% to 10%) | 0/100 = 0% (0% to 4%) | 0/100 = 0% (0% to 4%) | 0 | 3 |
| abstention | 100 | 99/100 = 99% (95% to 100%) | 92/99 = 93% (86% to 97%) | 7/99 = 7% (3% to 14%) | 0/100 = 0% (0% to 4%) | 0/100 = 0% (0% to 4%) | 1 | 5 |
| assertive wrong | 100 | 98/100 = 98% (93% to 99%) | 96/98 = 98% (93% to 99%) | 2/98 = 2% (1% to 7%) | 0/100 = 0% (0% to 4%) | 0/100 = 0% (0% to 4%) | 2 | 3 |

All rows: commits 396/400 = 99% (97% to 100%), abstains 0/400 = 0% (0% to 1%), hedged 0/400 = 0% (0% to 1%), internal trace 12/400 = 3% (2% to 5%), spend on extraction 0.126 USD (uncached calls of this run).
