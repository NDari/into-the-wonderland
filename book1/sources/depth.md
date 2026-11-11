# Claim ledger: depth

Chapter: `depth` (Book 1, "Making deep networks trainable (2010-2016)").
Stage: verified, 2026-11-11 [D-005].

This chapter was split from the planned `toolkit` chapter by D-017, after its research was done. Its sources, claims, and disputes are logged in `book1/sources/toolkit.md` and are not repeated here:

- Claims K15 (initialization), K17-K19 (dropout and its two conventions), K20-K23 (batch and layer normalization), K24-K27 (residual connections, the residual stream, highway networks, the transformer's use of both), K22 (the textbook's 2016 baseline), and K30 (the ResNet and Transformer recipes).
- Disputes D1 (why batch normalization works), D4 (credit for residual connections), and D6 (dropout's p).
- The source table, with URLs and page conventions.

Before drafting, the writer spot-checked K15, K18, K20, K21, K23, K24, K25, and K26 in the same fetched copies.

## Worked examples [D-009]

All computed by `code/checks/depth.py` (standard library, fixed seeds).

- Example 1: the variance of a signal through 10 linear layers of 256 units, starting from 1.
  - The old rule (uniform in plus or minus 1/sqrt(n)) gives 0.332, 0.112, 0.0377, 0.0123, ... down to 1.56e-05. Theory predicts (1/3)^10 = 1.7e-05.
  - Glorot's rule keeps the variance between 0.919 and 1.02.
  - For n = 512, the per-weight variance is 0.000651 under the old rule and 0.001953 under Glorot's; He's rule gives a standard deviation of 0.0625.
- Example 2: dropout.
  - A unit that outputs 2.0 averages 1.0 when kept with probability 0.5. Framework scaling gives 0 or 4.0, averaging 2.0.
  - 2^100 = 1.27e30 thinned networks.
  - For linear regression with a keep probability of 0.8, the average loss over all 64 masks is 4.9044, which equals the ridge-style formula (3.5632 + 1.3412).
- Example 3: normalization.
  - Batch norm on 2, 4, 6, 8 (mean 5, variance 5) gives -1.342, -0.447, 0.447, 1.342. With scale 2 and shift 1 these become -1.683, 0.106, 1.894, 3.683; with scale sqrt(5) and shift 5, the original values return.
  - Layer norm on 2, 1, 0 gives 1.225, 0, -1.225.
- Example 4: residual blocks take [1.00, 2.00] to [1.10, 1.95], [1.08, 2.03], and [1.11, 2.04]. Through 20 layers with slopes in [-0.1, 0.1], the plain chain gives 4.2e-30 and the residual chain 0.58 (illustrative, seed 7).
- Example 5: on MNIST, 1.60% and 0.95% are 160 and 95 errors; batch norm's 31.0/2.1 = 14.8 (printed as "14 times"); ResNet's 152/19 = 8.

## Figures [D-014]

- `figures/depth-init.svg`: Example 1.
- `figures/depth-norm.svg`: Example 3's table, with the batch norm column and the layer norm row.
- `figures/depth-residual.svg`: Example 4, the outline's key figure. `residual_figure()` takes labels and values so that `anatomy` can reuse the layout.

## Terms defined in the chapter

For the glossary: initialization (Glorot or Xavier; He), dropout, thinned network, batch normalization, internal covariate shift (the authors' term), layer normalization, degradation problem, residual (skip) connection, highway network, residual stream (named; defined in `anatomy`).

## Independent check

2026-11-11. A separate agent fetched every source itself (adding highway networks v1 and LLaMA v1) and checked each claim, quote, page, number, and figure. All numbers matched `code/checks/depth.py`, and dispute D1 (batch norm) was judged fair.

- Errors found and fixed:
  1. The degradation quote stopped mid-sentence, dropping "as reported in [11, 42]" (ref. 42 is the highway-network paper). The quote is now complete, with a lead-in.
  2. "Every transformer" used post-norm LayerNorm(x + Sublayer(x)), but LLaMA normalizes sub-layer inputs with RMSNorm. The text now says "the 2017 transformer", with a pointer to `since-2017`, and the summary bullet is softened.
  3. The Santurkar et al. quote is restored with "in a certain sense".
  4. The highway sentence put a concession in He et al.'s mouth. It is now a statement of dates, with both papers building on older shortcuts.
  5. The variance-versus-signal slip is fixed: the variance, not the signal, is multiplied by one third per layer.
- Warnings acted on:
  - Batch norm: "less than half the steps" for batch norm alone, and "14 times fewer" attributed to batch norm with its enabling changes (p. 454).
  - The 2015 winner is described as an ensemble of networks of up to 152 layers.
  - "In full" is dropped from the recipe.
  - Goodfellow's batch norm hedge is restored, and the Transformer dropout rate is marked as the base model's.
  - "Trained very rarely, if at all" for thinned networks, and the ridge check described as probability-weighted.
  - He initialization: twice Glorot's variance, compared with Glorot's rule rather than the old rule.
  - He 2016's sum form now states its identity condition, and He et al. p. 1 is cited for "tens of layers".
  - Batch norm at inference now uses the authors' reason.
  - The "8×" sign, the explanation of 19.4M, and the 0.95% qualifier.
- Not changed: W11 (the Glorot paraphrase) was judged acceptable.
- Re-checked after fixing: the writer located the new quotes in the same fetched texts (He et al. 2015 pp. 1 and 7; Ioffe and Szegedy, BN-Baseline and BN-x5; Santurkar et al. p. 2; Srivastava et al. p. 1931; Goodfellow et al. p. 420).


## Consistency pass (2026-11-11)

Editorial pass to make the chapters agree with each other; no sourced fact, quote, number, or citation changed except where noted.

- Un-bolded "dropout" (first bolded in `deep-turn`) and added a callback link to that chapter.
- Glossed "ensemble" at its first use in the book (bolded later in `seq2seq`).
- "dataset" to "data set" in prose (line 84); the He et al. quotation keeps "dataset", and "mini-batch" stays inside the recipe quotation.

## Style pass (2026-11-11)

Reader call-outs made generic per D-023.

- "For this book's reader, the most useful view is a third one." -> "The most useful view here is a third one, from classical statistics."
- "A reader of the 2000s standardizes features before fitting a model" -> "Standardizing features before fitting a model is routine in statistics"
- "A reader's instinct says a deeper network should overfit" -> "Ordinary statistical intuition says a deeper network should overfit"
- "the reader can read both halves of a modern training recipe" -> "both halves of a modern training recipe are now covered"
