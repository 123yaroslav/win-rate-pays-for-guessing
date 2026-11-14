"""Diagnose Adaption inference limits: status codes and rate-limit headers under a burst, and
whether a reasoning switch is accepted (so short answers do not come back empty)."""
import asyncio, json, sys, time
from pathlib import Path
import httpx
ROOT = Path(__file__).resolve().parents[1]
KEY = [l.split("=", 1)[1].strip() for l in (ROOT / ".env").read_text().splitlines() if l.startswith("ADAPTION_API_KEY=")][0]
URL = "https://api.prod.adaptionlabs.ai/api/v1/responses"
Q = "A 54-year-old man has crushing chest pain radiating to the left arm with ST elevation in leads II, III and aVF. Which coronary artery is most likely occluded? A. LAD B. RCA C. LCx D. Left main. Reply with only the letter."
async def one(c, model, extra, i):
    t = time.time()
    body = {"model": model, "input": [{"role": "user", "content": Q + f" (probe {i})"}], "temperature": 0, "max_output_tokens": 3000, "store": False, **extra}
    r = await c.post(URL, json=body, headers={"Authorization": f"Bearer {KEY}"})
    hd = {k: v for k, v in r.headers.items() if "rate" in k.lower() or "retry" in k.lower()}
    if r.status_code != 200:
        return (model, i, r.status_code, round(time.time() - t, 1), r.text[:140].replace("\n", " "), hd)
    d = r.json(); u = d.get("usage") or {}
    txt = d.get("output_text") or "".join(x.get("text", "") for it in d.get("output", []) for x in (it.get("content") or []) if x.get("type") == "output_text")
    return (model, i, 200, round(time.time() - t, 1), repr(txt[:30]), d.get("status"), "out", u.get("output_tokens"), "reason", (u.get("output_tokens_details") or {}).get("reasoning_tokens"), hd)
async def main():
    async with httpx.AsyncClient(timeout=120) as c:
        print("--- reasoning switches ---")
        for m in ["deepseek-v4-flash", "qwen3.8-27b", "gemma-4-31b-it"]:
            for extra in [{}, {"reasoning": {"effort": "low"}}, {"reasoning": {"enabled": False}}, {"reasoning": {"effort": "none"}}]:
                try: print(json.dumps(extra), await one(c, m, extra, 0))
                except Exception as e: print(m, extra, "EXC", repr(e)[:100])
        print("--- burst of 40 on gemma ---")
        t = time.time()
        res = await asyncio.gather(*[one(c, "gemma-4-31b-it", {}, i) for i in range(40)], return_exceptions=True)
        codes = {}
        for r in res:
            k = r[2] if isinstance(r, tuple) else "EXC"; codes[k] = codes.get(k, 0) + 1
        print(codes, round(time.time() - t, 1), "s"); print([r for r in res if isinstance(r, tuple) and r[2] != 200][:2])
asyncio.run(main())
