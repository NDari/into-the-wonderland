#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `deep-turn` [D-009].

Run: python3 code/checks/deep-turn.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. Examples 3, 5, 6 and 7 redo arithmetic on numbers
printed in the sources logged in book1/sources/deep-turn.md; the others use
illustrative values.
"""
import math

# ---------------------------------------------------------------------------
# Example 1: a layer is a matrix product, and its outputs are independent sums.
W = [[0.2, -0.5, 1.0],
     [0.7, 0.1, -0.3]]
X = [1.0, 2.0, 3.0]


def example_matmul():
    print("Example 1: one layer as a matrix product")
    products = [[w * x for w, x in zip(row, X)] for row in W]
    for i, row in enumerate(products):
        print(f"  output {i + 1}: " + " + ".join(f"{p:+.1f}" for p in row) + f" = {sum(row):+.1f}")
    n_mult = sum(len(r) for r in products)
    print(f"  {n_mult} multiplications, {len(W)} independent sums")
    n, m, batch = 4096, 4096, 128
    print(f"  AlexNet's 4096 x 4096 layer: {n * m:,} multiply-adds per image, "
          f"{n * m * batch:,} per batch of {batch}; {m * batch:,} independent outputs")
    print()


# ---------------------------------------------------------------------------
# Example 2: slopes of the sigmoid and of the rectified linear unit.
def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def example_slopes():
    print("Example 2: slopes")
    for z in (0, 2, 5):
        s = sigmoid(z)
        print(f"  sigmoid at {z}: output {s:.3f}, slope {s * (1 - s):.4f}")
    for z in (3.0, -2.0):
        print(f"  ReLU at {z:+.0f}: output {max(0.0, z):.0f}, slope {1 if z > 0 else 0}")
    for layers in (1, 5, 10):
        print(f"  best case through {layers:>2} layers: sigmoid {0.25 ** layers:.2e}, ReLU {1 ** layers}")
    print()


# ---------------------------------------------------------------------------
# Example 3: AlexNet's parameters from the layer sizes printed on pp. 4-5.
# The fully connected layer's input of 6 x 6 x 256 is inferred (see ledger).
LAYERS = [
    ("conv1", 96 * 11 * 11 * 3, 96),
    ("conv2", 256 * 5 * 5 * 48, 256),
    ("conv3", 384 * 3 * 3 * 256, 384),
    ("conv4", 384 * 3 * 3 * 192, 384),
    ("conv5", 256 * 3 * 3 * 192, 256),
    ("fc6", 6 * 6 * 256 * 4096, 4096),
    ("fc7", 4096 * 4096, 4096),
    ("fc8", 4096 * 1000, 1000),
]


def example_alexnet():
    print("Example 3: AlexNet's parameters (weights plus biases)")
    total = sum(w + b for _, w, b in LAYERS)
    conv = sum(w + b for name, w, b in LAYERS if name.startswith("conv"))
    for name, w, b in LAYERS:
        print(f"  {name}: {w + b:>12,} ({(w + b) / total:.1%})")
    print(f"  total {total:,}; convolutional layers {conv:,} ({conv / total:.1%}); "
          f"fully connected {total - conv:,} ({(total - conv) / total:.1%})")
    print()


# ---------------------------------------------------------------------------
# Example 4: top-1 and top-5 error by hand, on five made-up images.
CASES = [
    ("leopard", ["leopard", "jaguar", "cheetah", "snow leopard", "cat"]),
    ("cherry", ["dalmatian", "grape", "cherry", "elderberry", "currant"]),
    ("mite", ["black widow", "cockroach", "tick", "starfish", "mite"]),
    ("grille", ["convertible", "grille", "pickup", "beach wagon", "fire engine"]),
    ("mushroom", ["agaric", "gyromitra", "stinkhorn", "earthstar", "hen-of-the-woods"]),
]


def example_top5():
    print("Example 4: top-1 and top-5 error on five images")
    top1 = sum(guesses[0] != truth for truth, guesses in CASES)
    top5 = sum(truth not in guesses for truth, guesses in CASES)
    for truth, guesses in CASES:
        print(f"  true '{truth}': first guess '{guesses[0]}', in top five: {truth in guesses}")
    print(f"  top-1 error {top1}/{len(CASES)} = {top1 / len(CASES):.0%}; "
          f"top-5 error {top5}/{len(CASES)} = {top5 / len(CASES):.0%}")
    print()


# ---------------------------------------------------------------------------
# Example 5: ILSVRC winning top-5 error, provided training data only.
ILSVRC = [(2010, "NEC", 28.2), (2011, "XRCE", 25.8), (2012, "SuperVision", 16.4),
          (2013, "Clarifai", 11.7), (2014, "GoogLeNet", 6.7), (2015, "ResNet", 3.57)]
RUNNER_UP_2012 = 26.2
EXTRA_DATA_2012 = 15.3
HUMAN_ONE_ANNOTATOR = 5.1


def example_ilsvrc():
    print("Example 5: ILSVRC winners and ratios")
    for year, team, err in ILSVRC:
        print(f"  {year} {team}: {err}%")
    print(f"  2010 to 2014: {28.2 / 6.7:.1f} times fewer errors; 2012 to 2014: {16.4 / 6.7:.1f} times")
    print(f"  2012 entry vs 2012 runner-up: {1 - 16.4 / RUNNER_UP_2012:.0%} fewer errors "
          f"(provided data), {1 - EXTRA_DATA_2012 / RUNNER_UP_2012:.0%} (with extra data)")
    print(f"  2012 winner vs 2011 winner: {1 - 16.4 / 25.8:.0%} fewer errors")
    print(f"  ILSVRC 2010 images: 1,261,406 + 50,000 + 150,000 = {1261406 + 50000 + 150000:,}")
    print()


# ---------------------------------------------------------------------------
# Example 6: small checks on numbers printed in the sources.
def example_small():
    print("Example 6: small checks")
    hinton2006 = 784 * 500 + 500 * 500 + (500 + 10) * 2000
    print(f"  Hinton et al. 2006 weights: 784x500 + 500x500 + 510x2000 = {hinton2006:,}")
    print(f"  Deng et al. 2009: 3,200,000 / 5,247 = {3200000 / 5247:.0f} images per category")
    for cpu, gpu in ((497, 38.6), (2987, 184), (93586, 1376), (125381, 1726)):
        print(f"  Raina et al. speedup: {cpu} / {gpu} = {cpu / gpu:.1f}")
    print()


# ---------------------------------------------------------------------------
# Example 7: speech recognition, relative reductions (Hinton et al. 2012, Table 3).
SPEECH = [("Switchboard, test set 1", 27.4, 18.5), ("Switchboard, test set 2", 23.6, 16.1),
          ("Google Voice Input", 16.0, 12.3), ("Bing voice search (sentence errors)", 36.2, 30.4),
          ("YouTube", 52.3, 47.6), ("English Broadcast News", 18.8, 17.5)]


def example_speech():
    print("Example 7: speech error rates, old system vs deep network")
    for task, old, new in SPEECH:
        print(f"  {task}: {old} -> {new}, {1 - new / old:.0%} relative reduction")
    print()


if __name__ == "__main__":
    example_matmul()
    example_slopes()
    example_alexnet()
    example_top5()
    example_ilsvrc()
    example_small()
    example_speech()
