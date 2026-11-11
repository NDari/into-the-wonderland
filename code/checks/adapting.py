#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `adapting` [D-009].

Run: python3 code/checks/adapting.py
Uses numpy for the singular value decomposition in Example 2; everything else
is plain arithmetic on numbers printed in the sources (see
book1/sources/adapting.md, "Mechanism claims to check numerically").
"""
import math

import numpy as np

# Llama 3 8B shapes (Llama 3 paper, Table 3) and its parameter count, as
# computed in code/checks/anatomy.py, Example 3.
D_MODEL, LAYERS, FFN, KV = 4096, 32, 14336, 8 * 128
N_8B = 8_028_164_096
GB = 1e9


def lora_count(d, k, r):
    """Trainable numbers in a rank-r update B A of a d x k matrix."""
    return r * (d + k)


def example_lora_matrix():
    print("Example 1: one 4,096 x 4,096 weight matrix and a low-rank update")
    full = D_MODEL * D_MODEL
    print(f"  full matrix: {full:,} weights")
    for r in (1, 4, 8, 16, 64):
        n = lora_count(D_MODEL, D_MODEL, r)
        print(f"  rank {r}: B is {D_MODEL:,} x {r}, A is {r} x {D_MODEL:,}: {n:,} numbers "
              f"({n / full:.3%}; 1/{full // n})")
    print(f"  break-even rank for a square 4,096 matrix: {D_MODEL * D_MODEL // (2 * D_MODEL):,}")
    print()


def example_svd():
    print("Example 2: the best low-rank approximation (Eckart and Young), on a made-up 8 x 6 matrix")
    rng = np.random.default_rng(1936)
    sv = np.array([10.0, 5.0, 1.0, 0.5, 0.2, 0.1])
    u, _ = np.linalg.qr(rng.standard_normal((8, 6)))
    v, _ = np.linalg.qr(rng.standard_normal((6, 6)))
    m = u @ np.diag(sv) @ v.T
    s = np.linalg.svd(m, compute_uv=False)
    print("  singular values: " + ", ".join(f"{x:g}" for x in s))
    total = float((s ** 2).sum())
    U, S, Vt = np.linalg.svd(m, full_matrices=False)
    for k in (1, 2, 3):
        approx = U[:, :k] @ np.diag(S[:k]) @ Vt[:k]
        err = float(np.linalg.norm(m - approx))
        dropped = math.sqrt(float((S[k:] ** 2).sum()))
        b = U[:, :k] * S[:k]          # 8 x k
        a = Vt[:k]                    # k x 6
        assert np.allclose(b @ a, approx)
        print(f"  rank {k}: keeps {float((S[:k] ** 2).sum()) / total:.2%} of the squared size; "
              f"error {err:.3f} = square root of the dropped squares {dropped:.3f}; "
              f"stored as {b.shape[0]} x {k} times {k} x {a.shape[1]}: {k * (8 + 6)} numbers instead of 48")
    # A random rank-2 subspace for comparison: project the rows onto it.
    q, _ = np.linalg.qr(rng.standard_normal((6, 2)))
    rand = m @ q @ q.T
    print(f"  a random rank-2 approximation of the same kind: error {float(np.linalg.norm(m - rand)):.2f}")
    print(f"  size of the whole matrix: {math.sqrt(total):.3f}")
    print()


def example_whole_model():
    print("Example 3: LoRA counted over whole models")
    per_rank_gpt3 = 96 * 2 * (12288 + 12288)
    for r in (1, 4, 8):
        print(f"  GPT-3 175B, queries and values in 96 layers, rank {r}: {per_rank_gpt3 * r:,}")
    print(f"  175,255.8M / {per_rank_gpt3 * 4 / 1e6:.2f}M = {175255.8e6 / (per_rank_gpt3 * 4):,.0f}; "
          f"350 GB / 35 MB = {350e9 / 35e6:,.0f}; {per_rank_gpt3 * 4 / 1e6:.2f}M x 2 bytes = "
          f"{per_rank_gpt3 * 4 * 2 / 1e6:.1f} MB")
    print(f"  100 adapted copies: 350 GB + 100 x 35 MB = {350 + 100 * 0.035:.1f} GB vs 100 x 350 GB = "
          f"{100 * 350 / 1000:.0f} TB")
    per_layer = (lora_count(D_MODEL, D_MODEL, 1) * 2          # queries, output
                 + lora_count(D_MODEL, KV, 1) * 2              # keys, values
                 + lora_count(D_MODEL, FFN, 1) * 3)            # gate, up, down
    per_rank = per_layer * LAYERS
    print(f"  Llama 3 8B, every linear layer in the 32 blocks: {per_layer:,} per layer per unit of rank; "
          f"{per_rank:,} per unit of rank")
    for r in (8, 16, 64):
        print(f"    rank {r}: {per_rank * r:,} ({per_rank * r / N_8B:.2%} of {N_8B:,})")
    print()


QLORA_BITS = 4 + 8 / 64 + 32 / (64 * 256)   # NF4 plus double-quantized constants
LORA_RANK = 16
LORA_N = 2_621_440 * LORA_RANK                # every linear layer of Llama 3 8B (Example 3)


def memory_parts():
    """GB for each part of the memory bill, used by figures/adapting.py."""
    return {
        "full fine-tuning": [("16-bit weights", 2 * N_8B / GB), ("gradients", 2 * N_8B / GB),
                             ("32-bit copy and Adam state", 12 * N_8B / GB)],
        "LoRA, rank 16": [("16-bit weights", 2 * N_8B / GB), ("adapters, with their gradients and state", 16 * LORA_N / GB)],
        "QLoRA, rank 16": [("4-bit weights", N_8B * QLORA_BITS / 8 / GB),
                           ("adapters, with their gradients and state", 16 * LORA_N / GB)],
    }


def example_memory():
    print("Example 4: memory to adapt Llama 3 8B (weights and optimizer only; activations not counted)")
    full = 16 * N_8B
    print(f"  full fine-tuning at 16 bytes per parameter: {full / GB:.1f} GB")
    lora_n = LORA_N
    frozen16 = 2 * N_8B
    adapters = 16 * lora_n
    print(f"  LoRA, rank 16 on every linear layer: frozen 16-bit weights {frozen16 / GB:.2f} GB + "
          f"{lora_n:,} trainable at 16 bytes {adapters / GB:.2f} GB = {(frozen16 + adapters) / GB:.1f} GB")
    bits = QLORA_BITS
    q = N_8B * bits / 8
    print(f"  QLoRA: 4-bit weights plus {bits - 4:.3f} bits of scale constants = {bits:.3f} bits; "
          f"weights {q / GB:.2f} GB + adapters {adapters / GB:.2f} GB = {(q + adapters) / GB:.1f} GB")
    emb = 2 * 128000 * D_MODEL
    q2 = (N_8B - emb) * bits / 8 + emb * 2
    print(f"  (if the {emb:,} embedding and output parameters stayed in 16 bits: "
          f"{(q2 + adapters) / GB:.1f} GB)")
    print(f"  ratio full / LoRA {full / (frozen16 + adapters):.1f}; full / QLoRA {full / (q + adapters):.0f}")
    for name, parts in memory_parts().items():
        print(f"  {name}: " + " + ".join(f"{v:.2f}" for _, v in parts) + f" = {sum(v for _, v in parts):.1f} GB")
    print()


def example_qlora_numbers():
    print("Example 5: QLoRA's printed arithmetic")
    print(f"  constants: 32/64 = {32 / 64:.3f} bits; with double quantization 8/64 + 32/(64 x 256) = "
          f"{8 / 64 + 32 / (64 * 256):.3f}; saving {32 / 64 - (8 / 64 + 32 / (64 * 256)):.3f} bits")
    print(f"  65B x 0.373 bits = {65e9 * 0.373 / 8 / GB:.2f} GB saved; 65B at 4.127 bits = "
          f"{65e9 * 4.127 / 8 / GB:.1f} GB")
    print(f"  780 GB / 65B = {780 / 65:.1f} bytes per parameter; 16 bytes x 65B = {16 * 65:,} GB; "
          f"GPT-3: 1.2 TB / 175B = {1200 / 175:.1f}")
    print()


def example_adapters_and_prompts():
    print("Example 6: adapters, prompt tuning, intrinsic dimension")
    d, m = 1024, 64
    per = 2 * m * d + d + m
    print(f"  Houlsby adapter, d = 1,024, m = 64: 2md + d + m = {per:,}; two per layer, 24 layers: "
          f"{per * 2 * 24:,} ({per * 2 * 24 / 330e6:.1%} of 330M)")
    print(f"  nine tasks at 3.6% each: {1 + 9 * 0.036:.2f} times one model; full fine-tuning 9 times")
    print(f"  GLUE 80.4 vs 80.0: {80.4 - 80.0:.1f} points, {(80.4 - 80.0) / 80.4:.1%} relative")
    print(f"  prompt tuning: 5 x 4,096 = {5 * 4096:,}; 11B / 20,480 = {11e9 / 20480:,.0f}")
    print(f"  Li et al.: 750 / 199,210 = {750 / 199210:.2%}")
    print()


def softmax_t(scores, t):
    e = [math.exp(s / t) for s in scores]
    z = sum(e)
    return [x / z for x in e]


def example_distillation():
    print("Example 7: soft targets (constructed teacher scores for car, truck, carrot)")
    scores = [10.0, 4.0, -2.0]
    for t in (1, 4):
        p = softmax_t(scores, t)
        print(f"  T = {t}: car {p[0]:.4f}, truck {p[1]:.4f}, carrot {p[2]:.6f}; truck/carrot {p[1] / p[2]:.0f}")
    print(f"  Hinton speech: (60.8 - 58.9) / (61.1 - 58.9) = {(60.8 - 58.9) / (61.1 - 58.9):.1%}")
    print(f"  DistilBERT: 66/110 = {66 / 110:.0%}; 77.0/79.5 = {77.0 / 79.5:.1%}; "
          f"668/410 = {668 / 410:.2f}; 410/668 = {410 / 668:.2f}")
    print()


def example_knowledge():
    print("Example 8: printed results on new knowledge and forgetting")
    print("  Ovadia et al., current events, Mistral 7B: base 0.481, with retrieval 0.875, "
          "fine-tuned 0.504, fine-tuned on paraphrases 0.588")
    print(f"  Luo et al., BLOOMZ-7.1b social science: 36.18 - 26.06 = {36.18 - 26.06:.2f} points")
    print("  McCloskey and Cohen (via French): 100% to 20% in 1-5 trials, 1% after five more, 0 by 15")
    print()


if __name__ == "__main__":
    example_lora_matrix()
    example_svd()
    example_whole_model()
    example_memory()
    example_qlora_numbers()
    example_adapters_and_prompts()
    example_distillation()
    example_knowledge()
