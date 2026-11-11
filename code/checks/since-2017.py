#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `since-2017` [D-009].

Run: python3 code/checks/since-2017.py
Standard library only. Every number printed in the chapter comes from this
output. Model shapes are typed in from their published sources:
Transformer base: Vaswani et al. 2017, Table 3. Llama 3 8B: Grattafiori et al.
2024, Table 3. Mistral 7B: Jiang et al. 2023, Table 1. Mixtral 8x7B: Jiang et
al. 2024, Table 1. Measured numbers (BLEU, seconds, perplexities) are typed in
from the tables cited next to them. The masked softmax is imported from
code/checks/anatomy.py so the two chapters use the same function.
"""
import importlib.util
import math
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "anatomy_checks", Path(__file__).resolve().parent / "anatomy.py")
A = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(A)
softmax = A.softmax          # handles -inf (masked) entries

# Shapes used by the chapter and by figures/since-2017.py.
BASE_2017 = dict(d=512, ff=2048, heads=8, head_dim=64, layers=6)               # Vaswani Table 3
LLAMA3_8B = dict(d=4096, ff=14336, heads=32, kv_heads=8, head_dim=128, layers=32,
                 rope_base=500_000)                                             # Llama 3 Table 3
MIXTRAL = dict(d=4096, layers=32, head_dim=128, ff=14336, heads=32, kv_heads=8,
               vocab=32000, experts=8, top_k=2)                                 # Mixtral Table 1
ROUTER_SCORES = [1.2, -0.3, 2.1, 0.4, -1.0, 1.7, 0.1, -0.6]                    # made up, 8 experts


def mean(xs):
    return sum(xs) / len(xs)


def layer_norm(x):
    m = mean(x)
    sd = math.sqrt(mean([(v - m) ** 2 for v in x]))      # population sd, Zhang and Sennrich Eq. 3
    return [(v - m) / sd for v in x], m, sd


def rms_norm(x):
    rms = math.sqrt(mean([v * v for v in x]))
    return [v / rms for v in x], rms


def fmt(xs, n=4):
    return "(" + ", ".join(f"{v:.{n}f}" for v in xs) + ")"


def example_norms():
    print("Example 1: LayerNorm and RMSNorm on four numbers (gain 1, no bias)")
    for x in ([2, -1, 3, 0], [4, 1, 5, 2], [3, 0, -3, 0]):
        ln, m, sd = layer_norm(x)
        rn, rms = rms_norm(x)
        print(f"  x = {tuple(x)}: mean {m:g}, sd {sd:.4f}, RMS {rms:.4f}; LayerNorm {fmt(ln)}; RMSNorm {fmt(rn)}")
    print("  (the second x is the first shifted by 2: LayerNorm output unchanged, RMSNorm changed;")
    print("   the third has mean 0: the two agree)")
    ln_s, rms_s = 248, 231            # Zhang and Sennrich Table 4: seconds per 1k steps, Transformer base
    print(f"  Transformer timing: ({ln_s} - {rms_s}) / {ln_s} = {(ln_s - rms_s) / ln_s:.1%} faster; "
          f"pRMSNorm 225 s: {(ln_s - 225) / ln_s:.1%}")
    print(f"  RNN translation (Table 2): (665 - 501) / 665 = {(665 - 501) / 665:.1%}; "
          f"image-caption model (Table 8): (12.02 - 7.12) / 12.02 = {(12.02 - 7.12) / 12.02:.1%}")
    print()


def example_ffn():
    print("Example 2: the feed-forward network, two matrices or three")
    d, ff = 768, 3072
    two = 2 * d * ff
    three = 3 * d * 2048
    print(f"  Shazeer's T5 base: 2 x {d} x {ff:,} = {two:,}; 3 x {d} x 2,048 = {three:,}; equal: {two == three}")
    L = LLAMA3_8B
    swiglu = 3 * L["d"] * L["ff"]
    relu4d = 2 * L["d"] * 4 * L["d"]
    print(f"  Llama 3 8B: 3 x 4,096 x 14,336 = {swiglu:,}; a 2017-style 4d network 2 x 4,096 x 16,384 = {relu4d:,} "
          f"({swiglu / relu4d:.2f} times)")
    print(f"  14,336 / 4,096 = {L['ff'] / L['d']}; LLaMA's 2/3 x 4d = {2 / 3 * 4 * L['d']:.1f}")
    b = BASE_2017
    print(f"  Transformer base FFN: {b['d']} -> {b['ff']:,} -> {b['d']}")
    relu, swi = 1.677, 1.636                      # Shazeer 2020 Table 1, 524,288 steps
    print(f"  held-out log-perplexity ReLU {relu} vs SwiGLU {swi}: {relu - swi:.3f} lower ({(relu - swi) / relu:.1%})")
    print(f"  GELU(x) = x * Phi(x): x = 2 -> {2 * 0.5 * (1 + math.erf(2 / math.sqrt(2))):.3f}; "
          f"x = -2 -> {-2 * 0.5 * (1 + math.erf(-2 / math.sqrt(2))):.3f}; x = 0.5 -> "
          f"{0.5 * 0.5 * (1 + math.erf(0.5 / math.sqrt(2))):.3f}")
    print()


def rotate(v, angle):
    c, s = math.cos(angle), math.sin(angle)
    return (c * v[0] - s * v[1], s * v[0] + c * v[1])


ROPE_Q, ROPE_K, ROPE_STEP = (1.0, 2.0), (3.0, -1.0), 0.5


def rope_score(m, n, q=ROPE_Q, k=ROPE_K, step=ROPE_STEP):
    qr, kr = rotate(q, m * step), rotate(k, n * step)
    return qr[0] * kr[0] + qr[1] * kr[1]


def example_rope():
    print(f"Example 3: rotary positions on one pair of numbers, q = {ROPE_Q}, k = {ROPE_K}, {ROPE_STEP} radians per position")
    for m, n in ((3, 1), (10, 8), (100, 98), (5, 5), (1, 3)):
        print(f"  query at {m}, key at {n} (gap {m - n:+d}): score {rope_score(m, n):.4f}")
    d = 128
    for base in (10_000, 500_000):
        fast = 2 * math.pi
        slow = 2 * math.pi * base ** ((d - 2) / d)
        print(f"  base {base:,}, {d}-number head: fastest pair turns once every {fast:.2f} positions, "
              f"slowest once every {slow:,.0f}")
    k = 16
    print(f"  Shaw et al. clipping k = {k}: 2k + 1 = {2 * k + 1} learned distance vectors per layer and head")
    print()


def alibi_slopes(n_heads):
    start = 2 ** (-8 / n_heads)
    return [start ** (i + 1) for i in range(n_heads)]


def example_alibi():
    print("Example 4: ALiBi")
    s8 = alibi_slopes(8)
    print("  slopes, 8 heads: " + ", ".join(f"1/{round(1 / s)}" for s in s8) + f" ({s8[0]:.5f} to {s8[-1]:.5f})")
    print(f"  slopes, 16 heads: first {alibi_slopes(16)[0]:.5f}")
    m = 0.5
    print(f"  5 x 5 causal bias table, slope {m} (row = query position, blank = masked):")
    for i in range(5):
        row = [f"{-m * (i - j) + 0.0:5.1f}" if j <= i else "     " for j in range(5)]
        print("   " + " ".join(row))
    raw = [0.0] * 5                                   # equal raw scores, distances 0..4
    w = softmax([r - m * dist for dist, r in enumerate(raw)])
    print("  equal raw scores, distances 0-4: factors " + ", ".join(f"{math.exp(-m * t):.4f}" for t in range(5))
          + "; weights " + ", ".join(f"{x:.4f}" for x in w))
    print()


def example_interpolation():
    print("Example 5: stretching a rotary model after training")
    print(f"  LLaMA 2,048 -> 32,768: positions multiplied by 2,048 / 32,768 = 1/{32768 // 2048}")
    print(f"  Chen et al.'s figure, 2,048 -> 4,096: position 3,000 becomes {3000 * 2048 / 4096:,.0f}")
    print(f"  YaRN vs PI (Llama 2 7B, 4k -> 8k): 1,000 / 400 = {1000 / 400} times fewer steps")
    print(f"  Llama 2 long-context table: NarrativeQA F1 0.21 (2k) vs 17.26 (4k); HellaSwag 75.1 vs 74.8")
    gpu = {"pre-training": 2664, "context extension": 119, "post-training": 5}   # DeepSeek-V3 Table 1, K GPU hours
    tot = sum(gpu.values())
    print(f"  DeepSeek-V3 GPU hours (thousands): {gpu}; total {tot:,}; "
          f"context extension {gpu['context extension'] / tot:.1%}")
    print()


def kv_bytes_per_token(layers, kv_heads, head_dim, bytes_per=2):
    return 2 * layers * kv_heads * head_dim * bytes_per      # keys and values


def example_kv():
    print("Example 6: fewer key-value heads (Llama 3 8B, 16-bit); same formula as code/checks/generation.py Example 5")
    L = LLAMA3_8B
    for name, kv in (("32 (multi-head)", 32), ("8 (grouped, as released)", 8), ("1 (multi-query)", 1)):
        b = kv_bytes_per_token(L["layers"], kv, L["head_dim"])
        print(f"  {name}: {b:,} bytes = {b // 1024} KiB per token; 131,072 tokens {b * 131072 / 1e9:.1f} GB")
    print(f"  Shazeer 2019 decoder step: 46 / 3.8 = {46 / 3.8:.1f} times; BLEU 26.7 -> 26.5")
    print(f"  Ainslie et al. Table 1: MHA-XXL 1.51 ms / GQA-8 0.28 = {1.51 / 0.28:.1f} times; "
          f"/ MQA 0.24 = {1.51 / 0.24:.1f} times; scores 47.2, 47.1, 46.6")
    print()


def example_flash():
    print("Example 7: the attention score matrix, one head, one layer, 16-bit")
    for n in (1024, 2048, 8192, 131072, 1048576):
        b = n * n * 2
        # Decimal units (1 MB = 10^6 bytes), the book's convention; same figures as code/checks/notation.py Example 1.
        unit = "MB" if b < 10 ** 9 else ("GB" if b < 10 ** 12 else "TB")
        div = {"MB": 10 ** 6, "GB": 10 ** 9, "TB": 10 ** 12}[unit]
        print(f"  {n:>9,} tokens: {n * n:>17,} scores, {b:,} bytes = {b / div:.1f} {unit}")
    out = 131072 * 128 * 2
    print(f"  the output it is used to make, 131,072 x 128 x 2 bytes = {out:,} bytes = {out / 10 ** 6:.1f} MB")
    print(f"  A100 on-chip memory: 192 kB x 108 = {192 * 108:,} kB (about {192 * 108 / 1000:.0f} MB) "
          f"against 40-80 GB main memory")
    print()


def example_sparse():
    print("Example 8: sparse and sliding-window attention")
    for n in (1024, 16384, 65536):
        print(f"  {n:,} tokens: n^2 {n * n:,} vs n x sqrt(n) {int(n * math.sqrt(n)):,}: {math.sqrt(n):.0f} times fewer")
    print(f"  Mistral 7B: 32 layers x 4,096 window = {32 * 4096:,} positions 'theoretical' span; "
          f"cache at 32,768 tokens: 32,768 / 4,096 = {32768 // 4096} times smaller")
    print()


CONTEXTS = [  # (model, year, tokens, source note)
    ("GPT-1", "2018", 512, "paper"),
    ("GPT-2", "2019", 1024, "paper"),
    ("GPT-3", "2020", 2048, "paper"),
    ("LLaMA", "2023", 2048, "paper"),
    ("Llama 2", "2023", 4096, "paper"),
    ("Mistral 7B", "2023", 8192, "paper"),
    ("Mixtral 8x7B", "2024", 32768, "paper"),
    ("Llama 3 (3.1)", "2024", 131072, "paper"),
    ("DeepSeek-V3", "2024", 131072, "paper"),
]


def example_context():
    print("Example 9: context windows and the square")
    for name, year, n, _ in CONTEXTS:
        print(f"  {name} ({year}): {n:,}")
    for n in (131072, 1048576):
        print(f"  512 -> {n:,}: {n // 512:,} times longer, {(n // 512) ** 2:,} times more scores per head per layer")
    print()


def mixtral_counts(n_experts_used):
    M = MIXTRAL
    d = M["d"]
    attn = d * (M["heads"] * M["head_dim"]) * 2 + d * (M["kv_heads"] * M["head_dim"]) * 2
    expert = 3 * d * M["ff"]
    router = d * M["experts"]
    norms = 2 * d
    tables = 2 * M["vocab"] * d
    per_layer = attn + n_experts_used * expert + router + norms
    return M["layers"] * per_layer + tables + d, attn, expert, router, tables


def example_moe():
    print("Example 10: mixture of experts")
    total, attn, expert, router, tables = mixtral_counts(MIXTRAL["experts"])
    active, *_ = mixtral_counts(MIXTRAL["top_k"])
    print(f"  Mixtral per layer: attention {attn:,}; one SwiGLU expert {expert:,}; router {router:,}; norms {2 * 4096:,}")
    print(f"  tables {tables:,}; total {total:,} ({total / 1e9:.1f}B, printed 47B); "
          f"active (2 experts) {active:,} ({active / 1e9:.1f}B, printed 13B)")
    print(f"  active share {active / total:.1%}; experts' share of all parameters "
          f"{MIXTRAL['layers'] * MIXTRAL['experts'] * expert / total:.1%}; naive 8 x 7 = 56")
    no_moe = MIXTRAL["layers"] * (attn + expert + 2 * 4096) + tables + 4096
    print(f"  same shape with one feed-forward block (Mistral 7B): {no_moe:,}")
    for name, a, t in (("Mixtral", 13, 47), ("DeepSeek-V3", 37, 671), ("Llama 4 Scout", 17, 109),
                       ("Llama 4 Maverick", 17, 400)):
        print(f"  {name}: {a}B of {t}B active = {a / t:.2%}")
    print(f"  Llama 2 70B vs Mixtral active: 70 / 13 = {70 / 13:.1f}")
    s = ROUTER_SCORES
    top = sorted(range(len(s)), key=lambda i: -s[i])[:2]
    masked = [s[i] if i in top else -math.inf for i in range(len(s))]
    w = softmax(masked)
    print(f"  toy router scores {s}: top 2 are experts {[i + 1 for i in sorted(top)]}; "
          f"weights " + ", ".join(f"expert {i + 1} {w[i]:.3f}" for i in sorted(top)))
    print(f"  Shazeer 2017 low-budget MoE: 8.9 / 151 = {8.9 / 151:.1%} of the computation per time step")
    print(f"  DeepSeek-V3: 2,788K GPU hours x $2 = ${2.788 * 2:.3f}M (official run only)")
    print(f"  Switch-C: 1,571B parameters over 2,048 experts")
    print()


if __name__ == "__main__":
    example_norms()
    example_ffn()
    example_rope()
    example_alibi()
    example_interpolation()
    example_kv()
    example_flash()
    example_sparse()
    example_context()
    example_moe()
