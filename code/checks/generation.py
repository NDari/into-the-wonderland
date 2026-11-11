#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `generation` [D-009].

Run: python3 code/checks/generation.py
Standard library only. Every number printed in the chapter comes from this
output. The running example reuses the destination chapter's scores and its
random draw (imported from code/checks/destination.py), so the two chapters
share one example.
"""
import importlib.util
import math
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "destination_checks", Path(__file__).resolve().parent / "destination.py")
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)

TOKENS = [t.strip() for t, _ in D.LOGITS]
SCORES = [s for _, s in D.LOGITS]


def softmax_t(scores, t):
    m = max(scores)
    e = [math.exp((s - m) / t) for s in scores]
    z = sum(e)
    return [x / z for x in e]


def entropy_bits(p):
    return -sum(x * math.log2(x) for x in p if x > 0)


def pick(probs, draw):
    lo = 0.0
    for tok, p in zip(TOKENS, probs):
        if lo <= draw < lo + p:
            return tok, lo, lo + p
        lo += p
    return TOKENS[-1], lo, 1.0


TEMPS = (0.5, 1.0, 2.0)


def example_temperature():
    print(f"Example 1: temperature on the destination's scores for '{D.CONTEXT} ...'")
    print("  tokens: " + ", ".join(TOKENS) + "; scores " + ", ".join(f"{s:g}" for s in SCORES))
    for t in (0.25, 0.5, 0.7, 1.0, 1.5, 2.0, 5.0):
        p = softmax_t(SCORES, t)
        print(f"  T = {t}: " + ", ".join(f"{x:.3f}" for x in p) + f"; entropy {entropy_bits(p):.3f} bits")
    print(f"  uniform over six tokens: {math.log2(6):.3f} bits")
    for t in TEMPS:
        print(f"  mat/floor probability ratio at T = {t}: {math.exp(1 / t):.2f}")
    for t in TEMPS:
        tok, lo, hi = pick(softmax_t(SCORES, t), D.DRAW)
        print(f"  draw {D.DRAW} at T = {t}: '{tok}' (band {lo:.3f} to {hi:.3f})")
    print()


def truncate_top_k(p, k):
    keep = sorted(range(len(p)), key=lambda i: -p[i])[:k]
    z = sum(p[i] for i in keep)
    return keep, z, {i: p[i] / z for i in keep}


def truncate_top_p(p, top_p):
    order = sorted(range(len(p)), key=lambda i: -p[i])
    keep, z = [], 0.0
    for i in order:
        keep.append(i)
        z += p[i]
        if z >= top_p:
            break
    return keep, z, {i: p[i] / z for i in keep}


def example_truncation():
    print("Example 2: top-k and top-p at T = 1")
    p = softmax_t(SCORES, 1.0)
    cum = 0.0
    cums = []
    for x in sorted(p, reverse=True):
        cum += x
        cums.append(cum)
    print("  cumulative: " + ", ".join(f"{c:.3f}" for c in cums))
    for k in (2, 3):
        keep, z, new = truncate_top_k(p, k)
        print(f"  top-k = {k}: keeps {z:.3f} of the probability; renormalized "
              + ", ".join(f"{TOKENS[i]} {new[i]:.3f}" for i in keep))
    for tp in (0.75, 0.9, 0.95):
        keep, z, new = truncate_top_p(p, tp)
        print(f"  top-p = {tp}: keeps {len(keep)} tokens ({z:.3f}); renormalized "
              + ", ".join(f"{TOKENS[i]} {new[i]:.3f}" for i in keep))
    for t in TEMPS:
        keep, _, _ = truncate_top_p(softmax_t(SCORES, t), 0.9)
        print(f"  temperature {t} applied first, then top-p 0.9: keeps {len(keep)} tokens")
    print()


def example_flat_vs_peaked():
    print("Example 3: a fixed k against a flat and a peaked distribution (constructed)")
    peaked = softmax_t(SCORES, 0.5)
    keep, z, _ = truncate_top_p(peaked, 0.9)
    print(f"  peaked (the T = 0.5 distribution): top-p 0.9 keeps {len(keep)}; top-k 3 keeps "
          f"{', '.join(TOKENS[i] for i in truncate_top_k(peaked, 3)[0])}")
    # 20 plausible tokens with equal scores, 1,000 tail tokens 7 points lower.
    flat_scores = [0.0] * 20 + [-7.0] * 1000
    flat = softmax_t(flat_scores, 1.0)
    keep, z, _ = truncate_top_p(flat, 0.9)
    print(f"  flat: 20 plausible tokens each {flat[0]:.4f}, 1,000 tail tokens each {flat[-1]:.6f}, "
          f"tail total {sum(flat[20:]):.3f}")
    print(f"  flat: top-p 0.9 keeps {len(keep)} tokens, {sum(1 for i in keep if i < 20)} of them plausible; "
          f"top-k 3 keeps 3 of the 20 plausible ones")
    print()


def example_sequences():
    print("Example 4: twenty steps at a time (toy: the same distribution at every step)")
    for t in (1.0, 0.5, 0.25):
        top = softmax_t(SCORES, t)[0]
        print(f"  T = {t}: chance all 20 draws are the top token {top ** 20:.3g} (1 in {1 / top ** 20:,.0f}); "
              f"expected non-top picks {20 * (1 - top):.1f}")
    print()


def example_kv():
    print("Example 5: KV cache size (16-bit numbers, 2 bytes each)")
    def per_token(layers, kv_dim):
        return 2 * layers * kv_dim * 2
    g = per_token(12, 768)
    print(f"  GPT-2 small: 2 x 12 x 768 x 2 = {g:,} bytes per token; 1,024 tokens: {g * 1024 / 1e6:.1f} MB")
    l3 = per_token(32, 8 * 128)
    print(f"  Llama 3 8B: 2 x 32 x (8 x 128) x 2 = {l3:,} bytes = {l3 // 1024} KiB per token; "
          f"8,192 tokens {l3 * 8192 / 2 ** 30:.0f} GiB; 131,072 tokens {l3 * 131072 / 2 ** 30:.0f} GiB ({l3 * 131072 / 1e9:.1f} GB)")
    l3full = per_token(32, 32 * 128)
    print(f"  without grouping (32 key-value heads): {l3full * 131072 / 2 ** 30:.0f} GiB at 131,072 tokens")
    n8b = 8_028_164_096   # code/checks/anatomy.py, Example 3 (from the Llama 3 paper's Table 3)
    print(f"  Llama 3 8B weights in 16-bit: {n8b:,} x 2 = {n8b * 2 / 1e9:.1f} GB")
    opt = 2 * 5120 * 40 * 2
    print(f"  Kwon et al.'s OPT-13B check: {opt:,} bytes = {opt / 1024:.0f} KiB per token; x 2,048 = {opt * 2048 / 1e9:.2f} GB")
    m, n = 1000, 500
    redo = n * m + n * (n + 1) // 2
    print(f"  writing {n} tokens after a {m}-token prompt: {redo:,} positions recomputed without a cache, "
          f"{m + n:,} with one ({redo / (m + n):.0f} times fewer)")
    print()


def example_speeds():
    print("Example 6: printed speed ratios and speculative decoding")
    print(f"  Shazeer (2019): decoder 46 us vs encoder 1.7 us per token: {46 / 1.7:.0f} times")
    for a in (0.6, 0.8, 0.9):
        row = ", ".join(f"{g} guesses {(1 - a ** (g + 1)) / (1 - a):.2f}" for g in (2, 4, 8))
        print(f"  acceptance {a}: tokens per big-model pass: {row}")
    print(f"  Thinking Machines: 992 + 8 = {992 + 8}")
    print()


if __name__ == "__main__":
    example_temperature()
    example_truncation()
    example_flat_vs_peaked()
    example_sequences()
    example_kv()
    example_speeds()
