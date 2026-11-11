#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `anatomy` [D-009].

Run: python3 code/checks/anatomy.py
Standard library only. Every number printed in the chapter comes from this
output. Model shapes are typed in from their published sources:
GPT-2: hparams.json in OpenAI's gpt-2 release (n_vocab 50257, n_ctx 1024,
n_embd 768, n_head 12, n_layer 12 for the 124M model, and the larger sizes).
GPT-1: Radford et al. 2018, p. 5, and the released params_shapes.json
(vocabulary 40,478). GPT-3: Brown et al. 2020, Table 2.1. Llama 3 8B:
Grattafiori et al. 2024, Table 3.
"""
import math


def gpt2_count(vocab, ctx, d, layers, final_norm=True, tied=True):
    """Exact parameter count of a GPT-2-style model (biases and layer norms included)."""
    norms = 2 * (2 * d)                    # two layer norms per block, gain and bias
    attn = (d * 3 * d + 3 * d) + (d * d + d)
    ffn = (d * 4 * d + 4 * d) + (4 * d * d + d)
    block = norms + attn + ffn
    parts = {
        "token table": vocab * d,
        "position table": ctx * d,
        "attention": layers * attn,
        "feed-forward": layers * ffn,
        "layer norms": layers * norms + (2 * d if final_norm else 0),
    }
    if not tied:
        parts["output layer"] = vocab * d
    return parts, block


def example_gpt2():
    print("Example 1: GPT-2 small, counted from its five hyperparameters")
    d, layers = 768, 12
    parts, block = gpt2_count(50257, 1024, d, layers)
    total = sum(parts.values())
    for name, n in parts.items():
        print(f"  {name:>15}: {n:>12,}  ({n / total:.2%})")
    print(f"  {'total':>15}: {total:>12,}  (the released checkpoint holds 124,439,808)")
    print(f"  one block: {block:,}; twelve blocks: {layers * block:,}")
    ffn_share = parts["feed-forward"] / (parts["attention"] + parts["feed-forward"] + layers * 4 * d)
    print(f"  inside the blocks, feed-forward is {ffn_share:.1%}; attention {parts['attention'] / (layers * block):.1%}")
    print(f"  float32 storage: {total * 4:,} bytes")
    print(f"  per block: attention 4 x 768 x 768 + biases = {4 * d * d + 4 * d:,}; "
          f"feed-forward 2 x 768 x 3,072 + biases = {8 * d * d + 5 * d:,}")
    untied, _ = gpt2_count(50257, 1024, d, layers, tied=False)
    print(f"  an untied output layer would add {50257 * d:,}: total {sum(untied.values()):,} "
          f"({sum(untied.values()) / total - 1:.0%} more)")
    print()


def example_kaplan():
    print("Example 2: Kaplan et al.'s estimate 12 x layers x width^2 against the exact count")
    for name, d, layers, vocab, ctx in (("GPT-2 small", 768, 12, 50257, 1024), ("GPT-2 medium", 1024, 24, 50257, 1024),
                                         ("GPT-2 large", 1280, 36, 50257, 1024), ("GPT-2 XL", 1600, 48, 50257, 1024)):
        parts, _ = gpt2_count(vocab, ctx, d, layers)
        exact = sum(parts.values()) - parts["token table"] - parts["position table"]
        est = 12 * layers * d * d
        print(f"  {name}: estimate {est:,}; exact without embeddings {exact:,} ({est / exact - 1:+.2%}); "
              f"total {sum(parts.values()):,}")
    print()


def example_others():
    print("Example 3: other models from the same formula")
    p, _ = gpt2_count(40478, 512, 768, 12, final_norm=False)
    print(f"  GPT-1 (vocabulary 40,478, context 512, no final norm): {sum(p.values()):,} (rounds to 117M)")
    p, _ = gpt2_count(50257, 2048, 768, 12)
    print(f"  GPT-3 Small (GPT-2 small with context 2,048): {sum(p.values()):,} (printed 125M)")
    p, _ = gpt2_count(50257, 2048, 12288, 96)
    print(f"  GPT-3 (96 layers, width 12,288): {sum(p.values()):,} (printed 175.0B)")
    # Llama 3 8B: 32 layers, width 4,096, feed-forward 14,336 (three matrices, SwiGLU),
    # 32 query heads and 8 key/value heads of 128, vocabulary 128,000, untied, RMSNorm gains only.
    d, layers, ff, kv = 4096, 32, 14336, 8 * 128
    attn = 2 * d * d + 2 * d * kv
    ffn = 3 * d * ff
    norms = 2 * d
    blocks = layers * (attn + ffn + norms)
    total = blocks + 2 * 128000 * d + d
    print(f"  Llama 3 8B: attention per layer {attn:,}; feed-forward {ffn:,}; blocks {blocks:,}; "
          f"embedding and output tables {2 * 128000 * d:,}; total {total:,}")
    print(f"  Llama 3 8B: feed-forward share of a block {ffn / (attn + ffn + norms):.1%}; "
          f"12 x layers x width^2 would give {12 * layers * d * d:,} for the blocks")
    print()


def softmax(scores):
    m = max(s for s in scores if s != -math.inf)
    e = [0.0 if s == -math.inf else math.exp(s - m) for s in scores]
    return [x / sum(e) for x in e]


def example_mask():
    print("Example 4: a causal mask on 'The cat sat on the'")
    n = 5
    allowed = sum(1 for i in range(n) for j in range(n) if j <= i)
    print(f"  {n * n} cells, {allowed} allowed (the diagonal and below)")
    scores = [0.4, 1.3, 0.9, 2.0, -0.5]   # made-up scores for position 3 ("sat") over positions 1-5
    masked = [s if j <= 2 else -math.inf for j, s in enumerate(scores)]
    w = softmax(masked)
    print(f"  'sat': scores {scores}; masked weights " + ", ".join(f"{x:.2f}" for x in w))
    scores2 = scores[:3] + [9.0, 9.0]
    w2 = softmax([s if j <= 2 else -math.inf for j, s in enumerate(scores2)])
    print(f"  changing the masked scores to 9.0 leaves the weights unchanged: {w == w2}")
    print()


def example_positions():
    print("Example 5: one pass, many predictions; scores grow with the square of the length")
    print(f"  a window of 1,025 tokens gives 1,024 predictions; GPT-2's batch of 512 windows gives {512 * 1024:,} per step")
    for n in (1024, 2048, 8192, 131072):
        print(f"  {n:>7,} tokens: {n * n:>15,} scores per head per layer ({n * (n + 1) // 2:,} allowed by the mask)")
    print(f"  GPT-2 small at 1,024 tokens: 12 heads x 12 layers x 1,048,576 = {12 * 12 * 1024 * 1024:,} scores per pass")
    n_param = 12 * 12 * 768 * 768
    for ctx in (1024, 131072):
        attn = 2 * 12 * ctx * 768
        print(f"  per-token compute (Kaplan Table 1), GPT-2 small at {ctx:,} tokens: 2N = {2 * n_param:,}; "
              f"attention scores term {attn:,} ({attn / (2 * n_param):.0%} of 2N)")
    print()


def example_follow():
    print("Example 6: following one token through GPT-2 small")
    print("  ' cat' is ID 3797: row 3,797 of the 50,257 x 768 token table, plus row 2 (counting from 1) of the 1,024 x 768 position table")
    print("  12 blocks, each: normalize a copy, attention (12 heads of 64), add back; normalize a copy, 768 -> 3,072 -> 768, add back")
    print("  final normalization; 50,257 dot products with the token table give 50,257 logits")
    print()


if __name__ == "__main__":
    example_gpt2()
    example_kaplan()
    example_others()
    example_mask()
    example_positions()
    example_follow()
