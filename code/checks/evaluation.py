#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `evaluation` [D-009].

Run: python3 code/checks/evaluation.py
Standard library only. Every number printed in the chapter comes from this
output or is printed in a source (see book1/sources/evaluation.md,
"Mechanism claims to check numerically at drafting"). figures/evaluation.py
imports the functions and constants below [D-014].
"""
import math
import random

Z95 = 1.96

# Benchmark sizes from the ledger: HumanEval (EV11), GPQA Diamond (EV24),
# GSM8K test (EV10, Hugging Face record), HLE public set as of the October
# 2026 version (EV25, EVD3), MMLU test (EV7).
BENCHMARKS = [("HumanEval", 164), ("GPQA Diamond", 198), ("GSM8K test", 1319),
              ("HLE public set", 2500), ("MMLU test", 14079)]

# Arena snapshot, 8 October 2026 (EV33): ratings and votes, no model names.
ARENA_TOP, ARENA_TOP_LO, ARENA_TOP_HI, ARENA_TOP_VOTES = 1525.2, 1516.4, 1534.0, 4932
ARENA_2, ARENA_2_VOTES = 1504.7, 77636
ARENA_13 = 1489.7
ARENA_TOTAL_VOTES = 8_626_731
ARENA_JAN_2024_VOTES = 240_000        # "over 240K votes" (chiang2024chatbot, p. 1)


def half_width(p, n):
    """95% interval half-width, in percentage points, for accuracy p on n questions."""
    return 100 * Z95 * math.sqrt(p * (1 - p) / n)


def win_prob(d):
    """Probability that a model rated d points higher wins a vote (Arena scale)."""
    return 1 / (1 + 10 ** (-d / 400))


def example_standard_error():
    print("Example 1: sampling noise in a benchmark score (95% interval, +- percentage points)")
    for p in (0.8, 0.5):
        row = "; ".join(f"{name} n = {n:,}: +-{half_width(p, n):.2f}" for name, n in BENCHMARKS)
        print(f"  p = {p}: {row}")
    print(f"  n = 1,000, p = 0.8: +-{half_width(0.8, 1000):.2f}")
    print("  difference between two models at 80% (independent samples, so slightly too wide):")
    for n in (164, 1000, 14079):
        print(f"    n = {n:,}: +-{math.sqrt(2) * half_width(0.8, n):.2f}")
    print()


def comb(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def pass_at_k(n, c, k):
    """Chen et al.'s unbiased estimator: 1 - C(n - c, k) / C(n, k)."""
    return 1 - comb(n - c, k) / comb(n, k)


def example_pass_at_k():
    print("Example 2: pass@k for one problem, 10 attempts, 3 of them pass")
    n, c = 10, 3
    for k in (1, 5, 10):
        naive = 1 - (1 - c / n) ** k
        print(f"  pass@{k} = {pass_at_k(n, c, k):.4f}; naive 1 - (1 - 0.3)^{k} = {naive:.4f}")
    print(f"  ways to pick 5 of 10: {comb(10, 5)}; ways with no passing attempt: {comb(7, 5)}")
    print(f"  n = 200, c = 1: pass@100 = {pass_at_k(200, 1, 100):.4f}; naive {1 - (1 - 1 / 200) ** 100:.4f}")
    print()


def fit_bradley_terry(votes, m):
    """Logistic regression with a +1 / -1 feature per model, model 0 fixed at 0.

    votes: list of (a, b, a_won). Newton's method on the log-likelihood.
    Returns strengths on the log-odds scale.
    """
    beta = [0.0] * m
    for _ in range(50):
        g = [0.0] * m
        h = [[0.0] * m for _ in range(m)]
        for a, b, a_won in votes:
            x = [0.0] * m
            x[a], x[b] = 1.0, -1.0
            p = 1 / (1 + math.exp(-(beta[a] - beta[b])))
            for i in range(1, m):
                g[i] += (a_won - p) * x[i]
                for j in range(1, m):
                    h[i][j] += p * (1 - p) * x[i] * x[j]
        # Solve the (m - 1) x (m - 1) system h * step = g (here 2 x 2).
        (h11, h12), (h21, h22) = (h[1][1], h[1][2]), (h[2][1], h[2][2])
        det = h11 * h22 - h12 * h21
        s1 = (h22 * g[1] - h12 * g[2]) / det
        s2 = (h11 * g[2] - h21 * g[1]) / det
        beta[1] += s1
        beta[2] += s2
        if abs(s1) + abs(s2) < 1e-12:
            break
    return beta


