Natural-output duels: the assert-style response against the abstain-style abstention of the same model on the same question, both orders, default instruction. 328 of 1500 pool questions have an abstain-style abstention, 328 were sampled, 328 have an assert-style response with a parsed option (91 wrong, 237 correct by the key). Intervals are 95% item bootstraps (10000 resamples).

| judge | b_nat, wrong answer beats abstention | 95% CI | items | bootstrap share b_nat <= 0.5 | a_nat, correct answer beats abstention | 95% CI | items | picks first position | unparsed verdicts |
|---|---|---|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 | 95.0% | 91.1% to 98.3% | 90 | 0.0000 | 98.7% | 97.5% to 99.8% | 237 | 49.4% | 6 |
| openai/gpt-5.6-luna | 94.5% | 90.1% to 98.4% | 91 | 0.0000 | 100.0% | 100.0% to 100.0% | 237 | 50.6% | 0 |
| mistralai/mistral-small-2603 | 99.5% | 98.4% to 100.0% | 91 | 0.0000 | 99.4% | 98.5% to 100.0% | 237 | 49.7% | 0 |

P5a (b_nat above 0.5 for each of the three judges, bootstrap share at or below 0.5 under 0.05): holds. It holds for 3 of 3 judges (anthropic/claude-haiku-5.5, openai/gpt-5.6-luna, mistralai/mistral-small-2603).
