# Two studies for the AI x Epistemics Research Sprint

Work done at the Apart Research AI x Epistemics Research Sprint, November 13 to 15, 2026. The repository holds two independent reports, their pre-registrations, all code, every model call and every number that the reports print.

| | Report A | Report B |
|---|---|---|
| Title | Win Rate Pays for Guessing: LLM Judges Prefer a Wrong Answer to an Honest "I Don't Know" | Removed Notes Account for a Third of AI Writers' Helpful-Rate Advantage on X Community Notes |
| PDF | `paper_A/main.pdf` | `paper_B/main.pdf` |
| Pre-registration | `prereg/A_prereg.md`, commit `26ef52c`, amendment `d816b76` | `prereg/B_prereg.md`, commit `39f5c5b` |
| Data | MedQA and MMLU questions, judged by seven LLMs | Public X Community Notes files, snapshot of 2026-11-14 |

## Prior work

Everything here was written during the sprint. No code, data file or text existed before November 13, 2026. The exploratory pilots that came before each pre-registration are kept in `pilots/`, `tools/cn_pilot.py` and `results/pilot*`, and they are labelled as exploratory.

## Report A

An LLM judge compares two responses to a multiple-choice question with a known key. The responses are fixed sentences, so only the named option and the wording differ. The two key rates are a, the rate at which an assertive right answer beats "I don't know", and b, the same rate for an assertive wrong answer.

| Step | Script | Output |
|---|---|---|
| Build item lists | `src/items.py` | `data/items/` |
| Run duels, the judge's own answers and the detection check | `src/duels.py` | `results/study1_*/calls.jsonl`, `results/study4_*/calls.jsonl` |
| Registered tests and tables | `src/analyze_duels.py` | `results/study1/summary.md`, `results/study4/summary.md` |
| Selection loop: pool, selection, duels on the model's own outputs, training records | `src/loop_*.py` | `results/study5/` |
| Evaluation of fine-tuned models on a GPU | `src/gpu_eval.py`, `src/gpu_train_lora.py`, `docs/gpu_eval_runbook.md` | `results/study5/eval_*` |
| Audit of the data pipeline | `src/adapt_audit2.py`, `src/adapt_analyze.py` | `results/study3/`, `results/study3c/` |
| Numbers, tables and figures of the report | `src/numbers_a.py`, `src/fig_a.py` | `paper_A/numbers.tex`, `paper_A/tab_*.tex`, `paper_A/figs/` |

To rebuild the report from the stored calls, with no API access:

```
python src/analyze_duels.py --runs results/study1_openrouter results/study1_adaption results/study1_frontier \
    --items data/items/medqa_confirm.jsonl data/items/law_confirm.jsonl data/items/geo_confirm.jsonl \
    --out results/study1/summary
python src/numbers_a.py
python src/fig_a.py --style src/paper.mplstyle
cd paper_A && make
```

To rerun the judges you need an `.env` file with `ADAPTION_API_KEY` and `OPENROUTER_API_KEY`. Every call is cached by a hash of its prompt in `calls.jsonl`, so a rerun only sends what is missing.

Fine-tuned adapter weights are not in the repository.

## Report B

`noteStatusHistory` keeps a row for a note after the note has left the public notes file. The analysis compares the helpful rate over notes still in the file with the rate over all notes in the status history, for AI writers and human writers.

| Step | Script | Output |
|---|---|---|
| Registered analysis | `src/cn_confirm.py` | `results/cn_confirm/confirm.md`, `confirm.json` |
| Ratings on removed notes | `src/cn_ratings.py` | `results/cn_confirm/ratings.json` |
| Post hoc checks | `src/cn_posthoc.py` | `results/cn_confirm/posthoc_*.json` |
| Numbers and figures of the report | `src/numbers_b.py`, `src/figs_b.py` | `paper_B/numbers.tex`, `paper_B/figs/` |

The raw files are not in the repository (about 2 GB). Download them from `https://ton.twimg.com/birdwatch-public-data/2026/11/14/` into `data/raw/cn/`. Their SHA-256 values are in the pre-registration. Run every script that reads them with `python3 -I`.

## Layout

```
prereg/      pre-registrations
src/         all code
data/items/  question lists with the planted wrong options
results/     model calls, analysis outputs, logs
paper_A/     report A (LaTeX, generated numbers and tables, PDF)
paper_B/     report B
docs/        sprint brief, literature notes with verified references, runbook
pilots/      exploratory pilots that preceded the pre-registrations
```
