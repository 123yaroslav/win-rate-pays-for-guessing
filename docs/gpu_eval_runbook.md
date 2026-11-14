# GPU evaluation runbook (Study 5, evaluation by the key)

`src/gpu_eval.py` runs on a rented GPU and writes one greedy response per question for the base model and for
each LoRA adapter, parses the final line and scores it against the key. `src/loop_eval_analyze.py` runs on the
laptop and turns the output files into the tables for P5c and P5e. The pod below holds the environment, the
weights, the scripts, the 300 questions and the four adapters and outputs of the follow-up training (section
"Follow-up training"). The four service adapters and the outputs of the registered evaluation are on the laptop
only. The log of every billable action is `results/study5/runpod_log.md`.

## The pod

| | |
|---|---|
| Pod id, name | `tsx9ltdt7jjhy9`, `epi-study5-eval-3` |
| GPU | 1 x NVIDIA A40, 48 GB, Secure Cloud, data center CA-MTL-1 |
| Price | 0.59 USD/h while running. Stopped: only the volume is billed, 45 GB at 0.20 USD per GB per month, about 0.0125 USD/h (9 USD per month) |
| Image | `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404` (Ubuntu 24.04, Python 3.12, CUDA 12.8) |
| Disks | container 20 GB (wiped at every stop), volume 45 GB at `/workspace` (survives a stop, deleted with the pod) |
| Keys on the pod | no Hugging Face token and no API key. Only SSH public keys, in the pod variable `PUBLIC_KEY`: the laptop's `~/.ssh/id_ed25519.pub` and the key registered in the RunPod account |

This is the third pod. The first one (`omacru723l4qql`, same GPU type, CA-MTL-1) ran the base model on
14 November, was stopped, and could not be started again two hours later because the GPUs of its machine were
taken. It was rebuilt with the section "A new pod from scratch" and then deleted. The second one
(`o9m5gie80kmn40`, EU-SE-1) ran the registered evaluation and could not be started again either. The third pod
gave the same 300 base responses (same file checksum), ran the follow-up training, and the second was deleted.

Installed on the volume, so a stop keeps all of it:

- `/workspace/venv`: torch 2.8.0+cu128, transformers 5.23.0, peft 0.21.3, accelerate 1.15.0, safetensors 0.8.0,
  huggingface-hub 2.4.0, tokenizers 0.23.3. No vLLM: the script uses transformers and peft directly.
- `/workspace/hf`: `Qwen/Qwen3.5-9B` at revision `c202236235762e1c871ad0ccb60c8ee5ba337b9a`, 19 GB. The model is
  public and not gated.
- `/workspace/study5`: `gpu_eval.py`, `gpu_train_lora.py`, `medqa_eval.jsonl` (the same file as
  `data/items/medqa_eval.jsonl`), `train_{C,J,K,R}.jsonl`, `adapters_followup/{C3,J3,K3,R3}` (116 MB each, not
  on the laptop) and `out_followup/` with the outputs of the follow-up. `adapters/{J,F,K,R}`, the style prompts
  and `out/` of the registered evaluation are not on this pod, section (b) sends them again.

The commands below need the RunPod API key on the laptop once: `runpodctl doctor`. The Start, Stop and Terminate
buttons of the RunPod console do the same as the `runpodctl pod` commands.

## (a) Restart the pod

```bash
POD=tsx9ltdt7jjhy9
runpodctl pod start $POD       # billing at 0.59 USD/h starts here
runpodctl ssh info $POD        # prints ip and port, the port changes at every start
```

Put the two values in and check the pod. For a minute or two after the start `ssh info` can still show the old
port and SSH can be refused. Read it again then.

```bash
IP=194.68.245.27; PORT=22073   # replace with the values from `ssh info`
SSH=(ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p $PORT root@$IP)
SCP=(scp -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P $PORT)
"${SSH[@]}" 'nvidia-smi -L; ls /workspace/study5 /workspace/study5/out; /workspace/venv/bin/python -V'
```

