Duels between the test outputs of model J and model K. 63 of 300 questions differ in option or abstention.

| judge | J wins | 95% CI | questions | bootstrap share at or below 0.5 |
|---|---|---|---|---|
| claude-haiku-5.5 | 42.9% | 32.5% to 53.2% | 63 | 0.9272 |
| gpt-5.6-luna | 48.4% | 38.1% to 58.7% | 63 | 0.6455 |
| mistral-small-2603 | 36.5% | 27.8% to 46.0% | 63 | 0.9986 |

By what the two outputs are (share of duels won by J, pooled view per judge in the JSON).

| outputs | claude-haiku-5.5 | gpt-5.6-luna | mistral-small-2603 | questions |
|---|---|---|---|---|
| J right, K wrong | 47% | 56% | 34% | 34 |
| J wrong, K right | 36% | 28% | 44% | 18 |
| J wrong, K wrong | 41% | 59% | 32% | 11 |

spend 0.033 USD
