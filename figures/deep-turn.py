#!/usr/bin/env python3
"""Figures for Book 1, chapter `deep-turn` [D-014].

Run: python3 figures/deep-turn.py
Writes deep-turn-ilsvrc.svg and deep-turn-pipeline.svg next to this script.
Numbers come from code/checks/deep-turn.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "deep_turn_checks", OUT.parent / "code" / "checks" / "deep-turn.py")
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
OLD = "#9a9a9a"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def ilsvrc_figure():
    years = [y for y, _, _ in C.ILSVRC]
    errs = [e for _, _, e in C.ILSVRC]
    fig, ax = plt.subplots(figsize=(5.6, 2.8))
    colors = [OLD if y < 2012 else ACCENT for y in years]
    bars = ax.bar([str(y) for y in years], errs, color=colors, width=0.6)
    for b, e in zip(bars, errs):
        ax.text(b.get_x() + b.get_width() / 2, e + 0.6, f"{e:g}%", ha="center",
                va="bottom", fontsize=8, color=INK,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.6))
    ax.axhline(C.HUMAN_ONE_ANNOTATOR, color=MUTED, linewidth=1, linestyle="--", zorder=0)
    ax.text(5.45, C.HUMAN_ONE_ANNOTATOR, "one trained\nhuman\nannotator:\n5.1%",
            ha="left", va="center", fontsize=7, color=MUTED,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.6))
    ax.set_xlim(-0.5, 6.3)
    ax.text(0.5, 31.5, "hand-built features\n+ SVM", ha="center", va="bottom", fontsize=7.5, color=MUTED)
    ax.text(2, 19.2, "first deep-\nnetwork\nwinner", ha="center", va="bottom", fontsize=7.5, color=ACCENT)
    ax.set_ylabel("top-5 error of the winner", color=MUTED)
    ax.set_ylim(0, 37)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)
    save(fig, "deep-turn-ilsvrc")


def box(ax, x, y, w, h, text, learned):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=FILL if learned else "white", edgecolor=INK, linewidth=1))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=7.5, color=INK)


def arrow(ax, a, b):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=9, color=INK, linewidth=1))


def pipeline_figure():
    fig, ax = plt.subplots(figsize=(6.6, 2.6))
    h, w, gap = 0.8, 1.7, 0.35
    rows = [
        (2.0, "the 2000s", [("pixels", False), ("hand-made\nfeatures", False),
                            ("classifier\n(e.g. SVM)", True), ("label", False)]),
        (0.4, "deep learning", [("pixels", False), ("layer\n(edges)", True), ("layer\n(motifs)", True),
                                ("layer\n(parts)", True), ("label", False)]),
    ]
    for y, title, items in rows:
        ax.text(-0.15, y + h / 2, title, ha="right", va="center", fontsize=8, color=MUTED)
        for i, (text, learned) in enumerate(items):
            x = i * (w + gap)
            box(ax, x, y, w, h, text, learned)
            if i:
                arrow(ax, (x - gap, y + h / 2), (x, y + h / 2))
    ax.add_patch(FancyBboxPatch((4.2, 3.05), 0.28, 0.2, boxstyle="square,pad=0",
                                facecolor=FILL, edgecolor=INK, linewidth=0.8))
    ax.text(4.55, 3.15, "learned from data", va="center", fontsize=7.5, color=INK)
    ax.set_xlim(-1.9, 5 * (w + gap))
    ax.set_ylim(0.2, 3.4)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "deep-turn-pipeline")


if __name__ == "__main__":
    ilsvrc_figure()
    pipeline_figure()
