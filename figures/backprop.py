#!/usr/bin/env python3
"""Figures for Book 1, chapter `backprop` [D-014].

Run: python3 figures/backprop.py
Writes backprop-bowl.svg, backprop-network.svg, and backprop-curve.svg next to
this script. All numbers come from code/checks/backprop.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "backprop_checks", OUT.parent / "code" / "checks" / "backprop.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
GRID = "#d0d0d0"
ACCENT = "#2f6fae"
BLAME = "#b5523b"
FILL = "#dbe7f3"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def quiet_axes(ax):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)


def bowl_figure():
    """Gradient descent on the regression bowl, one panel per learning rate."""
    rates = (0.02, 0.1, 0.25)
    titles = {0.02: "too small: slow", 0.1: "about right", 0.25: "too large: overshoots"}
    # The overshooting panel needs a wider view to show its zig-zag.
    view = {0.02: (-0.5, 4.5, 25), 0.1: (-0.5, 4.5, 25), 0.25: (-3.0, 8.5, 200)}
    steps = {0.02: 5, 0.1: 5, 0.25: 3}
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.4))
    for ax, rate in zip(axes, rates):
        lo, hi, top = view[rate]
        ws = [lo + (hi - lo) * i / 400 for i in range(401)]
        ax.plot(ws, [C.mse(w) for w in ws], color=GRID, linewidth=2, zorder=1)
        w, path = 0.0, [0.0]
        for _ in range(steps[rate]):
            w = w - rate * C.mse_slope(w)
            path.append(w)
        ax.plot(path, [C.mse(v) for v in path], "-o", color=ACCENT,
                linewidth=1.2, markersize=5, zorder=2)
        ax.set_title(f"learning rate {rate}\n{titles[rate]}", fontsize=8.5, color=INK)
        ax.set_xlim(lo, hi)
        ax.set_ylim(0, top)
        ax.set_xlabel("weight w", color=MUTED)
        quiet_axes(ax)
    axes[0].set_ylabel("mean squared error", color=MUTED)
    fig.tight_layout()
    save(fig, "backprop-bowl")


def network_figure():
    """The 2-2-1 network of Example 2, with forward values and backward blame."""
    p = C.START
    x, d = (1, 0), 1
    (h1, h2, y), (do, d1, d2), _ = C.backprop(p, x, d)
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    pos = {"x1": (0, 2.2), "x2": (0, 0.4), "h1": (2.6, 2.2), "h2": (2.6, 0.4), "y": (5.2, 1.3)}
    edges = [("x1", "h1", p["a11"]), ("x2", "h1", p["a12"]), ("x1", "h2", p["a21"]),
             ("x2", "h2", p["a22"]), ("h1", "y", p["c1"]), ("h2", "y", p["c2"])]
    r = 0.38
    for a, b, w in edges:
        (xa, ya), (xb, yb) = pos[a], pos[b]
        ax.add_patch(FancyArrowPatch((xa + r, ya), (xb - r, yb), arrowstyle="-|>",
                                     mutation_scale=9, color=MUTED, linewidth=0.9))
        # Place each weight label by hand: straight edges get a label at the
        # middle (top above, bottom below); crossing edges get one to the
        # left of the line, clear of both diagonals.
        place = {("x1", "h1"): (0.5, "above"), ("x2", "h2"): (0.5, "below"),
                 ("x1", "h2"): (0.3, "left"), ("x2", "h1"): (0.3, "left"),
                 ("h1", "y"): (0.5, "above"), ("h2", "y"): (0.5, "below")}
        t, side = place[(a, b)]
        lx, ly = xa + r + (xb - xa - 2 * r) * t, ya + (yb - ya) * t
        if side == "left":
            ax.text(lx - 0.3, ly, f"{w:+.1f}", ha="right", va="center", fontsize=7.5, color=INK)
        else:
            dy = 0.12 if side == "above" else -0.12
            ax.text(lx, ly + dy, f"{w:+.1f}", ha="center", va="bottom" if dy > 0 else "top",
                    fontsize=7.5, color=INK)
    values = {"x1": (f"{x[0]}", None), "x2": (f"{x[1]}", None),
              "h1": (f"{h1:.3f}", d1), "h2": (f"{h2:.3f}", d2), "y": (f"{y:.3f}", do)}
    for k, (val, blame) in values.items():
        cx, cy = pos[k]
        ax.add_patch(Circle((cx, cy), r, facecolor="white" if k[0] == "x" else FILL,
                            edgecolor=INK, linewidth=1))
        ax.text(cx, cy, val, ha="center", va="center", fontsize=8, color=INK)
        if blame is not None:
            ax.text(cx, cy - r - 0.12, f"blame {blame:+.4f}", ha="center", va="top",
                    fontsize=7.5, color=BLAME)
    ax.text(0, 2.2 + r + 0.15, "inputs", ha="center", va="bottom", color=MUTED, fontsize=7.5)
    ax.text(2.6, 2.2 + r + 0.15, "hidden units", ha="center", va="bottom", color=MUTED, fontsize=7.5)
    ax.text(5.2, 1.3 + r + 0.15, f"output\n(wanted {d})", ha="center", va="bottom",
            color=MUTED, fontsize=7.5)
    ax.annotate("", xy=(1.2, -0.75), xytext=(4.4, -0.75),
                arrowprops=dict(arrowstyle="-|>", color=BLAME, linewidth=1))
    ax.text(2.8, -0.65, "blame flows backward", ha="center", va="bottom", color=BLAME, fontsize=7.5)
    ax.annotate("", xy=(4.4, 3.15), xytext=(1.2, 3.15),
                arrowprops=dict(arrowstyle="-|>", color=INK, linewidth=1))
    ax.text(2.8, 3.25, "values flow forward", ha="center", va="bottom", color=INK, fontsize=7.5)
    ax.set_xlim(-0.8, 6.0)
    ax.set_ylim(-1.0, 3.7)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "backprop-network")


def curve_figure():
    """Total error while training on XOR (Example 3)."""
    import random
    rng = random.Random(C.SEED)
    p0 = C.random_start(rng)
    marks = tuple(range(0, C.EPOCHS + 1, 10))
    _, log = C.train(p0, C.RATE, C.EPOCHS, record=marks)
    log[0] = C.error(p0)
    xs = sorted(log)
    fig, ax = plt.subplots(figsize=(5.0, 2.4))
    ax.plot(xs, [log[m] for m in xs], color=ACCENT, linewidth=2)
    ax.set_xlabel("sweeps through the four XOR cases", color=MUTED)
    ax.set_ylabel("total error", color=MUTED)
    ax.set_xlim(0, 1500)
    ax.set_ylim(0, 0.55)
    quiet_axes(ax)
    ax.annotate("stalled near 0.5", xy=(150, 0.5), xytext=(480, 0.44), fontsize=7.5,
                color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8))
    save(fig, "backprop-curve")


if __name__ == "__main__":
    bowl_figure()
    network_figure()
    curve_figure()
