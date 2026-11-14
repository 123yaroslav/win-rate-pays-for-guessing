# RunPod log, Study 5 evaluation

Budget for this step: 3.00 USD hard cap (10 USD on the account). One pod only. All times UTC, 2026-11-14.

## Price read before creating anything

| Time | Read | Result |
|---|---|---|
| 16:56 | pods on the account | none |
| 16:57 | GPU catalog, Community Cloud, pods | RTX 3090 24 GB 0.22 USD/h (stock Low), RTX 4090 24 GB 0.34 USD/h, RTX A5000 24 GB 0.16 USD/h (no stock), A40 48 GB only on Secure Cloud at 0.59 USD/h |
| 17:00 | RTX 3090, Community Cloud, per host CUDA version | stock only on hosts with CUDA 12.4, none on 12.8 or newer |

First choice: 1 x RTX 3090 24 GB, Community Cloud, 0.22 USD/h, with the official PyTorch 2.4 image for
CUDA 12.4 hosts. RunPod refused to place it, and the RTX 3090 Ti after it, so the pod that was created is an
A40 on Secure Cloud at 0.59 USD/h (see the table below). The read times above are approximate.

Disk: container 20 GB, volume 45 GB at `/workspace`. Disk price from the RunPod docs: about 0.10 USD per GB
per month while running, 0.20 USD per GB per month for the volume while stopped (45 GB stopped is about
0.0125 USD/h).

## Billable actions

| Time | Action | Price | Note |
|---|---|---|---|
| 17:00 | create pod, RTX 3090 Community, CUDA 12.4 image | 0.22 USD/h | refused twice by RunPod, "no instances available". Nothing created, nothing billed |
| 17:01 | create pod, RTX 3090 Ti Community, CUDA 12.8 image | 0.27 USD/h | refused, same message. Nothing created, nothing billed |
| 17:01 | stock read, Secure Cloud | | RTX 3090 24 GB 0.50 USD/h (EUR-IS-2, Low), A40 48 GB 0.59 USD/h (CA-MTL-1, Low), RTX A5000 none |
| 17:01:36 | **create pod `omacru723l4qql`**, 1 x A40 48 GB, Secure Cloud, CA-MTL-1 | **0.59 USD/h** | billing starts. Image `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`, container 20 GB, volume 45 GB at `/workspace`, port 22/tcp. A40 chosen over the Secure 3090: 0.09 USD/h more for twice the memory |
| 17:04 to 17:09 | install the environment, download the weights (19 GB in 26 s) | | no extra charge, part of the pod time |
| 17:09 to 17:21 | smoke tests, batch and padding checks, adapter path test | | |
| 17:21 to 17:28 | base model on the 300 questions, 369 s | | output copied to `results/study5/eval_base.jsonl`, checksums equal |
| 17:29:52 | **stop pod** | storage only | ran 1,696 s |
| 17:29:59 | **start pod** (restart test for the runbook) | 0.59 USD/h | volume intact, SSH port changed from 22046 to 22014 |
| 17:32 to 17:39 | base model again on the 300 questions after the restart | | 300 of 300 rows identical to the first run, rerun output deleted |
| 17:40:15 | **stop pod**, final state EXITED | storage only | ran 616 s |

## Spend

| Item | Amount |
|---|---|
| GPU time, 2,312 s (0.642 h) at 0.59 USD/h | 0.38 USD |
| Disks while running, 65 GB at 0.10 USD per GB per month | under 0.01 USD |
| **Total for this step** | **about 0.39 USD** of the 3.00 USD cap |
| From now on, pod stopped, volume 45 GB at 0.20 USD per GB per month | about 0.0125 USD/h, 0.30 USD per day, until the pod is deleted |

The total is computed from the run times above. The RunPod billing history showed no record for the pod yet at
17:41, so the invoiced figure can differ by a cent or two.

Nothing else was created: no network volume, no template, no endpoint, no second pod. The account had no pods
before this step.

## Step 2: four adapters and three reference runs (cap for this step 1.50 USD)

All times UTC, 2026-11-14. The four adapter folders were complete on the laptop at 18:31.

