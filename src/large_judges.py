"""Amendment 4, part A. Two larger judges on fresh multiple-choice and free-form questions.

Runs the analyses of Amendments 2 and 3 unchanged on results/confirm2_large and results/freeform_large,
then applies the tests L1 to L3.

    python src/large_judges.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import confirm2  # noqa: E402
import freeform  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LARGE = ["adaption/qwen3.5-397b", "adaption/glm-5.2"]


def main() -> None:
    c = confirm2.main(["results/confirm2_large"], LARGE, "results/large/confirm")
    f = freeform.analyze(["results/freeform_large"], LARGE, "results/large/free")
    ck = [j for j in c["judges"] if not c["judges"][j]["dropped"]]
    fk = [j for j in f["judges"] if not f["judges"][j]["dropped"]]
    tests = {
        "L1_pass": sum(c["judges"][j]["c1_pass"] for j in ck), "L1_judges": len(ck),
        "L2_pass": sum(c["judges"][j]["c2_pass"] for j in ck),
        "L3_pass": sum(f["judges"][j].get("f1_pass", False) for j in fk), "L3_judges": len(fk),
    }
    tests["L1_holds"] = tests["L1_pass"] == len(LARGE)
    tests["L2_holds"] = tests["L2_pass"] == len(LARGE)
    tests["L3_holds"] = tests["L3_pass"] >= 1
    out = {"confirm": c["judges"], "free": f["judges"], "tests": tests}
    od = ROOT / "results/large"
    od.mkdir(parents=True, exist_ok=True)
    (od / "summary.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(tests, indent=1))


if __name__ == "__main__":
    main()
