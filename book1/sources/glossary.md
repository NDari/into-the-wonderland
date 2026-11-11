# Ledger: glossary

Chapter: `glossary` (Book 1, appendix B, "Glossary").
Stage: verified, 2026-11-11 [D-005]. Compiled by a drafting agent from the verified chapters; independent check and post-consistency-pass update recorded at the end.

## Method

1. A script (kept outside the repository) listed every bold span in the 25 Book 1 chapters, in `OUTLINE.md` order, with chapter ID, line number, and the surrounding sentence: 640 spans. Appendices were excluded.
2. Bold spans that are list labels or emphasis ("**Text.**", "**The problem.**", "**What it cost.**", table totals, history labels such as "**Linnainmaa, 1970.**", claims such as "**A neuron with a sigmoid activation is logistic regression.**") were dropped; a term defined inside such a label was kept (for example "**The feed-forward network.**").
3. Variants were merged (singular and plural, "active parameters" and "active parameter count", "loss" and "loss function"). Abbreviations get the full form with the abbreviation in parentheses, plus a cross-entry ("RLHF: see ..."). Terms with two meanings in the book ("demonstration", "query", "prefill", "saturation", and after the update "pretraining" and "fine-tuning") get one entry with numbered senses, each linked to its own chapter.
4. Each definition paraphrases the defining sentence of the chapter, read in context; no facts were added beyond what the chapter states. The chapter given is the first chapter in book order that bolds the term (or, for the unbolded terms listed in finding (e), the chapter that defines it).
5. A few central terms that the chapters define without bold were added (finding (e)), so the glossary covers what a reader needs.
6. Model and product names that the chapters do not bold (GPT, BERT, Llama, T5, ELMo, and so on) are not entries.
7. The file is generated alphabetically (case-insensitive, ignoring spaces and punctuation) as a Pandoc definition list, which the Typst build renders as a terms list. 531 entries, of which 43 are cross-entries (535 and 44 after the update below). `python3 build/build.py glossary` gives 28 pages (US letter, default template), against a budget of about 12; trimming would mean dropping entries or shortening the chapter titles in the links.
8. `book1/chapters/local.md` was being revised during this work; it was re-read at the end (unchanged since extraction).

## Consistency findings

For the coordinator. Line numbers are in `book1/chapters/`.

### (a) Terms bolded in more than one chapter

Definitions agree unless noted.

