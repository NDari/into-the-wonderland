#!/usr/bin/env python3
"""Figures for Book 1, chapter `generation` [D-014].

Run: python3 figures/generation.py
Writes generation-temperature.svg and generation-truncation.svg next to this
script. Numbers come from code/checks/generation.py [D-009], which reuses the
destination chapter's scores and random draw.
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "generation_checks", OUT.parent / "code" / "checks" / "generation.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
GRID = "#d0d0d0"
ACCENT = "#2f6fae"
LIGHT = "#c9dbee"
WARM = "#b5523b"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def quiet(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)
    ax.set_yticks([])


def temperature_figure():
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.6), sharey=True)
    for ax, t in zip(axes, C.TEMPS):
        p = C.softmax_t(C.SCORES, t)
        picked, _, _ = C.pick(p, C.D.DRAW)
        colors = [WARM if tok == picked else ACCENT for tok in C.TOKENS]
        ax.bar(range(len(p)), p, color=colors, width=0.7)
        for i, x in enumerate(p):
            ax.text(i, x + 0.02, f"{x:.2f}", ha="center", fontsize=7, color=INK)
        ax.set_xticks(range(len(p)))
        ax.set_xticklabels(C.TOKENS, rotation=0, fontsize=7)
        ax.set_title(f"temperature {t:g}", fontsize=8, color=INK)
        ax.text(2.5, 1.15, f"entropy {C.entropy_bits(p):.2f} bits\nthe 0.80 draw picks \"{picked}\"",
                ha="center", va="top", fontsize=7, color=MUTED)
        ax.set_ylim(0, 1.18)
        quiet(ax)
    fig.subplots_adjust(wspace=0.08)
    save(fig, "generation-temperature")


def truncation_figure():
    p = C.softmax_t(C.SCORES, 1.0)
    keep, z, new = C.truncate_top_p(p, 0.9)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.6, 2.5), sharey=True)
    ax1.bar(range(len(p)), p, color=[ACCENT if i in keep else LIGHT for i in range(len(p))], width=0.7)
    for i, x in enumerate(p):
        ax1.text(i, x + 0.02, f"{x:.3f}", ha="center", fontsize=7, color=INK)
    ax1.axvline(len(keep) - 0.5, color=WARM, linewidth=1, linestyle="--")
    ax1.text(len(keep) - 0.4, 0.6, f"top-p 0.9 and top-k 3\ncut here (kept {z:.3f})", fontsize=7, color=WARM)
    ax1.set_title("(a) temperature 1: before the cut", fontsize=8, color=INK, loc="left")
    ax2.bar(range(len(p)), [new.get(i, 0) for i in range(len(p))], color=ACCENT, width=0.7)
    for i in keep:
        ax2.text(i, new[i] + 0.02, f"{new[i]:.3f}", ha="center", fontsize=7, color=INK)
    ax2.set_title("(b) after: the kept three, rescaled to sum to 1", fontsize=8, color=INK, loc="left")
    for ax in (ax1, ax2):
        ax.set_xticks(range(len(p)))
        ax.set_xticklabels(C.TOKENS, fontsize=7)
        ax.set_ylim(0, 0.75)
        quiet(ax)
    fig.subplots_adjust(wspace=0.1)
    save(fig, "generation-truncation")


if __name__ == "__main__":
    temperature_figure()
    truncation_figure()
