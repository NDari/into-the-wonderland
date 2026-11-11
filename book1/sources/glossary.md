# Ledger: glossary

Chapter: `glossary` (Book 1, appendix B, "Glossary").
Stage: drafted, 2026-11-11 [D-005]. Compiled by a drafting agent from the verified chapters; independent check pending.

## Method

1. A script (kept outside the repository) listed every bold span in the 25 Book 1 chapters, in `OUTLINE.md` order, with chapter ID, line number, and the surrounding sentence: 640 spans. Appendices were excluded.
2. Bold spans that are list labels or emphasis ("**Text.**", "**The problem.**", "**What it cost.**", table totals, history labels such as "**Linnainmaa, 1970.**", claims such as "**A neuron with a sigmoid activation is logistic regression.**") were dropped; a term defined inside such a label was kept (for example "**The feed-forward network.**").
3. Variants were merged (singular and plural, "active parameters" and "active parameter count", "loss" and "loss function"). Abbreviations get the full form with the abbreviation in parentheses, plus a cross-entry ("RLHF: see ..."). Terms with two meanings in the book ("demonstration", "query", "prefill", "saturation") get one entry with numbered senses, each linked to its own chapter.
4. Each definition paraphrases the defining sentence of the chapter, read in context; no facts were added beyond what the chapter states. The chapter given is the first chapter in book order that bolds the term (or, for the unbolded terms listed in finding (e), the chapter that defines it).
5. A few central terms that the chapters define without bold were added (finding (e)), so the glossary covers what a reader needs.
6. Model and product names that the chapters do not bold (GPT, BERT, Llama, T5, ELMo, and so on) are not entries.
7. The file is generated alphabetically (case-insensitive, ignoring spaces and punctuation) as a Pandoc definition list, which the Typst build renders as a terms list. 531 entries, of which 43 are cross-entries. `python3 build/build.py glossary` gives 28 pages (US letter, default template), against a budget of about 12; trimming would mean dropping entries or shortening the chapter titles in the links.
8. `book1/chapters/local.md` was being revised during this work; it was re-read at the end (unchanged since extraction).

## Consistency findings

For the coordinator. Line numbers are in `book1/chapters/`.

### (a) Terms bolded in more than one chapter

Definitions agree unless noted.

