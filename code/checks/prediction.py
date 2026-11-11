#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `prediction` [D-009].

Run: python3 code/checks/prediction.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output. Examples 1, 2, 5 and 6 redo arithmetic on numbers
printed in the sources logged in book1/sources/prediction.md.

Example 7 counts word pairs in Jane Austen's "Pride and Prejudice", Project
Gutenberg eBook #1342. The text is downloaded once into out/cache/ (which is
not committed) and checked against a pinned SHA-256 hash; if Project
Gutenberg revises the file, the script stops rather than print different
numbers.
"""
import hashlib
import math
import re
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "out" / "cache"
PG_URL = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
PG_FILE = CACHE / "pg1342.txt"
PG_SHA256 = "3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75"


def log2(x):
    return math.log(x, 2)


# ---------------------------------------------------------------------------
# Example 1: bigram probabilities by counting (Jurafsky and Martin's corpus).
JM = ["<s> I am Sam </s>", "<s> Sam I am </s>", "<s> I do not like green eggs and ham </s>"]


def bigram_counts(sentences):
    uni, bi = Counter(), Counter()
    for s in sentences:
        w = s.split()
        uni.update(w[:-1])
        bi.update(zip(w, w[1:]))
    return uni, bi


def example_counting():
    print("Example 1: bigram probabilities by counting")
    uni, bi = bigram_counts(JM)
    for prev, word in (("<s>", "I"), ("<s>", "Sam"), ("I", "am"), ("Sam", "</s>"), ("am", "Sam"), ("I", "do")):
        print(f"  P({word} | {prev}) = {bi[(prev, word)]}/{uni[prev]} = {bi[(prev, word)] / uni[prev]:.3f}")
    print()


# ---------------------------------------------------------------------------
# Example 2: a zero count, and add-one smoothing (Chen and Goodman's corpus).
CG = ["<bos> John read Moby Dick <eos>", "<bos> Mary read a different book <eos>",
      "<bos> She read a book by Cher <eos>"]


def sentence_prob(sentence, uni, bi, add=0, V=None):
    w = sentence.split()
    p = 1.0
    for a, b in zip(w, w[1:]):
        p *= (bi[(a, b)] + add) / (uni[a] + add * (V or 0))
    return p


def example_smoothing():
    print("Example 2: the zero-count problem and add-one smoothing")
    uni, bi = bigram_counts(CG)
    s1, s2 = "<bos> John read a book <eos>", "<bos> Cher read a book <eos>"
    print(f"  counting only: P(John read a book) = {sentence_prob(s1, uni, bi):.4f}; "
          f"P(Cher read a book) = {sentence_prob(s2, uni, bi):g} (no 'Cher read' in the corpus)")
    for V in (11, 12):
        print(f"  add-one with V = {V}: {sentence_prob(s1, uni, bi, 1, V):.6f} and {sentence_prob(s2, uni, bi, 1, V):.7f}")
    print(f"  Jurafsky and Martin's 'want to': unsmoothed 608/927 = {608 / 927:.3f}; "
          f"add-one (608+1)/(927+1446) = {609 / (927 + 1446):.3f}")
    print()


# ---------------------------------------------------------------------------
# Example 3: cross-entropy and perplexity.
def cross_entropy(probs):
    return -sum(log2(p) for p in probs) / len(probs)


def example_perplexity():
    print("Example 3: cross-entropy (bits per word) and perplexity")
    a = [1 / 3] * 5
    b = [0.8] * 4 + [0.1]
    for name, ps in (("model A, uniform over 3 colors", a), ("model B, red 0.8", b)):
        h = cross_entropy(ps)
        print(f"  'red red red red blue' under {name}: probability {math.prod(ps):.6f}, "
              f"{h:.3f} bits per word, perplexity {2 ** h:.3f}")
    dest = [0.040, 0.010, 0.150, 0.400, 0.600, math.exp(3) / sum(math.exp(s) for s in (3.0, 2.0, 1.5, 1.0, -1.0, -2.0))]
    surprisal = [-log2(p) for p in dest]
    h = sum(surprisal) / len(surprisal)
    print("  the destination chapter's six-token text: surprisal in bits " + ", ".join(f"{s:.3f}" for s in surprisal))
    print(f"  average {h:.3f} bits per token, perplexity {2 ** h:.2f}")
    print()


# ---------------------------------------------------------------------------
# Example 4: entropy of dice, and the cost of the wrong model.
def entropy(ps):
    return -sum(p * log2(p) for p in ps if p > 0)


def example_dice():
    print("Example 4: entropy of dice")
    fair = [1 / 6] * 6
    loaded = [0.1] * 5 + [0.5]
    for name, ps in (("fair die", fair), ("loaded die (six half the time)", loaded)):
        h = entropy(ps)
        print(f"  {name}: {h:.3f} bits, perplexity {2 ** h:.2f}")
    print(f"  coins: fair {entropy([0.5, 0.5]):.3f} bits; 0.9/0.1 coin {entropy([0.9, 0.1]):.3f} bits")
    ce = -sum(p * log2(q) for p, q in zip(loaded, fair))
    print(f"  loaded-die rolls scored by a model that thinks the die is fair: {ce:.3f} bits "
          f"(true entropy {entropy(loaded):.3f}; extra {ce - entropy(loaded):.3f})")
    print()


# ---------------------------------------------------------------------------
# Example 5: possible n-grams against what corpora contain.
def example_sparsity():
    print("Example 5: possible versus observed n-grams")
    V = 260741   # Brown et al. 1992, Table 1: 260,740 words plus an unknown-word token
    print(f"  Brown et al.: V^2 = {V ** 2:.4g}, V^3 = {V ** 3:.4g}")
    print(f"  bigrams seen: 14,494,217 of {V ** 2:.4g} = {14494217 / V ** 2:.3%} (1 in {V ** 2 / 14494217:,.0f})")
    print(f"  trigrams seen: 75,349,888 of {V ** 3:.4g} = {75349888 / V ** 3:.2g}")
    print(f"  share of new text unseen (singletons / words): trigrams {53737350 / 365893263:.1%}, "
          f"bigrams {8045024 / 365893263:.1%}")
    print(f"  Shakespeare V = 29,066: V^2 = {29066 ** 2:,}; V^4 = {29066 ** 4:.3g}")
    print(f"  IBM Tangora, 20,000 words: 20,000^3 = {20000 ** 3:.2g} possible trigrams")
    print(f"  Bengio et al.: 100,000^10 = {100000 ** 10:.0e}")
    print(f"  letters: 27^2 = {27 ** 2:,}, 27^3 = {27 ** 3:,}, 27^4 = {27 ** 4:,}")
    print()


# ---------------------------------------------------------------------------
# Example 6: Shannon's numbers.
GAME_TEXT = ["THE ROOM WAS NOT VERY LIGHT A SMALL OBLONG ",
             "READING LAMP ON THE DESK SHED GLOW ON ",
             "POLISHED WOOD BUT LESS ON THE SHABBY RED CARPET "]
GAME_REDUCED = ["----ROO------NOT-V-----I------SM----OBL----",
                "REA----------O------D----SHED-GLO--O--",
                "P-L-S-----O---BU--L-S--O------SH-----RE--C------"]
GUESS_TEXT = "THERE IS NO REVERSE ON A MOTORCYCLE A "
GUESS_NUMBERS = [1, 1, 1, 5, 1, 1, 2, 1, 1, 2, 1, 1, 15, 1, 17, 1, 1, 1, 2, 1, 3, 2, 1, 2, 2, 7,
                 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 1]


def example_shannon():
    print("Example 6: Shannon's numbers")
    total = sum(len(t) for t in GAME_TEXT)
    right = sum(r.count("-") for r in GAME_REDUCED)
    consistent = all(len(t) == len(r) and all(c == "-" or c == tc for c, tc in zip(r, t))
                     for t, r in zip(GAME_TEXT, GAME_REDUCED))
    print(f"  guessing game (1951): {right} of {total} guessed right = {right / total:.0%}; transcription consistent: {consistent}")
    print(f"  second game, first line: {len(GUESS_NUMBERS)} numbers for {len(GUESS_TEXT)} symbols; "
          f"first-guess hits {GUESS_NUMBERS.count(1)}")
    print(f"  second game totals: 79 + 8 + 3 + 2 + 2 + 8 = {79 + 8 + 3 + 2 + 2 + 8}; 79/102 = {79 / 102:.1%}")
    print(f"  log2 26 = {log2(26):.2f}; log2 27 = {log2(27):.2f}")
    for bits in (4.70, 4.14, 3.56, 3.3, 2.3, 1.3, 0.6):
        print(f"  {bits} bits per letter = perplexity {2 ** bits:.2f}")
    print()


# ---------------------------------------------------------------------------
# Example 7: how empty a real bigram table is (Pride and Prejudice).
def load_austen():
    if not PG_FILE.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(PG_URL) as r:
            PG_FILE.write_bytes(r.read())
    data = PG_FILE.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != PG_SHA256:
        raise SystemExit(f"pg1342.txt has changed (sha256 {digest}); numbers would not match the chapter")
    text = data.decode("utf-8")
    start = text.index("*** START OF THE PROJECT GUTENBERG EBOOK")
    start = text.index("\n", start) + 1
    end = text.index("*** END OF THE PROJECT GUTENBERG EBOOK")
    return text[start:end]


def austen_tokens():
    return re.findall(r"[a-z]+(?:'[a-z]+)?", load_austen().lower())


MID_RANKS = (200, 210)   # words ranked 201 to 210 by frequency
TOP = 8


def austen_tables():
    toks = austen_tokens()
    uni = Counter(toks)
    bi = Counter(zip(toks, toks[1:]))
    tri = Counter(zip(toks, toks[1:], toks[2:]))
    ranked = [w for w, _ in uni.most_common()]
    mid = ranked[MID_RANKS[0]:MID_RANKS[1]]
    top = ranked[:TOP]
    return toks, uni, bi, tri, mid, top


def example_austen():
    print("Example 7: Pride and Prejudice, lowercased words")
    toks, uni, bi, tri, mid, top = austen_tables()
    V = len(uni)
    print(f"  {len(toks):,} words; vocabulary {V:,}")
    print(f"  distinct bigrams {len(bi):,} of {V ** 2:,} possible = {len(bi) / V ** 2:.3%} seen; "
          f"{sum(1 for c in bi.values() if c == 1):,} seen only once")
    print(f"  distinct trigrams {len(tri):,} of {V ** 3:.3g} possible")
    zeros = sum(1 for a in mid for b in mid if bi[(a, b)] == 0)
    print(f"  words ranked {MID_RANKS[0] + 1}-{MID_RANKS[1]}: {', '.join(mid)}")
    print(f"  in their 10 x 10 table of word pairs, {zeros} of 100 cells are zero")
    for a in mid:
        print("   ", a.ljust(10), " ".join(f"{bi[(a, b)]:>3}" for b in mid))
    zeros_top = sum(1 for a in top for b in top if bi[(a, b)] == 0)
    print(f"  8 most frequent words ({', '.join(top)}): {zeros_top} of 64 pairs never occur")
    print()


if __name__ == "__main__":
    example_counting()
    example_smoothing()
    example_perplexity()
    example_dice()
    example_sparsity()
    example_shannon()
    example_austen()
