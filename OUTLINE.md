# Outline

A living document. It changes as the books are written; nothing here is fixed.

**Unverified:** every date, name, and attribution below comes from model memory and has not been checked against a source. They are here to define scope. Each is verified at the chapter's research stage, per `AGENTS.md`. "Candidate sources" are the ones to fetch first, not a claim that they have been read.

**Conventions** (checked by `tools/check.py`):

- Every chapter has a stable ID in its heading, `{#like-this}`. Chapters refer to each other by ID, never by number [D-010].
- "Depends on" lists chapters the reader must have read first. They must come earlier in the outline.
- "Builds on" (Book 2) lists the Book 1 chapters a chapter makes concrete.
- Status is one of `outlined`, `researched`, `drafted`, `verified`, `approved`.

Two books [D-001]. Book 1 is the priority.

## Book 1 - Concepts and history

Intuition only [D-002], no code [D-003]. Scope: core plus modern practice [D-004]. Target: about 350 pages of chapters plus about 30 pages of appendices. Page counts are rough budgets.

Structure [D-008]: the destination first, then two parallel histories (how networks learn, Parts I-II; how language is modeled, Part III) that meet at the transformer in Part IV.

| Part | Title | Years covered |
|------|-------|---------------|
| - | The destination | - |
| I | Neural networks before deep learning | 1943-2005 |
| II | Deep learning starts working | 2006-2016 |
| III | Teaching machines language | 1948-2016 |
| IV | The transformer | 2017 |
| V | From transformer to LLM | 2018-2022 |
| VI | From LLM to assistant | 2020-2024 |
| VII | The working landscape | 2017-present |

### Front matter

#### Preface {#preface}

- **Goal:** Who the book is for, what it assumes, what it deliberately leaves out (derivations, code), how to read it, its as-of date, and where Book 2 picks up. (~4 pp)
- **Depends on:** none
- **Status:** outlined

#### 1. The destination: an LLM in one picture {#destination}

- **Goal:** Give the reader the whole machine at low resolution before the history begins, so every later chapter has a place to land. (~10 pp)
- **Concepts:** next-token prediction; the pipeline (text, tokens, vectors, layers, probabilities, sampling, loop); parameters; training vs inference; "model" vs "chat product".
- **Bridge:** an LLM is a (very large) classifier over a vocabulary, applied repeatedly.
- **Key figure:** the end-to-end pipeline diagram, reused and progressively filled in across the book.
- **Depends on:** none
- **Status:** approved

### Part I - Neural networks before deep learning

#### 2. The artificial neuron (1943-1969) {#neuron}

- **Goal:** What a neuron computes, how a single one learns, and why the first wave ended. (~14 pp)
- **Concepts:** weights, bias, activation, decision boundary, linear separability, the perceptron learning rule, the XOR problem.
- **History:** McCulloch and Pitts (1943); Hebb (1949); Rosenblatt's perceptron (1958) and the press around it; Widrow and Hoff's ADALINE (1960); Minsky and Papert's *Perceptrons* (1969); the first winter.
- **Bridge:** a neuron with a sigmoid is logistic regression.
- **Key figure:** one neuron as a weighted vote; XOR points that no single line separates.
- **Candidate sources:** McCulloch and Pitts 1943; Hebb 1949; Rosenblatt 1958; Widrow and Hoff 1960; Olazaran 1993 (history of the perceptron controversy; used in place of Olazaran 1996, which is paywalled); Goodfellow, Bengio, Courville 2016. Minsky and Papert 1969 and the 1958 press coverage are quoted through Olazaran 1993.
- **Depends on:** `destination`
- **Status:** verified

#### 3. Learning in layers (1970-1989) {#backprop}

