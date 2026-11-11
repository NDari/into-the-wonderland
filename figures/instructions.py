#!/usr/bin/env python3
"""Figures for Book 1, chapter `instructions` [D-014].

Run: python3 figures/instructions.py
Writes instructions-completions.svg, instructions-chat.svg,
instructions-steps.svg and instructions-bradley-terry.svg next to this script.
Numbers come from code/checks/instructions.py [D-009].

The completions figure reproduces the text printed in Figure 8 (p. 15) of
Ouyang et al. (2022), arXiv v1: real model outputs, not invented. Line-break
hyphens of the printed page are rejoined; "[...]" is printed in the paper.
The chat figure follows the layouts in Meta's released code (Llama 2:
llama/generation.py at c9c493f20f6b; Llama 3: llama/tokenizer.py at
71367a6cafec); the message texts in it are constructed.
"""
import importlib.util
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402
from matplotlib.textpath import TextPath  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "instructions_checks", OUT.parent / "code" / "checks" / "instructions.py")
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
PAPER = "#f7f7f7"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def box(ax, x, y, w, h, face, edge, lw=0.8, pad=0.0, rounding=0.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={pad},rounding_size={rounding}",
                                facecolor=face, edgecolor=edge, linewidth=lw))


# --- Figure 1: one prompt, two completions (InstructGPT paper, Figure 8) ---

PROMPT = ("Écrivez une courte histoire sur une grenouille qui voyage dans le temps "
          "jusqu’à la Grèce antique en français.")
GPT3 = [
    "Écrivez une histoire au sujet d’un enfant qui voudrait tout savoir sur les jeux "
    "des dieux et qui se retrouve dans l’une de leurs histoires.",
    "Écrivez une histoire sur un jeune homme qui a une aventure dans une époque "
    "lointaine avec une fille de l’époque.",
    "Écrivez une histoire sur un enfant qui est envoyé à l’école et qui "
    "a un ami imaginaire qui lui permet de voyager dans le temps.",
]
INSTRUCT = [
    "La grenouille était perdue et épuisée. Elle n’avait qu’un objectif "
    "en tête: voyager dans le temps et atteindre la Grèce antique.",
    "Premier problème, trouver un moyen de transport. Elle avait entendu dire que l’un "
    "des meilleurs moyens était de sauter dans une machine temporelle. Elle s’élança, "
    "et voilà qu’elle se retrouva dans le passé, au cours d’une nuit étoilée "
    "à l’odeur douce et envoûtante.",
    "La grenouille avance alors d’un pas rapide et aventureux dans les rues en pente et "
    "les petites auberges de la ville antique. [...]",
]
ENGLISH = {
    "prompt": "Write a short story about a frog that travels back in time to ancient Greece, in French.",
    "gpt3": "Three more requests of the same kind: write a story about a child who wants to know all "
            "about the games of the gods; about a young man's adventure in a distant era; about a "
            "child with an imaginary friend who lets him travel in time.",
    "instruct": "The frog was lost and exhausted, with one goal: to travel in time and reach ancient "
                "Greece. ... it jumped into a time machine and found itself in the past, on a starry "
                "night ... and walked through the sloping streets and little inns of the ancient town.",
}


def wrap_paragraphs(paras, width):
    lines = []
    for i, p in enumerate(paras):
        if i:
            lines.append("")
        lines.extend(textwrap.wrap(p, width))
    return "\n".join(lines)


