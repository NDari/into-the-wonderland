#!/usr/bin/env python3
"""Figures for Book 1, chapter `anatomy` [D-014].

Run: python3 figures/anatomy.py
Writes anatomy-architecture.svg and anatomy-masks.svg next to this script.
Sizes are GPT-2 small's, as in code/checks/anatomy.py [D-009].
"""
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

OUT = Path(__file__).parent
plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
ACCENT = "#2f6fae"
FILL = "#dbe7f3"
PLAIN = "#f4f4f4"
WARM = "#b5523b"
WARMFILL = "#f3dcd6"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def box(ax, x, y, w, h, text, face=FILL, edge=ACCENT, size=7.5):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=face, edgecolor=edge, linewidth=0.8))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=INK)


def arrow(ax, x0, y0, x1, y1, color=MUTED, lw=0.9):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=lw, shrinkA=0, shrinkB=0,
                                mutation_scale=7))


def plus(ax, x, y):
    ax.add_patch(plt.Circle((x, y), 0.13, facecolor="white", edgecolor=ACCENT, linewidth=1.0, zorder=4))
    ax.text(x, y, "+", ha="center", va="center", fontsize=9, color=ACCENT, zorder=5)


def architecture_figure():
    fig, ax = plt.subplots(figsize=(6.4, 7.6))
    sx = 1.6          # x of the residual stream
    bx = 4.3          # x of the sub-layer boxes
    # Bottom: token IDs and the two tables.
    box(ax, sx, 0.0, 3.4, 0.45, "token IDs, e.g. 3797 (\" cat\") at position 2", face=PLAIN, edge="#999999")
    box(ax, 0.9, 1.0, 1.9, 0.55, "token table\n50,257 x 768")
    box(ax, 3.1, 1.0, 1.9, 0.55, "position table\n1,024 x 768")
    arrow(ax, 1.2, 0.23, 1.0, 0.72)
    arrow(ax, 2.0, 0.23, 2.9, 0.72)
    plus(ax, sx, 1.75)
    arrow(ax, 0.9, 1.28, sx - 0.1, 1.66)
    arrow(ax, 3.1, 1.28, sx + 0.1, 1.66)
    # The residual stream: a thick line up through the block.
    y0, y1 = 1.88, 6.2
    ax.plot([sx, sx], [y0, y1], color=ACCENT, linewidth=5, alpha=0.35, solid_capstyle="butt", zorder=1)
    ax.text(sx - 0.3, 3.0, "residual stream:\n768 numbers\nper position", ha="right", va="center", fontsize=7.5,
            color=ACCENT)
    def sublayer(base, text):
        # branch off the stream at `base`, normalize, compute, add back above.
        ax.plot([sx, bx], [base, base], color=MUTED, linewidth=0.9)
        box(ax, bx, base + 0.4, 1.6, 0.4, "layer norm", face=PLAIN, edge="#999999")
        arrow(ax, bx, base, bx, base + 0.2)
        box(ax, bx, base + 1.15, 2.6, 0.6, text)
        arrow(ax, bx, base + 0.6, bx, base + 0.85)
        top = base + 1.7
        ax.plot([bx, bx], [base + 1.45, top], color=MUTED, linewidth=0.9)
        arrow(ax, bx, top, sx + 0.13, top)
        plus(ax, sx, top)

    sublayer(2.1, "masked multi-head attention\n12 heads of 64\n(mixes in earlier positions)")
    sublayer(4.1, "feed-forward network\n768 \u2192 3,072 \u2192 768\n(each position on its own)")
    # Bracket for the block.
    ax.add_patch(Rectangle((0.15, 1.95), 5.85, 4.05, fill=False, edgecolor="#bbbbbb", linewidth=0.8,
                           linestyle="--"))
    ax.text(5.95, 1.9, "one block, repeated 12 times", ha="right", va="top", fontsize=7.5, color=MUTED)
    # Top: final norm, output layer, softmax.
    box(ax, sx, 6.55, 1.9, 0.4, "final layer norm", face=PLAIN, edge="#999999")
    arrow(ax, sx, 6.1, sx, 6.35)
    box(ax, sx, 7.35, 2.9, 0.6, "output layer: dot product with\nevery row of the token table")
    arrow(ax, sx, 6.75, sx, 7.05)
    box(ax, sx, 8.2, 2.6, 0.45, "50,257 logits → softmax\n(the destination chapter)", face=WARMFILL, edge=WARM)
    arrow(ax, sx, 7.65, sx, 7.97)
    ax.annotate("", xy=(0.35, 1.0), xytext=(0.2, 7.35),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, linewidth=0.8, linestyle=(0, (3, 2)),
                                connectionstyle="arc3,rad=0.25", mutation_scale=7))
    ax.text(-0.75, 4.2, "same table\n(tied)", ha="center", va="center", fontsize=7, color=MUTED, rotation=90)
    ax.set_xlim(-1.1, 6.1)
    ax.set_ylim(-0.4, 8.6)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "anatomy-architecture")


def masks_figure():
    words = ["The", "cat", "sat", "on", "the"]
    n = len(words)
    fig, axes = plt.subplots(1, 2, figsize=(5.6, 2.8))
    for ax, causal, title in ((axes[0], False, "fully visible\n(encoder-only, e.g. BERT)"),
                              (axes[1], True, "causal\n(decoder-only, e.g. GPT)")):
        for i in range(n):
            for j in range(n):
                ok = (j <= i) or not causal
                ax.add_patch(Rectangle((j, n - 1 - i), 0.92, 0.92, facecolor=ACCENT if ok else "#eeeeee",
                                       edgecolor="none"))
        for k, w in enumerate(words):
            ax.text(-0.15, n - 1 - k + 0.46, w, ha="right", va="center", fontsize=7.5, color=INK)
            ax.text(k + 0.46, n + 0.1, w, ha="center", va="bottom", fontsize=7.5, color=INK)
        ax.text(n / 2, -0.35, title, ha="center", va="top", fontsize=7.5, color=MUTED)
        ax.set_xlim(-1.4, n + 0.1)
        ax.set_ylim(-1.3, n + 0.6)
        ax.set_aspect("equal")
        ax.axis("off")
    save(fig, "anatomy-masks")


if __name__ == "__main__":
    architecture_figure()
    masks_figure()
