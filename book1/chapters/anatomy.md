# Anatomy of a transformer {#anatomy}

<!-- D-002: intuition only; formulas in standard form (the feed-forward network, the parameter estimate), every symbol explained. D-003: no code. D-009: numbers from code/checks/anatomy.py. D-014: figures from figures/anatomy.py. D-019: "residual stream" for the vector between layers. -->

[The destination chapter](#destination) drew an LLM as a row of boxes and left one of them, "Layers", closed. [The previous chapter](#attention) explained the mechanism inside it. This chapter opens the box and follows one token all the way through a real model, from its ID to the scores for the next token. The model is GPT-2 small, which OpenAI released in 2019: small enough that every number can be written down, and built the same way, in all essentials, as the much larger models that followed.

By the end the reader should be able to name every part of a transformer language model, say what each part does and how many parameters it holds, and tell the three main families of transformer apart.

## From the 2017 translator to a language model

The 2017 transformer was a translation system with two stacks. "The encoder is composed of a stack of N = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network" [@vaswani2017attention, p. 3]. The decoder had the same two sub-layers plus a third, attention from the decoder to the encoder's output, the transformer's version of Bahdanau's attention from [the chapter on sequences](#seq2seq), often called **cross-attention**. This book calls each repeated unit a **block**; papers say "layer" or "block" for the same thing.

A language model needs only one stack. In January 2018, Peter Liu and colleagues at Google, working on summarizing Wikipedia sources, introduced "a decoder-only architecture": they dropped the encoder, joined the input and output into a single sequence, and trained the decoder "as a standard language model" [@liu2018generating, pp. 1, 5]. A few months later OpenAI's GPT used "a multi-layer Transformer decoder" for its language model, citing Liu and colleagues [@radford2018improving, p. 3]. With no encoder there is nothing for cross-attention to attend to, so a **decoder-only** block has two sub-layers: masked self-attention and a feed-forward network. That is the block of GPT-2, GPT-3, and Llama 3.

## Following one token

![GPT-2 small (2019), with its sizes. A token ID picks a row of the token table, a position picks a row of the position table, and their sum starts the residual stream. Each of 12 blocks computes attention, then a feed-forward network, each from its own normalized copy of the stream, and adds each result back. A final normalization and the output layer, which reuses the token table, give one score per vocabulary entry. Blue boxes hold learned parameters; the layer normalizations (grey) hold a few as well, 38,400 in all. The 2017 transformer normalized the stream after each addition instead of normalizing each sub-layer's input; later models differ in the ways described at the end of the chapter.](../../figures/anatomy-architecture.svg){#fig:anatomy-architecture}

<!-- D-009: code/checks/anatomy.py, Example 6 -->

Take the token " cat" in "The cat sat on the", the destination chapter's example. Its ID in GPT-2's vocabulary is 3797 ([the chapter on tokens](#tokens)), and it is the second token of the text.

**The two tables.** The ID selects one row of the **token table** (the embedding table of [the destination chapter](#destination)), which has 50,257 rows (one per vocabulary entry) of 768 numbers each. The position selects one row of a second table, the **position table**, with 1,024 rows of 768 numbers: GPT-2 learned a vector for each position rather than using the 2017 paper's sine waves, as GPT-1 had [@radford2018improving, p. 5; @openai2019gpt2code]. The two rows are added. The result, 768 numbers for this position, is where the computation for " cat" begins. Every position in the text gets its own such vector, and all of them travel up through the model side by side.

**The residual stream.** From here on, think of each position's vector as a running total. [The chapter on deep networks](#depth) introduced residual connections, in which each layer adds a correction to a running value instead of replacing it; in a transformer, every sub-layer works that way. Interpretability researchers, who try to work out what a trained model's numbers mean, call the running vector the **residual stream**: "The residual stream is simply the sum of the output of all the previous layers and the original embedding. We generally think of the residual stream as a communication channel, since it doesn't do any processing itself and all layers communicate through it" [@elhage2021mathematical]. Kaplan and colleagues already used the term in a 2020 paper, and this 2021 one, which shares some of its authors, developed it [@kaplan2020scaling, p. 6]. Other writing calls the same vector the hidden state. This book keeps "embedding" for the rows of the token table, and "residual stream" for the running vector built on top of it. The residual stream is a way of describing the computation that researchers have found useful; it is not a claim about what the numbers mean.

**A block.** Each of GPT-2 small's 12 blocks does two updates to the stream. First, it takes a normalized copy of every position's vector, runs masked multi-head attention over them, with 12 heads of 64 numbers each, and adds the result back into each position's stream. This is the only step in which information moves between positions: here the stream at " cat" can take in something from "The". Second, it takes a normalized copy again, runs it through a feed-forward network, and adds the result back. In OpenAI's words, layer normalization "was moved to the input of each sub-block" [@radford2019language, p. 4], so inside the blocks the stream itself is never normalized, only the copies the sub-layers read.

**The feed-forward network.** The second sub-layer, the **feed-forward network**, is the reader's old friend the multilayer perceptron: a network with one hidden layer, of the kind [the backpropagation chapter](#backprop) trained. The 2017 paper gives its standard form:

$$\text{FFN}(x) = \max(0,\, x W_1 + b_1)\, W_2 + b_2$$

where $x$ is one position's vector, $W_1$ and $b_1$ are the weights and biases of a hidden layer four times wider than $x$, $\max(0,\, x W_1 + b_1)$ applies the ReLU of [the deep learning chapter](#deep-turn) to each number, and $W_2$ and $b_2$ map the result back to the original width [@vaswani2017attention, p. 5]. The same network, with the same weights, is "applied to each position separately and identically" [@vaswani2017attention, p. 5]: like one fitted model scoring every row of a data table. In GPT-2 small it maps 768 numbers to 3,072 and back, with a variant of ReLU called GELU [@radford2018improving, p. 5; @openai2019gpt2code]. What these layers do is less clear than what attention does. Mor Geva and colleagues argued in 2021 that they "operate as key-value memories", in which the first matrix holds detectors for patterns in the text and the second holds what to add when a detector fires, especially in later layers [@geva2021transformer, p. 5484]. That was one study of one model, and the authors of the residual-stream paper wrote that they had had "much less success in understanding MLP layers" [@elhage2021mathematical]. It is an interpretation, not settled fact.

**The output layer.** After the 12th block comes one more normalization [@radford2019language, p. 4], and then the output layer of [the destination chapter](#destination): one score, or logit, per vocabulary entry. In GPT-2 each score is the dot product of the final vector with that entry's own row of the token table. The same table is used at the bottom to turn IDs into vectors and at the top to turn vectors into scores, an idea called **weight tying**, which Ofir Press and Lior Wolf recommended in a 2017 paper after finding that it lowered perplexity on held-out text, a sign of less overfitting [@press2017using, pp. 157, 161]. The 2017 transformer tied its tables too [@vaswani2017attention, p. 5]. Not every model does: Meta's released code for Llama 3 has a separate output layer [@meta2024llama3code]. The 50,257 scores go to the softmax, and the rest is the destination chapter's story.

That is the whole path. A row of each table, added; twelve rounds of "read a normalized copy, compute, add back", alternating between mixing positions and processing each position alone; a final normalization; a dot product with every row of the token table. Every box in the destination chapter's figure now has a name: the "Vectors" box is the two tables, "Layers" is the stack of blocks and its residual stream, and "Scores" is the output layer.

## Where the parameters are

<!-- D-009: code/checks/anatomy.py, Example 1 -->

Every learned number sits in one of these boxes, and they can be counted exactly from five published settings: a vocabulary of 50,257, a context of 1,024, a width of 768, 12 heads, and 12 layers [@openai2019gpt2code].

| Part | Parameters | Share |
|---|---:|---:|
| Token table (50,257 x 768) | 38,597,376 | 31.02% |
| Position table (1,024 x 768) | 786,432 | 0.63% |
| Attention, 12 blocks | 28,348,416 | 22.78% |
| Feed-forward networks, 12 blocks | 56,669,184 | 45.54% |
| Layer normalizations | 38,400 | 0.03% |
| **Total** | **124,439,808** | |

Inside one block, attention holds four matrices of 768 by 768 (queries, keys, values, and the output that recombines the heads), and the feed-forward network two of 768 by 3,072, plus small biases: 2,362,368 and 4,722,432 numbers. So two-thirds of each block is feed-forward network, as Geva and colleagues noted [@geva2021transformer, p. 5484], but for the whole model, with its large token table, the share is under half. The number of heads does not change the count: twelve heads of 64 numbers use the same matrices as one head of 768. Weight tying matters at this size: a separate output table would add another 38,597,376 parameters, 31% more.

The total matches OpenAI's released checkpoint (the saved file of trained weights), 124,439,808 numbers, which shows that nothing is hidden. It does not match the GPT-2 paper, which listed the smallest model as 117 million parameters [@radford2019language, p. 4]. OpenAI later wrote that "our original parameter counts were wrong due to an error (in our previous blog posts and paper)", and released the models as 124M, 355M, 774M, and 1558M [@openai2019gpt2code]. It did not say what the error was.

<!-- D-009: code/checks/anatomy.py, Example 2 -->

Papers often quote a shortcut. Jared Kaplan and colleagues estimated the parameters of a transformer, leaving out the embedding tables, as

$$N \approx 12\, n_{\text{layer}}\, d_{\text{model}}^2$$

where $n_{\text{layer}}$ is the number of blocks and $d_{\text{model}}$ is the width of the residual stream: 4 width-by-width matrices for attention and 8 for the feed-forward network in each block [@kaplan2020scaling, p. 6]. For GPT-2 small it gives 84,934,656 against an exact 85,056,000 without the tables, 0.14% low. Leaving out the tables is a convention for Kaplan and colleagues' scaling laws ([the chapter on scale](#scale)); the sizes in model names include them. <!-- D-009: code/checks/anatomy.py, Example 3 --> Counting every part the same way gives about 175 billion for GPT-3's 96 blocks of width 12,288 [@brown2020language, p. 8], but the shortcut fails for newer designs: for Llama 3 8B, whose blocks differ in ways described below, it gives 6.44 billion for the blocks against an exact 6.98 billion.

## Every position predicts at once

<!-- D-009: code/checks/anatomy.py, Example 4 -->

![Two attention masks for "The cat sat on the". Each row is a token doing the looking, each column a token it may look at; blue cells are allowed. Left: fully visible, every token sees every other, as in an encoder. Right: causal, each token sees only itself and earlier tokens, as in a decoder-only language model.](../../figures/anatomy-masks.svg){#fig:anatomy-masks}

A language model's job at each position is to predict the next token, so no position may see the tokens after it. [The previous chapter](#attention) introduced the fix in passing, the **causal mask**; here is what it does to the model. Before the softmax, every attention score from a position to a later position is set to minus infinity, so its weight comes out exactly zero. The 2017 paper: masking "ensures that the predictions for position i can depend only on the known outputs at positions less than i" [@vaswani2017attention, p. 3]. In a five-token text, 15 of the 25 possible pairs are allowed. For example, if "sat" gives made-up scores to the five positions, the mask leaves weights of 0.20, 0.48, and 0.32 on "The", "cat", and "sat", and exactly zero on the two later positions, whatever their scores were. This is the rule against leakage that the reader knows from validating forecasts: a model must not be scored on data it could peek at.

<!-- D-009: code/checks/anatomy.py, Example 5 -->

The mask has a large payoff in training. Because each position can see only its past, one pass through the model makes a separate, honest prediction at every position at once. GPT-1's training compared the vector at every position with the token that actually came next [@openai2018finetunecode], and GPT-2's code asks, in a comment, "Do tokens <n predict token n?" [@openai2019gpt2code]. A window of 1,025 tokens gives 1,024 predictions from one pass; if each of GPT-2's batch of 512 [@radford2019language, p. 4] is a full window, that is 524,288 predictions per training step. [The chapter on training](#training) builds on this. Generating new text is different: there the next token is not known in advance, so it is still produced one at a time.

## Three families

The mask, more than anything else, separates the three kinds of transformer the reader will meet.

- **Decoder-only** models (GPT, Llama) use the causal mask in every block. They read and write left to right, which is what generating text needs.
- **Encoder-only** models (BERT, 2018) use a fully visible mask: every token sees the whole input. BERT's authors note that such a model is "often referred to as a "Transformer encoder" while the left-context-only version is referred to as a "Transformer decoder" since it can be used for text generation" [@devlin2019bert, pp. 4173-4174]. An encoder-only model is good at understanding a text it is given but cannot continue it left to right.
- **Encoder-decoder** models (the 2017 transformer, and T5 in 2019) keep both stacks: a fully visible encoder for the input, a causal decoder for the output, and cross-attention between them [@raffel2020exploring, p. 16].

So "decoder-only" names a mask, not a decoder of anything. Why the families diverged, and what each was trained to do, is the subject of [the chapter on pretraining](#pretraining).

## The context window

The context window of [the destination chapter](#destination) now has a concrete meaning. In GPT-2, the position table has 1,024 rows, so the model cannot be given a 1,025th token: there is no vector for that position. GPT-1 had 512 positions [@radford2018improving, p. 5], GPT-2 1,024 [@radford2019language, p. 4], and GPT-3 2,048 [@brown2020language, p. 8]. Models that use rotary positions instead of a table, such as Llama 3 [@grattafiori2024llama, p. 7], have no such table, so their limit is set by how long the texts they were trained on were, up to 131,072 tokens for Llama 3.1 [@grattafiori2024llama, pp. 3, 10].

A longer window costs more, in two ways. Each head in each block scores every pair of positions, so the number of scores grows with the square of the length: about a million per head per layer at 1,024 tokens, and about 17 billion at 131,072. BERT's authors put it plainly: "Longer sequences are disproportionately expensive because attention is quadratic to the sequence length" [@devlin2019bert, p. 4183]. At short lengths, though, this is a small part of the work. Kaplan and colleagues' accounting gives two operations per parameter for each token, plus a term for the attention scores [@kaplan2020scaling, p. 7]; <!-- D-009: code/checks/anatomy.py, Example 5 --> for GPT-2 small at 1,024 tokens the scores add only 11% to the parameter term, but at 131,072 tokens they would be about fourteen times as large as it. The second cost is memory while generating text: a model keeps the keys and values of every earlier token, which is why Llama 3 uses fewer key and value heads "to reduce the size of key-value caches during decoding" [@grattafiori2024llama, p. 6]. [The chapter on generation](#generation) explains that cache.

## What changed after 2017

The skeleton has lasted: a token table, a stack of blocks that alternate attention and a feed-forward network, each with a residual connection and a normalization, and an output layer. The parts have been adjusted. As of Llama 3 (2024):

- **Where the normalization sits.** The 2017 transformer normalized the stream after each addition, "LayerNorm(x + Sublayer(x))" [@vaswani2017attention, p. 3], usually called post-norm. GPT-2 moved it to the input of each sub-layer (pre-norm), and LLaMA (2023) did the same "to improve the training stability" [@touvron2023llama, p. 3]. This is not one-sided. A 2020 analysis found that post-norm needs a warmup, starting with a small learning rate and raising it gradually, which pre-norm can do without [@xiong2020layer, p. 1], but another 2020 study, on translation models, found that post-norm, when it trained at all, "is more likely to reach a better performance" [@liu2020understanding, p. 5749]. GPT-2, GPT-3, LLaMA, and Llama 3 all use pre-norm (as of 2024).
- **A simpler normalization.** LLaMA uses RMSNorm, which rescales without subtracting the mean [@touvron2023llama, p. 3; @zhang2019root, p. 1].
- **A gated feed-forward network.** LLaMA replaced ReLU with SwiGLU [@touvron2023llama, p. 3], a design with three matrices instead of two [@shazeer2020glu, p. 2], whose author wrote with unusual candor, "We offer no explanation as to why these architectures seem to work; we attribute their success, as all else, to divine benevolence" [@shazeer2020glu, p. 3].
- **Positions inside attention.** Rotary embeddings replaced the position table ([the previous chapter](#attention)).
- **Fewer key and value heads.** Llama 3 8B uses 32 query heads but only 8 key and value heads (the larger Llama 3 models also use 8), an arrangement called grouped-query attention, to speed up generation [@grattafiori2024llama, pp. 6-7; @ainslie2023gqa, p. 4895].

[The chapter on the transformer since 2017](#since-2017) covers these changes. The Llama 3 paper is clear about their weight: it "does not deviate significantly from Llama and Llama 2", and "our performance gains are primarily driven by improvements in data quality and diversity as well as by increased training scale" [@grattafiori2024llama, p. 6].

## What to carry forward

- A decoder-only transformer is a token table, a position signal, a stack of identical blocks, a final normalization, and an output layer.
- Each position carries a vector, the residual stream, from bottom to top. Every sub-layer reads a normalized copy and adds its result back.
- Each block has two sub-layers: attention, the only place information moves between positions, and a feed-forward network, a small multilayer perceptron applied to each position on its own.
- The output layer scores every vocabulary entry; in GPT-2 it reuses the token table (weight tying).
- GPT-2 small has 124,439,808 parameters: about a third in the token table, and two-thirds of each block in the feed-forward network. The paper's 117 million was later corrected.
- The causal mask lets one pass train every position at once; generation is still one token at a time.
- The mask separates the families: decoder-only (causal), encoder-only (fully visible), and encoder-decoder (both, joined by cross-attention).
- The context window is limited by the position table or by training, and its cost grows with the square of its length once it is long.
- Since 2017 the details changed (pre-norm, RMSNorm, SwiGLU, rotary positions, grouped-query attention); the skeleton did not.
