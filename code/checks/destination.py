#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `destination` [D-009].

Run: python3 code/checks/destination.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. The scores and probabilities in the toy examples are
made up for illustration; the arithmetic on them is exact.
"""
import math

# Example 1: one next-token prediction.
# Context: "The cat sat on the". A toy vocabulary of six candidate tokens with
# made-up scores (logits). A real model scores every token in its vocabulary.
CONTEXT = "The cat sat on the"
LOGITS = [
    (" mat", 3.0),
    (" floor", 2.0),
    (" sofa", 1.5),
    (" roof", 1.0),
    (" dog", -1.0),
    (" the", -2.0),
]
# A random draw between 0 and 1, fixed so the example is reproducible.
DRAW = 0.80


def softmax(scores):
    exps = [math.exp(s) for s in scores]
    total = sum(exps)
    return [e / total for e in exps], exps, total


def example_next_token():
    print(f"Example 1: next token after {CONTEXT!r}")
    probs, exps, total = softmax([s for _, s in LOGITS])
    print(f"  sum of exp(score) = {total:.3f}")
    print(f"  {'token':<8} {'score':>6} {'exp':>8} {'prob':>6} {'band':>13}")
    low = 0.0
    bands = []
    for (tok, s), e, p in zip(LOGITS, exps, probs):
        high = low + p
        bands.append((tok, low, high))
        print(f"  {tok!r:<8} {s:>6.1f} {e:>8.3f} {p:>6.3f}   {low:.3f}-{high:.3f}")
        low = high
    print(f"  probabilities sum to {sum(probs):.6f}")
    best = max(zip(LOGITS, probs), key=lambda x: x[1])
    print(f"  most likely: {best[0][0]!r} at {best[1]:.3f}")
    picked = next(tok for tok, lo, hi in bands if lo <= DRAW < hi)
    print(f"  random draw {DRAW:.2f} falls in the band of {picked!r}")
    print()


# Example 2: the probability of a whole text is a chain of next-token
# predictions multiplied together. Made-up conditional probabilities.
CHAIN = [
    ("The", "(start of text)", 0.040),
    (" cat", "The", 0.010),
    (" sat", "The cat", 0.150),
    (" on", "The cat sat", 0.400),
    (" the", "The cat sat on", 0.600),
    # The last step reuses the probability computed in Example 1.
    (" mat", "The cat sat on the", None),
]


def example_chain():
    print("Example 2: probability of a text as a product of next-token probabilities")
    running = 1.0
    p_mat = softmax([s for _, s in LOGITS])[0][0]
    for tok, given, p in CHAIN:
        p = p_mat if p is None else p
        running *= p
        print(f"  P({tok!r:<7} | {given!r:<22}) = {p:.3f}   running product = {running:.3e}")
    print(f"  probability of the whole text = {running:.3e}")
    print()


# Example 3: what a parameter count means as storage.
# Parameter counts as rounded in the sources logged in
# book1/sources/destination.md.
MODELS = [
    ("GPT-2 (largest)", 1.5e9),
    ("Llama 3.1 8B", 8e9),
    ("GPT-3", 175e9),
    ("Llama 3.1 405B", 405e9),
]
# Bytes per parameter for common number formats.
FORMATS = [("32-bit", 4), ("16-bit", 2)]


def example_storage():
    print("Example 3: storage for the parameters alone (1 GB = 10^9 bytes)")
    header = "".join(f"{name:>10}" for name, _ in FORMATS)
    print(f"  {'model':<18}{'parameters':>17}{header}")
    for model, n in MODELS:
        cells = "".join(f"{n * b / 1e9:>7,.0f} GB" for _, b in FORMATS)
        print(f"  {model:<18}{n:>17,.0f}{cells}")
    print()


if __name__ == "__main__":
    example_next_token()
    example_chain()
    example_storage()