def example_bradley_terry():
    print("Example 3: Bradley-Terry ratings and the Arena scale")
    for d in (0, 10, 15, 25, 35, 50, 100, 200, 400):
        print(f"  gap {d:>3} points: higher-rated model wins {win_prob(d):.3f}")
    print(f"  one Arena point = ln 10 / 400 = {math.log(10) / 400:.5f} on the log-odds scale")
    for n in (100, 1000, ARENA_TOP_VOTES, 10000):
        print(f"  sigma for {n:,} votes between equal models: 347.4 / sqrt(n) = {347.4 / math.sqrt(n):.2f}; "
              f"check (400 / ln 10) x 2 / sqrt(n) = {400 / math.log(10) * 2 / math.sqrt(n):.2f}")
    print(f"  snapshot: top model interval {ARENA_TOP_LO} to {ARENA_TOP_HI}, half-width "
          f"{(ARENA_TOP_HI - ARENA_TOP_LO) / 2:.2f}, on {ARENA_TOP_VOTES:,} votes")
    for label, gap in (("rank 1 vs 2", ARENA_TOP - ARENA_2), ("rank 2 vs 13", ARENA_2 - ARENA_13),
                       ("rank 1 vs 13", ARENA_TOP - ARENA_13), ("AI Index, 1,503 vs 1,481", 1503 - 1481)):
        print(f"  {label}: gap {gap:.1f}, win probability {win_prob(gap):.3f}")
    print(f"  votes: {ARENA_JAN_2024_VOTES:,} (Jan 2024) to {ARENA_TOTAL_VOTES:,} (Oct 2026): "
          f"factor {ARENA_TOTAL_VOTES / ARENA_JAN_2024_VOTES:.0f}")
    rng = random.Random(0)
    true = [0.0, 0.4, 1.0]
    votes = []
    for _ in range(3000):
        a, b = rng.sample(range(3), 2)
        p = 1 / (1 + math.exp(-(true[a] - true[b])))
        votes.append((a, b, 1 if rng.random() < p else 0))
    fit = fit_bradley_terry(votes, 3)
    scale = 400 / math.log(10)
    print(f"  simulated 3,000 votes among 3 models, true strengths {true}: fitted "
          + ", ".join(f"{b:.3f}" for b in fit))
    print("  on the Arena scale (1000 + 173.7 x strength): "
          + ", ".join(f"{1000 + scale * b:.1f}" for b in fit)
          + f"; true {', '.join(f'{1000 + scale * b:.1f}' for b in true)}")
    print()


def example_bits_per_byte():
    print("Example 4: bits per byte and perplexity")
    total_bits, n_bytes = 900, 1000
    for name, tokens in (("A", 250), ("B", 400)):
        per_tok = total_bits / tokens
        print(f"  tokenizer {name}: {tokens} tokens, {per_tok:.2f} bits/token, perplexity {2 ** per_tok:.2f}, "
              f"{total_bits / n_bytes:.3f} bits per byte")
    ratio = 0.29335
    print(f"  Pile: loss 2.5 nats/token x {ratio} tokens/byte / ln 2 = {ratio * 2.5 / math.log(2):.3f} BPB")
    for name, bpb in (("GPT-3 davinci", 0.7177), ("GPT-2 small", 1.2253)):
        nats = bpb * math.log(2) / ratio
        print(f"  {name}: {bpb} BPB = {nats:.3f} nats per GPT-2 token, perplexity {math.exp(nats):.2f}")
    print()


# Invented text for Example 5 (not a real benchmark item).
QUESTION = ("A farmer has three fields of wheat and sells half of the grain from each field "
            "at the market on Monday then keeps the rest for winter how much remains").split()


