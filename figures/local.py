#!/usr/bin/env python3
"""Figures for Book 1, chapter `local` [D-014].

Run: python3 figures/local.py
Writes local-memory.svg, local-groups.svg and local-bandwidth.svg next to this
script. Numbers come from code/checks/local.py [D-009].
"""
import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402

OUT = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "local_checks", OUT.parent / "code" / "checks" / "local.py")
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
BAD = 0.03   # errors above this are drawn in the warm colour

# Memory bands for the heat map: weights only, against memory sizes the
# chapter names (16 and 32 GB GPUs and laptops; 64 and 128 GB Macs).
BANDS = [
    (16, "up to 16 GB", "#e8f0f8"),
    (32, "16 to 32 GB", "#b9d0e8"),
    (64, "32 to 64 GB", "#7fa9d3"),
    (128, "64 to 128 GB", "#3f78b0"),
    (float("inf"), "over 128 GB", "#1f4a75"),
]


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {path}")


def band(gb):
    for i, (limit, _, color) in enumerate(BANDS):
        if gb <= limit:
            return i, color
    raise ValueError(gb)


def memory_figure():
    tab = C.weights_table()
    models, types = C.TABLE_MODELS, C.TABLE_TYPES
    fig = plt.figure(figsize=(7.0, 5.6))
    ax = fig.add_axes([0.16, 0.42, 0.82, 0.52])
    for r, m in enumerate(models):
        for c, t in enumerate(types):
            gb = tab[m][t]
            i, color = band(gb)
            ax.add_patch(Rectangle((c, r), 1, 1, facecolor=color, edgecolor="white", linewidth=1.5))
            text = f"{gb:.1f}" if gb < 100 else f"{gb:.0f}"
            ax.text(c + 0.5, r + 0.5, text, ha="center", va="center", fontsize=8,
                    color="white" if i >= 3 else INK)
    ax.set_xlim(0, len(types))
    ax.set_ylim(len(models), 0)
    ax.set_xticks([c + 0.5 for c in range(len(types))])
    ax.set_xticklabels([f"{t}\n{C.BITS[t]:.2f} bits" for t in types], fontsize=7.5, color=INK)
    ax.xaxis.tick_top()
    ax.set_yticks([r + 0.5 for r in range(len(models))])
    ax.set_yticklabels([f"{m}\n{C.PARAMS[m] / 1e9:.2f} billion" for m in models], fontsize=7.5, color=INK)
    ax.tick_params(length=0)
    for side in ax.spines.values():
        side.set_visible(False)
    ax.set_title("(a) Weights only, GB, by model and llama.cpp type", fontsize=8.5, color=INK, loc="left", pad=30)
    handles = [Patch(facecolor=color, edgecolor=GRID, label=label) for _, label, color in BANDS]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, -0.02), ncol=5, fontsize=7, frameon=False)

    # (b) weights at Q4_K_M plus the 16-bit cache at 8K and 32K tokens.
    bx = fig.add_axes([0.16, 0.05, 0.82, 0.24])
    tot = C.totals()
    names = list(tot)
    for row, m in enumerate(names):
        w, k8, k32 = tot[m]
        bx.barh(row, w, height=0.55, color=ACCENT, label="weights (Q4_K_M)" if row == 0 else None)
        bx.barh(row, k8, left=w, height=0.55, color=WARM, label="KV cache, first 8K tokens" if row == 0 else None)
        bx.barh(row, k32 - k8, left=w + k8, height=0.55, color=WARMFILL, edgecolor=WARM, linewidth=0.6,
                label="KV cache, 8K to 32K tokens" if row == 0 else None)
        bx.text(w + k32 + 0.8, row, f"{w + k8:.1f} GB at 8K, {w + k32:.1f} GB at 32K",
                va="center", fontsize=7.5, color=INK)
    bx.set_yticks(range(len(names)))
    bx.set_yticklabels(names, fontsize=7.5, color=INK)
    bx.invert_yaxis()
    bx.set_xlim(0, 80)
    bx.set_xlabel("GB (16-bit cache; no allowance for the runtime's working memory)", fontsize=7.5, color=MUTED)
    for side in ("top", "right", "left"):
        bx.spines[side].set_visible(False)
    bx.spines["bottom"].set_color(GRID)
    bx.tick_params(colors=MUTED, length=0, labelsize=7.5)
    bx.legend(loc="upper right", fontsize=7, frameon=False)
    bx.set_title("(b) Weights at Q4_K_M plus the KV cache", fontsize=8.5, color=INK, loc="left")
    save(fig, "local-memory")


