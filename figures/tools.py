#!/usr/bin/env python3
"""Figures for Book 1, chapter `tools` [D-014].

Run: python3 figures/tools.py
Writes tools-rag.svg, tools-bm25.svg and tools-loop.svg next to this script.
Numbers come from code/checks/tools.py [D-009]; the retrieval scores in
tools-rag.svg use the GloVe vectors through that script (hash-checked cache in
out/cache/, D-018). tools-loop.svg is a diagram with no data. No model output
is drawn anywhere: the last box of tools-rag.svg says what the model is given,
not what it writes.
"""
import importlib.util
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "tools_checks", OUT.parent / "code" / "checks" / "tools.py")
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


def box(ax, x, y, w, h, text, face=GREY, edge=MUTED, color=INK, size=8, weight="normal", ha="center"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=face, edgecolor=edge, linewidth=0.8))
    tx = x + w / 2 if ha == "center" else x + 0.12
    ax.text(tx, y + h / 2, text, ha=ha, va="center", fontsize=size, color=color, weight=weight)


def arrow(ax, x0, y0, x1, y1, color=MUTED, rad=0.0):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=10,
                                 color=color, linewidth=1.0, connectionstyle=f"arc3,rad={rad}"))


# ---------------------------------------------------------------------------
def rag_figure():
    scores = C.toy_scores()
    cols = [("tf-idf\n(keywords)", "tf-idf"),
            ("averaged word\nvectors (GloVe),\nstop words removed", "averaged GloVe, stop words removed"),
            ("OpenAI's trained\nembedding model\n(their figures)", "OpenAI's trained model (quoted)")]
    traced = "averaged GloVe, stop words removed"
    top = C.ranking(scores[traced])[:C.TOP_K]

    fig, ax = plt.subplots(figsize=(7.4, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.6)
    ax.axis("off")

    # 1. The question.
    ax.text(0, 7.45, "1  The question", fontsize=8.5, color=INK, weight="bold", va="top")
    box(ax, 0.0, 6.55, 4.2, 0.55, f"“{C.QUERY}”", face=LIGHT, edge=ACCENT, size=9)
    ax.text(4.45, 6.82, "represented the same way as every passage, then compared",
            fontsize=7.5, color=MUTED, va="center")
    arrow(ax, 2.1, 6.55, 2.1, 6.1)

    # 2. Scores for every passage.
    ax.text(0, 6.0, "2  Score every passage in the collection; keep the top two",
            fontsize=8.5, color=INK, weight="bold", va="top")
    x_text, x_cols = 0.0, [6.15, 7.65, 9.25]
    y_head = 5.3
    for (label, key), xc in zip(cols, x_cols):
        ax.text(xc, y_head, label, ha="center", va="center", fontsize=7.2,
                color=WARM if key == traced else MUTED)
    ax.text(x_text, y_head, "passage", ha="left", va="center", fontsize=7.2, color=MUTED)
    ax.plot([0, 9.95], [4.85, 4.85], color=GRID, linewidth=0.8)
    row_y = [4.5, 3.95, 3.4]
    for i, (p, y) in enumerate(zip(C.PASSAGES, row_y)):
        ax.text(x_text, y, f"D{i + 1}  {p}", ha="left", va="center", fontsize=7.6, color=INK)
        for (_, key), xc in zip(cols, x_cols):
            s = scores[key][i]
            kept = i in C.ranking(scores[key])[:C.TOP_K]
            face = WARMFILL if (key == traced and kept) else (LIGHT if kept else "white")
            edge = WARM if key == traced and kept else (ACCENT if kept else GRID)
            ax.add_patch(FancyBboxPatch((xc - 0.42, y - 0.2), 0.84, 0.4,
                                        boxstyle="round,pad=0.01,rounding_size=0.05",
                                        facecolor=face, edgecolor=edge, linewidth=0.7))
            txt = f"{s:.0%}" if "OpenAI" in key else f"{s:.3f}"
            ax.text(xc, y, txt, ha="center", va="center", fontsize=7.8, color=INK)
    ax.plot([0, 9.95], [3.1, 3.1], color=GRID, linewidth=0.8)
    ax.text(0, 3.0, "Shaded: the top two passages by each score. Keyword scores keep the moon cake; "
            "both vector methods keep the moon landings.\nThe first two columns are computed for this "
            "book; the third is quoted from OpenAI's guide, not computed.\nSteps 3 and 4 follow the "
            "middle column.", fontsize=7, color=MUTED, va="top")

    # 3. The prompt.
    ax.text(0, 2.25, "3  Paste the two kept passages into the prompt", fontsize=8.5, color=INK, weight="bold", va="top")
    lines = [f"Passage: {C.PASSAGES[top[0]]}", f"Passage: {C.PASSAGES[top[1]]}",
             "Based on these texts, answer this question:", C.QUERY]
    y = 1.75
    for j, line in enumerate(lines):
        face = WARMFILL if j < 2 else (LIGHT if j == 3 else GREY)
        edge = WARM if j < 2 else (ACCENT if j == 3 else MUTED)
        box(ax, 0.0, y - 0.19, 5.6, 0.38, line, face=face, edge=edge, size=7.6, ha="left")
        y -= 0.45
    arrow(ax, 5.75, 1.08, 6.35, 1.08)

    # 4. The model.
    ax.text(6.4, 2.25, "4  The model reads the prompt", fontsize=8.5, color=INK, weight="bold", va="top")
    box(ax, 6.4, 0.18, 3.2, 1.75,
        "\n".join(textwrap.wrap("The model writes its answer from the question plus these passages, "
                                "one token at a time, as in any other reply.", 30)),
        face="white", edge=MUTED, size=7.8)
    save(fig, "tools-rag")


# ---------------------------------------------------------------------------
def bm25_figure():
    xs = [x / 10 for x in range(10, 301)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 2.7))
    ax1.plot([x for x in xs if x <= 3.6], [x for x in xs if x <= 3.6], color=MUTED, linewidth=1.2)
    ax1.plot(xs, [C.tf_slp3(x) for x in xs], color=ACCENT, linewidth=1.4)
    ax1.plot(xs, [C.bm25_tf(x) for x in xs], color=WARM, linewidth=1.6)
    ax1.axhline(1.0, color=WARM, linewidth=0.6, linestyle=":")
    ax1.text(3.4, 3.35, "raw count\n(10 at 10, 100 at 100)", fontsize=7, color=MUTED, va="top")
    ax1.text(30, C.tf_slp3(30) + 0.1, "1 + log10 count\n(3 at 100, no ceiling)", fontsize=7,
             color=ACCENT, ha="right", va="bottom")
    ax1.text(30, C.bm25_tf(30) - 0.1, f"BM25, k1 = {C.K1}: ceiling 1", fontsize=7, color=WARM,
             ha="right", va="top")
    for t in (1, 3, 10):
        ax1.plot([t], [C.bm25_tf(t)], "o", color=WARM, markersize=3)
        ax1.text(t + 0.4, C.bm25_tf(t) - 0.2, f"{C.bm25_tf(t):.3f}", fontsize=6.8, color=WARM)
    ax1.set_ylim(0, 3.6)
    ax1.set_title("(a) how much a word's count adds", fontsize=8, color=INK, loc="left")

    for r, col, lab in ((0.5, ACCENT, "half the average length"), (1.0, WARM, "average length"),
                        (2.0, MUTED, "twice the average length")):
        ax2.plot(xs, [C.bm25_tf(x, dl_over_avdl=r) for x in xs], color=col, linewidth=1.4)
        v = C.bm25_tf(3, dl_over_avdl=r)
        ax2.plot([3], [v], "o", color=col, markersize=3)
        ax2.text(30, 0.42 - 0.09 * [0.5, 1.0, 2.0].index(r), f"{lab}: {v:.3f} at 3", fontsize=7, color=col,
                 ha="right", va="center")
    ax2.set_ylim(0, 1.05)
    ax2.set_title(f"(b) BM25 by document length, b = {C.B}", fontsize=8, color=INK, loc="left")
    for ax in (ax1, ax2):
        ax.set_xlim(0, 31)
        ax.set_xlabel("times the word appears in the document", fontsize=7.5, color=MUTED)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
        ax.tick_params(colors=MUTED, length=0, labelsize=7)
    fig.subplots_adjust(wspace=0.25)
    save(fig, "tools-bm25")


