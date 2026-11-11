# Claim ledger: depth

Chapter: `depth` (Book 1, "Making deep networks trainable (2010-2016)").
Stage: drafted, 2026-11-11 [D-005].

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