If the start is refused with "not enough free GPUs on the host machine", the GPU of that machine is rented by
someone else. Wait and retry, or build a new pod with the section "A new pod from scratch" and delete this one.
This happened once already, so count on it.

## (b) Send the four adapter folders

From the repository root on the laptop. Each folder must hold `adapter_config.json` and
`adapter_model.safetensors`. The four folders are 520 MB and took about 5 minutes.

```bash
cd <repository root>
"${SCP[@]}" -r results/study5/adapters/J results/study5/adapters/F results/study5/adapters/K results/study5/adapters/R root@$IP:/workspace/study5/adapters/
"${SCP[@]}" src/gpu_eval.py data/items/medqa_eval.jsonl results/study5/train_R.jsonl root@$IP:/workspace/study5/
"${SCP[@]}" -r results/study5/style_prompts root@$IP:/workspace/study5/
"${SSH[@]}" 'ls -la /workspace/study5/adapters/*; sha256sum /workspace/study5/adapters/*/adapter_model.safetensors'
```

Without SSH the same goes through the relay, as in the previous sprint: `tar -C results/study5 -cf adapters.tar
adapters && runpodctl send adapters.tar` on the laptop, then in the pod's web terminal
`cd /workspace/study5 && runpodctl receive <code> && tar -xf adapters.tar`.

## (c) Run the evaluation

The registered evaluation, base model plus four adapters with no system prompt:

```bash
"${SSH[@]}" 'cd /workspace/study5; HF_HOME=/workspace/hf HF_HUB_OFFLINE=1 nohup /workspace/venv/bin/python gpu_eval.py --items medqa_eval.jsonl --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a --out out --adapters J=adapters/J F=adapters/F K=adapters/K R=adapters/R > /workspace/logs/eval_all.log 2>&1 < /dev/null &'
"${SSH[@]}" 'grep -v "falling back\|it/s\|Warning" /workspace/logs/eval_all.log | tail -n 12'   # progress, then the table
```

The run of 14 November added the three reference runs and the format probe. It is the same command with these
options before the `>`:

```bash
--system-file assert=style_prompts/assert.txt hedge=style_prompts/hedge.txt abstain=style_prompts/abstain.txt --probe train_R.jsonl --probe-n 64
```

The first command returns at once and the run goes on in the background. Repeat the second one to follow it.
The run is over when the table with one line per model is printed. A model whose output is complete on the
volume is skipped, so the same command finishes a run that was cut short. Add `--force` to run everything again.

Time on the A40 for 300 questions: about a minute to load the weights, 368 seconds for the base model with no
system prompt (it writes to the token limit), 84 to 242 seconds for the base model with a style instruction and
318 to 351 seconds per adapter. The whole run of 14 November took 43 minutes, about 0.42 USD.

Keep `--batch-size` at its default of 16 for every model. The model runs in bfloat16, where the batch a question
sits in can flip a near-tie between two tokens, so another batch size gives slightly different text. Batch 16
needs up to 39 GB of GPU memory with an adapter loaded, so the card must have 48 GB.

What the options do:

- `--system-file NAME=FILE` runs the base model with the text of the file as system prompt and writes
  `eval_base_NAME`. The three files in `results/study5/style_prompts/` are the final style instructions of
  `results/study5/style_prompts.json` (version v7c), byte for byte. These runs are a labelled reference. The
  registered evaluation has no system prompt.
- `--probe FILE` takes the first rows of a training file (`prompt`, `completion`) and measures how well each
  model predicts the completion when the prompt is put in six formats: the chat template with thinking off (the
  registered setting), with an open think tag, with no think tag, the chat template around the prompt as a JSON
  string, and the bare prompt as text or as a JSON string. The result is `out/format_probe.json`. The format an
  adapter was trained in shows the largest drop against the base model.
- `--assistant-start think_open` or `plain` runs every model with another start of the assistant turn and
  writes to `eval_<name>__think_open`. Not used so far.
