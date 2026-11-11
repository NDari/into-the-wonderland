#!/usr/bin/env python3
"""Figures for Book 1, chapter `tokens` [D-014].

Run: python3 figures/tokens.py
Writes tokens-three-ways.svg and tokens-bpe-merges.svg next to this script.
Numbers come from code/checks/tokens.py [D-009]; GPT-2's vocabulary files are
downloaded and hash-checked by that script [D-018].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "tokens_checks", OUT.parent / "code" / "checks" / "tokens.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
ACCENT = "#2f6fae"
FILL = "#dbe7f3"
WARMFILL = "#f3dcd6"
WARM = "#b5523b"
MONO = "DejaVu Sans Mono"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


CHAR_W = 0.13   # width of one monospaced character, in axis units


def chips(ax, y, pieces, face, edge, ids=None, gap=0.05):
    x = 0.0
    for i, p in enumerate(pieces):
        w = max(len(p), 1) * CHAR_W + 0.1
        if ids is not None:
            w = max(w, len(str(ids[i])) * 0.095 + 0.06)
        ax.add_patch(FancyBboxPatch((x, y - 0.17), w, 0.34, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=face, edgecolor=edge, linewidth=0.6))
        ax.text(x + w / 2, y, p, ha="center", va="center", family=MONO, fontsize=7.5, color=INK)
        if ids is not None:
            ax.text(x + w / 2, y - 0.3, str(ids[i]), ha="center", va="top", fontsize=5.8, color=MUTED)
        x += w + gap
    return x


def three_ways_figure():
    g = C.GPT2()
    text = C.THREE_WAYS
    words = C.word_split(text)
    chars = [c if c != " " else "␣" for c in text]
    toks = g.tokens(text)
    fig, ax = plt.subplots(figsize=(7.4, 2.4))
    rows = [("words", words, FILL, ACCENT, None, 2.4),
            ("characters", chars, "#f2f2f2", "#b0b0b0", None, 1.5),
            ("GPT-2 tokens", [g.readable(t) for t in toks], WARMFILL, WARM, g.ids(text), 0.6)]
    right = 0
    for label, pieces, face, edge, ids, y in rows:
        ax.text(-0.15, y, label, ha="right", va="center", fontsize=8, color=INK)
        end = chips(ax, y, pieces, face, edge, ids, gap=0.03 if label == "characters" else 0.1)
        ax.text(end + 0.1, y, f"{len(pieces)}", ha="left", va="center", fontsize=8, color=MUTED)
        right = max(right, end)
    ax.text(right + 0.1, 2.85, "count", ha="left", va="center", fontsize=7, color=MUTED)
    ax.set_xlim(-1.9, right + 0.7)
    ax.set_ylim(0.0, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "tokens-three-ways")


def merges_figure():
    merges = C.learn_bpe(C.TOY, 10)
    lines = [("start", "", "l o w </w>  ×5   l o w e r </w>  ×2   n e w e s t </w>  ×6   w i d e s t </w>  ×3")]
    for i, (pair, count, words) in enumerate(merges, 1):
        freq = [5, 2, 6, 3]
        lines.append((f"{i}", f"{pair[0]} + {pair[1]}  ({count})",
                      "   ".join(f"{w}  ×{f}" for w, f in zip(words, freq))))
    fig, ax = plt.subplots(figsize=(9.0, 3.6))
    n = len(lines)
    ax.text(0.0, n + 0.2, "step", fontsize=7.5, color=MUTED, va="bottom")
    ax.text(0.6, n + 0.2, "pair (count)", fontsize=7.5, color=MUTED, va="bottom")
    ax.text(3.6, n + 0.2, "the corpus afterwards (×: how often each word occurs)", fontsize=7.5, color=MUTED,
            va="bottom")
    for k, (num, pair, corpus) in enumerate(lines):
        y = n - k - 0.4
        if k % 2 == 0:
            ax.add_patch(plt.Rectangle((-0.05, y - 0.45), 13.0, 0.9, facecolor="#f5f7fa", edgecolor="none"))
        ax.text(0.1, y, num, fontsize=7.5, color=INK, va="center")
        ax.text(0.6, y, pair, fontsize=7.5, family=MONO, color=WARM, va="center")
        ax.text(3.6, y, corpus, fontsize=7, family=MONO, color=INK, va="center")
    tested = " | ".join(C.apply_bpe("lowest", merges))
    ax.text(0.0, -0.6, f"applying the ten merges to the unseen word \"lowest\": {tested}", fontsize=7.5,
            color=INK, va="center")
    ax.set_xlim(-0.1, 13.0)
    ax.set_ylim(-1.0, n + 0.7)
    ax.axis("off")
    save(fig, "tokens-bpe-merges")


if __name__ == "__main__":
    three_ways_figure()
    merges_figure()
