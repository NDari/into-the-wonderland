#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `training` [D-009].

Run: python3 code/checks/training.py
Uses numpy (for 16-bit floating point). Every number printed in the chapter
comes from this output.

Example 8 reads BLOOM-176B's public training log (BigScience, 2022; the file
logs/main/main_log.txt of the Hugging Face repository bigscience/tr11-176B-logs,
pinned to a commit). Per D-018 it is downloaded once into out/cache/ (not
committed) and checked against a pinned SHA-256; the script stops if it differs.
"""
import hashlib
import math
import re
import statistics
import urllib.request
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "out" / "cache"
BLOOM_URL = ("https://huggingface.co/bigscience/tr11-176B-logs/resolve/"
             "67ef5a3a19e97dd114efe55be55ffaca37683638/logs/main/main_log.txt")
BLOOM_LOG = CACHE / "bloom-176b-main_log.txt"
BLOOM_SHA256 = "908ce0dd3cd0c42efa525ebfd94d314861733567f6441c62b98e82bf1d644cf5"
BLOOM_VOCAB = 250_680


def example_steps():
    print("Example 1: tokens per step and steps per run")
    print(f"  BLOOM at full batch: 2,048 sequences x 2,048 tokens = {2048 * 2048:,} predictions per step")
    print(f"  Llama 3 405B: 16 x 8 x 131,072 = 32 x 64 x 8,192 = {32 * 64 * 8192:,} tokens per step")
    print(f"  GPT-3 175B: 3.2M tokens / 2,048 = {3.2e6 / 2048:,.0f} sequences; 300B / 3.2M = {300e9 / 3.2e6:,.0f} steps if full from the start")
    print(f"  LLaMA 65B: 1.4T / 4M = {1.4e12 / 4e6:,.0f} steps")
    secs = 1.4e12 / (380 * 2048)
    print(f"  LLaMA 65B wall clock: 1.4T / (380 tokens/s/GPU x 2,048 GPUs) = {secs / 86400:.1f} days (paper: about 21)")
    print()


def example_mixture():
    print("Example 2: GPT-3's training mix (Table 2.2, as printed)")
    for name, size, weight, epochs in (("Common Crawl (filtered)", 410, 60, 0.44), ("WebText2", 19, 22, 2.9),
                                       ("Books1", 12, 8, 1.9), ("Books2", 55, 8, 0.43), ("Wikipedia", 3, 3, 3.4)):
        print(f"  {name}: {size}B tokens, {weight}% of the mix, {epochs} epochs")
    print(f"  sum of weights: {60 + 22 + 8 + 8 + 3}% (rounding)")
    print()


def example_memory():
    print("Example 3: memory for training with Adam in mixed precision (ZeRO's accounting)")
    per = 2 + 2 + 4 + 4 + 4
    print(f"  16-bit weights 2 + 16-bit gradients 2 + 32-bit master weights 4 + two Adam averages 4 + 4 = {per} bytes per parameter")
    for name, n in (("GPT-2 1.5B", 1.5e9), ("70B", 70e9), ("Llama 3 405B", 405e9)):
        gb = n * per / 1e9
        print(f"  {name}: {gb:,.0f} GB, at least {math.ceil(gb / 80)} GPUs of 80 GB for these alone")
    print()


def example_precision():
    print("Example 4: 16-bit numbers")
    f16 = np.finfo(np.float16)
    print(f"  float16: largest {float(f16.max):,.0f}; smallest normal {float(f16.tiny):.2e}; "
          f"spacing near 1 {float(f16.eps):.2e}")
    print(f"  float16: 2^-24 = {float(np.float16(2.0 ** -24)):.2e} survives; 2^-25 becomes {float(np.float16(2.0 ** -25))}")
    print(f"  float16: 1 + 1/1024 = {float(np.float16(1) + np.float16(1 / 1024)):.6f}; "
          f"1 + 1/4096 = {float(np.float16(1) + np.float16(1 / 4096)):.6f}")

    def bf16(x):
        b = np.array([x], dtype=np.float32).view(np.uint32)[0]
        b = (int(b) + 0x7FFF + ((int(b) >> 16) & 1)) & 0xFFFF0000   # round to nearest even
        return float(np.array([b], dtype=np.uint32).view(np.float32)[0])
    print(f"  bfloat16: 1 + 1/256 = {bf16(1 + 1 / 256)}; 1 + 1/128 = {bf16(1 + 1 / 128)}; 3e38 = {bf16(3e38):.3e}; "
          f"1e-30 = {bf16(1e-30):.3e}")
    print(f"  spacing near 1: float32 {float(np.finfo(np.float32).eps):.2e}, float16 {float(f16.eps):.2e}, bfloat16 {2 ** -7:.2e}")
    print()


def example_failures():
    print("Example 5: Llama 3's interruptions")
    print(f"  466 - 47 planned = {466 - 47} unexpected in 54 days: {466 / 54:.1f} per day, {419 / 54:.1f} unexpected per day")
    print()


def example_weights_vs_data():
    print("Example 6: weights against data (reconstruction)")
    weights = 405e9 * 2
    text = 15.6e12 * 3.94
    print(f"  Llama 3 405B in 16-bit: {weights / 1e9:,.0f} GB; 15.6T tokens x 3.94 characters = {text / 1e12:.1f} trillion "
          f"characters, about {text / weights:.0f} times the weights")
    print(f"  bits of weight per training token: 405B x 16 / 15.6T = {405e9 * 16 / 15.6e12:.2f}")
    print()


def example_dedup():
    print("Example 7: Lee et al. Table 4")
    print(f"  1.926 / 0.189 = {1.926 / 0.189:.1f}; 1.926 / 0.138 = {1.926 / 0.138:.1f}")
    print()


# ---------------------------------------------------------------------------
# BLOOM-176B's log.
LINE = re.compile(
    r"iteration\s+(\d+)/\s*\d+ \| consumed samples:\s+\d+ \| consumed tokens:\s+(\d+) \|"
    r".*?learning rate: ([0-9.E+-]+) \| global batch size:\s+(\d+) \| lm loss: ([0-9.E+-]+) \|"
    r" grad norm: ([0-9.]+|nan|inf)")


def bloom_rows():
    if not BLOOM_LOG.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(BLOOM_URL) as r, open(BLOOM_LOG, "wb") as f:
            while chunk := r.read(1 << 20):
                f.write(chunk)
    h = hashlib.sha256()
    with open(BLOOM_LOG, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    if h.hexdigest() != BLOOM_SHA256:
        raise SystemExit("the BLOOM log does not match its pinned hash")
    rows, order = {}, []
    with open(BLOOM_LOG, encoding="utf-8", errors="replace") as f:
        for line in f:
            if "lm loss" not in line:
                continue
            m = LINE.search(line)
            if not m:
                continue
            it = int(m.group(1))
            rows[it] = (int(m.group(2)), float(m.group(3)), int(m.group(4)), float(m.group(5)), m.group(6))
            order.append(it)   # later lines replace earlier ones after a restart
    restarts = sum(1 for a, b in zip(order, order[1:]) if b < a)
    return rows, restarts


def bloom_series():
    rows, restarts = bloom_rows()
    its = sorted(rows)
    tokens = [rows[i][0] for i in its]
    lr = [rows[i][1] for i in its]
    batch = [rows[i][2] for i in its]
    loss = [rows[i][3] for i in its]
    return its, tokens, lr, batch, loss, rows, restarts


def example_bloom():
    print("Example 8: BLOOM-176B's training log")
    its, tokens, lr, batch, loss, rows, restarts = bloom_series()
    print(f"  {len(its):,} iterations ({its[0]} to {its[-1]}), gaps: {sum(1 for a, b in zip(its, its[1:]) if b - a > 1)}; "
          f"restarts from a checkpoint: {restarts}")
    print(f"  iteration 1: loss {loss[0]:.2f}, batch {batch[0]} sequences; uniform guessing over {BLOOM_VOCAB:,} tokens "
          f"would be ln({BLOOM_VOCAB:,}) = {math.log(BLOOM_VOCAB):.2f}")
    below = next(i for i, l in zip(its, loss) if l < math.log(BLOOM_VOCAB))
    print(f"  loss first below that at iteration {below}")
    k = max(range(len(its)), key=lambda j: lr[j])
    print(f"  learning-rate peak {lr[k]:.1e} at iteration {its[k]}, {tokens[k] / 1e6:.0f}M tokens, loss {loss[k]:.2f}")
    full = next(j for j in range(len(its)) if batch[j] == 2048)
    print(f"  full batch of 2,048 sequences from iteration {its[full]}, {tokens[full] / 1e9:.1f}B tokens, loss {loss[full]:.2f}")
    for target in (1e9, 1e10, 5e10, 1e11, 2e11, 3e11, 3.41e11):
        j = next(j for j in range(len(its)) if tokens[j] >= target)
        print(f"  at {target / 1e9:.0f}B tokens: loss {loss[j]:.2f}")
    s = max(range(len(its)), key=lambda j: loss[j] if tokens[j] > 1e10 else 0)
    print(f"  largest spike: iteration {its[s]}, {tokens[s] / 1e9:.2f}B tokens, loss {loss[s]:.2f} "
          f"(previous {loss[s - 1]:.2f}), grad norm {rows[its[s]][4]}")
    print(f"  loss {loss[s + 11]:.2f} at iteration {its[s + 11]}, {loss[s + 31]:.2f} at iteration {its[s + 31]}")
    print(f"  end: iteration {its[-1]:,}, {tokens[-1] / 1e9:.1f}B tokens, loss {loss[-1]:.3f} nats "
          f"= {loss[-1] / math.log(2):.2f} bits; learning rate {lr[-1]:.2e}")
    print(f"  median of the first 500 iterations {statistics.median(loss[:500]):.2f}; of the last 500 {statistics.median(loss[-500:]):.2f}")
    print()


if __name__ == "__main__":
    example_steps()
    example_mixture()
    example_memory()
    example_precision()
    example_failures()
    example_weights_vs_data()
    example_dedup()
    example_bloom()
