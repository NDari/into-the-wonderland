#!/usr/bin/env python3
"""Figures for Book 1, chapter `pretraining` [D-014].

Run: python3 figures/pretraining.py
Writes pretraining-objectives.svg next to this script. The sentence and the
masked words come from code/checks/pretraining.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "pretraining_checks", OUT.parent / "code" / "checks" / "pretraining.py")
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
GREY = "#eeeeee"

W, GAP = 1.0, 0.12


def token(ax, x, y, text, face=FILL, edge=ACCENT, color=INK):
    ax.add_patch(FancyBboxPatch((x - W / 2, y - 0.22), W, 0.44, boxstyle="round,pad=0,rounding_size=0.06",
                                facecolor=face, edgecolor=edge, linewidth=0.7))
    ax.text(x, y, text, ha="center", va="center", fontsize=7.5, color=color)


def xs(n):
    return [i * (W + GAP) for i in range(n)]


def objectives_figure():
    words = C.SENTENCE
    n = len(words)
    pos = xs(n)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.4, 3.9))
    # (a) next-token prediction: inputs below, targets above, shifted by one.
    for i, w in enumerate(words[:-1]):
        token(ax1, pos[i], 0, w)
    for i, w in enumerate(words[1:]):
        token(ax1, pos[i], 1.0, w, face=WARMFILL, edge=WARM)
        ax1.annotate("", xy=(pos[i], 0.76), xytext=(pos[i], 0.24),
                     arrowprops=dict(arrowstyle="-|>", color=MUTED, linewidth=0.7, mutation_scale=6))
    # One sample target ("sofa"), with faint lines from every word it may use.
    k = words.index("sofa") - 1
    for i in range(k):
        ax1.annotate("", xy=(pos[k] - 0.12, 0.8), xytext=(pos[i], 0.22),
                     arrowprops=dict(arrowstyle="-", color=ACCENT, linewidth=0.4, alpha=0.35,
                                     connectionstyle="arc3,rad=-0.15"))
    ax1.text(-0.65, 0, "input", ha="right", va="center", fontsize=7.5, color=MUTED)
    ax1.text(-0.65, 1.0, "predict", ha="right", va="center", fontsize=7.5, color=WARM)
    ax1.text(-0.65, 1.55, f"(a) next-token prediction: {n - 1} predictions, each using only the words to its left",
             ha="left", va="center", fontsize=8, color=INK)
    ax1.set_xlim(-1.6, pos[-1] + 0.7)
    ax1.set_ylim(-0.45, 1.8)
    ax1.axis("off")
    # (b) masked prediction: some words hidden, predicted from both sides.
    masked_idx = [i for i, w in enumerate(words) if w in C.MASKED]
    for i, w in enumerate(words):
        if i in masked_idx:
            token(ax2, pos[i], 0, "[MASK]", face=GREY, edge="#999999", color=MUTED)
        else:
            token(ax2, pos[i], 0, w)
    for m in masked_idx:
        token(ax2, pos[m], 1.0, words[m], face=WARMFILL, edge=WARM)
        ax2.annotate("", xy=(pos[m], 0.76), xytext=(pos[m], 0.24),
                     arrowprops=dict(arrowstyle="-|>", color=MUTED, linewidth=0.7, mutation_scale=6))
        for i in range(n):
            if i in masked_idx:
                continue
            ax2.annotate("", xy=(pos[m] + (0.12 if i > m else -0.12), 0.8), xytext=(pos[i], 0.22),
                         arrowprops=dict(arrowstyle="-", color=ACCENT, linewidth=0.4, alpha=0.35,
                                         connectionstyle="arc3,rad=-0.15" if i < m else "arc3,rad=0.15"))
    ax2.text(-0.65, 0, "input", ha="right", va="center", fontsize=7.5, color=MUTED)
    ax2.text(-0.65, 1.0, "predict", ha="right", va="center", fontsize=7.5, color=WARM)
    ax2.text(-0.65, 1.55, f"(b) masked prediction: {len(masked_idx)} predictions, each using the words on both sides",
             ha="left", va="center", fontsize=8, color=INK)
    ax2.set_xlim(-1.6, pos[-1] + 0.7)
    ax2.set_ylim(-0.45, 1.8)
    ax2.axis("off")
    fig.subplots_adjust(hspace=0.15)
    save(fig, "pretraining-objectives")


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


if __name__ == "__main__":
    objectives_figure()
