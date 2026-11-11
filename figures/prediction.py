#!/usr/bin/env python3
"""Figures for Book 1, chapter `prediction` [D-014].

Run: python3 figures/prediction.py
Writes prediction-shannon-game.svg and prediction-sparse-counts.svg next to
this script. Data come from code/checks/prediction.py [D-009]: Shannon's
printed 1951 sequences, and bigram counts from Pride and Prejudice.
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "prediction_checks", OUT.parent / "code" / "checks" / "prediction.py")
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
MISS = "#f3dcd6"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def shannon_figure():
    """Shannon (1951), sequence (8): which letters the subject guessed first time."""
    fig, ax = plt.subplots(figsize=(6.8, 2.2))
    w, h = 0.135, 0.42
    y = 0.0
    for text, reduced in zip(C.GAME_TEXT, C.GAME_REDUCED):
        for i, (c, r) in enumerate(zip(text, reduced)):
            hit = r == "-"
            ax.add_patch(Rectangle((i * w, y), w * 0.92, h, facecolor=FILL if hit else MISS,
                                   edgecolor="none"))
            ax.text(i * w + w * 0.46, y + h / 2, c if c != " " else "·", ha="center", va="center",
                    fontsize=6.5, family="DejaVu Sans Mono", color=INK if not hit else MUTED,
                    fontweight="bold" if not hit else "normal")
        y -= 0.62
    ax.add_patch(Rectangle((0, y - 0.05), w, 0.3, facecolor=FILL, edgecolor="none"))
    ax.text(w * 1.4, y + 0.1, "guessed right first time", va="center", fontsize=7, color=MUTED)
    ax.add_patch(Rectangle((2.6, y - 0.05), w, 0.3, facecolor=MISS, edgecolor="none"))
    ax.text(2.6 + w * 1.4, y + 0.1, "missed (shown in bold); · is a space", va="center", fontsize=7, color=MUTED)
    ax.set_xlim(-0.05, 49 * w)
    ax.set_ylim(y - 0.2, 0.5)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "prediction-shannon-game")


def sparse_figure():
    """A 10 x 10 corner of the bigram table for mid-frequency words."""
    _, _, bi, _, mid, _ = C.austen_tables()
    n = len(mid)
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    for i, a in enumerate(mid):
        for j, b in enumerate(mid):
            c = bi[(a, b)]
            ax.add_patch(Rectangle((j, n - 1 - i), 0.95, 0.95, facecolor=ACCENT if c else "#f2f2f2",
                                   edgecolor="none"))
            ax.text(j + 0.475, n - 1 - i + 0.475, f"{c}", ha="center", va="center", fontsize=7.5,
                    color="white" if c else "#b0b0b0")
        ax.text(-0.15, n - 1 - i + 0.475, a, ha="right", va="center", fontsize=7.5, color=INK)
        ax.text(i + 0.475, n + 0.15, mid[i], ha="left", va="bottom", rotation=50, fontsize=7.5, color=INK)
    ax.text(-0.15, -0.6, "first word (rows), followed by second word (columns)", ha="left",
            va="top", fontsize=7.5, color=MUTED)
    ax.set_xlim(-2.2, n + 0.3)
    ax.set_ylim(-1.2, n + 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "prediction-sparse-counts")


if __name__ == "__main__":
    shannon_figure()
    sparse_figure()
