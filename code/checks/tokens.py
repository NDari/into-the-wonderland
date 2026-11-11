#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `tokens` [D-009].

Run: python3 code/checks/tokens.py
Standard library only. Every number printed in the chapter's worked examples
comes from this output.

Examples 4 to 6 use GPT-2's released vocabulary (OpenAI, 2019: encoder.json
and vocab.bpe from the gpt-2 release). Per D-018 they are downloaded once into
out/cache/ (not committed) and checked against pinned SHA-256 hashes.

GPT-2 first cuts text into pieces with a pattern that needs the third-party
`regex` module. This script uses a standard-library version of that pattern
(letters = [^\\W\\d_], digits = \\d). It matches the original for the plain
ASCII, Cyrillic, and Chinese/Japanese text used below, but not in general.
"""
import hashlib
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "out" / "cache"
GPT2_BASE = "https://openaipublic.blob.core.windows.net/gpt-2/models/124M/"
GPT2_FILES = {
    "encoder.json": "196139668be63f3b5d6574427317ae82f612a97c5d1cdaf36ed2256dbf636783",
    "vocab.bpe": "1ce1664773c50f3e0cc8842619a93edc4624525b728b188a9e0be33b7726adc5",
}


# ---------------------------------------------------------------------------
# Example 1: Gage's byte pair encoding, as compression (1994).
def gage(data, new_symbols):
    steps = [data]
    for sym in new_symbols:
        pairs = {}
        for a, b in zip(data, data[1:]):
            pairs[a + b] = pairs.get(a + b, 0) + 1
        best = max(pairs, key=pairs.get)   # first most frequent pair, left to right
        if pairs[best] < 2:
            break
        data = data.replace(best, sym)
        steps.append((best, sym, data))
    return steps


def example_gage():
    print("Example 1: Gage's BPE as compression")
    steps = gage("ABABCABCD", "XY")
    print(f"  {steps[0]}")
    for best, sym, data in steps[1:]:
        print(f"  replace {best} with {sym}: {data}")
    n, subs = 1024, 0
    while n > 1:
        n //= 2
        subs += 1
    print(f"  1,024 identical bytes become 1 after {subs} pair substitutions")
    print()


# ---------------------------------------------------------------------------
# Example 2: BPE on words, on the toy corpus in Sennrich et al.'s Algorithm 1.
# Words are split into characters plus an end-of-word marker. Tie-break: among
# pairs with the highest count, take the first one met, reading the words in
# corpus order and each word left to right.
END = "</w>"
TOY = {"low": 5, "lower": 2, "newest": 6, "widest": 3}


def pair_counts(corpus):
    counts = {}
    for symbols, freq in corpus:
        for a, b in zip(symbols, symbols[1:]):
            counts[(a, b)] = counts.get((a, b), 0) + freq
    return counts


def merge_word(symbols, pair):
    out, i = [], 0
    while i < len(symbols):
        if i + 1 < len(symbols) and (symbols[i], symbols[i + 1]) == pair:
            out.append(symbols[i] + symbols[i + 1])
            i += 2
        else:
            out.append(symbols[i])
            i += 1
    return out


def learn_bpe(words, n_merges):
    corpus = [(list(w) + [END], f) for w, f in words.items()]
    merges = []
    for _ in range(n_merges):
        counts = pair_counts(corpus)
        best = max(counts, key=counts.get)
        merges.append((best, counts[best]))
        corpus = [(merge_word(s, best), f) for s, f in corpus]
        merges[-1] = (best, counts[best], [" ".join(s) for s, _ in corpus])
    return merges


def apply_bpe(word, merges):
    symbols = list(word) + [END]
    for pair, _, _ in merges:
        symbols = merge_word(symbols, pair)
    return symbols


def example_toy_bpe():
    print("Example 2: learning BPE merges on the toy corpus (low 5, lower 2, newest 6, widest 3)")
    base = sorted({c for w in TOY for c in w} | {END})
    print(f"  starting symbols ({len(base)}): {' '.join(base)}")
    merges = learn_bpe(TOY, 10)
    for i, (pair, count, words) in enumerate(merges, 1):
        print(f"  merge {i}: {pair[0]} + {pair[1]} (count {count}) -> {' | '.join(words)}")
    print(f"  vocabulary = {len(base)} starting symbols + {len(merges)} merges = {len(base) + len(merges)}")
    print()
    print("Example 3: applying the merges to words")
    for w in ("lowest", "lower", "newer", "slowest", "widest", "low"):
        print(f"  {w}: {' | '.join(apply_bpe(w, merges))}")
    print(f"  with a word vocabulary of the four training words, 'lowest' is unknown: {'lowest' not in TOY}")
    print()


# ---------------------------------------------------------------------------
# GPT-2's tokenizer, re-implemented with the standard library.
def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gpt2_files():
    CACHE.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, digest in GPT2_FILES.items():
        path = CACHE / f"gpt2-{name}"
        if not path.exists():
            with urllib.request.urlopen(GPT2_BASE + name) as r:
                path.write_bytes(r.read())
        if sha256(path) != digest:
            raise SystemExit(f"{path.name} does not match its pinned hash")
        paths[name] = path
    return paths


def bytes_to_unicode():
    # GPT-2's table from bytes to printable characters (encoder.py).
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, map(chr, cs)))


PRESPLIT = re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?[^\W\d_]+| ?\d+| ?(?:[^\s\w]|_)+|\s+(?!\S)|\s+""")


