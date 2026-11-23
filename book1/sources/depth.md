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

## Story pass (2026-11-22)

Rewritten per D-025 (concepts first, few names, few quotations) and D-026 (credit questions to the `credit` appendix). No claim was added; every citation key and page of the earlier text is still cited, in the chapter or in the appendix (checked by script against the committed version). Quotation marks fell from 90 to 22, and block quotations from 2 to 1; the chapter from 3,476 to 3,404 words. All headings, bold terms, numbers, figures, captions, HTML comments, cross-chapter links, and the "What to carry forward" list are unchanged.

- Moved to `credit` (section "Making deep networks trainable", `#credit-depth`): the credit half of the highway-network paragraph, that is, He et al.'s "concurrent with our work" (p. 2), Schmidhuber's "a version (with open gates) of our earlier Highway Net (May 2015)" (schmidhuber2022annotated p. 12), and the sentence on the dates (May and December 2015, older shortcut connections, he2015deep p. 2). The concept stays in the chapter, because the glossary's "highway networks" entry points here: the bold term, the learned gate, the 900 layers (srivastava2015highway p. 1), and the difference that a highway gate can close while the identity shortcuts never do (he2015deep p. 2). One neutral sentence links to the appendix.
- Names dropped from the prose, the citation now carrying them: Sergey Ioffe and Christian Szegedy (now "a paper" in 2015, and "the batch normalization paper (reference 16)" in the recipe); Shibani Santurkar (now "a 2018 study"); Nitish Srivastava (now "the 2014 journal version of dropout" and "the 2014 paper"); Jimmy Ba, Jamie Kiros, and Hinton as authors of layer normalization (now "a variant from 2016"); Goodfellow, Bengio, and Courville (now "the 2016 deep learning textbook"); Xiangyu Zhang, Shaoqing Ren, and Jian Sun (now "Kaiming He and colleagues"); Rupesh Srivastava, Klaus Greff, and Jürgen Schmidhuber (only in the appendix now). Kept: Glorot and Bengio (the rule is named after Glorot, "Xavier" after his first name, and `deep-turn` names him), Kaiming He (He initialization, and he recurs as ResNet's first author), Hinton (dropout; recurs across the book).
- Quotations turned into close paraphrase, same source and page: Glorot and Bengio's objective and the sigmoid's saturation (p. 249, keeping "understand better" and "especially"); He et al. 2015a on "extremely deep models (e.g., 30 conv/fc layers)" (p. 3); Hinton et al. on omitting units, co-adaptations (p. 1), and halved weights (p. 2); PyTorch on "with probability p" and "1/(1-p)"; Srivastava et al. on 2^n thinned networks, "very rarely, if at all" (p. 1931), and "2-3 times longer" (p. 1952, keeping "typically"); Ioffe and Szegedy on the changing input distribution (p. 448), the identity transform (p. 450), inference (p. 451), "less than half the number of training steps" and "14 times fewer" (pp. 448, 454), and dropout (p. 449); Santurkar et al. on distributional stability and the smoother landscape (p. 1), and "in a certain sense ... might not even" (p. 2, hedges kept); Ba et al. on batch size and recurrent networks, the summed inputs (p. 1), and identical training and test computation (pp. 1-2); He et al. 2015b on "tens of layers" and the degradation passage, formerly a block quotation (p. 1, keeping "might be unsurprising", "unexpectedly", and "as reported in" earlier work including the highway paper), the constructed solution (p. 1, kept as their argument, "indicates ... should"), "push the residual to zero" (p. 2), "neither extra parameter nor computational complexity" (p. 2), "8x deeper" (p. 1), and "may be unnecessarily large (19.4M)" (p. 8, keeping "may"); He et al. 2016 on the sum of residual functions (pp. 3-4) and the gradient that "does not vanish" (p. 4); Goodfellow et al.'s 2016 baseline and warning (p. 420, keeping "likely").
- Quotations kept, because the wording itself is the point: "Xavier" (the name); "dropout 0.8" (an example of recipe wording); "thinned" (the term); the ridge-regression equivalence (Srivastava et al. p. 1950, the claim the chapter then checks by brute force); "We refer to this phenomenon as internal covariate shift ..." (Ioffe and Szegedy p. 448, the term coined there and the account the dispute examines); "exceeding the accuracy of human raters" (p. 448, the authors' claim, which the chapter qualifies); "adaptive reparametrization" (Goodfellow et al. p. 313, the textbook's term); "degradation problem" (He et al. p. 1, the term); "LayerNorm(x + Sublayer(x))" (Vaswani et al. p. 3, the exact form); the ResNet recipe block quotation (He et al. p. 4, the text the section reads).
- Added for the reader, no new claim: "The correction $F(x)$ is the residual" (He et al. p. 2 names F the residual mapping); a gloss of "optimization landscape" as the shape of the loss over all the weights.
- Dropped as unneeded: the bracketed reference numbers "[11, 42]" of the degradation quotation (the paraphrase says "earlier work, including the highway-network paper").

## Independent check (story pass, 2026-11-22)

By an agent that did not write the story pass. Compared the committed chapter (`git show HEAD`) with the rewrite, sentence by sentence, against the quotes in `book1/sources/toolkit.md` (K15, K17-K26, D1, D4). Re-fetched in this session and located: Ioffe and Szegedy (PMLR PDF), "less than half the number of training steps" (BN-Baseline, p. 454) and "regularizes the model and reduces the need for Dropout" (p. 449); He et al. 2015 (arXiv v1), "networks with tens of layers to start converging" (p. 1); Goodfellow et al., guidelines chapter, "should be introduced quickly if optimization appears to be problematic", "Early stopping should be used almost universally", and the "progresses quickly" warning (p. 420). Everything else was checked against the ledger quotes only.

- By script: every citation key and page of the committed chapter is still cited in the chapter or in the `credit` draft; no key or page was added. Bold terms, HTML comments, figures, captions, and cross-chapter links are unchanged (plus the new `#credit-depth` link). Names dropped are named elsewhere only in `timeline`, `further-reading`, and `credit`; no later chapter refers back to them.
- Fixed, meaning:
  1. Batch normalization's motivation: the rewrite stated the shifting input distribution in the narrator's voice and dropped the authors' claim that it makes training harder ("is complicated by", p. 448). Now "In their account, training is harder because ...".
  2. Layer normalization's two objections to batch normalization (Ba et al. p. 1) had moved into the narrator's voice; now attributed to its authors.
  3. Highway networks, 900 layers: the authors' "we found" had become a narrator's statement; now "Their authors reported". "Residual connections had a predecessor" implied the lineage that the `credit` entry leaves open; now "A related design had appeared earlier in 2015".
  4. Recipe: the batch normalization paper "had found" became "had reported" (the source asserts it).
- Fixed, near-verbatim unquoted text reworded: Glorot and Bengio's objective and the sigmoid's saturation (p. 249); Hinton et al. on omitted units, co-adaptations ("what they called"), and halved weights (pp. 1-2); Srivastava et al. on 2^n thinned networks (p. 1931) and training time (p. 1952); Santurkar et al. pp. 1-2 (also removed a doubled "even"); Ba et al. on the summed inputs and identical computation (pp. 1-2); He et al. 2015 on tens of layers, the degradation passage, the constructed solution (p. 1), and the cost of shortcuts (p. 2); He et al. 2016 on the gradient (p. 4); the batch normalization paper on dropout (p. 449); the textbook's "excellent regularizer" (p. 420, now "which it rated").
- Appendix draft (`credit-depth`): checked against K26 and D4. It gives He et al.'s "concurrent" and the closed-gate distinction, Schmidhuber's "a version (with open gates)", and the undisputed dates, each cited; it picks no winner. No change.
- The "Story pass" entry above is accurate, except that the bold term "layer normalization" is now capitalized as a sentence start, and the dates of May and December 2015 left the chapter with the credit paragraph.
- Not changed, for the author: the glossary entry "highway networks" still says "a predecessor of residual connections" (outside this check's files).
- After the fixes: `python3 tools/check.py` 0 errors; `python3 build/build.py depth` builds.
