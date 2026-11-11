#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `toolkit` [D-009].

Run: python3 code/checks/toolkit.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. Random draws use fixed seeds, so the output is the
same on every run. Data and settings are illustrative.
"""
import math
import random

# ---------------------------------------------------------------------------
# Example 1: tensor shapes.
def example_shapes():
    print("Example 1: shapes")
    b, n_in, n_out = 4, 3, 2
    print(f"  batch {b} x {n_in} features, times {n_in} x {n_out} weights -> {b} x {n_out}; "
          f"{b * n_in} inputs, {n_in * n_out} weights")
    seqs, length, width, wide = 32, 128, 512, 2048
    print(f"  ({seqs}, {length}, {width}) = {seqs * length * width:,} numbers; through {width} x {wide} "
          f"weights ({width * wide:,}) -> ({seqs}, {length}, {wide}) = {seqs * length * wide:,} numbers")
    print()


# ---------------------------------------------------------------------------
# Example 2: minibatch gradients are noisy estimates of the full gradient.
def make_regression(seed=0, n=1000):
    rng = random.Random(seed)
    xs = [rng.uniform(0, 2) for _ in range(n)]
    ys = [2 * x + rng.gauss(0, 1) for x in xs]
    return xs, ys


def grad_at(w, xs, ys):
    """Slope of the mean squared error of y = w x, over the given examples."""
    return sum(2 * x * (w * x - y) for x, y in zip(xs, ys)) / len(xs)


def example_minibatch():
    print("Example 2: minibatch estimates of the gradient at w = 0 (y = 2x + noise, 1,000 points)")
    xs, ys = make_regression()
    full = grad_at(0.0, xs, ys)
    per_example = [grad_at(0.0, [x], [y]) for x, y in zip(xs, ys)]
    mean = sum(per_example) / len(per_example)
    sd_one = math.sqrt(sum((g - mean) ** 2 for g in per_example) / len(per_example))
    print(f"  full gradient {full:.2f}; spread of single-example gradients (sd) {sd_one:.2f}")
    rng = random.Random(1)
    idx = list(range(len(xs)))
    for size in (1, 10, 100):
        ests = []
        for _ in range(2000):
            pick = rng.sample(idx, size)
            ests.append(grad_at(0.0, [xs[i] for i in pick], [ys[i] for i in pick]))
        m = sum(ests) / len(ests)
        sd = math.sqrt(sum((e - m) ** 2 for e in ests) / len(ests))
        print(f"  minibatch of {size:>3}: mean {m:.2f}, sd {sd:.2f}  (sd / sqrt(size) predicts {sd_one / math.sqrt(size):.2f})")
    print()
    return xs, ys


# ---------------------------------------------------------------------------
# Example 3: momentum in a narrow valley, f(x, y) = (x^2 + 100 y^2) / 2.
def valley_grad(x, y):
    return x, 100 * y


def valley_f(x, y):
    return 0.5 * (x * x + 100 * y * y)


def run_valley(rate, momentum=0.0, start=(10.0, 1.0), limit=5000, record=False):
    x, y = start
    vx = vy = 0.0
    path = [(x, y)]
    for step in range(1, limit + 1):
        gx, gy = valley_grad(x, y)
        vx = momentum * vx - rate * gx
        vy = momentum * vy - rate * gy
        x, y = x + vx, y + vy
        if record:
            path.append((x, y))
        f = valley_f(x, y)
        if f < 1e-6:
            return step, path
        if f > 1e12:
            return None, path
    return None, path


def example_valley():
    print("Example 3: steps to reach f < 1e-6 from (10, 1), start f = 100")
    for rate, mom in ((0.01, 0.0), (0.019, 0.0), (0.021, 0.0), (0.01, 0.9)):
        steps, path = run_valley(rate, mom, record=True)
        label = f"learning rate {rate}" + (f", momentum {mom}" if mom else "")
        print(f"  {label}: {steps if steps else 'diverges'}")
    _, path = run_valley(0.021, 0.0, limit=4, record=True)
    print("  y with learning rate 0.021:", ", ".join(f"{p[1]:.3f}" for p in path))
    print("  momentum 0.9 multiplies the top speed by 1 / (1 - 0.9) =", round(1 / (1 - 0.9), 1))
    print()


# ---------------------------------------------------------------------------
# Example 4: Adam by hand, with the ICLR 2015 default settings.
def example_adam():
    print("Example 4: Adam on one weight, gradients 0.5, 0.4, -0.1")
    a, b1, b2, eps = 0.001, 0.9, 0.999, 1e-8
    w = m = v = 0.0
    for t, g in enumerate((0.5, 0.4, -0.1), 1):
        m = b1 * m + (1 - b1) * g
        v = b2 * v + (1 - b2) * g * g
        mh, vh = m / (1 - b1 ** t), v / (1 - b2 ** t)
        step = a * mh / (math.sqrt(vh) + eps)
        w -= step
        print(f"  step {t}: gradient {g:+.1f}, step size {step:.6f}, weight {w:+.6f}")
    for g in (0.001, 1000.0):
        mh = g
        vh = g * g
        print(f"  first gradient {g:g}: Adam's first step {a * mh / (math.sqrt(vh) + eps):.6f}; "
              f"plain gradient descent with rate 0.001 would step {0.001 * g:g}")
    print()


# ---------------------------------------------------------------------------
# Example 5: learning-rate schedules.
def transformer_lr(step, d_model=512, warmup=4000):
    return d_model ** -0.5 * min(step ** -0.5, step * warmup ** -1.5)


def cosine_lr(step, total=1000, peak=3e-4, floor_frac=0.1):
    lo = peak * floor_frac
    return lo + 0.5 * (peak - lo) * (1 + math.cos(math.pi * step / total))


def example_schedules():
    print("Example 5: learning-rate schedules")
    for s in (100, 1000, 4000, 10000, 100000):
        print(f"  Transformer schedule at step {s:>6}: {transformer_lr(s):.6f}")
    for frac in (0, 0.25, 0.5, 0.75, 1):
        print(f"  cosine from 3e-4 to 10% at {frac:.0%} of training: {cosine_lr(frac * 1000):.2e}")
    print(f"  linear scaling: 0.1 x 8,192 / 256 = {0.1 * 8192 / 256:g}")
    print()


# ---------------------------------------------------------------------------
# Example 6: gradient clipping.
def example_clip():
    print("Example 6: clipping the gradient (3, 4) to length 1")
    g = (3.0, 4.0)
    norm = math.hypot(*g)
    print(f"  length {norm:g}; clipped to ({g[0] / norm:g}, {g[1] / norm:g})")
    print()


# ---------------------------------------------------------------------------
# Example 7: loss curves from a small training run.
# 20 training examples, 15 random features, a linear model trained by
# minibatch gradient descent with momentum. Validation on 500 fresh examples.
def make_problem(seed=3, n_train=20, n_val=500, p=15):
    rng = random.Random(seed)
    true_w = [1.0, -2.0, 0.5] + [0.0] * (p - 3)

    def sample(n):
        X = [[rng.gauss(0, 1) for _ in range(p)] for _ in range(n)]
        y = [sum(a * b for a, b in zip(row, true_w)) + rng.gauss(0, 1.0) for row in X]
        return X, y
    return sample(n_train), sample(n_val)


def mse(w, X, y):
    return sum((sum(a * b for a, b in zip(row, w)) - t) ** 2 for row, t in zip(X, y)) / len(y)


def train_linear(rate, epochs, seed=5, batch=5, momentum=0.9):
    (X, y), (Xv, yv) = make_problem()
    p = len(X[0])
    rng = random.Random(seed)
    w = [0.0] * p
    vel = [0.0] * p
    log = []
    for epoch in range(1, epochs + 1):
        order = list(range(len(y)))
        rng.shuffle(order)
        for k in range(0, len(order), batch):
            idx = order[k:k + batch]
            grad = [0.0] * p
            for i in idx:
                err = sum(a * b for a, b in zip(X[i], w)) - y[i]
                for j in range(p):
                    grad[j] += 2 * err * X[i][j] / len(idx)
            vel = [momentum * v - rate * g for v, g in zip(vel, grad)]
            w = [a + b for a, b in zip(w, vel)]
        tr, va = mse(w, X, y), mse(w, Xv, yv)
        log.append((epoch, tr, va))
        if not math.isfinite(tr) or tr > 1e6:
            break
    return log


RUNS = {"too small (0.00005)": 0.00005, "good (0.001)": 0.001, "too large (0.08)": 0.08}


def example_curves():
    print("Example 7: a small training run (20 examples, 15 features, minibatches of 5, momentum 0.9)")
    runs = {name: train_linear(rate, 300) for name, rate in RUNS.items()}
    for name, log in runs.items():
        first, last = log[0], log[-1]
        print(f"  {name}: epoch 1 training {first[1]:.2f}; after epoch {last[0]} training {last[1]:.3g}, "
              f"validation {last[2]:.3g}")
    log = runs["good (0.001)"]
    best = min(log, key=lambda r: r[2])
    print(f"  good rate: lowest validation loss {best[2]:.2f} at epoch {best[0]} (training {best[1]:.2f}); "
          f"epoch {log[-1][0]}: validation {log[-1][2]:.2f}, training {log[-1][1]:.2f}")
    print(f"  starting point (all weights zero): validation {mse([0.0] * 15, *make_problem()[1]):.2f}")
    print()
    return runs


# ---------------------------------------------------------------------------
# Example 8: reverse-mode automatic differentiation by hand, on Baydin et al.'s
# example y = ln(x1) + x1 x2 - sin(x2) at (2, 5).
def example_autodiff():
    print("Example 8: reverse mode on y = ln(x1) + x1*x2 - sin(x2) at (2, 5)")
    x1, x2 = 2.0, 5.0
    v1, v2 = math.log(x1), x1 * x2
    v3 = math.sin(x2)
    y = v1 + v2 - v3
    # Backward: start from dy/dy = 1 and pass it to each intermediate.
    bar_v1, bar_v2, bar_v3 = 1.0, 1.0, -1.0
    bar_x1 = bar_v1 / x1 + bar_v2 * x2
    bar_x2 = bar_v2 * x1 + bar_v3 * math.cos(x2)
    print(f"  forward: ln(2) = {v1:.3f}, 2 x 5 = {v2:.0f}, sin(5) = {v3:.3f}, y = {y:.3f}")
    print(f"  backward: dy/dx1 = 1/x1 + x2 = {bar_x1:.3f}; dy/dx2 = x1 - cos(x2) = {bar_x2:.3f}")
    print()


if __name__ == "__main__":
    example_shapes()
    example_minibatch()
    example_valley()
    example_adam()
    example_schedules()
    example_clip()
    example_curves()
    example_autodiff()
