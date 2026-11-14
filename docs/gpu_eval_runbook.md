# GPU evaluation runbook (Study 5, evaluation by the key)

`src/gpu_eval.py` runs on a rented GPU and writes one greedy response per question for the base model and for
each LoRA adapter, parses the final line and scores it against the key. The pod below already holds the
environment, the weights, the script, the 300 questions and the base-model output, so the four adapters need
steps (a) to (e) only. The log of every billable action is `results/study5/runpod_log.md`.

## The pod

| | |
|---|---|
| Pod id, name | `omacru723l4qql`, `epi-study5-eval` |
| GPU | 1 x NVIDIA A40, 48 GB, Secure Cloud, data center CA-MTL-1 |
| Price | 0.59 USD/h while running. Stopped: only the volume is billed, 45 GB at 0.20 USD per GB per month, about 0.0125 USD/h (9 USD per month) |
| Image | `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404` (Ubuntu 24.04, Python 3.12, CUDA 12.8) |
| Disks | container 20 GB (wiped at every stop), volume 45 GB at `/workspace` (survives a stop, deleted with the pod) |
| Keys on the pod | no Hugging Face token and no API key. Only SSH public keys, in the pod variable `PUBLIC_KEY`: the laptop's `~/.ssh/id_ed25519.pub` and the key registered in the RunPod account |

Installed on the volume, so a stop keeps all of it:

- `/workspace/venv`: torch 2.8.0+cu128, transformers 5.23.0, peft 0.21.3, accelerate 1.15.0, safetensors 0.8.0,
  huggingface-hub 2.4.0, tokenizers 0.23.3. No vLLM: the script uses transformers and peft directly.
- `/workspace/hf`: `Qwen/Qwen3.5-9B` at revision `c202236235762e1c871ad0ccb60c8ee5ba337b9a`, 19 GB. The model is
  public and not gated.
- `/workspace/study5`: `gpu_eval.py`, `medqa_eval.jsonl` (the same file as `data/items/medqa_eval.jsonl`),
  `out/eval_base.jsonl`, `out/eval_base_summary.json`, an empty `adapters/`.

The commands below need the RunPod API key on the laptop once: `runpodctl doctor`. The Start, Stop and Terminate
buttons of the RunPod console do the same as the `runpodctl pod` commands.

## (a) Restart the pod

```bash
POD=omacru723l4qql
runpodctl pod start $POD       # billing at 0.59 USD/h starts here
runpodctl ssh info $POD        # prints ip and port, the port changes at every start
```

Put the two values in and check the pod. For a minute or two after the start `ssh info` can still show the old
port and SSH can be refused. Read it again then. In the test of 14 November the port went from 22046 to 22014.

```bash
IP=63.141.33.140; PORT=22014   # replace with the values from `ssh info`
SSH=(ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p $PORT root@$IP)
SCP=(scp -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P $PORT)
"${SSH[@]}" 'nvidia-smi -L; ls /workspace/study5 /workspace/study5/out; /workspace/venv/bin/python -V'
```

If the start is refused because the GPU of that machine is taken, wait and retry, or build a new pod with the
section "A new pod from scratch" and delete this one.

## (b) Send the four adapter folders

From the repository root on the laptop. Each folder must hold `adapter_config.json` and
`adapter_model.safetensors`.

```bash
cd <repository root>
"${SCP[@]}" -r results/study5/adapters/J results/study5/adapters/F results/study5/adapters/K results/study5/adapters/R root@$IP:/workspace/study5/adapters/
"${SCP[@]}" src/gpu_eval.py data/items/medqa_eval.jsonl root@$IP:/workspace/study5/
"${SSH[@]}" 'ls -la /workspace/study5/adapters/*'
```

Without SSH the same goes through the relay, as in the previous sprint: `tar -C results/study5 -cf adapters.tar
adapters && runpodctl send adapters.tar` on the laptop, then in the pod's web terminal
`cd /workspace/study5 && runpodctl receive <code> && tar -xf adapters.tar`.

## (c) Run the evaluation for base plus four adapters

```bash
"${SSH[@]}" 'cd /workspace/study5; HF_HOME=/workspace/hf HF_HUB_OFFLINE=1 nohup /workspace/venv/bin/python gpu_eval.py --items medqa_eval.jsonl --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a --out out --adapters J=adapters/J F=adapters/F K=adapters/K R=adapters/R > /workspace/logs/eval_all.log 2>&1 < /dev/null &'
"${SSH[@]}" 'grep -v "falling back\|it/s" /workspace/logs/eval_all.log | tail -n 12'   # progress, then the table
```

The first command returns at once and the run goes on in the background. Repeat the second one to follow it.
The run is over when the table with one line per model is printed.

The base model is skipped because its output of 14 November is complete on the volume. Add `--force` to run it
again. A rerun on this pod gives the same text (checked, see "What was checked"). The base run took 369 seconds
for 300 questions, plus about a minute to load the weights. A fine-tune that ends early is faster, so the four
adapters should take 15 to 30 minutes, about 0.15 to 0.30 USD.

Keep `--batch-size` at its default of 16 for every model. The model runs in bfloat16, where the batch a question
sits in can flip a near-tie between two tokens, so another batch size gives slightly different text. Batch 16
needs about 24 GB of GPU memory.

