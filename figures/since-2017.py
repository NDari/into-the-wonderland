#!/usr/bin/env python3
"""Figures for Book 1, chapter `since-2017` [D-014].

Run: python3 figures/since-2017.py
Writes since-2017-blocks.svg, since-2017-positions.svg and since-2017-moe.svg
next to this script. Shapes and numbers come from code/checks/since-2017.py
[D-009]; the block drawing reuses the box, arrow and plus helpers of
figures/anatomy.py so the two figures match.
"""
import importlib.util
import math
import random
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Arc, FancyBboxPatch, Rectangle  # noqa: E402

OUT = Path(__file__).parent


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C = _load("since_2017_checks", OUT.parent / "code" / "checks" / "since-2017.py")

plt.rcParams["svg.hashsalt"] = "into-the-wonderland"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5

INK = "#222222"
MUTED = "#666666"
GRID = "#d0d0d0"
ACCENT = "#2f6fae"
FILL = "#dbe7f3"
PLAIN = "#f4f4f4"
WARM = "#b5523b"
WARMFILL = "#f3dcd6"
GREY = "#e4e4e4"


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


# The same three helpers as figures/anatomy.py, with a zorder so boxes sit on the stream line.
def box(ax, x, y, w, h, text, face=FILL, edge=ACCENT, size=7.5):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=face, edgecolor=edge, linewidth=0.8, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=INK, zorder=4)


def arrow(ax, x0, y0, x1, y1, color=MUTED, lw=0.9):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=lw, shrinkA=0, shrinkB=0,
                                mutation_scale=7))


def plus(ax, x, y):
    ax.add_patch(plt.Circle((x, y), 0.13, facecolor="white", edgecolor=ACCENT, linewidth=1.0, zorder=4))
    ax.text(x, y, "+", ha="center", va="center", fontsize=9, color=ACCENT, zorder=5)


def stream(ax, x, y0, y1):
    ax.plot([x, x], [y0, y1], color=ACCENT, linewidth=5, alpha=0.35, solid_capstyle="butt", zorder=1)


def blocks_figure():
    b, L = C.BASE_2017, C.LLAMA3_8B
    fig, ax = plt.subplots(figsize=(7.2, 6.4))
    # Left column: the 2017 encoder block, post-norm.
    sx, bx = 0.9, 3.1
    ax.text(2.0, 7.35, "2017: Transformer base\n(one encoder block)", ha="center", va="center", fontsize=8.5,
            color=INK, fontweight="bold")
    box(ax, sx + 0.9, 0.0, 3.4, 0.5, "token vectors + sine-wave\npositions, added once here", face=PLAIN,
        edge="#999999")
    stream(ax, sx, 0.25, 6.9)

    def post_sublayer(base, text, h):
        ax.plot([sx, bx], [base, base], color=MUTED, linewidth=0.9)
        top = base + 0.35 + h + 0.3
        arrow(ax, bx, base, bx, base + 0.35)
        box(ax, bx, base + 0.35 + h / 2, 2.5, h, text)
        ax.plot([bx, bx], [base + 0.35 + h, top], color=MUTED, linewidth=0.9)
        arrow(ax, bx, top, sx + 0.13, top)
        plus(ax, sx, top)
        box(ax, sx, top + 0.5, 1.3, 0.34, "LayerNorm", face=PLAIN, edge="#999999", size=7)
        return top + 0.5

    y = post_sublayer(0.75, f"multi-head attention\n{b['heads']} heads of {b['head_dim']}, each with\n"
                            "its own keys and values", 0.85)
    y = post_sublayer(y + 0.55, f"feed-forward network\n{b['d']} \u2192 {b['ff']:,} \u2192 {b['d']}\nReLU", 0.85)
    ax.add_patch(Rectangle((0.05, 0.55), 4.55, 6.0, fill=False, edgecolor="#bbbbbb", linewidth=0.8,
                           linestyle="--"))
    ax.text(4.55, 0.5, f"repeated {b['layers']} times", ha="right", va="top", fontsize=7, color=MUTED)
    ax.text(sx - 0.25, 1.5, "residual\nstream", ha="right", va="center", fontsize=7, color=ACCENT)

    # Right column: Llama 3 8B, pre-norm with RMSNorm.
    ox = 5.4
    sx, bx = ox + 0.9, ox + 3.25
    ax.text(ox + 2.1, 7.35, "2024: Llama 3 8B\n(one block)", ha="center", va="center", fontsize=8.5,
            color=INK, fontweight="bold")
    box(ax, sx + 0.9, 0.0, 3.4, 0.5, "token vectors\n(no position table)", face=PLAIN, edge="#999999")
    stream(ax, sx, 0.25, 6.45)

    def pre_sublayer(base, text, h):
        ax.plot([sx, bx], [base, base], color=MUTED, linewidth=0.9)
        arrow(ax, bx, base, bx, base + 0.2)
        box(ax, bx, base + 0.37, 1.3, 0.34, "RMSNorm", face=WARMFILL, edge=WARM, size=7)
        arrow(ax, bx, base + 0.54, bx, base + 0.7)
        box(ax, bx, base + 0.7 + h / 2, 2.75, h, text, face=WARMFILL, edge=WARM)
        top = base + 0.7 + h + 0.25
        ax.plot([bx, bx], [base + 0.7 + h, top], color=MUTED, linewidth=0.9)
        arrow(ax, bx, top, sx + 0.13, top)
        plus(ax, sx, top)
        return top

    y = pre_sublayer(0.75, f"grouped-query attention\n{L['heads']} query heads share\n{L['kv_heads']} key-value heads "
                           f"of {L['head_dim']};\nrotary positions on\nqueries and keys", 1.25)
    pre_sublayer(y + 0.35, f"SwiGLU feed-forward\n{L['d']:,} \u2192 2 x {L['ff']:,} \u2192 {L['d']:,}", 0.75)
    ax.add_patch(Rectangle((ox + 0.05, 0.55), 4.75, 5.6, fill=False, edgecolor="#bbbbbb", linewidth=0.8,
                           linestyle="--"))
    ax.text(ox + 4.8, 0.5, f"repeated {L['layers']} times", ha="right", va="top", fontsize=7, color=MUTED)
    box(ax, sx + 0.3, 6.65, 2.5, 0.34, "final RMSNorm (once)", face=WARMFILL, edge=WARM, size=7)
    ax.text(sx - 0.25, 1.6, "residual\nstream:\nnever\nnormalized", ha="right", va="center", fontsize=7,
            color=ACCENT)
    ax.set_xlim(-0.6, 10.4)
    ax.set_ylim(-0.4, 7.7)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "since-2017-blocks")


