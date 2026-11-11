#!/usr/bin/env python3
"""Figures for Book 1, chapter `depth` [D-014].

Run: python3 figures/depth.py
Writes depth-residual.svg, depth-norm.svg, and depth-init.svg next to this
script. Numbers come from code/checks/depth.py [D-009]. The residual figure
is the outline's key figure; `anatomy` can reuse residual_figure() with its
own block labels.
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "depth_checks", OUT.parent / "code" / "checks" / "depth.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
GRID = "#d0d0d0"
ACCENT = "#2f6fae"
FILL = "#dbe7f3"
WARM = "#b5523b"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def arrow(ax, a, b, color=INK, lw=1.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=9, color=color, linewidth=lw))


def residual_figure(name="depth-residual", labels=("block 1", "block 2", "block 3"),
                    values=None, corrections=None):
    """A running value passes along a line; each block reads it and adds a correction."""
    values = values or ["[1.00, 2.00]", "[1.10, 1.95]", "[1.08, 2.03]", "[1.11, 2.04]"]
    corrections = corrections or ["+[0.10, -0.05]", "+[-0.02, 0.08]", "+[0.03, 0.01]"]
    fig, ax = plt.subplots(figsize=(6.6, 2.4))
    y = 0.0
    xs_plus = [2.0, 4.6, 7.2]
    ax.plot([-0.6, 9.2], [y, y], color=ACCENT, linewidth=3, zorder=1)
    arrow(ax, (8.9, y), (9.4, y), color=ACCENT, lw=1.5)
    ax.text(-0.6, y - 0.35, values[0], ha="left", va="top", fontsize=7.5, color=INK)
    for k, (xp, lab, corr) in enumerate(zip(xs_plus, labels, corrections)):
        bx = xp - 1.0
        ax.add_patch(FancyBboxPatch((bx - 0.75, 0.8), 1.5, 0.75, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    facecolor=FILL, edgecolor=INK, linewidth=1, zorder=2))
        ax.text(bx, 1.33, lab, ha="center", va="center", fontsize=7.5, color=INK, zorder=3)
        ax.text(bx, 1.0, corr, ha="center", va="center", fontsize=7, color=MUTED, zorder=3)
        arrow(ax, (bx - 0.3, y + 0.05), (bx - 0.3, 0.78))
        arrow(ax, (bx + 0.77, 1.1), (xp, y + 0.2))
        ax.add_patch(Circle((xp, y), 0.18, facecolor="white", edgecolor=INK, linewidth=1, zorder=4))
        ax.text(xp, y, "+", ha="center", va="center", fontsize=9, color=INK, zorder=5)
        ax.text(xp + 0.25, y - 0.35, values[k + 1], ha="left", va="top", fontsize=7.5, color=INK)
    ax.text(4.3, -0.95, "the running value: what came in, plus the sum of all corrections so far",
            ha="center", va="top", fontsize=7.5, color=ACCENT)
    ax.set_xlim(-0.8, 9.6)
    ax.set_ylim(-1.3, 1.75)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, name)


def norm_figure():
    """Example 3's table, with what batch norm and layer norm each average over."""
    fig, ax = plt.subplots(figsize=(5.4, 2.6))
    T = C.TABLE
    for i, row in enumerate(T):
        for j, v in enumerate(row):
            ax.add_patch(Rectangle((j, 3 - i), 1, 1, facecolor="white", edgecolor=GRID, linewidth=1))
            ax.text(j + 0.5, 3 - i + 0.5, f"{v}", ha="center", va="center", fontsize=9, color=INK)
    for j in range(3):
        ax.text(j + 0.5, 4.15, f"unit {j + 1}", ha="center", va="bottom", fontsize=7.5, color=MUTED)
    for i in range(4):
        ax.text(-0.15, 3 - i + 0.5, f"example {i + 1}", ha="right", va="center", fontsize=7.5, color=MUTED)
    ax.add_patch(Rectangle((0.05, 0.05), 0.9, 3.9, fill=False, edgecolor=ACCENT, linewidth=2))
    ax.text(3.4, 2.6, "batch norm: one unit,\naveraged across the examples\nin the minibatch",
            ha="left", va="center", fontsize=7.5, color=ACCENT)
    ax.add_patch(Rectangle((0.05, 3.05), 2.9, 0.9, fill=False, edgecolor=WARM, linewidth=2, linestyle="--"))
    ax.text(3.4, 3.7, "layer norm: one example,\naveraged across its units",
            ha="left", va="center", fontsize=7.5, color=WARM)
    ax.set_xlim(-1.6, 6.2)
    ax.set_ylim(-0.1, 4.6)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "depth-norm")


def init_figure():
    """Example 1: signal variance after each of 10 layers under two starting rules."""
    old = C.layer_variances("old")
    glo = C.layer_variances("glorot")
    layers = list(range(1, 11))
    fig, ax = plt.subplots(figsize=(5.0, 2.3))
    ax.plot(layers, glo, "-o", color=ACCENT, linewidth=1.6, markersize=3.5)
    ax.plot(layers, old, "-o", color=WARM, linewidth=1.6, markersize=3.5)
    ax.set_yscale("log")
    ax.set_xticks(layers)
    ax.set_xlabel("layer", color=MUTED)
    ax.set_ylabel("variance of the signal", color=MUTED)
    ax.text(10, glo[-1] * 1.6, "scaled by layer size (Glorot)", ha="right", va="bottom", fontsize=7.5, color=INK)
    ax.text(5.3, old[4], "uniform in plus or minus 1/sqrt(n)", ha="left", va="center", fontsize=7.5, color=INK)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)
    save(fig, "depth-init")


if __name__ == "__main__":
    residual_figure()
    norm_figure()
    init_figure()
