# Claim ledger: destination

Chapter: `destination` (Book 1, "The destination: an LLM in one picture").
Stage: approved by the author, 2026-11-11 (verified the same day) [D-005]. Locations added while drafting are logged as "Also used" under the claim they belong to, and C10 to C12 were added after the independent check. See "Independent check" at the end.

The chapter is mostly mechanism, which needs no citation per sentence. The claims below are the ones the draft is planned to make that need a source: a few named models used as concrete anchors, and the numbers attached to them. All sources were fetched on 2026-11-11 and each claim was located in the fetched text. Page numbers are PDF page numbers of the version named in the URL.

## Sourced claims

### C1. The core objective: probability of a text as a chain of next-symbol predictions
- Use in chapter: the opening idea, "an LLM is trained to predict the next token".
- Source: `radford2019language`, https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- Location: section 2, equation (1), p. 2.
- Quote: "it is common to factorize the joint probabilities over symbols as the product of conditional probabilities (Jelinek & Mercer, 1980) (Bengio et al., 2003)", followed by p(x) as the product over n of p(s_n | s_1, ..., s_{n-1}).
- Note: the paper itself credits the idea to 1980 and 2003 work. The chapter should not imply it was new with GPT. The history belongs to `prediction`.

### C2. The whole pipeline in one published equation (tokens, embedding, stacked transformer blocks, softmax over the vocabulary)
- Use in chapter: support for the end-to-end diagram and for the bridge "a classifier over the vocabulary".
- Source: `radford2018improving`, https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- Location: section 3.1, equation (2), p. 3.
- Quote: "we use a multi-layer Transformer decoder [34] for the language model, which is a variant of the transformer [62]. This model applies a multi-headed self-attention operation over the input context tokens followed by position-wise feedforward layers to produce an output distribution over target tokens", then h_0 = U W_e + W_p; h_l = transformer_block(h_{l-1}); P(u) = softmax(h_n W_e^T), "where U = (u_{-k}, ..., u_{-1}) is the context vector of tokens, n is the number of layers, W_e is the token embedding matrix, and W_p is the position embedding matrix."
- Note: Book 1 has no formulas beyond standard forms [D-002]. The equation is the source for the diagram's boxes, not something to print.
- Also used: "multi-layer Transformer decoder" (p. 3) as the source for "OpenAI's GPT models use transformer blocks". The GPT-2 paper calls this 2018 model "the OpenAI GPT model (Radford et al., 2018)" (section 2.3, p. 4), which is the source for naming it "OpenAI's 2018 GPT model". Year confirmed by the PDF's creation date, 2018-06-08.
- Also used: "768 dimensional states" (section 4.1, p. 5), the source for "turned each token into 768 numbers". The W_p term in equation (2), "the position embedding matrix" (p. 3), is the source for "a second table, of position vectors".

### C3. The transformer was introduced in 2017, built on attention, replacing recurrence
- Use in chapter: one sentence naming what the "layers" box is and pointing to `attention`.
- Source: `vaswani2017attention`, https://arxiv.org/abs/1706.03762 (v1 submitted 2017-06-12; text checked in v7)
- Location: section 7 (Conclusion), p. 10.
- Quote: "we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention."

### C4. GPT-2: vocabulary of 50,257 tokens; context of 1,024 tokens; largest model 1.5B parameters
- Use in chapter: a concrete vocabulary size for "the classifier has one output per token".
- Source: `radford2019language` (URL above)
- Location: section 2.3, p. 4 (vocabulary and context); abstract, p. 1 (1.5B); Table 2, p. 4 (four sizes 117M, 345M, 762M, 1542M).
- Quotes: "The vocabulary is expanded to 50,257. We also increase the context size from 512 to 1024 tokens"; "Our largest model, GPT-2, is a 1.5B parameter Transformer".
- Also used: Table 2 columns are Parameters, Layers, d_model; the 1542M row has 48 layers and d_model 1600 (source for "48 blocks" and "1,600 numbers per token"). Year confirmed by the PDF's creation date, 2019-02-14.