The run stops with an error instead of writing results if an adapter's tensors do not all land in the model, or
if the base model is not back to its original state after an adapter. Two warnings are worth reading:
"does not change the logits" (the adapter has no effect) and "has its own chat template" (the adapter folder
ships a template that differs from the base one, and the base template is used for all models).

## (d) Fetch the results

```bash
"${SCP[@]}" "root@$IP:/workspace/study5/out/eval_*" results/study5/
ls results/study5/eval_*
```

Per model there is `eval_<name>.jsonl` (id, key, raw text, `parsed`, `outcome`, `correct`, token count, finish
reason) and `eval_<name>_summary.json` (abstention rate, accuracy, wrong-answer rate, unparsed rate, penalised
score, the adapter checks, versions, the exact prompt of the first question). All rates are shares of all 300
questions. `parsed` reads the last line that starts with "Final answer:". `parsed_lastline` also asks that it is
the last line of the response, the rule of `src/loop_common.py`.

## (e) Stop or delete the pod

```bash
runpodctl pod stop $POD        # keeps the volume, about 0.0125 USD/h until the pod is deleted
runpodctl pod delete $POD      # deletes the pod and the volume, all billing ends
runpodctl pod list             # check
```

Delete the pod once the results are on the laptop and no second run per rule is planned. Everything on it can
be rebuilt in ten minutes.

## A new pod from scratch

Needed only if the stopped pod cannot start. A 48 GB card keeps batch 16. Price and stock change, so read them
first (`runpodctl gpu list`). A new pod takes the SSH keys registered in the account, so register the laptop
key once with `runpodctl ssh add-key --key-file ~/.ssh/id_ed25519.pub`.

```bash
runpodctl pod create --name epi-study5-eval --image runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404 \
  --gpu-id "NVIDIA A40" --cloud-type SECURE --min-cuda-version 12.8 \
  --container-disk-in-gb 20 --volume-in-gb 45 --volume-mount-path /workspace --ports "22/tcp" --wait
```

Set `POD`, `IP`, `PORT`, `SSH` and `SCP` as in (a), then install (about 3 minutes) and continue with (b):

```bash
"${SSH[@]}" 'mkdir -p /workspace/study5/adapters /workspace/logs && uv venv /workspace/venv --python /usr/bin/python3 --system-site-packages && uv pip install --python /workspace/venv/bin/python torch==2.8.0 transformers==5.23.0 peft==0.21.3 accelerate==1.15.0 safetensors && HF_HOME=/workspace/hf /workspace/venv/bin/hf download Qwen/Qwen3.5-9B --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a'
```

On a new pod the base model runs again in (c). Use that new `eval_base` output together with the adapters
from the same pod, since another GPU type can flip near-ties.

## What the script does

- Prompt: one user turn with exactly the item's `qtext`, no system prompt, the model's own chat template with
  `enable_thinking=False`, which ends the prompt with an empty think block.
- Decoding: greedy (no sampling, which is temperature 0), repetition penalty 1, at most 300 new tokens, stop at
  `<|im_end|>` or `<|endoftext|>`.
- Batches: questions are sorted by prompt length and cut into fixed batches, so every model and every rerun
  sees the same batches. Output files keep the order of the items file.
- Adapters: loaded with peft on top of the base model one after another, without merging. The base is loaded
  once.
- The transformers messages about `causal_conv1d` and `flash-linear-attention` are harmless: the reference
  PyTorch code is used, which is exact and slower.

## What was checked on 14 November

| Check | Result |
|---|---|
| Stop, start, then the full base run again (300 questions, batch 16) | the volume kept the environment, the weights and the results. 300 of 300 rows identical to the first run, same file checksum |
| Same command twice, 8 questions, batch 8 | 8 of 8 texts identical |
| Left padding | next-token logits of a question alone and inside a padded batch differ by at most 0.30, the same as for a question with no padding (0.25). This is bfloat16 rounding, not a padding error |
| Batch 1 against batch 8, 8 questions | 2 of 8 texts identical, the others split at a near-tie. This is why the batch size stays fixed |
| Throwaway adapter (rank 8, q_proj and v_proj, random weights, written by `--make-test-adapter`) | 32 of 32 tensors placed, the first-prompt logits move by 1.5, 16 of 16 responses differ from the base |
| The same adapter with keys renamed to the multimodal layout (`language_model.layers`) | peft alone leaves it unloaded with a warning. The script places it by module path and gives the same 16 texts |
| An adapter with a tensor for a layer that has no q_proj | the run stops with an error, nothing is written |
| Base model restored after each adapter | yes: the first-prompt logits are compared after every adapter and the run stops on a drift above 0.001 |
| A model whose output is complete | skipped on the next run, the table is printed from the stored summary |

The throwaway adapters and their outputs were deleted from the pod after the test.

## Base model result (14 November)

300 questions, `results/study5/eval_base.jsonl` and `results/study5/eval_base_summary.json`: abstention 0.000,
accuracy 0.000, wrong 0.000, unparsed 1.000, penalised score -1.000. With no instruction the base model writes
a long analysis: 296 of 300 responses reach the 300-token limit, the other 4 end with a sentence such as
"the correct answer is B", and none contains a "Final answer:" line. By the registered rule every response is
unparsed.