class GPT2:
    def __init__(self, n_merges=None):
        paths = gpt2_files()
        self.encoder = json.loads(paths["encoder.json"].read_text(encoding="utf-8"))
        lines = paths["vocab.bpe"].read_text(encoding="utf-8").split("\n")[1:]
        merges = [tuple(l.split()) for l in lines if l]
        self.n_all = len(merges)
        if n_merges is not None:
            merges = merges[:n_merges]
        self.ranks = {m: i for i, m in enumerate(merges)}
        self.byte_enc = bytes_to_unicode()

    def bpe(self, piece):
        word = list(piece)
        while len(word) > 1:
            pairs = [(self.ranks.get(p, float("inf")), i, p) for i, p in enumerate(zip(word, word[1:]))]
            rank, _, best = min(pairs)
            if rank == float("inf"):
                break
            word = merge_word(word, best)
        return word

    def tokens(self, text):
        out = []
        for piece in PRESPLIT.findall(text):
            mapped = "".join(self.byte_enc[b] for b in piece.encode("utf-8"))
            out.extend(self.bpe(mapped))
        return out

    def ids(self, text):
        return [self.encoder[t] for t in self.tokens(text)]

    def readable(self, tok):
        dec = {v: k for k, v in self.byte_enc.items()}
        return bytes(dec[c] for c in tok).decode("utf-8", errors="replace").replace(" ", "␣")


THREE_WAYS = "The tokenizer read Kierkegaard in 1843."


def word_split(text):
    return re.findall(r"\w+|[^\w\s]", text)


def example_gpt2():
    print("Example 4: GPT-2's vocabulary and tokenizer")
    g = GPT2()
    print(f"  {len(g.encoder):,} entries = 256 single bytes + {g.n_all:,} merges + 1 special token "
          f"(<|endoftext|> has ID {g.encoder['<|endoftext|>']:,})")
    for text in ("The cat sat on the mat.", THREE_WAYS, "1234567", " 2026", "dog. dog! dog?",
                 " Hello world", " Hallo Welt", " strawberry", " lower", " unbelievably", "защо", "言"):
        toks = g.tokens(text)
        print(f"  {text!r}: {len(toks)} tokens: {' | '.join(g.readable(t) for t in toks)}; IDs {g.ids(text)}")
    print(f"  ' SolidGoldMagikarp' is a single token, ID {g.encoder['ĠSolidGoldMagikarp']:,}")
    single3 = sum(1 for n in range(1000) if len(g.tokens(f"{n:03d}")) == 1)
    print(f"  of the 1,000 strings 000 to 999, {single3} are single tokens")
    words = word_split(THREE_WAYS)
    print(f"  three ways: {len(words)} words and marks, {len(THREE_WAYS)} characters, {len(g.tokens(THREE_WAYS))} GPT-2 tokens")
    print()


def example_tradeoff():
    print("Example 5: vocabulary size against tokens for one sentence (GPT-2's merges, first k only)")
    for k in (0, 10, 100, 1000, 10000, 50000):
        g = GPT2(n_merges=k)
        print(f"  vocabulary {256 + k + 1:,}: {len(g.tokens(THREE_WAYS))} tokens")
    print()


# ---------------------------------------------------------------------------
# Example 6: characters against bytes in UTF-8.
def example_utf8():
    print("Example 6: characters and UTF-8 bytes")
    for w in ("cat", "naïve", "Straße", "привет", "مرحبا", "東京", "😀"):
        print(f"  {w}: {len(w)} characters, {len(w.encode('utf-8'))} bytes")
    print()


# ---------------------------------------------------------------------------
# Example 7: arithmetic on numbers printed in the sources, and number chunking.
def chunks(digits, from_right):
    if from_right:
        head = len(digits) % 3
        parts = ([digits[:head]] if head else []) + [digits[i:i + 3] for i in range(head, len(digits), 3)]
    else:
        parts = [digits[i:i + 3] for i in range(0, len(digits), 3)]
    return " | ".join(parts)


def example_sources():
    print("Example 7: arithmetic on printed numbers")
    print(f"  Gage: default BPE 276,955 / 544,789 bytes = {276955 / 544789:.1%} of the original")
    print(f"  Sennrich et al. Table 1: characters 550m / words 100m = {550 / 100:.1f}; BPE 112m / 100m = {112 / 100:.2f}")
    print(f"  Sennrich et al. rare words: 56 + 21 + 6 + 5 + 1 + 1 = {56 + 21 + 6 + 5 + 1 + 1} of 100")
    print(f"  Wu et al. Table 4: character model 1.0530 s / wordpiece model 0.2118 s = {1.0530 / 0.2118:.2f}")
    print(f"  Llama 3: 3.17 / 3.94 = {3.17 / 3.94:.3f}, about {1 - 3.17 / 3.94:.0%} fewer tokens")
    print(f"  100K + 28K = {100 + 28}K")
    print(f"  1234567 in threes from the left: {chunks('1234567', False)}; from the right: {chunks('1234567', True)}")
    print()


if __name__ == "__main__":
    example_gage()
    example_toy_bpe()
    example_gpt2()
    example_tradeoff()
    example_utf8()
    example_sources()
