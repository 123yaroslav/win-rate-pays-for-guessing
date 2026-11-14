"""Study 5, step 4: one LoRA fine-tune of the base model per selection rule with AutoScientist.

Rows are chat-format: `prompt` is a JSON list with one user turn (the question with its options, no
system prompt), `completion` is the selected response. One iteration, LoRA, no augmentation, the
hyperparameters the platform recommends for the dataset and model.

    python src/loop_train.py prepare            # results/study5/upload/s5_train_{J,F,K,R}.jsonl
    python src/loop_train.py upload             # raw upload, one dataset per rule
    python src/loop_train.py quote              # recommended hyperparameters (the API has no price quote)
    python src/loop_train.py launch             # four runs
    python src/loop_train.py status             # one status line per run, terminal states are logged
    python src/loop_train.py download           # adapters to results/study5/adapters/{rule}/

Every step is appended to results/study5/autoscientist_runs.jsonl.
"""
from __future__ import annotations

import argparse
import json
import tarfile
import time

from adaption import Adaption

from loop_common import ENV, OUT, read_jsonl

RULES = ["J", "F", "K", "R"]
MODEL = "Qwen/Qwen3.5-9B"
LEDGER = OUT / "autoscientist_runs.jsonl"
UPLOAD = OUT / "upload"
# a raw upload stores the mapped columns under these names, and training must name them
TRAIN_COLUMNS = {"prompt": "original_prompt", "completion": "original_completion"}


def log(rec: dict) -> None:
    with LEDGER.open("a") as f:
        f.write(json.dumps({**rec, "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z")}, default=str) + "\n")


def latest(op: str, attempt: int | None = None) -> dict[str, dict]:
    """The last ledger record of an operation for every rule."""
    out = {}
    for d in read_jsonl(LEDGER):
        if d.get("op") == op and (attempt is None or d.get("attempt") == attempt):
            out[d["rule"]] = d
    return out


def prepare(rules: list[str]) -> None:
    UPLOAD.mkdir(parents=True, exist_ok=True)
    for r in rules:
        rows = read_jsonl(OUT / f"train_{r}.jsonl")
        assert len(rows) == 1500 and len({x["id"] for x in rows}) == 1500, (r, len(rows))
        out = UPLOAD / f"s5_train_{r}.jsonl"
        out.write_text("".join(json.dumps({
            "prompt": json.dumps([{"role": "user", "content": x["prompt"]}]),
            "completion": x["completion"]}) + "\n" for x in rows))
        print(r, len(rows), "->", out)


def upload(c: Adaption, rules: list[str]) -> None:
    done = latest("upload")
    for r in rules:
        if r in done and done[r].get("status") == "succeeded":
            print(r, "already uploaded", done[r]["dataset_id"])
            continue
        f = UPLOAD / f"s5_train_{r}.jsonl"
        n = sum(1 for _ in f.open())
        ds = c.datasets.upload_file(str(f), processing_mode="raw",
                                    column_mapping={"prompt": "prompt", "completion": "completion"})
        st = c.datasets.wait_for_completion(ds.dataset_id)
        print(r, ds.dataset_id, st.status, st.row_count)
        log({"op": "upload", "rule": r, "file": str(f.relative_to(OUT.parents[1])), "rows_local": n,
             "dataset_id": ds.dataset_id, "status": st.status, "rows": st.row_count})


def quote(c: Adaption, rules: list[str]) -> None:
    ds = latest("upload")
    for r in rules:
        hp = c.autoscientist.recommend_hyperparams(dataset_id=ds[r]["dataset_id"], model=MODEL)
        print(r, hp.model, json.dumps(hp.hyperparams.to_dict()))
        log({"op": "recommend", "rule": r, "dataset_id": ds[r]["dataset_id"], "model": hp.model,
             "hyperparams": hp.hyperparams.to_dict(),
             "note": "the API (SDK 0.19) has no price quote and no credit balance endpoint for training runs"})


