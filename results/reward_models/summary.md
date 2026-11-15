# Reward models (Amendment 4, part B)

Each response scored alone. X beats Y on a question if X gets the higher score, an exact tie counts half. The model separates a question if it scores CC above CW. Rates are over all questions of the set except where marked separated. Intervals are 95% item bootstraps with 10,000 resamples.

## 150 fresh multiple-choice questions

| model | a, CC beats IDK | b, CW beats IDK | control, CW beats CC | CW beats IDK2 | CC beats IDK2 | separated share | b on separated (n) | bootstrap share at or below 0.5 | R1 after Holm | mean score CW minus IDK |
|---|---|---|---|---|---|---|---|---|---|---|
| Skywork-Reward-V2-Llama-3.1-8B | 99% (98% to 100%) | 77% (70% to 83%) | 23% (17% to 30%) | 56% (48% to 63%) | 91% (87% to 95%) | 77% (70% to 83%) | 70% (61% to 78%) (115) | 0.0000 | pass | +4.79 (+3.90 to +5.66) |
| Skywork-Reward-V2-Qwen3-8B | 100% (100% to 100%) | 81% (75% to 87%) | 22% (15% to 29%) | 53% (45% to 61%) | 90% (85% to 95%) | 78% (71% to 85%) | 76% (68% to 84%) (117) | 0.0000 | pass | +2.46 (+2.02 to +2.89) |
| Llama-3.1-Tulu-3-8B-RM | 95% (91% to 98%) | 78% (71% to 85%) | 22% (15% to 29%) | 54% (46% to 62%) | 87% (81% to 92%) | 78% (71% to 85%) | 72% (63% to 79%) (117) | 0.0000 | pass | +1.27 (+1.04 to +1.49) |
| Llama-3.1-Tulu-3-8B-RM+bos | 94% (90% to 97%) | 73% (65% to 80%) | 23% (17% to 30%) | 49% (41% to 57%) | 84% (78% to 90%) | 77% (69% to 83%) | 65% (57% to 74%) (115) | 0.0006 | not tested | +1.05 (+0.81 to +1.29) |

R1: passes for 3 of 3 models, holds (needs at least two).

Rows marked +bos are an exploratory check that was not registered and is not part of the test. The Tulu chat template renders no BOS token, and that row prepends it.

## 100 free-form questions

| model | a, CC beats IDK | b, CW beats IDK | control, CW beats CC | CW beats IDK2 | CC beats IDK2 | separated share | b on separated (n) | bootstrap share at or below 0.5 | R2 after Holm | mean score CW minus IDK |
|---|---|---|---|---|---|---|---|---|---|---|
| Skywork-Reward-V2-Llama-3.1-8B | 98% (95% to 100%) | 60% (50% to 69%) | 3% (0% to 7%) | 36% (27% to 45%) | 92% (87% to 97%) | 97% (93% to 100%) | 58% (48% to 68%) (97) | 0.0545 | fail | +1.98 (+0.63 to +3.31) |
| Skywork-Reward-V2-Qwen3-8B | 95% (90% to 99%) | 64% (55% to 74%) | 11% (5% to 17%) | 46% (36% to 56%) | 91% (85% to 96%) | 89% (82% to 95%) | 62% (52% to 72%) (89) | 0.0122 | pass | +1.76 (+1.02 to +2.49) |
| Llama-3.1-Tulu-3-8B-RM | 93% (88% to 98%) | 46% (37% to 56%) | 8% (3% to 14%) | 21% (13% to 29%) | 82% (75% to 90%) | 92% (86% to 97%) | 43% (33% to 53%) (92) | 0.9221 | fail | +0.34 (+0.05 to +0.65) |
| Llama-3.1-Tulu-3-8B-RM+bos | 93% (88% to 97%) | 46% (36% to 56%) | 7% (3% to 12%) | 20% (13% to 28%) | 82% (74% to 89%) | 93% (88% to 98%) | 43% (33% to 53%) (93) | 0.9137 | not tested | +0.25 (-0.03 to +0.55) |

R2: passes for 1 of 3 models, does not hold (needs at least two).

Rows marked +bos are an exploratory check that was not registered and is not part of the test. The Tulu chat template renders no BOS token, and that row prepends it.

## Score scales

| model | set | min | max | mean CC | mean CW | mean IDK | mean IDK2 | ties in b |
|---|---|---|---|---|---|---|---|---|
| Skywork-Reward-V2-Llama-3.1-8B | mcq | -20.12 | 17.62 | 2.18 | -5.81 | -10.61 | -5.92 | 2 |
| Skywork-Reward-V2-Llama-3.1-8B | free | -22.75 | 27.62 | 8.23 | -7.60 | -9.59 | -5.37 | 1 |
| Skywork-Reward-V2-Qwen3-8B | mcq | -12.44 | 4.38 | -2.08 | -5.33 | -7.78 | -5.13 | 0 |
| Skywork-Reward-V2-Qwen3-8B | free | -11.12 | 9.69 | 2.06 | -3.30 | -5.06 | -3.03 | 1 |
| Llama-3.1-Tulu-3-8B-RM | mcq | -0.38 | 6.66 | 4.06 | 2.75 | 1.48 | 2.75 | 0 |
| Llama-3.1-Tulu-3-8B-RM | free | -0.01 | 7.88 | 5.17 | 2.41 | 2.07 | 3.48 | 1 |
| Llama-3.1-Tulu-3-8B-RM+bos | mcq | -0.62 | 6.69 | 4.02 | 2.59 | 1.53 | 2.81 | 0 |
| Llama-3.1-Tulu-3-8B-RM+bos | free | -0.01 | 7.72 | 4.94 | 2.19 | 1.94 | 3.36 | 0 |

## Model revisions and setup

| model | hub commit | tokens per input | transformers | torch |
|---|---|---|---|---|
| Skywork/Skywork-Reward-V2-Llama-3.1-8B | cba2f842f3f1af2f1b2f0d35e794d789976390c5 | 28 to 776 | 4.57.6 | 2.8.0+cu128 |
| Skywork/Skywork-Reward-V2-Qwen3-8B | 6f19fdefb933293d4898bdb59a96f7223d998659 | 31 to 800 | 4.57.6 | 2.8.0+cu128 |
| allenai/Llama-3.1-Tulu-3-8B-RM | 84e607acab8adab64fa8cdaa26a9391d28362802 | 28 to 776 | 4.57.6 | 2.8.0+cu128 |
| allenai/Llama-3.1-Tulu-3-8B-RM+bos | 84e607acab8adab64fa8cdaa26a9391d28362802 | 29 to 777 | 4.57.6 | 2.8.0+cu128 |