def positions_figure():
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7), gridspec_kw=dict(width_ratios=[1, 1, 1.15]))
    for ax, (m, n) in zip(axes[:2], ((3, 1), (10, 8))):
        q = C.rotate(C.ROPE_Q, m * C.ROPE_STEP)
        k = C.rotate(C.ROPE_K, n * C.ROPE_STEP)
        ax.add_patch(plt.Circle((0, 0), 3.3, fill=False, edgecolor=GRID, linewidth=0.6))
        ax.plot([-3.4, 3.4], [0, 0], color=GRID, linewidth=0.5)
        ax.plot([0, 0], [-3.4, 3.4], color=GRID, linewidth=0.5)
        for v, col, lab in ((q, ACCENT, f"query,\nposition {m}"), (k, WARM, f"key,\nposition {n}")):
            ax.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, linewidth=1.4,
                                                                 mutation_scale=9, shrinkA=0, shrinkB=0))
            r = math.hypot(*v)
            ax.text(v[0] * (r + 1.25) / r, v[1] * (r + 1.25) / r, lab, ha="center", va="center", fontsize=7,
                    color=col)
        aq = math.degrees(math.atan2(q[1], q[0])) % 360
        ak = math.degrees(math.atan2(k[1], k[0])) % 360
        lo, hi = (ak, aq) if (aq - ak) % 360 <= 180 else (aq, ak)
        ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=lo, theta2=hi if hi > lo else hi + 360, color=INK,
                         linewidth=0.8))
        gap = (aq - ak) % 360
        gap = min(gap, 360 - gap)
        ax.set_title(f"gap {m - n}: angle {gap:.0f}\u00b0, score {C.rope_score(m, n):.2f}", fontsize=7.5,
                     color=INK)
        ax.set_xlim(-4.4, 4.4)
        ax.set_ylim(-4.4, 4.4)
        ax.set_aspect("equal")
        ax.axis("off")
    ax = axes[2]
    slope, n = 0.5, 5
    for i in range(n):
        for j in range(n):
            if j <= i:
                v = -slope * (i - j)
                shade = 1 - (-v + 0.3) / 2.9
                face = (0.184 + (1 - 0.184) * shade, 0.435 + (1 - 0.435) * shade, 0.682 + (1 - 0.682) * shade)
                ax.add_patch(Rectangle((j, n - 1 - i), 0.92, 0.92, facecolor=face, edgecolor="none"))
                ax.text(j + 0.46, n - 1 - i + 0.46, f"{v + 0.0:.1f}", ha="center", va="center", fontsize=7,
                        color="white" if -v >= 1.5 else INK)
            else:
                ax.add_patch(Rectangle((j, n - 1 - i), 0.92, 0.92, facecolor="#eeeeee", edgecolor="none"))
        ax.text(-0.15, n - 1 - i + 0.46, f"{i + 1}", ha="right", va="center", fontsize=7, color=MUTED)
        ax.text(i + 0.46, n + 0.1, f"{i + 1}", ha="center", va="bottom", fontsize=7, color=MUTED)
    ax.text(n / 2, n + 0.65, "key position", ha="center", va="bottom", fontsize=7, color=MUTED)
    ax.text(-0.75, n / 2, "query position", ha="center", va="center", fontsize=7, color=MUTED, rotation=90)
    ax.text(n / 2, -0.3, f"ALiBi bias added to each score\n(slope {slope}; grey: masked)", ha="center", va="top",
            fontsize=7.5, color=INK)
    ax.set_xlim(-1.1, n + 0.1)
    ax.set_ylim(-1.4, n + 1.2)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "since-2017-positions")


