#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `backprop` [D-009].

Run: python3 code/checks/backprop.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. Data and starting weights are chosen for illustration;
the arithmetic is exact, and every backpropagated gradient is checked against
a finite-difference estimate.
"""
import math
import random

# ---------------------------------------------------------------------------
# Example 1: gradient descent on a regression bowl.
# Fit y = w * x to three points by minimizing the mean squared error.
DATA = [(1, 2), (2, 4), (3, 7)]


def mse(w):
    return sum((w * x - y) ** 2 for x, y in DATA) / len(DATA)


def mse_slope(w):
    """Derivative of the mean squared error with respect to w."""
    return sum(2 * x * (w * x - y) for x, y in DATA) / len(DATA)


def example_bowl():
    print("Example 1: gradient descent on the mean squared error of y = w * x")
    best = sum(x * y for x, y in DATA) / sum(x * x for x, _ in DATA)
    print(f"  least-squares answer: w = {best:.3f}, error there = {mse(best):.3f}")
    print(f"  at w = 0: error = {mse(0):.3f}, slope = {mse_slope(0):.3f}")
    for rate in (0.02, 0.1, 0.25):
        w = 0.0
        path = [w]
        for _ in range(10):
            w = w - rate * mse_slope(w)
            path.append(w)
        shown = ", ".join(f"{v:.2f}" for v in path[:6])
        print(f"  learning rate {rate}: w over the first 5 steps = {shown}; "
              f"after 10 steps w = {path[-1]:.3f}, error = {mse(path[-1]):.3f}")
    print()


# ---------------------------------------------------------------------------
# Examples 2-4: a 2-2-1 network of sigmoid units learning XOR, trained by
# back-propagation on the total squared error, as in Rumelhart et al. (1986).
POINTS = [(0, 0), (0, 1), (1, 0), (1, 1)]
XOR = [0, 1, 1, 0]


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


# Parameters: h1 = sig(a11*x1 + a12*x2 + b1), h2 = sig(a21*x1 + a22*x2 + b2),
# y = sig(c1*h1 + c2*h2 + c0).
NAMES = ["a11", "a12", "b1", "a21", "a22", "b2", "c1", "c2", "c0"]

# Starting weights for the one-step worked example (small, unequal).
START = dict(a11=0.5, a12=-0.4, b1=0.1, a21=-0.3, a22=0.6, b2=-0.2,
             c1=0.7, c2=-0.5, c0=0.2)


def forward(p, x):
    z1 = p["a11"] * x[0] + p["a12"] * x[1] + p["b1"]
    z2 = p["a21"] * x[0] + p["a22"] * x[1] + p["b2"]
    h1, h2 = sigmoid(z1), sigmoid(z2)
    zo = p["c1"] * h1 + p["c2"] * h2 + p["c0"]
    return h1, h2, sigmoid(zo)


def error(p, cases=None):
    """Total squared error, halved, as in the 1986 papers."""
    cases = cases if cases is not None else list(zip(POINTS, XOR))
    return sum(0.5 * (forward(p, x)[2] - d) ** 2 for x, d in cases)


def backprop(p, x, d):
    """Gradients of 0.5 * (y - d)^2 for one case, by the chain rule."""
    h1, h2, y = forward(p, x)
    # Blame at the output: how the error changes with the output unit's
    # weighted sum.
    delta_o = (y - d) * y * (1 - y)
    # Blame passed back to each hidden unit through its outgoing weight.
    delta_1 = delta_o * p["c1"] * h1 * (1 - h1)
    delta_2 = delta_o * p["c2"] * h2 * (1 - h2)
    grads = dict(
        c1=delta_o * h1, c2=delta_o * h2, c0=delta_o,
        a11=delta_1 * x[0], a12=delta_1 * x[1], b1=delta_1,
        a21=delta_2 * x[0], a22=delta_2 * x[1], b2=delta_2,
    )
    return (h1, h2, y), (delta_o, delta_1, delta_2), grads


def numeric_grad(p, cases, name, eps=1e-6):
    up, down = dict(p), dict(p)
    up[name] += eps
    down[name] -= eps
    return (error(up, cases) - error(down, cases)) / (2 * eps)


def example_one_step():
    print("Example 2: one forward pass, one backward pass, one update")
    x, d = (1, 0), 1
    rate = 0.5
    p = dict(START)
    (h1, h2, y), (do, d1, d2), g = backprop(p, x, d)
    z1 = p["a11"] * x[0] + p["a12"] * x[1] + p["b1"]
    z2 = p["a21"] * x[0] + p["a22"] * x[1] + p["b2"]
    zo = p["c1"] * h1 + p["c2"] * h2 + p["c0"]
    print(f"  input {x}, wanted output {d}")
    print(f"  forward:  hidden 1 sum = {z1:+.3f} -> {h1:.3f};  hidden 2 sum = {z2:+.3f} -> {h2:.3f}")
    print(f"            output sum = {zo:+.3f} -> output {y:.3f}")
    print(f"  error for this case = 0.5 * ({y:.3f} - {d})^2 = {0.5 * (y - d) ** 2:.4f}")
    print(f"  backward: blame at output = {do:+.4f}")
    print(f"            blame at hidden 1 = {d1:+.4f} (through weight {p['c1']:+.1f})")
    print(f"            blame at hidden 2 = {d2:+.4f} (through weight {p['c2']:+.1f})")
    worst = 0.0
    for name in NAMES:
        num = numeric_grad(p, [(x, d)], name)
        worst = max(worst, abs(num - g[name]))
    print(f"  largest gap between backprop and finite-difference gradients: {worst:.1e}")
    new = {k: p[k] - rate * g[k] for k in NAMES}
    print(f"  update with learning rate {rate}:")
    for k in NAMES:
        print(f"    {k}: {p[k]:+.3f} - {rate} * ({g[k]:+.4f}) = {new[k]:+.4f}")
    y_new = forward(new, x)[2]
    print(f"  output for {x} after the update: {y:.3f} -> {y_new:.3f}")
    print()


def train(p, rate, epochs, record=()):
    """Full-batch gradient descent: add up gradients over all four cases,
    then update once per sweep, as in the 1986 Nature letter."""
    p = dict(p)
    cases = list(zip(POINTS, XOR))
    log = {}
    for epoch in range(1, epochs + 1):
        total = {k: 0.0 for k in NAMES}
        for x, d in cases:
            _, _, g = backprop(p, x, d)
            for k in NAMES:
                total[k] += g[k]
        for k in NAMES:
            p[k] -= rate * total[k]
        if epoch in record:
            log[epoch] = error(p)
    return p, log


def solved(p):
    return all((forward(p, x)[2] > 0.5) == bool(d) for x, d in zip(POINTS, XOR))


def random_start(rng, spread=1.0):
    return {k: rng.uniform(-spread, spread) for k in NAMES}


RATE = 2.0
EPOCHS = 5000
SEED = 1


def example_training():
    print(f"Example 3: training on all four XOR cases, learning rate {RATE}, "
          f"random start in [-1, 1], seed {SEED}")
    # Check the summed gradient against finite differences once.
    rng = random.Random(SEED)
    p0 = random_start(rng)
    cases = list(zip(POINTS, XOR))
    total = {k: sum(backprop(p0, x, d)[2][k] for x, d in cases) for k in NAMES}
    worst = max(abs(numeric_grad(p0, cases, k) - total[k]) for k in NAMES)
    print(f"  gradient check at the start: largest gap {worst:.1e}")
    marks = (0, 100, 500, 1000, 2000, 5000)
    p, log = train(p0, RATE, EPOCHS, record=marks)
    log[0] = error(p0)
    for m in marks:
        print(f"    after {m:>4} sweeps: total error = {log[m]:.4f}")
    for x, d in cases:
        print(f"    input {x}: output {forward(p, x)[2]:.3f}, wanted {d}")
    print(f"  solved (every output on the correct side of 0.5): {solved(p)}")
    # When does the stall end, and when is XOR first solved?
    q = dict(p0)
    below, first_solved = None, None
    for epoch in range(1, EPOCHS + 1):
        q, _ = train(q, RATE, 1)
        if below is None and error(q) < 0.45:
            below = epoch
        if first_solved is None and solved(q):
            first_solved = epoch
        if below and first_solved:
            break
    print(f"  error first drops below 0.45 at sweep {below}; "
          f"XOR first solved at sweep {first_solved}")
    print()

    # How often does training from a random start succeed?
    trials, wins = 100, 0
    rng = random.Random(0)
    for _ in range(trials):
        q, _ = train(random_start(rng), RATE, EPOCHS)
        wins += solved(q)
    print(f"  {trials} random starts, {EPOCHS} sweeps each: {wins} solve XOR, "
          f"{trials - wins} have not solved it yet")
    print()


def example_symmetry():
    print("Example 4: all weights start equal (0.5)")
    p0 = {k: 0.5 for k in NAMES}
    p, _ = train(p0, RATE, EPOCHS)
    same = all(abs(p[a] - p[b]) < 1e-12 for a, b in (("a11", "a21"), ("a12", "a22"),
                                                       ("b1", "b2"), ("c1", "c2")))
    print(f"  after {EPOCHS} sweeps the two hidden units are still identical: {same}")
    print(f"  total error = {error(p):.4f}; solved: {solved(p)}")
    for x, d in zip(POINTS, XOR):
        print(f"    input {x}: output {forward(p, x)[2]:.3f}, wanted {d}")
    print()


if __name__ == "__main__":
    example_bowl()
    example_one_step()
    example_training()
    example_symmetry()