| Time | Action | Price | Note |
|---|---|---|---|
| 18:31:48 | start pod `omacru723l4qql` | 0.59 USD/h | refused by RunPod: "not enough free GPUs on the host machine". Nothing started, nothing billed beyond its storage |
| 18:32 | stock read, A40 48 GB, Secure Cloud | 0.59 USD/h | stock Low in CA-MTL-1 and EU-SE-1 |
| 18:32:24 | **create pod `o9m5gie80kmn40`** (`epi-study5-eval-2`), 1 x A40 48 GB, Secure Cloud, EU-SE-1 | **0.59 USD/h** | billing starts. Same image, disks and settings as the first pod |
| 18:33 to 18:37 | install the environment, download the weights | | part of the pod time |
| 18:34 to 18:39 | upload the four adapter folders, 520 MB | | checksums equal on both sides |
| 18:38 to 18:41 | smoke test on 16 questions with adapter K, the three style prompts and the format probe | | throwaway output deleted |
| 18:42 to 19:25 | full run: base, base with the three style prompts, format probe, adapters J, F, K, R | | 18 output files copied to `results/study5/`, checksums equal |
| 19:26:02 | **stop pod `o9m5gie80kmn40`**, final state EXITED | storage only | ran 3,218 s |
| 19:26:20 | **delete pod `omacru723l4qql`** (the first pod) | billing for it ends | it could not start, and the second pod holds the same environment, weights and base output (300 of 300 base responses identical on the two pods) |

### Spend of step 2

| Item | Amount |
|---|---|
| GPU time of the second pod, 3,218 s (0.894 h) at 0.59 USD/h | 0.53 USD |
| Disks of the second pod while running | under 0.01 USD |
| Volume of the first pod while stopped, 17:40 to 19:26 at 0.0125 USD/h | 0.02 USD |
| **Total for step 2** | **about 0.56 USD** of the 1.50 USD cap |
| **Total for both steps** | **about 0.95 USD** |
| From now on, second pod stopped, volume 45 GB | about 0.0125 USD/h, 0.30 USD per day, until the pod is deleted |

The RunPod billing history confirms the first step (0.389 USD for 17:00 to 18:00) and the stopped rate
(0.00625 USD for half an hour of the stopped first pod). The GPU time of the second pod was not in the history
yet at 19:27, so its amount is computed from the run time.

One pod is left on the account: `o9m5gie80kmn40`, stopped.

## Step 3: follow-up training (cap for this step 2.50 USD)

All times UTC, 2026-11-14 (15 November local time). Four LoRA adapters are trained on the pod with
`src/gpu_train_lora.py` and evaluated with `src/gpu_eval.py`. Pod actions went through the RunPod API, files
through SSH with the laptop key.

| Time | Action | Price | Note |
|---|---|---|---|
| 19:43 | pods on the account | | one, `o9m5gie80kmn40`, stopped |
| 19:50 | start pod `o9m5gie80kmn40` | 0.59 USD/h | refused twice by RunPod: "This machine does not have the resources to deploy your pod". Nothing started, nothing billed beyond its storage |
| 19:50 | stock read, A40 48 GB, Secure Cloud | 0.59 USD/h | stock Low in CA-MTL-1 and EU-SE-1 |
| 19:50:32 | **create pod `tsx9ltdt7jjhy9`** (`epi-study5-eval-3`), 1 x A40 48 GB, Secure Cloud, CA-MTL-1 | **0.59 USD/h** | billing starts. Same image, disks (container 20 GB, volume 45 GB at `/workspace`) and port as before. `PUBLIC_KEY` holds the laptop key and the account key, no other key or token on the pod |
| 19:51 to 19:54 | install the environment (same pinned versions), download the weights, 19 GB | | part of the pod time |
| 19:51 | upload `gpu_eval.py`, `gpu_train_lora.py`, `medqa_eval.jsonl`, `train_{C,J,K,R}.jsonl`, 8 MB | | checksums equal on both sides |
| 19:55 to 20:06 | memory and time measurements of one training step, nothing trained | | 16 examples in one forward pass do not fit in 48 GB, see `deviations.md` |
| 20:07 to 20:11 | smoke test: 4 training steps, then `gpu_eval.py` loads the saved adapter on 16 questions | | 256 of 256 tensors placed directly. Throwaway output deleted |