# ---------------------------------------------------------------------------
def loop_figure():
    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    ax.set_xlim(0, 10)
    ax.set_ylim(0.5, 6.0)
    ax.axis("off")

    # The context window, as a stack of text.
    ax.text(0.0, 5.85, "The context window (all text)", fontsize=8.5, color=INK, weight="bold", va="top")
    stack = [("instructions from the system", GREY, MUTED),
             ("tool definitions: name, description,\nwhat arguments it takes", GREY, MUTED),
             ("the user's request", LIGHT, ACCENT),
             ("the model's request for a tool", WARMFILL, WARM),
             ("the tool's result", LIGHT, ACCENT),
             ("... repeated as needed ...", "white", GRID)]
    y = 5.35
    for text, face, edge in stack:
        h = 0.62 if "\n" in text else 0.45
        box(ax, 0.0, y - h, 3.3, h - 0.06, text, face=face, edge=edge, size=7.5)
        y -= h
    # The model.
    box(ax, 4.3, 3.9, 1.9, 0.9, "model\nreads everything,\nwrites tokens", face="white", edge=INK, size=7.8)
    arrow(ax, 3.4, 4.35, 4.25, 4.35)
    # Two ways to stop.
    box(ax, 7.0, 4.6, 2.9, 1.0,
        "stops: “end of turn”\nthe reply goes to the user;\nthe loop ends",
        face="white", edge=MUTED, size=7.5)
    arrow(ax, 6.25, 4.55, 6.95, 5.0)
    box(ax, 7.0, 2.75, 2.9, 1.45,
        "stops: “tool use”\na filled-in request:\n tool:  weather lookup\n place:  Paris",
        face=WARMFILL, edge=WARM, size=7.5)
    arrow(ax, 6.25, 4.1, 6.95, 3.6, color=WARM)
    # The program.
    box(ax, 7.0, 0.65, 2.9, 1.5,
        "the program, not the model,\nchecks the request, may ask\nthe user, runs the tool, and\n"
        "writes the result as text",
        face=GREY, edge=MUTED, size=7.5)
    arrow(ax, 8.45, 2.72, 8.45, 2.2, color=WARM)
    ax.add_patch(FancyArrowPatch((6.95, 1.4), (1.65, 2.42), arrowstyle="-|>", mutation_scale=10,
                                 color=ACCENT, linewidth=1.0,
                                 connectionstyle="angle,angleA=180,angleB=90,rad=0"))
    ax.text(4.2, 1.5, "result appended to the context; the model runs again",
            fontsize=7.2, color=ACCENT, ha="center", va="bottom")
    # ReAct names.
    ax.text(5.25, 3.65, "ReAct's names:\nthe model's text = thought\nthe request = action\n"
            "the result = observation", fontsize=7, color=MUTED, ha="center", va="top")
    save(fig, "tools-loop")


if __name__ == "__main__":
    rag_figure()
    bm25_figure()
    loop_figure()