def ngrams(words, n=13):
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def example_ngram_overlap():
    print("Example 5: GPT-3-style 13-gram overlap on an invented question")
    page = "Homework help forum : ".split() + QUESTION[:22] + "? Thanks in advance".split()
    q = ngrams(QUESTION)
    shared = q & ngrams(page)
    print(f"  question: {len(QUESTION)} words, {len(q)} distinct 13-grams")
    print(f"  web page containing the first 22 words: {len(shared)} shared 13-grams -> flagged {bool(shared)}")
    # A light rewording: three words changed, so no 13 words in a row survive.
    para = list(QUESTION)
    para[4], para[15], para[18] = "plots", "plot", "fair"
    shared_p = q & ngrams(para)
    changed = sum(1 for a, b in zip(QUESTION, para) if a != b)
    print(f"  paraphrase with {changed} of {len(QUESTION)} words changed: {len(shared_p)} shared 13-grams "
          f"-> flagged {bool(shared_p)}")
    print()


def two_proportion_z(p1, n1, p2, n2):
    pooled = (p1 * n1 + p2 * n2) / (n1 + n2)
    se = math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se
    p_two = math.erfc(abs(z) / math.sqrt(2))
    return z, p_two


def example_gsm1k():
    print("Example 6: a fresh test from the same distribution (GSM8K test vs GSM1k), two-proportion z-test")
    n8, n1 = 1319, 1205
    for label, a, b in (("largest drop (Yi-6B-Chat)", 0.437, 0.357), ("frontier model (gpt-4)", 0.911, 0.923)):
        z, p = two_proportion_z(a, n8, b, n1)
        print(f"  {label}: {a:.1%} on {n8:,} vs {b:.1%} on {n1:,}: drop {100 * (a - b):.1f} points "
              f"({(a - b) / a:.1%} relative); z = {z:.2f}, two-sided p = {p:.2g}")
    print()


def example_printed_arithmetic():
    print("Example 7: arithmetic on printed numbers")
    print(f"  MMLU: 5 x 57 + 1,540 + 14,079 = {5 * 57 + 1540 + 14079:,} (paper says 15,908)")
    print(f"  GSM8K: 7,473 + 1,319 = {7473 + 1319:,}")
    print(f"  GLUE: 88.4 - 87.1 = {88.4 - 87.1:.1f}; SuperGLUE: 89.8 - 69.0 = {89.8 - 69.0:.1f}")
    print(f"  HELM OPT HellaSwag: 79.1 - 30.2 = {79.1 - 30.2:.1f} points")
    print(f"  GPQA Diamond: 93.0 - 81.2 = {93.0 - 81.2:.1f}")
    print(f"  GPT-4 HumanEval: 65.58 - 67.0 = {65.58 - 67.0:.2f} points; relative {(65.58 - 67.0) / 67.0:.2%}")
    print(f"  MMLU: 43.9 (2020) to 86.4 (2023): {86.4 - 43.9:.1f} points")
    print(f"  HLE: under 10% to 38.3% in 2025; Jan 2025 range 2.7 to 13.4")
    print(f"  Arena top 13 span: {ARENA_TOP:.1f} - {ARENA_13:.1f} = {ARENA_TOP - ARENA_13:.1f}")
    print()


def expected_score(q, t):
    """Expected score for answering with confidence q when a wrong answer costs t / (1 - t)."""
    penalty = t / (1 - t)
    return q - (1 - q) * penalty


def example_scoring_rule():
    print("Example 8: guessing under different scoring rules (I don't know scores 0)")
    for t, qs in ((0.0, (0.3,)), (0.5, (0.3, 0.6)), (0.9, (0.8, 0.95))):
        pen = t / (1 - t)
        print(f"  t = {t} (wrong answer costs {pen:g}): "
              + "; ".join(f"confidence {q}: {expected_score(q, t):+.2f}" for q in qs))
    print(f"  Kalai et al.'s t = 0.75: 0.75 / 0.25 = {0.75 / 0.25:g} (they print 2)")
    print()


if __name__ == "__main__":
    example_standard_error()
    example_pass_at_k()
    example_bradley_terry()
    example_bits_per_byte()
    example_ngram_overlap()
    example_gsm1k()
    example_printed_arithmetic()
    example_scoring_rule()
