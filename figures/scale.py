#!/usr/bin/env python3
"""Figures for Book 1, chapter `scale` [D-014].

Run: python3 figures/scale.py
Writes scale-models.svg, scale-powerlaw.svg, and scale-emergence.svg next to
this script. Numbers come from code/checks/scale.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "scale_checks", OUT.parent / "code" / "checks" / "scale.py")
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
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)
    ax.grid(True, which="major", color="#eeeeee", linewidth=0.6)
    ax.set_axisbelow(True)


# Hand-placed label offsets (points), so names do not collide.
OFFSETS = {
    "GPT": (5, -3), "BERT-large": (5, -3), "GPT-2": (5, -3), "T5-11B": (-38, 4), "GPT-3": (-34, 2),
    "Gopher": (-34, -3), "Chinchilla": (-50, -10), "PaLM": (5, 3), "LLaMA-65B": (-12, -13), "Llama 2 70B": (5, -3),
    "Llama 3.1 405B": (-48, -13),
}
TOKEN_OFFSETS = {
    "BERT-large": (5, -3), "T5-11B": (5, -3), "GPT-3": (5, -6), "Gopher": (5, 2), "Chinchilla": (-50, 6),
    "PaLM": (5, -6), "LLaMA-65B": (4, -11), "Llama 2 70B": (5, -3), "Llama 3.1 405B": (-80, 2),
}


def models_figure():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.4, 3.3))
    for name, year, n, d, fam in C.MODELS:
        marker = "o" if fam == "decoder" else ("s" if fam == "encoder" else "D")
        color = ACCENT if fam == "decoder" else WARM
        ax1.scatter([year], [n], marker=marker, color=color, s=22, zorder=3)
        ax1.annotate(name, (year, n), xytext=OFFSETS.get(name, (5, -3)), textcoords="offset points", fontsize=6.8,
                     color=INK)
        if d:
            ax2.scatter([year], [d], marker=marker, color=color, s=22, zorder=3)
            ax2.annotate(name, (year, d), xytext=TOKEN_OFFSETS.get(name, (5, -3)), textcoords="offset points",
                         fontsize=6.8, color=INK)
    for ax, title in ((ax1, "(a) parameters"), (ax2, "(b) training tokens")):
        ax.set_yscale("log")
        ax.set_xlim(2017.9, 2025.0)
        ax.set_xticks([2018, 2019, 2020, 2021, 2022, 2023, 2024])
        ax.set_xticklabels(["2018", "", "2020", "", "2022", "", "2024"])
        ax.set_title(title, fontsize=8, color=INK, loc="left")
        quiet(ax)
    ax1.set_ylim(5e7, 2e12)
    ax2.set_ylim(5e10, 5e13)
    ax1.scatter([], [], marker="o", color=ACCENT, s=22, label="decoder-only")
    ax1.scatter([], [], marker="s", color=WARM, s=22, label="encoder (BERT)")
    ax1.scatter([], [], marker="D", color=WARM, s=22, label="encoder-decoder (T5)")
    ax1.legend(frameon=False, fontsize=6.8, loc="lower right")
    fig.subplots_adjust(wspace=0.28)
    save(fig, "scale-models")


def powerlaw_figure():
    ns = [10 ** (6 + i * 0.05) for i in range(101)]
    ls = [C.kaplan_loss(n) for n in ns]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.8))
    for ax in (ax1, ax2):
        meas = [(n, l) for n, l in zip(ns, ls) if n <= 1.5e9]
        extra = [(n, l) for n, l in zip(ns, ls) if n >= 1.5e9]
        ax.plot([n for n, _ in meas], [l for _, l in meas], color=ACCENT, linewidth=1.6, label="range Kaplan et al. measured")
        ax.plot([n for n, _ in extra], [l for _, l in extra], color=ACCENT, linewidth=1.6, linestyle="--",
                label="extrapolated")
        ax.set_xlabel("parameters (without embeddings)", color=MUTED)
        quiet(ax)
    ax1.set_ylabel("predicted loss (nats per token)", color=MUTED)
    ax1.set_xlim(0, 1.05e10)
    ax1.set_xticks([0, 2.5e9, 5e9, 7.5e9, 1e10])
    ax1.set_xticklabels(["0", "2.5B", "5B", "7.5B", "10B"])
    ax1.set_title("(a) ordinary axes", fontsize=8, color=INK, loc="left")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_yticks([1.5, 2, 3, 4])
    ax2.set_yticklabels(["1.5", "2", "3", "4"])
    ax2.minorticks_off()
    ax2.set_title("(b) log-log axes: a straight line", fontsize=8, color=INK, loc="left")
    ax2.legend(frameon=False, fontsize=7, loc="upper right")
    fig.subplots_adjust(wspace=0.3)
    save(fig, "scale-powerlaw")


def emergence_figure():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.8))
    sizes = [n for _, n in C.GPT3_SIZES]
    ax1.plot(sizes, C.ADD2_FEW, marker="o", color=ACCENT, linewidth=1.2, markersize=4, label="2-digit addition")
    ax1.plot(sizes, C.ADD3_FEW, marker="s", color=WARM, linewidth=1.2, markersize=4, label="3-digit addition")
    ax1.set_xscale("log")
    ax1.set_xlabel("GPT-3 model size (parameters)", color=MUTED)
    ax1.set_ylabel("accuracy, few-shot (%)", color=MUTED)
    ax1.set_title("(a) published: GPT-3, Table H.1", fontsize=8, color=INK, loc="left")
    ax1.legend(frameon=False, fontsize=7, loc="upper left")
    quiet(ax1)
    ps = [0.4 + i * 0.006 for i in range(101)]
    ax2.plot(ps, ps, color=MUTED, linewidth=1.2, label="each token right (p)")
    ax2.plot(ps, [p ** 5 for p in ps], color=WARM, linewidth=1.6, label="all 5 tokens right (p⁵)")
    ax2.set_xlabel("chance of getting each token right", color=MUTED)
    ax2.set_ylabel("score", color=MUTED)
    ax2.set_title("(b) constructed: a strict score on 5 tokens", fontsize=8, color=INK, loc="left")
    ax2.legend(frameon=False, fontsize=7, loc="upper left")
    quiet(ax2)
    fig.subplots_adjust(wspace=0.32)
    save(fig, "scale-emergence")


if __name__ == "__main__":
    models_figure()
    powerlaw_figure()
    emergence_figure()
