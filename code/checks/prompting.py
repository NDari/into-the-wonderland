#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `prompting` [D-009].

Run: python3 code/checks/prompting.py
Standard library only. Every number printed in the chapter comes from this
output. Printed values from papers are copied here with their source and page;
the script does the arithmetic on them.

Example 2 counts tokens with GPT-2's tokenizer, reused from
code/checks/tokens.py, which reads GPT-2's vocabulary from out/cache/ and
checks it against pinned hashes [D-018]. GPT-2's tokenizer stands in for the
tokenizers of the models discussed; other tokenizers give other counts.
"""
import importlib.util
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(f"{name}_checks", HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Printed values, used by this script and by figures/prompting.py [D-014].

# Wei et al. 2022 (chain of thought), Table 2, p. 21: GSM8K accuracy (%),
# standard prompting / chain-of-thought prompting, by model and size.
WEI_TABLE2 = {
    "LaMDA": [("420M", 0.42e9, 2.6, 0.4), ("2B", 2e9, 3.6, 1.9), ("8B", 8e9, 3.2, 1.6),
              ("68B", 68e9, 5.7, 8.2), ("137B", 137e9, 6.5, 14.3)],
    "GPT-3": [("350M", 0.35e9, 2.2, 0.5), ("1.3B", 1.3e9, 2.4, 0.5), ("6.7B", 6.7e9, 4.0, 2.4),
              ("175B", 175e9, 15.6, 46.9)],
    "PaLM": [("8B", 8e9, 4.9, 4.1), ("62B", 62e9, 9.6, 29.9), ("540B", 540e9, 17.9, 56.9)],
}
WEI_PRIOR_BEST = 55.0      # Table 1, p. 20: finetuned GPT-3 with a verifier (Cobbe et al. 2021)

# Liu et al., Lost in the Middle, arXiv v3 Table 6 (PDF p. 18): 20 documents,
# accuracy (%) with the answer document at position 1, 5, 10, 15, 20.
LIU_POSITIONS = [1, 5, 10, 15, 20]
LIU_TABLE6 = {
    "GPT-3.5-Turbo": [75.8, 57.2, 53.8, 55.4, 63.2],
    "GPT-3.5-Turbo (16K)": [75.7, 57.3, 54.1, 55.4, 63.1],
    "Claude-1.3": [59.9, 55.9, 56.8, 57.2, 60.1],
    "MPT-30B-Instruct": [53.7, 51.8, 52.2, 52.7, 56.3],
    "LongChat-13B (16K)": [68.6, 57.4, 55.3, 52.5, 55.0],
}
LIU_CLOSED_BOOK = 56.1     # GPT-3.5-Turbo, Table 1 (TACL p. 161)
LIU_TOKENS_20 = 2946.2     # Table 3 (arXiv v3 PDF p. 17), GPT-3.5-Turbo tokenizer, 20 documents


# ---------------------------------------------------------------------------
def example_orderings():
    print("Example 1: how many orderings of k demonstrations (k!)")
    for k in (4, 8, 16, 64):
        f = math.factorial(k)
        print(f"  {k}! = {f:,}" if f < 10 ** 6 else f"  {k}! = {f:.3g}")
    print()


# Zhao et al. p. 12697, the two-shot prompt (four lines).
ZHAO_PROMPT = ("Input: Subpar acting. Sentiment: Negative\n"
               "Input: Beautiful film. Sentiment: Positive\n"
               "Input: Amazing.\n"
               "Sentiment:")
# Wei et al. Fig. 1, p. 1: the exemplar, standard and with a chain of thought.
WEI_Q = ("Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. "
         "Each can has 3 tennis balls. How many tennis balls does he have now?")
WEI_STANDARD = WEI_Q + "\nA: The answer is 11."
WEI_COT = WEI_Q + ("\nA: Roger started with 5 balls. 2 cans of 3 tennis balls each is "
                   "6 tennis balls. 5 + 6 = 11. The answer is 11.")
KOJIMA = " Let's think step by step."


def example_tokens():
    print("Example 2: what a demonstration costs in tokens (GPT-2 tokenizer as a stand-in)")
    g = load("tokens").GPT2()
    z = len(g.ids(ZHAO_PROMPT))
    s = len(g.ids(WEI_STANDARD))
    c = len(g.ids(WEI_COT))
    k = len(g.ids(KOJIMA))
    print(f"  Zhao et al.'s two-shot prompt: {z} tokens")
    print(f"  Wei et al.'s exemplar: standard {s} tokens, with chain of thought {c} ({c / s:.2f} times)")
    print(f"  eight exemplars of these lengths: {8 * s} vs {8 * c} tokens")
    print(f"  Kojima et al.'s '{KOJIMA.strip()}': {k} tokens")
    print(f"  GPT-3's 2,048-token window holds at most {2048 // c} chain-of-thought exemplars of {c} tokens")
    print()
    return c


def example_middle():
    print("Example 3: where the middle of Liu et al.'s 20-document prompt is")
    per_doc = LIU_TOKENS_20 / 20
    print(f"  {LIU_TOKENS_20:,} tokens / 20 = {per_doc:.1f} tokens per document (if spread evenly; they are not)")
    for pos in (1, 10, 20):
        print(f"  position {pos} begins about {(pos - 1) / 20:.0%} of the way in "
              f"(token {(pos - 1) * per_doc:,.0f})")
    print()


def example_u_curve():
    print("Example 4: the U-curve in numbers (Liu et al., Table 6, 20 documents)")
    for name, row in LIU_TABLE6.items():
        worst = min(row)
        print(f"  {name}: first {row[0]}, worst {worst} (position {LIU_POSITIONS[row.index(worst)]}), "
              f"last {row[-1]}; first minus worst {row[0] - worst:.1f}")
    row = LIU_TABLE6["GPT-3.5-Turbo"]
    print(f"  GPT-3.5-Turbo worst minus closed-book ({LIU_CLOSED_BOOK}): {min(row) - LIU_CLOSED_BOOK:+.1f}")
    print()


def example_gains(cot_tokens):
    print("Example 5: gains and losses, arithmetic on printed numbers")
    for fam, rows in WEI_TABLE2.items():
        for name, _, std, cot in rows:
            print(f"  Wei Table 2, {fam} {name}: {std} -> {cot} ({cot - std:+.1f})")
    print(f"  PaLM 540B ratio: {56.9 / 17.9:.1f} times")
    print(f"  Kojima MultiArith 17.7 -> 78.7 ({78.7 - 17.7:+.1f}); GSM8K 10.4 -> 40.7 ({40.7 - 10.4:+.1f})")
    print(f"  Kojima Table 4 range of wordings: 9.3 to 78.7 ({78.7 - 9.3:.1f} points); "
          f"'Let's think' 57.5 vs no trigger 17.7")
    print(f"  Wang et al. PaLM-540B: 56.5 -> 74.4 ({74.4 - 56.5:+.1f})")
    print(f"  Zhao et al. order spread: 54.3 -> 93.4 ({93.4 - 54.3:.1f} points)")
    print(f"  Wei et al. 2023 flipped labels: 90.3 -> 22.5 ({22.5 - 90.3:+.1f} points)")
    print(f"  Sclar et al. Fig. 1: 0.036 to 0.804 ({(0.804 - 0.036) * 100:.1f} points)")
    print(f"  Turpin et al.: 1 of 426 = {1 / 426:.2%}")
    print()
    print("Example 6: self-consistency's price")
    for n in (5, 10, 40):
        print(f"  {n} sampled chains: {n} times the generated tokens; "
              f"with a {cot_tokens}-token chain as a stand-in, {n * cot_tokens:,} vs {cot_tokens}")
    print()


MASK_TOKENS = ["{", '"', "Hello", " The", "}", "newline"]
MASK_SCORES = [1.0, 0.5, 3.0, 2.5, 0.2, 0.1]   # constructed, not from a model


def softmax(scores):
    m = max(scores)
    e = [math.exp(s - m) for s in scores]
    z = sum(e)
    return [x / z for x in e]


def masked(scores, allowed):
    # Disallowed scores set to minus infinity, then softmax as before.
    return softmax([s if t in allowed else -math.inf for t, s in zip(MASK_TOKENS, scores)])


def example_mask():
    print("Example 7: a grammar mask on constructed scores")
    p = softmax(MASK_SCORES)
    print("  before: " + ", ".join(f"{t!r} {x:.3f}" for t, x in zip(MASK_TOKENS, p)))
    for allowed in ({"{"}, {"{", '"'}):
        q = masked(MASK_SCORES, allowed)
        held = sum(x for t, x in zip(MASK_TOKENS, p) if t in allowed)
        print(f"  allow {sorted(allowed)}: model had {held:.3f} on them; after: "
              + ", ".join(f"{t!r} {x:.3f}" for t, x in zip(MASK_TOKENS, q) if x > 0))
    print()


def example_confidence():
    print("Example 8: Kalai et al.'s confidence target, penalty t/(1 - t)")
    for t in (0.5, 0.75, 0.9):
        print(f"  t = {t}: penalty {t / (1 - t):.0f}")
    t = 0.75
    pen = t / (1 - t)
    for p in (0.6, 0.75, 0.9):
        print(f"  t = 0.75, confidence p = {p}: expected score {p - (1 - p) * pen:+.2f} (abstaining scores 0)")
    print(f"  with the printed penalty 2, break-even confidence would be {2 / 3:.3f}")
    print()


def example_sizes():
    print("Example 9: context sizes in words (OpenAI's estimate: 3/4 of a word per token)")
    for n in (2048, 1_000_000):
        print(f"  {n:,} tokens: about {n * 3 / 4:,.0f} words")
    print(f"  1,000,000 / 2,048 = {1_000_000 / 2048:.0f} times GPT-3's window")
    print()


def example_reynolds():
    print("Example 10: Reynolds and McDonell's Fig. 3, f(x) = x*x")
    f = lambda x: x * x  # noqa: E731
    print(f"  f(3) = {f(3)}; f(f(3)) = f({f(3)}) = {f(f(3))}; GPT-3's printed answer was 27 = 3*3*3 = {3 * 3 * 3}")
    print()


if __name__ == "__main__":
    example_orderings()
    cot = example_tokens()
    example_middle()
    example_u_curve()
    example_gains(cot)
    example_mask()
    example_confidence()
    example_sizes()
    example_reynolds()
