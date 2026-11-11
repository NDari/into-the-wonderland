#!/usr/bin/env python3
"""Figures for Book 1, chapter `adapting` [D-014].

Run: python3 figures/adapting.py
Writes adapting-lora.svg and adapting-memory.svg next to this script. Numbers
come from code/checks/adapting.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "adapting_checks", OUT.parent / "code" / "checks" / "adapting.py")
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
WARMFILL = "#f3dcd6"
GREY = "#e4e4e4"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def lora_figure():
    d, r = C.D_MODEL, 8
    full = d * d
    small = C.lora_count(d, d, r)
    fig, ax = plt.subplots(figsize=(7.0, 2.9))
    side, thin = 2.4, 0.22          # thin is drawn far wider than 8/4,096 of the side
    y0 = 0.3
    # W0, frozen
    ax.add_patch(Rectangle((0, y0), side, side, facecolor=GREY, edgecolor=MUTED, linewidth=0.8))
    ax.text(side / 2, y0 + side / 2 + 0.25, "$W_0$", ha="center", va="center", fontsize=13, color=INK)
    ax.text(side / 2, y0 + side / 2 - 0.2, "frozen", ha="center", va="center", fontsize=8, color=MUTED)
    ax.text(side / 2, y0 - 0.22, f"{d:,} x {d:,}\n{full:,} weights", ha="center", va="top", fontsize=7.5, color=INK)
    ax.text(side + 0.45, y0 + side / 2, "+", ha="center", va="center", fontsize=16, color=INK)
    # B, tall and thin
    bx = side + 0.9
    ax.add_patch(Rectangle((bx, y0), thin, side, facecolor=WARMFILL, edgecolor=WARM, linewidth=0.8))
    ax.text(bx + thin / 2, y0 + side + 0.12, "$B$", ha="center", va="bottom", fontsize=12, color=WARM)
    ax.text(bx + thin / 2, y0 - 0.22, f"{d:,} x {r}", ha="center", va="top", fontsize=7.5, color=INK)
    ax.text(bx + thin + 0.3, y0 + side - thin / 2, "x", ha="center", va="center", fontsize=11, color=INK)
    # A, short and wide, level with the top of B
    axx = bx + thin + 0.6
    ax.add_patch(Rectangle((axx, y0 + side - thin), side, thin, facecolor=WARMFILL, edgecolor=WARM, linewidth=0.8))
    ax.text(axx + side / 2, y0 + side + 0.12, "$A$", ha="center", va="bottom", fontsize=12, color=WARM)
    ax.text(axx + side / 2, y0 + side - thin - 0.1, f"{r} x {d:,}", ha="center", va="top", fontsize=7.5, color=INK)
    ax.text(axx + side / 2, y0 + side / 2 - 0.25,
            f"trainable: {r} x ({d:,} + {d:,})\n= {small:,} numbers\n({small / full:.2%} of $W_0$)",
            ha="center", va="center", fontsize=8, color=WARM)
    ax.text(axx + side / 2, y0 - 0.22, f"rank {r}; B starts at zero,\nso training starts from $W_0$ exactly",
            ha="center", va="top", fontsize=7.5, color=MUTED)
    ax.text(0, y0 + side + 0.6, "widths of B and A drawn much wider than to scale", fontsize=7, color=MUTED)
    ax.set_xlim(-0.2, axx + side + 0.2)
    ax.set_ylim(-0.75, y0 + side + 0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "adapting-lora")


def memory_figure():
    parts = C.memory_parts()
    colors = {"16-bit weights": ACCENT, "4-bit weights": "#7fa9d3", "gradients": LIGHT,
              "32-bit copy and Adam state": GREY, "adapters, with their gradients and state": WARM}
    fig, ax = plt.subplots(figsize=(7.0, 2.2))
    names = list(parts)
    seen = set()
    for row, name in enumerate(names):
        left = 0.0
        for label, gb in parts[name]:
            lab = None if label in seen else label
            seen.add(label)
            ax.barh(row, gb, left=left, height=0.55, color=colors[label], edgecolor="white", linewidth=1, label=lab)
            left += gb
        ax.text(left + 1.5, row, f"{left:.1f} GB", va="center", fontsize=8, color=INK)
    ax.axvline(48, color=MUTED, linewidth=0.8, linestyle="--")
    ax.text(48.8, -0.55, "48 GB, the single GPU of the QLoRA paper", fontsize=7, color=MUTED, va="center")
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=8, color=INK)
    ax.invert_yaxis()
    ax.set_xlim(0, 145)
    ax.set_ylim(len(names) - 0.4, -0.85)
    ax.set_xlabel("GB for an 8-billion-parameter model (weights and optimizer only; activations not counted)",
                  fontsize=7.5, color=MUTED)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)
    ax.legend(loc="lower right", fontsize=7, frameon=False)
    save(fig, "adapting-memory")


if __name__ == "__main__":
    lora_figure()
    memory_figure()
