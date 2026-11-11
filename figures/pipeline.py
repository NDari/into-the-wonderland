#!/usr/bin/env python3
"""The end-to-end LLM pipeline diagram [D-014].

Run: python3 figures/pipeline.py
Writes one SVG per variant next to this script. The diagram recurs across
Book 1; later chapters add a variant here (for example, one that highlights
the box the chapter explains) so that every version shares this layout.

The probabilities in the boxes are computed by code/checks/destination.py
[D-009]. The token IDs are GPT-2's for "The cat sat on the", as produced by
code/checks/tokens.py (Example 4).
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

OUT = Path(__file__).parent

# Load the worked example so the figure shows the same computed numbers.
_spec = importlib.util.spec_from_file_location(
    "destination_checks", OUT.parent / "code" / "checks" / "destination.py")
_checks = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_checks)
_probs = _checks.softmax([s for _, s in _checks.LOGITS])[0]
_ranked = sorted(zip((t.strip() for t, _ in _checks.LOGITS), _probs), key=lambda x: -x[1])
PROBS_TEXT = f"{_ranked[0][0]} {_ranked[0][1]:.3f}\n{_ranked[1][0]} {_ranked[1][1]:.3f}  ..."
PICKED = _ranked[0][0]  # the box shows the most probable token

# Reproducible SVG output: fixed hash salt, no timestamp.
plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
PARAM_FILL = "#dbe7f3"   # boxes that contain learned parameters
PLAIN_FILL = "#ffffff"
HIGHLIGHT = "#c0392b"

# Each box: key, title, subtitle, example content, holds learned parameters?
TOP = [
    ("text", "Text", "", "“The cat sat\non the”", False),
    ("tokens", "Tokens", "", "The | cat | sat\n| on | the", False),
    ("ids", "Token IDs", "", "464  3797  3332\n319  262", False),
    ("vectors", "Vectors", "embedding table", "one list of numbers\nper token", True),
]
BOTTOM = [
    ("layers", "Layers", "transformer blocks,\nstacked", "updated using its own\nand earlier vectors", True),
    ("scores", "Scores", "output layer", "one score per\nvocabulary entry", True),
    ("probs", "Probabilities", "softmax", PROBS_TEXT, False),
    ("pick", "Pick one", "sampling", f"“{PICKED}”", False),
]

BOX_W, BOX_H = 2.5, 1.7
GAP = 0.6
ROW_Y = {"top": 3.2, "bottom": 0.0}


def box_positions():
    pos = {}
    for i, (key, *_rest) in enumerate(TOP):
        pos[key] = (i * (BOX_W + GAP), ROW_Y["top"])
    # Bottom row runs right to left, so the flow makes a loop.
    for i, (key, *_rest) in enumerate(BOTTOM):
        pos[key] = ((len(BOTTOM) - 1 - i) * (BOX_W + GAP), ROW_Y["bottom"])
    return pos


def draw(name, highlight=()):
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    pos = box_positions()
    for key, title, subtitle, example, has_params in TOP + BOTTOM:
        x, y = pos[key]
        edge = HIGHLIGHT if key in highlight else INK
        ax.add_patch(FancyBboxPatch(
            (x, y), BOX_W, BOX_H, boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=PARAM_FILL if has_params else PLAIN_FILL,
            edgecolor=edge, linewidth=2.0 if key in highlight else 1.0))
        ax.text(x + BOX_W / 2, y + BOX_H - 0.12, title, ha="center", va="top",
                fontweight="bold", color=INK)
        if subtitle:
            ax.text(x + BOX_W / 2, y + BOX_H - 0.45, subtitle, ha="center", va="top",
                    fontsize=7, color=INK)
        ax.text(x + BOX_W / 2, y + 0.12, example, ha="center", va="bottom",
                fontsize=7, color=MUTED)

    def arrow(start, end, **kw):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=12,
                                     color=INK, linewidth=1.0, **kw))

    mid = BOX_H / 2
    order = [k for k, *_ in TOP] + [k for k, *_ in BOTTOM]
    for a, b in zip(order, order[1:]):
        (xa, ya), (xb, yb) = pos[a], pos[b]
        if ya == yb and xb > xa:      # top row, left to right
            arrow((xa + BOX_W, ya + mid), (xb, yb + mid))
        elif ya == yb:                # bottom row, right to left
            arrow((xa, ya + mid), (xb + BOX_W, yb + mid))
        else:                         # down from the top row to the bottom row
            arrow((xa + BOX_W / 2, ya), (xb + BOX_W / 2, yb + BOX_H))

    # The loop: the picked token is appended to the text and the pipeline runs again.
    (xp, yp), (xt, yt) = pos["pick"], pos["text"]
    arrow((xp + BOX_W / 2, yp + BOX_H), (xt + BOX_W / 2, yt),
          connectionstyle="arc3,rad=0.0")
    ax.text(xp + BOX_W / 2 + 0.08, (yp + BOX_H + yt) / 2, "append to the text\nand repeat",
            ha="left", va="center", fontsize=7, color=INK, style="italic")

    # Legend for the shaded boxes.
    lx, ly = pos["text"][0], ROW_Y["top"] + BOX_H + 0.25
    ax.add_patch(FancyBboxPatch((lx, ly), 0.3, 0.2, boxstyle="square,pad=0",
                                facecolor=PARAM_FILL, edgecolor=INK, linewidth=0.8))
    ax.text(lx + 0.4, ly + 0.1, "shaded boxes contain learned parameters",
            va="center", fontsize=7, color=INK)

    width = len(TOP) * BOX_W + (len(TOP) - 1) * GAP
    ax.set_xlim(-0.1, width + 0.1)
    ax.set_ylim(-0.1, ROW_Y["top"] + BOX_H + 0.55)
    ax.set_aspect("equal")
    ax.axis("off")
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


VARIANTS = {
    # The full picture at low resolution, used in `destination`.
    "pipeline-destination": (),
}

if __name__ == "__main__":
    for variant, highlight in VARIANTS.items():
        draw(variant, highlight)
