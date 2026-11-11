#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `local` [D-009].

Run: python3 code/checks/local.py
Standard library only. Every number printed in the chapter, its tables, and
its figures (figures/local.py imports this file [D-014]) comes from this
output. Inputs are hard-coded with the claim in book1/sources/local.md that
sources them (LCnn). The KV-cache formula is the generation chapter's; this
file imports code/checks/generation.py and checks that it gives the same
per-token size for Llama 3 8B. 1 GB = 10^9 bytes, as in `destination`.
"""
import contextlib
import importlib.util
import io
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "generation_checks", Path(__file__).resolve().parent / "generation.py")
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

GB = 1e9
GIB = 2 ** 30

# Exact parameter counts from the Hugging Face model API, read 2026-11-11
# (LC26, field safetensors.total).
PARAMS = {
    "Llama 3.2 1B": 1_235_814_400,
    "Llama 3.2 3B": 3_212_749_824,
    "Phi-3-mini": 3_821_079_552,
    "Mistral 7B": 7_241_732_096,
    "Llama 3.1 8B": 8_030_261_248,
    "Qwen3-8B": 8_190_735_360,
    "Mixtral 8x7B": 46_702_792_704,
    "Llama 3.1 70B": 70_553_706_496,
}
TABLE_MODELS = ["Llama 3.2 1B", "Llama 3.2 3B", "Phi-3-mini", "Llama 3.1 8B",
                "Qwen3-8B", "Mixtral 8x7B", "Llama 3.1 70B"]

# Bits per weight. Pure types from llama.cpp's block layouts (LC33): a block
# of numbers plus its scales. Mixed types (the _M variants and Q2_K) from the
# llama.cpp README's table for Llama 3.1 8B (LC31): measured on that model;
# other models differ slightly.
BITS = {
    "F16": 16.0,
    "Q8_0": 8.5,
    "Q6_K": 6.5625,
    "Q5_K_M": 5.7036,
    "Q4_K_M": 4.8944,
    "Q4_0": 4.5,
    "Q3_K_M": 3.9960,
    "Q2_K": 3.1593,
}
TABLE_TYPES = ["F16", "Q8_0", "Q6_K", "Q5_K_M", "Q4_K_M", "Q3_K_M", "Q2_K"]

# Architecture for the KV cache: layers, key-value heads, head dimension.
# Llama 3.1 from the Llama 3 paper's Table 3 (LC20; head dimension 4,096/32
# and 8,192/64); Qwen3-8B and Phi-3-mini from their Hub config files (LC26).
ARCH = {
    "Llama 3.1 8B": (32, 8, 4096 // 32),
    "Qwen3-8B": (36, 8, 128),
    "Llama 3.1 70B": (80, 8, 8192 // 64),
    "Phi-3-mini": (32, 32, 3072 // 32),
}
PHI3_WINDOW = 4096          # Phi-3-mini-4k config, max_position_embeddings (LC26)
CONTEXTS = (8192, 32768)    # the chapter's fixed context lengths ("8K", "32K")

# Peak memory bandwidth in GB/s, vendor figures with their dates (LC50), and
# the largest memory each offers in GB (same sources; None if not sourced).
DEVICES = [
    ("Apple M4 (2024-10)", 120, 32),
    ("Apple M5 (2025-10)", 153, None),
    ("Apple M4 Pro (2024-10)", 273, 64),
    ("Apple M4 Max (2024-10)", 546, 128),
    ("NVIDIA RTX 4080", 716.8, 16),
    ("NVIDIA RTX 4090", 1008, 24),
    ("NVIDIA RTX 5090", 1792, 32),
]


def weight_gb(n, bits):
    return n * bits / 8 / GB


def kv_bytes_per_token(layers, kv_heads, head_dim, bits=16):
    """2 (key and value) x layers x KV heads x head dimension x bytes per number."""
    return 2 * layers * kv_heads * head_dim * bits / 8


def example_blocks():
    print("Example 1: bits per weight from llama.cpp's block layouts (LC33)")
    q4_0 = (32 * 4 + 16) / 32
    q8_0 = (32 * 8 + 16) / 32
    print(f"  Q4_0: 32 weights x 4 bits + one 16-bit scale = {32 * 4 + 16} bits / 32 = {q4_0} bits per weight")
    print(f"  Q8_0: 32 x 8 + 16 = {32 * 8 + 16} bits / 32 = {q8_0}")
    print(f"  the scale's share: 16 / 32 = {16 / 32} extra bits per weight")
    for name, nbytes in (("Q2_K", 84), ("Q3_K", 110), ("Q4_K", 2 + 2 + 12 + 128), ("Q5_K", 176), ("Q6_K", 210)):
        print(f"  {name}: {nbytes} bytes per super-block of 256 weights = {nbytes * 8 / 256} bits per weight")
    print(f"  GPTQ group of 128 with one 16-bit scale: {16 / 128:.3f} extra bits; "
          f"with a 3-bit zero point too: {(16 + 3) / 128:.3f} (paper: about 0.15)")
    print(f"  Q4_K_M vs Q4_K_S (README, Llama 3.1 8B): 4.8944 vs 4.6672 bits per weight ({4.8944:.2f} vs {4.6672:.2f})")
    print("  bits per weight as printed in the chapter: "
          + ", ".join(f"{t} {BITS[t]:.2f}" for t in TABLE_TYPES))
    for g in (8, 32):
        print(f"  4-bit numbers in groups of {g} with a 16-bit scale: {(g * 4 + 16) / g} bits per weight")
    print()


# Example 2: made-up weights, rounded to 4 bits with one shared scale.
# Absmax rounding to the integers -7..7, a simplification of llama.cpp's
# simplest 4-bit type, not identical to it. Illustrative numbers [D-002].
DEMO = [0.12, -0.31, 0.05, 0.27, -0.08, 0.19, -0.22, 0.02]
OUTLIER_FACTOR = 20          # LLM.int8(): outliers "up to 20x larger" (LC36)
LEVELS = 7


def absmax_round(ws):
    s = max(abs(w) for w in ws) / LEVELS
    q = [round(w / s) for w in ws]
    return s, q, [s * x for x in q]


def demo_cases():
    """Return the three cases used in the chapter and the figure."""
    base = list(DEMO)
    out = list(DEMO)
    out[-1] = OUTLIER_FACTOR * max(abs(w) for w in DEMO[:-1])
    cases = {}
    s, q, r = absmax_round(base)
    cases["no outlier"] = (base, s, q, r)
    s, q, r = absmax_round(out)
    cases["outlier, one scale"] = (out, s, q, r)
    # Outlier kept aside in 16 bits; the other seven share their own scale.
    s, q, r = absmax_round(out[:-1])
    cases["outlier kept aside"] = (out, s, q + [None], r + [out[-1]])
    return cases


def mean_abs_err(ws, rs, n=7):
    return sum(abs(w - r) for w, r in zip(ws[:n], rs[:n])) / n


def example_rounding():
    print("Example 2: rounding eight made-up weights to 4 bits (absmax, integers -7..7)")
    cases = demo_cases()
    for name, (ws, s, q, r) in cases.items():
        print(f"  {name}: weights " + ", ".join(f"{w:g}" for w in ws))
        print(f"    scale {s:.4f}; stored integers " + ", ".join("16-bit" if x is None else str(x) for x in q))
        print("    reconstructed " + ", ".join(f"{x:.3f}" for x in r))
        print(f"    mean absolute error on the first seven: {mean_abs_err(ws, r):.3f}")
    ws = cases["outlier, one scale"][0]
    print(f"  mean size of the seven ordinary weights: {sum(abs(w) for w in ws[:7]) / 7:.3f}")
    # Two groups of four, each with its own scale.
    g1, g2 = ws[:4], ws[4:]
    s1, _, r1 = absmax_round(g1)
    s2, q2, r2 = absmax_round(g2)
    print(f"  two groups of four: scales {s1:.4f} and {s2:.4f}; second group's integers {q2}; "
          f"errors {mean_abs_err(g1, r1, 4):.4f} (no outlier) and {mean_abs_err(g2, r2, 3):.4f} (three beside the outlier)")
    print()


def weights_table():
    return {m: {t: weight_gb(PARAMS[m], BITS[t]) for t in BITS} for m in PARAMS}


def example_weights():
    print("Example 3: memory for the weights, parameters x bits per weight / 8 (GB)")
    tab = weights_table()
    print(f"  {'model':<14}{'parameters':>16}" + "".join(f"{t:>8}" for t in TABLE_TYPES) + f"{'Q4_0':>8}")
    for m in TABLE_MODELS:
        print(f"  {m:<14}{PARAMS[m]:>16,}" + "".join(f"{tab[m][t]:>8.2f}" for t in TABLE_TYPES)
              + f"{tab[m]['Q4_0']:>8.2f}")
    print(f"  (Mistral 7B: " + ", ".join(f"{t} {tab['Mistral 7B'][t]:.2f}" for t in TABLE_TYPES) + ")")
    print("  the chapter's table (one decimal, as printed; the figure uses the same rounding):")
    for m in TABLE_MODELS:
        cells = " | ".join(f"{tab[m][t]:.1f}" if tab[m][t] < 100 else f"{tab[m][t]:.0f}" for t in TABLE_TYPES)
        print(f"  | {m} | {PARAMS[m] / 1e9:.2f} billion | {cells} |")
    n = PARAMS["Llama 3.1 8B"]
    print("  cross-checks against llama.cpp's README (LC31, LC35):")
    print(f"    8B F16 {n * 16.0005 / 8 / GIB:.2f} GiB (README 14.96); 8B Q4_K_M {n * 4.8944 / 8 / GIB:.2f} GiB (README 4.58)")
    print(f"    8B at 32 bits {n * 4 / GB:.2f} GB (README 32.1); 70B Q4_K_M {tab['Llama 3.1 70B']['Q4_K_M']:.2f} GB (README 43.1)")
    print(f"    70B and 405B at 32 bits from Hub counts: {PARAMS['Llama 3.1 70B'] * 4 / GB:.1f} GB (README 280.9), "
          f"{405_853_388_800 * 4 / GB:.1f} GB (README 1,625.1)")
    print(f"    1 GiB = {GIB / GB:.4f} GB; 4.58 GiB = {4.58 * GIB / GB:.2f} GB")
    phi = PARAMS["Phi-3-mini"]
    print(f"  Phi-3-mini at Q4_0: {weight_gb(phi, 4.5):.2f} GB; at exactly 4 bits {weight_gb(phi, 4):.2f} GB (report: about 1.8 GB)")
    print(f"  Apple's 'nearly 200 billion parameters' at 4 bits: {200e9 * 4 / 8 / GB:.0f} GB of weights")
    print(f"  destination's nominal 8B in 16-bit: {8e9 * 2 / GB:.0f} GB; exact count: {weight_gb(n, 16):.2f} GB")
    print(f"  8B: F16 / Q4_K_M = {BITS['F16'] / BITS['Q4_K_M']:.2f} times smaller")
    print()


def kv_table():
    out = {}
    for m, (layers, heads, hd) in ARCH.items():
        per = kv_bytes_per_token(layers, heads, hd)
        out[m] = {"per_token": per, **{c: per * c / GB for c in CONTEXTS}}
    return out


def example_kv():
    print("Example 4: KV cache, 2 x layers x KV heads x head dimension x bytes per number x tokens")
    l3 = kv_bytes_per_token(32, 8, 128)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        G.example_kv()
    assert f"{l3:,.0f} bytes" in buf.getvalue()
    print(f"  Llama 3 8B per token: {l3:,.0f} bytes, the same as code/checks/generation.py, Example 5")
    kv = kv_table()
    for m, (layers, heads, hd) in ARCH.items():
        row = kv[m]
        print(f"  {m}: 2 x {layers} x {heads} x {hd} x 2 = {row['per_token']:,.0f} bytes per token; "
              + "; ".join(f"{c:,} tokens {row[c]:.2f} GB" for c in CONTEXTS)
              + f"; 131,072 tokens {row['per_token'] * 131072 / GB:.2f} GB")
    phi = kv["Phi-3-mini"]["per_token"]
    print(f"  Phi-3-mini, its whole 4,096-token window: {phi * PHI3_WINDOW / GB:.2f} GB "
          f"(weights at Q4_K_M {weight_gb(PARAMS['Phi-3-mini'], BITS['Q4_K_M']):.2f} GB)")
    for bits, name in ((8.5, "8-bit (q8_0)"), (4.5, "4-bit (q4_0)")):
        per = kv_bytes_per_token(32, 8, 128, bits)
        print(f"  Llama 3.1 8B with a {name} cache: {per:,.0f} bytes per token ({per / l3:.2f} of 16-bit); "
              f"32,768 tokens {per * 32768 / GB:.2f} GB")
    print()


def totals():
    """Weights at Q4_K_M plus the 16-bit cache at each fixed context."""
    w = weights_table()
    kv = kv_table()
    return {m: (w[m]["Q4_K_M"], kv[m][CONTEXTS[0]], kv[m][CONTEXTS[1]])
            for m in ("Llama 3.1 8B", "Qwen3-8B", "Llama 3.1 70B")}


def example_totals():
    print("Example 5: weights at Q4_K_M plus a 16-bit KV cache (no allowance for working memory)")
    for m, (w, k8, k32) in totals().items():
        print(f"  {m}: weights {w:.2f} + 8K cache {k8:.2f} = {w + k8:.2f} GB; + 32K cache {k32:.2f} = {w + k32:.2f} GB"
              f" (one decimal: {w:.1f} + {k8:.1f} = {w + k8:.1f}; {w:.1f} + {k32:.1f} = {w + k32:.1f})")
    print()


def example_moe():
    print("Example 6: mixture of experts (Mixtral 8x7B)")
    mix, mis = PARAMS["Mixtral 8x7B"], PARAMS["Mistral 7B"]
    print(f"  8 x Mistral 7B = {8 * mis / 1e9:.1f} billion; Mixtral actually {mix / 1e9:.1f} billion "
          f"(blog: 46.7 total, 12.9 active per token)")
    active = 12.9e9
    w = weight_gb(mix, BITS["Q4_K_M"])
    read = weight_gb(active, BITS["Q4_K_M"])
    print(f"  Q4_K_M: memory for all weights {w:.2f} GB; read per token about {read:.2f} GB (active only, approximate)")
    print(f"  active share {active / mix:.0%}")
    print()


def example_bandwidth():
    print("Example 7: upper bound on decoding speed = bandwidth / bytes read per token")
    w = weights_table()
    m8, m70 = w["Llama 3.1 8B"], w["Llama 3.1 70B"]
    for name, bw, mem in DEVICES:
        q4 = bw / m8["Q4_K_M"]
        f16 = bw / m8["F16"]
        # Weights alone, against the stated memory; no hard verdict this close to the limit (the chapter says "nearly fill").
        if mem is None:
            fits16 = f"weights {m8['F16']:.2f} GB, memory not given"
        else:
            share = m8["F16"] / mem
            fits16 = f"weights {m8['F16']:.2f} GB against {mem} GB, {share:.0%}"
            if share >= 0.9:
                fits16 += ": nearly fills it, leaving almost no room for the cache"
        b70 = bw / m70["Q4_K_M"]
        fits70 = "unknown memory" if mem is None else ("fits" if m70["Q4_K_M"] <= mem else "does not fit")
        print(f"  {name}: {bw} GB/s, memory {mem} GB; 8B Q4_K_M <= {q4:.0f} t/s; 8B F16 <= {f16:.1f} t/s ({fits16}); "
              f"70B Q4_K_M <= {b70:.1f} t/s ({fits70})")
    mix_read = weight_gb(12.9e9, BITS["Q4_K_M"])
    mix_all = weight_gb(PARAMS["Mixtral 8x7B"], BITS["Q4_K_M"])
    bw = 546
    print(f"  Mixtral Q4_K_M on M4 Max: <= {bw / mix_read:.0f} t/s reading active weights, "
          f"<= {bw / mix_all:.0f} t/s if every weight were read")
    kv8 = kv_table()["Llama 3.1 8B"][32768]
    print(f"  8B Q4_K_M at a full 32K cache on RTX 4090: <= {1008 / (m8['Q4_K_M'] + kv8):.0f} t/s "
          f"(reads {m8['Q4_K_M'] + kv8:.2f} GB per token)")
    print()


def example_measured():
    print("Example 8: bounds against measurements")
    size = 4_677_120_000 / GB      # llama-bench example file, bytes (LC52)
    bound = 716.8 / size
    print(f"  RTX 4080, Qwen2.5-7B Q4_K_M ({size:.2f} GB): bound {bound:.1f} t/s; measured 119.92 = {119.92 / bound:.0%}")
    print(f"  same run: prompt 7285.68 t/s vs generation 119.92 t/s = {7285.68 / 119.92:.0f} times")
    print("  implied bandwidth = size x tokens/s (README table, hardware unstated, LC31):")
    for name, gib, tps in (("F16", 14.96, 29.17), ("Q8_0", 7.95, 50.93), ("Q6_K", 6.14, 58.67),
                           ("Q4_K_M", 4.58, 71.93), ("Q2_K", 2.95, 79.85), ("IQ1_S", 1.87, 79.73)):
        print(f"    {name}: {gib} GiB x {tps} = {gib * GIB / GB * tps:.0f} GB/s")
    print(f"    F16 vs Q4_K_M: size ratio {14.96 / 4.58:.2f}, speed ratio {71.93 / 29.17:.2f}")
    print("  phone (Llama 3.2 card, OnePlus 12): file MB x decode t/s")
    for name, mb, tps in (("1B BF16", 2358, 19.2), ("1B SpinQuant", 1083, 50.2),
                          ("3B BF16", 6129, 7.6), ("3B SpinQuant", 2435, 19.7)):
        print(f"    {name}: {mb * 1e6 * tps / GB:.1f} GB/s")
    print(f"    1B file 1083/2358 = {1083 / 2358:.0%}; decode 50.2/19.2 = {50.2 / 19.2:.1f}x")
    ms = 61.41
    print(f"  llama.cpp's first run: {ms} ms per token = {1000 / ms:.1f} t/s")
    print("  llama-bench offload (7B Q4_0, hardware unstated): GPU layers set to 10: 13.45, 32: 54.78, 35: 131.66 t/s;"
          f" 35 vs 32: {131.66 / 54.78:.1f}x")
    print(f"  llama-bench CPU threads: 1 -> 4.05, 8 -> 16.71, 32 -> 16.41 t/s; 8 vs 1: {16.71 / 4.05:.1f}x")
    print()


def example_costs():
    print("Example 9: what rounding costs, from the sources' own numbers")
    for name, full, q in (("OPT-125M", 27.65, 31.12), ("OPT-175B", 8.34, 8.37),
                          ("BLOOM-560M", 22.42, 24.03), ("BLOOM-176B", 8.11, 8.21)):
        print(f"  GPTQ 4-bit {name}: perplexity {full} -> {q}, +{(q - full) / full:.1%}")
    print(f"  OPT-175B 4-bit round-to-nearest: 8.34 -> 10.54, +{(10.54 - 8.34) / 8.34:.0%}")
    print(f"  Llama 3.2 1B MMLU: 49.3 - 43.3 = {49.3 - 43.3:.1f} (plain rounding); 49.3 - 49.0 = {49.3 - 49.0:.1f} (QLoRA-style)")
    print(f"  Llama 3.2 3B MMLU: 63.4 - 60.5 = {63.4 - 60.5:.1f}; 63.4 - 62.4 = {63.4 - 62.4:.1f}")
    print(f"  GPTQ Table 6: A100 230/71 = {230 / 71:.2f}x; A6000 589/130 = {589 / 130:.2f}x")
    print(f"  AWQ OPT-6.7B INT3: round-to-nearest 43.2 vs 1% kept in FP16 13.0")
    print()


def example_small():
    print("Example 10: small against large, developers' own tables")
    for test, a, b, c in (("MMLU", 69.4, 83.6, 87.3), ("MATH", 51.9, 68.0, 73.8), ("GPQA", 32.8, 46.7, 51.1),
                          ("GSM8K", 84.5, 95.1, 96.8)):
        print(f"  Llama 3 {test}: 8B {a}, 70B {b}, 405B {c}; 70B - 8B = {b - a:.1f}")
    print(f"  Phi-3-mini vs Mistral 7B: MMLU 68.8 vs 61.7 ({68.8 - 61.7:+.1f}); TriviaQA 64.0 vs 75.2 ({64.0 - 75.2:+.1f})")
    print()


if __name__ == "__main__":
    example_blocks()
    example_rounding()
    example_weights()
    example_kv()
    example_totals()
    example_moe()
    example_bandwidth()
    example_measured()
    example_costs()
    example_small()
