#!/usr/bin/env python3
"""Figures for Book 1, chapter `embeddings` [D-014].

Run: python3 figures/embeddings.py
Writes embeddings-glove-pca.svg and embeddings-lsa.svg next to this script.
Numbers come from code/checks/embeddings.py [D-009]; the GloVe vectors are
downloaded and hash-checked by that script [D-018].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "embeddings_checks", OUT.parent / "code" / "checks" / "embeddings.py")
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
    ax.tick_params(colors=MUTED, length=0, labelsize=7)


def glove_figure():
    G = C.Glove()
    P, share = C.pca2(G, C.PLOT_WORDS)
    pos = {w: P[i] for i, w in enumerate(C.PLOT_WORDS)}
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    ax.scatter(P[:, 0], P[:, 1], s=14, color=ACCENT, zorder=3)
    # Hand-placed label offsets (in points) where labels would collide.
    offset = {"king": (-26, 4), "queen": (4, 6), "princess": (4, -10), "girl": (4, 6), "cat": (-4, -13),
              "boy": (5, -3), "woman": (-34, 6), "man": (-27, -3), "cow": (-22, 3), "bus": (-20, -11), "car": (4, 4),
              "france": (-14, 6), "italy": (5, 3), "paris": (5, -2), "berlin": (5, -7), "germany": (-10, -12)}
    for w, (x, y) in pos.items():
        ax.annotate(w, (x, y), xytext=offset.get(w, (4, 3)), textcoords="offset points", fontsize=8, color=INK)
    ax.set_xlabel(f"first principal component ({share[0]:.0%} of the variance)", color=MUTED)
    ax.set_ylabel(f"second principal component ({share[1]:.0%})", color=MUTED)
    quiet(ax)
    save(fig, "embeddings-glove-pca")


def lsa_figure():
    _, _, T2 = C.lsa()
    fig, ax = plt.subplots(figsize=(5.0, 3.4))
    offset = {"trees": (5, 2), "minors": (5, -9), "human": (5, -7), "interface": (5, 3)}
    for i, t in enumerate(C.TERMS):
        color = WARM if t in ("trees", "graph", "minors") else ACCENT
        ax.scatter(T2[i, 0], T2[i, 1], s=14, color=color, zorder=3)
        if t == "time":
            continue   # same point as "response" (identical rows in the count table)
        label = "response, time" if t == "response" else t
        ax.annotate(label, (T2[i, 0], T2[i, 1]), xytext=offset.get(t, (4, 3)), textcoords="offset points",
                    fontsize=8, color=INK)
    ax.axhline(0, color=GRID, linewidth=0.8, zorder=1)
    ax.set_xlabel("first factor", color=MUTED)
    ax.set_ylabel("second factor", color=MUTED)
    quiet(ax)
    save(fig, "embeddings-lsa")


if __name__ == "__main__":
    glove_figure()
    lsa_figure()
