#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `scale` [D-009].

Run: python3 code/checks/scale.py
Standard library only. Every number printed in the chapter comes from this
output. The model table holds numbers as stated by each model's developers
(sources in book1/sources/scale.md); None means the source does not state it.
"""
import math

# name, year (first public appearance), parameters, training tokens, family
MODELS = [
    ("GPT", 2018.45, 117e6, None, "decoder"),
    ("BERT-large", 2018.78, 340e6, 128e9, "encoder"),
    ("GPT-2", 2019.12, 1542e6, None, "decoder"),
    ("T5-11B", 2019.81, 11e9, 1e12, "encoder-decoder"),
    ("GPT-3", 2020.41, 175e9, 300e9, "decoder"),
    ("Gopher", 2021.94, 280e9, 300e9, "decoder"),
    ("Chinchilla", 2022.24, 70e9, 1.4e12, "decoder"),
    ("PaLM", 2022.26, 540e9, 780e9, "decoder"),
    ("LLaMA-65B", 2023.16, 65.2e9, 1.4e12, "decoder"),
    ("Llama 2 70B", 2023.54, 70e9, 2.0e12, "decoder"),
    ("Llama 3.1 405B", 2024.58, 405e9, 15.6e12, "decoder"),
]

PF_DAY = 1e15 * 86400


def example_models():
    print("Example 1: the model table, and tokens per parameter")
    for name, year, n, d, fam in MODELS:
        ratio = f"{d / n:.1f}" if d else "not stated"
        print(f"  {name:>15} ({int(year)}): {n:.3g} parameters, tokens {d if d is None else f'{d:.3g}'}, "
              f"tokens per parameter {ratio} [{fam}]")
    first, last = MODELS[0][2], MODELS[-1][2]
    print(f"  GPT (2018) to Llama 3.1 405B (2024): {last / first:,.0f} times as many parameters")
    print()


def example_6nd():
    print("Example 2: training compute is about 6 x parameters x tokens")
    c = 6 * 174.6e9 * 300e9
    print(f"  GPT-3: 6 x 174.6e9 x 300e9 = {c:.3e} FLOPs (printed 3.14E+23); {c / PF_DAY:,.0f} petaflop/s-days (printed 3.64E+03)")
    print(f"  one petaflop/s-day = 10^15 x 86,400 = {PF_DAY:.2e} FLOPs")
    chin, goph = 6 * 70e9 * 1.4e12, 6 * 280e9 * 300e9
    print(f"  Chinchilla 6ND {chin:.2e}; Gopher 6ND {goph:.2e}; ratio {chin / goph:.2f} (papers: same budget, 5.76e23)")
    print(f"  PaLM 6ND {6 * 540e9 * 780e9:.3e} (printed 2.56e24); Llama 3 6ND {6 * 405e9 * 15.6e12:.3e} (printed 3.8e25)")
    print(f"  Llama 3 405B against Llama 2 70B: 3.8e25 / {6 * 70e9 * 2e12:.2e} = {3.8e25 / (6 * 70e9 * 2e12):.0f} (paper: almost 50x)")
    print()


def kaplan_loss(n):
    return (8.8e13 / n) ** 0.076


def example_powerlaw():
    print("Example 3: Kaplan et al.'s power law for model size, L(N) = (8.8e13 / N)^0.076 nats")
    for n in (1e6, 1e8, 1e9, 1e10, 1e11):
        print(f"  N = {n:.0e}: loss {kaplan_loss(n):.2f} nats ({kaplan_loss(n) / math.log(2):.2f} bits)")
    print(f"  doubling N multiplies the loss by 2^-0.076 = {2 ** -0.076:.3f}; ten times N by {10 ** -0.076:.3f}")
    slope = (math.log(kaplan_loss(1e10)) - math.log(kaplan_loss(1e6))) / (math.log(1e10) - math.log(1e6))
    print(f"  slope on log-log axes: {slope:.3f}")
    print(f"  one nat = {1 / math.log(2):.4f} bits")
    print()


def example_allocation():
    print("Example 4: how to spend k times more compute")
    for k in (10, 100, 1000):
        print(f"  k = {k:>4}: Kaplan parameters x {k ** 0.73:.1f}, tokens x {k ** 0.27:.1f}; "
              f"Chinchilla both x {k ** 0.5:.1f}")
    rows = [(400e6, 8.0e9), (1e9, 20.2e9), (10e9, 205.1e9), (67e9, 1.5e12), (175e9, 3.7e12), (280e9, 5.9e12),
            (520e9, 11.0e12), (1e12, 21.2e12), (10e12, 216.2e12)]
    print("  Hoffmann et al. Table 3, tokens per parameter: " + ", ".join(f"{d / n:.1f}" for n, d in rows))
    print(f"  Llama 3's own fit at 3.8e25 FLOPs: 16.55T / 402B = {16.55e12 / 402e9:.0f} tokens per parameter")
    print(f"  LLaMA-7B: 1.0T / 6.7B = {1.0e12 / 6.7e9:.0f} tokens per parameter")
    print()


def example_metric():
    print("Example 5: an all-or-nothing score on a 5-token answer (constructed)")
    for p in (0.5, 0.7, 0.8, 0.9, 0.95, 0.99):
        print(f"  each token right with p = {p}: whole answer right {p ** 5:.3f}; expected wrong tokens {5 * (1 - p):.2f}")
    print()


GPT3_SIZES = [("Small", 125e6), ("Medium", 350e6), ("Large", 760e6), ("XL", 1.3e9), ("2.7B", 2.7e9),
              ("6.7B", 6.7e9), ("13B", 13e9), ("175B", 175e9)]
ADD2_FEW = [2.00, 4.10, 3.50, 4.50, 8.90, 11.9, 55.5, 100.0]
ADD3_FEW = [0.15, 0.45, 0.30, 0.55, 0.75, 0.90, 8.40, 80.4]


def example_arithmetic():
    print("Example 6: GPT-3 few-shot addition accuracy by size (Table H.1)")
    for (name, n), a2, a3 in zip(GPT3_SIZES, ADD2_FEW, ADD3_FEW):
        print(f"  {name:>6}: 2-digit {a2:5.1f}%, 3-digit {a3:5.2f}%")
    ratios = [b[1] / a[1] for a, b in zip(GPT3_SIZES, GPT3_SIZES[1:])]
    print("  size ratio between neighbours: " + ", ".join(f"{r:.1f}" for r in ratios))
    print()


def example_compute_trend():
    print("Example 7: OpenAI's 2018 compute trend")
    doublings = math.log2(300000)
    print(f"  300,000x is {doublings:.1f} doublings; at 3.43 months each, {doublings * 3.43:.0f} months")
    print(f"  per year: 2^(12 / 3.43) = {2 ** (12 / 3.43):.1f}")
    print()


def example_energy():
    print("Example 8: energy and emissions, reproduced from stated inputs")
    mwh = 1_022_362 * 400 * 1.1 / 1e6
    print(f"  LLaMA-65B: 1,022,362 GPU-hours x 400 W x 1.1 = {mwh:.1f} MWh; x 0.385 t/MWh = {mwh * 0.385:.1f} t CO2e")
    secs = 3.14e23 / (10000 * 24.6e12)
    days = secs / 86400
    gmwh = 10000 * 330 * days * 24 * 1.10 / 1e6
    print(f"  GPT-3 (Patterson et al.): {days:.2f} days on 10,000 GPUs; {gmwh:,.0f} MWh; x 0.429 = {gmwh * 0.429:.0f} t CO2e")
    print()


if __name__ == "__main__":
    example_models()
    example_6nd()
    example_powerlaw()
    example_allocation()
    example_metric()
    example_arithmetic()
    example_compute_trend()
    example_energy()
