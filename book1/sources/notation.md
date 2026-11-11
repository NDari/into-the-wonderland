# Ledger: notation

Chapter: `notation` (Book 1, appendix A, "Notation and math refresher").
Stage: verified, 2026-11-11 [D-005]. Compiled by a drafting agent from the verified chapters; independent check and post-consistency-pass update recorded at the end.

## Method

The appendix states standard textbook mathematics only (vectors, matrices, logarithms, probability, entropy, softmax, the logistic function) and makes no historical or quantitative claims about named papers or systems, so it cites no sources. Where it mentions a figure from a chapter (the KV-cache size, the scaling exponent 0.076, the doubling time of 207 days, the Elo scale of 400 points), the figure is the chapter's own, already verified and cited there; the appendix only recomputes it.

1. Inventory. A throwaway script (not in the repository) listed every inline and display math span in the 25 Book 1 chapter files, with line numbers, plus plain-text formulas and unit words (powers of ten written as text, "softmax", "log", "nats", "bits per", KiB, MiB, GiB). It found math in 22 of the 25 chapters (none in `pretraining`, `seq2seq`, `tokens`) 354 spans in all. A second pass collected unit usage (GB, GiB, MB, MiB, KB, KiB, TB) and the multiplication signs used in prose.
2. Conventions. From the inventory, the notation actually used was listed (below, "Notation inconsistencies found", covers the conflicts). The appendix covers only what appears in the chapters; transposes, determinants, eigenvectors, integrals, and continuous distributions do not appear and are left out.
3. First use. The "First used" column of the symbol tables was checked with a second throwaway script that finds, for each symbol, the first chapter in OUTLINE.md order whose math spans contain it. Every mismatch it reported was a different meaning of the same letter, already a separate row. One row is a judgment call: $\Delta$ is first used inside a quotation in `instructions` (line 67, "Δ(Elo Score)"), before its first use in math in `adapting`; the table gives `instructions`.
4. Numbers. Every number in the appendix's prose and the first table is printed by `code/checks/notation.py` [D-009]. A scratch comparison of the numbers in the appendix text against the script's output found none missing except the scores 3.0, -1.0, and -2.0 (printed by the script as 3, -1, -2) and the year in a chapter's title.
5. Build. `python3 build/build.py notation` gave 12 pages in the first draft: about 8 of text and 4 of symbol tables. A single symbol table did not fit on one page (Pandoc's Typst output puts each table in a figure, which does not break across pages), so it was split into four tables, each checked by eye in the rendered PDF. After the update recorded at the end it gives 13 pages: 8 of text and 5 of symbol tables, each table page 81% to 97% full.

## Worked examples used

All from `code/checks/notation.py`. Examples that repeat a chapter's example reuse that chapter's script, so the numbers cannot drift apart.

| Example | Appendix section | What it computes | Reused from |
|---|---|---|---|
| 1 | Numbers and units | powers of 2; $10^{-8}$; $\pi$; GPT-3's $6ND$; memory for 8 billion parameters at 32, 16, 8, 4 bits in GB and GiB; Llama 3 8B KV cache per token (131,072 bytes = 128 KiB) and per 131,072-token window (17.2 GB = 16 GiB); the GiB figure as a number 6.9% smaller than the GB figure; the score tables of `since-2017` in MiB and MB (for inconsistency 4 below) | arithmetic restated from `generation.py` Example 5 and `scale.py` Example 2 |
| 2 | Vectors and dot products | dot product, lengths, and cosine of "cat" and "dog" (0.990), "cat" and "car" (0.303); doubling invariance; one-hot distance 1.414; the neuron's vote as $w \cdot x + b$ = 0.1 | vectors read from `embeddings.py` (TOY, Example 2) without executing it, since it needs numpy; vote weights imported from `neuron.py` |
| 3 | Matrices | a 2 by 3 matrix times a vector, in both orders; GPT-2 small feed-forward parameter count 4,722,432 (matches `anatomy.py` Example 1); a rank-1 product; LoRA rank 8 on 4,096 by 4,096 (65,536 numbers, 0.39%, matches `adapting.py` Example 1) | new |
| 4 | Logarithms | ln 2, bits per nat, the destination chapter's text probability $8.222 \times 10^{-6}$ as a sum of logs (16.89 bits, 11.71 nats; 2.815 bits = 1.951 nats per token); $2^{-0.076}$ and $10^{-0.076}$; $2^{365/207}$ | chain from `destination.py` (CHAIN, softmax) |
| 5 | Probability | fair and loaded die entropy (2.585, 2.161 bits), perplexity (6.00, 4.47), cross-entropy under a fair-die model (2.585) and KL (0.424); destination text perplexity 7.04 from bits and from nats; SE at p = 0.8, n = 164 (6.12 points, matches `evaluation.py` Example 1) | `prediction.py` (entropy, cross_entropy, log2) and `destination.py` |
| 6 | Softmax and temperature | the destination chapter's softmax table; shift invariance; temperature 0.5, 1, 2 (0.831, 0.571, 0.375; 0.86, 1.70, 2.23 bits); two-score softmax equals the logistic of the difference (0.599, the router example of `since-2017.py`); a masked score | `destination.py` (softmax), `generation.py` (softmax_t, entropy_bits), `neuron.py` (sigmoid) |
| 7 | Logistic function | $\sigma$ at -2, -1, 0, 0.1, 1, 2; symmetry; log-odds of 0.731 = 1.000; Elo 400-point gap (0.909) and 173.7 Elo points per natural log-odds unit (matches `instructions.py` Example 2); log loss 0.313 and 0.693 (matches `instructions.py` Example 1) | `neuron.py` (sigmoid) |

## Notation inconsistencies found

For the coordinator. Line numbers are as of 2026-11-11, before the consistency pass. Each item gives the file and line, the two usages, and a suggested fix. The drafting pass edited only the appendix, its script, and this ledger; the consistency pass then changed the chapters. Each item ends with its status, checked against the chapter files after that pass. Items are in rough order of importance.

1. **$\sigma$ used undefined for a standard deviation.** `book1/chapters/toolkit.md:23` writes the standard error of a mean as $\sigma/\sqrt{n}$ and `toolkit.md:29` repeats it in a table header, but never says what $\sigma$ is. Everywhere else $\sigma$ is the logistic function, introduced at `neuron.md:43` and used at `instructions.md:59-61`, `since-2017.md:35`, and `frontier.md:83-85`. This also breaks D-002's "every symbol explained". Suggested fix at `toolkit.md:23`: "the standard error of a mean estimated from $n$ samples is $\sigma/\sqrt{n}$, where $\sigma$ is the standard deviation of a single sample (here, of one example's gradient; not the logistic function of [the neuron chapter](#neuron))". **Resolved:** `toolkit.md:23` now defines $\sigma$ as the standard deviation of a single sample, not the logistic function.

2. **Two symbols for one quantity in one chapter.** `book1/chapters/frontier.md:83-85` calls a model's time horizon $h$; `frontier.md:91-93` calls the same horizon $H$ (and $H_0$ at the start). $H$ is also entropy and cross-entropy at `prediction.md:37` and `prediction.md:129`. Suggested fix: at `frontier.md:91` write $h = h_0 \times 2^{d/T}$, and at `frontier.md:93` "where $h_0$ is the horizon at the start ... and $h$ the horizon after $d$ days". **Resolved:** `frontier.md:91-93` now writes $h = h_0 \times 2^{d/T}$.

3. **The dot $\cdot$ means three different operations.** It is the dot product of two vectors at `embeddings.md:23-25` and `attention.md:25-27`. It is ordinary multiplication of two numbers at `frontier.md:83`, $(\log h - \log t) \cdot \beta$. It is a number times its own sigmoid, entry by entry, at `since-2017.md:35`, $x \cdot \sigma(x)$. And it is a vector times a matrix at `since-2017.md:129`, $\text{TopK}(x \cdot W_g)$, where the same chapter (`since-2017.md:37`, $x W$) and `anatomy.md:31` ($x W_1$) write that product with no sign. A reader who has just learned that $\cdot$ is a dot product will misread the last one. Suggested fixes: `since-2017.md:129` write $\text{TopK}(x W_g)$; `frontier.md:83` write $\beta\,(\log h - \log t)$; `since-2017.md:35` write $x\,\sigma(x)$. **Resolved in the chapters:** `since-2017.md:35` writes $x\,\sigma(x)$, `since-2017.md:129` writes $\text{TopK}(x W_g)$, and `frontier.md:83` writes $(\log h - \log t) \times \beta$; in the 25 chapters $\cdot$ is now only the dot product. **Not resolved** in the glossary appendix: the Swish entry of `glossary.md` still writes $x \cdot \sigma(x)$; outside this pass's files.

4. **Binary units used before (or without) definition, and mixed with decimal ones.** `book1/chapters/since-2017.md:81` gives "128 KiB per token" and "16 KiB", then window sizes in decimal GB (68.7, 17.2, 2.1 GB) in the same paragraph; `since-2017.md:87` gives "2 MiB", "128 MiB", "32 GiB", and "32 MiB". KiB and MiB are defined in no chapter; GiB is first defined at `local.md:124`, the next chapter. The generation chapter, which `since-2017.md:81` cites, gives the same per-token figure as "131,072 bytes" (`generation.md:81`), and the book's convention is decimal GB (`destination.md:117`, `local.md:59`). Suggested fix, either (a) keep the binary units and define them at first use, `since-2017.md:81`: "128 KiB (131,072 bytes; a KiB is 1,024 bytes, a MiB 1,024 KiB, a GiB 1,024 MiB) per token", or (b) switch to decimal units, as `notation.py` Example 1 prints them: at `since-2017.md:81` "131,072 bytes per token", "16,384 bytes"; at `since-2017.md:87` "2.1 MB at 1,024 tokens, 134.2 MB at 8,192, and 34.4 GB at 131,072, while the output ... is only 33.6 MB". Option (b) matches the rest of the book; if chosen, `code/checks/since-2017.py` Example 7 should print the decimal figures. **Resolved, option (b):** `since-2017.md:81` and `:87` now use decimal units only (131,072 bytes, 16,384 bytes, 2.1 MB, 134.2 MB, 34.4 GB, 33.6 MB), and `:85` writes "192 kB". GiB remains only at `local.md:124`, where it is defined. `code/checks/since-2017.py:161` still prints a KiB figure alongside bytes; the chapter does not print it.

5. **Logarithm base not stated.** `book1/chapters/instructions.md:61` ($-\log \sigma(r_w - r_l)$) and `instructions.md:83` ($\beta \log$ of a ratio) do not say which logarithm; the chapter's numbers (0.693 at `instructions.md:133`, "nats" at `instructions.md:85`) show it is the natural one. Elsewhere the base is explicit: $\log_2$ at `prediction.md:37`, $\log_{10}$ at `tools.md:27`, "natural logarithms" in words at `scale.md:31` and `training.md:41`. Suggested fix: at `instructions.md:61` add "(natural logarithms throughout this chapter, so log-ratios are in nats)". Separately, `frontier.md:83` ($\log h - \log t$) gives no base. The base does not change the model's predictions but does change the value of the fitted slope $\beta$; if the chapter ever quotes a value of $\beta$, the base should be checked against `kwa2025measuring` and stated. Not checked here. **Resolved for `instructions`:** `instructions.md:61` now says "natural logarithms throughout this chapter, so log-ratios are in nats". **Not changed:** `frontier.md:83` still gives no base; the appendix says the base changes only the size of the fitted slope.

6. **Bold vector in one formula only.** `book1/chapters/since-2017.md:21` and `:23` write the vector as bold $\mathbf{a}$. Every other chapter writes vectors in plain italics ($a$, $b$ at `embeddings.md:23`; $q$, $k_j$ at `attention.md:25`; $x$ at `anatomy.md:31`), and so does the same chapter elsewhere ($x$ at `since-2017.md:37` and `:129`). Suggested fix: write $\text{RMS}(a)$ unbolded at `since-2017.md:21` and `:23`. If changed, update the appendix's symbol table row "$\text{RMS}(\mathbf{a})$" and the remark in its "Vectors and dot products" section. **Resolved:** `since-2017.md:21-23` writes plain $a$; the appendix's remark and table row were updated.

7. **$n$ used for two things in one chapter.** In `book1/chapters/since-2017.md:21-23`, $n$ is the length of the vector being normalized; in `since-2017.md:129-131`, $n$ is the number of experts. Suggested fix: write the RMS formula with $d$ for the vector's length (matching $d$ for widths elsewhere), $\sqrt{\frac{1}{d} \sum_{j=1}^{d} a_j^2}$, with "$d$ its length" at `:23`. **Resolved:** RMSNorm now uses $d$, "its number of entries"; $n$ in `since-2017` is only the number of experts.

8. **$d$ for a head's size versus the model's width.** `book1/chapters/attention.md:77` uses $d$ for the whole vector of a token (512 in the 2017 transformer) and $d_k$ (`attention.md:27`) for the numbers in one key, that is, in one head. `book1/chapters/since-2017.md:57` uses plain $d$ for the numbers in one head ("a head of $d$ numbers"). Suggested fix: `since-2017.md:57` write $\theta_i = 10000^{-2(i-1)/d_k}$ and "the $d_k/2$ pairs in a head of $d_k$ numbers". Low priority: the RoPE paper writes $d$, and the sentence defines it. **Resolved:** `since-2017.md:57` now uses $d_k$, with a pointer to the attention chapter.

9. **Capitalized Softmax.** `book1/chapters/since-2017.md:129` writes $\text{Softmax}$ (and $\text{TopK}$); `attention.md:25` writes $\text{softmax}_j$ and all prose uses "softmax". Suggested fix: lowercase $\text{softmax}$ at `since-2017.md:129`. **Resolved:** `since-2017.md:129` writes lowercase $\text{softmax}$.

10. **Two orders for matrix times vector.** `book1/chapters/anatomy.md:31` and `since-2017.md:37`, `:129` put the vector on the left ($x W_1$, $x W$, following the transformer paper); `adapting.md:49` puts it on the right ($h = W_0 x + BAx$, following the LoRA paper, with $W_0$ described as $d$ rows by $k$ columns at `adapting.md:45`). Both are correct for their sources, and the appendix's "Matrices" section explains both. Optional fix: a clause at `adapting.md:49`, "(LoRA writes the input on the right of the matrix; [the anatomy chapter](#anatomy) wrote it on the left; see [the appendix on notation](#notation))". **Not changed** in the chapters (optional). The appendix explains both orders, and its "Matrix times matrix" sentence now says which order it assumes.

11. **Same letter, another chapter's meaning, defined in place.** Each is explained where it is used, so no change is required; the appendix's symbol tables list every meaning. Listed in case the coordinator wants fewer collisions. **Not changed**, except $H$ in `frontier` (now $h$, item 2), which removes one collision.
    - $T$: temperature at `generation.md:53-59`; doubling time in days at `frontier.md:91-93`. Optional: `frontier.md:91` could give the doubling time in words or as $T_2$.
    - $d$: width at `attention.md:77`; Arena-score difference at `evaluation.md:87-91`; days at `frontier.md:91-93`; a document at `tools.md:27-29`. Optional: `evaluation.md:89` could use $\Delta$, as in the Anthropic quotation at `instructions.md:67`.
    - $t$: time step at `structure.md:98-102`; confidence threshold at `prompting.md:140` and `evaluation.md:115`; a word at `tools.md:27-29`; a task's human time at `frontier.md:83-85`.
    - $N$: words in a text at `prediction.md:127-131`; parameters at `anatomy.md:62`, `scale.md:35-45`, `local.md:57-59`; documents at `tools.md:27-29`; disks at `frontier.md:57`.
    - $\beta$: KL penalty strength at `instructions.md:83-85` and `:131-133`; a fitted slope at `frontier.md:83-85`.
    - $\alpha$: momentum at `toolkit.md:55`; the exponent $\alpha_N$ at `scale.md:35-37`; LoRA's "alpha" (in words) at `adapting.md:49`.
    - $A$, $B$: sounds at `prediction.md:81`; LoRA matrices at `adapting.md:47-55`; advantage $A_i$ at `frontier.md:33-35`; bandwidth $B$ at `local.md:193-195`.
    - $W$: words at `prediction.md:81`; weight matrices at `anatomy.md:31`, `adapting.md:45`, `since-2017.md:37`.
    - $L$: loss at `backprop.md:41` and `scale.md:35`; largest integer at `local.md:71-73`.
    - $b$: bias at `neuron.md:33`; bits per weight at `local.md:57-59`; a BM25 setting at `tools.md:35-41`.
    - $s$: LSTM cell value at `structure.md:98-102`; quantization scale at `local.md:71-73`.
    - $q$: query at `attention.md:23`; stored integer $q_i$ at `local.md:71-73`.
    - $h$: LoRA layer output at `adapting.md:49`; time horizon at `frontier.md:83`.
    - $r$: LoRA rank at `adapting.md:49`; rewards at `instructions.md:59-61` and `frontier.md:33-35`.
    - $G$: group size at `frontier.md:33-35`; router weights $G(x)$ at `since-2017.md:129-131`.
    - $k$: key $k_j$ at `attention.md:25`; columns at `adapting.md:45`; number of examples at `prompting.md:52`; BM25 $k_1$ at `tools.md:35`.
    - $w$, $w_i$: weights at `neuron.md:33`, `backprop.md:41`, `local.md:71`; words $w_1 \ldots w_N$ at `prediction.md:129`; BM25 term weight at `tools.md:35`.
    - $H$: entropy at `prediction.md:37` and cross-entropy at `prediction.md:129` in the same chapter (the text says which; the appendix writes the general cross-entropy as $H(p, q)$).

12. **Notes, no change suggested.** **Not changed.** One update: `frontier.md:83` and `:91` now use $\times$ inside formulas, as the appendix's convention says.
    - `since-2017.md:37-39` writes the entry-by-entry product as $\otimes$, following Shazeer's paper. Many texts write $\odot$ and keep $\otimes$ for the outer (Kronecker) product. The chapter defines it in place; the appendix says the symbol follows its source.
    - `instructions.md:83-85` writes a model's probability as $\pi(y \mid x)$ (from InstructGPT), where `prediction.md:129` writes $P(\ldots)$. The appendix explains $\pi$ as a policy, not 3.14159.
    - Prose writes multiplication as a letter "x" (`adapting.md:51`, `scale.md:45`, `instructions.md:133`) and shapes as "by" (`adapting.md:45-51`) or "x" (`anatomy.md:47-48`); the sign "×" appears only inside quotations (`depth.md:84`, `depth.md:94`, `toolkit.md:123`, `since-2017.md:93`, `since-2017.md:159`, `adapting.md:69`). The appendix states the convention. Consistent enough.
    - `depth.md:38` already flags that dropout's $p$ means "keep" in one convention and "drop" in another.

## Independent check (notation appendix)

2026-11-11. A separate agent recomputed every number in the appendix independently of `code/checks/notation.py`, compared each against the chapters it repeats, checked all 111 rows of the symbol tables against the math spans of the 25 chapters (meaning and first chapter in reading order), and read the rendered PDF.

- Errors found and fixed:
  1. The logistic function was called "the link function" of logistic regression; the link is the logit, its inverse. Now "the curve that turns the weighted sum of the reader's logistic regression into a probability (the inverse of its logit link)"; the neuron chapter's 0.1 and 0.525 re-checked against `neuron.md:27` and `:47`.
  2. The gates bullet said the SwiGLU layer uses sigmoids as switches between 0 and 1; its switch is Swish, $x\,\sigma(x)$, which is not limited to 0 to 1. Split into two sentences, the second saying so.
  3. The KL divergence of the appendix (model against truth) was said to be "what" the KL penalty keeps small; the penalty measures two models against each other. Now "uses the same measure between two models, the one being trained and the one it started from".
  4. "Multiplying a vector by $B A$ is the same as multiplying it by $A$ first and then by $B$" holds only with the vector on the right; now says so ("as LoRA writes it").
  5. Row $a \cdot b$ said "in two chapters, plain multiplication"; after the consistency pass the chapters use the dot only for the dot product. Now "dot product".
  6. Row $n$ for `since-2017` said "length of a vector; number of experts"; the chapter now uses $d$ for the length. Now "number of experts".
  7. The logistic-function section had no "Used in" line, unlike every other section. Added, listing the 11 chapters that use the sigmoid, the logistic function, or tanh (`neuron`, `backprop`, `structure`, `deep-turn`, `depth`, `embeddings`, `generation`, `instructions`, `since-2017`, `evaluation`, `frontier`), each confirmed by search. `toolkit` is left out: its $\sigma$ is a standard deviation.
- Warnings acted on: the "First used" column gives short chapter titles as link text instead of raw IDs; the Meaning column is left-aligned; the opening's "every symbol in the book" became "every letter, sign, and named function in the book's formulas", and rows were added for the named functions (see the update below); "width or length in numbers" became "width, or the number of its entries"; the GiB figure is now printed by `notation.py` Example 1 ("a number 6.9% smaller"), and the text gives 6.9% instead of "about 7%"; tanh is "a sigmoid stretched to run from -1 to 1"; the claim in "Reading the formulas" that every formula is followed by the meaning of its symbols now holds, since `toolkit` defines $\sigma$. Float gaps: the symbol tables were regrouped into five tables of 21 to 29 rows, with the "First used" column wide enough that names do not wrap, so each table page is 81% to 97% full; no raw Typst was used [D-003].

## Update after the consistency pass

2026-11-11. The math-span inventory was re-run over the 25 chapters after the consistency pass (360 spans, against 358 before) and diffed against the earlier dump. Every difference traces to a change listed under "Notation inconsistencies found" above. Rows changed in the symbol tables:

- $a_i$, $\bar{a}_i$ became $a$; $a_i$, $\bar{a}_i$ ("a vector; its entry $i$, before and after normalization"), since RMSNorm now names the vector $a$.
- $\text{RMS}(\mathbf{a})$ became $\text{RMS}(a)$; the remark on the bold vector in "Vectors and dot products" was removed.
- $d$: "dimension of a vector: the number of its entries (the model's width)"; "size of an attention head" moved to $d_k$, which `since-2017` now uses for it.
- $H$, $H_0$ (time horizon) removed; the `frontier` row is now $h$, $h_0$.
- $n$ in `since-2017`: "number of experts" only.
- $a \cdot b$: "dot product" only.
- $\Delta$ removed: in formulas it appears only as $\Delta W$ (`adapting`), already a row; its use in `instructions` is inside a quotation.
- $\log_2$, $\log_{10}$ split into two rows, each with its own first chapter.
- $\lvert w \rvert$; round split into three rows: $\lvert w \rvert$, $\max_j$ (largest value, `local`), round.
- BM25 row: "its idf part" (shorter, so the row does not wrap).
- Added: $\ldots$ (`neuron`), $\sqrt{n}$ (`toolkit`), $\times$ (`depth`), softmax (`destination`, where it is defined; its first appearance inside a formula is in `attention`), $\cos(a, b)$ (`embeddings`), $\text{FFN}(x)$ (`anatomy`), $\text{tf-idf}(t, d)$ (`tools`), $\text{Swish}(x)$ and $\text{TopK}$ (`since-2017`), $\mathrm{mean}$, $\mathrm{std}$ (`frontier`).
- Unchanged rows whose chapter text changed: $\sigma$ (standard deviation, `toolkit`, now defined there); $\max(0, z)$ (`anatomy` now writes $\max(0,\, x W_1 + b_1)$, the same ReLU); $\times$ in `frontier`'s two formulas.

The first-use script was re-run; its only mismatches are different meanings of the same letter, each a separate row, as before. Statements in the prose checked against the current chapters: the bold-vector remark (removed), the KiB/MiB/GiB paragraph (the chapters now use only decimal units and, in `local`, GiB; the appendix still defines KiB and MiB for its own Llama 3 example), the base of $\log$ in `instructions` (now stated in the chapter), and the Swish formula (now $x\,\sigma(x)$ in the chapter). The glossary's Swish entry (`glossary.md`) still writes $x \cdot \sigma(x)$, outside this pass.

## Style pass (2026-11-11)

Reader call-outs made generic per D-023.

- "It is a refresher, not a course: the reader's undergraduate linear algebra," -> "It is a refresher, not a course: undergraduate linear algebra,"
- "uses a familiar idea in an unfamiliar way." -> "uses an old idea in a new way."
- "The reader's PCA rests on the same idea:" -> "PCA rests on the same idea:"
- "the weighted sum of the reader's logistic regression" -> "the weighted sum of logistic regression"
