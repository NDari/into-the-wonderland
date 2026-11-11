#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `tools` [D-009].

Run: python3 code/checks/tools.py
Uses numpy (already required by matplotlib for the figures). Every number
printed in the chapter's worked examples comes from this output.

Example 1 compares three ways of scoring three passages against a question.
The question and passages are quoted from OpenAI's retrieval guide (as of
2026-11; see book1/sources/tools.md, TL10). Its third method uses the GloVe
6B 50-dimensional word vectors through code/checks/embeddings.py's loader,
which checks pinned hashes of the copy in out/cache/ [D-018]. OpenAI's own
similarity percentages for the same sentences are printed for comparison as
quoted figures; they cannot be recomputed here.

The other examples are arithmetic on numbers printed in the sources (see the
ledger, "Mechanism claims to check numerically at drafting").
"""
import importlib.util
import math
import re
from collections import Counter
from pathlib import Path

import numpy as np

_spec = importlib.util.spec_from_file_location(
    "embeddings_checks", Path(__file__).resolve().parent / "embeddings.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

# ---------------------------------------------------------------------------
# Example 1: the toy retrieval used in the chapter's key figure.
QUERY = "When did we go to the moon?"
PASSAGES = [
    "The first lunar landing occurred in July of 1969.",
    "The first man on the moon was Neil Armstrong.",
    "When I ate the moon cake, it was delicious.",
]
# Quoted from OpenAI's retrieval guide (as of 2026-11), "Semantic Similarity",
# computed there with a trained embedding model. Not reproducible here.
OPENAI_SEMANTIC = [0.65, 0.43, 0.28]
# A small list of high-frequency function words (the idea of a stop list,
# SLP3 ch. 11 p. 9). Chosen for this example, not taken from a source.
STOP = {"the", "a", "an", "of", "to", "in", "on", "at", "was", "is", "it", "i", "we",
        "did", "when", "and"}
TOP_K = 2


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def cosine_dict(a, b):
    dot = sum(a[k] * b.get(k, 0.0) for k in a)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def tf_slp3(count):
    """Term frequency as in SLP3 Eq. 11.4: 1 + log10(count), or 0."""
    return 1 + math.log10(count) if count > 0 else 0.0


def idf_table(docs):
    """idf_t = log10(N / df_t) over the passages (SLP3 Eq. 11.5)."""
    n = len(docs)
    df = Counter(t for d in docs for t in set(words(d)))
    return n, df, {t: math.log10(n / c) for t, c in df.items()}


def tfidf_vec(text, idf):
    c = Counter(words(text))
    return {t: tf_slp3(k) * idf.get(t, 0.0) for t, k in c.items()}


def count_scores():
    q = Counter(words(QUERY))
    return [cosine_dict(q, Counter(words(p))) for p in PASSAGES]


def tfidf_scores():
    _, _, idf = idf_table(PASSAGES)
    q = tfidf_vec(QUERY, idf)
    return [cosine_dict(q, tfidf_vec(p, idf)) for p in PASSAGES]


_GLOVE = None


def glove():
    global _GLOVE
    if _GLOVE is None:
        _GLOVE = E.Glove()
    return _GLOVE


def average_vector(text, stop=frozenset()):
    g = glove()
    vs = [g.vec(w) for w in words(text) if w not in stop and w in g.index]
    return np.mean(vs, axis=0)


def glove_scores(stop=frozenset()):
    q = average_vector(QUERY, stop)
    return [E.cosine(q, average_vector(p, stop)) for p in PASSAGES]


def toy_scores():
    """Scores used by the chapter and by figures/tools.py."""
    return {
        "word counts": count_scores(),
        "tf-idf": tfidf_scores(),
        "averaged GloVe, all words": glove_scores(),
        "averaged GloVe, stop words removed": glove_scores(STOP),
        "OpenAI's trained model (quoted)": OPENAI_SEMANTIC,
    }


def ranking(scores):
    return sorted(range(len(scores)), key=lambda i: -scores[i])


def example_toy_retrieval():
    print("Example 1: three passages scored against one question")
    print(f"  question: {QUERY!r}; words {words(QUERY)}")
    for i, p in enumerate(PASSAGES, 1):
        print(f"  D{i}: {p!r}; shared words with the question: "
              f"{sorted(set(words(p)) & set(words(QUERY)))}")
    n, df, idf = idf_table(PASSAGES)
    print(f"  N = {n} passages; idf of shared words: " +
          ", ".join(f"{t} df {df[t]} idf {idf[t]:.3f}" for t in ("the", "moon", "when")))
    for name, s in toy_scores().items():
        order = ranking(s)
        print(f"  {name:36s} " + "  ".join(f"D{i + 1} {x:.3f}" for i, x in enumerate(s)) +
              f"   ranking: {' > '.join(f'D{i + 1}' for i in order)}; top {TOP_K}: "
              f"{', '.join(f'D{i + 1}' for i in order[:TOP_K])}")
    g = glove()
    for a, b in (("moon", "lunar"), ("moon", "cake"), ("moon", "armstrong"), ("go", "landing")):
        print(f"  GloVe cosine {a}-{b} = {E.cosine(g.vec(a), g.vec(b)):.3f}")
    print(f"  stop list used ({len(STOP)} words): {', '.join(sorted(STOP))}")
    q = [w for w in words(QUERY) if w not in STOP]
    print(f"  question words left after the stop list: {q}")
    print()


# ---------------------------------------------------------------------------
# Example 2: Sparck Jones's 1972 weights (reprint p. 6).
def f_sj(n):
    m = 0
    while 2 ** m < n:
        m += 1
    return m


def example_sparck_jones():
    print("Example 2: Sparck Jones (1972), weight = f(N) - f(n) + 1 with 2^(m-1) < n <= 2^m")
    big_n = 200
    for n in (90, 3):
        w = f_sj(big_n) - f_sj(n) + 1
        print(f"  N = {big_n}: f(N) = {f_sj(big_n)}; n = {n}: f(n) = {f_sj(n)}, weight {w}; "
              f"log2(N/n) = {math.log2(big_n / n):.2f}")
    print()


# ---------------------------------------------------------------------------
# Example 3: BM25's term-frequency part (Robertson and Zaragoza 2009, Eq. 3.15)
# with k1 = 1.2 and b = 0.75, inside the range those authors call reasonably
# good in many circumstances (p. 360).
K1, B = 1.2, 0.75
TFS = (1, 2, 3, 5, 10, 100)


def bm25_tf(tf, k1=K1, b=B, dl_over_avdl=1.0):
    return tf / (k1 * ((1 - b) + b * dl_over_avdl) + tf)


def example_bm25():
    print(f"Example 3: BM25 saturation, k1 = {K1}, b = {B}")
    print("  tf:              " + "  ".join(f"{t:>6}" for t in TFS))
    print("  raw count:       " + "  ".join(f"{t:>6}" for t in TFS))
    print("  1 + log10 tf:    " + "  ".join(f"{tf_slp3(t):6.3f}" for t in TFS))
    print("  BM25 tf part:    " + "  ".join(f"{bm25_tf(t):6.3f}" for t in TFS))
    print("  with (k1+1) top: " + "  ".join(f"{(K1 + 1) * bm25_tf(t):6.3f}" for t in TFS)
          + f"   (ceiling {K1 + 1:.1f}; same ranking)")
    for label, r in (("half the average length", 0.5), ("average length", 1.0), ("twice the average", 2.0)):
        bb = (1 - B) + B * r
        print(f"  tf = 3 in a document {label}: B = {bb:.3f}, tf part {bm25_tf(3, dl_over_avdl=r):.3f}")
    print()


# ---------------------------------------------------------------------------
# Example 4: idf at DPR's scale (21,015,324 passages).
N_DPR = 21_015_324
DIM_DPR = 768


def example_idf_scale():
    print(f"Example 4: idf over {N_DPR:,} passages")
    for n in (1, 10, 1_000, 100_000, 1_000_000, 10_000_000):
        rsj = math.log((N_DPR - n + 0.5) / (n + 0.5))
        print(f"  word in {n:>10,} passages: RSJ idf (natural log) {rsj:6.2f}; log10(N/n) {math.log10(N_DPR / n):5.2f}")
    print()


# ---------------------------------------------------------------------------
# Example 5: index memory and brute-force search cost.
def example_memory():
    print("Example 5: memory of a vector index (vectors x dimensions x bytes)")
    numbers = N_DPR * DIM_DPR
    print(f"  DPR/RAG index: {N_DPR:,} x {DIM_DPR} = {numbers:,} numbers "
          f"(also the multiply-adds of one brute-force search)")
    for label, bits in (("32-bit", 32), ("16-bit", 16), ("8-bit", 8), ("1-bit", 1)):
        print(f"    {label}: {numbers * bits / 8 / 1e9:.2f} GB")
    print(f"  Lewis et al.'s printed 21M x 728 = {21e6 * 728 / 1e9:.2f} billion (TLD3; not used)")
    for label, n, d in (("1,000,000 chunks at 1,024 dimensions", 1_000_000, 1024),
                        ("1,000,000 chunks at 1,536 dimensions", 1_000_000, 1536)):
        print(f"  {label}: float32 {n * d * 4 / 1e9:.2f} GB, int8 {n * d / 1e9:.2f} GB, "
              f"binary {n * d / 8 / 1e9:.3f} GB")
    print()


# ---------------------------------------------------------------------------
# Example 6: DPR against BM25, top-20 accuracy (Karpukhin et al. 2020, Table 2).
DPR_TOP20 = {"NQ": (59.1, 78.4), "TriviaQA": (66.9, 79.4), "WQ": (55.0, 73.2),
             "TREC": (70.9, 79.8), "SQuAD": (68.8, 63.2)}


def example_dpr():
    print("Example 6: DPR minus BM25, top-20 retrieval accuracy (points)")
    for k, (bm, dp) in DPR_TOP20.items():
        print(f"  {k:9s} BM25 {bm:5.1f}  DPR {dp:5.1f}  gap {dp - bm:+5.1f}")
    print()


# ---------------------------------------------------------------------------
# Example 7: RAG's world-leader test as counts of 82 (Lewis et al., p. 8).
def example_leaders():
    print("Example 7: printed percentages of 82 questions, as counts")
    for pct in (70, 68, 12, 4):
        fits = [c for c in range(83) if round(100 * c / 82) == pct]
        print(f"  {pct}%: counts that round to it {fits} ({', '.join(f'{100 * c / 82:.1f}%' for c in fits)})")
    print()


# ---------------------------------------------------------------------------
# Example 8: why not compare the question with every passage (SBERT, p. 3982).
def example_pairs():
    print("Example 8: cross-encoder pair count for 10,000 sentences")
    n = 10_000
    pairs = n * (n - 1) // 2
    print(f"  {n:,} x {n - 1:,} / 2 = {pairs:,}; 65 hours / pairs = {65 * 3600 / pairs * 1000:.1f} ms per pair")
    print()


# ---------------------------------------------------------------------------
# Example 9: chunking with overlap (OpenAI default as of 2026-11: 800 / 400).
def chunk_starts(length, size, overlap):
    step = size - overlap
    starts = [0]
    while starts[-1] + size < length:
        starts.append(starts[-1] + step)
    return starts


def example_chunks():
    print("Example 9: a 5,000-token document in 800-token chunks with 400 overlap")
    doc, size, overlap = 5000, 800, 400
    starts = chunk_starts(doc, size, overlap)
    stored = sum(min(s + size, doc) - s for s in starts)
    print(f"  starts {starts}; last chunk {starts[-1]}-{min(starts[-1] + size, doc)}")
    print(f"  {len(starts)} chunks, {stored:,} tokens stored, {stored / doc:.2f} times the document")
    print(f"  DPR: {N_DPR:,} passages of at most 100 words: at most {N_DPR * 100 / 1e9:.1f} billion words")
    print()


# ---------------------------------------------------------------------------
# Example 10: small consistency checks on printed numbers.
def example_misc():
    print("Example 10: consistency checks")
    for after in (3.7, 2.9, 1.9):
        print(f"  contextual retrieval: (5.7 - {after}) / 5.7 = {(5.7 - after) / 5.7:.1%}")
    print(f"  ReAct failure modes 47 + 23 + 0 + 29 = {47 + 23 + 0 + 29}; CoT 16 + 56 + 28 = {16 + 56 + 28}")
    print(f"  Llama 3.1: cutoff December 2023, released 23 July 2024: "
          f"{(2024 - 2023) * 12 + 7 - 12} months from the end of December to the end of July")
    print(f"  RAG-Sequence 44.5 vs T5-11B closed book 34.5: {44.5 - 34.5:.1f} points")
    print(f"  ReAct HotpotQA: ReAct 27.4 vs CoT 29.4 ({27.4 - 29.4:+.1f}); Fever 60.9 vs 56.3 ({60.9 - 56.3:+.1f})")
    print()


if __name__ == "__main__":
    example_toy_retrieval()
    example_sparck_jones()
    example_bm25()
    example_idf_scale()
    example_memory()
    example_dpr()
    example_leaders()
    example_pairs()
    example_chunks()
    example_misc()