- If an adapter folder ships a tokenizer or chat template that turns any question into other tokens than the
  base tokenizer does, the adapter is run a second time with the shipped files and written to
  `eval_<name>_shipped`. The summary of every adapter records the comparison under `shipped_files`.

The run stops with an error instead of writing results if an adapter's tensors do not all land in the model, or
if the base model is not back to its original state after an adapter. The long peft warnings about
`exclude_modules` and "missing adapter keys" are expected for these adapters: they were saved from the
multimodal class, their keys say `language_model.layers`, and the script places every tensor by its module path
and checks all 256 of them.

## (d) Fetch the results and build the tables

```bash
"${SCP[@]}" "root@$IP:/workspace/study5/out/*" results/study5/
ls results/study5/eval_* results/study5/format_probe.json
python src/loop_eval_analyze.py
```

Per model there is `eval_<name>.jsonl` (id, key, raw text, `parsed`, `outcome`, `correct`, token count, finish
reason) and `eval_<name>_summary.json` (abstention rate, accuracy, wrong-answer rate, unparsed rate, penalised
score, the adapter checks, versions, the exact prompt of the first question). `eval_summary.json` holds the
summaries of all models of the run. All rates are shares of all 300 questions. `parsed` reads the last line that
starts with "Final answer:". `parsed_lastline` also asks that it is the last line of the response, the rule of
`src/loop_common.py`.

`src/loop_eval_analyze.py` needs no GPU. It writes `results/study5/eval_table.md` and `eval_table.json`: the
metrics per model with 95% paired bootstrap intervals over the 300 questions (10,000 resamples, seed 20261115),
the paired differences J-K, F-K, J-F and J-R with the bootstrap share on the wrong side of zero, the verdicts
for P5c and P5e, and three raw responses for every model with more than 5% unparsed.

## (e) Stop or delete the pod

```bash
runpodctl pod stop $POD        # keeps the volume, about 0.0125 USD/h until the pod is deleted
runpodctl pod delete $POD      # deletes the pod and the volume, all billing ends
runpodctl pod list             # check
```

Delete the pod once the results are on the laptop and no second run per rule is planned. Everything on it can
be rebuilt in ten minutes.

## A new pod from scratch

Needed if the stopped pod cannot start. A 48 GB card is required for batch 16. Price and stock change, so read
them first (`runpodctl gpu list`). A new pod takes the SSH keys registered in the account, so register the laptop
key once with `runpodctl ssh add-key --key-file ~/.ssh/id_ed25519.pub`.

```bash
runpodctl pod create --name epi-study5-eval --image runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404 \
  --gpu-id "NVIDIA A40" --cloud-type SECURE --min-cuda-version 12.8 \
  --container-disk-in-gb 20 --volume-in-gb 45 --volume-mount-path /workspace --ports "22/tcp" --wait
```

Set `POD`, `IP`, `PORT`, `SSH` and `SCP` as in (a), then install (3 minutes on 14 November) and continue with (b):

```bash
"${SSH[@]}" 'mkdir -p /workspace/study5/adapters /workspace/logs && uv venv /workspace/venv --python /usr/bin/python3 --system-site-packages && uv pip install --python /workspace/venv/bin/python torch==2.8.0 transformers==5.23.0 peft==0.21.3 accelerate==1.15.0 safetensors && HF_HOME=/workspace/hf /workspace/venv/bin/hf download Qwen/Qwen3.5-9B --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a'
```

On a new pod every model runs again in (c), the base model included. Use outputs of one pod together. The two
pods of 14 November (same GPU type, different data centers) gave the same 300 base responses, but another GPU
type can flip near-ties.

## Follow-up training

`src/gpu_train_lora.py` trains one LoRA adapter per arm on the pod, with the settings fixed in
`results/study5/deviations.md` (section "Follow-up on a rented GPU"), and saves it in the layout `gpu_eval.py`
loads. The run of 14 November, from `/workspace/study5` with `train_{C,J,K,R}.jsonl` next to the scripts:

