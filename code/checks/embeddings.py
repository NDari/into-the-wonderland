#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `embeddings` [D-009].

Run: python3 code/checks/embeddings.py
Uses numpy (already required by matplotlib for the figures). Every number
printed in the chapter's worked examples comes from this output.

Example 8 uses the GloVe 6B 50-dimensional word vectors (Pennington, Socher,
Manning 2014; PDDL licence). Per D-018 they are downloaded once into
out/cache/ (not committed) and checked against pinned SHA-256 hashes; the
script stops if either hash differs.
"""
import hashlib
import io
import urllib.request
import zipfile
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "out" / "cache"
GLOVE_URL = "https://huggingface.co/stanfordnlp/glove/resolve/main/glove.6B.zip"
GLOVE_ZIP = CACHE / "glove.6B.zip"
GLOVE_ZIP_SHA256 = "6471382cdd837544bf3ac72497a38715e845897d265b2b424b4761832009c837"
GLOVE_MEMBER = "glove.6B.50d.txt"
GLOVE_MEMBER_SHA256 = "c99ba128d1efdaa3496b7542ba599ecdd1dd6679114d3b5ce19f0ec208b4aa5b"


def cosine(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


# ---------------------------------------------------------------------------
# Example 1: one-hot vectors are all equally far apart.
def example_onehot():
    print("Example 1: one-hot vectors")
    words = ["cat", "dog", "car", "king", "queen"]
    eye = np.eye(len(words))
    print(f"  distance cat-dog {np.linalg.norm(eye[0] - eye[1]):.3f}, cat-car {np.linalg.norm(eye[0] - eye[2]):.3f}; "
          f"cosine cat-dog {cosine(eye[0], eye[1]):.0f}")
    print(f"  with GloVe's vocabulary (400,000 words in the paper; 400,001 lines in the released file),"
          f" each one-hot vector has about 400,000 zeros")
    print()


# ---------------------------------------------------------------------------
# Example 2: cosine similarity on made-up dense vectors.
TOY = {"cat": [0.9, 0.8, 0.1], "dog": [0.8, 0.9, 0.2], "car": [0.1, 0.2, 0.9]}


def example_cosine():
    print("Example 2: cosine on made-up 3-number vectors")
    for a, b in (("cat", "dog"), ("cat", "car")):
        print(f"  cosine {a}-{b} = {cosine(TOY[a], TOY[b]):.3f}")
    print(f"  doubling cat's vector: cosine cat-dog still {cosine(2 * np.array(TOY['cat']), TOY['dog']):.3f}")
    print()


# ---------------------------------------------------------------------------
# Example 3: latent semantic analysis on Deerwester et al.'s example
# (1990, Table 2): 12 terms in 9 technical-memo titles, raw counts.
TERMS = ["human", "interface", "computer", "user", "system", "response", "time", "EPS",
         "survey", "trees", "graph", "minors"]
TITLES = ["c1", "c2", "c3", "c4", "c5", "m1", "m2", "m3", "m4"]
COUNTS = [
    [1, 0, 0, 1, 0, 0, 0, 0, 0],   # human
    [1, 0, 1, 0, 0, 0, 0, 0, 0],   # interface
    [1, 1, 0, 0, 0, 0, 0, 0, 0],   # computer
    [0, 1, 1, 0, 1, 0, 0, 0, 0],   # user
    [0, 1, 1, 2, 0, 0, 0, 0, 0],   # system
    [0, 1, 0, 0, 1, 0, 0, 0, 0],   # response
    [0, 1, 0, 0, 1, 0, 0, 0, 0],   # time
    [0, 0, 1, 1, 0, 0, 0, 0, 0],   # EPS
    [0, 1, 0, 0, 0, 0, 0, 0, 1],   # survey
    [0, 0, 0, 0, 0, 1, 1, 1, 0],   # trees
    [0, 0, 0, 0, 0, 0, 1, 1, 1],   # graph
    [0, 0, 0, 0, 0, 0, 0, 1, 1],   # minors
]
PRINTED_SINGULAR = [3.34, 2.54, 2.35, 1.64, 1.50, 1.31, 0.85, 0.56, 0.36]


def lsa():
    X = np.array(COUNTS, float)
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    terms2 = U[:, :2] * s[:2]
    return X, s, terms2


def example_lsa():
    print("Example 3: LSA on Deerwester et al.'s 12 x 9 example")
    X, s, terms2 = lsa()
    print("  singular values: " + ", ".join(f"{v:.2f}" for v in s))
    print(f"  match the paper's printed values: {np.allclose(np.round(s, 2), PRINTED_SINGULAR)}")
    idx = {t: i for i, t in enumerate(TERMS)}
    for a, b in (("human", "user"), ("human", "computer"), ("human", "trees"), ("trees", "graph")):
        print(f"  {a}-{b}: cosine on raw counts {cosine(X[idx[a]], X[idx[b]]):.3f}, "
              f"in two factors {cosine(terms2[idx[a]], terms2[idx[b]]):.3f}")
    share = (s[:2] ** 2).sum() / (s ** 2).sum()
    print(f"  the two factors keep {share:.0%} of the sum of squares")
    print()


# ---------------------------------------------------------------------------
# Example 4: analogy arithmetic on made-up 3-number vectors, compared by
# cosine as in the chapter.
def example_toy_analogy():
    print("Example 4: analogy arithmetic on made-up vectors (cosine)")
    man, king = np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.0])
    queen = np.array([0.0, 0.9, 1.0])
    for label, woman in (("offset as large as king-to-queen", np.array([1.0, 0.9, 0.0])),
                         ("small offset", np.array([1.0, 0.3, 0.0]))):
        r = king - man + woman
        sims = {w: cosine(r, v) for w, v in (("king", king), ("queen", queen), ("man", man), ("woman", woman))}
        order = sorted(sims, key=sims.get, reverse=True)
        print(f"  {label}: woman {woman.tolist()}, result {r.tolist()}; cosines " +
              ", ".join(f"{w} {sims[w]:.3f}" for w in order))
    print()


# ---------------------------------------------------------------------------
# Example 5: embedding tables as parameters.
def example_params():
    print("Example 5: embedding table sizes")
    for name, v, d in (("GloVe 6B 50d", 400000, 50), ("Bengio et al. AP News", 17964, 100),
                       ("Bengio et al. Brown", 16383, 30)):
        print(f"  {name}: {v:,} x {d} = {v * d:,}")
    print()


# ---------------------------------------------------------------------------
# Example 6: arithmetic on numbers printed in the sources.
def example_sources():
    print("Example 6: arithmetic on printed numbers")
    print(f"  Bengio et al. Brown corpus: 800,000 + 200,000 + 181,041 = {800000 + 200000 + 181041:,}")
    print(f"  Brown test perplexity: best n-gram 312 / neural 252 = {312 / 252:.3f}; trigram 336 / 252 = {336 / 252:.3f}")
    print(f"  AP News: 117 / 109 = {117 / 109:.3f} (the paper says about 8%)")
    print(f"  word2vec analogy questions: 8,869 + 10,675 = {8869 + 10675:,}")
    print()


# ---------------------------------------------------------------------------
# Example 7: Harris's graded similarity, made numeric with invented counts of
# the environments in which three words appear.
ENVIRONMENTS = ["examined my eyes", "prescribed glasses", "drafted the will", "charged a fee", "went to court"]
HARRIS = {"oculist": [8, 6, 0, 3, 0], "eye-doctor": [7, 5, 0, 4, 0], "lawyer": [0, 0, 6, 5, 7]}


def example_harris():
    print("Example 7: invented environment counts")
    for a, b in (("oculist", "eye-doctor"), ("oculist", "lawyer")):
        print(f"  cosine {a}-{b} = {cosine(HARRIS[a], HARRIS[b]):.3f}")
    print()


# ---------------------------------------------------------------------------
# Example 8: real vectors (GloVe 6B, 50 dimensions).
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_glove():
    # Checks both pinned hashes on every run, then parses the 50d member [D-018].
    if not GLOVE_ZIP.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(GLOVE_URL) as r, open(GLOVE_ZIP, "wb") as f:
            while chunk := r.read(1 << 20):
                f.write(chunk)
    if sha256_file(GLOVE_ZIP) != GLOVE_ZIP_SHA256:
        raise SystemExit("glove.6B.zip does not match its pinned hash")
    data = zipfile.ZipFile(GLOVE_ZIP).read(GLOVE_MEMBER)
    if hashlib.sha256(data).hexdigest() != GLOVE_MEMBER_SHA256:
        raise SystemExit("glove.6B.50d.txt does not match its pinned hash")
    words, rows = [], []
    for line in io.TextIOWrapper(io.BytesIO(data), encoding="utf-8"):
        parts = line.rstrip("\n").split(" ")
        words.append(parts[0])
        rows.append(parts[1:])
    return words, np.array(rows, dtype=np.float32)


class Glove:
    def __init__(self):
        self.words, self.M = load_glove()
        self.index = {w: i for i, w in enumerate(self.words)}
        self.unit = self.M / np.linalg.norm(self.M, axis=1, keepdims=True)

    def vec(self, w):
        return self.M[self.index[w]]

    def nearest(self, v, k=5, exclude=()):
        sims = self.unit @ (v / np.linalg.norm(v))
        out = []
        for i in np.argsort(-sims):
            w = self.words[i]
            if w in exclude:
                continue
            out.append((w, float(sims[i])))
            if len(out) == k:
                return out

    def analogy(self, a, b, c, k=3, exclude_inputs=True):
        v = self.vec(b) - self.vec(a) + self.vec(c)
        return self.nearest(v, k, exclude=(a, b, c) if exclude_inputs else ())


PLOT_WORDS = ["king", "queen", "man", "woman", "prince", "princess", "boy", "girl",
              "paris", "france", "rome", "italy", "berlin", "germany",
              "cat", "dog", "horse", "cow", "car", "truck", "bus", "train"]


def pca2(G, words):
    X = np.vstack([G.vec(w) for w in words]).astype(float)
    Xc = X - X.mean(axis=0)
    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    share = s ** 2 / (s ** 2).sum()
    return Xc @ Vt[:2].T, share[:2]


def example_glove():
    print("Example 8: GloVe 6B 50d")
    G = Glove()
    print(f"  {len(G.words):,} words x {G.M.shape[1]} numbers; first word '{G.words[0]}' starts "
          + " ".join(f"{x:g}" for x in G.M[0][:3]))
    for a, b in (("cat", "dog"), ("cat", "car"), ("king", "queen"), ("king", "man")):
        print(f"  cosine {a}-{b} = {cosine(G.vec(a), G.vec(b)):.3f}")
    for w in ("frog", "bank", "france"):
        print(f"  nearest to {w}: " + ", ".join(f"{n} {s:.2f}" for n, s in G.nearest(G.vec(w), 6, exclude=(w,))))
    for a, b, c in (("man", "king", "woman"), ("man", "doctor", "woman"), ("france", "paris", "italy"),
                    ("big", "bigger", "small")):
        allw = G.analogy(a, b, c, exclude_inputs=False)
        ex = G.analogy(a, b, c)
        print(f"  {b} - {a} + {c}: nearest overall " + ", ".join(f"{n} {s:.3f}" for n, s in allw)
              + "; excluding the three inputs " + ", ".join(f"{n} {s:.3f}" for n, s in ex))
    _, share = pca2(G, PLOT_WORDS)
    print(f"  PCA of {len(PLOT_WORDS)} words: the first two components keep {share[0]:.1%} and {share[1]:.1%}")
    print()


if __name__ == "__main__":
    example_onehot()
    example_cosine()
    example_lsa()
    example_toy_analogy()
    example_params()
    example_sources()
    example_harris()
    example_glove()
