#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `attention` [D-009].

Run: python3 code/checks/attention.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. The vectors and weight maps in Examples 1 to 4 are made
up for illustration; nothing here is learned.
"""
import math
import random

# ---------------------------------------------------------------------------
# A toy attention head. Each word has four numbers, labelled by meaning so the
# reader can follow them: (function word, money, water, thing).
DIMS = ["function", "money", "water", "thing"]
WORDS = {
    "the":   [1.0, 0.0, 0.0, 0.0],
    "bank":  [0.0, 0.3, 0.3, 1.0],
    "of":    [1.0, 0.0, 0.0, 0.2],
    "river": [0.0, 0.0, 1.0, 1.0],
    "lent":  [0.2, 0.3, 0.0, 0.0],
    "us":    [1.0, 0.0, 0.0, 0.0],
    "money": [0.0, 1.0, 0.0, 1.0],
}
D_K = 2


def query(x):
    # Things ask "what topic is near me?"; function words ask "where is a thing?"
    return [3 * x[3], x[0]]


def key(x):
    # Every word advertises its topic (money + water) and whether it is a thing.
    return [x[1] + x[2], x[3]]


def value(x):
    return list(x)


def softmax(scores):
    m = max(s for s in scores if s != -math.inf)
    e = [0.0 if s == -math.inf else math.exp(s - m) for s in scores]
    t = sum(e)
    return [v / t for v in e]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def head(sentence, causal=False, positions=None):
    xs = [list(WORDS[w]) for w in sentence]
    if positions is not None:
        xs = [[a + b for a, b in zip(x, p)] for x, p in zip(xs, positions)]
    keys = [key(x) for x in xs]
    vals = [value(x) for x in xs]
    rows = []
    for i, x in enumerate(xs):
        q = query(x)
        scores = [dot(q, k) / math.sqrt(D_K) for k in keys]
        if causal:
            scores = [s if j <= i else -math.inf for j, s in enumerate(scores)]
        w = softmax(scores)
        out = [sum(wj * v[d] for wj, v in zip(w, vals)) for d in range(4)]
        rows.append((q, scores, w, out))
    return rows


RIVER = ["the", "bank", "of", "the", "river"]
MONEY = ["the", "bank", "lent", "us", "money"]


def fmt(v, n=2):
    return "[" + ", ".join(f"{x:.{n}f}" for x in v) + "]"


def example_head():
    print("Example 1: one head on 'the bank of the river'")
    rows = head(RIVER)
    q, scores, w, out = rows[1]
    print(f"  bank: query {fmt(q, 1)}; keys " + ", ".join(fmt(key(WORDS[t]), 1) for t in RIVER))
    print(f"  bank: scores {fmt(scores)}; weights {fmt(w)} (sum {sum(w):.2f})")
    print(f"  bank: before {fmt(WORDS['bank'])}, after {fmt(out)}  ({', '.join(DIMS)})")
    print("  full weight table (rows: the word asking; columns: the word looked at)")
    for t, (_, _, w, _) in zip(RIVER, rows):
        print(f"    {t:>6}: {fmt(w)}")
    print()
    print("Example 2: the same head on 'the bank lent us money'")
    q, scores, w, out = head(MONEY)[1]
    print(f"  bank: scores {fmt(scores)}; weights {fmt(w)}")
    print(f"  bank: before {fmt(WORDS['bank'])}, after {fmt(out)}")
    print()


def sinusoid(pos, d):
    pe = []
    for i in range(0, d, 2):
        rate = 1 / 10000 ** (i / d)
        pe += [math.sin(pos * rate), math.cos(pos * rate)]
    return pe


def example_order():
    print("Example 3: without positions, word order is invisible")
    swapped = ["the", "river", "of", "the", "bank"]
    a, b = head(RIVER), head(swapped)
    print(f"  'bank' in 'the bank of the river': {fmt(a[1][3])}")
    print(f"  'bank' in 'the river of the bank': {fmt(b[4][3])}")
    same = all(fmt(a[RIVER.index(t) if t != 'the' else 0][3]) == fmt(b[swapped.index(t) if t != 'the' else 0][3])
               for t in set(RIVER))
    print(f"  every word gets the same output in both orders: {same}")
    pos = [[0.5 * v for v in sinusoid(p, 4)] for p in range(5)]
    a, b = head(RIVER, positions=pos), head(swapped, positions=pos)
    print(f"  with half-size sinusoid positions added: bank {fmt(a[1][3])} vs {fmt(b[4][3])}")
    print("  4-number sinusoid encodings, positions 0-4: " + "; ".join(fmt(sinusoid(p, 4), 3) for p in range(5)))
    print()


def example_causal():
    print("Example 4: the same head with a causal mask (each word sees only itself and earlier words)")
    rows = head(RIVER, causal=True)
    for t, (_, _, w, out) in zip(RIVER, rows):
        print(f"  {t:>6}: weights {fmt(w)}; output {fmt(out)}")
    print()


def example_scaling():
    print("Example 5: why divide by the square root of d_k (random vectors, seed 1)")
    rng = random.Random(1)
    for d in (2, 4, 16, 64, 512):
        dots = []
        for _ in range(2000):
            q = [rng.gauss(0, 1) for _ in range(d)]
            k = [rng.gauss(0, 1) for _ in range(d)]
            dots.append(dot(q, k))
        mean = sum(dots) / len(dots)
        var = sum((x - mean) ** 2 for x in dots) / len(dots)
        top_raw = top_scaled = 0.0
        trials = 300
        for _ in range(trials):
            q = [rng.gauss(0, 1) for _ in range(d)]
            s = [dot(q, [rng.gauss(0, 1) for _ in range(d)]) for _ in range(10)]
            top_raw += max(softmax(s))
            top_scaled += max(softmax([x / math.sqrt(d) for x in s]))
        print(f"  d_k = {d:>3}: variance of q.k {var:6.1f}; largest of 10 weights: "
              f"unscaled {top_raw / trials:.2f}, scaled {top_scaled / trials:.2f}")
    for p in (0.5, 0.999):
        print(f"  slope of the winning weight p(1 - p) at p = {p}: {p * (1 - p):.4f}")
    print()


def example_kernel():
    print("Example 6: Nadaraya-Watson kernel regression as attention")
    xs, ys, q, h = [1, 2, 3, 4, 5], [1, 3, 2, 5, 4], 2.4, 0.7
    k = [math.exp(-((x - q) ** 2) / (2 * h * h)) for x in xs]
    w = [v / sum(k) for v in k]
    print(f"  keys x = {xs}, values y = {ys}, query {q}, width {h}")
    print(f"  weights {fmt(w, 3)}; estimate {sum(a * b for a, b in zip(w, ys)):.2f}")
    # With keys of equal length, Gaussian-kernel weights equal softmax of scaled dot products.
    rng = random.Random(2)
    d = 4
    keys = []
    for _ in range(5):
        v = [rng.gauss(0, 1) for _ in range(d)]
        n = math.sqrt(dot(v, v))
        keys.append([2 * x / n for x in v])
    qv = [rng.gauss(0, 1) for _ in range(d)]
    width2 = math.sqrt(d)
    gk = [math.exp(-sum((a - b) ** 2 for a, b in zip(qv, kk)) / (2 * width2)) for kk in keys]
    nw = [g / sum(gk) for g in gk]
    sm = softmax([dot(qv, kk) / math.sqrt(d) for kk in keys])
    print(f"  equal-length keys: largest difference between kernel and attention weights {max(abs(a - b) for a, b in zip(nw, sm)):.1e}")
    print()


def example_cost():
    print("Example 7: cost per layer, n^2 d (self-attention) against n d^2 (recurrent), d = 512")
    d = 512
    for n in (30, 100, 512, 1000, 2048, 8192, 131072):
        print(f"  n = {n:>7,}: attention / recurrent = {n * n * d / (n * d * d):.2f}")
    n = dim = 1000
    print(f"  Vaswani and Huang's slide, n = dim = 1000, kernel 3: 4 n^2 d = {4 * n * n * dim:.1e}, "
          f"16 n d^2 = {16 * n * dim * dim:.1e}, 2 k n d^2 = {2 * 3 * n * dim * dim:.1e}")
    for n in (30, 1024, 131072):
        print(f"  attention weights per head per layer at n = {n:,}: {n * n:,}")
    print()


def example_params():
    print("Example 8: parameters of the 2017 base model (reconstruction, weights only)")
    d, ff, layers, vocab = 512, 2048, 6, 37000
    attn = 4 * d * d
    ffn = 2 * d * ff
    enc, dec = attn + ffn, 2 * attn + ffn
    stack = layers * (enc + dec)
    emb = vocab * d
    print(f"  one attention layer: 4 x 512 x 512 = {attn:,}; eight heads of 64 use 3 x 8 x 512 x 64 = {3 * 8 * d * 64:,} "
          f"for queries, keys, values, the same as one head of 512 ({3 * d * d:,})")
    print(f"  feed-forward 2 x 512 x 2048 = {ffn:,}; encoder layer {enc:,}; decoder layer {dec:,}")
    print(f"  6 + 6 layers {stack:,}; shared embedding 37,000 x 512 = {emb:,}; total {stack + emb:,} (paper: 65M)")
    print(f"  attention layers {3 * layers} x 8 heads = {3 * layers * 8} heads; attention share of the layers "
          f"{3 * layers * attn / stack:.0%}")
    print()


def example_training():
    print("Example 9: training arithmetic from the paper")
    print(f"  base: 100,000 steps x 0.4 s = {100000 * 0.4 / 3600:.1f} hours (paper: 12 hours)")
    print(f"  big: 300,000 steps x 1.0 s = {300000 / 86400:.2f} days (paper: 3.5 days)")
    print(f"  FLOP estimates: 12 h x 8 GPUs x 9.5e12 = {12 * 3600 * 8 * 9.5e12:.2e}; "
          f"3.5 days x 8 x 9.5e12 = {3.5 * 86400 * 8 * 9.5e12:.2e}")
    print(f"  English-German: 28.4 - 26.36 = {28.4 - 26.36:.2f}; base 27.3 - 26.36 = {27.3 - 26.36:.2f}")
    print(f"  GNMT + RL English-German cost 2.3e19 / base 3.3e18 = {2.3e19 / 3.3e18:.1f}")
    print()


def example_steps():
    print("Example 10: steps one after another, for a 30-token sentence")
    n = 30
    print(f"  recurrent layer: {n} sequential steps; path from first to last token {n - 1} steps")
    print("  self-attention layer: 1 step (matrix products); path from first to last token 1 step")
    print()


if __name__ == "__main__":
    example_head()
    example_order()
    example_causal()
    example_scaling()
    example_kernel()
    example_cost()
    example_params()
    example_training()
    example_steps()
