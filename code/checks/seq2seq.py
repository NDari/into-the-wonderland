#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `seq2seq` [D-009].

Run: python3 code/checks/seq2seq.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output.
"""
import math


def softmax(scores):
    m = max(scores)
    e = [math.exp(s - m) for s in scores]
    total = sum(e)
    return [x / total for x in e]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


# ---------------------------------------------------------------------------
# Example 1: arithmetic on numbers printed in the sources.
def example_sources():
    print("Example 1: arithmetic on printed numbers")
    kn5 = 221
    for label, ppl in (("single RNN alone", 173), ("single RNN + KN5", 155),
                       ("3 dynamic RNNs + KN5", 121), ("best mix", 112)):
        print(f"  Mikolov et al. 2010, {label}: perplexity {kn5} -> {ppl}, {(kn5 - ppl) / kn5:.1%} lower")
    print(f"  word error rate 13.5% -> 11.1%: {(13.5 - 11.1) / 13.5:.1%} fewer errors")
    print(f"  Cho et al. 2014: 33.30 -> 33.87 (+{33.87 - 33.30:.2f}), -> 34.64 (+{34.64 - 33.30:.2f}) BLEU")
    print(f"  Sutskever et al.: 34.81 - 33.30 = {34.81 - 33.30:.2f}; reranking 36.5 - 33.30 = {36.5 - 33.30:.1f}; "
          f"state of the art 37.0 - 36.5 = {37.0 - 36.5:.1f}; reversal 25.9 -> 30.6 (+{30.6 - 25.9:.1f})")
    print(f"  Bahdanau et al.: RNNsearch-50 - RNNencdec-50 = {26.75 - 17.82:.2f} (all), {34.16 - 26.71:.2f} (no UNK)")
    print(f"  Koehn et al. 2003: 3,152k phrase pairs / 320k sentence pairs = {3152 / 320:.2f} per sentence pair")
    print(f"  Wu et al.: 96 GPUs x 6 days = {96 * 6} GPU-days")
    print()


# ---------------------------------------------------------------------------
# Example 2: the bottleneck in sizes.
def example_bottleneck():
    print("Example 2: numbers the decoder can look at")
    for n in (10, 30, 50):
        print(f"  {n}-word sentence: fixed vector 1,000 (one layer's state); "
              f"attention keeps {n} x 2,000 = {n * 2000:,}")
    print()


# ---------------------------------------------------------------------------
# Example 3: where Sutskever et al.'s parameters are (a reconstruction).
def example_params():
    print("Example 3: Sutskever et al.'s parameters, reconstructed")
    h, layers = 1000, 4
    per_layer = 4 * h * (h + h)
    lstm = layers * per_layer
    emb_in, emb_out, softmax_w = 160_000 * h, 80_000 * h, 80_000 * h
    total = 2 * lstm + emb_in + emb_out + softmax_w
    print(f"  one LSTM layer: 4 x 1000 x (1000 + 1000) = {per_layer:,}; 4 layers = {lstm:,}; "
          f"encoder + decoder = {2 * lstm:,}")
    print(f"  word tables: 160,000 x 1000 + 80,000 x 1000 + output 80,000 x 1000 = {emb_in + emb_out + softmax_w:,}")
    print(f"  total {total:,} (the paper says 380M); word tables are {(emb_in + emb_out + softmax_w) / total:.0%}")
    print()


# ---------------------------------------------------------------------------
# Example 4: reversing the source keeps the average distance and shrinks the
# shortest one. Source, end symbol, and target laid out as one sequence;
# source word i translates to target word i.
def reversal_distances(n, reverse):
    dists = []
    for i in range(n):
        src_pos = (n - 1 - i) if reverse else i
        tgt_pos = n + 1 + i            # after the n source words and the end symbol
        dists.append(tgt_pos - src_pos)
    return dists


def example_reversal():
    print("Example 4: reversing the source")
    for n in (3, 20):
        a, b = reversal_distances(n, False), reversal_distances(n, True)
        print(f"  n = {n}: normal {a if n < 5 else '...'} (average {sum(a) / n:g}, shortest {min(a)}); "
              f"reversed {b if n < 5 else '...'} (average {sum(b) / n:g}, shortest {min(b)})")
    print()


# ---------------------------------------------------------------------------
# Example 5: one attention step, with made-up vectors. Scores are plain dot
# products (Luong et al.'s "dot" score); Bahdanau et al. used a small network.
SOURCE = ["the", "European", "Economic", "Area"]
SOURCE_VECS = {
    "the":      [1.0, 0.0, 0.0, 0.0],
    "European": [0.0, 1.0, 0.3, 0.0],
    "Economic": [0.0, 0.3, 1.0, 0.0],
    "Area":     [0.0, 0.0, 0.2, 1.0],
}
DECODER_STATES = {   # the decoder's state just before writing each French word
    "zone":       [0.2, 0.3, 0.3, 3.0],
    "économique": [0.2, 0.3, 3.0, 0.5],
}


def attention_step(state):
    scores = [dot(state, SOURCE_VECS[w]) for w in SOURCE]
    weights = softmax(scores)
    context = [sum(wt * SOURCE_VECS[w][k] for wt, w in zip(weights, SOURCE)) for k in range(4)]
    return scores, weights, context


def example_attention():
    print("Example 5: one attention step with made-up vectors")
    for target, state in DECODER_STATES.items():
        scores, weights, context = attention_step(state)
        print(f"  before writing '{target}': scores " + ", ".join(f"{w} {s:.2f}" for w, s in zip(SOURCE, scores)))
        print("    weights " + ", ".join(f"{w} {x:.2f}" for w, x in zip(SOURCE, weights))
              + f" (sum {sum(weights):.2f})")
        print("    context " + ", ".join(f"{x:.2f}" for x in context))
    print()


# ---------------------------------------------------------------------------
# The heat map: constructed weights for Bahdanau et al.'s Fig. 3(a) sentence.
# Each French word gets a made-up score of 2.5 for the English word a translator
# would align it with, minus 0.8 per word of distance from it; a softmax turns
# the scores into weights. Not learned.
HEAT_SOURCE = ["The", "agreement", "on", "the", "European", "Economic", "Area", "was", "signed", "in",
               "August", "1992", "."]
HEAT_TARGET = ["L'", "accord", "sur", "la", "zone", "économique", "européenne", "a", "été", "signé", "en",
               "août", "1992", "."]
HEAT_ALIGN = [0, 1, 2, 3, 6, 5, 4, 7, 7, 8, 9, 10, 11, 12]


def heat_weights():
    rows = []
    for a in HEAT_ALIGN:
        scores = [2.5 * (j == a) - 0.8 * abs(j - a) for j in range(len(HEAT_SOURCE))]
        rows.append(softmax(scores))
    return rows


def example_heat():
    print("Example 6: constructed heat-map weights")
    rows = heat_weights()
    for t, row in zip(HEAT_TARGET, rows):
        top = max(range(len(row)), key=row.__getitem__)
        print(f"  {t}: largest weight {row[top]:.2f} on '{HEAT_SOURCE[top]}', every row sums to {sum(row):.2f}")
    print()


# ---------------------------------------------------------------------------
# Example 7: Wu et al. Table 10. "Relative improvement" reproduces, to within
# one point, as the share of the gap between the phrase-based system and human
# translators that the neural system closed.
TABLE10 = [("English-Spanish", 4.885, 5.428, 5.504, 87), ("English-French", 4.932, 5.295, 5.496, 64),
           ("English-Chinese", 4.035, 4.594, 4.987, 58), ("Spanish-English", 4.872, 5.187, 5.372, 63),
           ("French-English", 5.046, 5.343, 5.404, 83), ("Chinese-English", 3.694, 4.263, 4.636, 60)]


def example_gnmt():
    print("Example 7: Wu et al. Table 10")
    for pair, pb, nm, hu, printed in TABLE10:
        share = (nm - pb) / (hu - pb)
        print(f"  {pair}: ({nm} - {pb}) / ({hu} - {pb}) = {share:.1%}; printed {printed}%; "
              f"within one point: {abs(share * 100 - printed) < 1}")
    print(f"  mean of printed values {sum(r[4] for r in TABLE10) / 6:.1f}%")
    print()


# ---------------------------------------------------------------------------
# Example 8: steps that must run one after another, and attention's cost.
def example_steps():
    print("Example 8: sequential steps and attention cost")
    n, L = 30, 4
    print(f"  {n}-word sentence, {L} recurrent layers: {n * L} steps one layer at a time, "
          f"{n + L - 1} with layers pipelined across GPUs, {L} for {L} layers that each process all positions at once")
    for t in (15, 30, 50):
        print(f"  attention scores for a {t}-word sentence and a {t}-word translation: {t * t:,}")
    print()


# ---------------------------------------------------------------------------
# Example 9: BLEU's clipped precision (Papineni et al.'s example).
def example_bleu():
    print("Example 9: BLEU's clipped precision")
    cand = "the the the the the the the".split()
    refs = ["the cat is on the mat".split(), "there is a cat on the mat".split()]
    plain = sum(any(w in r for r in refs) for w in cand) / len(cand)
    clip = min(cand.count("the"), max(r.count("the") for r in refs)) / len(cand)
    print(f"  plain precision {plain:.0%} (7/7); clipped {clip:.3f} (2/7)")
    print()


if __name__ == "__main__":
    example_sources()
    example_bottleneck()
    example_params()
    example_reversal()
    example_attention()
    example_heat()
    example_gnmt()
    example_steps()
    example_bleu()