- token: destination:17 (and the label at destination:58), tokens:5. Agree; tokens:7 adds the older "token versus type" sense.
- self-supervised learning: destination:19, pretraining:23 (explicit callback). Agree.
- language model: destination:29 ("assigns a probability to a piece of text"), prediction:65 (distribution over the next word). Agree; destination:31 states the chain-rule link.
- tokenizer: destination:58, tokens:7. Agree.
- token ID: destination:60 (label "Token IDs."), tokens:7. Agree.
- context window: destination:98, anatomy:90, generation:75. Agree; each later bold is a callback that adds detail.
- parameters: destination:102, neuron:37, scale:7. Agree (callbacks).
- weights / weight: destination:102, neuron:13. Agree.
- pretraining: destination:125 (the general first phase of training an LLM) and deep-turn:31 (the 2006 layer-by-layer stage). Different senses; the link is made in deep-turn:112 and pretraining:7, so readers are not misled. See also (c).
- base model: destination:125, local:169. Agree.
- epoch: neuron:111, toolkit:21 (callback). Agree.
- gate / gates: structure:88, since-2017:35 (callback). Agree.
- fine-tuning: deep-turn:31 (after layer-wise pretraining, all weights adjusted together), pretraining:13 (adjusting a pretrained network on a new task). Compatible.
- benchmark: deep-turn:59 (hidden test set, metric, deadline, public results), evaluation:19 (fixed shared test set with a scoring rule, usually a leaderboard). Agree.
- dropout: deep-turn:102 (AlexNet: first two fully connected layers, probability 0.5), depth:30 (each hidden unit omitted with probability 0.5). Agree.
- beam search: seq2seq:39, generation:19 (callback). Agree.
- contextual embedding: attention:13, pretraining:27 (callback). Agree.
- query: attention:21 (attention vector) and tools:21 (information retrieval query). Different meanings, not flagged in tools. See (c).
- FLOPs: attention:85, scale:7. Agree; scale re-bolds without referring back to attention.
- demonstration(s): instructions:31 (a labeler's written response for a prompt) and prompting:19 (a worked example in a prompt, also "exemplar"). Different meanings. See (c).
- Bradley-Terry model: instructions:57, evaluation:85 (callback). Agree.
- reward hacking: instructions:125 (by reference to the 2017 robot at instructions:49), frontier:45 (formal definition quoted from DeepSeek). Agree.
- self-consistency and majority vote: prompting:78 (self-consistency samples many chains and takes "a majority vote"), frontier:19 ("a majority vote, also called self-consistency"). Agree in substance; frontier treats the two names as synonyms, prompting treats the vote as one step of self-consistency.
- reasoning model(s): prompting:90, frontier:11. Agree.
- needle in a haystack: prompting:116, since-2017:121. Agree; since-2017 re-bolds without a callback.
- knowledge cutoff: prompting:136 ("the date after which its training data stops"), tools:13 ("the date after which a model has seen little or no text"). Agree; tools adds the effective cutoff.
- retrieval: adapting:99, tools:7. Agree.
- saturation: tools:33 (BM25 term saturation), evaluation:63 (benchmark saturation); also "saturated" unit at deep-turn:65. Three meanings. See (c).
- agent: tools:125, frontier:65 (callback). Agree.
- model card(s): local:49, evaluation:121. Agree; evaluation introduces the term as if new although local comes first.
- contamination: evaluation:49, frontier:73 (callback). Agree.
- open-weight: adapting:83, local:11 ("open-weight model"). Agree [D-020].
- active parameters: since-2017:143 ("active parameter count"), local:63. Agree.
- reverse mode: backprop:131, toolkit:111 (callback). Agree.
- convolutional network: bolded twice in one chapter, structure:7 and structure:34.

### (b) Terms used before their bold definition (sample check)

A script listed every earlier occurrence of each bolded term outside quotations; the hits below were read in context. Most are previews in the destination chapter or forward references with a link, which is the book's design; the ones worth a look are marked *.

- * prompt: used throughout generation (generation:5, 11, 63, 79, 83, 101) and at destination:135, bolded only at prompting:5. generation never defines it.
- * multilayer perceptron: anatomy:29 and anatomy:110 call the feed-forward network "the multilayer perceptron of [the backpropagation chapter](#backprop)", but backprop.md never uses the phrase (only neuron:184 and neuron:201 say "multilayer networks/ones"). The reader is assumed to know the MLP (AGENTS.md), but the cross-reference points to a chapter that does not name it.
- * position table: attention:67 says "the position table of [the destination chapter](#destination)", but destination:62 says "a second table, of position vectors"; the term is bolded at anatomy:23.
- * KV cache: anatomy:92 ("key-value caches", in a quotation) discusses it before generation:79 names it (unbolded).
- * GELU, RMSNorm, SwiGLU, pre-norm, post-norm, grouped-query attention, rotary embeddings: introduced briefly at anatomy:33 and anatomy:98-102, bolded only in since-2017 (lines 13-79). anatomy gives a short gloss for each, so this is a preview, not a gap.
- * instruction tuning: training:7 (link text "the chapter on instruction tuning") and generation:97, before instructions:23.
- * checkpoint: anatomy:56 ("OpenAI's released checkpoint") before training:71.
- * pretrained: tokens:101 ("a pretrained network of the kind described in later chapters") before pretraining:13.
- * ensemble: depth:58 ("An ensemble of such networks") before seq2seq:41.
- * minibatch: deep-turn:112 ("minibatch sizes", in a block quotation) before toolkit:21.
- * benchmark: structure:50 and structure:125 before deep-turn:59.
- * memory bandwidth: deep-turn:47 before local:191.
- * GLUE: pretraining:63 and adapting:31 before evaluation:21.
- * leaderboard: tools:67 before evaluation:19.
- * reasoning models: instructions:165 before prompting:90.
- * prompt injection / SQL injection: instructions:109 (inside a quotation, "SQL injections") before prompting:126.
- * closed model: adapting:103 (with a parenthetical definition) before local:11.
- * bits per weight: adapting:77 before local:77.
- * key-value heads: generation:81 before since-2017:75.
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

- pretraining: destination:125 (general first phase of an LLM's training) and deep-turn:31 (2006 unsupervised layer-by-layer stage). Linked explicitly at deep-turn:112 and pretraining:7. The glossary gives both senses in one entry.
- demonstration: instructions:31 (response written by a labeler) and prompting:19 (worked example inside a prompt). Neither chapter mentions the other sense. The glossary numbers the two senses. destination:135 uses the first sense ("demonstrations of good responses").
- query: attention:21 (attention vector) and tools:21 (IR query). Not disambiguated in tools. Numbered senses in the glossary.
- saturation / saturated: deep-turn:65 (a unit with near-zero slope), tools:33 (BM25 cap on a term's contribution), evaluation:63 (a benchmark no longer separating models). Not cross-referenced. Glossary: "saturated" and a two-sense "saturation".
- calibration: generation:97 ("calibrated": confidence matches accuracy), prompting:50 (contextual calibration; prompting:50 itself flags the different meaning), local:93 (calibration data for quantization). The local sense is not flagged.
- prefill: generation:11 (the phase, unbolded) and prompting:104 (writing the start of the reply; prompting:104 flags the difference). Numbered senses in the glossary.
- alignment: seq2seq:77-81 (soft alignment of source and target words) and instructions:11 ("Alignment, in this sense", model behavior). Flagged only by "in this sense".
- agent: instructions:43 (the reinforcement learning agent, unbolded) and tools:125 (a model choosing actions in a loop). Related; not cross-referenced.
- hidden state: structure:56 (a recurrent network's summary) and anatomy:25 ("Other writing calls the same vector the hidden state", for the residual stream). Consistent with [D-019].
- block: anatomy:11 (a transformer block), local:69 (llama.cpp's name for a quantization group), since-2017:89 (tiles in FlashAttention). local:69 flags its use.
- dense: embeddings:17 (dense vector), since-2017:125 (dense network: every parameter used for every token), tools:51-63 (dense retrieval). Related senses; since-2017:125 does not mention the vector sense.
- feature: deep-turn:15 (input measurement, feature engineering) and frontier:125 (a direction in a layer's vectors, "here"). frontier flags it with "here".
- embedding table and token table: two names for one table. "Embedding table" at destination:62 (bold), backprop:118, embeddings:17, 65, 115, 122, tokens:11, 79, scale:37, 73, and anatomy:60; "token table" at anatomy:17-112 (bold at anatomy:23) and since-2017:147. [D-019] speaks of "the rows of the token table". The glossary has both entries, each pointing to the other.

### (d) Spelling variants outside quotations

- warmup (toolkit:77, 79, 81, 103, 119, 121, 131; depth:98; pretraining:37; since-2017:13) against warm-up at anatomy:98.
- fine-tuned against finetuned: prompting:68 (figure caption, "a finetuned GPT-3"). Other "finetun" hits are inside quotations.
- neighbour (British) only in tools: tools:71 (bold "nearest neighbour search", "approximate nearest neighbour"), tools:77 ("k-nearest-neighbours"), tools:158; everywhere else neighbor (for example embeddings:83, structure, pretraining). The glossary follows tools for those two entries.
- labelled (neuron:5, 105, 148 twice; structure:40, 42; attention:37; tools:129) against labeled (deep-turn:112, 129; instructions:119; pretraining:5-92, twelve times; scale:5; seq2seq:55).
- analysed (neuron:55, 142, 170; structure:82, 136) against analyzed (attention:31).
- colours (neuron:180) against color elsewhere (deep-turn, prediction, tools).
- data centres (frontier:145 four times, frontier:214) against data center(s) (adapting:83, local:5, scale:97, training:69).
- data set (sixteen times: deep-turn:9, 11, 122; generation:89; instructions:23, 25, 53; prediction:143; pretraining:15, 37, 43; prompting:29; tools:55, 63, 105; training:23) against dataset (deep-turn:102, depth:84, evaluation:57; deep-turn:120 is a block quotation).
- pre-trained at since-2017:71 (twice) against pretrained everywhere else.
- mini-batch (depth:94) and hyper-parameters (toolkit:119) occur only in block quotations of training recipes; not variants.

### (e) Terms defined without bold

Defined in prose but never bolded; added to the glossary with the defining chapter. The chapters may want to bold them at first use.

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
