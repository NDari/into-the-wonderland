#!/usr/bin/env python3
"""Figures for Book 1, chapter `prompting` [D-014].

Run: python3 figures/prompting.py
Writes prompting-cot-scale.svg and prompting-lost-in-middle.svg next to this
script. The values are the printed table values copied into
code/checks/prompting.py [D-009]; nothing is read off a published figure.
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "prompting_checks", OUT.parent / "code" / "checks" / "prompting.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
GRID = "#d0d0d0"
ACCENT = "#2f6fae"
LIGHT = "#9dbbd9"
WARM = "#b5523b"
WARMLIGHT = "#d9a294"


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
    ax.grid(True, which="major", color="#eeeeee", linewidth=0.6)
    ax.set_axisbelow(True)


def cot_scale_figure():
    fams = list(C.WEI_TABLE2)
    fig, axes = plt.subplots(1, len(fams), figsize=(7.0, 2.7), sharey=True)
    for i, (ax, fam) in enumerate(zip(axes, fams)):
        rows = C.WEI_TABLE2[fam]
        xs = [n for _, n, _, _ in rows]
        ax.plot(xs, [s for _, _, s, _ in rows], marker="o", color=MUTED, linewidth=1.2, markersize=3.5,
                label="standard prompting")
        ax.plot(xs, [c for _, _, _, c in rows], marker="s", color=WARM, linewidth=1.6, markersize=3.5,
                label="chain-of-thought prompting")
        ax.axhline(C.WEI_PRIOR_BEST, color=ACCENT, linewidth=0.8, linestyle="--")
        ax.set_xscale("log")
        ax.set_xticks(xs)
        names = [name for name, _, _, _ in rows]
        if fam == "LaMDA":              # 68B and 137B are too close to share one line
            names[-1] = "\n" + names[-1]
        if fam == "GPT-3":              # so are 350M and 1.3B
            names[1] = "\n" + names[1]
        ax.set_xticklabels(names, fontsize=7)
        ax.minorticks_off()
        ax.set_xlim(xs[0] / 2, xs[-1] * 4)
        ax.set_ylim(0, 62)
        ax.set_title(fam, fontsize=8, color=INK, loc="left")
        ax.set_xlabel("parameters", color=MUTED, fontsize=7.5)
        quiet(ax)
        if i == 0:
            ax.set_ylabel("GSM8K accuracy (%)", color=MUTED)
            ax.text(xs[0] / 1.8, C.WEI_PRIOR_BEST + 1.2, "prior best, finetuned (55)", fontsize=6.8, color=ACCENT)
            ax.legend(frameon=False, fontsize=6.8, loc="center left", bbox_to_anchor=(0.0, 0.62))
        last = rows[-1]
        dy = (3, -4) if fam == "LaMDA" else (0, 0)    # 14.3 and 6.5 are close together
        ax.annotate(f"{last[3]}", (last[1], last[3]), xytext=(5, dy[0]), textcoords="offset points",
                    fontsize=6.8, color=WARM, ha="left", va="center")
        ax.annotate(f"{last[2]}", (last[1], last[2]), xytext=(5, dy[1]), textcoords="offset points",
                    fontsize=6.8, color=MUTED, ha="left", va="center")
    fig.subplots_adjust(wspace=0.12)
    save(fig, "prompting-cot-scale")


STYLE = {
    "GPT-3.5-Turbo": dict(color=WARM, linewidth=1.8, marker="o", markersize=4),
    "GPT-3.5-Turbo (16K)": dict(color=WARMLIGHT, linewidth=1.0, marker="", linestyle=(0, (3, 2))),
    "Claude-1.3": dict(color=ACCENT, linewidth=1.2, marker="s", markersize=3.2),
    "MPT-30B-Instruct": dict(color=MUTED, linewidth=1.1, marker="^", markersize=3.2),
    "LongChat-13B (16K)": dict(color=LIGHT, linewidth=1.2, marker="D", markersize=3),
}
# Hand-placed vertical offsets (points) for the labels at the right end.
LABEL_DY = {"GPT-3.5-Turbo": 3, "GPT-3.5-Turbo (16K)": -6, "Claude-1.3": -2, "MPT-30B-Instruct": -3,
            "LongChat-13B (16K)": -4}


def lost_in_middle_figure():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    xs = C.LIU_POSITIONS
    for name, row in C.LIU_TABLE6.items():
        ax.plot(xs, row, label=name, **STYLE[name])
        if name != "GPT-3.5-Turbo (16K)":
            ax.annotate(name, (xs[-1], row[-1]), xytext=(6, LABEL_DY[name]), textcoords="offset points",
                        fontsize=7, color=STYLE[name]["color"], va="center")
    ax.annotate("GPT-3.5-Turbo (16K), dashed", (xs[-1], 63.1), xytext=(6, -8), textcoords="offset points",
                fontsize=6.5, color=WARMLIGHT, va="center")
    ax.axhline(C.LIU_CLOSED_BOOK, color=WARM, linewidth=0.8, linestyle=":")
    ax.text(1.0, 49.0, "dotted line: GPT-3.5-Turbo with no documents at all (closed-book), 56.1",
            fontsize=6.8, color=WARM)
    ax.set_xticks(xs)
    ax.set_xticklabels(["1st", "5th", "10th", "15th", "20th"])
    ax.set_xlim(0.5, 20.5)
    ax.set_ylim(47.5, 79)
    ax.set_xlabel("position of the document that contains the answer, among 20", color=MUTED)
    ax.set_ylabel("accuracy (%)", color=MUTED)
    quiet(ax)
    save(fig, "prompting-lost-in-middle")


if __name__ == "__main__":
    cot_scale_figure()
    lost_in_middle_figure()
