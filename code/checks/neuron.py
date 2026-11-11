#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `neuron` [D-009].

Run: python3 code/checks/neuron.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. Inputs and weights in the examples are chosen for
illustration; the arithmetic on them is exact.
"""
import math
from itertools import product

POINTS = [(0, 0), (0, 1), (1, 0), (1, 1)]
TARGETS = {
    "AND": [0, 0, 0, 1],
    "OR": [0, 1, 1, 1],
    "XOR": [0, 1, 1, 0],
}


def step(z):
    """Fire (1) if the weighted sum is above zero, else stay silent (0)."""
    return 1 if z > 0 else 0


def weighted_sum(w, b, x):
    return sum(wi * xi for wi, xi in zip(w, x)) + b


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


# Example 1: one neuron as a weighted vote.
VOTE_INPUTS = [1, 0, 1]
VOTE_WEIGHTS = [0.6, 0.9, -0.4]
VOTE_BIAS = -0.1


def example_vote():
    print("Example 1: a weighted vote")
    terms = [w * x for w, x in zip(VOTE_WEIGHTS, VOTE_INPUTS)]
    for i, (x, w, t) in enumerate(zip(VOTE_INPUTS, VOTE_WEIGHTS, terms), 1):
        print(f"  input {i}: x = {x}, weight = {w:+.1f}, contribution = {t:+.1f}")
    z = weighted_sum(VOTE_WEIGHTS, VOTE_BIAS, VOTE_INPUTS)
    print(f"  bias = {VOTE_BIAS:+.1f}")
    print(f"  weighted sum = {z:+.1f}, output (step) = {step(z)}")
    print(f"  with a sigmoid instead of the step: {sigmoid(z):.3f}")
    print()


# Example 2: AND and OR with hand-set weights (McCulloch-Pitts style:
# every input counts 1, and the neuron fires when enough inputs are on).
GATES = {
    "AND": ([1, 1], -1.5),  # fires only when both inputs are on
    "OR": ([1, 1], -0.5),   # fires when at least one input is on
}


def example_gates():
    print("Example 2: AND and OR with one threshold neuron")
    for name, (w, b) in GATES.items():
        print(f"  {name}: weights {w}, bias {b:+.1f}")
        for x, target in zip(POINTS, TARGETS[name]):
            z = weighted_sum(w, b, x)
            out = step(z)
            ok = "ok" if out == target else "WRONG"
            print(f"    x = {x}: sum = {z:+.1f}, output = {out}, wanted = {target} {ok}")
    print()


# Example 3: the perceptron learning rule, from zero weights.
def train_perceptron(name, epochs, rate=1.0, verbose=True):
    w, b = [0.0, 0.0], 0.0
    history = []
    updates = []
    for epoch in range(1, epochs + 1):
        errors = 0
        for x, target in zip(POINTS, TARGETS[name]):
            z = weighted_sum(w, b, x)
            out = step(z)
            err = target - out
            if err:
                errors += 1
                w = [wi + rate * err * xi for wi, xi in zip(w, x)]
                b = b + rate * err
                updates.append((epoch, x, out, target, err, w, b))
            if verbose:
                print(f"    epoch {epoch}, x = {x}: sum = {z:+.0f}, output = {out}, "
                      f"wanted = {target}, error = {err:+d} -> weights {w}, bias {b:+.0f}")
        history.append(errors)
        if errors == 0:
            break
    return w, b, history, updates


def example_perceptron_and():
    print("Example 3: perceptron rule on AND, starting from zero, rate 1")
    w, b, history, updates = train_perceptron("AND", epochs=20)
    print("  only the steps with a mistake (each changes the weights):")
    for epoch, x, out, target, err, wn, bn in updates:
        print(f"    epoch {epoch}, x = {x}: output {out}, wanted {target}, "
              f"error {err:+d} -> w1 = {wn[0]:.0f}, w2 = {wn[1]:.0f}, bias = {bn:+.0f}")
    print(f"  mistakes per epoch: {history} (total {sum(history)})")
    print(f"  final weights {w}, bias {b:+.0f}")
    print()


def example_perceptron_xor():
    print("Example 4: perceptron rule on XOR, 20 epochs")
    w, b, history, _ = train_perceptron("XOR", epochs=20, verbose=False)
    print(f"  mistakes per epoch: {history}")
    print(f"  never reaches zero mistakes: {0 not in history}")
    print()


# Example 5: search a grid of weights for a single line that separates
# each function. Not a proof, but a direct check of the claim.
def example_grid():
    print("Example 5: grid search over weights and bias")
    values = [v / 4 for v in range(-12, 13)]  # -3.0 to 3.0 in steps of 0.25
    grid = list(product(values, repeat=3))
    print(f"  {len(grid):,} combinations of (w1, w2, b), each from -3 to 3 in steps of 0.25")
    for name, targets in TARGETS.items():
        hits = sum(
            1 for w1, w2, b in grid
            if [step(weighted_sum([w1, w2], b, x)) for x in POINTS] == targets
        )
        print(f"  {name}: {hits:,} combinations compute it")
    print()


# Example 6: the bridge to logistic regression. Same weighted sum, sigmoid
# instead of step. Larger weights make the sigmoid behave like a step.
def example_sigmoid():
    print("Example 6: AND with a sigmoid instead of a step")
    for scale in (1, 10):
        w = [1 * scale, 1 * scale]
        b = -1.5 * scale
        print(f"  weights {w}, bias {b:+.1f}:")
        for x in POINTS:
            z = weighted_sum(w, b, x)
            print(f"    x = {x}: sum = {z:+.1f}, sigmoid = {sigmoid(z):.3f}")
    print()


# Example 7: two layers compute XOR. Hidden neuron 1 is OR, hidden neuron 2
# is AND, and the output fires for "OR and not AND".
def example_two_layer_xor():
    print("Example 7: XOR from two layers (OR and AND feeding one more neuron)")
    (w_or, b_or), (w_and, b_and) = GATES["OR"], GATES["AND"]
    w_out, b_out = [1, -1], -0.5
    print(f"  output neuron: weights {w_out}, bias {b_out:+.1f}")
    for x, target in zip(POINTS, TARGETS["XOR"]):
        h = [step(weighted_sum(w_or, b_or, x)), step(weighted_sum(w_and, b_and, x))]
        out = step(weighted_sum(w_out, b_out, h))
        ok = "ok" if out == target else "WRONG"
        print(f"    x = {x}: OR = {h[0]}, AND = {h[1]}, output = {out}, XOR = {target} {ok}")
    print()


if __name__ == "__main__":
    example_vote()
    example_gates()
    example_perceptron_and()
    example_perceptron_xor()
    example_grid()
    example_sigmoid()
    example_two_layer_xor()