def completions_figure():
    fig, ax = plt.subplots(figsize=(7.0, 5.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    # prompt
    box(ax, 1, 84.5, 98, 14.5, PAPER, MUTED)
    ax.text(3, 97.8, "Prompt (the same for both models)", fontsize=7.5, color=MUTED, va="top")
    ax.text(3, 95.0, "\n".join(textwrap.wrap(PROMPT, 76)), fontsize=8, color=INK, va="top")
    ax.text(3, 87.9, "(" + ENGLISH["prompt"] + ")", fontsize=6.8, color=MUTED, va="top", style="italic")
    cols = (
        (1, "GPT-3 175B, a base model", GREY, MUTED, GPT3, ENGLISH["gpt3"]),
        (51, "InstructGPT 175B, the same network\nafter post-training", LIGHT, ACCENT, INSTRUCT,
         ENGLISH["instruct"]),
    )
    for x, title, face, edge, paras, english in cols:
        box(ax, x, 1, 48, 82, face if face != GREY else "#f0f0f0", edge)
        ax.text(x + 2, 81.3, title, fontsize=8, color=edge if edge != MUTED else INK, va="top",
                fontweight="bold")
        ax.text(x + 2, 73.5, wrap_paragraphs(paras, 44), fontsize=7.5, color=INK, va="top",
                linespacing=1.3)
        ax.text(x + 2, 19.0, "\n".join(textwrap.wrap("(" + english + ")", 50)), fontsize=6.6,
                color=MUTED, va="top", style="italic", linespacing=1.25)
    save(fig, "instructions-completions")


# --- Figure 2: a conversation is one token sequence ---

CHAT_W, CHAT_X = 7.2, 104.0      # figure width in inches, x range in data units


def text_width(text, size, italic=False):
    """Width of a string in data units of the chat figure, measured from the glyphs."""
    prop = FontProperties(family="DejaVu Sans", style="italic" if italic else "normal")
    pts = TextPath((0, 0), text, size=size, prop=prop).get_extents().width
    return pts / (CHAT_W * 72 / CHAT_X)


def token_row(ax, x0, y, items, h=5.0, gap=0.5):
    """Draw a row of boxes. items: (text, kind) with kind 'special', 'role', 'text' or 'open'."""
    x = x0
    for text, kind in items:
        size = 6.4 if kind == "special" else 6.9
        w = text_width(text, size, kind == "open") + 2.0
        if kind == "special":
            face, edge, color = WARMFILL, WARM, WARM
        elif kind == "role":
            face, edge, color = LIGHT, ACCENT, INK
        elif kind == "open":
            face, edge, color = "white", ACCENT, ACCENT
        else:
            face, edge, color = "white", MUTED, INK
        ls = "--" if kind == "open" else "-"
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.8",
                                    facecolor=face, edgecolor=edge, linewidth=0.8, linestyle=ls))
        ax.text(x + w / 2, y + h / 2, text, fontsize=size, color=color, ha="center", va="center",
                style="italic" if kind == "open" else "normal")
        x += w + gap
    return x


def chat_figure():
    fig, ax = plt.subplots(figsize=(CHAT_W, 4.1))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)   # so text_width() is exact
    ax.set_xlim(0, CHAT_X)
    ax.set_ylim(0, 72)
    ax.axis("off")
    ax.text(0, 70.5, "(a) Llama 3 (2024): markers are special tokens with IDs of their own",
            fontsize=8.5, color=INK, va="top", fontweight="bold")
    rows = [
        [("<|begin_of_text|>", "special"), ("<|start_header_id|>", "special"), ("system", "role"),
         ("<|end_header_id|>", "special"), ("Answer in one sentence.", "text"), ("<|eot_id|>", "special")],
        [("<|start_header_id|>", "special"), ("user", "role"), ("<|end_header_id|>", "special"),
         ("Why is the sky blue?", "text"), ("<|eot_id|>", "special")],
        [("<|start_header_id|>", "special"), ("assistant", "role"), ("<|end_header_id|>", "special"),
         ("the model writes here, then <|eot_id|>", "open")],
    ]
    y = 59
    for i, items in enumerate(rows):
        x0 = 0 if i == 0 else 14.0
        token_row(ax, x0, y, items)
        y -= 7.5
    ax.text(0, y + 3.2, "The three rows are one sequence; it is broken here only to fit the page.",
            fontsize=6.8, color=MUTED, va="top")
    ax.text(0, 30.5, "(b) Llama 2 (2023): markers are ordinary text, tokenized like any other words",
            fontsize=8.5, color=INK, va="top", fontweight="bold")
    items = [("<s>", "special"), ("[INST]", "text"), ("<<SYS>>", "text"), ("Answer in one sentence.", "text"),
             ("<</SYS>>", "text"), ("Why is the sky blue?", "text"), ("[/INST]", "text"),
             ("the model writes here", "open")]
    token_row(ax, 0, 19, items)
    ax.text(0, 15.2, "The system text is folded into the first user message. Because \"[INST]\" and \"<<SYS>>\" "
            "are plain text,\nMeta's code refuses any message that contains them.",
            fontsize=6.8, color=MUTED, va="top")
    # legend
    lx, ly = 0, 2.5
    for label, face, edge in (("special token (one vocabulary ID)", WARMFILL, WARM),
                              ("role name, ordinary text", LIGHT, ACCENT),
                              ("message text, ordinary text", "white", MUTED)):
        ax.add_patch(FancyBboxPatch((lx, ly), 3.0, 3.0, boxstyle="round,pad=0,rounding_size=0.5",
                                    facecolor=face, edgecolor=edge, linewidth=0.8))
        ax.text(lx + 4.0, ly + 1.5, label, fontsize=7, color=INK, va="center")
        lx += 34
    save(fig, "instructions-chat")


# --- Figure 3: InstructGPT's three steps ---

