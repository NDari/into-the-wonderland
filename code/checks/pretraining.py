#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `pretraining` [D-009].

Run: python3 code/checks/pretraining.py
Standard library only. Every number printed in the chapter comes from this
output. All inputs are numbers printed in the papers cited in
book1/sources/pretraining.md; derived quantities are labelled as such.
"""

SENTENCE = "The cat sat on the sofa because it was warm".split()
MASKED = {"sat", "sofa"}


def example_objectives():
    print("Example 1: what each objective learns from one sentence (whole words as tokens)")
    n = len(SENTENCE)
    print(f"  sentence: {' '.join(SENTENCE)} ({n} words)")
    print(f"  next-token: {n - 1} predictions, each from the words to its left")
    masked_input = ["[MASK]" if w in MASKED else w for w in SENTENCE]
    print(f"  masked: input {' '.join(masked_input)}; {len(MASKED)} predictions ({len(MASKED) / n:.0%} of positions), "
          f"each from both sides")
    print()


def example_bert_masking():
    print("Example 2: BERT's masking on a 512-token input (expected values)")
    n = 512
    chosen = 0.15 * n
    print(f"  15% chosen: {chosen:.1f}; of these 80% [MASK] {0.8 * chosen:.2f}, 10% random {0.1 * chosen:.2f}, "
          f"10% unchanged {0.1 * chosen:.2f}")
    print(f"  per token: [MASK] {0.15 * 0.8:.1%}, random {0.15 * 0.1:.1%}, unchanged {0.15 * 0.1:.1%}, not predicted {1 - 0.15:.0%}")
    print(f"  a next-token model gets a prediction at every position: {n} (versus {chosen:.1f})")
    print()


def example_bert_tokens():
    print("Example 3: tokens BERT saw in pretraining (derived from the paper's figures)")
    per_batch = 256 * 512
    print(f"  256 sequences x 512 tokens = {per_batch:,} per batch (paper: 128,000)")
    all512 = 1_000_000 * per_batch
    actual = 900_000 * 256 * 128 + 100_000 * 256 * 512
    print(f"  1,000,000 steps all at 512 tokens: {all512 / 1e9:.1f}B positions, {all512 / 3.3e9:.1f} passes over 3.3B words")
    print(f"  with 90% of steps at 128 tokens: {actual / 1e9:.1f}B positions, {actual / 3.3e9:.1f} passes")
    print()


def example_cost():
    print("Example 4: pretraining against fine-tuning cost (derived)")
    base, large = 16 * 96, 64 * 96
    print(f"  BERT-base pretraining: 16 chips x 4 days = {base:,} chip-hours; BERT-large: 64 x 4 days = {large:,}")
    print(f"  fine-tuning: at most 1 hour on one Cloud TPU (4 chips) = 4 chip-hours; ratio for BERT-large {large // 4:,} to 1")
    print(f"  GPT-1: 8 GPUs x about 30 days = {8 * 30} GPU-days")
    print(f"  BERT-base classifier for 3 labels: 3 x 768 = {3 * 768:,} new weights, {3 * 768 / 110e6:.4%} of 110M")
    print()


def rel_err_score(old, new):
    return (new - old) / (100 - old)


def rel_err_error(old, new):
    return (old - new) / old


def example_relative():
    print("Example 5: relative error reduction")
    print(f"  ELMo, SQuAD F1 81.1 -> 85.8: {85.8 - 81.1:.1f} points; relative error reduction {rel_err_score(81.1, 85.8):.1%}")
    print(f"  ELMo, SNLI 88.0 -> 88.7: {rel_err_score(88.0, 88.7):.1%}")
    print(f"  ULMFiT, IMDb error 5.9 -> 4.6: {rel_err_error(5.9, 4.6):.1%}; against CoVe 8.2 -> 4.6: {rel_err_error(8.2, 4.6):.1%}")
    for name, old, new in (("AG", 6.57, 5.01), ("DBpedia", 0.84, 0.80), ("Yelp-bi", 2.64, 2.16),
                           ("Yelp-full", 30.58, 29.98), ("TREC-6", 3.9, 3.6)):
        print(f"  ULMFiT, {name} {old} -> {new}: {rel_err_error(old, new):.1%}")
    print(f"  ELMo SRL: 486 epochs -> 10: {1 - 10 / 486:.1%} fewer updates")
    print(f"  Dai and Le, Rotten Tomatoes error 20.3% -> 16.7%: accuracy {100 - 20.3:.1f}% -> {100 - 16.7:.1f}%")
    print()


def example_ablations():
    print("Example 6: ablations")
    print(f"  GPT-1 without pretraining: 74.7 -> 59.9, {74.7 - 59.9:.1f} points, {(74.7 - 59.9) / 74.7:.1%} relative")
    print(f"  GPT-1 with an LSTM: 74.7 -> 69.1, {74.7 - 69.1:.1f} points")
    base = {"MNLI": 84.4, "QNLI": 88.4, "MRPC": 86.7, "SST-2": 92.7, "SQuAD": 88.5}
    no_nsp = {"MNLI": 83.9, "QNLI": 84.9, "MRPC": 86.5, "SST-2": 92.6, "SQuAD": 87.9}
    ltr = {"MNLI": 82.1, "QNLI": 84.3, "MRPC": 77.5, "SST-2": 92.1, "SQuAD": 77.8}
    print("  BERT without next-sentence prediction: " + ", ".join(f"{k} {no_nsp[k] - base[k]:+.1f}" for k in base))
    print("  left-to-right instead of masked (both without NSP): " + ", ".join(f"{k} {ltr[k] - no_nsp[k]:+.1f}" for k in base))
    print(f"  BERT masking recipes, MNLI range: {84.4 - 83.6:.1f} points across six recipes")
    print()


def example_t5():
    print("Example 7: T5 span corruption on 512 tokens (expected values)")
    corrupted = 0.15 * 512
    spans = corrupted / 3
    print(f"  15% corrupted = {corrupted:.1f} tokens in about {spans:.1f} spans of mean length 3; "
          f"target about {corrupted + spans + 1:.0f} tokens instead of 512")
    print(f"  T5 final pretraining: 2,048 x 512 x 1,000,000 = {2048 * 512 * 1_000_000:.3e} tokens")
    print()


if __name__ == "__main__":
    example_objectives()
    example_bert_masking()
    example_bert_tokens()
    example_cost()
    example_relative()
    example_ablations()
    example_t5()
