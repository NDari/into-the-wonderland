#!/usr/bin/env python3
"""Figures for Book 1, chapter `frontier` [D-014].

Run: python3 figures/frontier.py
Writes frontier-aime.svg and frontier-horizons.svg next to this script.
Numbers come from code/checks/frontier.py [D-009]: printed values only, nothing
read off a plot. METR's values are hard-coded there with their source, access
date, and hash.
"""
import importlib.util
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "frontier_checks", OUT.parent / "code" / "checks" / "frontier.py")
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


def aime_figure():
    rows = [("GPT-4o, one sample", 1.8, GREY),
            ("o1, one sample", 11.1, LIGHT),
            ("o1, majority vote of 64 samples", 12.5, ACCENT),
            ("o1, best of 1,000 chosen by a learned scorer", 13.9, WARM)]
    fig, ax = plt.subplots(figsize=(7.0, 1.9))
    for i, (label, solved, color) in enumerate(rows):
        ax.barh(i, solved, height=0.6, color=color, edgecolor="white")
        ax.text(solved + 0.2, i, f"{solved} of 15 ({solved / 15:.0%})", va="center", fontsize=8, color=INK)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=8, color=INK)
    ax.invert_yaxis()
    ax.set_xlim(0, 15)
    ax.set_xticks([0, 5, 10, 15])
    ax.set_xlabel("problems solved, average over the 2024 AIME (15 problems per exam)", fontsize=7.5, color=MUTED)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)
    save(fig, "frontier-aime")


def horizons_figure():
    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    limit = C.METR_LIMIT_MIN
    x0, x1 = date(2018, 10, 1), date(2026, 10, 1)
    ax.axhspan(limit, 1e5, color=WARMFILL, zorder=0, linewidth=0)
    ax.text(date(2019, 1, 1), limit * 1.35, "above 16 hours: unreliable with METR's task suite",
            fontsize=7, color=WARM, va="bottom")
    for y in (1, 60, 8 * 60):
        ax.axhline(y, color=GRID, linewidth=0.6, zorder=1)
    offsets = {
        "GPT-2": (6, 4, "left"),
        "GPT-4": (6, 4, "left"),
        "o1": (-6, 6, "right"),
        "o3": (-6, 6, "right"),
        "GPT-5": (-6, 6, "right"),
        "GPT-5.2": (6, -14, "left"),
    }
    # Crowded points get labels placed to the left, with a leader line.
    leaders = {
        "Claude Opus 4.5": (date(2024, 7, 1), 800.0),
        "Claude Opus 4.6": (date(2024, 7, 1), 2000.0),
        "Claude Mythos Preview (early)": (date(2024, 7, 1), 5000.0),
    }
    for name, d, p50, ci in C.METR:
        if ci:
            ax.errorbar([d], [p50], yerr=[[p50 - ci[0]], [ci[1] - p50]], fmt="none",
                        ecolor=ACCENT, elinewidth=0.9, capsize=2.5, zorder=2)
        ax.plot([d], [p50], "o", color=ACCENT, markersize=4.5, zorder=3)
        if name in leaders:
            ax.annotate(name, (d, p50), xytext=leaders[name], textcoords="data",
                        ha="right", va="center", fontsize=7, color=INK,
                        arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.5,
                                        shrinkA=2, shrinkB=3))
        else:
            dx, dy, ha = offsets[name]
            ax.annotate(name, (d, p50), xytext=(dx, dy), textcoords="offset points",
                        ha=ha, va="center", fontsize=7, color=INK)
    ax.set_yscale("log")
    ax.set_ylim(0.006, 1e4)
    ticks = [0.1, 1, 10, 60, 8 * 60, limit]
    ax.set_yticks(ticks)
    ax.set_yticklabels(["6 s", "1 min", "10 min", "1 h", "8 h", "16 h"])
    ax.minorticks_off()
    ax.set_xlim(x0, x1)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_xlabel("model release date", fontsize=7.5, color=MUTED)
    ax.set_ylabel("length of tasks (human time) completed\nwith 50% success, log scale", fontsize=7.5, color=MUTED)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)
    save(fig, "frontier-horizons")


if __name__ == "__main__":
    aime_figure()
    horizons_figure()
