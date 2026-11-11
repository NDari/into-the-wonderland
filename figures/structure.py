#!/usr/bin/env python3
"""Figures for Book 1, chapter `structure` [D-014].

Run: python3 figures/structure.py
Writes structure-conv1d.svg, structure-unrolled.svg, and structure-cell.svg
next to this script. All numbers come from code/checks/structure.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "structure_checks", OUT.parent / "code" / "checks" / "structure.py")
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


def arrow(ax, a, b, color=INK, lw=1.0, style="-|>"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=9, color=color, linewidth=lw))


def conv_figure():
    """Example 3: the same three-weight filter slid along Elman's vectors."""
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    rows = [("A", C.A, C.slide(C.A, C.RUN), 3.0), ("B", C.B, C.slide(C.B, C.RUN), 0.6)]
    for name, sig, out, y in rows:
        ax.text(-0.6, y + 0.4, f"input {name}", ha="right", va="center", color=MUTED)
        for i, v in enumerate(sig):
            ax.add_patch(Rectangle((i, y), 0.9, 0.8, facecolor=INK if v else "white",
                                   edgecolor=INK, linewidth=0.8))
        ax.text(-0.6, y - 0.55, "filter output", ha="right", va="center", color=MUTED)
        peak = max(out)
        for i, v in enumerate(out):
            # Each output sits under the middle of its three-cell window.
            cx = i + 1 + 0.45
            ax.text(cx, y - 0.55, f"{v}", ha="center", va="center", fontsize=9,
                    color=ACCENT if v == peak else INK, fontweight="bold" if v == peak else "normal")
        # Bracket over the window that gives the peak.
        start = out.index(peak)
        ax.add_patch(Rectangle((start - 0.05, y - 0.05), 2.9, 0.9, fill=False,
                               edgecolor=ACCENT, linewidth=1.6))
    ax.text(4.5, 4.15, "filter: weights 1, 1, 1 (the same three numbers at every position)",
            ha="center", va="bottom", color=ACCENT, fontsize=8)
    ax.set_xlim(-3.2, 9.3)
    ax.set_ylim(-0.3, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "structure-conv1d")


def unrolled_figure():
    """A recurrent network unrolled over a sentence, with the shrinking signal."""
    words = ["In", "2009", ",", "I", "went", "to", "Nepal"]
    n = len(words)
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    dx = 1.3
    for i, w in enumerate(words):
        x = i * dx
        ax.text(x, 0.0, w, ha="center", va="center", color=INK)
        arrow(ax, (x, 0.2), (x, 0.75), color=MUTED)
        ax.text(x + 0.08, 0.47, "U", ha="left", va="center", fontsize=7, color=MUTED)
        ax.add_patch(FancyBboxPatch((x - 0.35, 0.8), 0.7, 0.55, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    facecolor=FILL, edgecolor=INK, linewidth=1))
        ax.text(x, 1.075, f"h{i + 1}", ha="center", va="center", color=INK)
        if i < n - 1:
            arrow(ax, (x + 0.37, 1.075), (x + dx - 0.37, 1.075))
            ax.text(x + dx / 2, 1.16, "W", ha="center", va="bottom", fontsize=7.5, color=INK)
    # Backward signal: an error at the last step, scaled by 0.5 per step back.
    base = 1.75
    ax.text(-0.6, base + 0.75, "share of an error at the last word\nthat reaches each step (factor 0.5 per step)",
            ha="left", va="bottom", fontsize=7.5, color=WARM)
    for i in range(n):
        k = n - 1 - i
        h = 0.6 * (0.5 ** k)
        x = i * dx
        ax.add_patch(Rectangle((x - 0.25, base), 0.5, h, facecolor=WARM, edgecolor="none"))
        ax.text(x, base + h + 0.04, f"1/{2 ** k}" if k else "1", ha="center", va="bottom", fontsize=7, color=INK)
    ax.text((n - 1) * dx / 2, -0.45, "the same weights U and W are used at every step",
            ha="center", va="center", fontsize=7.5, color=MUTED)
    ax.set_xlim(-0.8, (n - 1) * dx + 0.6)
    ax.set_ylim(-0.7, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "structure-unrolled")


def cell_figure():
    """Example 6: a stored value over 100 steps, memory cell versus ordinary unit."""
    steps = list(range(1, 101))
    cell = [C.run_cell(t) for t in steps]
    plain = [C.run_cell(t, forget=0.9) for t in steps]
    fig, ax = plt.subplots(figsize=(5.0, 2.3))
    ax.plot(steps, cell, color=ACCENT, linewidth=2)
    ax.plot(steps, plain, color=WARM, linewidth=2)
    ax.text(100, cell[-1] + 0.04, "memory cell (keeps 1.0 of its value)", ha="right",
            va="bottom", fontsize=7.5, color=INK)
    ax.text(22, 0.18, "ordinary unit (keeps 0.9 each step)", ha="left", va="bottom",
            fontsize=7.5, color=INK)
    ax.set_xlabel("step", color=MUTED)
    ax.set_ylabel("stored value", color=MUTED)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)
    save(fig, "structure-cell")


if __name__ == "__main__":
    conv_figure()
    unrolled_figure()
    cell_figure()