def launch(c: Adaption, rules: list[str], attempt: int) -> None:
    ds = latest("upload")
    started = latest("train", attempt)
    for r in rules:
        if r in started:
            print(r, "already launched", started[r]["run_id"])
            continue
        run = c.autoscientist.create(dataset_id=ds[r]["dataset_id"], model=MODEL, training_method="instruction",
                                     data_format="chat", max_iterations=1, column_mapping=TRAIN_COLUMNS,
                                     hyperparams={"training_type": "lora"},
                                     idempotency_key=f"s5-{r}-{ds[r]['dataset_id']}-a{attempt}")
        print(r, "run", run.id, run.model, run.status, run.max_iterations)
        log({"op": "train", "rule": r, "attempt": attempt, "dataset_id": ds[r]["dataset_id"], "model": MODEL,
             "run_id": run.id, "launched_unix": time.time(), "response": run.to_dict()})


def status(c: Adaption, rules: list[str], attempt: int) -> None:
    runs = latest("train", attempt)
    final = {(d["rule"], d["run_id"]) for d in read_jsonl(LEDGER) if d.get("op") == "final"}
    for r in rules:
        if r not in runs:
            print(r, "not launched")
            continue
        x = c.autoscientist.get(runs[r]["run_id"])
        d = x.to_dict()
        wall = (x.completed_at - x.created_at).total_seconds() / 60 if x.completed_at else None
        print(r, x.id, x.status, f"iterations {x.iterations_completed}/{x.max_iterations}",
              "best_win_rate", x.best_win_rate, "download", x.download_available,
              "minutes", None if wall is None else round(wall, 1), "error", x.error)
        if x.status in ("succeeded", "failed", "cancelled") and (r, x.id) not in final:
            log({"op": "final", "rule": r, "attempt": attempt, "run_id": x.id, "status": x.status,
                 "best_win_rate": x.best_win_rate, "wall_minutes": wall, "response": d})


def download(c: Adaption, rules: list[str], attempt: int) -> None:
    import zstandard

    runs = latest("train", attempt)
    for r in rules:
        out_dir = OUT / "adapters" / r
        out_dir.mkdir(parents=True, exist_ok=True)
        tgz = out_dir / "checkpoint.tgz"
        with c.autoscientist.with_streaming_response.download(runs[r]["run_id"]) as resp:
            resp.stream_to_file(tgz)
        names = []
        with tgz.open("rb") as fh:                         # streamed, the archive is never held in memory
            if fh.read(4) == b"\x28\xb5\x2f\xfd":            # zstd-compressed tar
                fh.seek(0)
                src, mode = zstandard.ZstdDecompressor().stream_reader(fh), "r|"
            else:
                fh.seek(0)
                src, mode = fh, "r|*"
            with tarfile.open(fileobj=src, mode=mode) as t:
                for m in t:
                    names.append(m.name)
                    t.extract(m, out_dir, filter="data")
        tgz.unlink()
        size = sum(p.stat().st_size for p in out_dir.rglob("*") if p.is_file())
        print(r, "extracted", len(names), "files,", round(size / 1e6, 1), "MB ->", out_dir)
        log({"op": "download", "rule": r, "attempt": attempt, "run_id": runs[r]["run_id"],
             "out": str(out_dir.relative_to(OUT.parents[1])), "files": sorted(names), "bytes": size})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["prepare", "upload", "quote", "launch", "status", "download"])
    ap.add_argument("--rules", nargs="+", default=RULES)
    ap.add_argument("--attempt", type=int, default=1)
    a = ap.parse_args()
    if a.cmd == "prepare":
        prepare(a.rules)
        return
    c = Adaption(api_key=ENV["ADAPTION_API_KEY"])
    if a.cmd == "upload":
        upload(c, a.rules)
    elif a.cmd == "quote":
        quote(c, a.rules)
    elif a.cmd == "launch":
        launch(c, a.rules, a.attempt)
    elif a.cmd == "status":
        status(c, a.rules, a.attempt)
    else:
        download(c, a.rules, a.attempt)


if __name__ == "__main__":
    main()