### C5. GPT-3: 175 billion parameters, 2,048-token context window, trained on 300 billion tokens
- Use in chapter: a concrete sense of "parameters" and of training data scale.
- Source: `brown2020language`, https://arxiv.org/abs/2005.14165 (text checked in v4)
- Location: abstract, p. 1 (175B); section 2.1 and Table 2.1, p. 8 (context, tokens).
- Quotes: "we train GPT-3, an autoregressive language model with 175 billion parameters" (also the source for the chapter's quoted phrase "an autoregressive language model"); "All models were trained for a total of 300 billion tokens."; "All models use a context window of nctx = 2048 tokens."

### C6. Llama 3: open-weight models of 8B, 70B, and 405B parameters; 128K-token vocabulary; 405B pretrained on 15.6T tokens; context up to 128K tokens
- Use in chapter: a second, more recent anchor (2024) whose weights are public, to contrast with C5 and to preview `local`. Dated in text as "as of 2024".
- Source: `grattafiori2024llama`, https://arxiv.org/abs/2407.21783 (text checked in v3)
- Location: section 1, pp. 2-3 (sizes, tokens, context); section 3.2, p. 7 (vocabulary).
- Quotes: "a herd of three multilingual language models with 8B, 70B, and 405B parameters"; "we pre-train a model with 405B parameters on 15.6T tokens using a context window of 8K tokens. This standard pre-training stage is followed by a continued pre-training stage that increases the supported context window to 128K tokens."; "We use a vocabulary with 128K tokens." Table 3 (p. 7) gives the vocabulary size as 128,000, the figure the chapter prints.
- Also used: "Our largest model is a dense Transformer with 405B parameters" (abstract, p. 1), as the source for Llama 3.1 using transformer blocks.
- Also used: Table 1 (p. 2) gives the release of the Llama 3.1 models as "July 2024", the source for "published in 2024".
- Also used: Table 3 (p. 7) gives "Model Dimension" 4,096, 8,192, and 16,384 for 8B, 70B, and 405B, the source for "the largest Llama 3.1 uses 16,384".
- Also used: Table 4 (p. 10) gives the long-context stage of 405B pretraining a sequence length of 131,072, the source for "128K, where K means 1,024, so 131,072 tokens". The paper itself writes "128K".
- Note: the paper says its results are for Llama 3.1 models, "which we will refer to as Llama 3 throughout". The chapter should say "Llama 3.1" or follow the paper's convention explicitly.

### C7. A pretrained model is not yet an assistant
- Use in chapter: the "model vs chat product" section.
- Source: `grattafiori2024llama` (URL above)
- Location: section 1, p. 3.
- Quote: "The pre-trained language model has a rich understanding of language but it does not yet follow instructions or behave in the way we would expect an assistant to."

### C8. InstructGPT: fine-tuning on human demonstrations and preferences; a 1.3B instruction-tuned model preferred over 175B GPT-3
- Use in chapter: one or two sentences on how a base model becomes an assistant, pointing to `instructions`.
- Source: `ouyang2022training`, https://arxiv.org/abs/2203.02155 (text checked in v1)
- Location: abstract, p. 1; Figure 2 caption, p. 3.
- Quotes: "Making language models bigger does not inherently make them better at following a user's intent."; "In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters."; "(1) supervised fine-tuning (SFT), (2) reward model (RM) training, and (3) reinforcement learning via proximal policy optimization (PPO) on this reward model."

### C9. ChatGPT: announced 2022-11-30; fine-tuned from a GPT-3.5 series model with RLHF, using InstructGPT's methods
- Use in chapter: the reader has almost certainly heard of ChatGPT; this pins down what it was relative to the underlying model.
- Source: `openai2022chatgpt`. openai.com returned HTTP 403 to direct fetches, so the post was read in the Internet Archive snapshot of the publication day: https://web.archive.org/web/20221130180912/https://openai.com/blog/chatgpt/
- Location: header and "Methods" section.
- Quotes: "November 30, 2022"; "ChatGPT is a sibling model to InstructGPT"; "We trained this model using Reinforcement Learning from Human Feedback (RLHF), using the same methods as InstructGPT, but with slight differences in the data collection setup."; "ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022."
- Note: a company blog post is a primary source for what the company released and when. It is not independent evidence for capability claims, and the chapter makes none from it.

### C10. An instruction-tuned model has the same architecture as its base model
- Use in chapter: "still the same pipeline. Only its parameters have changed."
- Source: `ouyang2022training` (URL above)
- Location: section 1, p. 3.
- Quote: "These models have the same architecture, and differ only by the fact that InstructGPT is fine-tuned on our human data."

### C11. A conversation is laid out as one text with markers for who is speaking
- Use in chapter: the sentence on chat turns as one document.
- Source: `grattafiori2024llama` (URL above)
- Location: section 4.1.1, p. 16.
- Quote: "we design a new multi-message chat protocol which uses various special header and termination tokens. The header tokens are used to indicate the source and destination of each message in a conversation."

### C12. Correction: the Llama 3.1 context window
- The draft printed "128,000" for the context window. The source says "128K", and its Table 4 (p. 10) shows the length is 131,072. Fixed as logged under C6.

## Worked examples [D-009]

All computed by `code/checks/destination.py`. The scores and probabilities are invented; the arithmetic on them is exact.

- Example 1: scores to probabilities by softmax on a six-token toy vocabulary, and one random draw (0.80) mapped to a token.
- Example 2: the probability of a six-token text as a product of next-token probabilities. Its last factor reuses Example 1.
- Example 3: storage for the parameter counts in C4 to C6, at 32 and 16 bits per parameter.

The figure `figures/pipeline-destination.svg` is drawn by `figures/pipeline.py` [D-014]. It imports Example 1 from the check script, so its probabilities are computed, not typed in. Its token IDs are labelled illustrative.

## Terms defined in this chapter

For the glossary, when it is drafted: large language model (LLM), token, vocabulary, self-supervised learning, language model, tokenizer, token ID, embedding table, vector, embedding, transformer, attention (named only), logits, softmax, sampling, autoregressive generation, context window, parameters, weights, architecture, training, loss (named only), pretraining, base model, inference, chat product.

## Deliberately left out

- Any parameter count or training cost for current closed frontier models: most are not disclosed by their makers, and a guess is not a source. If the chapter needs a "today" figure, it uses a disclosed open-weight model with an "as of" date.
- History of each component: each later chapter carries its own.

## Notes for later chapters

- `generation`: this chapter says the whole pipeline "runs again" for each new token. That is right conceptually, but in practice the work already done on earlier tokens is cached and reused. `generation` should present the cache as an optimization of the same loop, so it doesn't seem to contradict this chapter.
- `tokens`: not checked here, from the verifier's memory only: the released Llama 3.1 tokenizer may have 128,256 entries once special tokens are counted. The paper's 128,000 is what this chapter cites.

## Independent check

2026-11-11. A separate agent that did not write the chapter fetched all seven sources itself, in the versions named above, and checked every claim, quote, page number, worked-example number, and bibliography entry.

- Confirmed: C1 to C9 as logged, all quotes verbatim and all pages correct. All numbers in the three tables and the prose match `code/checks/destination.py`. The figure regenerates byte-identically. `tools/check.py` passes.
- Errors found and fixed: the Llama 3.1 context window was printed as 128,000 instead of 128K (131,072) (C12). "From a few hundred to several thousand" understated vector lengths, since Llama 3.1 405B uses 16,384.
- Warnings acted on:
  - "Tens of thousands" of classes now allows for larger vocabularies.
  - The GPT-2 paper is now said to "cite" the 1980 and 2003 work, not to "credit the idea" to it.
  - Attention now includes the token's own position.
  - Position information is now named.
  - The figure computes its numbers and says it shows the most probable pick.
  - "Most expensive step" was removed as unsourced, and "once" was replaced.
  - The knowledge-cutoff sentence now refers to the parameters.
  - The reply counts toward the context window.
  - "Often used interchangeably".
  - Reinforcement learning and fine-tuning are glossed.
  - C10 and C11 are cited.
  - "Successors" was reworded.
  - The thread sentence was rephrased.
- Re-checked after fixing: every new location (Table 1 p. 2, Table 3 p. 7, Table 4 p. 10, p. 16; ouyang2022training p. 3; radford2018improving pp. 3 and 5) was located again by the writer in the same fetched texts.
