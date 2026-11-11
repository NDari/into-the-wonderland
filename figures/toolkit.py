#!/usr/bin/env python3
"""Figures for Book 1, chapter `toolkit` [D-014].

Run: python3 figures/toolkit.py
Writes toolkit-valley.svg, toolkit-schedules.svg, and toolkit-loss.svg next
to this script. All numbers come from code/checks/toolkit.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "toolkit_checks", OUT.parent / "code" / "checks" / "toolkit.py")
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
    ax.tick_params(colors=MUTED, length=0)


def valley_figure():
    """Example 3: the first 40 steps in the narrow valley, with and without momentum."""
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.4), sharey=True)
    xs = [i / 10 for i in range(-20, 121)]
    ys = [j / 100 for j in range(-150, 151)]
    Z = [[C.valley_f(x, y) for x in xs] for y in ys]
    for ax, (rate, mom, title) in zip(axes, ((0.019, 0.0, "plain gradient descent, rate 0.019"),
                                             (0.01, 0.9, "with momentum 0.9, rate 0.01"))):
        ax.contour(xs, ys, Z, levels=[0.5, 2, 8, 20, 50, 100], colors=GRID, linewidths=0.8)
        _, path = C.run_valley(rate, mom, limit=40, record=True)
        ax.plot([p[0] for p in path], [p[1] for p in path], "-o", color=ACCENT, markersize=2.5, linewidth=1)
        ax.plot([0], [0], "x", color=INK, markersize=6)
        ax.set_title(f"{title}\nfirst 40 steps", fontsize=8.5, color=INK)
        ax.set_xlim(-2, 12)
        ax.set_ylim(-1.5, 1.5)
        ax.set_xlabel("weight 1", color=MUTED)
        quiet(ax)
    axes[0].set_ylabel("weight 2", color=MUTED)
    fig.tight_layout()
    save(fig, "toolkit-valley")


def schedules_figure():
    """Example 5: three learning-rate schedules, each scaled to its own peak."""
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.0), sharey=True)
    steps = list(range(1, 100001, 100))
    tr = [C.transformer_lr(s) for s in steps]
    peak = max(tr)
    axes[0].plot(steps, [v / peak for v in tr], color=ACCENT, linewidth=1.8)
    axes[0].set_title("warmup, then 1/sqrt(step)\n(Transformer, 2017)", fontsize=8, color=INK)
    frac = [i / 200 for i in range(201)]
    cos = [C.cosine_lr(f * 1000) for f in frac]
    axes[1].plot(frac, [v / max(cos) for v in cos], color=ACCENT, linewidth=1.8)
    axes[1].set_title("cosine, to 10% of peak\n(LLaMA, 2023)", fontsize=8, color=INK)
    sx = [0, 0.3, 0.3, 0.6, 0.6, 0.9, 0.9, 1.0]
    sy = [1, 1, 0.1, 0.1, 0.01, 0.01, 0.001, 0.001]
    axes[2].plot(sx, sy, color=ACCENT, linewidth=1.8)
    axes[2].set_title("divide by 10 in steps\n(ResNet, 2015)", fontsize=8, color=INK)
    for ax in axes:
        ax.set_xticks([])
        ax.set_xlabel("training time", color=MUTED)
        quiet(ax)
    axes[0].set_ylabel("learning rate\n(share of peak)", color=MUTED)
    fig.tight_layout()
    save(fig, "toolkit-schedules")


def loss_figure():
    """Example 7: training and validation loss for three learning rates."""
    runs = {name: C.train_linear(rate, 300) for name, rate in C.RUNS.items()}
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.4))
    for ax, (name, log) in zip(axes, runs.items()):
        ep = [r[0] for r in log]
        ax.plot(ep, [r[1] for r in log], color=ACCENT, linewidth=1.6)
        ax.plot(ep, [r[2] for r in log], color=WARM, linewidth=1.6)
        ax.set_title(f"learning rate {name}", fontsize=8, color=INK)
        if "large" in name:
            ax.set_yscale("log")
            ax.set_ylabel("log scale", color=MUTED)
        else:
            ax.set_ylim(0, 7.5)
        ax.set_xlabel("epoch", color=MUTED)
        quiet(ax)
    good = runs["good (0.001)"]
    best = min(good, key=lambda r: r[2])
    axes[1].axvline(best[0], color=MUTED, linestyle="--", linewidth=0.8)
    axes[1].text(best[0] + 6, 5.0, "lowest\nvalidation\nloss", fontsize=7, color=MUTED)
    axes[0].set_ylabel("mean squared error", color=MUTED)
    axes[0].text(150, 1.5, "training", color=ACCENT, fontsize=7.5)
    axes[0].text(150, 4.8, "validation", color=WARM, fontsize=7.5)
    fig.tight_layout()
    save(fig, "toolkit-loss")


if __name__ == "__main__":
    valley_figure()
    schedules_figure()
    loss_figure()
