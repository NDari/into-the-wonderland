#!/usr/bin/env python3
"""Figures for Book 1, chapter `seq2seq` [D-014].

Run: python3 figures/seq2seq.py
Writes seq2seq-bottleneck.svg and seq2seq-attention-heatmap.svg next to this
script. Numbers come from code/checks/seq2seq.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "seq2seq_checks", OUT.parent / "code" / "checks" / "seq2seq.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
ACCENT = "#2f6fae"
FILL = "#dbe7f3"
WARM = "#b5523b"
WARMFILL = "#f3dcd6"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def box(ax, x, y, w, h, text, face=FILL, edge=ACCENT, size=8):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                facecolor=face, edgecolor=edge, linewidth=0.8))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=INK)


def arrow(ax, x0, y0, x1, y1, color=MUTED, lw=0.8, alpha=1.0):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=lw, alpha=alpha,
                                shrinkA=0, shrinkB=0, mutation_scale=7))


def bottleneck_figure():
    src = C.SOURCE
    tgt = ["la", "zone", "économique", "européenne"]
    _, weights, _ = C.attention_step(C.DECODER_STATES["zone"])
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.0))
    xs = [0.5, 1.6, 2.7, 3.8]
    for ax, title in zip(axes, ("(a) encoder-decoder", "(b) with attention")):
        ax.set_xlim(0, 4.55)
        ax.set_ylim(-0.35, 3.35)
        ax.axis("off")
        ax.text(0.05, 3.25, title, fontsize=8.5, color=INK, va="top")
        for x, w in zip(xs, src):
            ax.text(x, 0.0, w, ha="center", va="center", fontsize=7.5, color=INK)
            box(ax, x, 0.65, 0.62, 0.36, "", size=7)
            arrow(ax, x, 0.15, x, 0.47)
        for x, w in zip(xs, tgt):
            box(ax, x, 2.45, 0.62, 0.36, "", face=WARMFILL, edge=WARM)
            ax.text(x, 2.95, w, ha="center", va="center", fontsize=7, color=INK)
            arrow(ax, x, 2.63, x, 2.83, color=WARM)
        for x0, x1 in zip(xs[:-1], xs[1:]):
            arrow(ax, x0 + 0.31, 0.65, x1 - 0.31, 0.65, color=ACCENT)
            arrow(ax, x0 + 0.31, 2.45, x1 - 0.31, 2.45, color=WARM)
        ax.text(4.5, 0.65, "encoder", ha="right", va="center", fontsize=7, color=MUTED, rotation=90)
        ax.text(4.5, 2.45, "decoder", ha="right", va="center", fontsize=7, color=MUTED, rotation=90)
    # (a): everything passes through one vector.
    ax = axes[0]
    box(ax, 2.15, 1.55, 0.9, 0.36, "one vector", face="#ffffff", edge=INK, size=7.5)
    arrow(ax, xs[-1], 0.83, 2.5, 1.37, color=ACCENT)
    for x in xs:
        arrow(ax, 2.15, 1.73, x, 2.27, color=INK, lw=0.6, alpha=0.6)
    ax.text(2.15, -0.3, "a fixed size, however long the sentence", ha="center", fontsize=7, color=MUTED)
    # (b): writing "zone" looks back at every source vector, weighted.
    ax = axes[1]
    for x, w in zip(xs, weights):
        ax.plot([x, xs[1]], [0.83, 2.27], color=WARM, linewidth=0.4 + 4.0 * w, alpha=0.85, solid_capstyle="round")
        ax.text(x + (xs[1] - x) * 0.18 + 0.05, 1.08, f"{w:.2f}", fontsize=6.5, color=WARM, ha="left")
    ax.text(2.15, -0.3, "one vector per source word, kept", ha="center", fontsize=7, color=MUTED)
    fig.subplots_adjust(wspace=0.08)
    save(fig, "seq2seq-bottleneck")


def heatmap_figure():
    rows = C.heat_weights()
    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    ax.imshow(rows, cmap="Blues", vmin=0, vmax=1, aspect="equal")
    ax.set_xticks(range(len(C.HEAT_SOURCE)))
    ax.set_xticklabels(C.HEAT_SOURCE, rotation=60, ha="left", fontsize=7.5)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(C.HEAT_TARGET)))
    ax.set_yticklabels(C.HEAT_TARGET, fontsize=7.5)
    ax.tick_params(length=0, colors=INK)
    for side in ax.spines.values():
        side.set_visible(False)
    ax.set_xlabel("English source", color=MUTED)
    ax.set_ylabel("French translation, written top to bottom", color=MUTED)
    save(fig, "seq2seq-attention-heatmap")


if __name__ == "__main__":
    bottleneck_figure()
    heatmap_figure()
