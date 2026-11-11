#!/usr/bin/env python3
"""Figures for Book 1, chapter `training` [D-014].

Run: python3 figures/training.py
Writes training-loss.svg and training-step.svg next to this script. The loss
curve is BLOOM-176B's public training log, read and hash-checked by
code/checks/training.py [D-009, D-018].
"""
import importlib.util
import math
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "training_checks", OUT.parent / "code" / "checks" / "training.py")
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
WARMFILL = "#f3dcd6"
PLAIN = "#f4f4f4"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def quiet(ax):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)


def loss_figure():
    its, tokens, lr, batch, loss, rows, _ = C.bloom_series()
    bt = [t / 1e9 for t in tokens]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.4, 3.2), gridspec_kw={"width_ratios": [1.5, 1]})
    # (a) the whole run; every 5th point keeps the SVG small without hiding the spike.
    keep = [j for j in range(len(its)) if j % 5 == 0 or loss[j] > 3.0]
    ax1.plot([bt[j] for j in keep], [loss[j] for j in keep], color=ACCENT, linewidth=0.5)
    ax1.set_ylim(1.5, 6.0)
    ax1.set_xlim(0, 375)
    ax1.set_xlabel("training tokens (billions)", color=MUTED)
    ax1.set_ylabel("training loss (nats per token)", color=MUTED)
    ax1.set_title("(a) the whole run, March to July 2022", fontsize=8, color=INK, loc="left")
    s = max(range(len(its)), key=lambda j: loss[j] if tokens[j] > 1e10 else 0)
    ax1.annotate(f"one large spike: {loss[s]:.2f}", (bt[s], loss[s]), xytext=(18, -6), textcoords="offset points",
                 fontsize=7, color=WARM, arrowprops=dict(arrowstyle="-", color=WARM, linewidth=0.6))
    full = next(j for j in range(len(its)) if batch[j] == 2048)
    ax1.annotate("full batch reached", (bt[full], loss[full]), xytext=(10, 28), textcoords="offset points",
                 fontsize=7, color=MUTED, arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.6))
    ax1.axvline(341, color=GRID, linewidth=0.8, linestyle=":")
    ax1.text(338, 5.6, "first pass over\nthe data ends", fontsize=7, color=MUTED, ha="right")
    ax1.annotate(f"end: {loss[-1]:.2f}", (bt[-1], loss[-1]), xytext=(-40, 22), textcoords="offset points",
                 fontsize=7, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.6))
    quiet(ax1)
    # (b) the first 2 billion tokens, log scale, with the learning rate.
    early = [j for j in range(len(its)) if tokens[j] <= 2e9]
    ax2.plot([bt[j] for j in early], [loss[j] for j in early], color=ACCENT, linewidth=0.8)
    ax2.axhline(math.log(C.BLOOM_VOCAB), color=GRID, linewidth=0.8, linestyle="--")
    ax2.text(1.95, math.log(C.BLOOM_VOCAB) * 1.07, "uniform guessing", fontsize=7, color=MUTED, ha="right")
    ax2.set_yscale("log")
    ax2.set_yticks([2, 4, 8, 16, 32, 64])
    ax2.set_yticklabels(["2", "4", "8", "16", "32", "64"])
    ax2.minorticks_off()
    ax2.set_xlabel("training tokens (billions)", color=MUTED)
    ax2.set_title("(b) the first 2 billion tokens", fontsize=8, color=INK, loc="left")
    quiet(ax2)
    ax3 = ax2.twinx()
    ax3.plot([bt[j] for j in early], [lr[j] * 1e5 for j in early], color=WARM, linewidth=0.9)
    ax3.set_ylim(0, 12)
    ax3.set_yticks([0, 2, 4, 6])
    ax3.set_yticklabels(["0", "2", "4", "6"])
    ax3.tick_params(colors=WARM, length=0, labelsize=7)
    ax3.set_ylabel("learning rate (x 10⁻⁵)", color=WARM, fontsize=7.5)
    for side in ("top", "left", "bottom"):
        ax3.spines[side].set_visible(False)
    ax3.spines["right"].set_color(GRID)
    fig.subplots_adjust(wspace=0.32)
    save(fig, "training-loss")


def box(ax, x, y, w, h, text, face=FILL, edge=ACCENT, size=7.3):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=face, edgecolor=edge, linewidth=0.8))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=INK)


def arrow(ax, x0, y0, x1, y1, color=MUTED):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=0.9, shrinkA=0, shrinkB=0, mutation_scale=7))


def step_figure():
    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    w, h = 1.85, 0.95
    top = [
        (1.0, "corpus\npacked into windows,\ndocuments separated by\nan end-of-text token", PLAIN, "#999999"),
        (3.2, "a batch of windows\n2,048 x 2,048 tokens\n(BLOOM)", PLAIN, "#999999"),
        (5.4, "forward pass:\na probability for\nthe next token at\nevery position", FILL, ACCENT),
        (7.6, "loss: cross-entropy\nat every position,\naveraged to\none number", WARMFILL, WARM),
    ]
    bottom = [
        (7.6, "backward pass:\na gradient for\nevery parameter", FILL, ACCENT),
        (5.4, "gradients averaged\nacross GPUs that\neach took part of\nthe batch", PLAIN, "#999999"),
        (3.2, "the optimizer\n(for example Adam)\nupdates every\nparameter", FILL, ACCENT),
        (1.0, "every so often:\nsave a checkpoint", PLAIN, "#999999"),
    ]
    for x, t, f, e in top:
        box(ax, x, 2.0, w, h + 0.25, t, f, e)
    for x, t, f, e in bottom:
        box(ax, x, 0.35, w, h + 0.25, t, f, e)
    for (x0, *_), (x1, *_) in zip(top, top[1:]):
        arrow(ax, x0 + w / 2, 2.0, x1 - w / 2, 2.0)
    arrow(ax, 7.6, 2.0 - (h + 0.25) / 2, 7.6, 0.35 + (h + 0.25) / 2)
    for (x0, *_), (x1, *_) in zip(bottom, bottom[1:]):
        arrow(ax, x0 - w / 2, 0.35, x1 + w / 2, 0.35)
    ax.annotate("", xy=(3.2, 2.0 - (h + 0.25) / 2), xytext=(3.2, 0.35 + (h + 0.25) / 2),
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, linewidth=0.9, linestyle=(0, (3, 2)), mutation_scale=7))
    ax.text(3.32, 1.17, "next step, next batch", fontsize=7, color=ACCENT, va="center")
    ax.set_xlim(-0.05, 8.65)
    ax.set_ylim(-0.4, 2.75)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "training-step")


if __name__ == "__main__":
    loss_figure()
    step_figure()
