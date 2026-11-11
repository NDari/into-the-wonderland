# Ledger: notation

Chapter: `notation` (Book 1, appendix A, "Notation and math refresher").
Stage: drafted, 2026-11-11 [D-005]. Compiled by a drafting agent from the verified chapters; independent check pending.

## Method

The appendix states standard textbook mathematics only (vectors, matrices, logarithms, probability, entropy, softmax, the logistic function) and makes no historical or quantitative claims about named papers or systems, so it cites no sources. Where it mentions a figure from a chapter (the KV-cache size, the scaling exponent 0.076, the doubling time of 207 days, the Elo scale of 400 points), the figure is the chapter's own, already verified and cited there; the appendix only recomputes it.

1. Inventory. A throwaway script (not in the repository) listed every inline and display math span in the 25 Book 1 chapter files, with line numbers, plus plain-text formulas and unit words (powers of ten written as text, "softmax", "log", "nats", "bits per", KiB, MiB, GiB). It found math in 22 of the 25 chapters (none in `pretraining`, `seq2seq`, `tokens`) 354 spans in all. A second pass collected unit usage (GB, GiB, MB, MiB, KB, KiB, TB) and the multiplication signs used in prose.
2. Conventions. From the inventory, the notation actually used was listed (below, "Notation inconsistencies found", covers the conflicts). The appendix covers only what appears in the chapters; transposes, determinants, eigenvectors, integrals, and continuous distributions do not appear and are left out.
3. First use. The "First used" column of the symbol tables was checked with a second throwaway script that finds, for each symbol, the first chapter in OUTLINE.md order whose math spans contain it. Every mismatch it reported was a different meaning of the same letter, already a separate row. One row is a judgment call: $\Delta$ is first used inside a quotation in `instructions` (line 67, "Δ(Elo Score)"), before its first use in math in `adapting`; the table gives `instructions`.
4. Numbers. Every number in the appendix's prose and the first table is printed by `code/checks/notation.py` [D-009]. A scratch comparison of the numbers in the appendix text against the script's output found none missing except the scores 3.0, -1.0, and -2.0 (printed by the script as 3, -1, -2) and the year in a chapter's title.
5. Build. `python3 build/build.py notation` gives 12 pages: about 8 of text and 4 of symbol tables. A single symbol table did not fit on one page (Pandoc's Typst output puts each table in a figure, which does not break across pages), so it was split into four tables, each checked by eye in the rendered PDF.

## Worked examples used

All from `code/checks/notation.py`. Examples that repeat a chapter's example reuse that chapter's script, so the numbers cannot drift apart.

| Example | Appendix section | What it computes | Reused from |
|---|---|---|---|
| 1 | Numbers and units | powers of 2; $10^{-8}$; $\pi$; GPT-3's $6ND$; memory for 8 billion parameters at 32, 16, 8, 4 bits in GB and GiB; Llama 3 8B KV cache per token (131,072 bytes = 128 KiB) and per 131,072-token window (17.2 GB = 16 GiB); the score tables of `since-2017` in MiB and MB (for the inconsistency below) | arithmetic restated from `generation.py` Example 5 and `scale.py` Example 2 |
| 2 | Vectors and dot products | dot product, lengths, and cosine of "cat" and "dog" (0.990), "cat" and "car" (0.303); doubling invariance; one-hot distance 1.414; the neuron's vote as $w \cdot x + b$ = 0.1 | vectors read from `embeddings.py` (TOY, Example 2) without executing it, since it needs numpy; vote weights imported from `neuron.py` |
| 3 | Matrices | a 2 by 3 matrix times a vector, in both orders; GPT-2 small feed-forward parameter count 4,722,432 (matches `anatomy.py` Example 1); a rank-1 product; LoRA rank 8 on 4,096 by 4,096 (65,536 numbers, 0.39%, matches `adapting.py` Example 1) | new |
| 4 | Logarithms | ln 2, bits per nat, the destination chapter's text probability $8.222 \times 10^{-6}$ as a sum of logs (16.89 bits, 11.71 nats; 2.815 bits = 1.951 nats per token); $2^{-0.076}$ and $10^{-0.076}$; $2^{365/207}$ | chain from `destination.py` (CHAIN, softmax) |
| 5 | Probability | fair and loaded die entropy (2.585, 2.161 bits), perplexity (6.00, 4.47), cross-entropy under a fair-die model (2.585) and KL (0.424); destination text perplexity 7.04 from bits and from nats; SE at p = 0.8, n = 164 (6.12 points, matches `evaluation.py` Example 1) | `prediction.py` (entropy, cross_entropy, log2) and `destination.py` |
| 6 | Softmax and temperature | the destination chapter's softmax table; shift invariance; temperature 0.5, 1, 2 (0.831, 0.571, 0.375; 0.86, 1.70, 2.23 bits); two-score softmax equals the logistic of the difference (0.599, the router example of `since-2017.py`); a masked score | `destination.py` (softmax), `generation.py` (softmax_t, entropy_bits), `neuron.py` (sigmoid) |
| 7 | Logistic function | $\sigma$ at -2, -1, 0, 0.1, 1, 2; symmetry; log-odds of 0.731 = 1.000; Elo 400-point gap (0.909) and 173.7 Elo points per natural log-odds unit (matches `instructions.py` Example 2); log loss 0.313 and 0.693 (matches `instructions.py` Example 1) | `neuron.py` (sigmoid) |

## Notation inconsistencies found

For the coordinator. Line numbers are as of 2026-11-11. Each item gives the file and line, the two usages, and a suggested fix. None of these was changed: this pass edited only the appendix, its script, and this ledger. Items are in rough order of importance.

1. **$\sigma$ used undefined for a standard deviation.** `book1/chapters/toolkit.md:23` writes the standard error of a mean as $\sigma/\sqrt{n}$ and `toolkit.md:29` repeats it in a table header, but never says what $\sigma$ is. Everywhere else $\sigma$ is the logistic function, introduced at `neuron.md:43` and used at `instructions.md:59-61`, `since-2017.md:35`, and `frontier.md:83-85`. This also breaks D-002's "every symbol explained". Suggested fix at `toolkit.md:23`: "the standard error of a mean estimated from $n$ samples is $\sigma/\sqrt{n}$, where $\sigma$ is the standard deviation of a single sample (here, of one example's gradient; not the logistic function of [the neuron chapter](#neuron))".

2. **Two symbols for one quantity in one chapter.** `book1/chapters/frontier.md:83-85` calls a model's time horizon $h$; `frontier.md:91-93` calls the same horizon $H$ (and $H_0$ at the start). $H$ is also entropy and cross-entropy at `prediction.md:37` and `prediction.md:129`. Suggested fix: at `frontier.md:91` write $h = h_0 \times 2^{d/T}$, and at `frontier.md:93` "where $h_0$ is the horizon at the start ... and $h$ the horizon after $d$ days".

3. **The dot $\cdot$ means three different operations.** It is the dot product of two vectors at `embeddings.md:23-25` and `attention.md:25-27`. It is ordinary multiplication of two numbers at `frontier.md:83`, $(\log h - \log t) \cdot \beta$. It is a number times its own sigmoid, entry by entry, at `since-2017.md:35`, $x \cdot \sigma(x)$. And it is a vector times a matrix at `since-2017.md:129`, $\text{TopK}(x \cdot W_g)$, where the same chapter (`since-2017.md:37`, $x W$) and `anatomy.md:31` ($x W_1$) write that product with no sign. A reader who has just learned that $\cdot$ is a dot product will misread the last one. Suggested fixes: `since-2017.md:129` write $\text{TopK}(x W_g)$; `frontier.md:83` write $\beta\,(\log h - \log t)$; `since-2017.md:35` write $x\,\sigma(x)$.

4. **Binary units used before (or without) definition, and mixed with decimal ones.** `book1/chapters/since-2017.md:81` gives "128 KiB per token" and "16 KiB", then window sizes in decimal GB (68.7, 17.2, 2.1 GB) in the same paragraph; `since-2017.md:87` gives "2 MiB", "128 MiB", "32 GiB", and "32 MiB". KiB and MiB are defined in no chapter; GiB is first defined at `local.md:124`, the next chapter. The generation chapter, which `since-2017.md:81` cites, gives the same per-token figure as "131,072 bytes" (`generation.md:81`), and the book's convention is decimal GB (`destination.md:117`, `local.md:59`). Suggested fix, either (a) keep the binary units and define them at first use, `since-2017.md:81`: "128 KiB (131,072 bytes; a KiB is 1,024 bytes, a MiB 1,024 KiB, a GiB 1,024 MiB) per token", or (b) switch to decimal units, as `notation.py` Example 1 prints them: at `since-2017.md:81` "131,072 bytes per token", "16,384 bytes"; at `since-2017.md:87` "2.1 MB at 1,024 tokens, 134.2 MB at 8,192, and 34.4 GB at 131,072, while the output ... is only 33.6 MB". Option (b) matches the rest of the book; if chosen, `code/checks/since-2017.py` Example 7 should print the decimal figures.

5. **Logarithm base not stated.** `book1/chapters/instructions.md:61` ($-\log \sigma(r_w - r_l)$) and `instructions.md:83` ($\beta \log$ of a ratio) do not say which logarithm; the chapter's numbers (0.693 at `instructions.md:133`, "nats" at `instructions.md:85`) show it is the natural one. Elsewhere the base is explicit: $\log_2$ at `prediction.md:37`, $\log_{10}$ at `tools.md:27`, "natural logarithms" in words at `scale.md:31` and `training.md:41`. Suggested fix: at `instructions.md:61` add "(natural logarithms throughout this chapter, so log-ratios are in nats)". Separately, `frontier.md:83` ($\log h - \log t$) gives no base. The base does not change the model's predictions but does change the value of the fitted slope $\beta$; if the chapter ever quotes a value of $\beta$, the base should be checked against `kwa2025measuring` and stated. Not checked here.

6. **Bold vector in one formula only.** `book1/chapters/since-2017.md:21` and `:23` write the vector as bold $\mathbf{a}$. Every other chapter writes vectors in plain italics ($a$, $b$ at `embeddings.md:23`; $q$, $k_j$ at `attention.md:25`; $x$ at `anatomy.md:31`), and so does the same chapter elsewhere ($x$ at `since-2017.md:37` and `:129`). Suggested fix: write $\text{RMS}(a)$ unbolded at `since-2017.md:21` and `:23`. If changed, update the appendix's symbol table row "$\text{RMS}(\mathbf{a})$" and the remark in its "Vectors and dot products" section.

7. **$n$ used for two things in one chapter.** In `book1/chapters/since-2017.md:21-23`, $n$ is the length of the vector being normalized; in `since-2017.md:129-131`, $n$ is the number of experts. Suggested fix: write the RMS formula with $d$ for the vector's length (matching $d$ for widths elsewhere), $\sqrt{\frac{1}{d} \sum_{j=1}^{d} a_j^2}$, with "$d$ its length" at `:23`.

8. **$d$ for a head's size versus the model's width.** `book1/chapters/attention.md:77` uses $d$ for the whole vector of a token (512 in the 2017 transformer) and $d_k$ (`attention.md:27`) for the numbers in one key, that is, in one head. `book1/chapters/since-2017.md:57` uses plain $d$ for the numbers in one head ("a head of $d$ numbers"). Suggested fix: `since-2017.md:57` write $\theta_i = 10000^{-2(i-1)/d_k}$ and "the $d_k/2$ pairs in a head of $d_k$ numbers". Low priority: the RoPE paper writes $d$, and the sentence defines it.

9. **Capitalized Softmax.** `book1/chapters/since-2017.md:129` writes $\text{Softmax}$ (and $\text{TopK}$); `attention.md:25` writes $\text{softmax}_j$ and all prose uses "softmax". Suggested fix: lowercase $\text{softmax}$ at `since-2017.md:129`.

10. **Two orders for matrix times vector.** `book1/chapters/anatomy.md:31` and `since-2017.md:37`, `:129` put the vector on the left ($x W_1$, $x W$, following the transformer paper); `adapting.md:49` puts it on the right ($h = W_0 x + BAx$, following the LoRA paper, with $W_0$ described as $d$ rows by $k$ columns at `adapting.md:45`). Both are correct for their sources, and the appendix's "Matrices" section explains both. Optional fix: a clause at `adapting.md:49`, "(LoRA writes the input on the right of the matrix; [the anatomy chapter](#anatomy) wrote it on the left; see [the appendix on notation](#notation))".

11. **Same letter, another chapter's meaning, defined in place.** Each is explained where it is used, so no change is required; the appendix's symbol tables list every meaning. Listed in case the coordinator wants fewer collisions.
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

12. **Notes, no change suggested.**
    - `since-2017.md:37-39` writes the entry-by-entry product as $\otimes$, following Shazeer's paper. Many texts write $\odot$ and keep $\otimes$ for the outer (Kronecker) product. The chapter defines it in place; the appendix says the symbol follows its source.
    - `instructions.md:83-85` writes a model's probability as $\pi(y \mid x)$ (from InstructGPT), where `prediction.md:129` writes $P(\ldots)$. The appendix explains $\pi$ as a policy, not 3.14159.
    - Prose writes multiplication as a letter "x" (`adapting.md:51`, `scale.md:45`, `instructions.md:133`) and shapes as "by" (`adapting.md:45-51`) or "x" (`anatomy.md:47-48`); the sign "×" appears only inside quotations (`depth.md:84`, `depth.md:94`, `toolkit.md:123`, `since-2017.md:93`, `since-2017.md:159`, `adapting.md:69`). The appendix states the convention. Consistent enough.
    - `depth.md:38` already flags that dropout's $p$ means "keep" in one convention and "drop" in another.