- **Goal:** How a network with hidden layers learns: the credit assignment problem and backpropagation as its answer. (~16 pp)
- **Concepts:** hidden layers, forward pass, loss function, gradient descent as "walking downhill", backpropagation as passing blame backward, learning rate, epochs, local minima, universal approximation (what it does and does not promise).
- **History:** Linnainmaa (1970) and Werbos (1974) as precursors; Rumelhart, Hinton, and Williams (1986); the PDP volumes; Cybenko (1989) and Hornik et al. (1989). The priority dispute is presented, not adjudicated.
- **Bridge:** gradient descent on a loss is the same idea as fitting a regression, with more knobs.
- **Key figure:** a tiny 2-2-1 network solving XOR, with one worked forward pass and one weight update in numbers.
- **Candidate sources:** Rumelhart, Hinton, Williams 1986 (Nature letter and PDP chapter); Cybenko 1989; Hornik, Stinchcombe, White 1989; Griewank 2012 and Schmidhuber 2014 (priority history); Olazaran 1993. Werbos 1974 and Linnainmaa 1970 are described through these.
- **Depends on:** `neuron`
- **Status:** verified

#### 4. Networks with structure, and the second winter (1980-2005) {#structure}

- **Goal:** Why plain layered networks were not enough, the two structural ideas that survived (sharing weights across space and across time), and why the field moved to SVMs in the reader's own era. (~14 pp)
- **Concepts:** convolution and weight sharing (brief; images are not this book's subject [D-016]); recurrent networks and hidden state; unrolling through time; vanishing and exploding gradients; LSTM gates as a memory cell.
- **History:** Fukushima's neocognitron (1980); LeCun's digit recognizers (1989, 1998); Elman (1990); Hochreiter (1991) and Bengio et al. (1994) on vanishing gradients; Hochreiter and Schmidhuber's LSTM (1997); Cortes and Vapnik's SVM (1995) and the 2000s consensus.
- **Bridge:** this is the point where the reader's own knowledge of the field begins and ends.
- **Key figure:** an RNN unrolled over a sentence, with the gradient signal fading as it travels back.
- **Candidate sources:** Fukushima 1980; LeCun et al. 1989 and 1998; Elman 1990; Hochreiter 1991 (in German); Bengio, Simard, Frasconi 1994; Cortes and Vapnik 1995; Hochreiter and Schmidhuber 1997; Hochreiter et al. 2001; LeCun, Bengio, Hinton 2015; Schmidhuber 2014; Goodfellow et al. 2016.
- **Depends on:** `backprop`
- **Status:** verified

### Part II - Deep learning starts working

#### 5. The turn: data, compute, and depth (2006-2012) {#deep-turn}

- **Goal:** What changed between the reader's era and 2012, and why "the same old networks" suddenly won. (~14 pp)
- **Concepts:** depth and learned feature hierarchies; representation learning vs hand-built features; GPUs and why matrix arithmetic suits them; large labeled datasets; ReLU; the benchmark as a forcing function.
- **History:** Hinton, Osindero, and Teh's deep belief nets (2006); Raina, Madhavan, and Ng on GPUs (2009); ImageNet (2009); speech recognition results (2009-2012); AlexNet (2012).
- **Bridge:** feature engineering, the core 2000s skill, is what the network now does for itself.
- **Key figure:** ImageNet error rate by year, with 2012 marked.
- **Candidate sources:** Hinton et al. 2006; Deng et al. 2009; Krizhevsky, Sutskever, Hinton 2012; LeCun, Bengio, Hinton 2015 (Nature review).
- **Depends on:** `backprop`, `structure`
- **Status:** verified

#### 6. The training loop (1951-2017) {#toolkit}

- **Goal:** How a modern network is trained step by step, so the reader can read the optimizer half of a training recipe. Split from a larger chapter [D-017]. (~13 pp)
- **Concepts:** tensors and shapes; minibatches and stochastic gradient descent; momentum; RMSProp and Adam; learning-rate schedules and warmup; gradient clipping; hyperparameters and the validation set; early stopping; reading a loss curve; automatic differentiation; frameworks.
- **History:** Robbins and Monro (1951); momentum (Polyak 1964; Rumelhart et al. 1986); RMSProp (2012) and Adam (2014); warmup (2015-2017); Theano, Torch, TensorFlow, PyTorch.
- **Bridge:** SGD is a 1951 statistics idea run at scale; the validation set, early stopping, and weight decay are the reader's own tools.
- **Key figure:** plain gradient descent against momentum in a narrow valley; an annotated loss curve.
- **Candidate sources:** Robbins and Monro 1951; Bottou 2010; Sutskever et al. 2013; Kingma and Ba 2015; Goyal et al. 2017; Baydin et al. 2018.
- **Depends on:** `backprop`, `deep-turn`
- **Status:** verified

#### 7. Making deep networks trainable (2010-2016) {#depth}

- **Goal:** The architectural and regularizing parts that let networks go from a handful of layers to hundreds, so the reader can read the model half of a recipe and recognize the parts of a transformer block [D-017]. (~13 pp)
- **Concepts:** initialization by layer size; dropout; batch normalization; layer normalization; residual (skip) connections and the degradation problem; reading a training recipe.
- **History:** Glorot and Bengio (2010); He et al. on initialization (2015); dropout (2012-2014); batch norm (2015) and the dispute over why it works; highway networks and ResNet (2015); layer norm (2016).
- **Bridge:** dropout on a linear model is ridge regression in expectation; the degradation problem is not overfitting.
- **Key figure:** a residual block as "a correction added to a running value" (this returns in `anatomy` as the residual stream).
- **Candidate sources:** Glorot and Bengio 2010; Srivastava et al. 2014; Ioffe and Szegedy 2015; Santurkar et al. 2018; He et al. 2015; Srivastava, Greff, Schmidhuber 2015; Ba, Kiros, Hinton 2016.
- **Depends on:** `toolkit`
- **Status:** verified

### Part III - Teaching machines language

#### 8. Language as prediction (1948-2000) {#prediction}

- **Goal:** Establish that "predict the next word" is an old, well-defined statistical problem, and show exactly where the classical solution breaks. (~14 pp)
- **Concepts:** language model; probability of a sequence; n-grams; sparsity and smoothing; entropy, cross-entropy, and perplexity (by intuition: "how surprised is the model"); the curse of dimensionality.
- **History:** Shannon (1948, 1951) and his guessing game; n-gram models in speech recognition and translation (Jelinek and IBM); smoothing work through the 1990s.
- **Bridge:** the reader likely knows n-grams and naive Bayes; this is the same counting, pushed until it fails.
- **Key figure:** Shannon's game on one sentence; a count table that is almost entirely zeros.
- **Candidate sources:** Shannon 1948; Shannon 1951; Chen and Goodman 1998; Jurafsky and Martin (textbook).
- **Depends on:** `destination`
- **Status:** verified

#### 9. Words as vectors (1954-2014) {#embeddings}

- **Goal:** The single most important new idea for the reader: meaning as position in a learned space. (~16 pp)
- **Concepts:** one-hot vs dense representations; the distributional hypothesis; embeddings; similarity as closeness; the neural language model; learning embeddings as a side effect of prediction; analogies and their limits; one vector per word as a weakness.
- **History:** Harris (1954) and Firth (1957); latent semantic analysis (1990); Bengio et al.'s neural probabilistic language model (2003); Collobert and Weston (2008); word2vec (2013); GloVe (2014).
- **Bridge:** LSA applies the SVD behind PCA to a word-document matrix; embeddings are the learned, predictive version, which later analysis showed to be closer to counting than it looked.
- **Key figure:** a 2D projection of real word vectors, with the numbers computed, not drawn by hand.
- **Candidate sources:** Deerwester et al. 1990; Bengio et al. 2003; Mikolov et al. 2013 (both papers); Pennington et al. 2014.
- **Depends on:** `backprop`, `prediction`
- **Status:** verified

#### 10. Reading and writing sequences (2010-2016) {#seq2seq}

- **Goal:** How networks came to process whole sentences, the bottleneck that limited them, and attention as the fix. This chapter sets up the transformer. (~16 pp)
- **Concepts:** RNN language models; LSTM and GRU in use; encoder-decoder (seq2seq); the fixed-vector bottleneck; attention as "look back at the input and weight what matters"; alignment; why recurrence is slow to train.
- **History:** Mikolov's RNN language model (2010); Cho et al. and Sutskever, Vinyals, and Le (2014); Bahdanau, Cho, and Bengio's attention (2014); Google's neural translation system (2016).
- **Bridge:** statistical machine translation with phrase tables, replaced in about two years.
- **Key figure:** an attention heat map between a source and target sentence.
- **Candidate sources:** Sutskever et al. 2014; Cho et al. 2014; Bahdanau et al. 2014; Wu et al. 2016.
- **Depends on:** `structure`, `toolkit`, `embeddings`
- **Status:** verified

#### 11. Tokens: what the model actually sees (1994-2018) {#tokens}

- **Goal:** Why models read neither words nor characters, and what follows from that. (~12 pp)
- **Concepts:** vocabulary; the out-of-vocabulary problem; character vs word vs subword; byte-pair encoding step by step; special tokens; token IDs; why token counts drive cost and limits; known oddities (spelling, arithmetic, non-English text).
- **History:** Gage's BPE for compression (1994); Sennrich, Haddow, and Birch bring it to translation (2015-2016); WordPiece; SentencePiece (2018).
- **Key figure:** one sentence tokenized three ways; a BPE merge table built by hand on a toy corpus.
- **Candidate sources:** Gage 1994; Sennrich et al. 2016; Kudo and Richardson 2018.
- **Depends on:** `prediction`, `embeddings`
- **Status:** verified

### Part IV - The transformer

#### 12. Attention without recurrence (2017) {#attention}

- **Goal:** Self-attention, fully understood by intuition: every token gathers information from every other token, in parallel. (~18 pp)
- **Concepts:** self-attention; queries, keys, and values as a soft lookup; attention weights via softmax; multiple heads as multiple questions asked at once; why order must be added back (positional information); why parallelism mattered for training on GPUs.
- **History:** the Google team and the paper "Attention Is All You Need" (2017); what it was built for (translation) and what it replaced.
- **Bridge:** a soft, learned version of a database lookup or a kernel-weighted average.
- **Key figure:** one attention head worked through on a five-token sentence with real small numbers.
- **Candidate sources:** Vaswani et al. 2017; first-hand accounts by the authors where available.
- **Depends on:** `toolkit`, `embeddings`, `seq2seq`, `tokens`
- **Status:** verified

#### 13. Anatomy of a transformer {#anatomy}

- **Goal:** Follow one token from input to output prediction through the whole model. After this chapter the reader can label every box in the `destination` diagram. (~18 pp)
- **Concepts:** embedding table; the residual stream; the block (attention, then feed-forward network, each with normalization and a skip connection); stacking layers; the output layer, logits, and softmax; encoder, decoder, and encoder-decoder variants; causal masking; context window; where the parameters are and how to count them.
- **Key figure:** the full annotated architecture; a parameter-count table for a small model.
- **Candidate sources:** Vaswani et al. 2017; Radford et al. 2018 for the decoder-only form; Elhage et al. 2021 for the residual-stream framing.
- **Depends on:** `toolkit`, `depth`, `attention`
- **Status:** verified

### Part V - From transformer to LLM

#### 14. Pretraining: learn language first, tasks later (2015-2019) {#pretraining}

- **Goal:** The shift from one model per task to one pretrained model adapted to many. (~14 pp)
- **Concepts:** transfer learning; self-supervised learning (labels for free from raw text); pretraining and fine-tuning; contextual embeddings; masked vs causal objectives; why BERT-style and GPT-style models diverged.
- **History:** Dai and Le (2015); ELMo and ULMFiT (2018); GPT (2018); BERT (2018); T5 (2019).
- **Bridge:** the 2000s rule "you need labeled data for your task" stops being true.
- **Key figure:** masked prediction vs next-token prediction on the same sentence.
- **Candidate sources:** Peters et al. 2018; Howard and Ruder 2018; Radford et al. 2018; Devlin et al. 2018.
- **Depends on:** `anatomy`
- **Status:** verified

#### 15. Scale (2019-2022) {#scale}

- **Goal:** Why making the same model much larger changed what it could do, and what "large" means in numbers. (~14 pp)
- **Concepts:** parameters, data, and compute as the three dials; in-context and few-shot learning; scaling laws; emergent abilities and the debate around the term; the cost of a training run; the general-methods argument.
- **History:** GPT-2 and its staged release (2019); Sutton's "The Bitter Lesson" (2019); GPT-3 (2020); Kaplan et al. scaling laws (2020); Chinchilla (2022).
- **Key figure:** model size and training-data size by year on a log scale.
- **Candidate sources:** Radford et al. 2019; Brown et al. 2020; Kaplan et al. 2020; Hoffmann et al. 2022; Sutton 2019.
- **Depends on:** `pretraining`
- **Status:** verified

#### 16. How an LLM is trained {#training}

- **Goal:** The pretraining process from raw text to a finished set of weights, as a procedure the reader could describe to someone else. (~14 pp)
- **Concepts:** corpus collection, filtering, and deduplication; tokenizing the corpus; the training example (a window of text, predict each next token); loss; the training loop at scale (batches, steps, checkpoints); precision and hardware; what the loss curve tells you; what the weights do and do not contain (memorization vs generalization).
- **Key figure:** one training step drawn end to end; an annotated real loss curve.
- **Candidate sources:** Brown et al. 2020 (training details); Touvron et al. 2023 (LLaMA); published model cards and data statements.
- **Depends on:** `toolkit`, `depth`, `tokens`, `anatomy`, `scale`
- **Status:** drafted

#### 17. Generating text {#generation}

- **Goal:** What happens when you press enter: inference, one token at a time. (~14 pp)
- **Concepts:** autoregressive generation; logits to probabilities; greedy decoding, temperature, top-k, top-p; why the same prompt gives different answers; stop conditions; the context window as working memory; caching earlier computation; hallucination as a predictable property of sampling from a language model.
- **History:** beam search and its decline for open-ended text; nucleus sampling (Holtzman et al., 2019).
- **Key figure:** one next-token distribution reshaped by three temperature settings, with computed numbers.
- **Candidate sources:** Holtzman et al. 2019; Radford et al. 2019.
- **Depends on:** `anatomy`, `training`
- **Status:** drafted

### Part VI - From LLM to assistant

#### 18. Teaching models to follow instructions (2017-2023) {#instructions}

- **Goal:** How a text-completion engine becomes a chat assistant. (~16 pp)
- **Concepts:** base model vs instruction-tuned model; supervised fine-tuning on demonstrations; chat format, roles, and the system prompt as plain tokens; reinforcement learning from human feedback (reward model, policy update) by intuition; preference-based alternatives; safety training and refusals; alignment as an open problem.
- **History:** learning from human preferences (Christiano et al., 2017); InstructGPT (2022); ChatGPT (November 2022); Constitutional AI (2022); direct preference optimization (2023).
- **Key figure:** the same prompt completed by a base model and by an instruction-tuned one.
- **Candidate sources:** Christiano et al. 2017; Ouyang et al. 2022; Bai et al. 2022; Rafailov et al. 2023.
- **Depends on:** `pretraining`, `generation`
- **Status:** outlined

#### 19. Prompting and context {#prompting}

- **Goal:** Why the input text matters so much, explained from mechanism rather than folklore. (~14 pp)
- **Concepts:** zero-shot and few-shot prompts; in-context learning revisited; chain-of-thought; structured output; the context window as the only short-term memory; context management; prompt injection; what prompting cannot fix.
- **History:** few-shot prompting in GPT-3 (2020); chain-of-thought (2022).
- **Candidate sources:** Brown et al. 2020; Wei et al. 2022; Kojima et al. 2022.
- **Depends on:** `generation`, `instructions`
- **Status:** outlined

#### 20. Adapting a model: fine-tuning and LoRA {#adapting}

- **Goal:** How to change a model's behavior without training one from scratch, and when that is the right tool. (~14 pp)
- **Concepts:** full fine-tuning; catastrophic forgetting; parameter-efficient methods; adapters; LoRA as a small low-rank correction to frozen weights; QLoRA; distillation; choosing between prompting, retrieval, and fine-tuning.
- **History:** adapters (2019); LoRA (2021); QLoRA (2023); knowledge distillation (2015).
- **Bridge:** low-rank approximation is the same idea as truncated SVD or PCA.
- **Key figure:** a frozen weight matrix plus a thin low-rank update, with parameter counts.
- **Candidate sources:** Houlsby et al. 2019; Hu et al. 2021; Dettmers et al. 2023; Hinton, Vinyals, Dean 2015.
- **Depends on:** `pretraining`, `training`
- **Status:** outlined

#### 21. Giving models knowledge and tools {#tools}

- **Goal:** How systems get around what the weights do not know and cannot do. (~14 pp)
- **Concepts:** knowledge cutoff; retrieval-augmented generation; embedding models and vector search; chunking; grounding and citations; tool (function) calling as structured text the surrounding program acts on; the loop that turns a model into an agent (introduced here, surveyed in `frontier`).
- **History:** RAG (Lewis et al., 2020); dense retrieval (2020); ReAct (2022); tool use in deployed assistants (2023 onward).
- **Bridge:** retrieval is classical information retrieval with learned vectors in place of keyword scores.
- **Key figure:** a RAG request traced from question to retrieved passages to answer.
- **Candidate sources:** Lewis et al. 2020; Karpukhin et al. 2020; Yao et al. 2022.
- **Depends on:** `embeddings`, `generation`, `prompting`
- **Status:** outlined

### Part VII - The working landscape

#### 22. The transformer since 2017 {#since-2017}

- **Goal:** Reconcile the 2017 design with what current models use, so that a modern architecture description reads as familiar. (~12 pp)
- **Concepts:** pre-normalization and RMSNorm; rotary and relative position schemes; newer activations in the feed-forward network; grouped-query attention; faster attention implementations; longer context windows; mixture-of-experts. Each as "what problem, what change", no more.
- **Candidate sources:** Su et al. 2021 (rotary positions); Zhang and Sennrich 2019 (RMSNorm); Dao et al. 2022 (FlashAttention); Touvron et al. 2023.
- **Depends on:** `anatomy`
- **Status:** outlined

#### 23. Small models and local inference {#local}

- **Goal:** The knowledge needed to choose a model that will run on one's own machine and to read its name and file. Hands-on use is in Book 2. (~14 pp)
- **Concepts:** open-weight vs closed models; licenses; reading a model name (size, variant, quantization); memory arithmetic (parameters times bits); quantization by intuition; model file formats; local runtimes; CPU vs GPU; throughput in tokens per second; what small models are and are not good at.
- **History:** the open-weight lineage from 2023 onward; the Hugging Face hub; llama.cpp.
- **Key figure:** a table mapping model size and quantization level to memory needed, computed.
- **Candidate sources:** project documentation and model cards (fetched at research time, date-stamped).
- **Depends on:** `training`, `generation`, `adapting`
- **Status:** outlined

#### 24. Measuring models {#evaluation}

- **Goal:** Enough evaluation vocabulary to read a model card or a leaderboard with appropriate skepticism. Short chapter, kept provisionally [D-011]. (~10 pp)
- **Concepts:** perplexity revisited; benchmarks and what they measure; held-out data and contamination; human preference rankings; saturation; why a benchmark score is not a capability guarantee.
- **History:** GLUE (2018); MMLU (2020); the cycle of benchmark creation and saturation.
- **Bridge:** train/test leakage, a familiar sin, at internet scale.
- **Candidate sources:** Wang et al. 2018; Hendrycks et al. 2020.
- **Depends on:** `prediction`, `scale`
- **Status:** outlined

#### 25. The frontier (as of the book's date) {#frontier}

- **Goal:** A dated survey so the reader can place current headlines. Explicitly the chapter that ages fastest. (~14 pp)
- **Concepts:** reasoning models and test-time computation; agents and long-running tasks; multimodal models (images, audio) in outline; interpretability in outline; open problems (reliability, evaluation, cost, safety).
- **Candidate sources:** gathered at research time; every claim carries an as-of date.
- **Depends on:** `instructions`, `prompting`, `tools`
- **Status:** outlined

### Appendices

#### A. Notation and math refresher {#notation}

- **Goal:** Vectors, matrices, dot products, logarithms, probability distributions, softmax. Only what the chapters use. (~8 pp)
- **Depends on:** none
- **Status:** outlined

#### B. Glossary {#glossary}

- **Goal:** Every term defined in the book, with the chapter of first use. (~12 pp)
- **Depends on:** none
- **Status:** outlined

#### C. Timeline {#timeline}

- **Goal:** A chronology of the events in the book, with citations. (~4 pp)
- **Depends on:** none
- **Status:** outlined

#### D. Further reading {#further-reading}

- **Goal:** An annotated reading list; how to read an ML paper and a model card; a pointer to Book 2. (~4 pp)
- **Depends on:** none
- **Status:** outlined

## Book 2 - Building and running

Hands-on, a bit deeper and more technical than Book 1, not exhaustive [D-001]. Chapter titles and one-line goals only for now, so Book 1 can point forward. Detail is added when Book 2 is started. Framework, hardware target, and length are parked questions in `DECISIONS.md`.

Three stages: build a tiny GPT and train it once [D-006]; run a real open-weight model with llama.cpp; study how a harness drives a model, using Tau [D-007].

### Stage 1 - Build

#### 1. Setting up {#b2-setup}

- **Goal:** The tools, the pinned versions, what hardware is needed, and how the book's code is organized.
- **Builds on:** `local`
- **Depends on:** none
- **Status:** outlined

#### 2. Text to tokens {#b2-tokenizer}

- **Goal:** Write a small byte-pair-encoding tokenizer and compare it with a real one.
- **Builds on:** `tokens`
- **Depends on:** `b2-setup`
- **Status:** outlined

#### 3. A network that learns {#b2-learning}

- **Goal:** Tensors, automatic differentiation, and a training loop on a tiny network, so the mechanics are familiar before the transformer.
- **Builds on:** `backprop`, `toolkit`, `depth`
- **Depends on:** `b2-setup`
- **Status:** outlined

#### 4. Attention in code {#b2-attention}

- **Goal:** Implement one attention head, then multi-head attention with causal masking, checking shapes and numbers at each step.
- **Builds on:** `attention`
- **Depends on:** `b2-learning`
- **Status:** outlined

#### 5. A tiny GPT {#b2-gpt}

- **Goal:** Assemble embeddings, blocks, and the output layer into a complete small model and count its parameters.
- **Builds on:** `anatomy`
- **Depends on:** `b2-tokenizer`, `b2-attention`
- **Status:** outlined

#### 6. Training it, once {#b2-train}

- **Goal:** One short training run on a small corpus: watch the loss fall and the samples improve, then generate text. For understanding, not for use [D-006].
- **Builds on:** `training`, `generation`
- **Depends on:** `b2-gpt`
- **Status:** outlined

### Stage 2 - Run

#### 7. A real model on your machine {#b2-llamacpp}

- **Goal:** Install llama.cpp, choose and download an open-weight model, and understand the file, the quantization level, and the memory it needs.
- **Builds on:** `local`, `since-2017`
- **Depends on:** `b2-setup`
- **Status:** outlined

#### 8. Talking to the model {#b2-chat}

- **Goal:** Sampling settings, chat templates, the system prompt, and the local server API, each tied back to the mechanism behind it.
- **Builds on:** `generation`, `instructions`, `prompting`
- **Depends on:** `b2-llamacpp`
- **Status:** outlined

#### 9. Retrieval {#b2-retrieval}

- **Goal:** A minimal retrieval-augmented setup over a small set of documents with a local embedding model.
- **Builds on:** `embeddings`, `tools`
- **Depends on:** `b2-chat`
- **Status:** outlined

### Stage 3 - Harness

#### 10. Tool calling and the agent loop by hand {#b2-agent-loop}

- **Goal:** Write the smallest possible loop: the model requests a tool, the program runs it, the result goes back in.
- **Builds on:** `tools`
- **Depends on:** `b2-chat`
- **Status:** outlined

#### 11. Reading a real harness: Tau {#b2-tau}

- **Goal:** Run Tau against the local model and read its layers (provider, agent loop, frontend) to see what a production-shaped harness adds to the hand-written loop [D-007].
- **Builds on:** `tools`, `frontier`
- **Depends on:** `b2-agent-loop`
- **Status:** outlined
