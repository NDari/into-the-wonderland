#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, appendix `notation` [D-009].

Run: python3 code/checks/notation.py
Standard library only. Every number printed in the appendix comes from this
output. Where an example repeats one from a chapter, the chapter's own script
is reused: the destination chapter's scores and text (destination.py), the
generation chapter's temperature softmax (generation.py), the prediction
chapter's entropy and dice (prediction.py), and the neuron chapter's weighted
vote (neuron.py) are imported; the embeddings chapter's toy vectors are read
from embeddings.py without running it, because that script needs numpy.
"""
import ast
import importlib.util
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name):
    spec = importlib.util.spec_from_file_location(f"{name}_checks", HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D = _load("destination")
G = _load("generation")
P = _load("prediction")
NEU = _load("neuron")


def _embeddings_toy():
    """The TOY vectors of code/checks/embeddings.py, Example 2, read as a literal."""
    tree = ast.parse((HERE / "embeddings.py").read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "TOY" for t in node.targets):
            return ast.literal_eval(node.value)
    raise LookupError("TOY not found in embeddings.py")


TOY = _embeddings_toy()
GB, GIB = 10 ** 9, 2 ** 30


def example_units():
    print("Example 1: big numbers, bytes, GB and GiB")
    print(f"  2^10 = {2 ** 10:,}; 2^20 = {2 ** 20:,}; 2^30 = {2 ** 30:,}")
    print(f"  1 GiB / 1 GB = {GIB / GB:.3f}; 1 KiB / 1 kB = {1024 / 1000:.3f}")
    print(f"  2^100 = {2.0 ** 100:.3g}")
    print(f"  10^-8 = {10 ** -8:.8f}; pi = {math.pi:.5f}")
    c = 6 * 174.6e9 * 300e9
    print(f"  6 x 174.6 billion x 300 billion = {c:.3g}")
    # Weight memory, N x b / 8, for the destination chapter's 8-billion-parameter model.
    n = 8_000_000_000
    for b in (32, 16, 8, 4):
        by = n * b / 8
        print(f"  {n:,} parameters at {b} bits: {by:,.0f} bytes = {by / GB:.0f} GB = {by / GIB:.2f} GiB")
    # The generation chapter's KV cache for Llama 3 8B: 131,072 bytes per token.
    per_token = 2 * 32 * (8 * 128) * 2
    window = per_token * 131072
    print(f"  KV cache: {per_token:,} bytes per token = {per_token // 1024} KiB = {per_token / 1000:.1f} kB")
    print(f"  x 131,072 tokens = {window:,} bytes = {window / GB:.1f} GB = {window / GIB:.0f} GiB")
    # The since-2017 chapter's score tables (one head, one layer, 16-bit), in both units.
    for tokens in (1024, 8192, 131072):
        t = tokens * tokens * 2
        print(f"  score table at {tokens:,} tokens: {t:,} bytes = {t / 2 ** 20:,.0f} MiB = {t / 1e6:,.1f} MB"
              + (f" = {t / GIB:.0f} GiB = {t / GB:.1f} GB" if t >= GIB else ""))
    out = 131072 * 128 * 2
    print(f"  attention output at 131,072 tokens: {out:,} bytes = {out / 2 ** 20:.0f} MiB = {out / 1e6:.1f} MB")
    print()


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def example_vectors():
    print("Example 2: dot products, lengths, cosine (the embeddings chapter's toy vectors)")
    cat, dog, car = TOY["cat"], TOY["dog"], TOY["car"]
    print(f"  cat = {cat}, dog = {dog}, car = {car}")
    terms = " + ".join(f"{x:g} x {y:g}" for x, y in zip(cat, dog))
    print(f"  cat . dog = {terms} = {dot(cat, dog):.2f}")
    print(f"  |cat| = sqrt({dot(cat, cat):.2f}) = {norm(cat):.3f}; |dog| = sqrt({dot(dog, dog):.2f}) = {norm(dog):.3f}")
    print(f"  cos(cat, dog) = {dot(cat, dog):.2f} / ({norm(cat):.3f} x {norm(dog):.3f}) = "
          f"{dot(cat, dog) / (norm(cat) * norm(dog)):.3f}")
    print(f"  cat . car = {dot(cat, car):.2f}; cos(cat, car) = {dot(cat, car) / (norm(cat) * norm(car)):.3f}")
    cat2 = [2 * x for x in cat]
    print(f"  doubled cat: dot with dog {dot(cat2, dog):.2f}, cosine {dot(cat2, dog) / (norm(cat2) * norm(dog)):.3f}")
    onehot = [[1, 0, 0], [0, 1, 0]]
    diff = [x - y for x, y in zip(*onehot)]
    print(f"  two one-hot vectors: dot {dot(*onehot)}, distance sqrt(2) = {norm(diff):.3f}")
    # The neuron chapter's weighted vote as a dot product plus a bias.
    w, x, b = NEU.VOTE_WEIGHTS, NEU.VOTE_INPUTS, NEU.VOTE_BIAS
    z = NEU.weighted_sum(w, b, x)
    print(f"  neuron: w = {w}, x = {x}, b = {b}: w . x + b = {dot(w, x):.1f} + ({b}) = {z:.1f}")
    # Scaled dot product: a dot product of 64-number vectors divided by sqrt(64).
    print(f"  scaling for keys of 64 numbers: divide by sqrt(64) = {math.sqrt(64):.0f}")
    print()


def matvec(m, v):
    return [dot(row, v) for row in m]


def matmul(a, b):
    cols = list(zip(*b))
    return [[dot(row, col) for col in cols] for row in a]


def example_matrices():
    print("Example 3: matrix times vector, shapes, rank")
    W = [[1, 0, 2], [0, 1, -1]]
    x = [3, 1, 2]
    print(f"  W (2 x 3) = {W}; x (3 numbers) = {x}")
    for row in W:
        print(f"    row {row} . x = {dot(row, x)}")
    print(f"  W x = {matvec(W, x)} (2 numbers)")
    # Row convention: x times the 3 x 2 matrix whose columns are W's rows gives the same numbers.
    Wt = [list(c) for c in zip(*W)]
    xW = [dot(x, col) for col in zip(*Wt)]
    print(f"  x times the 3 x 2 matrix {Wt}: {xW} (same numbers)")
    # Parameter count of a layer: GPT-2 small's feed-forward network, 768 -> 3,072 -> 768.
    up = 768 * 3072 + 3072
    down = 3072 * 768 + 768
    print(f"  768 x 3,072 + 3,072 = {up:,}; 3,072 x 768 + 768 = {down:,}; together {up + down:,}")
    # A rank-1 matrix from a column times a row.
    B = [[1], [2], [3]]
    A = [[2, 0, 1]]
    BA = matmul(B, A)
    print(f"  B (3 x 1) = {[r[0] for r in B]}, A (1 x 3) = {A[0]}: BA = {BA}")
    print(f"  every row of BA is a multiple of {A[0]}: rank 1; {len(B) + len(A[0])} numbers make {len(BA) * len(BA[0])}")
    d = k = 4096
    for r in (8,):
        print(f"  LoRA at rank {r} on a {d:,} x {k:,} matrix: r(d + k) = {r * (d + k):,} of {d * k:,} "
              f"({r * (d + k) / (d * k):.2%})")
    print()


def example_logs():
    print("Example 4: logarithms, bits and nats")
    print(f"  ln 2 = {math.log(2):.3f}; 1 nat = 1 / ln 2 = {1 / math.log(2):.3f} bits; "
          f"ln 10 = {math.log(10):.3f}; log10 2 = {math.log10(2):.3f}; log2 10 = {math.log2(10):.2f}")
    print(f"  e = {math.e:.3f}; e^1 = {math.exp(1):.3f}; e^-1 = {math.exp(-1):.3f}")
    probs = [p if p is not None else D.softmax([s for _, s in D.LOGITS])[0][0] for _, _, p in D.CHAIN]
    prod = math.prod(probs)
    bits = [-math.log2(p) for p in probs]
    nats = [-math.log(p) for p in probs]
    print("  destination chain: " + " x ".join(f"{p:.3f}" for p in probs) + f" = {prod:.3e}")
    print(f"  log2 of the product = {math.log2(prod):.2f}; sum of the log2s = {-sum(bits):.2f}")
    print(f"  total surprise {sum(bits):.2f} bits = {sum(nats):.2f} nats; "
          f"per token {sum(bits) / len(bits):.3f} bits = {sum(nats) / len(nats):.3f} nats")
    # Power law and doubling.
    print(f"  2^-0.076 = {2 ** -0.076:.3f}; 10^-0.076 = {10 ** -0.076:.3f}")
    print(f"  doubling every 207 days, over 365 days: 2^(365/207) = {2 ** (365 / 207):.2f}")
    print(f"  log10 of 1,000,000 = {math.log10(1e6):.0f}; log2 of 1,024 = {math.log2(1024):.0f}")
    print()


def example_probability():
    print("Example 5: entropy, cross-entropy, KL, perplexity")
    fair = [1 / 6] * 6
    loaded = [0.1] * 5 + [0.5]
    h_fair, h_loaded = P.entropy(fair), P.entropy(loaded)
    ce = -sum(p * P.log2(q) for p, q in zip(loaded, fair))
    print(f"  fair die: entropy {h_fair:.3f} bits, perplexity {2 ** h_fair:.2f}")
    print(f"  loaded die (six half the time): entropy {h_loaded:.3f} bits, perplexity {2 ** h_loaded:.2f}")
    print(f"  surprise of a six: loaded {-P.log2(0.5):.0f} bit; any other face {-P.log2(0.1):.3f} bits")
    print(f"  cross-entropy of loaded rolls under a fair-die model: {ce:.3f} bits; KL = {ce - h_loaded:.3f} bits")
    probs = [p if p is not None else D.softmax([s for _, s in D.LOGITS])[0][0] for _, _, p in D.CHAIN]
    h = P.cross_entropy(probs)
    h_nats = h * math.log(2)
    print(f"  destination text: {h:.3f} bits per token, perplexity 2^H = {2 ** h:.2f}; "
          f"{h_nats:.3f} nats, e^H = {math.exp(h_nats):.2f}")
    # Standard error of a benchmark score, as in the evaluation chapter.
    p, n = 0.8, 164
    se = math.sqrt(p * (1 - p) / n)
    print(f"  SE at p = {p}, n = {n}: sqrt({p} x {1 - p:.1f} / {n}) = {se:.4f}; 1.96 SE = {1.96 * se * 100:.2f} points")
    print()


def example_softmax():
    print("Example 6: softmax and temperature (the destination chapter's scores)")
    scores = G.SCORES
    probs, exps, total = D.softmax(scores)
    print("  tokens " + ", ".join(G.TOKENS) + "; scores " + ", ".join(f"{s:g}" for s in scores))
    print("  e^score " + ", ".join(f"{e:.3f}" for e in exps) + f"; sum {total:.3f}")
    print("  probabilities " + ", ".join(f"{p:.3f}" for p in probs) + f"; sum {sum(probs):.3f}")
    print(f"  mat / floor = e^(3 - 2) = {probs[0] / probs[1]:.3f}")
    shifted, _, _ = D.softmax([s + 10 for s in scores])
    print(f"  add 10 to every score: same probabilities {all(abs(a - b) < 1e-12 for a, b in zip(probs, shifted))}")
    for t in (0.5, 1.0, 2.0):
        pt = G.softmax_t(scores, t)
        print(f"  T = {t}: mat {pt[0]:.3f}, the {pt[-1]:.2g}; entropy {G.entropy_bits(pt):.2f} bits")
    print(f"  six equally likely tokens: {math.log2(6):.2f} bits")
    # A softmax over two scores is the logistic function of their difference.
    a, b = 2.1, 1.7
    two, _, _ = D.softmax([a, b])
    print(f"  softmax of [{a}, {b}] = [{two[0]:.3f}, {two[1]:.3f}]; sigma({a} - {b}) = {NEU.sigmoid(a - b):.3f}")
    masked = [math.exp(s) if s != -math.inf else 0.0 for s in (1.0, 2.0, -math.inf)]
    print("  scores [1, 2, minus infinity]: weights " + ", ".join(f"{x / sum(masked):.3f}" for x in masked))
    print()


def example_logistic():
    print("Example 7: the logistic function and log-odds")
    for z in (-2, -1, 0, 0.1, 1, 2):
        print(f"  sigma({z:g}) = {NEU.sigmoid(z):.3f}")
    s1 = NEU.sigmoid(1)
    print(f"  1 - sigma(1) = {1 - s1:.3f} = sigma(-1)")
    print(f"  log-odds of {s1:.3f}: ln({s1:.3f} / {1 - s1:.3f}) = {math.log(s1 / (1 - s1)):.3f}")
    print(f"  odds at p = 0.731: {s1 / (1 - s1):.3f} = e")
    elo = 1 / (1 + 10 ** (-400 / 400))
    print(f"  Elo gap 400: 1 / (1 + 10^-1) = {elo:.3f}, odds {elo / (1 - elo):.0f} to 1")
    print(f"  400 / ln 10 = {400 / math.log(10):.1f} Elo points per unit on the natural log-odds scale")
    print(f"  log loss when the chosen answer gets sigma(1): -ln {s1:.3f} = {-math.log(s1):.3f}; "
          f"at sigma(0): {-math.log(0.5):.3f}")
    print()


if __name__ == "__main__":
    example_units()
    example_vectors()
    example_matrices()
    example_logs()
    example_probability()
    example_softmax()
    example_logistic()