def steps_figure():
    sft = C.SFT_LABELER + C.SFT_CUSTOMER
    rm = C.RM_LABELER + C.RM_CUSTOMER
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 64)
    ax.axis("off")
    cols = [
        ("1. Supervised fine-tuning",
         "A labeler writes the answer\nthey want for a prompt",
         "GPT-3 is trained further on\nthese demonstrations,\nwith the ordinary\nnext-token loss",
         f"{sft:,} prompts (about 13k),\nmostly written by labelers;\n16 epochs"),
        ("2. Reward model",
         "Models write 4 to 9 answers\nto a prompt; a labeler ranks\nthem from best to worst",
         "A 6B network learns to give\neach answer a score, so that\npreferred answers score\nhigher (Bradley-Terry)",
         f"{rm:,} prompts (about 33k),\nmostly from API customers;\n6 to 36 pairs per prompt"),
        ("3. Reinforcement learning",
         "The model answers a new\nprompt; the reward model\nscores the answer",
         "PPO nudges the model toward\nhigher scores, minus a penalty\nfor drifting from the SFT\nmodel, plus pretraining text",
         f"{C.PPO_CUSTOMER:,} prompts (about 31k),\nall from API customers;\n256k episodes"),
    ]
    w, gapx = 29.0, 6.0
    for i, (title, a, b, counts) in enumerate(cols):
        x = 1 + i * (w + gapx)
        box(ax, x, 55, w, 7.5, ACCENT, ACCENT)
        ax.text(x + w / 2, 58.75, title, fontsize=7.4, color="white", ha="center", va="center",
                fontweight="bold")
        box(ax, x, 39.5, w, 12.5, LIGHT, ACCENT)
        ax.text(x + w / 2, 45.75, a, fontsize=7.2, color=INK, ha="center", va="center")
        box(ax, x, 18.5, w, 16, "white", ACCENT)
        ax.text(x + w / 2, 26.5, b, fontsize=7.2, color=INK, ha="center", va="center")
        ax.add_patch(FancyArrowPatch((x + w / 2, 39.3), (x + w / 2, 34.7), arrowstyle="-|>",
                                     mutation_scale=9, color=MUTED, linewidth=0.8))
        ax.text(x + w / 2, 15.5, counts, fontsize=6.8, color=MUTED, ha="center", va="top")
        if i < 2:
            ax.add_patch(FancyArrowPatch((x + w + 0.3, 26.5), (x + w + gapx - 0.3, 26.5), arrowstyle="-|>",
                                         mutation_scale=9, color=WARM, linewidth=1.0))
    for i, label in enumerate(("starts\nfrom\nSFT", "used\nto\nscore")):
        xm = 1 + (i + 1) * w + i * gapx + gapx / 2
        ax.text(xm, 25.0, label, fontsize=5.8, color=WARM, ha="center", va="top")
    ax.text(1, 3.0, "Labels by about 40 contractors. The penalty uses β = 0.02. Counts are training prompts "
            "from the paper's Table 6.", fontsize=6.8, color=MUTED, va="center")
    save(fig, "instructions-steps")


# --- Figure 4: the Bradley-Terry curve ---

def bradley_terry_figure():
    import math
    fig, ax = plt.subplots(figsize=(6.0, 2.9))
    xs = [i / 50 for i in range(-200, 201)]
    ax.plot(xs, [C.sigmoid(x) for x in xs], color=ACCENT, linewidth=1.6)
    ax.axhline(0.5, color=GRID, linewidth=0.7, zorder=0)
    ax.axvline(0.0, color=GRID, linewidth=0.7, zorder=0)
    for d in (-1.0, 0.0, 1.0, 2.0):
        p = C.sigmoid(d)
        ax.plot([d], [p], "o", color=WARM, markersize=4.5, zorder=3)
        ax.text(d + 0.15, p - 0.07, f"{d:+g}: {p:.3f}" if d else f"0: {p:.3f}", fontsize=7.5, color=WARM, ha="left", va="center")
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 1)
    ax.set_xlabel("difference in reward-model scores, $r_A - r_B$", fontsize=8, color=INK)
    ax.set_ylabel("probability A is preferred", fontsize=8, color=INK)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)
    sec = ax.secondary_xaxis("top", functions=(lambda d: d * C.ELO_PER_UNIT, lambda e: e / C.ELO_PER_UNIT))
    sec.set_xticks([-600, -400, -200, 0, 200, 400, 600])
    sec.set_xlabel(f"the same difference in chess Elo points ({C.ELO_PER_UNIT:.1f} per unit)",
                   fontsize=7.5, color=MUTED)
    sec.tick_params(colors=MUTED, length=0, labelsize=7)
    sec.spines["top"].set_color(GRID)
    assert abs(C.elo_win(174) - C.sigmoid(1)) < 1e-3 and math.isclose(C.sigmoid(0), 0.5)
    save(fig, "instructions-bradley-terry")


if __name__ == "__main__":
    completions_figure()
    chat_figure()
    steps_figure()
    bradley_terry_figure()
