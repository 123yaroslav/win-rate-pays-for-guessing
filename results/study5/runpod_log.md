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
