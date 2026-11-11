#!/usr/bin/env python3
"""Figures for Book 1, chapter `attention` [D-014].

Run: python3 figures/attention.py
Writes attention-head.svg, attention-kernel.svg, and attention-cost.svg next
to this script. Numbers come from code/checks/attention.py [D-009].
"""
import importlib.util
import math
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "attention_checks", OUT.parent / "code" / "checks" / "attention.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
GRID = "#d0d0d0"
ACCENT = "#2f6fae"
WARM = "#b5523b"
LIGHT = "#9fbfdc"


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


def head_figure():
    rows = C.head(C.RIVER)
    weights = [w for _, _, w, _ in rows]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={"width_ratios": [1, 1.25]})
    ax1.imshow(weights, cmap="Blues", vmin=0, vmax=0.8)
    for i, row in enumerate(weights):
        for j, w in enumerate(row):
            ax1.text(j, i, f"{w:.2f}", ha="center", va="center", fontsize=7.5,
                     color="white" if w > 0.45 else INK)
    ax1.add_patch(plt.Rectangle((-0.5, 0.5), 5, 1, fill=False, edgecolor=WARM, linewidth=1.4))
    ax1.set_xticks(range(5))
    ax1.set_xticklabels(C.RIVER)
    ax1.xaxis.tick_top()
    ax1.set_yticks(range(5))
    ax1.set_yticklabels(C.RIVER)
    ax1.tick_params(length=0, colors=INK)
    for s in ax1.spines.values():
        s.set_visible(False)
    ax1.set_xlabel("(a) weights: rows ask, columns are looked at",
                   color=MUTED, fontsize=7.5)
    # (b) the vector for "bank" before and after, in two sentences.
    before = C.WORDS["bank"]
    after_river = C.head(C.RIVER)[1][3]
    after_money = C.head(C.MONEY)[1][3]
    xs = range(len(C.DIMS))
    wd = 0.26
    ax2.bar([x - wd for x in xs], before, wd, color="#c8c8c8", label="\"bank\" alone")
    ax2.bar(list(xs), after_river, wd, color=ACCENT, label="after: \"the bank of the river\"")
    ax2.bar([x + wd for x in xs], after_money, wd, color=WARM, label="after: \"the bank lent us money\"")
    ax2.set_xticks(list(xs))
    ax2.set_xticklabels(C.DIMS)
    ax2.set_ylim(0, 1.25)
    ax2.legend(frameon=False, fontsize=7, loc="upper left")
    ax2.set_xlabel("(b) the four numbers of \"bank\", before and after the head", color=MUTED, fontsize=7.5)
    quiet(ax2)
    fig.subplots_adjust(wspace=0.25)
    save(fig, "attention-head")


def kernel_figure():
    xs, ys, q, h = [1, 2, 3, 4, 5], [1, 3, 2, 5, 4], 2.4, 0.7
    k = [math.exp(-((x - q) ** 2) / (2 * h * h)) for x in xs]
    w = [v / sum(k) for v in k]
    est = sum(a * b for a, b in zip(w, ys))
    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    grid = [0.5 + i * 0.01 for i in range(501)]
    bump = [math.exp(-((g - q) ** 2) / (2 * h * h)) for g in grid]
    ax.fill_between(grid, 0, [5.6 * b for b in bump], color=LIGHT, alpha=0.35, linewidth=0)
    ax.scatter(xs, ys, s=[20 + 260 * v for v in w], color=ACCENT, zorder=3)
    for x, y, v in zip(xs, ys, w):
        ax.annotate(f"{v:.2f}", (x, y), xytext=(8, 4), textcoords="offset points", fontsize=7.5, color=ACCENT)
    ax.axvline(q, color=WARM, linewidth=0.8, linestyle="--")
    ax.scatter([q], [est], marker="D", s=30, color=WARM, zorder=4)
    ax.annotate(f"estimate {est:.2f}", (q, est), xytext=(-78, -12), textcoords="offset points", fontsize=7.5,
                color=WARM)
    ax.text(q - 0.06, 5.75, "query x = 2.4", ha="right", fontsize=7.5, color=WARM)
    ax.set_xlabel("x (keys: where the observations were made)", color=MUTED)
    ax.set_ylabel("y (values)", color=MUTED)
    ax.set_xlim(0.5, 5.6)
    ax.set_ylim(0, 6.1)
    quiet(ax)
    save(fig, "attention-kernel")


def cost_figure():
    d = 512
    ns = [2 ** (i / 4) for i in range(16, 69)]
    fig, ax = plt.subplots(figsize=(5.0, 2.9))
    ax.plot(ns, [n * n * d for n in ns], color=ACCENT, linewidth=1.6, label="self-attention layer: grows as n²")
    ax.plot(ns, [n * d * d for n in ns], color=WARM, linewidth=1.6, label="recurrent layer: grows as n")
    ax.set_xscale("log", base=2)
    ax.set_yscale("log")
    ax.axvline(512, color=GRID, linewidth=0.8)
    ax.text(600, 2e7, "equal at n = 512", fontsize=7, color=MUTED)
    for n, label in ((30, "a 30-token\nsentence"), (131072, "131,072\ntokens")):
        ax.axvline(n, color=GRID, linewidth=0.8, linestyle=":")
        ax.text(n, 1e15, label, fontsize=7, color=MUTED, ha="center")
    ax.set_xticks([16, 128, 1024, 8192, 65536])
    ax.set_xticklabels(["16", "128", "1,024", "8,192", "65,536"])
    ax.set_xlabel("sequence length n (tokens), with vectors of d = 512 numbers", color=MUTED)
    ax.set_ylabel("multiply-adds per layer", color=MUTED)
    ax.legend(frameon=False, fontsize=7.5, loc="upper left", bbox_to_anchor=(0.12, 0.8))
    ax.set_ylim(1e6, 3e16)
    quiet(ax)
    save(fig, "attention-cost")


if __name__ == "__main__":
    head_figure()
    kernel_figure()
    cost_figure()
