#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `frontier` [D-009].

Run: python3 code/checks/frontier.py
Standard library only. Every number printed in the chapter comes from this
output. The inputs are numbers printed in the sources (see
book1/sources/frontier.md, "Mechanism claims to check numerically", M1 to M13);
nothing is read off a plot.

METR's time horizons (Example 6) are hard-coded from METR's raw-data file,
not downloaded:
  source: https://metr.org/assets/benchmark_results_1_1.yaml, linked from
          https://metr.org/time-horizons/ ("LAST UPDATED September 8, 2026",
          "This page is no longer actively updated.")
  accessed: 2026-11-11 by the research agent for this chapter
  SHA-256 of the file as downloaded (decompressed):
          aae31902b0519a4da73e16643915e5e8aca13cd3315c3aac893ce3d6dfe92ad9
The figure script figures/frontier.py imports these values from here.
"""
import math
import statistics
from datetime import date

# ----------------------------------------------------------------------------
# METR, 50% time horizons in minutes, 95% confidence intervals, and release
# dates as given in the YAML file (frontier models only; GPT-2 has no interval
# in the ledger). Name, release date, p50, (low, high).
METR = [
    ("GPT-2", date(2019, 2, 14), 0.1, None),
    ("GPT-4", date(2023, 3, 14), 4.0, (1.9, 8.0)),
    ("o1", date(2024, 12, 5), 38.8, (21.2, 65.0)),
    ("o3", date(2025, 4, 16), 119.7, (74.6, 190.9)),
    ("GPT-5", date(2025, 8, 7), 203.0, (112.6, 405.6)),
    ("Claude Opus 4.5", date(2025, 11, 24), 293.0, (161.7, 623.7)),
    ("GPT-5.2", date(2025, 12, 11), 352.2, (198.1, 815.2)),
    ("Claude Opus 4.6", date(2026, 2, 5), 718.8, (316.7, 3633.8)),
    ("Claude Mythos Preview (early)", date(2026, 4, 7), 1044.8, (508.9, 3304.3)),
]
# 80% horizons printed in the same file (minutes).
METR_P80 = {"o3": 30.0, "GPT-5": 38.3, "Claude Opus 4.6": 69.9,
            "Claude Mythos Preview (early)": 185.9}
# METR states that measurements above 16 hours are unreliable.
METR_LIMIT_MIN = 16 * 60
# Doubling times in days.
DOUBLING_PAPER = 207          # Kwa et al. v4, p. 6: 2019-2025, 50% horizon
DOUBLING_PAPER_CI = (166, 240)
DOUBLING_TH11_POST2023 = 131  # METR, Time Horizon 1.1 (January 2026)
DOUBLING_YAML_FROM2023 = 128.744
DOUBLING_YAML_FROM2023_CI = (104.428, 158.012)
DOUBLING_YAML_STITCHED = 187.778

DAYS_PER_YEAR = 365.25


def example_aime():
    print("Example 1: o1 on the 2024 AIME (15 problems), OpenAI, September 2024")
    for label, solved in (("GPT-4o", 1.8), ("o1, one sample", 11.1),
                          ("o1, majority of 64", 12.5), ("o1, best of 1,000 by a scorer", 13.9)):
        print(f"  {label}: {solved}/15 = {solved / 15:.1%}")
    print()


def example_grpo():
    print("Example 2: a group-relative advantage (GRPO), constructed group of 16 answers")
    rewards = [1] * 4 + [0] * 12
    mean = statistics.fmean(rewards)
    sd = statistics.pstdev(rewards)          # population standard deviation (assumption)
    print(f"  rewards: 4 correct (1), 12 wrong (0); G = {len(rewards)}")
    print(f"  mean {mean:.2f}; population standard deviation {sd:.3f}")
    print(f"  advantage of a correct answer: (1 - {mean:.2f}) / {sd:.3f} = {(1 - mean) / sd:+.2f}")
    print(f"  advantage of a wrong answer:   (0 - {mean:.2f}) / {sd:.3f} = {(0 - mean) / sd:+.2f}")
    adv = [(r - mean) / sd for r in rewards]
    print(f"  the advantages sum to {abs(sum(adv)):.6f} and have standard deviation {statistics.pstdev(adv):.3f}")
    for k in (1, 8, 15):
        rs = [1] * k + [0] * (16 - k)
        m, s = statistics.fmean(rs), statistics.pstdev(rs)
        print(f"  {k:2d} of 16 correct: correct {(1 - m) / s:+.2f}, wrong {(0 - m) / s:+.2f}")
    print(f"  16 of 16 correct: standard deviation {statistics.pstdev([1] * 16):.1f}, no signal")
    print(f"  R1-Zero batch: 32 questions x 16 samples = {32 * 16}")
    print()


def example_costs():
    print("Example 3: DeepSeek-R1 training costs (R1 paper v2, Table 7; V3 report, Table 1)")
    gpus = 64 * 8
    print(f"  64 x 8 = {gpus} H800 GPUs")
    print(f"  R1-Zero: {gpus} x 198 h = {gpus * 198:,} GPU hours (printed 101K)")
    print(f"  R1:      {gpus} x 80 h = {gpus * 80:,} GPU hours (printed 41K)")
    total_k = 101 + 5 + 41
    print(f"  total: 101K + 5K + 41K = {total_k}K GPU hours; x $2 = ${total_k * 2}K")
    v3 = 2664 + 119 + 5
    print(f"  V3 final run: 2,664K + 119K + 5K = {v3:,}K GPU hours; x $2 = ${v3 * 2 / 1000:.3f}M")
    print(f"  R1's stages as a share of V3's final run: {total_k}/{v3:,} = {total_k / v3:.1%}")
    print()


def example_hanoi():
    print("Example 4: Tower of Hanoi moves and per-token reliability")
    for n in (3, 7, 8, 10, 12, 15):
        print(f"  N = {n}: 2^N - 1 = {2 ** n - 1:,} moves")
    print(f"  N = 15 at 10 tokens per move: {(2 ** 15 - 1) * 10:,} tokens")
    print(f"  failure near move 40 of 255: {40 / 255:.1%}")
    for p in (0.9999, 0.999):
        print(f"  {p}^10,000 = {p ** 10000:.6f} ({p ** 10000:.4%})")
    print()


def example_swebench():
    print("Example 5: SWE-bench and SWE-bench Verified")
    print(f"  original: 2,294 of about 90,000 pull requests kept = {2294 / 90000:.1%}")
    print(f"  Verified: 500 of 1,699 annotated = {500 / 1699:.1%}; 68.3% filtered -> {100 - 68.3:.1f}% kept")
    print(f"  audit: 138/500 = {138 / 500:.1%}; 59.4% of 138 = {0.594 * 138:.1f} problems")
    print(f"  74.9% -> 80.9%: {80.9 - 74.9:.1f} points in six months")
    print("  score history (different sets): 1.96% (Oct 2023, full set), 33.2% (Aug 2024, Verified)")
    print()


def example_metr():
    print("Example 6: METR time horizons (hard-coded from the frozen page; see docstring)")
    for days in (DOUBLING_PAPER, *DOUBLING_PAPER_CI, DOUBLING_YAML_STITCHED,
                 DOUBLING_TH11_POST2023, DOUBLING_YAML_FROM2023, *DOUBLING_YAML_FROM2023_CI):
        print(f"  doubling every {days} days: x{2 ** (DAYS_PER_YEAR / days):.2f} per year; "
              f"{days / (DAYS_PER_YEAR / 12):.1f} months")
    for name, d, p50, ci in METR:
        hrs = p50 / 60
        flag = " (above METR's 16-hour limit)" if p50 > METR_LIMIT_MIN else ""
        span = f"; CI {ci[0]} to {ci[1]} min, ratio {ci[1] / ci[0]:.1f}" if ci else ""
        print(f"  {name} ({d}): {p50} min = {hrs:.2f} h{flag}{span}")
    for name, p80 in METR_P80.items():
        p50 = next(m[2] for m in METR if m[0] == name)
        print(f"  {name}: 50% {p50} min / 80% {p80} min = {p50 / p80:.2f}; 80% = {p80 / 60:.2f} h")
    gpt2_s = 0.1 * 60
    print(f"  GPT-2: 0.1 min = {gpt2_s:.0f} s (paper: 'only 2 seconds' under the earlier task suite)")
    # Logistic fit read at the horizon: sigma(0).
    print(f"  logistic at t = h: sigma(0) = {1 / (1 + math.exp(0)):.2f}")
    # METR's own extrapolation threshold: one work month.
    print(f"  167 work hours = {167 * 60:,} minutes; from 110 min: log2(10020/110) = "
          f"{math.log2(10020 / 110):.2f} doublings")
    print()


def example_images_audio():
    print("Example 7: images and audio as sequences")
    side, patch = 224, 16
    n = side // patch
    print(f"  224 / 16 = {n}; {n} x {n} = {n * n} patches; each 16 x 16 x 3 = {patch * patch * 3} numbers")
    n14 = side // 14
    print(f"  with 14 x 14 patches: 224 / 14 = {n14}; {n14} x {n14} = {n14 * n14} patches")
    b = 32768
    print(f"  CLIP batch {b:,}: {b * b:,} pairings, {b:,} true, {b * b - b:,} wrong "
          f"(1 in {b:,} true)")
    print(f"  Whisper: 30 s / 10 ms = {round(30 / 0.010):,} frames of 80 numbers")
    print()


def example_energy():
    print("Example 8: energy (IEA executive summaries; Google, May 2025 data)")
    print(f"  415 TWh at 1.5% implies world use of about {415 / 0.015:,.0f} TWh (2024)")
    print(f"  415 x 1.17 = {415 * 1.17:.1f} TWh (IEA 2026 gives 485 TWh for 2025)")
    print(f"  945 / 415 = {945 / 415:.2f}; 950 / 485 = {950 / 485:.2f}")
    print(f"  0.24 Wh in 9 s of television implies {0.24 / (9 / 3600):.0f} W")
    print(f"  comprehensive / narrow boundary: 0.24 / 0.10 = {0.24 / 0.10:.1f}")
    print()


def example_compute():
    print("Example 9: training compute growth (International AI Safety Report 2026)")
    print(f"  5x per year for 5 years: 5^5 = {5 ** 5:,} (report: roughly 3,000 times)")
    print()


def example_moe():
    print("Example 10: active parameters per token in open-weight mixture-of-experts models")
    rows = [("DeepSeek-V3 (Dec 2024)", 37, 671), ("DeepSeek-V4-Pro", 49, 1600),
            ("DeepSeek-V4-Flash", 13, 284), ("Qwen3.8-2.4T-A95B", 95, 2400),
            ("Mistral Large 4 (incl. embeddings)", 52, 1000), ("Mistral Large 4 (excl.)", 49, 1000),
            ("Kimi K3.1 Pro", 104, 2800), ("gpt-oss-120b", 5.1, 116.8)]
    for name, act, tot in rows:
        print(f"  {name}: {act}/{tot:,} = {act / tot:.1%}")
    print(f"  Kimi K3.1 Pro weights at 4 bits: 2.8e12 x 0.5 bytes = {2.8e12 * 0.5 / 1e12:.1f} TB")
    print()


if __name__ == "__main__":
    example_aime()
    example_grpo()
    example_costs()
    example_hanoi()
    example_swebench()
    example_metr()
    example_images_audio()
    example_energy()
    example_compute()
    example_moe()
