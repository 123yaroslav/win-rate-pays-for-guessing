"""Shared pieces of Study 5 (selection loop): paths, the final-line parser, a cached OpenRouter client.

Every call is appended to a JSONL file with the hash of its request, so a stopped run resumes for free.
Attempts that cost money but gave no usable text are appended to the same file as "wasted" lines, so the
sum of `cost` over a file is the full spend of that step.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import random
import re
import time
from pathlib import Path

import httpx
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "study5"
ENV = dict(ln.split("=", 1) for ln in (ROOT / ".env").read_text().splitlines()
           if "=" in ln and not ln.lstrip().startswith("#"))
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SEED = 20261115
BASE_MODEL = "qwen/qwen3.5-9b"
STYLES = ["assert", "hedge", "abstain"]
GEN_MAX_TOKENS = 200
TOTAL_CAP = 2.00                      # OpenRouter spend of the whole study, USD
STEP_FILES = {"gen": "gen_calls.jsonl", "select": "judge_calls.jsonl", "natural": "natural_calls.jsonl"}
STEP_CAPS = {"gen": 0.80, "select": 0.80, "natural": 0.40}


def load_items(path: str | Path) -> list[dict]:
    p = Path(path)
    p = p if p.is_absolute() else ROOT / p
    return [json.loads(ln) for ln in p.read_text().splitlines() if ln.strip()]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(ln) for ln in path.read_text().splitlines() if ln.strip()]


_FINAL = re.compile(r"^final answer\s*:\s*(.*)$", re.I)
_LETTER = re.compile(r"^\(?([A-D])\)?(?:[.):,\s].*)?$")
_IDK = re.compile(r"^i\s+(?:don['’]?t|do\s+not)\s+know\b", re.I)


def parse_final(text: str) -> str:
    """Read the last non-empty line. Returns an option letter, "ABSTAIN" or "UNPARSED"."""
    lines = [ln.strip() for ln in (text or "").strip().splitlines() if ln.strip()]
    if not lines:
        return "UNPARSED"
    m = _FINAL.match(lines[-1].strip("*_`# ").strip())
    if not m:
        return "UNPARSED"
    v = m.group(1).strip("*_` ").strip()
    if _IDK.match(v):
        return "ABSTAIN"
    m2 = _LETTER.match(v)
    return m2.group(1) if m2 else "UNPARSED"


def strict_final(text: str) -> bool:
    """True if the last line is exactly "Final answer: <letter>" or "Final answer: I don't know"."""
    lines = [ln.strip() for ln in (text or "").strip().splitlines() if ln.strip()]
    return bool(lines) and bool(re.fullmatch(r"Final answer: (?:[A-D]|I don't know)", lines[-1]))


def outcome(parsed: str, key: str) -> str:
    if parsed == "ABSTAIN":
        return "abstain"
    if parsed == "UNPARSED":
        return "unparsed"
    return "correct" if parsed == key else "wrong"


def boot_means(cols: np.ndarray, boot: int = 10000, seed: int = SEED, chunk: int = 500) -> np.ndarray:
    """Bootstrap over questions. `cols` is (questions, columns). Returns (boot, columns): the column means of
    every resample. One resample draws the same questions for all columns, so differences are paired."""
    rng = np.random.default_rng(seed)
    n = cols.shape[0]
    out = np.empty((boot, cols.shape[1]))
    p = np.full(n, 1.0 / n)
    for s in range(0, boot, chunk):
        m = min(chunk, boot - s)
        counts = rng.multinomial(n, p, size=m)          # how often each question is drawn
        out[s:s + m] = counts @ cols / n
    return out


def interval(draws: np.ndarray) -> tuple[float, float]:
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return float(lo), float(hi)


def file_spend(path: Path) -> float:
    return sum(float(d.get("cost") or 0) for d in read_jsonl(path))


def study_spend() -> dict[str, float]:
    return {step: file_spend(OUT / f) for step, f in STEP_FILES.items()}


class BudgetReached(SystemExit):
    pass


class Client:
    """OpenRouter chat client with a JSONL cache and a hard budget for one step of the study."""

    def __init__(self, step: str, conc: int = 6, reuse: tuple[str, ...] = ()):
        OUT.mkdir(parents=True, exist_ok=True)
        self.step = step
        self.path = OUT / STEP_FILES[step]
        self.cache: dict[str, dict] = {}
        for d in read_jsonl(self.path):
            if d.get("k"):
                self.cache[d["k"]] = d
        # calls of another step with an identical request can be reused at no cost
        self.other: dict[str, dict] = {}
        for s in reuse:
            for d in read_jsonl(OUT / STEP_FILES[s]):
                if d.get("k"):
                    self.other[d["k"]] = {**d, "reused_from": STEP_FILES[s]}
        spent = study_spend()
        self.spent = spent[step]
        self.budget = min(STEP_CAPS[step], self.spent + TOTAL_CAP - sum(spent.values()))
        self.http = httpx.AsyncClient(timeout=httpx.Timeout(120, connect=20), limits=httpx.Limits(max_connections=16))
        self.sem = asyncio.Semaphore(min(conc, 8))
        self.done = self.fresh = self.failed = self.n429 = 0
        self.t0 = time.time()

    def _write(self, rec: dict) -> None:
        with self.path.open("a") as f:
            f.write(json.dumps(rec) + "\n")

    async def _call(self, body: dict) -> dict:
        if self.spent >= self.budget:
            raise BudgetReached(f"OpenRouter budget of step {self.step} reached: {self.spent:.4f} of {self.budget:.4f}")
        async with self.sem:
            r = await self.http.post(OPENROUTER_URL, json=body,
                                     headers={"Authorization": f"Bearer {ENV['OPENROUTER_API_KEY']}"})
        if r.status_code == 429:
            self.n429 += 1
            await asyncio.sleep(5 + random.random() * 10)
            raise RuntimeError("429")
        if r.status_code == 402:
            raise BudgetReached("OpenRouter answered 402 (out of credits)")
        r.raise_for_status()
        d = r.json()
        if "choices" not in d:
            raise RuntimeError(str(d)[:200])
        return d

    @staticmethod
    def key(model: str, system: str | None, user: str, max_tokens: int, provider: str | None = None) -> str:
        return hashlib.sha256(json.dumps([model, system, user, max_tokens, provider], sort_keys=True).encode()).hexdigest()

    def lookup(self, model: str, system: str | None, user: str, max_tokens: int,
               provider: str | None = None) -> dict | None:
        """The cached record of a request, without calling the API."""
        return self.cache.get(self.key(model, system, user, max_tokens, provider))

    async def ask(self, model: str, system: str | None, user: str, max_tokens: int, meta: dict,
                  provider: str | None = None, tries: int = 8) -> dict | None:
        """Returns the cached or fresh record ({"text", "finish", "provider", ...}) or None after `tries` failures."""
        k = self.key(model, system, user, max_tokens, provider)
        if k in self.cache:
            self.done += 1
            return self.cache[k]
        if k in self.other:
            rec = {**self.other[k], **meta, "cost": 0.0}
            self.cache[k] = rec
            self._write(rec)
            self.done += 1
            return rec
        messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
        body = {"model": model, "messages": messages, "temperature": 0, "max_tokens": max_tokens,
                "usage": {"include": True}, "reasoning": {"enabled": False}}
        if provider:
            body["provider"] = {"order": [provider], "allow_fallbacks": False}
        delay = 2.0
        for _ in range(tries):
            try:
                d = await self._call(body)
                ch = d["choices"][0]
                text = ch["message"].get("content") or ""
                u = d.get("usage") or {}
                cost = float(u.get("cost") or 0)
                self.spent += cost
                base = {"model": model, **meta, "in": u.get("prompt_tokens"), "out": u.get("completion_tokens"),
                        "cost": cost, "finish": ch.get("finish_reason"), "provider": d.get("provider"),
                        "t": round(time.time(), 1)}
                if not text.strip():
                    self._write({"k": None, "wasted": True, **base})
                    raise RuntimeError("empty reply")
                rec = {"k": k, **base, "text": text}
                self.cache[k] = rec
                self._write(rec)
                self.done += 1
                self.fresh += 1
                if self.fresh % 250 == 0:
                    el = time.time() - self.t0
                    print(f"[{time.strftime('%H:%M:%S')}] fresh {self.fresh} done {self.done} failed {self.failed} "
                          f"429s {self.n429} step spend {self.spent:.4f} rate {self.fresh / el * 60:.0f}/min", flush=True)
                return rec
            except BudgetReached:
                raise
            except Exception:  # noqa: BLE001
                await asyncio.sleep(delay + random.random())
                delay = min(delay * 2, 40)
        self.failed += 1
        return None

    async def close(self) -> None:
        await self.http.aclose()
        print(f"step {self.step}: fresh {self.fresh} cached {self.done - self.fresh} failed {self.failed} "
              f"429s {self.n429} step spend {self.spent:.4f} USD (cap {self.budget:.2f})", flush=True)
