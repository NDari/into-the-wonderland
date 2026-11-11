#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `structure` [D-009].

Run: python3 code/checks/structure.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. Example 1 re-does the arithmetic behind numbers
printed in LeCun et al. (1989) and LeCun et al. (1998); the other examples use
illustrative values.
"""
import math

# ---------------------------------------------------------------------------
# Example 1: the 1989 zip-code network's counts, from its printed layer sizes.
def example_lecun1989():
    print("Example 1: LeCun et al. (1989), recomputed from the layer sizes")
    h1_units = 12 * 8 * 8                  # 12 feature maps of 8 by 8 units
    h1_conn = h1_units * (25 + 1)          # 5 by 5 window plus a bias each
    h1_params = h1_units + 25 * 12         # one bias per unit, one 5x5 filter per map
    print(f"  H1: {h1_units} units, {h1_conn:,} connections, {h1_params:,} free parameters")
    h2_units = 12 * 4 * 4
    h2_conn = h2_units * 201
    h2_params = 12 * 200 + h2_units
    h3_conn = h3_params = 30 * h2_units + 30
    out_conn = out_params = 10 * 30 + 10
    units = 16 * 16 + h1_units + h2_units + 30 + 10
    conn = h1_conn + h2_conn + h3_conn + out_conn
    params = h1_params + h2_params + h3_params + out_params
    print(f"  whole network: {units:,} units, {conn:,} connections, {params:,} free parameters")
    print(f"  data: 7,291 + 2,007 = {7291 + 2007:,} digits; 23 passes x 7,291 = {23 * 7291:,} presentations")
    print(f"  errors: 10 / 7,291 = {10 / 7291:.2%} (train); 102 / 2,007 = {102 / 2007:.2%} (test; printed as 5.0%)")
    # LeNet-5's first layer (1998).
    c1_params = 6 * (25 + 1)
    print(f"  LeNet-5 C1: 6 x (25 + 1) = {c1_params} parameters, "
          f"{c1_params} x 28 x 28 = {c1_params * 28 * 28:,} connections")
    print()


# ---------------------------------------------------------------------------
# Example 2: what weight sharing saves, for the 1989 first hidden layer.
def example_sharing():
    print("Example 2: parameters for the same 768 units of H1, three ways")
    shared = 768 + 25 * 12
    local = 768 * (25 + 1)
    full = 256 * 768 + 768
    print(f"  local windows, shared weights (as built): {shared:,}")
    print(f"  local windows, every unit its own weights: {local:,}")
    print(f"  fully connected, every pixel to every unit: {full:,}")
    print(f"  fully connected / shared = {full / shared:.0f} times as many")
    print()


# ---------------------------------------------------------------------------
# Example 3: a filter sliding along a sequence (one-dimensional convolution),
# on the two vectors Elman (1990) uses to show the problem with fixed windows.
A = [0, 1, 1, 1, 0, 0, 0, 0, 0]
B = [0, 0, 0, 1, 1, 1, 0, 0, 0]
RUN = [1, 1, 1]          # responds to a run of three ones
EDGE = [-1, 1]           # responds to a step up (0 then 1)


def slide(signal, filt):
    n = len(filt)
    return [sum(f * s for f, s in zip(filt, signal[i:i + n])) for i in range(len(signal) - n + 1)]


def example_conv():
    print("Example 3: one filter slid along Elman's two vectors")
    shared = sum(a * b for a, b in zip(A, B))
    dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(A, B)))
    cos = shared / (math.sqrt(sum(A)) * math.sqrt(sum(B)))
    print(f"  A = {A}")
    print(f"  B = {B}")
    print(f"  as raw vectors: {shared} position in common, distance {dist:.2f}, cosine {cos:.3f}")
    ra, rb = slide(A, RUN), slide(B, RUN)
    print(f"  filter {RUN} on A: {ra}  (peak {max(ra)} at window starting position {ra.index(max(ra)) + 1})")
    print(f"  filter {RUN} on B: {rb}  (peak {max(rb)} at window starting position {rb.index(max(rb)) + 1})")
    print(f"  B's output is A's output shifted by two places: {rb[2:] == ra[:-2]}")
    print(f"  edge filter {EDGE} on A: {slide(A, EDGE)}")
    print(f"  edge filter {EDGE} on B: {slide(B, EDGE)}")
    print(f"  parameters used, at any signal length: {len(RUN)} (run filter), {len(EDGE)} (edge filter)")
    print()


# ---------------------------------------------------------------------------
# Example 4: a recurrent network's weights do not grow with sentence length.
def example_rnn_size():
    print("Example 4: weights in a recurrent network (illustrative sizes, no biases)")
    n_in, n_hid, n_out = 31, 150, 31     # Elman's (1990) layer sizes
    rnn = n_in * n_hid + n_hid * n_hid + n_hid * n_out
    print(f"  input to hidden {n_in * n_hid:,} + hidden to hidden {n_hid * n_hid:,} "
          f"+ hidden to output {n_hid * n_out:,} = {rnn:,}, for any sentence length")
    print(f"  separate weights for each of 10 positions instead: {10 * rnn:,}")
    print()


# ---------------------------------------------------------------------------
# Example 5: a signal multiplied by the same factor at every step back in time.
def example_shrink():
    print("Example 5: one number multiplied by the same factor at every step")
    rows = [(0.5, 20), (0.25, 10), (0.25, 20), (0.9, 100), (1.0, 100), (1.5, 20)]
    for factor, steps in rows:
        v = factor ** steps
        shown = f"{v:,.0f}" if v >= 10 else f"{v:.3g}"
        print(f"  {factor} ** {steps} = {shown}")
    print("  step by step with factor 0.5 (for the figure): 1, then 1/2 ** k")
    print("   ", ", ".join(f"1/{2 ** k}" if k else "1" for k in range(0, 7)),
          f"(last = {0.5 ** 6:.3f})")
    print()


# ---------------------------------------------------------------------------
# Example 6: a memory cell holding a value, in the 1997 form
#   s(t) = s(t-1) + (input gate) * (new value)
# and, labelled separately, the later form with a forget gate f:
#   s(t) = f * s(t-1) + (input gate) * (new value)
def run_cell(steps, write_at=1, value=0.8, forget=1.0):
    s = 0.0
    for t in range(1, steps + 1):
        gate_in = 1.0 if t == write_at else 0.0
        s = forget * s + gate_in * value
    return s


def example_cell():
    print("Example 6: storing 0.8 at step 1 and reading at step 100")
    print(f"  1997 memory cell (self-connection 1.0): s(100) = {run_cell(100):.4f}")
    print(f"  effect of s(1) on s(100) through the self-connection: 1.0 ** 99 = {1.0 ** 99}")
    plain = 0.8 * 0.9 ** 99
    print(f"  ordinary unit that keeps 0.9 of its value each step: {plain:.6f} "
          f"(0.8 x 0.9 ** 99; effect of step 1 on step 100 = {0.9 ** 99:.2e})")
    print("  later form with a forget gate (constant here, for illustration):")
    for f in (1.0, 0.9, 0.0):
        print(f"    forget gate {f}: s(100) = {run_cell(100, forget=f):.6f}")
    print()


if __name__ == "__main__":
    example_lecun1989()
    example_sharing()
    example_conv()
    example_rnn_size()
    example_shrink()
    example_cell()
