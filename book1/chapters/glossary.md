# Glossary {#glossary}

<!-- D-010: chapters linked by ID. D-019, D-020: terminology. -->

This glossary lists the terms the book defines, each with a short definition and the chapter where it is first defined, where the full explanation is. Abbreviations point to their full forms, and a term with more than one meaning in the book has each meaning numbered, with its own chapter.

### A

acceptable use policy
:   A list of forbidden uses that a model license incorporates, as Meta's Llama 2 license does. ([Small models and local inference](#local))

acoustic model
:   In speech recognition, the probability of the sounds given the words. Bayes' rule combines it with a language model, the probability of the words themselves. ([Language as prediction (1948-2000)](#prediction))

action
:   In ReAct, a command the model writes for the program to carry out. ([Giving models knowledge and tools](#tools))

activation function
:   The function a neuron applies to its weighted sum to decide its output, such as the step function or the sigmoid. ([The artificial neuron (1943-1969)](#neuron))

active parameter count
:   In a mixture of experts, the parameters used for one token, as opposed to the total parameter count, all the parameters stored. Also called the active parameters. ([The transformer since 2017](#since-2017))

active parameters
:   See *active parameter count*.

ADALINE
:   Widrow and Hoff's "adaptive linear" neuron of 1960, "about the size of a lunch pail", whose training rule was a special case of stochastic gradient descent. ([The artificial neuron (1943-1969)](#neuron))

Adam
:   An optimizer (2015; "adaptive moment estimation") that keeps running averages of each weight's gradients (the momentum part) and of their squares (the RMSProp part) and divides one by the square root of the other, so each weight gets its own step size. ([The training loop (1951-2017)](#toolkit))

AdamW
:   Adam with weight decay applied separately from the gradient step; the optimizer of the book's language-model recipe. ([The training loop (1951-2017)](#toolkit))

adapters
:   Small extra layers inserted into each block of a pretrained transformer and trained while the original weights stay frozen. ([Adapting a model: fine-tuning and LoRA](#adapting))

add-one smoothing
:   Smoothing that adds one to every count before dividing, like the Laplace correction of naive Bayes. It takes too much probability from frequent events. ([Language as prediction (1948-2000)](#prediction))

advantage
:   In GRPO, how much better one answer did than its siblings: its reward minus the group's average, divided by the group's standard deviation. ([The frontier (as of the book's date)](#frontier))

agent
:   A system in which a model chooses actions in a loop, asking for a tool, reading the result, and asking for another until the task is done, while a program carries the actions out. (In reinforcement learning, the agent is whatever acts and receives rewards.) ([Giving models knowledge and tools](#tools))

agent harness
:   The program that runs an agent's loop: it sends the task, executes the tool calls, and feeds back the results. Also called a scaffold. ([The frontier (as of the book's date)](#frontier))

ALiBi (attention with linear biases)
:   A position method (2022) that adds no position vectors: after each query-key score it adds a fixed penalty proportional to the distance, with a slope per head fixed before training. ([The transformer since 2017](#since-2017))

alignment
:   Making a model's behavior match what its users intend. (In translation, alignment means which source words an output word corresponds to; see soft alignment.) ([Teaching models to follow instructions (2017-2023)](#instructions))

alignment tax
:   A loss of performance on some tasks that comes with alignment training. It is not universal: one lab reported "alignment bonuses" for its larger models. ([Teaching models to follow instructions (2017-2023)](#instructions))

AND
:   The logic function that is true only when both inputs are true; a neuron computes it if it fires only when both inputs are on. ([The artificial neuron (1943-1969)](#neuron))

annotators
:   See *labelers*.

approximate nearest neighbor search
:   Search that finds most of the nearest vectors quickly and may miss a few, used because comparing a question with every stored vector is too slow. ([Giving models knowledge and tools](#tools))

architecture
:   The arrangement of a model's parts, chosen by its designers; it does not change during training. ([The destination: an LLM in one picture](#destination))

Arena score
:   Chatbot Arena's displayed rating: a model's Bradley-Terry strength rescaled (1,000 plus about 174 times the strength) to resemble the Elo rating of chess. ([Measuring models](#evaluation))

artificial neuron
:   A unit that takes several numbers as input and produces one: it multiplies each input by a weight, adds them and a bias, and passes the total through an activation function. ([The artificial neuron (1943-1969)](#neuron))

attention
:   A mechanism by which a network, at each output step, scores a set of input vectors for how well they match what it needs, turns the scores into weights with a softmax, and takes the weighted average. Invented for translation in 2014; the center of the transformer. ([Reading and writing sequences (2010-2016)](#seq2seq))

attention head
:   One set of learned maps that make the queries, keys, and values. A transformer layer runs several heads in parallel. ([Attention without recurrence (2017)](#attention))

autoencoder
:   A network trained to reproduce its input through a narrow middle layer, so that the middle layer becomes a compressed code. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

automatic differentiation
:   A family of techniques, more general than backpropagation, for computing exact derivatives of numeric functions written as computer programs. Backpropagation is a special case of its reverse mode. ([The training loop (1951-2017)](#toolkit))

autoregressive
:   Generating text one token at a time, with each new token fed back as input for the next. ([The destination: an LLM in one picture](#destination))

### B

back-off
:   Smoothing that uses the longer context when it has been seen and backs off to a shorter one otherwise. ([Language as prediction (1948-2000)](#prediction))

backpropagation
:   The method that trains networks with hidden layers: a forward pass computes every unit's value, a backward pass uses the chain rule to pass blame for the error from the output back to every weight, and gradient descent updates the weights. ([Learning in layers (1970-1989)](#backprop))

backpropagation through time
:   Backpropagation applied to an unrolled recurrent network: activations are stored going forward in time, and the backward phase runs backward in time. ([Networks with structure, and the second winter (1980-2005)](#structure))

backward pass
:   The part of backpropagation that starts at the output and passes each unit's share of the blame back through the network. ([Learning in layers (1970-1989)](#backprop))

base frequency
:   In rotary position embeddings, the constant (10,000 in the original formula) that sets how scores behave at large distances; later models changed it. ([The transformer since 2017](#since-2017))

baseline
:   A reference score to beat: a simple model, random guessing, or people. ([Measuring models](#evaluation))

base model
:   The result of pretraining alone: a model that continues text and has not been trained to follow instructions. ([The destination: an LLM in one picture](#destination))

batch normalization
:   Normalizing each unit's values across the examples of a minibatch (subtract the mean, divide by the standard deviation), then applying a learned scale and shift. ([Making deep networks trainable (2010-2016)](#depth))

batch size
:   The number of examples in a minibatch. ([The training loop (1951-2017)](#toolkit))

beam search
:   Decoding that keeps the few best partial outputs at each step, instead of only the single most probable next token, and returns the most probable whole sequence it finds. ([Reading and writing sequences (2010-2016)](#seq2seq))

benchmark
:   A fixed, shared test set with a scoring rule, usually with a public leaderboard. ImageNet's yearly challenge added a hidden test set and a deadline. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

best-of-N
:   Generating N answers and keeping the one that a verifier rates highest. ([The frontier (as of the book's date)](#frontier))

bfloat16
:   A 16-bit number format that keeps the range of 32-bit numbers (up to about $3 \times 10^{38}$) by giving up precision: the spacing near 1 is about 0.008. ([How an LLM is trained](#training))

bias
:   The extra number a neuron adds to its weighted sum; it sets how easily the neuron fires regardless of its inputs. ([The artificial neuron (1943-1969)](#neuron))

bidirectional
:   Of a recurrent encoder: one network reads the sentence left to right, another right to left, and each word's vector joins the two. ([Reading and writing sequences (2010-2016)](#seq2seq))

bi-encoder
:   A retrieval setup with separate encoders for question and passage, so passage vectors can be computed in advance and compared quickly. Less accurate than a cross-encoder. ([Giving models knowledge and tools](#tools))

BIG-bench
:   A collection of 204 benchmark tasks from 450 authors. ([Measuring models](#evaluation))

bigram
:   An n-gram of two consecutive symbols. ([Language as prediction (1948-2000)](#prediction))

binary grading
:   Scoring 1 for a right answer and 0 for anything else, including "I don't know". Under it, guessing when unsure maximizes the expected score. ([Measuring models](#evaluation))

bit
:   The unit of uncertainty: a fair coin's outcome carries 1 bit. ([Language as prediction (1948-2000)](#prediction))

bits per byte
:   A language model's total surprise in bits on a text, divided by the text's length in bytes. ([Measuring models](#evaluation))

bits per weight
:   Everything stored for a quantized model, scales included, divided by the number of weights: the honest measure of a quantization format's size. ([Small models and local inference](#local))

BLEU
:   A translation score (2002) that counts how many of a system's word sequences of one to four words also appear in human reference translations, combines the counts into one number, and penalizes output that is too short. ([Reading and writing sequences (2010-2016)](#seq2seq))

block
:   The repeated unit of a transformer: sub-layers (attention, then a feed-forward network), each adding its output to the residual stream. Papers say "layer" or "block" for the same thing. (In llama.cpp, "block" also names a quantization group.) ([Anatomy of a transformer](#anatomy))

BM25
:   The standard keyword retrieval method: tf-idf plus saturation and length normalization. ([Giving models knowledge and tools](#tools))

BPE
:   See *byte pair encoding*.

Bradley-Terry model
:   A model in which the probability that one item is preferred to another, or beats it, is a logistic function of the difference of their scores. It trains reward models and ranks models in Chatbot Arena. ([Teaching models to follow instructions (2017-2023)](#instructions))

byte pair encoding (BPE)
:   A 1994 compression algorithm that replaces common pairs of bytes by single new symbols, adapted in 2015 for tokenization: start from characters, repeatedly merge the most frequent adjacent pair into a new symbol, then cut new text by applying the learned merges. ([Tokens: what the model actually sees (1994-2018)](#tokens))

### C

calibrated
:   A model is calibrated if, of all the answers it gives with 70% confidence, about 70% are right. (Contextual calibration and calibration data use the word in other senses.) ([Generating text](#generation))

calibration data
:   A small sample of text used to tune the rounding of a quantized model rather than to train it. ([Small models and local inference](#local))

canary string
:   A unique random identifier placed in benchmark files so that they can be filtered out of training data. ([Measuring models](#evaluation))

capability threshold
:   In a frontier safety framework, a named level of capability; crossing it calls for stronger safeguards before release. ([The frontier (as of the book's date)](#frontier))

catastrophic forgetting
:   The loss of what a network learned earlier when it is trained on new data, because every fact is stored across the same shared weights. First called catastrophic interference. ([Adapting a model: fine-tuning and LoRA](#adapting))

causal mask
:   In attention, setting every score from a position to a later position to minus infinity before the softmax, so each token sees only itself and earlier tokens. It lets one training pass make an honest prediction at every position. ([Anatomy of a transformer](#anatomy))

CBOW
:   See *continuous bag of words*.

chain of command
:   In OpenAI's Model Spec, a ranking of authorities whose instructions a model follows; quoted text, attachments, and tool outputs get no authority by default. ([Prompting and context](#prompting))

chain of thought
:   A series of intermediate reasoning steps that a model writes before its answer. ([Prompting and context](#prompting))

chain-of-thought prompting
:   Few-shot prompting in which each demonstration includes a chain of thought. ([Prompting and context](#prompting))

Chatbot Arena
:   A site, running since April 2023, that collects people's votes between the answers of two models and ranks the models with a Bradley-Terry model. ([Measuring models](#evaluation))

chat format
:   A layout of a conversation as one sequence of tokens, with markers saying who speaks. Also called a chat template. ([Teaching models to follow instructions (2017-2023)](#instructions))

chat product
:   A model plus the software around it: the interface, instructions from the provider that the user does not see, rules about what to display, and possibly tools. ([The destination: an LLM in one picture](#destination))

chat template
:   See *chat format*.

checkpoint
:   A saved copy of the weights and optimizer state, written regularly so that a training run can resume after a crash. ([How an LLM is trained](#training))

chunk
:   A piece of a document prepared for retrieval. Cutting documents into chunks is chunking. ([Giving models knowledge and tools](#tools))

chunking
:   See *chunk*.

citation
:   In a generated answer, a pointer from a statement to a passage that supports it. ([Giving models knowledge and tools](#tools))

citation precision
:   Whether any of an answer's citations are irrelevant. ([Giving models knowledge and tools](#tools))

citation recall
:   Whether each statement of an answer is supported by the passages it cites. ([Giving models knowledge and tools](#tools))

clean subset
:   A version of a benchmark with the examples that may have leaked into training data removed. ([Measuring models](#evaluation))

client
:   In the Model Context Protocol, the connector inside the host application. ([Giving models knowledge and tools](#tools))

closed-book
:   Of a model: answering from its parameters alone, without looking anything up. ([Giving models knowledge and tools](#tools))

closed model
:   A model whose weights are not released; it is reached only through its maker's service, and its weights never leave the vendor's computers. ([Adapting a model: fine-tuning and LoRA](#adapting))

collocation
:   The words a word habitually appears next to. ([Words as vectors (1954-2014)](#embeddings))

common token bias
:   In few-shot prompting, a model's tendency to favor answers that are frequent in its training data. ([Prompting and context](#prompting))

compaction
:   Context management that replaces the older turns of a conversation with a summary or a compressed item. ([Prompting and context](#prompting))

compute
:   The total arithmetic done in training, counted in FLOPs. ([Scale (2019-2022)](#scale))

compute-optimal
:   Of training: getting the lowest loss a fixed computing budget can buy. Hoffmann and colleagues (Chinchilla, 2022) found that model size and training tokens should then grow equally. ([Scale (2019-2022)](#scale))

computer use
:   An agent loop with a screen as input: the model sees screenshots and acts through the mouse and keyboard. ([The frontier (as of the book's date)](#frontier))

conditional computation
:   Running only parts of a network for each example, which promises more capacity without a proportional increase in computation. ([The transformer since 2017](#since-2017))

confidence interval
:   A range around a score; a 95% interval is about 1.96 standard errors either side. ([Measuring models](#evaluation))

connectedness
:   The problem of deciding whether a figure is in one piece; Minsky and Papert analyzed what single-layer perceptrons can compute about it. ([The artificial neuron (1943-1969)](#neuron))

Constitutional AI
:   A method (2022) that replaces human labels for harmlessness with a model's judgments guided by a written list of principles. A model criticizes and rewrites its own answers and is fine-tuned on the revisions; then a model's comparisons train a reward model for RLAIF. ([Teaching models to follow instructions (2017-2023)](#instructions))

constrained decoding
:   Generation in which, at each step, every token that could not continue a valid output gets probability zero, so the output follows a grammar. Vendors also say constrained sampling. ([Prompting and context](#prompting))

contamination
:   Test data appearing in training data. Also called data contamination or test-set leakage. ([Measuring models](#evaluation))

context editing
:   Context management that clears old material, such as tool results, from the window. ([Prompting and context](#prompting))

context extension
:   Extra training to lengthen a model's context window. ([The transformer since 2017](#since-2017))

context-free grammar
:   A grammar that allows nesting, such as records inside records. ([Prompting and context](#prompting))

context management
:   Deciding what goes into the context window on each call, since the model keeps nothing between calls. ([Prompting and context](#prompting))

context rot
:   A vendor and practitioner term for accuracy and recall degrading as the context grows; not a measurement. ([Prompting and context](#prompting))

contextual calibration
:   Measuring a model's bias on a content-free input and rescaling its output probabilities so that input comes out even, then applying the same rescaling to real inputs. ([Prompting and context](#prompting))

contextual embedding
:   A vector for a token that depends on the words around it. ([Attention without recurrence (2017)](#attention))

context window
:   The largest number of tokens a model can take as input at once; in GPT-2, the 1,024 rows of the position table. It is the model's whole working memory while it generates. ([The destination: an LLM in one picture](#destination))

continuous bag of words (CBOW)
:   The word2vec method that predicts a word from the average of its neighbors' vectors; the partner of skip-gram. ([Words as vectors (1954-2014)](#embeddings))

contrastive training
:   Training two encoders so that the vectors of true pairs (an image and its caption) get high cosine similarity and those of every wrong pairing in the batch get low similarity. ([The frontier (as of the book's date)](#frontier))

convex
:   Of a problem: every local minimum is also the global minimum, so gradient descent is guaranteed to find the best weights. ([Networks with structure, and the second winter (1980-2005)](#structure))

convolution
:   Sliding a filter along the input. ([Networks with structure, and the second winter (1980-2005)](#structure))

convolutional network
:   A network built from layers that slide small shared filters across positions in an image or signal. ([Networks with structure, and the second winter (1980-2005)](#structure))

cosine
:   The cosine of the angle between two vectors: 1 if they point the same way, 0 if perpendicular, -1 if opposite. The standard measure of similarity between embeddings. ([Words as vectors (1954-2014)](#embeddings))

credit assignment problem
:   Which part of a system deserves credit or blame for its success or failure; for a layered network, how much each inner weight should change when the output is wrong. ([Learning in layers (1970-1989)](#backprop))

cross-attention
:   Attention from a transformer's decoder to the encoder's output. ([Anatomy of a transformer](#anatomy))

cross-encoder
:   One model that reads question and passage together: more accurate than a bi-encoder, but nothing can be computed in advance. ([Giving models knowledge and tools](#tools))

cross-entropy
:   A model's average surprise on a text, in bits per word (or token); the standard loss for language models. ([Language as prediction (1948-2000)](#prediction))

curse of dimensionality
:   The number of possible configurations of a set of variables grows exponentially with the number of variables. ([Language as prediction (1948-2000)](#prediction))

### D

data augmentation
:   Creating extra training examples by altering the originals, as by cropping and mirroring images. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

decision boundary
:   The line where a neuron's output switches from 0 to 1. ([The artificial neuron (1943-1969)](#neuron))

decode
:   The second phase of producing a reply: writing it one token per forward pass. It is limited by memory traffic more than arithmetic. ([Generating text](#generation))

decoder
:   The network that writes the output sequence in an encoder-decoder model. ([Reading and writing sequences (2010-2016)](#seq2seq))

decoder-only
:   Of a transformer: no encoder, and blocks with only masked self-attention and a feed-forward network, using the causal mask throughout (GPT, Llama). ([Anatomy of a transformer](#anatomy))

decoding strategy
:   The rule that turns each set of next-token probabilities into a choice. ([Generating text](#generation))

deduplication
:   Finding and removing repeated copies in training data, as exact repeated strings or near-duplicate documents. ([How an LLM is trained](#training))

deep
:   Of a network: having many layers. ([Networks with structure, and the second winter (1980-2005)](#structure))

demonstration
:   \(1) In instruction tuning, the response a labeler wrote for a prompt, as the answer the model should give ([Teaching models to follow instructions (2017-2023)](#instructions)). (2) In a prompt, one worked example, such as a sentence followed by its label; also called an exemplar ([Prompting and context](#prompting)).

dense
:   Of a network: every parameter is used for every token. (A dense vector is a different idea; dense retrieval uses dense vectors.) ([The transformer since 2017](#since-2017))

dense passage retrieval (DPR)
:   A trained retriever (2020) in which two BERT models turn a question and a passage into vectors, and a passage is scored by the dot product of the two. ([Giving models knowledge and tools](#tools))

dense vector
:   A short list of numbers in which every number carries some information and similar items get similar lists. ([Words as vectors (1954-2014)](#embeddings))

directed generation
:   Generation where the output is a constrained transformation of the input, as in translation or summarization. ([Generating text](#generation))

direct preference optimization (DPO)
:   A method (2023) that trains on preference pairs with a classification loss, raising the probability of the preferred answer and lowering the rejected one relative to a frozen reference model, with no separate reward model and no sampling during training. ([Teaching models to follow instructions (2017-2023)](#instructions))

distillation
:   See *knowledge distillation*.

distributed
:   Of a representation: each item's code is spread across several units, each standing for a feature, rather than held in a single unit. ([Words as vectors (1954-2014)](#embeddings))

distributional hypothesis
:   Words that occur in similar contexts tend to have similar meanings. ([Words as vectors (1954-2014)](#embeddings))

document
:   In information retrieval, whatever unit of text the system indexes and retrieves. ([Giving models knowledge and tools](#tools))

DPO
:   See *direct preference optimization*.

DPR
:   See *dense passage retrieval*.

dropout
:   During training, setting each unit's output to zero at random (with probability 0.5 in the original papers), so that no unit can rely on others being present. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

### E

early stopping
:   Keeping a copy of the weights whenever the validation loss improves and returning the best copy at the end. ([The training loop (1951-2017)](#toolkit))

effective context length
:   The longest input length at which a model stays above a fixed score on a test. ([Prompting and context](#prompting))

effective cutoff
:   The date a model's knowledge actually reflects, which can differ greatly from its reported knowledge cutoff. ([Giving models knowledge and tools](#tools))

Elo rating
:   The rating system of chess, which Chatbot Arena first used and its Arena score is scaled to resemble. ([Measuring models](#evaluation))

embedding
:   A token's vector, one row of the embedding table; more generally, a learned vector representing a word or other item (see word embedding). This book keeps the word for these rows and not for the vectors between layers, which form the residual stream. ([The destination: an LLM in one picture](#destination))

embedding model
:   A model that turns a text into one vector, trained so that closeness means relevance. ([Giving models knowledge and tools](#tools))

embedding table
:   The large table of a language model whose rows are the tokens' vectors; each token ID selects one row. Also called the token table. ([The destination: an LLM in one picture](#destination))

emergent ability
:   An ability not present in smaller models but present in larger ones, so not predictable by extrapolating smaller models' performance. Whether such jumps reflect the models or the strictness of the scoring is disputed. ([Scale (2019-2022)](#scale))

encoder
:   The network that reads the input sequence in an encoder-decoder model. ([Reading and writing sequences (2010-2016)](#seq2seq))

encoder-decoder
:   A model with both an encoder and a decoder. In a transformer: a fully visible encoder for the input, a causal decoder for the output, and cross-attention between them (the 2017 transformer, T5). ([Anatomy of a transformer](#anatomy))

encoder-only
:   Of a transformer: one stack with a fully visible mask, so every token sees the whole input (BERT). ([Anatomy of a transformer](#anatomy))

ensemble
:   Several models whose predictions are combined. ([Reading and writing sequences (2010-2016)](#seq2seq))

entropy
:   The uncertainty of an outcome, measured in bits. ([Language as prediction (1948-2000)](#prediction))

epoch
:   One pass through all the training examples. ([The artificial neuron (1943-1969)](#neuron))

evaluation awareness
:   A model's ability to tell test settings from real deployment, which can make test results a poor guide to its behavior. ([The frontier (as of the book's date)](#frontier))

exact attention
:   Attention whose output is mathematically the same as the standard method's, unlike approximations; FlashAttention computes it. ([The transformer since 2017](#since-2017))

exemplar
:   See *demonstration*.

experts
:   In a mixture of experts, the several sub-networks among which a router chooses for each input; in a transformer, they replace the feed-forward sub-layer. ([The transformer since 2017](#since-2017))

exploding gradient
:   The backward signal growing as it is multiplied by factors above 1 at each step, until one update throws the weights far away. ([Networks with structure, and the second winter (1980-2005)](#structure))

exposure bias
:   In training a model always predicts from real text, but in generation from its own output, so it continues its own earlier mistakes fluently. ([Generating text](#generation))

extrapolation
:   A model's ability to keep performing well on inputs longer than those it was trained on. ([The transformer since 2017](#since-2017))

### F

FAISS
:   An open-source library for similarity search and clustering of dense vectors. ([Giving models knowledge and tools](#tools))

faithful
:   Of an explanation: accurately representing the reasons behind the model's prediction. ([Prompting and context](#prompting))

false refusal
:   Declining a request that should have been answered. ([Teaching models to follow instructions (2017-2023)](#instructions))

feature
:   In interpretability, a direction in a layer's vectors that corresponds to something recognizable. (In the 2000s sense, an input measurement; see feature engineering.) ([The frontier (as of the book's date)](#frontier))

feature engineering
:   Choosing by hand what to measure about the data, so that the learning algorithm only weighs the measurements. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

feature map
:   The sequence of a filter's outputs: a record of where the filter's pattern occurs. ([Networks with structure, and the second winter (1980-2005)](#structure))

feed-forward network
:   The second sub-layer of a transformer block: a small multilayer perceptron with one hidden layer, applied to each position on its own. ([Anatomy of a transformer](#anatomy))

few-shot
:   Of a prompt: a description of the task plus several examples. ([Scale (2019-2022)](#scale))

filter
:   The small set of weights that a convolution slides along its input. ([Networks with structure, and the second winter (1980-2005)](#structure))

fine-tuning
:   \(1) In the 2006 deep belief networks, the step after layer-by-layer pretraining in which all the weights were adjusted together ([The turn: data, compute, and depth (2006-2012)](#deep-turn)). (2) In the wider, later sense, adjusting a pretrained network's weights on a new task ([Pretraining: learn language first, tasks later (2015-2019)](#pretraining)).

FlashAttention
:   An IO-aware way (2022) to compute exact attention by tiling, avoiding reading and writing the full attention matrix to and from main memory. ([The transformer since 2017](#since-2017))

floating-point operations (FLOPs)
:   The unit for counting compute: each multiplication or addition counts as one. ([Attention without recurrence (2017)](#attention))

FLOPs
:   See *floating-point operations*.

forget gate
:   An LSTM gate that lets the network learn when to clear its memory, by multiplying the stored value by something less than 1. ([Networks with structure, and the second winter (1980-2005)](#structure))

forward pass
:   Running a network on an input from the inputs to the output, recording every unit's value along the way. ([Learning in layers (1970-1989)](#backprop))

framework
:   Software that provides tensors on GPUs together with automatic differentiation, such as Theano, Torch, TensorFlow, or PyTorch. ([The training loop (1951-2017)](#toolkit))

frontier safety framework
:   A developer's if-then policy: if testing shows a model has crossed a named capability threshold, stronger safeguards come before release. ([The frontier (as of the book's date)](#frontier))

full fine-tuning
:   Continuing to train every parameter of a pretrained model on new data. ([Adapting a model: fine-tuning and LoRA](#adapting))

fully connected
:   Of a layer: every unit receives every input. ([Networks with structure, and the second winter (1980-2005)](#structure))

functional correctness
:   The criterion that a generated program counts as right if it passes its unit tests. ([Measuring models](#evaluation))

### G

gate
:   A learned switch that sets how much of a signal passes, by multiplying it by a value between 0 and 1, as in the LSTM and the gated linear unit. ([Networks with structure, and the second winter (1980-2005)](#structure))

gated
:   Of a model on Hugging Face: its files can be downloaded only after an access request, which shares the user's username and email address with the model's authors. ([Small models and local inference](#local))

gated linear unit
:   A feed-forward layer whose hidden layer is the component-wise product of two linear projections, one of them first passed through a sigmoid. ([The transformer since 2017](#since-2017))

gated recurrent unit (GRU)
:   A recurrent unit with an update gate and a reset gate, simpler than the LSTM. ([Reading and writing sequences (2010-2016)](#seq2seq))

Gaussian Error Linear Unit (GELU)
:   An activation function, a variant of ReLU, used in the feed-forward networks of GPT and GPT-2. ([The transformer since 2017](#since-2017))

GELU
:   See *Gaussian Error Linear Unit*.

generalized delta rule
:   The name the 1986 Parallel Distributed Processing volumes gave to backpropagation. ([Learning in layers (1970-1989)](#backprop))

GGUF
:   The model file format of runtimes built on llama.cpp, introduced on August 21, 2023. ([Small models and local inference](#local))

GLUE
:   A benchmark (2018) of nine sentence or sentence-pair language-understanding tasks, with an online leaderboard based mainly on private test data. ([Measuring models](#evaluation))

goal hijacking
:   A prompt injection attack that makes a model do something else, such as print an attacker's phrase. ([Prompting and context](#prompting))

Goodhart's law
:   Usually paraphrased as "when a measure becomes a target, it ceases to be a good measure". ([Measuring models](#evaluation))

GPQA
:   A benchmark (2023) of 448 multiple-choice questions in biology, physics, and chemistry, built to be hard even for people who could search. ([Measuring models](#evaluation))

GPU
:   See *graphics processing unit*.

gradient
:   The list of the loss's derivatives, one per weight. ([Learning in layers (1970-1989)](#backprop))

gradient clipping
:   If the gradient, viewed as one long vector, is longer than a threshold, shrinking it to the threshold while keeping its direction; a guard against exploding gradients. ([The training loop (1951-2017)](#toolkit))

gradient descent
:   Repeatedly taking a step downhill on the loss, of a size proportional to the gradient and set by the learning rate. ([Learning in layers (1970-1989)](#backprop))

grammar
:   A set of rules defining which strings are valid. ([Prompting and context](#prompting))

graphics processing unit (GPU)
:   A chip built for graphics, with many simple processing cores and high memory bandwidth, which suits the matrix arithmetic of neural networks. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

greedy decoding
:   Always taking the most probable next token. ([Generating text](#generation))

grounded
:   Of an answer: based on facts from a curated collection, with the passage it came from available to the user. ([Giving models knowledge and tools](#tools))

group
:   In quantization, a set of weights that share one scale. llama.cpp calls it a block. ([Small models and local inference](#local))

grouped-query attention
:   Attention in which query heads are divided into groups, each sharing a single key head and value head; it shrinks the KV cache. ([The transformer since 2017](#since-2017))

Group Relative Policy Optimization (GRPO)
:   The reinforcement learning algorithm of DeepSeek-R1: for each question the model generates a group of answers, and each answer's reward is standardized within its group to give its advantage. ([The frontier (as of the book's date)](#frontier))

GRPO
:   See *Group Relative Policy Optimization*.

GRU
:   See *gated recurrent unit*.

GSM1k
:   1,205 problems in the style of GSM8K, written by people in 2024 without help from any LLM and kept private: a fresh test set for detecting overfitting to GSM8K. ([Measuring models](#evaluation))

GSM8K
:   A benchmark (2021) of about 8,500 grade-school math word problems that take between 2 and 8 steps to solve. ([Measuring models](#evaluation))

### H

hallucination
:   Generated content that is nonsensical or unfaithful to the provided source; the usual word for a fluent model stating falsehoods. ([Generating text](#generation))

HELM
:   An evaluation (2022) that ran 30 models under the same conditions on 16 core scenarios, measuring seven metrics from accuracy and calibration to fairness and toxicity. ([Measuring models](#evaluation))

hidden layer
:   A set of hidden units side by side. ([Learning in layers (1970-1989)](#backprop))

hidden state
:   In a recurrent network, the summary of everything read so far, combined with each new input. (Other writing also uses the term for the residual stream of a transformer.) ([Networks with structure, and the second winter (1980-2005)](#structure))

hidden unit
:   A neuron that is neither an input nor an output. ([Learning in layers (1970-1989)](#backprop))

hierarchical navigable small world graphs (HNSW)
:   An approximate nearest neighbor method that builds a multi-layer structure of graphs, with few vectors in the top layers and all of them at the bottom, and searches from the top down. ([Giving models knowledge and tools](#tools))

highway networks
:   Networks (2015) that carry the input around each block through a learned gate; a predecessor of residual connections. ([Making deep networks trainable (2010-2016)](#depth))

HLE
:   See *Humanity's Last Exam*.

HNSW
:   See *hierarchical navigable small world graphs*.

host
:   In the Model Context Protocol, the application the user works in. ([Giving models knowledge and tools](#tools))

human baseline
:   The score people achieve on a benchmark. ([Measuring models](#evaluation))

HumanEval
:   A benchmark (2021) of 164 programming problems, each with unit tests. ([Measuring models](#evaluation))

human in the loop
:   A person who approves an action before the program carries it out. ([Giving models knowledge and tools](#tools))

Humanity's Last Exam (HLE)
:   A benchmark (January 2025) whose questions have known, unambiguous, easily verifiable answers but cannot be quickly answered by searching the internet. ([Measuring models](#evaluation))

hybrid search
:   Combining the rankings of keyword search and vector search. ([Giving models knowledge and tools](#tools))

hyperparameter
:   A setting of training chosen by people rather than learned, such as the batch size or the learning rate, usually chosen on a validation set. ([The training loop (1951-2017)](#toolkit))

### I

idf
:   See *inverse document frequency*.

ImageNet
:   A collection of images (2009) organized by the noun categories of WordNet; its yearly challenge was the benchmark on which deep networks won in 2012. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

in-context learning
:   Using the text input of a pretrained language model as the task specification: given an instruction and/or a few demonstrations, the model completes further instances by predicting what comes next. ([Scale (2019-2022)](#scale))

indirect prompt injection
:   Instructions planted in a web page, email, or document that reach a model when an application retrieves that content into its window. ([Prompting and context](#prompting))

induction head
:   An attention head that completes a pattern by copying: having seen token A followed by B, when A appears again it predicts B. ([Prompting and context](#prompting))

inference
:   Using a trained model to produce text. The parameters do not change during inference. ([The destination: an LLM in one picture](#destination))

inference-time compute
:   See *test-time compute*.

information retrieval (IR)
:   The field of retrieving media based on users' information needs; in its basic task, a query returns an ordered set of documents from a collection. ([Giving models knowledge and tools](#tools))

instruction hierarchy
:   Training a model to give instructions different priority by source, so that, for example, a system prompt outranks text from untrusted users and third parties. ([Prompting and context](#prompting))

instruction tuning
:   Fine-tuning language models on a collection of datasets described via instructions. ([Teaching models to follow instructions (2017-2023)](#instructions))

instruct model
:   An instruction-tuned model: one trained further, after pretraining, to follow instructions and converse. ([Small models and local inference](#local))

intrinsic dimension
:   The smallest number of free parameters with which a network, trained in a random subspace of its weights, reaches a set fraction (90% in the example) of its normal performance. ([Adapting a model: fine-tuning and LoRA](#adapting))

inverse document frequency (idf)
:   A word's weight in retrieval, larger the fewer documents contain it (a logarithm of the collection size over the number of documents containing the word). ([Giving models knowledge and tools](#tools))

inverted index
:   A table that, given a query term, gives the list of documents that contain it. ([Giving models knowledge and tools](#tools))

IO-aware
:   Organized around reads and writes of memory rather than arithmetic. ([The transformer since 2017](#since-2017))

IR
:   See *information retrieval*.

iteration
:   See *step*.

### J

jailbreak
:   Getting a model to break its own vendor's safety rules. ([Prompting and context](#prompting))

JSON
:   A plain-text notation for records of named fields, lists, numbers, and strings, used throughout the web. ([Prompting and context](#prompting))

JSON Schema
:   A description of what a valid JSON record must contain: which fields, of which types. ([Prompting and context](#prompting))

### K

key
:   In attention, the vector that says what a token offers to others looking. ([Attention without recurrence (2017)](#attention))

key-value head
:   A set of keys and values used by one or more query heads. ([The transformer since 2017](#since-2017))

KL penalty
:   In RLHF, a charge for making an answer more probable than the starting model did; it keeps the trained model close to that model, like a leash. ([Teaching models to follow instructions (2017-2023)](#instructions))

Kneser-Ney smoothing
:   Smoothing that, when backing off to a single word, asks in how many different contexts the word appears rather than how frequent it is. ([Language as prediction (1948-2000)](#prediction))

knowledge cutoff
:   The date after which a model's training data stops. ([Prompting and context](#prompting))

knowledge distillation
:   Training a different, usually smaller model, the student, to imitate a larger one, the teacher, often on the teacher's probabilities. ([Adapting a model: fine-tuning and LoRA](#adapting))

Kullback-Leibler divergence
:   A measure of how far apart two probability distributions are. ([Teaching models to follow instructions (2017-2023)](#instructions))

KV cache
:   The stored keys and values of every earlier token in every layer, kept during generation so that each is computed once. It grows with every token. ([Generating text](#generation))

### L

labelers
:   People hired to write demonstrations and compare responses for training; other papers say annotators. ([Teaching models to follow instructions (2017-2023)](#instructions))

label space
:   The set of possible answers in a classification task given in a prompt. ([Prompting and context](#prompting))

language model
:   Anything that assigns a probability to a piece of text; equivalently, a probability distribution over the possible next word given the words so far. ([The destination: an LLM in one picture](#destination))

large language model (LLM)
:   A program that reads a piece of text and computes, for every possible next piece of text, the probability that it comes next. "Large" refers to the number of parameters. ([The destination: an LLM in one picture](#destination))

latent concept
:   In one account of in-context learning, the hidden kind of document a model must infer to predict the next word, and which it infers as shared by the examples in a prompt. ([Prompting and context](#prompting))

latent semantic analysis (LSA)
:   A method (1990) that applies the singular-value decomposition, the factorization behind PCA, to a table of how often each word appears in each document; also called latent semantic indexing. ([Words as vectors (1954-2014)](#embeddings))

layer normalization
:   Normalizing with the mean and variance of all the units in a layer for a single example, so it works the same in training and testing and with a batch of one. ([Making deep networks trainable (2010-2016)](#depth))

leaderboard
:   A public ranking of results on a benchmark. ([Measuring models](#evaluation))

learning rate
:   The number that sets the size of the steps in gradient descent. ([Learning in layers (1970-1989)](#backprop))

learning-rate schedule
:   The plan for changing the learning rate during training. ([The training loop (1951-2017)](#toolkit))

length normalization
:   BM25's correction for long documents, which contain more of every word. ([Giving models knowledge and tools](#tools))

license
:   A model maker's terms for who may use the weights, for what, and on what conditions. ([Small models and local inference](#local))

linearly separable
:   Of a task: the examples labeled 1 and those labeled 0 can be separated by one straight cut. ([The artificial neuron (1943-1969)](#neuron))

linear probe
:   A logistic regression trained on a model's internal activations. ([The frontier (as of the book's date)](#frontier))

llama.cpp
:   A program, begun on March 10, 2023, to run Meta's LLaMA model in pure C/C++; other runtimes, such as Ollama, are built on it. ([Small models and local inference](#local))

LLM
:   See *large language model*.

LLM-as-a-judge
:   Using a strong model, instead of human votes, to judge the answers of models. ([Measuring models](#evaluation))

load balancing
:   Keeping the experts of a mixture of experts in roughly equal use, for example with an extra loss term that penalizes unequal use. ([The transformer since 2017](#since-2017))

local minimum
:   A point lower than everything near it but not the lowest point overall. ([Learning in layers (1970-1989)](#backprop))

logits
:   The raw scores a model's output layer computes, one per vocabulary entry, before the softmax turns them into probabilities. ([The destination: an LLM in one picture](#destination))

long short-term memory (LSTM)
:   A recurrent design (1997) in which a memory cell is guarded by learned gates, so it can carry information across long gaps. ([Networks with structure, and the second winter (1980-2005)](#structure))

long-term dependencies
:   Relationships between things far apart in a sequence. ([Networks with structure, and the second winter (1980-2005)](#structure))

LoRA
:   See *low-rank adaptation*.

loss
:   The number that measures how wrong a model's predictions are on the training data; the formula that computes it is the loss function. ([The destination: an LLM in one picture](#destination))

loss curve
:   The loss plotted against training time: the main instrument panel of training. ([The training loop (1951-2017)](#toolkit))

loss function
:   See *loss*.

low-rank adaptation (LoRA)
:   Fine-tuning that freezes a weight matrix and trains only a correction to it, written as the product of two thin matrices of small rank. ([Adapting a model: fine-tuning and LoRA](#adapting))

LSA
:   See *latent semantic analysis*.

LSTM
:   See *long short-term memory*.

### M

majority label bias
:   In few-shot prompting, a model's tendency to favor the answer that appears most often among the examples. ([Prompting and context](#prompting))

majority vote
:   Taking the most common final answer among many sampled answers: the last step of self-consistency ([Prompting and context](#prompting)). [The frontier (as of the book's date)](#frontier) counts it, with best-of-N, among the ways of spending more computation at answer time.

Markov assumption
:   Predicting each word from only the last one or two words, forgetting the rest of the past. ([Language as prediction (1948-2000)](#prediction))

masked language model (MLM)
:   BERT's training task: choose some of the input tokens at random (about 15%), mostly replace them with a mask token, and predict them from the words on both sides. ([Pretraining: learn language first, tasks later (2015-2019)](#pretraining))

MCP
:   See *Model Context Protocol*.

mean squared error
:   The average of the squared differences between predictions and true values. ([Learning in layers (1970-1989)](#backprop))

mechanistic interpretability
:   Research that tries to explain how a trained network computes, as a programmer might reverse engineer a compiled program into readable source code. ([The frontier (as of the book's date)](#frontier))

memory bandwidth
:   The number of bytes per second a machine's memory can deliver to the processor. ([Small models and local inference](#local))

memory cell
:   The stored value of an LSTM, guarded by gates. ([Networks with structure, and the second winter (1980-2005)](#structure))

memory tool
:   A tool that lets a model keep notes in files outside the context window and read them in a later conversation. ([Prompting and context](#prompting))

minibatch
:   A small random sample of the training examples, used to estimate the gradient at each step. ([The training loop (1951-2017)](#toolkit))

mixed precision
:   Training that keeps a 32-bit master copy of the weights to receive the updates and does the bulk of the arithmetic in 16 bits. ([How an LLM is trained](#training))

mixture of experts
:   A model made of several experts plus a router that decides, for each input, which of them to use. ([The transformer since 2017](#since-2017))

MLM
:   See *masked language model*.

MLX
:   Apple's array framework for machine learning on Apple silicon; its companion MLX LM generates text with, fine-tunes, and quantizes models. ([Small models and local inference](#local))

MMLU
:   A broad multiple-choice exam (2020) covering 57 tasks, each question with four choices, so random guessing scores 25%. ([Measuring models](#evaluation))

model card
:   The documentation that comes with a model; as proposed in 2019, a short document giving benchmarked evaluation, intended uses, and how the evaluation was done. ([Small models and local inference](#local))

Model Context Protocol (MCP)
:   An open standard (Anthropic, November 2024) for connecting AI assistants to data and tools, made of hosts, clients, and servers. ([Giving models knowledge and tools](#tools))

model hub
:   A website that hosts model files with their documentation. ([Small models and local inference](#local))

momentum
:   Keeping a running velocity that accumulates past gradients and stepping with it, instead of with the current gradient alone. ([The training loop (1951-2017)](#toolkit))

MT-Bench
:   A set of 80 multi-turn questions (2023) used to compare a strong model's verdicts as a judge with people's. ([Measuring models](#evaluation))

multi-head attention
:   Running several attention heads in parallel, each on its own learned, smaller projections of the queries, keys, and values, and joining their results. ([Attention without recurrence (2017)](#attention))

multimodal
:   Of a model: taking more than one kind of input, such as text and images. ([The frontier (as of the book's date)](#frontier))

multi-query attention
:   Attention in which the keys and values are shared across all the heads. ([The transformer since 2017](#since-2017))

### N

nats
:   Units of information measured with natural logarithms instead of base-2 ones; one nat is about 1.44 bits. ([Scale (2019-2022)](#scale))

n-best list
:   The list of candidate translations an older system proposes for a network to re-rank. ([Reading and writing sequences (2010-2016)](#seq2seq))

nearest neighbor search
:   Finding the stored vectors closest to a query's vector: the k-nearest-neighbors classifier without the vote. ([Giving models knowledge and tools](#tools))

needle in a haystack
:   A test that hides one fact in a long irrelevant text and asks the model for it. ([Prompting and context](#prompting))

negative sampling
:   Replacing a softmax over the whole vocabulary with yes-or-no questions answered by logistic regression: is this word a real neighbor, or one drawn at random? ([Words as vectors (1954-2014)](#embeddings))

neocognitron
:   Fukushima's 1980 model of visual pattern recognition, which recognized patterns regardless of their position. ([Networks with structure, and the second winter (1980-2005)](#structure))

next-sentence prediction
:   BERT's second training task: given two passages, guess whether the second really follows the first. ([Pretraining: learn language first, tasks later (2015-2019)](#pretraining))

n-gram
:   A sequence of n consecutive symbols, such as words. ([Language as prediction (1948-2000)](#prediction))

n-gram overlap
:   A contamination check that flags any test example sharing an n-gram (a 13-gram for GPT-3) with the training data. ([Measuring models](#evaluation))

non-parametric memory
:   An index of passages that a model searches at question time, as opposed to the parametric memory in its weights. ([Giving models knowledge and tools](#tools))

nucleus sampling
:   Keeping the smallest set of most probable tokens whose probabilities add up to at least p, then rescaling and drawing among them. Usually called top-p. ([Generating text](#generation))

### O

observation
:   In ReAct, the result that the program pastes in after an action. ([Giving models knowledge and tools](#tools))

offloading
:   Running a model too big for VRAM by keeping some layers on the graphics card and the rest in ordinary memory, run by the main processor. ([Small models and local inference](#local))

Ollama
:   A popular program that downloads and runs models with llama.cpp underneath. ([Small models and local inference](#local))

one-hot vector
:   A list as long as the vocabulary, with a 1 in the word's own position and 0 everywhere else. ([Words as vectors (1954-2014)](#embeddings))

one-shot
:   Of a prompt: a description of the task plus one worked example. ([Scale (2019-2022)](#scale))

open-book
:   Of a model: looking things up rather than answering from its parameters alone. ([Giving models knowledge and tools](#tools))

open-ended generation
:   Generation with no single right output, such as continuing a story. ([Generating text](#generation))

open-weight
:   Of a model: its trained weights can be downloaded and run on one's own hardware ([Adapting a model: fine-tuning and LoRA](#adapting)). [Small models and local inference](#local) states the book's policy: "open source" only in the Open Source Initiative's stricter sense or in quotations.

OR
:   The logic function that is true when at least one input is true; a neuron computes it if it fires when either input is on. ([The artificial neuron (1943-1969)](#neuron))

outliers
:   In quantization, a few dimensions of a model's activations with values up to 20 times larger than the rest, which one method keeps in 16 bits while rounding the rest to 8. ([Small models and local inference](#local))

overlap
:   In chunking, consecutive chunks sharing some text, so that a sentence cut at one chunk's edge appears whole in the next. ([Giving models knowledge and tools](#tools))

overoptimization
:   Optimizing against a reward model past the point where it tracks people's judgments. ([Teaching models to follow instructions (2017-2023)](#instructions))

### P

parallel corpus
:   A large collection of sentences paired with their human translations. ([Reading and writing sequences (2010-2016)](#seq2seq))

parameter-efficient fine-tuning
:   Adapting a small part of a model while leaving the rest frozen. ([Adapting a model: fine-tuning and LoRA](#adapting))

parameters
:   The numbers in a model that are set by training; also called weights. ([The destination: an LLM in one picture](#destination))

parametric memory
:   What a model knows in its weights, as opposed to non-parametric memory, an index it searches. ([Giving models knowledge and tools](#tools))

parity
:   The problem of deciding whether an input contains an odd number of active points; Minsky and Papert analyzed it for single-layer perceptrons. ([The artificial neuron (1943-1969)](#neuron))

pass@1
:   The average accuracy of a single attempt. ([The frontier (as of the book's date)](#frontier))

pass@k
:   The chance that at least one of k attempts passes. ([Measuring models](#evaluation))

patches
:   The square tiles an image is cut into for a transformer, each becoming one token (16 by 16 pixels in the 2021 vision transformer). ([The frontier (as of the book's date)](#frontier))

perceptron
:   In this book, a single threshold neuron whose weights are learned from examples. ([The artificial neuron (1943-1969)](#neuron))

perceptron convergence theorem
:   Rosenblatt's result that if a set of weights that does a task exists, the perceptron learning rule will find one in a finite number of steps. ([The artificial neuron (1943-1969)](#neuron))

perceptron learning rule
:   An error-correction rule: on each mistake, move the weights in the direction that would have reduced it; go through the examples in turn and repeat. ([The artificial neuron (1943-1969)](#neuron))

perplexity
:   2 raised to the cross-entropy in bits: the number of equally likely choices the model is, in effect, choosing among at each step. ([Language as prediction (1948-2000)](#prediction))

petaflop/s-days
:   A unit of compute: a thousand trillion operations per second for a day, $8.64 \times 10^{19}$ FLOPs. ([Scale (2019-2022)](#scale))

phrase-based translation
:   The leading form of statistical machine translation: cut the input sentence into phrases, translate each phrase, and possibly reorder the results. ([Reading and writing sequences (2010-2016)](#seq2seq))

phrase table
:   In phrase-based translation, the table of phrase translations, built by counting. ([Reading and writing sequences (2010-2016)](#seq2seq))

policy
:   In reinforcement learning, the agent's rule for choosing actions. ([Teaching models to follow instructions (2017-2023)](#instructions))

polysemantic
:   Of a neuron: responding to a mixture of unrelated things. ([The frontier (as of the book's date)](#frontier))

pooling
:   Shrinking feature maps by keeping one summary value per small neighborhood (also called subsampling), which makes the result less sensitive to small shifts. ([Networks with structure, and the second winter (1980-2005)](#structure))

positional encoding
:   Information about each token's position added to its vector before the first layer, so the model can use word order; fixed patterns of sine and cosine waves in the 2017 paper. ([Attention without recurrence (2017)](#attention))

position bias
:   A judge model favoring an answer for where it appears. ([Measuring models](#evaluation))

position interpolation
:   Extending a context window by linearly down-scaling position indices to match the original window size, so that every position is one the model knows. ([The transformer since 2017](#since-2017))

position table
:   A table with a learned vector for each position (1,024 rows in GPT-2); the row for a token's position is added to the token's row of the token table. ([Anatomy of a transformer](#anatomy))

post-norm
:   Normalizing the residual stream after each addition, as the 2017 transformer did. ([The transformer since 2017](#since-2017))

post-training
:   Any model training that happens after pretraining; it turns a base model into an assistant. ([Teaching models to follow instructions (2017-2023)](#instructions))

post-training quantization
:   Rounding a model's weights to fewer bits after training. ([Small models and local inference](#local))

power law
:   A relation of the form $L(N) = (N_c/N)^{\alpha_N}$: the loss falls as a fixed power of the model size (or data or compute). ([Scale (2019-2022)](#scale))

PPO
:   See *proximal policy optimization*.

prefill
:   \(1) The first phase of producing a reply, in which every prompt token passes through the network in one forward pass ([Generating text](#generation)). (2) Writing the start of a model's reply, such as an opening brace, for the model to continue ([Prompting and context](#prompting)).

prefix tuning
:   Training a short sequence of learned vectors that is prepended at every layer, while the model stays frozen. ([Adapting a model: fine-tuning and LoRA](#adapting))

pre-norm
:   Leaving the residual stream unnormalized: each sub-layer reads a normalized copy, and one last normalization comes before the output layer. ([The transformer since 2017](#since-2017))

pretrained
:   Of a network: trained first on one task or on general data, so that what it learned can be reused for another. ([Pretraining: learn language first, tasks later (2015-2019)](#pretraining))

pretraining
:   \(1) The first, general phase of training an LLM on large amounts of text, whose result is a base model ([The destination: an LLM in one picture](#destination)). (2) In the 2006 deep belief networks, the layer-by-layer stage, mostly without labels, before fine-tuning ([The turn: data, compute, and depth (2006-2012)](#deep-turn)).

previous-token head
:   An attention head that copies information about each token into the position after it. ([Prompting and context](#prompting))

primacy
:   The advantage of information placed at the beginning of a long input. ([Prompting and context](#prompting))

prompt
:   The text given to a model. ([Prompting and context](#prompting))

prompt caching
:   Keeping the cached keys and values of a prompt prefix that many requests share, so it need not be recomputed. ([Generating text](#generation))

prompt engineering
:   Writing prompts that get the result one wants. ([Prompting and context](#prompting))

prompt injection
:   Text that turns a model against the intent of whoever built the application. ([Prompting and context](#prompting))

prompt leaking
:   A prompt injection attack that makes a model print the application's hidden instructions. ([Prompting and context](#prompting))

prompt tuning
:   Training a soft prompt at the input only, while the model stays frozen. ([Adapting a model: fine-tuning and LoRA](#adapting))

proximal policy optimization (PPO)
:   A reinforcement learning algorithm (2017), used in RLHF to adjust the model toward answers the reward model scores higher. ([Teaching models to follow instructions (2017-2023)](#instructions))

pure sampling
:   Drawing the next token from the full distribution. ([Generating text](#generation))

### Q

QLoRA
:   LoRA trained through a frozen, 4-bit quantized model, enough to fine-tune a 65-billion-parameter model on a single 48 GB GPU. ([Adapting a model: fine-tuning and LoRA](#adapting))

quantization
:   Storing numbers with fewer bits by rounding them to a small set of allowed values. ([Adapting a model: fine-tuning and LoRA](#adapting))

quantization-aware training
:   Continuing training briefly with the rounding in the loop, so the model learns to tolerate it. ([Small models and local inference](#local))

query
:   \(1) In attention, the vector that says what a token is looking for ([Attention without recurrence (2017)](#attention)). (2) In information retrieval, what the user asks, for which the system returns documents ([Giving models knowledge and tools](#tools)).

### R

RAG
:   See *retrieval-augmented generation*.

random-chance baseline
:   The score of random guessing, such as 25% on four-choice questions. ([Measuring models](#evaluation))

rank
:   In LoRA, the small number of columns and rows of the two thin matrices whose product is the correction. ([Adapting a model: fine-tuning and LoRA](#adapting))

raw text contamination
:   Training data containing a test's original text before annotation, as opposed to the annotated test itself. ([Measuring models](#evaluation))

ReAct
:   A pattern (2022) for agents, from "reasoning and acting": the model alternates thoughts, actions, and observations. ([Giving models knowledge and tools](#tools))

reasoning effort
:   A setting that controls how much intermediate text a reasoning model writes before answering; more effort costs more and takes longer. ([The frontier (as of the book's date)](#frontier))

reasoning model
:   A language model trained, usually with reinforcement learning, to generate useful intermediate text, often long chains of thought, before answering. ([Prompting and context](#prompting))

recency
:   The advantage of information placed at the end of a long input. ([Prompting and context](#prompting))

recency bias
:   In few-shot prompting, a model's tendency to favor answers near the end of the prompt. ([Prompting and context](#prompting))

rectified linear unit (ReLU)
:   An activation function that outputs the input if it is positive and zero otherwise. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

recurrent network
:   A network that shares weights across steps in time by feeding its own hidden layer back into itself, reading one input per step. Also recurrent neural network (RNN). ([Networks with structure, and the second winter (1980-2005)](#structure))

reference model
:   In DPO, the starting model, kept frozen for comparison. ([Teaching models to follow instructions (2017-2023)](#instructions))

refusal
:   A reply that declines a request. ([Teaching models to follow instructions (2017-2023)](#instructions))

reinforcement learning
:   The part of machine learning in which an agent acts, receives a reward that says how well it did, and learns to act so as to collect more. ([Teaching models to follow instructions (2017-2023)](#instructions))

reinforcement learning from human feedback (RLHF)
:   The recipe of supervised fine-tuning, then training a reward model on people's comparisons, then reinforcement learning (PPO) against that reward model. ([Teaching models to follow instructions (2017-2023)](#instructions))

rejection sampling
:   The model writes several answers, the reward model picks the best, and the model is fine-tuned on the winners. ([Teaching models to follow instructions (2017-2023)](#instructions))

relative error reduction
:   The share of the remaining error that an improvement removes. ([Pretraining: learn language first, tasks later (2015-2019)](#pretraining))

relative position bias
:   One learned number per range of distances between query and key, added to the attention score (T5). ([The transformer since 2017](#since-2017))

ReLU
:   See *rectified linear unit*.

representation learning
:   Methods that let a machine be fed raw data and discover for itself the representations needed for detection or classification; a deep network does this in stages, each layer building on the one below. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

reranker
:   A cross-encoder that reorders the top candidates from a cheap first retrieval pass. ([Giving models knowledge and tools](#tools))

reset gate
:   In a GRU, the gate that lets the unit ignore the old hidden state and start again from the current input. ([Reading and writing sequences (2010-2016)](#seq2seq))

residual connection
:   A shortcut that carries a block's input around it and adds it to the block's output, so the block learns a correction to a running value. Also called a skip connection. ([Making deep networks trainable (2010-2016)](#depth))

residual stream
:   The vector each position carries from layer to layer of a transformer: the sum of the original embedding and the outputs of all the sub-layers so far. Other writing calls it the hidden state. ([Anatomy of a transformer](#anatomy))

retrieval
:   Finding relevant text at question time and placing it in the model's input, where the model reads it like any other input. ([Adapting a model: fine-tuning and LoRA](#adapting))

retrieval-augmented generation (RAG)
:   Combining a retriever with a model that writes its answer from the retrieved passages; the name comes from a 2020 paper. ([Giving models knowledge and tools](#tools))

reverse mode
:   The mode of automatic differentiation that computes the derivatives of a sequence of calculations by running backward through it; backpropagation is a special case. ([Learning in layers (1970-1989)](#backprop))

reward
:   In reinforcement learning, the number that says how well the agent did. ([Teaching models to follow instructions (2017-2023)](#instructions))

reward hacking
:   A model exploiting flaws in its reward to score highly without doing what was intended, like a robot that learned to look as if it grasped an object. ([Teaching models to follow instructions (2017-2023)](#instructions))

reward model
:   A network that, given a prompt and a response, outputs one number, a score, learned from people's comparisons. ([Teaching models to follow instructions (2017-2023)](#instructions))

RLAIF
:   Reinforcement learning from AI feedback: RLHF with a model in place of the human judge. ([Teaching models to follow instructions (2017-2023)](#instructions))

RLHF
:   See *reinforcement learning from human feedback*.

RMSNorm
:   A normalization that rescales a vector by its root mean square, with a learned gain, without subtracting the mean. ([The transformer since 2017](#since-2017))

RMSProp
:   An optimizer that divides each weight's learning rate by a running average of the magnitudes of that weight's recent gradients. ([The training loop (1951-2017)](#toolkit))

RNN
:   See *recurrent network*.

role
:   The label of each message in a chat format: usually system, user, or assistant. ([Teaching models to follow instructions (2017-2023)](#instructions))

root mean square
:   The square root of the average squared entry of a vector. ([The transformer since 2017](#since-2017))

RoPE
:   See *rotary position embeddings*.

rotary position embeddings (RoPE)
:   Positions encoded inside attention: pairs of numbers in each query and key are turned by angles proportional to their positions, so the score depends on the two words and their relative position only. ([The transformer since 2017](#since-2017))

round-to-nearest
:   The simplest quantization scheme: stretch a group of weights so the largest in absolute value lands on the largest allowed integer, round each to the nearest integer, and store the integers plus the scale. ([Small models and local inference](#local))

router
:   In a mixture of experts, the gating network that chooses experts for each input: a softmax classifier with one class per expert. ([The transformer since 2017](#since-2017))

runtime
:   The program that loads a model's weights and runs the generation loop; also called an inference engine. ([Small models and local inference](#local))

### S

safetensors
:   A file format for storing tensors safely: a short header listing each tensor's name, number type, shape, and position, then the raw numbers. ([Small models and local inference](#local))

sampling
:   Choosing the next token from the model's probabilities, a separate step from computing them. ([The destination: an LLM in one picture](#destination))

saturated
:   Of a unit: its slope is near zero, so it passes almost no blame backward. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

saturation
:   \(1) In BM25, the cap on how much one term can add to a document's score however often it occurs ([Giving models knowledge and tools](#tools)). (2) Of a benchmark: models score so high that it can no longer tell them apart ([Measuring models](#evaluation)).

scaffold
:   See *agent harness*.

scale
:   In quantization, the one number shared by a group of weights that maps them onto the allowed integers. ([Small models and local inference](#local))

scaled dot-product attention
:   Attention as the 2017 transformer computes it: dot products of a query with every key, divided by the square root of the key length, turned into weights by a softmax, which then average the values. ([Attention without recurrence (2017)](#attention))

scaling law
:   A fitted curve, a power law, of a model's loss against its size, training data, or compute. ([Scale (2019-2022)](#scale))

scratchpad
:   Intermediate results a model is trained to write before its answer. ([Prompting and context](#prompting))

self-attention
:   Attention in which every token in a sequence gathers information from every other token in the same sequence, all at once. ([Attention without recurrence (2017)](#attention))

self-consistency
:   Sampling many chains of thought at a temperature above zero and taking the most common final answer, a majority vote. ([Prompting and context](#prompting))

self-enhancement bias
:   A judge model favoring its own answers. ([Measuring models](#evaluation))

self-supervised learning
:   Learning in which the data provide their own labels, as when the next token of a text is the correct answer for the text before it. ([The destination: an LLM in one picture](#destination))

semantic prior
:   What a model already knows about the words used as labels, which small models answer from even when the prompt's labels are flipped. ([Prompting and context](#prompting))

SentencePiece
:   A software tool (2018) that implements both BPE and the unigram language model method for tokenization. ([Tokens: what the model actually sees (1994-2018)](#tokens))

server
:   In the Model Context Protocol, a service that offers capabilities to a host. ([Giving models knowledge and tools](#tools))

SFT
:   See *supervised fine-tuning*.

SGD
:   See *stochastic gradient descent*.

shape
:   The sizes of a tensor along each of its axes. ([The training loop (1951-2017)](#toolkit))

shared expert
:   In a mixture of experts, an expert that every token uses. ([The transformer since 2017](#since-2017))

sigmoid
:   The logistic function, which turns any number into a value between 0 and 1. A neuron with a sigmoid activation is logistic regression. ([The artificial neuron (1943-1969)](#neuron))

SiLU
:   See *Swish*.

skip connection
:   See *residual connection*.

skip-gram
:   The word2vec method that uses a word's vector to predict the words around it. Its partner is CBOW. ([Words as vectors (1954-2014)](#embeddings))

sliding-window attention
:   Attention in which each token attends only to a fixed number of tokens before it. ([The transformer since 2017](#since-2017))

smoothing
:   Taking a little probability from more frequent events and giving it to unseen ones, so that no sequence gets probability zero. ([Language as prediction (1948-2000)](#prediction))

soft alignment
:   Bahdanau and colleagues' name for attention weights: how much each source word contributes to each output word. ([Reading and writing sequences (2010-2016)](#seq2seq))

softmax
:   The function that turns scores into probabilities: exponentiate each score and divide by the sum. It ends multinomial logistic regression. ([The destination: an LLM in one picture](#destination))

soft prompt
:   A handful of extra embedding vectors, found by backpropagation, that correspond to no real words. ([Adapting a model: fine-tuning and LoRA](#adapting))

soft targets
:   A teacher model's probabilities, used to train the student. ([Adapting a model: fine-tuning and LoRA](#adapting))

sparse attention
:   Attention in which each position attends to a structured subset of positions. ([The transformer since 2017](#since-2017))

sparse autoencoder
:   A network that rewrites each activation vector as a combination of many learned directions, far more than the layer's width, with a penalty that keeps few active at once. ([The frontier (as of the book's date)](#frontier))

sparse retrieval
:   Keyword retrieval, in which each document's vector has an entry for every word in the vocabulary, almost all zero. ([Giving models knowledge and tools](#tools))

special token
:   A vocabulary entry with its own ID that marks structure rather than content, such as the end of a text. ([Tokens: what the model actually sees (1994-2018)](#tokens))

speculative decoding
:   Using a small, fast model to guess several tokens ahead and the large model to check all the guesses in one parallel pass. ([Generating text](#generation))

SQL injection
:   An old database attack in which text typed into a form is read as part of a database command; its cure keeps commands and data structurally apart. ([Prompting and context](#prompting))

squashing function
:   A function, like the sigmoid, that squeezes any number into a fixed range. ([Learning in layers (1970-1989)](#backprop))

standard error
:   The typical error of a score due to the finite number of questions; for accuracy $p$ on $n$ questions, $\sqrt{p(1-p)/n}$. ([Measuring models](#evaluation))

state space models
:   Recurrent models that carry a fixed-size state from token to token, so their cost grows in proportion to the length; Mamba is one. ([The transformer since 2017](#since-2017))

static embeddings
:   Embeddings that give each word one fixed vector, whatever its context. ([Words as vectors (1954-2014)](#embeddings))

statistical machine translation
:   Translation learned from a parallel corpus by counting, the dominant approach of the late 2000s. ([Reading and writing sequences (2010-2016)](#seq2seq))

steering
:   Changing a model's behavior by setting internal features. ([The frontier (as of the book's date)](#frontier))

step
:   One update of the weights; also called an iteration. ([The training loop (1951-2017)](#toolkit))

step function
:   An activation function that outputs 1 if the weighted sum is above zero, and 0 otherwise. ([The artificial neuron (1943-1969)](#neuron))

stochastic gradient descent (SGD)
:   Gradient descent in which each step estimates the gradient from a minibatch rather than the whole training set. ([The training loop (1951-2017)](#toolkit))

stop list
:   A list of high-frequency words, often function words, that retrieval drops. ([Giving models knowledge and tools](#tools))

structured output
:   A model reply in a fixed shape, a set of named fields a program can read, usually JSON. ([Prompting and context](#prompting))

student
:   In knowledge distillation, the model trained to imitate the teacher. ([Adapting a model: fine-tuning and LoRA](#adapting))

subsampling
:   See *pooling*.

SuperGLUE
:   The 2019 successor of GLUE, with eight harder tasks. ([Measuring models](#evaluation))

superposition
:   A hypothesized phenomenon in which a network represents more independent features than it has neurons, by giving each feature its own combination of neurons. ([The frontier (as of the book's date)](#frontier))

supervised fine-tuning (SFT)
:   Fine-tuning on demonstrations: prompts paired with the responses people want. ([Teaching models to follow instructions (2017-2023)](#instructions))

support vector machine (SVM)
:   The 1995 method of Cortes and Vapnik, which maps inputs into a very high-dimensional feature space and is trained by solving a convex quadratic problem with a unique answer. ([Networks with structure, and the second winter (1980-2005)](#structure))

SVM
:   See *support vector machine*.

SwiGLU
:   The gated linear unit variant whose switch is the Swish function; used in LLaMA's feed-forward networks. ([The transformer since 2017](#since-2017))

Swish
:   The function $x\,\sigma(x)$, with $\sigma$ the logistic sigmoid; also called SiLU. ([The transformer since 2017](#since-2017))

sycophancy
:   Telling users what they appear to want to hear. ([Teaching models to follow instructions (2017-2023)](#instructions))

system prompt
:   The opening message of a conversation, written by whoever deploys the model, with instructions for the whole conversation. ([Teaching models to follow instructions (2017-2023)](#instructions))

### T

task location
:   The hypothesis that examples in a prompt serve to locate a task the model already learned, rather than to teach it. ([Prompting and context](#prompting))

teacher
:   In knowledge distillation, the larger model whose behavior the student imitates. ([Adapting a model: fine-tuning and LoRA](#adapting))

temperature
:   A number by which every score is divided before the softmax: below 1 it sharpens the distribution toward the top token, above 1 it flattens it. ([Generating text](#generation))

tensor
:   An array of numbers arranged on a regular grid with a variable number of axes. ([The training loop (1951-2017)](#toolkit))

term frequency (tf)
:   How often a word occurs in a document. ([Giving models knowledge and tools](#tools))

test-time compute
:   Computation spent while answering rather than while training; also called inference-time compute. ([The frontier (as of the book's date)](#frontier))

tf
:   See *term frequency*.

tf-idf
:   A word's term frequency in a document multiplied by its inverse document frequency. ([Giving models knowledge and tools](#tools))

thought
:   In ReAct, free text the model writes for itself. ([Giving models knowledge and tools](#tools))

threshold
:   The amount a step neuron's weighted sum of inputs must exceed for it to fire: a bias of -0.1 means a threshold of 0.1. ([The artificial neuron (1943-1969)](#neuron))

tiling
:   Splitting queries, keys, and values into blocks that fit on the chip and working through them block by block. ([The transformer since 2017](#since-2017))

time horizon
:   The time humans typically take to complete the tasks that an AI model can complete with a 50% success rate. ([The frontier (as of the book's date)](#frontier))

time to first token
:   The delay before the first word of a reply appears. ([Generating text](#generation))

token
:   One of the pieces of text in a model's vocabulary, often a whole common word and sometimes a piece of a rarer word. (In older usage, an occurrence of a word, as opposed to a type.) ([The destination: an LLM in one picture](#destination))

token ID
:   A token's number: its position in the vocabulary list. ([The destination: an LLM in one picture](#destination))

tokenizer
:   The separate procedure, fixed before the model is trained, that cuts text into tokens. ([The destination: an LLM in one picture](#destination))

token table
:   The table whose rows are the tokens' vectors (50,257 rows of 768 numbers in GPT-2 small); the same as the embedding table. ([Anatomy of a transformer](#anatomy))

tool
:   A program that the system around a model can run on its behalf, such as a search engine, a calculator, or a database. ([Giving models knowledge and tools](#tools))

tool call
:   Part of a model's reply: a tool name with its arguments filled in, for the program to run. ([Giving models knowledge and tools](#tools))

tool definition
:   What a model sees of a tool: a name, a short description, and a description of its arguments. ([Giving models knowledge and tools](#tools))

tool result
:   The output of a tool call, which the program sends back to the model. ([Giving models knowledge and tools](#tools))

top-1 error
:   The fraction of test images for which the model's first guess is wrong. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

top-20 accuracy
:   The share of questions for which at least one of the 20 highest-scoring passages contains the answer. ([Giving models knowledge and tools](#tools))

top-5 error
:   The fraction of test images for which the correct label is not among the model's five most probable labels. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

top-k routing
:   In a mixture of experts, keeping the k highest-scoring experts and running only those. ([The transformer since 2017](#since-2017))

top-k sampling
:   Keeping the k most probable tokens, rescaling their probabilities to sum to one, and drawing among them. ([Generating text](#generation))

top-p
:   See *nucleus sampling*.

total parameter count
:   In a mixture of experts, all the parameters stored, as opposed to the active parameter count. ([The transformer since 2017](#since-2017))

training
:   Setting a model's parameters: it is shown text, its next-token predictions are compared with the actual tokens, and the parameters are adjusted to reduce the loss. ([The destination: an LLM in one picture](#destination))

training tokens
:   How many tokens of text a model reads during training. ([Scale (2019-2022)](#scale))

transfer learning
:   Using what has been learned in one setting to improve generalization in another. ([Pretraining: learn language first, tasks later (2015-2019)](#pretraining))

transformer
:   A network design published in 2017 and built on attention: a stack of blocks, each letting every position gather information from others and then processing each position on its own. ([The destination: an LLM in one picture](#destination))

trigram
:   An n-gram of three consecutive symbols. ([Language as prediction (1948-2000)](#prediction))

type
:   A distinct word, as opposed to its occurrences (tokens, in the older sense). ([Tokens: what the model actually sees (1994-2018)](#tokens))

### U

unified memory
:   One pool of memory shared by the processor and the graphics unit, as on Apple's chips. ([Small models and local inference](#local))

unigram
:   An n-gram of one symbol. ([Language as prediction (1948-2000)](#prediction))

unigram language model
:   A tokenization method (2018) that starts from a large set of candidate pieces and repeatedly removes the ones whose removal hurts the fit least, until the vocabulary is the size wanted. ([Tokens: what the model actually sees (1994-2018)](#tokens))

unit tests
:   Small programs that check an answer, here a generated program. ([Measuring models](#evaluation))

universal approximation theorem
:   The 1989 result that a network with one hidden layer of squashing units can approximate essentially any function as closely as desired, given enough hidden units. It promises existence, not that training will find the weights. ([Learning in layers (1970-1989)](#backprop))

unrolling
:   Drawing a recurrent network as a chain with one copy per time step; also called unfolding. ([Networks with structure, and the second winter (1980-2005)](#structure))

update gate
:   In a GRU, the gate that decides how much of the old hidden state to keep. ([Reading and writing sequences (2010-2016)](#seq2seq))

UTF-8
:   The encoding that writes each character of text as a sequence of one to four bytes. ([Tokens: what the model actually sees (1994-2018)](#tokens))

### V

validation set
:   Data held out from the training data and used to choose hyperparameters. ([The training loop (1951-2017)](#toolkit))

value
:   In attention, the vector a token passes on if it is looked at. ([Attention without recurrence (2017)](#attention))

vanishing gradient
:   The backward signal shrinking as it is multiplied by factors below 1 at each step, so that learning to bridge long gaps becomes very slow or fails. ([Networks with structure, and the second winter (1980-2005)](#structure))

vector
:   A list of numbers. ([The destination: an LLM in one picture](#destination))

vector database
:   A product that stores vectors and searches them by approximate nearest neighbor search. Also called a vector store. ([Giving models knowledge and tools](#tools))

vector store
:   See *vector database*.

verbosity bias
:   A judge model favoring longer answers even if they are not as clear, good, or accurate. ([Measuring models](#evaluation))

verifiability
:   The property that a reader can check a statement against its cited source. ([Giving models knowledge and tools](#tools))

verifiable reward
:   A reward that a program can check, with no human or learned model judging, such as whether a math answer is correct. ([The frontier (as of the book's date)](#frontier))

verifier
:   A separately trained model that rates answers. ([The frontier (as of the book's date)](#frontier))

violation rate
:   How often a model answers adversarial prompts unsafely. ([Teaching models to follow instructions (2017-2023)](#instructions))

vision-language model
:   A model that reads images and text and writes text. ([The frontier (as of the book's date)](#frontier))

vocabulary
:   The fixed list of tokens a model knows. ([The destination: an LLM in one picture](#destination))

VRAM
:   A graphics card's own memory. ([Small models and local inference](#local))

### W

warmup
:   A start to the learning-rate schedule in which the rate begins small and rises before it falls. ([The training loop (1951-2017)](#toolkit))

weight decay
:   Shrinking every weight a little at each step; for plain SGD the same as the L2 penalty of ridge regression, but not for Adam. ([The training loop (1951-2017)](#toolkit))

weighted sum
:   A neuron's inputs each multiplied by their weight and added up, plus the bias. ([The artificial neuron (1943-1969)](#neuron))

weights
:   Another name for parameters. In a neuron, an input's weight says how much that input counts and in which direction. ([The destination: an LLM in one picture](#destination))

weight sharing
:   Letting many connections be controlled by one parameter, as in convolution. ([Networks with structure, and the second winter (1980-2005)](#structure))

weight tying
:   Using the same table at the bottom of a model to turn token IDs into vectors and at the top to turn vectors into scores. ([Anatomy of a transformer](#anatomy))

word embedding
:   A dense vector that represents a word. ([Words as vectors (1954-2014)](#embeddings))

word error rate
:   The percentage of words a speech recognizer gets wrong. ([The turn: data, compute, and depth (2006-2012)](#deep-turn))

WordPiece
:   A tokenization method (2012) that, like BPE, repeatedly joins two units, choosing the join that most increases the likelihood of the training data under a language model. ([Tokens: what the model actually sees (1994-2018)](#tokens))

### X

XOR
:   Exclusive or: the output is 1 when exactly one of two inputs is 1. No single straight line separates its cases, so a single neuron cannot compute it. ([The artificial neuron (1943-1969)](#neuron))

### Y

YaRN
:   A context extension method (2023) for rotary position embeddings that stretches only the slow pairs. ([The transformer since 2017](#since-2017))

### Z

zero-shot
:   Of a prompt: only a description of the task, with no examples. ([Scale (2019-2022)](#scale))

zero-shot chain of thought
:   Adding a phrase such as "Let's think step by step" before the answer, with no demonstrations, so the model writes its reasoning; a second call extracts the final answer. ([Prompting and context](#prompting))
