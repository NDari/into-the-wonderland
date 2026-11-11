#!/usr/bin/env python3
"""Figures for Book 1, chapter `neuron` [D-014].

Run: python3 figures/neuron.py
Writes neuron-vote.svg and neuron-xor.svg next to this script. Weights and
points come from code/checks/neuron.py [D-009], so the figures and the
worked examples cannot disagree.
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent

_spec = importlib.util.spec_from_file_location(
    "neuron_checks", OUT.parent / "code" / "checks" / "neuron.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
GRID = "#d0d0d0"
ACCENT = "#2f6fae"      # decision boundary lines
FILL = "#dbe7f3"        # same light blue as the pipeline figure


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def vote_figure():
    """One neuron as a weighted vote, with the numbers of Example 1."""
    fig, ax = plt.subplots(figsize=(6.4, 2.8))
    xs = C.VOTE_INPUTS
    ws = C.VOTE_WEIGHTS
    z = C.weighted_sum(ws, C.VOTE_BIAS, xs)
    ys = [2.2, 1.2, 0.2]
    sum_xy = (3.6, 1.2)
    for i, (x, w, y) in enumerate(zip(xs, ws, ys), 1):
        ax.add_patch(Circle((0.6, y), 0.32, facecolor="white", edgecolor=INK, linewidth=1))
        ax.text(0.6, y, f"{x}", ha="center", va="center", fontsize=10, color=INK)
        ax.text(0.0, y, f"input {i}", ha="right", va="center", color=MUTED, fontsize=7.5)
        start, end = (0.95, y), (sum_xy[0] - 0.5, sum_xy[1] + (y - 1.2) * 0.25)
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=10,
                                     color=INK, linewidth=1))
        # Label sits beside the arrow near its start: above for the upper two,
        # below for the lowest, so no label crosses a line.
        lx = 2.2
        ly = start[1] + (end[1] - start[1]) * (lx - start[0]) / (end[0] - start[0])
        below = i == len(xs)
        ax.text(lx, ly - 0.16 if below else ly + 0.16, f"weight {w:+.1f}",
                ha="center", va="top" if below else "bottom", fontsize=7.5, color=INK)
    # Sum node.
    ax.add_patch(Circle(sum_xy, 0.5, facecolor=FILL, edgecolor=INK, linewidth=1))
    ax.text(*sum_xy, "sum", ha="center", va="center", fontweight="bold", color=INK)
    ax.text(sum_xy[0], sum_xy[1] - 0.72, f"bias {C.VOTE_BIAS:+.1f}", ha="center",
            va="top", fontsize=7.5, color=INK)
    # Threshold box.
    bx, by = 4.8, 0.85
    ax.add_patch(FancyArrowPatch((sum_xy[0] + 0.5, sum_xy[1]), (bx, sum_xy[1]),
                                 arrowstyle="-|>", mutation_scale=10, color=INK, linewidth=1))
    ax.text((sum_xy[0] + 0.5 + bx) / 2, sum_xy[1] + 0.08, f"{z:+.1f}", ha="center",
            va="bottom", fontsize=7.5, color=INK)
    ax.add_patch(FancyBboxPatch((bx, by), 1.2, 0.7, boxstyle="round,pad=0.02,rounding_size=0.06",
                                facecolor="white", edgecolor=INK, linewidth=1))
    ax.text(bx + 0.6, by + 0.35, "above 0?", ha="center", va="center", color=INK)
    # Output.
    ox = 6.6
    ax.add_patch(FancyArrowPatch((bx + 1.2, sum_xy[1]), (ox - 0.32, sum_xy[1]),
                                 arrowstyle="-|>", mutation_scale=10, color=INK, linewidth=1))
    ax.add_patch(Circle((ox, sum_xy[1]), 0.32, facecolor="white", edgecolor=INK, linewidth=1))
    ax.text(ox, sum_xy[1], f"{C.step(z)}", ha="center", va="center", fontsize=10, color=INK)
    ax.text(ox, sum_xy[1] - 0.45, "output", ha="center", va="top", color=MUTED, fontsize=7.5)
    ax.set_xlim(-0.9, 7.1)
    ax.set_ylim(-0.4, 2.7)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "neuron-vote")


def boundary_panel(ax, name, line):
    """Plot the four input points; filled = wanted output 1, hollow = 0."""
    for (x1, x2), t in zip(C.POINTS, C.TARGETS[name]):
        ax.plot(x1, x2, "o", markersize=11, markeredgewidth=1.5, markeredgecolor=INK,
                markerfacecolor=INK if t else "white", zorder=3)
    if line:
        (w1, w2), b = line
        # Boundary: w1*x1 + w2*x2 + b = 0, so x2 = -(w1*x1 + b) / w2.
        xs = [-0.5, 1.5]
        ax.plot(xs, [-(w1 * x + b) / w2 for x in xs], color=ACCENT, linewidth=2, zorder=2)
        ax.set_title(f"{name}: one line separates", fontsize=8.5, color=INK)
    else:
        ax.set_title(f"{name}: no single line can", fontsize=8.5, color=INK)
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xlabel("input 1", color=MUTED)
    ax.set_ylabel("input 2", color=MUTED)
    ax.set_aspect("equal")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)


def xor_figure():
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.5))
    boundary_panel(axes[0], "AND", C.GATES["AND"])
    boundary_panel(axes[1], "OR", C.GATES["OR"])
    boundary_panel(axes[2], "XOR", None)
    fig.text(0.5, -0.04, "filled: output 1        hollow: output 0", ha="center",
             color=MUTED, fontsize=7.5)
    fig.tight_layout()
    save(fig, "neuron-xor")


if __name__ == "__main__":
    vote_figure()
    xor_figure()