def moe_figure():
    s = C.ROUTER_SCORES
    top = sorted(range(len(s)), key=lambda i: -s[i])[:2]
    w = C.softmax([s[i] if i in top else -math.inf for i in range(len(s))])
    total, *_ = C.mixtral_counts(C.MIXTRAL["experts"])
    active, *_ = C.mixtral_counts(C.MIXTRAL["top_k"])
    fig = plt.figure(figsize=(7.2, 4.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 1.7], height_ratios=[2.2, 1], hspace=0.55, wspace=0.15)
    # (a) router scores.
    ax = fig.add_subplot(gs[0, 0])
    xs = range(1, len(s) + 1)
    ax.bar(xs, s, color=[ACCENT if i in top else GREY for i in range(len(s))], width=0.7)
    ax.axhline(0, color=MUTED, linewidth=0.6)
    for i in top:
        ax.text(i + 1, s[i] + 0.12, f"weight\n{w[i]:.3f}", ha="center", va="bottom", fontsize=6.5, color=ACCENT)
    ax.set_xticks(list(xs))
    ax.set_xlabel("expert", fontsize=7.5, color=MUTED)
    ax.set_ylabel("router score (made up)", fontsize=7.5, color=MUTED)
    ax.set_ylim(-1.4, 3.3)
    ax.tick_params(labelsize=7, colors=MUTED)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.set_title("(a) router keeps the top 2 of 8", fontsize=7.5, color=INK)
    # (b) the flow for one token.
    ax = fig.add_subplot(gs[0, 1])
    sx = 0.3
    stream(ax, sx, -0.2, 4.2)
    ax.text(sx + 0.15, -0.25, "residual stream\n(one token)", ha="left", va="top", fontsize=7, color=ACCENT)
    ax.plot([sx, 1.4], [0.6, 0.6], color=MUTED, linewidth=0.9)
    box(ax, 2.1, 0.6, 1.4, 0.36, "RMSNorm", face=PLAIN, edge="#999999", size=7)
    box(ax, 3.75, 0.6, 1.1, 0.36, "router", face=PLAIN, edge="#999999", size=7)
    arrow(ax, 2.82, 0.6, 3.18, 0.6)
    ex = [1.0 + 0.82 * i for i in range(8)]
    for i, x in enumerate(ex):
        on = i in top
        box(ax, x, 2.0, 0.68, 0.5, f"E{i + 1}", face=FILL if on else GREY, edge=ACCENT if on else "#bbbbbb",
            size=7)
        if on:
            arrow(ax, 3.75, 0.78, x, 1.75, color=ACCENT)
            arrow(ax, x, 2.25, 4.0, 3.15, color=ACCENT)
            ax.text((x + 4.0) / 2 + (0.5 if x > 4 else -0.5), 2.8, f"x {w[i]:.3f}", ha="center",
                    va="center", fontsize=6.5, color=ACCENT)
    box(ax, 4.0, 3.4, 2.1, 0.4, "weighted sum", size=7)
    arrow(ax, 2.95, 3.4, sx + 0.13, 3.4)
    plus(ax, sx, 3.4)
    ax.text(7.6, -0.45, f"Mixtral 8x7B:\n{total / 1e9:.1f}B parameters in all,\n{active / 1e9:.1f}B used per token",
            ha="right", va="center", fontsize=7, color=INK)
    ax.set_xlim(-0.2, 7.7)
    ax.set_ylim(-0.9, 4.3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(b) only the chosen experts run", fontsize=7.5, color=INK)
    # (c) DeepSeek-V3's layout: 1 shared expert and 8 of 256 routed experts (positions illustrative).
    ax = fig.add_subplot(gs[1, :])
    rng = random.Random(3)
    lit = set(rng.sample(range(256), 8))
    ax.add_patch(Rectangle((3.5, 1.35), 0.36, 0.8, facecolor=WARM, edgecolor="none"))
    ax.text(3.3, 1.75, "1 shared expert\n(every token)", ha="right", va="center", fontsize=6.5, color=INK)
    for idx in range(256):
        r, c = divmod(idx, 64)
        ax.add_patch(Rectangle((4.5 + c * 0.42, 2.7 - r * 0.9), 0.36, 0.8,
                               facecolor=ACCENT if idx in lit else GREY, edgecolor="none"))
    ax.text(4.5, -0.35, "256 routed experts, 8 chosen per token (which 8 is illustrative); "
                        "every expert, shared or routed, has the same size", ha="left", va="top", fontsize=7, color=MUTED)
    ax.set_title("(c) DeepSeek-V3 (2024): many small experts", fontsize=7.5, color=INK, loc="left")
    ax.set_xlim(-0.1, 4.5 + 64 * 0.42 + 0.1)
    ax.set_ylim(-1.0, 3.7)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "since-2017-moe")


if __name__ == "__main__":
    blocks_figure()
    positions_figure()
    moe_figure()
