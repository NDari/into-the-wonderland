#!/usr/bin/env python3
"""Figures for Book 1, chapter `evaluation` [D-014].

Run: python3 figures/evaluation.py
Writes evaluation-ci.svg and evaluation-elo.svg next to this script. Numbers
come from code/checks/evaluation.py [D-009].
"""
import importlib.util
import math
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "evaluation_checks", OUT.parent / "code" / "checks" / "evaluation.py")
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
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("bottom", "left"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)


def ci_figure():
    ns = [50 * (20000 / 50) ** (i / 200) for i in range(201)]
    fig, ax = plt.subplots(figsize=(7.0, 3.0))
    ax.plot(ns, [C.half_width(0.5, n) for n in ns], color=ACCENT, linewidth=1.6)
    ax.plot(ns, [C.half_width(0.8, n) for n in ns], color=ACCENT, linewidth=1.6, linestyle="--")
    ax.text(60, C.half_width(0.5, 60) + 0.4, "true accuracy 50%", fontsize=7.5, color=ACCENT, va="bottom")
    ax.text(60, C.half_width(0.8, 60) - 0.5, "true accuracy 80%", fontsize=7.5, color=ACCENT, va="top")
    # Label positions (x, y in data units, alignment), chosen by eye to avoid the curves.
    places = {"HumanEval": (155, 4.2, "right"), "GPQA Diamond": (215, 7.3, "left"),
              "GSM8K test": (1400, 3.4, "left"), "HLE public set": (2650, 5.4, "left"),
              "MMLU test": (13000, 2.8, "right")}
    for name, n in C.BENCHMARKS:
        hw = C.half_width(0.8, n)
        ax.axvline(n, color=GRID, linewidth=0.8, zorder=0)
        ax.plot([n], [hw], "o", color=WARM, markersize=3.5, zorder=3)
        x, y, ha = places[name]
        ax.text(x, y, f"{name}\nn = {n:,}: \u00b1{hw:.1f}", ha=ha, va="bottom", fontsize=7, color=WARM)
    ax.set_xscale("log")
    ax.set_xlim(50, 20000)
    ax.set_ylim(0, 15)
    ax.set_xticks([50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000])
    ax.set_xticklabels(["50", "100", "200", "500", "1,000", "2,000", "5,000", "10,000", "20,000"])
    ax.minorticks_off()
    ax.set_xlabel("number of questions in the benchmark (log scale)", fontsize=7.5, color=MUTED)
    ax.set_ylabel("95% interval, ± percentage points", fontsize=7.5, color=MUTED)
    quiet(ax)
    save(fig, "evaluation-ci")


def elo_figure():
    gaps = list(range(0, 401, 2))
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    ax.plot(gaps, [C.win_prob(d) for d in gaps], color=ACCENT, linewidth=1.6)
    span = C.ARENA_TOP - C.ARENA_13
    ax.axvspan(0, span, color=LIGHT, alpha=0.6, linewidth=0, zorder=0)
    ax.text(span + 6, 0.9, f"shaded: the top 13 of the October 2026\nleaderboard, {span:.1f} points apart",
            fontsize=7, color=MUTED, va="center")
    for d in (15, 100, 200, 400):
        p = C.win_prob(d)
        ax.plot([d], [p], "o", color=WARM, markersize=3.5, zorder=3)
        dx, dy, ha = (8, -16, "left") if d < 400 else (-4, -22, "right")
        ax.annotate(f"{d} points: {p:.1%}", (d, p), xytext=(dx, dy), textcoords="offset points",
                    ha=ha, fontsize=7, color=WARM)
    ax.set_xlim(0, 410)
    ax.set_ylim(0.4, 1.0)
    ax.set_yticks([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_yticklabels(["40%", "50%", "60%", "70%", "80%", "90%", "100%"])
    ax.axhline(0.5, color=GRID, linewidth=0.8, zorder=0)
    ax.set_xlabel("rating gap between two models (Arena points)", fontsize=7.5, color=MUTED)
    ax.set_ylabel("chance the higher-rated\nmodel wins a vote", fontsize=7.5, color=MUTED)
    quiet(ax)
    save(fig, "evaluation-elo")


if __name__ == "__main__":
    ci_figure()
    elo_figure()