```bash
export HF_HOME=/workspace/hf HF_HUB_OFFLINE=1; REV=c202236235762e1c871ad0ccb60c8ee5ba337b9a; PY=/workspace/venv/bin/python
$PY gpu_train_lora.py --arms C J K R --data . --revision $REV --eval-items medqa_eval.jsonl --token-budget 1500 --out adapters_followup --log-dir out_followup
$PY gpu_eval.py --items medqa_eval.jsonl --revision $REV --out out_followup --adapters C3=adapters_followup/C3 J3=adapters_followup/J3 K3=adapters_followup/K3 R3=adapters_followup/R3
```

On the laptop, `src/loop_eval_followup.py` then writes `results/study5/eval_table_followup.md` and `.json`.

Time on the A40: about 5 s per optimiser step, 24 minutes per arm (282 steps), then 3 to 5 minutes of evaluation
per adapter. One forward pass over 16 examples does not fit in 48 GB, so `--token-budget 1500` splits a step into
about four passes of at most 1,500 padded tokens and adds up the gradients (peak 39.5 GB). `--preflight 1500`
measures memory and time of the heaviest step without training. In the run of 14 November arm C was trained
first and loaded by `gpu_eval.py` on 16 questions before the other three arms were started.

## What the script does

- Prompt: one user turn with exactly the item's `qtext`, no system prompt, the model's own chat template with
  `enable_thinking=False`, which ends the prompt with an empty think block.
- Decoding: greedy (no sampling, which is temperature 0), repetition penalty 1, at most 300 new tokens, stop at
  `<|im_end|>` or `<|endoftext|>`.
- Batches: questions are sorted by prompt length and cut into fixed batches, so every model and every rerun
  sees the same batches. Output files keep the order of the items file.
- Adapters: loaded with peft on top of the base model one after another, without merging. The base is loaded
  once, as the text tower of the checkpoint (`Qwen3_5ForCausalLM`).
- The transformers messages about `causal_conv1d` and `flash-linear-attention` are harmless: the reference
  PyTorch code is used, which is exact and slower.

## What was checked

On the first pod, 14 November, before the adapters existed:

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

On the second pod, with the four trained adapters:

| Check | Result |
|---|---|
| Adapter tensors | each of J, F, K, R: 256 of 256 tensors in the model (rank 16, alpha 32, on the q, k, v, o, gate, up and down projections of the text tower), placed by module path. The first-prompt logits move by 18.9 to 20.4, and 300 of 300 responses differ from the base |
| Shipped chat template | the same file in all four folders. It is the base template without three lines, the guard that raises "No user query found in messages". For all 300 questions the prompt is the same text and the same tokens with either template, so one run covers both and no `_shipped` output was written |
| Shipped tokenizer | the same file in all four folders. Against the base `tokenizer.json` it has the same vocabulary and merges, 7 extra audio and speech tokens, a pre-tokenizer pattern without the class of combining marks, and other decoder flags. Loaded on the pod it gives the same tokens for all 300 prompts |
| Format probe, 64 rows of `train_R.jsonl`, mean loss per completion token, base model then the range over the four adapters | chat template with thinking off 2.06 then 0.55 to 0.64. Chat template around the prompt as a JSON string 1.97 then 0.50 to 0.58. Open think tag 1.95 then 1.33 to 1.37. No think tag 1.80 then 1.37 to 1.41. Bare text 1.60 then 1.33 to 1.34. Bare JSON string 1.39 then 1.05 to 1.07 |
| What the probe says | the adapters were trained with the chat template and the empty think block, which is the prompt of the registered evaluation. The drop is the same with and without the JSON wrapping (1.43 to 1.51 against 1.40 to 1.47), so the probe does not show that the service fed the JSON string as text |
| Base model on the second pod | 300 of 300 responses identical to the run on the first pod |
| Base model restored after each adapter | yes, the run did not stop |