def groups_figure():
    cases = C.demo_cases()
    fig, ax = plt.subplots(figsize=(7.0, 3.3))
    cw, ch, gap = 0.78, 0.5, 1.5
    titles = {
        "no outlier": "(a) Eight weights, one shared scale",
        "outlier, one scale": "(b) The last weight 20 times larger, one shared scale",
        "outlier kept aside": "(c) The large weight kept aside in 16 bits, the rest with their own scale",
    }
    for row, (name, (ws, s, q, r)) in enumerate(cases.items()):
        y = -row * gap
        ax.text(0, y + ch + 0.33, titles[name], fontsize=8, color=INK, va="bottom")
        for i, (w, x, rec) in enumerate(zip(ws, q, r)):
            x0 = i * (cw + 0.08)
            aside = x is None
            err = abs(w - rec)
            fill = GREY if aside else (WARMFILL if err > BAD else LIGHT)
            ax.add_patch(Rectangle((x0, y), cw, ch, facecolor=fill, edgecolor=MUTED, linewidth=0.6))
            ax.text(x0 + cw / 2, y + ch + 0.05, f"{w:g}", ha="center", va="bottom", fontsize=7.5, color=INK)
            ax.text(x0 + cw / 2, y + ch / 2, "16-bit" if aside else f"{x:+d}", ha="center", va="center",
                    fontsize=8 if not aside else 7, color=INK)
            ax.text(x0 + cw / 2, y - 0.05, f"{rec:.3f}", ha="center", va="top", fontsize=7,
                    color=WARM if err > BAD else MUTED)
        right = 8 * (cw + 0.08) + 0.15
        ax.text(right, y + ch / 2 + 0.12, f"scale {s:.4f}", fontsize=7.5, color=INK, va="center")
        ax.text(right, y + ch / 2 - 0.18, f"mean error on the\nfirst seven {C.mean_abs_err(ws, r):.3f}",
                fontsize=7.5, color=WARM if C.mean_abs_err(ws, r) > BAD else INK, va="center")
    ax.text(-0.05, 0.25, "weight\nstored\nrebuilt", fontsize=6.5, color=MUTED, ha="right", va="center")
    ax.set_xlim(-0.75, 8 * (cw + 0.08) + 1.9)
    ax.set_ylim(-2 * gap - 0.4, ch + 0.75)
    ax.axis("off")
    save(fig, "local-groups")


def bandwidth_figure():
    w = C.weights_table()["Llama 3.1 8B"]["Q4_K_M"]
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    names = [d[0] for d in C.DEVICES]
    for row, (name, bw, _) in enumerate(C.DEVICES):
        bound = bw / w
        ax.barh(row, bound, height=0.55, color=LIGHT, edgecolor=ACCENT, linewidth=0.6)
        ax.text(bound + 4, row, f"{bound:.0f} ({bw:g} GB/s)", va="center", fontsize=7.5, color=INK)
    # The one measurement whose hardware is named: llama-bench's RTX 4080 example.
    size = 4_677_120_000 / C.GB
    row = names.index("NVIDIA RTX 4080")
    ax.plot([119.92], [row + 0.42], marker="o", color=WARM, markersize=5, linestyle="none")
    ax.text(119.92 + 4, row + 0.42,
            f"measured 119.9 for Qwen2.5-7B Q4_K_M ({size:.2f} GB; its bound {716.8 / size:.0f})",
            va="center", fontsize=7, color=WARM)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=7.5, color=INK)
    ax.set_ylim(len(names) - 0.4, -0.6)
    ax.set_xlim(0, 440)
    ax.set_xlabel(f"Upper bound on tokens per second for Llama 3.1 8B at Q4_K_M ({w:.2f} GB): "
                  "peak bandwidth / bytes per token", fontsize=7.5, color=MUTED)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=7.5)
    save(fig, "local-bandwidth")


if __name__ == "__main__":
    memory_figure()
    groups_figure()
    bandwidth_figure()
