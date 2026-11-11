#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `depth` [D-009].

Run: python3 code/checks/depth.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. Random draws use fixed seeds. Data and settings are
illustrative; Example 6 redoes arithmetic on numbers printed in the sources.
"""
import itertools
import math
import random

# ---------------------------------------------------------------------------
# Example 1: how the spread of starting weights changes a signal's size
# through 10 linear layers of 256 units (variance of the activations).
def layer_variances(rule, n=256, layers=10, seed=0, samples=200):
    rng = random.Random(seed)
    if rule == "old":                    # uniform in +-1/sqrt(n): variance 1/(3n)
        bound = 1 / math.sqrt(n)
        draw = lambda: rng.uniform(-bound, bound)
    else:                                # Glorot: variance 2/(n_in + n_out) = 1/n here
        bound = math.sqrt(6 / (n + n))
        draw = lambda: rng.uniform(-bound, bound)
    xs = [[rng.gauss(0, 1) for _ in range(n)] for _ in range(samples)]
    out = []
    for _ in range(layers):
        W = [[draw() for _ in range(n)] for _ in range(n)]
        xs = [[sum(w * v for w, v in zip(row, x)) for row in W] for x in xs]
        flat = [v for x in xs for v in x]
        m = sum(flat) / len(flat)
        out.append(sum((v - m) ** 2 for v in flat) / len(flat))
    return out


def example_init():
    print("Example 1: variance of the signal after each of 10 linear layers (256 units, input variance 1)")
    n = 512
    print(f"  for a layer with {n} inputs and {n} outputs: old rule variance 1/(3n) = {1 / (3 * n):.6f}; "
          f"Glorot 2/(n_in+n_out) = {2 / (n + n):.6f}; He sd sqrt(2/n) = {math.sqrt(2 / n):.4f}")
    for rule in ("old", "glorot"):
        v = layer_variances(rule)
        print(f"  {rule}: " + ", ".join(f"{x:.3g}" for x in v))
    print(f"  theory for the old rule: (1/3)^10 = {(1 / 3) ** 10:.2g}")
    print()


# ---------------------------------------------------------------------------
# Example 2: dropout keeps the expected output the same.
def example_dropout():
    print("Example 2: dropout on a unit whose output is 2.0")
    keep = 0.5
    print(f"  keep with probability {keep}: training output 0 or 2.0, average {keep * 2.0}; "
          f"test time multiplies by {keep}: {2.0 * keep}")
    drop = 0.5
    print(f"  framework style, drop with probability {drop}, scale by 1/(1 - p) in training: "
          f"0 or {2.0 / (1 - drop)}, average {(1 - drop) * 2.0 / (1 - drop)}; test time unchanged: 2.0")
    for units in (10, 100):
        print(f"  thinned networks with {units} units: 2^{units} = {2 ** units:.3g}")
    # Dropout on the inputs of a linear regression equals ridge in expectation.
    X = [[1.0, 2.0], [3.0, -1.0], [0.5, 4.0]]
    y = [3.0, 1.0, 2.0]
    w = [0.7, 0.4]
    p = 0.8
    expected = 0.0
    cells = [(i, j) for i in range(3) for j in range(2)]
    for mask in itertools.product((0, 1), repeat=len(cells)):
        prob = 1.0
        M = [[0, 0], [0, 0], [0, 0]]
        for (i, j), keep_ij in zip(cells, mask):
            prob *= p if keep_ij else (1 - p)
            M[i][j] = keep_ij
        loss = sum((y[i] - sum(M[i][j] * X[i][j] * w[j] for j in range(2))) ** 2 for i in range(3))
        expected += prob * loss
    fit = sum((y[i] - p * sum(X[i][j] * w[j] for j in range(2))) ** 2 for i in range(3))
    gamma2 = [sum(X[i][j] ** 2 for i in range(3)) for j in range(2)]
    penalty = p * (1 - p) * sum(g * wj * wj for g, wj in zip(gamma2, w))
    print(f"  linear regression, inputs kept with probability {p}: average loss over all 64 masks "
          f"{expected:.4f}; ridge-style formula {fit:.4f} + {penalty:.4f} = {fit + penalty:.4f}")
    print()


# ---------------------------------------------------------------------------
# Example 3: batch normalization (down a column) and layer normalization
# (along a row) on the same small table: 4 examples x 3 units.
TABLE = [[2, 1, 0], [4, 3, 1], [6, 2, 2], [8, 6, 1]]
EPS = 1e-5


def normalize(values):
    m = sum(values) / len(values)
    var = sum((v - m) ** 2 for v in values) / len(values)
    return m, var, [(v - m) / math.sqrt(var + EPS) for v in values]


def example_norm():
    print("Example 3: batch norm and layer norm on a 4 x 3 table")
    col = [row[0] for row in TABLE]
    m, var, z = normalize(col)
    print(f"  batch norm, unit 1 across the 4 examples {col}: mean {m:g}, variance {var:g}, "
          f"normalized " + ", ".join(f"{v:.3f}" for v in z))
    gamma, beta = 2.0, 1.0
    print(f"  with scale {gamma} and shift {beta}: " + ", ".join(f"{gamma * v + beta:.3f}" for v in z))
    g2, b2 = math.sqrt(var + EPS), m
    print(f"  with scale sqrt(variance) and shift mean: " + ", ".join(f"{g2 * v + b2:.3f}" for v in z))
    for k in (0, 3):
        m, var, z = normalize(TABLE[k])
        print(f"  layer norm, example {k + 1} {TABLE[k]}: mean {m:g}, variance {var:.3f}, "
              f"normalized " + ", ".join(f"{v:.3f}" for v in z))
    print()


# ---------------------------------------------------------------------------
# Example 4: a residual block adds a correction to a running value.
def example_residual():
    print("Example 4: a running value and three residual blocks")
    x = [1.0, 2.0]
    corrections = [[0.1, -0.05], [-0.02, 0.08], [0.03, 0.01]]
    print(f"  start {x}")
    for k, c in enumerate(corrections, 1):
        x = [a + b for a, b in zip(x, c)]
        print(f"  after block {k}: + {c} -> [{x[0]:.2f}, {x[1]:.2f}]")
    rng = random.Random(7)
    slopes = [rng.uniform(-0.1, 0.1) for _ in range(20)]
    plain = math.prod(slopes)
    residual = math.prod(1 + s for s in slopes)
    print(f"  backward signal through 20 layers whose own slopes lie in [-0.1, 0.1]: "
          f"plain chain {abs(plain):.2g}; residual chain {residual:.2f}")
    print()


# ---------------------------------------------------------------------------
# Example 5: arithmetic on printed numbers.
def example_sources():
    print("Example 5: arithmetic on numbers in the sources")
    print(f"  dropout on MNIST: 1.60% and 0.95% of 10,000 = {0.016 * 10000:.0f} and {0.0095 * 10000:.0f} errors")
    print(f"  batch norm: 31.0 / 2.1 = {31.0 / 2.1:.1f} times fewer steps")
    print(f"  ResNet-34 baseline: 3.6 / 19.6 = {3.6 / 19.6:.0%} of VGG-19's multiply-adds; 152 / 19 = {152 / 19:.0f} times deeper")
    print()


if __name__ == "__main__":
    example_init()
    example_dropout()
    example_norm()
    example_residual()
    example_sources()