- token: destination:17 (and the label at destination:58), tokens:5. Agree; tokens:7 adds the older "token versus type" sense. **Resolved in the consistency pass:** `tokens` no longer bolds it.
- self-supervised learning: destination:19, pretraining:23 (explicit callback). Agree. **Resolved in the consistency pass:** `pretraining` no longer bolds it.
- language model: destination:29 ("assigns a probability to a piece of text"), prediction:65 (distribution over the next word). Agree; destination:31 states the chain-rule link. **Resolved in the consistency pass:** `prediction` no longer bolds it.
- tokenizer: destination:58, tokens:7. Agree. **Resolved in the consistency pass:** `tokens` no longer bolds it.
- token ID: destination:60 (label "Token IDs."), tokens:7. Agree. **Resolved in the consistency pass:** `tokens` no longer bolds it.
- context window: destination:98, anatomy:90, generation:75. Agree; each later bold is a callback that adds detail. **Resolved in the consistency pass:** `anatomy` and `generation` no longer bold it.
- parameters: destination:102, neuron:37, scale:7. Agree (callbacks). **Resolved in the consistency pass:** `neuron` and `scale` no longer bold it.
- weights / weight: destination:102, neuron:13. Agree. **Resolved in the consistency pass:** `neuron` no longer bolds it.
- pretraining: destination:125 (the general first phase of training an LLM) and deep-turn:31 (the 2006 layer-by-layer stage). Different senses; the link is made in deep-turn:112 and pretraining:7, so readers are not misled. See also (c). **Resolved in the consistency pass:** `deep-turn` keeps its bold and says it is not the LLM sense; the glossary entry has numbered senses.
- base model: destination:125, local:169. Agree. **Resolved in the consistency pass:** `local` no longer bolds it.
- epoch: neuron:111, toolkit:21 (callback). Agree. **Resolved in the consistency pass:** `toolkit` no longer bolds it.
- gate / gates: structure:88, since-2017:35 (callback). Agree. **Resolved in the consistency pass:** `since-2017` no longer bolds it.
- fine-tuning: deep-turn:31 (after layer-wise pretraining, all weights adjusted together), pretraining:13 (adjusting a pretrained network on a new task). Compatible. **Resolved in the consistency pass:** `pretraining` keeps its bold "in a wider sense"; the glossary entry has numbered senses.
- benchmark: deep-turn:59 (hidden test set, metric, deadline, public results), evaluation:19 (fixed shared test set with a scoring rule, usually a leaderboard). Agree. **Resolved in the consistency pass:** `evaluation` no longer bolds it.
- dropout: deep-turn:102 (AlexNet: first two fully connected layers, probability 0.5), depth:30 (each hidden unit omitted with probability 0.5). Agree. **Resolved in the consistency pass:** `depth` no longer bolds it.
- beam search: seq2seq:39, generation:19 (callback). Agree. **Resolved in the consistency pass:** `generation` no longer bolds it.
- contextual embedding: attention:13, pretraining:27 (callback). Agree. **Resolved in the consistency pass:** `pretraining` no longer bolds it.
- query: attention:21 (attention vector) and tools:21 (information retrieval query). Different meanings, not flagged in tools. See (c). **Resolved in the consistency pass:** `tools` flags its sense.
- FLOPs: attention:85, scale:7. Agree; scale re-bolds without referring back to attention. **Resolved in the consistency pass:** `scale` no longer bolds it and links back.
- demonstration(s): instructions:31 (a labeler's written response for a prompt) and prompting:19 (a worked example in a prompt, also "exemplar"). Different meanings. See (c). **Resolved in the consistency pass:** `prompting` flags its sense.
- Bradley-Terry model: instructions:57, evaluation:85 (callback). Agree. **Resolved in the consistency pass:** `evaluation` no longer bolds it.
- reward hacking: instructions:125 (by reference to the 2017 robot at instructions:49), frontier:45 (formal definition quoted from DeepSeek). Agree. **Resolved in the consistency pass:** `frontier` no longer bolds it and links back.
- self-consistency and majority vote: prompting:78 (self-consistency samples many chains and takes "a majority vote"), frontier:19 ("a majority vote, also called self-consistency"). Agree in substance; frontier treats the two names as synonyms, prompting treats the vote as one step of self-consistency. **Resolved in the consistency pass:** `frontier` now says "the majority vote of self-consistency", as in `prompting`; the glossary entry describes both uses.
- reasoning model(s): prompting:90, frontier:11. Agree. **Resolved in the consistency pass:** `frontier` no longer bolds it.
- needle in a haystack: prompting:116, since-2017:121. Agree; since-2017 re-bolds without a callback. **Resolved in the consistency pass:** `since-2017` no longer bolds it and links back.
- knowledge cutoff: prompting:136 ("the date after which its training data stops"), tools:13 ("the date after which a model has seen little or no text"). Agree; tools adds the effective cutoff. **Resolved in the consistency pass:** `tools` no longer bolds it.
- retrieval: adapting:99, tools:7. Agree. **Resolved in the consistency pass:** `tools` no longer bolds it.
- saturation: tools:33 (BM25 term saturation), evaluation:63 (benchmark saturation); also "saturated" unit at deep-turn:65. Three meanings. See (c). **Resolved in the consistency pass:** `tools` and `evaluation` flag their senses.
- agent: tools:125, frontier:65 (callback). Agree. **Resolved in the consistency pass:** `frontier` no longer bolds it.
- model card(s): local:49, evaluation:121. Agree; evaluation introduces the term as if new although local comes first. **Resolved in the consistency pass:** `evaluation` no longer bolds it and points to `local`.
- contamination: evaluation:49, frontier:73 (callback). Agree. **Resolved in the consistency pass:** `frontier` no longer bolds it.
- open-weight: adapting:83, local:11 ("open-weight model"). Agree [D-020]. **Resolved in the consistency pass:** `local` no longer bolds it; `adapting` introduces it.
- active parameters: since-2017:143 ("active parameter count"), local:63. Agree. **Resolved in the consistency pass:** `local` no longer bolds it.
- reverse mode: backprop:131, toolkit:111 (callback). Agree. **Resolved in the consistency pass:** `toolkit` no longer bolds it.
- convolutional network: bolded twice in one chapter, structure:7 and structure:34. **Resolved in the consistency pass:** the second bold removed.

### (b) Terms used before their bold definition (sample check)

A script listed every earlier occurrence of each bolded term outside quotations; the hits below were read in context. Most are previews in the destination chapter or forward references with a link, which is the book's design; the ones worth a look are marked *.

- * prompt: used throughout generation (generation:5, 11, 63, 79, 83, 101) and at destination:135, bolded only at prompting:5. generation never defines it. **Resolved in the consistency pass:** glossed at first use in `destination` and `generation`.
- * multilayer perceptron: anatomy:29 and anatomy:110 call the feed-forward network "the multilayer perceptron of [the backpropagation chapter](#backprop)", but backprop.md never uses the phrase (only neuron:184 and neuron:201 say "multilayer networks/ones"). The reader is assumed to know the MLP (AGENTS.md), but the cross-reference points to a chapter that does not name it. **Resolved in the consistency pass:** `anatomy` reworded.
- * position table: attention:67 says "the position table of [the destination chapter](#destination)", but destination:62 says "a second table, of position vectors"; the term is bolded at anatomy:23. **Resolved in the consistency pass:** `attention` now uses destination's wording.
- * KV cache: anatomy:92 ("key-value caches", in a quotation) discusses it before generation:79 names it (unbolded).
- * GELU, RMSNorm, SwiGLU, pre-norm, post-norm, grouped-query attention, rotary embeddings: introduced briefly at anatomy:33 and anatomy:98-102, bolded only in since-2017 (lines 13-79). anatomy gives a short gloss for each, so this is a preview, not a gap.
- * instruction tuning: training:7 (link text "the chapter on instruction tuning") and generation:97, before instructions:23. **Resolved in the consistency pass:** link text in `training` and `generation` now names the chapter on teaching models to follow instructions.
- * checkpoint: anatomy:56 ("OpenAI's released checkpoint") before training:71. **Resolved in the consistency pass:** glossed in `anatomy`.
- * pretrained: tokens:101 ("a pretrained network of the kind described in later chapters") before pretraining:13. **Resolved in the consistency pass:** `tokens` links `pretraining`.
- * ensemble: depth:58 ("An ensemble of such networks") before seq2seq:41. **Resolved in the consistency pass:** glossed in `depth`.
- * minibatch: deep-turn:112 ("minibatch sizes", in a block quotation) before toolkit:21.
- * benchmark: structure:50 and structure:125 before deep-turn:59. **Resolved in the consistency pass:** glossed in `structure`.
- * memory bandwidth: deep-turn:47 before local:191. **Resolved in the consistency pass:** glossed in `deep-turn`.
- * GLUE: pretraining:63 and adapting:31 before evaluation:21.
- * leaderboard: tools:67 before evaluation:19. **Resolved in the consistency pass:** glossed in `tools`.
- * reasoning models: instructions:165 before prompting:90. **Resolved in the consistency pass:** glossed and linked in `instructions`.
- * prompt injection / SQL injection: instructions:109 (inside a quotation, "SQL injections") before prompting:126. **Resolved in the consistency pass:** glossed in `instructions` (independent check of that chapter).
- * closed model: adapting:103 (with a parenthetical definition) before local:11. **Resolved in the consistency pass:** `adapting` now bolds it at that definition.
- * bits per weight: adapting:77 before local:77.
- * key-value heads: generation:81 before since-2017:75. **Resolved in the consistency pass:** `generation` points back to `anatomy`.
- hidden units / hidden layers: neuron:164 ("later called hidden units") and neuron:186, before backprop:11. Deliberate forward reference.
- stochastic gradient descent: neuron:144, inside a quotation, before toolkit:21.
- fine-tuning, supervised fine-tuning, reward model, reinforcement learning, RLHF: destination:135-137, defined in passing, bolded later (deep-turn:31, instructions:31-75). Preview.
- n-gram: destination:21 and structure:22 before prediction:25; latent semantic analysis: destination:64 ("If you know latent semantic analysis") before embeddings:45. The reader is assumed to know both.
- WordPiece: seq2seq:99 (quoted "wordpieces") before tokens:53.
- decoder-only: attention:73 (with a link to anatomy) before anatomy:13.
- residual stream: depth:88 (a promise of the term) before anatomy:25 [D-019].
- MMLU: local:103 (described, with a forward link) before evaluation:25; GSM8K: prompting:68-70 (described) before evaluation:29; Goodhart's law: instructions:149 (quoted) before evaluation:117; verifier: prompting:68 (figure caption) before frontier:19.
- GPQA: evaluation:45 before evaluation:75 (same chapter).

### (c) The same term defined differently in two chapters

- pretraining: destination:125 (general first phase of an LLM's training) and deep-turn:31 (2006 unsupervised layer-by-layer stage). Linked explicitly at deep-turn:112 and pretraining:7. The glossary gives both senses in one entry. **Resolved in the consistency pass:** see (a).
- demonstration: instructions:31 (response written by a labeler) and prompting:19 (worked example inside a prompt). Neither chapter mentions the other sense. The glossary numbers the two senses. destination:135 uses the first sense ("demonstrations of good responses"). **Resolved in the consistency pass:** `prompting` names the other sense.
- query: attention:21 (attention vector) and tools:21 (IR query). Not disambiguated in tools. Numbered senses in the glossary. **Resolved in the consistency pass:** `tools` names the other sense.
- saturation / saturated: deep-turn:65 (a unit with near-zero slope), tools:33 (BM25 cap on a term's contribution), evaluation:63 (a benchmark no longer separating models). Not cross-referenced. Glossary: "saturated" and a two-sense "saturation". **Resolved in the consistency pass:** `tools` and `evaluation` name the other senses.
- calibration: generation:97 ("calibrated": confidence matches accuracy), prompting:50 (contextual calibration; prompting:50 itself flags the different meaning), local:93 (calibration data for quantization). The local sense is not flagged. **Resolved in the consistency pass:** `local` names the other sense.
- prefill: generation:11 (the phase, unbolded) and prompting:104 (writing the start of the reply; prompting:104 flags the difference). Numbered senses in the glossary. **Resolved in the consistency pass:** `generation` now bolds the phase.
- alignment: seq2seq:77-81 (soft alignment of source and target words) and instructions:11 ("Alignment, in this sense", model behavior). Flagged only by "in this sense". **Resolved in the consistency pass:** `instructions` names the other sense.
- agent: instructions:43 (the reinforcement learning agent, unbolded) and tools:125 (a model choosing actions in a loop). Related; not cross-referenced. **Resolved in the consistency pass:** `tools` names the reinforcement-learning sense.
- hidden state: structure:56 (a recurrent network's summary) and anatomy:25 ("Other writing calls the same vector the hidden state", for the residual stream). Consistent with [D-019].
- block: anatomy:11 (a transformer block), local:69 (llama.cpp's name for a quantization group), since-2017:89 (tiles in FlashAttention). local:69 flags its use.
- dense: embeddings:17 (dense vector), since-2017:125 (dense network: every parameter used for every token), tools:51-63 (dense retrieval). Related senses; since-2017:125 does not mention the vector sense. **Resolved in the consistency pass:** `since-2017` names the vector sense.
- feature: deep-turn:15 (input measurement, feature engineering) and frontier:125 (a direction in a layer's vectors, "here"). frontier flags it with "here".
- embedding table and token table: two names for one table. "Embedding table" at destination:62 (bold), backprop:118, embeddings:17, 65, 115, 122, tokens:11, 79, scale:37, 73, and anatomy:60; "token table" at anatomy:17-112 (bold at anatomy:23) and since-2017:147. [D-019] speaks of "the rows of the token table". The glossary has both entries, each pointing to the other. **Resolved in the consistency pass:** `anatomy` says the token table is destination's embedding table.

### (d) Spelling variants outside quotations

- warmup (toolkit:77, 79, 81, 103, 119, 121, 131; depth:98; pretraining:37; since-2017:13) against warm-up at anatomy:98. **Resolved in the consistency pass:** `anatomy` now says warmup.
- fine-tuned against finetuned: prompting:68 (figure caption, "a finetuned GPT-3"). Other "finetun" hits are inside quotations. **Resolved in the consistency pass:** caption now says fine-tuned.
- neighbour (British) only in tools: tools:71 (bold "nearest neighbour search", "approximate nearest neighbour"), tools:77 ("k-nearest-neighbours"), tools:158; everywhere else neighbor (for example embeddings:83, structure, pretraining). The glossary follows tools for those two entries. **Resolved in the consistency pass:** `tools` now says neighbor; the glossary follows.
- labelled (neuron:5, 105, 148 twice; structure:40, 42; attention:37; tools:129) against labeled (deep-turn:112, 129; instructions:119; pretraining:5-92, twelve times; scale:5; seq2seq:55). **Resolved in the consistency pass:** labeled throughout, outside quotations.
- analysed (neuron:55, 142, 170; structure:82, 136) against analyzed (attention:31). **Resolved in the consistency pass:** analyzed throughout.
- colours (neuron:180) against color elsewhere (deep-turn, prediction, tools). **Resolved in the consistency pass:** colors.
- data centres (frontier:145 four times, frontier:214) against data center(s) (adapting:83, local:5, scale:97, training:69). **Resolved in the consistency pass:** data centers, outside the IEA quotation.
- data set (sixteen times: deep-turn:9, 11, 122; generation:89; instructions:23, 25, 53; prediction:143; pretraining:15, 37, 43; prompting:29; tools:55, 63, 105; training:23) against dataset (deep-turn:102, depth:84, evaluation:57; deep-turn:120 is a block quotation). **Resolved in the consistency pass:** data set in prose; dataset remains inside quotations.
- pre-trained at since-2017:71 (twice) against pretrained everywhere else. **Resolved in the consistency pass:** pretrained.
- mini-batch (depth:94) and hyper-parameters (toolkit:119) occur only in block quotations of training recipes; not variants.

### (e) Terms defined without bold

Defined in prose but never bolded; added to the glossary with the defining chapter. The chapters may want to bold them at first use. **Resolved in the consistency pass:** every term below is now bolded at its first definition, in the chapter listed (prefill and decode, KV cache, and masked language model outside the quotations; scaling laws in the text after the heading).

- large language model (LLM): destination:7.
- vocabulary: destination:17 (unbolded there; bolded at tokens:7).
- byte pair encoding (BPE): tokens:27-37 (section heading, not bold).
- RMSProp: toolkit:63.
- multi-head attention: attention:55.
- causal mask: attention:73 (in passing) and anatomy:72.
- masked language model (MLM): pretraining:53 (quoted "masked LM").
- scaling law: scale:29 (heading) and scale:31; compute-optimal: scale:65; emergent ability: scale:91 (quoted definition).
- prefill and decode phases: generation:11 (quoted from Pope and colleagues).
- KV cache: generation:79 (quoted).
- Kullback-Leibler divergence: instructions:85.
- Group Relative Policy Optimization (GRPO): frontier:31 (inside a label).
- feed-forward network: anatomy:29 (inside the label "**The feed-forward network.**").
- CBOW (continuous bag of words): embeddings:79 (kept inside the skip-gram entry).

## Independent check (glossary appendix)

2026-11-11. A separate agent re-extracted the bold terms of the 25 chapters, compared each entry's link with the first chapter in book order that bolds the term, checked every link text against the chapter headings, sampled about 120 entries against the defining sentences in the chapters, and rendered sample pages of the PDF. No definition contradicted its chapter.

- Errors found and fixed (three):
  1. Two link texts were shortened chapter titles: "Teaching models to follow instructions" (in *demonstration*) and "Attention without recurrence" (in *query*). Now the full titles, "Teaching models to follow instructions (2017-2023)" and "Attention without recurrence (2017)"; all link texts are now filled in from the chapter headings.
  2. *vocabulary* linked `destination`, but the first bold was in `tokens`. Superseded by the consistency pass, which bolds vocabulary at its definition in `destination` and un-bolds it in `tokens`; the link stays.
- Missing entries added: *representation learning* (`deep-turn`) and *framework* (`toolkit`), both bolded in their chapters with no entry.
- Warnings acted on: numbered senses began with "(1)", which Pandoc reads as an ordered list; they are now written "\(1)" and render as text (checked on PDF page 19). *majority vote* had "also called self-consistency", which only `frontier` said; it now follows `prompting` (the vote is the last step of self-consistency) and says how `frontier` uses it. *pretraining* and *fine-tuning* now have numbered senses with their own links (2006 sense in `deep-turn`; LLM sense in `destination` and wider sense in `pretraining`). *open-weight* links `adapting`, which defines it, and names `local` for the book's policy on "open source" [D-020]. British spellings in definitions (neighbour, labelled, analysed) changed to American.

### Update after the consistency pass

The links were re-derived from the chapters as they now stand: every bold span of the 25 chapters was listed again in book order, and each entry was linked to the first chapter that bolds the term (or, for the few terms bolded only in a variant form, such as "reverse mode of automatic differentiation" or "approximate nearest neighbor", or not bolded, such as pass@1, the chapter that defines it). The only change of first chapter was *closed model*, now `adapting` instead of `local`; the fifteen terms of finding (e) were already linked to the chapters that now bold them, and their definitions were rechecked against the new bold sentences (*scaling law* and *masked language model* reworded to match). *continuous bag of words (CBOW)* got its own entry, as `embeddings` now bolds it. In all, 19 entries changed (link, link text, numbered senses, wording, or spelling, including the two nearest-neighbor entries renamed to American spelling) and 4 were added (*continuous bag of words (CBOW)*, its cross-entry *CBOW*, *representation learning*, *framework*): 535 entries, 44 of them cross-entries. `python3 build/build.py glossary` still gives 28 pages.

## Style pass (2026-11-11)

Reader call-outs made generic per D-023.

No changes needed.
