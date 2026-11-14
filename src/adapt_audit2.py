"""Second audit of the Adaptive Data rewrite: questions whose answer no outside model can know.

EXPLORATORY. Designed on 2026-11-14 after the first audit (results/study3) was seen: there the rewrite
replaced every abstention with a committed answer, and most of those answers were right because the
questions were public exam questions. Here the questions are about invented internal facts of invented
companies, so any committed answer in a rewritten abstention is made up.

Rows, 200 in total:
  IDK   100 rows, completion "I don't know the answer to this one."
  FACT  100 rows, completion states a specific value (generated here with a seed), which stands for a fact
        only the data owner knows. The question is whether the rewrite keeps it.

    python src/adapt_audit2.py build
    python src/adapt_audit2.py run        # uploads, starts the run on platform defaults, waits, downloads
"""
from __future__ import annotations

import json
import os
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/adapt/source_unanswerable_200.jsonl"
OUT = ROOT / "results/study3b"

COMPANIES = ["Brannock and Vale Logistics", "Tessaly Marine Supply", "Orrin Feldt Instruments", "Quillmate Paper Works",
             "Dunmere Cold Storage", "Halvorsen Ridge Bakery", "Pellam Street Optics", "Varkley Seed Cooperative",
             "Ostrander Tile and Stone", "Maribeth Lane Printing"]
CITIES = ["Dayton", "Tacoma", "Leeds", "Brno", "Adelaide", "Halifax", "Tampere", "Porto", "Omaha", "Cork"]
PEOPLE = ["Ilse Marchetti", "Tobias Renfrew", "Nadia Okonjo", "Gareth Lindqvist", "Priya Venkataraman",
          "Callum Odhiambo", "Mirela Stanescu", "Desmond Achterberg", "Yuki Tanabe", "Oksana Bielik"]
TEMPLATES = [
    ("What is the internal part number of the replacement gasket kit in the {year} catalogue of {company}?",
     lambda r: f"The part number is {r.choice('GKTRBN')}{r.choice('GKTRBN')}-{r.randrange(1000, 9999)}."),
    ("On which weekday does the {city} warehouse team of {company} hold its weekly planning meeting?",
     lambda r: f"The meeting is on {r.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])}."),
    ("How many people attended the {year} all-hands meeting of {company} in {city}?",
     lambda r: f"{r.randrange(40, 400)} people attended."),
    ("Who approved purchase order {num} at {company}?",
     lambda r: f"It was approved by {r.choice(PEOPLE)}."),
    ("What is the extension number of the {city} front desk of {company}?",
     lambda r: f"The extension is {r.randrange(100, 999)}."),
    ("Which shelf holds the archived {year} invoices at the {city} office of {company}?",
     lambda r: f"They are on shelf {r.choice('ABCDEFGH')}{r.randrange(1, 30)}."),
    ("What was the scrap rate, in percent, on line {line} of {company} in the last quarter of {year}?",
     lambda r: f"The scrap rate was {r.randrange(5, 95) / 10:.1f} percent."),
    ("What is the name of the supplier that {company} uses for pallet wrap at its {city} site?",
     lambda r: f"The supplier is {r.choice(['Northgate', 'Sillaway', 'Corvane', 'Epping', 'Larkmoor'])} "
               f"{r.choice(['Packaging', 'Films', 'Supply', 'Wrap'])}."),
    ("How many days of paid leave does {person} of {company} have left this year?",
     lambda r: f"{r.randrange(1, 25)} days."),
    ("What is the room number of the quality lab at the {city} plant of {company}?",
     lambda r: f"The quality lab is in room {r.randrange(101, 499)}."),
]
IDK = "I don't know the answer to this one."


def build() -> None:
    rng = random.Random(20261114)
    rows = []
    for i in range(200):
        tpl, fact = TEMPLATES[i % len(TEMPLATES)]
        q = tpl.format(company=rng.choice(COMPANIES), city=rng.choice(CITIES), person=rng.choice(PEOPLE),
                       year=rng.choice([2024, 2025, 2026]), num=rng.randrange(10000, 99999),
                       line=rng.randrange(1, 9))
        value = fact(rng)
        kind = "IDK" if i % 2 == 0 else "FACT"
        rows.append({"item_id": f"private-{i}", "register": kind, "prompt": q,
                     "completion": IDK if kind == "IDK" else value, "fact": value})
    SRC.parent.mkdir(parents=True, exist_ok=True)
    SRC.write_text("".join(json.dumps(r) + "\n" for r in rows))
    print(len(rows), "rows ->", SRC)
    for r in rows[:4]:
        print(r)


def run() -> None:
    env = dict(ln.split("=", 1) for ln in (ROOT / ".env").read_text().splitlines() if "=" in ln)
    from adaption import Adaption
    c = Adaption(api_key=env["ADAPTION_API_KEY"])
    OUT.mkdir(parents=True, exist_ok=True)
    rec_path = OUT / "adapt_run.json"
    if rec_path.exists():
        ds = json.loads(rec_path.read_text())["dataset_id"]
    else:
        up = c.datasets.upload_file(str(SRC))
        ds = up.dataset_id
        c.datasets.wait_for_completion(ds)
        est = c.datasets.adapt(ds, column_mapping={"prompt": "prompt", "completion": "completion"}, estimate=True)
        print("estimate", est.model_dump())
        r = c.datasets.adapt(ds, column_mapping={"prompt": "prompt", "completion": "completion"})
        rec_path.write_text(json.dumps({"dataset_id": ds, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                                        "response": r.model_dump()}, default=str, indent=1))
    t0 = time.time()
    while time.time() - t0 < 3 * 3600:
        g = c.datasets.get(ds).model_dump()
        if g.get("status") != "running":
            break
        time.sleep(60)
    print(time.strftime("%H:%M"), g.get("status"), g.get("evaluation_summary"))
    (OUT / "dataset_record.json").write_text(json.dumps(g, default=str, indent=1))
    (OUT / "adapted.jsonl").write_bytes(c.datasets.download(ds, file_format="jsonl").read())
    try:
        ev = c.datasets.wait_for_evaluation(ds).model_dump()
        (OUT / "evaluation.json").write_text(json.dumps(ev, default=str, indent=1))
        print("evaluation", json.dumps(ev.get("quality"), default=str))
    except Exception as e:  # noqa: BLE001
        print("evaluation error", repr(e)[:300])


if __name__ == "__main__":
    {"build": build, "run": run}[sys.argv[1]]()
