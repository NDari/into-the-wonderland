# Notation and math refresher {#notation}

<!-- D-002: intuition only; standard textbook formulas, every symbol explained, no derivations. D-003: no code. D-009: numbers from code/checks/notation.py, which imports the destination, generation, prediction, and neuron chapters' scripts and reads the embeddings chapter's toy vectors. D-010: chapters are referred to by ID. -->

This appendix collects the mathematics the chapters use, in the order they need it, with one small worked example per idea. It is a refresher, not a course: the reader's undergraduate linear algebra, calculus, and probability cover everything here. What may be new is the notation, which the book takes from the papers it describes, and the handful of places where machine learning uses a familiar idea in an unfamiliar way. Each section ends with the chapters that rely on it. The last section is a table of every symbol in the book, with its meaning and the chapter where it first appears.

## Reading the formulas

Letters in formulas are set in italics. A lowercase letter is a single number or a vector ($x$, $q$, $z$); an uppercase letter is usually a matrix or a count ($W$, $N$). A subscript picks out one item of a collection: $x_i$ is the $i$-th entry of $x$, and $k_j$ is the key of token $j$. A subscript in upright letters is a label, not an index: $d_{\text{model}}$ is "the $d$ of the model". The sum sign $\sum_j$ means "add up the following over every value of $j$". Formulas follow the source each chapter describes, so the same letter can mean different things in different chapters; every formula in the book is followed by the meaning of each of its symbols, and the table at the end lists them all.

In running text the book writes multiplication as "x" (6 x 174.6 billion) and the shape of a table as "by" or "x" (a 4,096 by 4,096 matrix); in formulas it uses $\times$.

## Numbers and units

**Large numbers.** A thousand is $10^3$, a million $10^6$, a billion $10^9$, and a trillion $10^{12}$. A model named "8B" has about 8 billion parameters. Numbers too large or too small to write out are given in **scientific notation**, $a \times 10^{b}$: a number $a$ between 1 and 10 times a power of ten. <!-- D-009: code/checks/notation.py, Example 1 --> The compute estimate of [the chapter on scale](#scale) for GPT-3, 6 x 174.6 billion x 300 billion, is $3.14 \times 10^{23}$ operations. A negative power means a small number: $10^{-8}$, the tiny constant in Adam ([the toolkit chapter](#toolkit)), is 0.00000001. Powers of two grow just as fast: $2^{10}$ is 1,024, $2^{30}$ is 1,073,741,824, and $2^{100}$, the number of ways to drop 100 units in [the chapter on depth](#depth), is about $1.27 \times 10^{30}$.

**Bits and bytes.** A **bit** is one binary digit, 0 or 1. A **byte** is 8 bits. A number stored in 32 bits takes 4 bytes; one in 16 bits, 2 bytes. The memory needed for a model's weights is

$$\text{memory for the weights, in bytes} = \frac{N \times b}{8}$$

where $N$ is the number of parameters and $b$ the number of bits per parameter; dividing by 8 turns bits into bytes. <!-- D-009: code/checks/notation.py, Example 1 --> For 8 billion parameters:

| Bits per parameter | Bytes | GB | GiB |
|---:|---:|---:|---:|
| 32 | 32,000,000,000 | 32 | 29.80 |
| 16 | 16,000,000,000 | 16 | 14.90 |
| 8 | 8,000,000,000 | 8 | 7.45 |
| 4 | 4,000,000,000 | 4 | 3.73 |

Table: Memory for 8 billion parameters at four precisions, in decimal gigabytes and binary gibibytes.

**GB and GiB.** Memory is counted in two systems. In this book, following [the destination chapter](#destination), a **gigabyte** (GB) is a billion bytes, $10^9$, and likewise a kilobyte (kB) is 1,000 bytes and a megabyte (MB) a million. The binary units count in powers of two: a **kibibyte** (KiB) is $2^{10}$ = 1,024 bytes, a mebibyte (MiB) $2^{20}$ = 1,048,576, and a **gibibyte** (GiB) $2^{30}$ = 1,073,741,824 bytes. <!-- D-009: code/checks/notation.py, Example 1 --> A GiB is about 1.074 GB, so the same quantity is about 7% smaller in GiB. The key-value cache of [the generation chapter](#generation) for Llama 3 8B takes 131,072 bytes per token, which is exactly 128 KiB (or 131.1 kB); for a window of 131,072 tokens it is 17,179,869,184 bytes, which is 17.2 GB and exactly 16 GiB. Software differs in which units it reports, so check the label before comparing two figures.

Used in: [the destination chapter](#destination), [the chapter on training](#training), [the generation chapter](#generation), [the chapter on the transformer since 2017](#since-2017), and [the chapter on local inference](#local).

## Vectors and dot products

A **vector** is an ordered list of numbers, such as the embedding of a word or the running value at one position of a transformer. The book writes a vector as a lowercase italic letter ($x$, $q$, $a$) and its $i$-th entry as $a_i$. The number of entries is the vector's **dimension**, often written $d$; the chapters also call it the vector's width or length in numbers. A vector of $d$ numbers can be pictured as an arrow in a space with $d$ axes. (One formula, in [the chapter on the transformer since 2017](#since-2017), prints a vector in bold, $\mathbf{a}$; it is the same kind of object.)

Two vectors of the same dimension are added entry by entry, which is what a residual connection does ([the chapter on depth](#depth)). The **dot product** multiplies matching entries and adds:

$$a \cdot b = \sum_{i=1}^{d} a_i b_i$$

where $a$ and $b$ are vectors of $d$ entries, $a_i$ and $b_i$ are their $i$-th entries, and the sum runs over all $d$ of them. The result is a single number. The **length** of a vector, written $\|a\|$, is the square root of its dot product with itself. The **cosine similarity** of [the embeddings chapter](#embeddings) divides the dot product by both lengths, so that only the direction counts:

$$\cos(a, b) = \frac{a \cdot b}{\|a\| \, \|b\|}$$

where $a \cdot b$ is the dot product and $\|a\|$ and $\|b\|$ are the lengths. It is 1 for vectors pointing the same way, 0 for perpendicular ones, and -1 for opposite ones.

<!-- D-009: code/checks/notation.py, Example 2 --> The embeddings chapter's made-up vectors are "cat" = [0.9, 0.8, 0.1] and "dog" = [0.8, 0.9, 0.2]. Their dot product is 0.9 x 0.8 + 0.8 x 0.9 + 0.1 x 0.2 = 1.46. The length of "cat" is the square root of 1.46, or 1.208, and that of "dog" the square root of 1.49, or 1.221. The cosine is 1.46 divided by 1.208 x 1.221, which is 0.990. Doubling every entry of "cat" doubles the dot product, to 2.92, but leaves the cosine at 0.990. Two one-hot vectors, each a single 1 among zeros, have a dot product of 0 and are a distance of $\sqrt{2}$, or 1.414, apart, whichever two words they stand for.

The weighted sum of [the neuron chapter](#neuron) is a dot product plus a bias, $z = w \cdot x + b$, with $w$ the vector of weights, $x$ the vector of inputs, and $b$ the bias. <!-- D-009: code/checks/notation.py, Example 2 --> In that chapter's vote, weights [0.6, 0.9, -0.4] and inputs [1, 0, 1] give a dot product of 0.2, and the bias of -0.1 brings it to 0.1. An attention score ([the attention chapter](#attention)) is the dot product of a query and a key, divided by the square root of the key's dimension $d_k$: by 8 for keys of 64 numbers.

Some operations work entry by entry. A function such as the ReLU of [the deep learning chapter](#deep-turn) is applied to each entry of a vector separately. The **entry-by-entry product** of two vectors multiplies matching entries and keeps them as a vector, without adding; [the chapter on the transformer since 2017](#since-2017) writes it $\otimes$, following its source.

Used in: [the neuron chapter](#neuron), [the embeddings chapter](#embeddings), [the attention chapter](#attention), [the anatomy chapter](#anatomy), and [the chapter on retrieval and tools](#tools).

## Matrices

A **matrix** is a rectangular table of numbers. A $d \times k$ matrix ("$d$ by $k$") has $d$ rows and $k$ columns. The book writes matrices as uppercase italic letters ($W$, $A$, $B$). Most of a neural network's parameters are the entries of weight matrices, and a layer's parameter count is its rows times its columns, plus one bias per output.

**Matrix times vector.** Multiplying a $d \times k$ matrix $W$ by a vector $x$ of $k$ entries gives a vector of $d$ entries: each output entry is the dot product of one row of $W$ with $x$. A weight matrix is therefore a bank of neurons, one per row, all reading the same input.

<!-- D-009: code/checks/notation.py, Example 3 --> Take the 2 by 3 matrix with rows [1, 0, 2] and [0, 1, -1], and the vector [3, 1, 2]. The first row's dot product with the vector is 1 x 3 + 0 x 1 + 2 x 2 = 7, and the second's is -1, so the product is the vector [7, -1]: three numbers in, two out.

Papers write this product in two orders. The LoRA paper, in [the chapter on adapting](#adapting), writes $W x$, with the vector on the right, as above. The transformer paper, followed in [the anatomy chapter](#anatomy), writes $x W$, with the vector on the left; then the matrix has one row per input entry and one column per output entry, the same table turned on its side. <!-- D-009: code/checks/notation.py, Example 3 --> Multiplying [3, 1, 2] by the 3 by 2 matrix with rows [1, 0], [0, 1], and [2, -1] gives the same [7, -1]. Both orders describe the same computation.

**Matrix times matrix.** Two matrices can be multiplied when the inner sizes match: a $d \times r$ matrix times an $r \times k$ matrix is a $d \times k$ matrix. Multiplying a vector by the product $B A$ is the same as multiplying it by $A$ first and then by $B$.

**Counting parameters.** <!-- D-009: code/checks/notation.py, Example 3 --> The feed-forward network of GPT-2 small, in [the anatomy chapter](#anatomy), maps 768 numbers to 3,072 and back. The first matrix has 768 x 3,072 weights and 3,072 biases, 2,362,368 parameters; the second has 3,072 x 768 weights and 768 biases, 2,360,064; together 4,722,432 in each block.

**Rank.** The **rank** of a matrix is the number of independent directions among its rows (equivalently, among its columns). A $d \times k$ matrix of rank $r$ can always be written as a $d \times r$ matrix times an $r \times k$ matrix, and so stored in $r(d + k)$ numbers instead of $d \times k$. <!-- D-009: code/checks/notation.py, Example 3 --> The column [1, 2, 3] times the row [2, 0, 1] gives a 3 by 3 matrix whose rows are [2, 0, 1], [4, 0, 2], and [6, 0, 3]: every row is a multiple of [2, 0, 1], so the rank is 1, and six numbers make nine. At scale the saving is large. A rank-8 change to a 4,096 by 4,096 matrix, LoRA's setting in [the chapter on adapting](#adapting), needs 65,536 numbers instead of 16,777,216, which is 0.39%. The reader's PCA rests on the same idea: keeping the top few components gives the best low-rank approximation of a centered data matrix, and latent semantic analysis in [the embeddings chapter](#embeddings) does the same with a table of word counts.

A table of numbers with more than two axes, such as a stack of matrices, is called a **tensor**; a vector is a tensor with one axis and a matrix one with two.

Used in: [the embeddings chapter](#embeddings), [the attention chapter](#attention), [the anatomy chapter](#anatomy), [the chapter on adapting](#adapting), and [the chapter on the transformer since 2017](#since-2017).

## Logarithms and exponentials

The number $e$, about 2.718, is the base of the natural logarithm. The **exponential function** $e^{x}$ is always positive, equals 1 at $x = 0$, and multiplies by about 2.718 for each step of 1 in $x$. <!-- D-009: code/checks/notation.py, Example 4 --> For example, $e^{-1}$ is 0.368.

The **logarithm** to base $b$ undoes raising $b$ to a power: $\log_b x$ is the power to which $b$ must be raised to give $x$. <!-- D-009: code/checks/notation.py, Example 4 --> So $\log_{10}$ of 1,000,000 is 6, and $\log_2$ of 1,024 is 10. Three bases appear in the book:

- **Base 2**, written $\log_2$, measures information in **bits** ([the prediction chapter](#prediction)).
- **Base $e$**, the **natural logarithm**, measures information in **nats** ([the chapter on scale](#scale), [the chapter on training](#training)). Training logs usually use it, so losses are usually reported in nats. In [the chapter on instructions](#instructions), $\log$ written without a base is the natural logarithm. In the time-horizon formula of [the frontier chapter](#frontier), the base does not change the predictions, only the size of the fitted slope.
- **Base 10**, written $\log_{10}$, appears in tf-idf ([the chapter on retrieval and tools](#tools)); the Elo scale of [the evaluation chapter](#evaluation) uses powers of 10.

Three rules do most of the work. The logarithm of a product is the sum of the logarithms; the logarithm of a ratio is the difference; and the logarithm of $x^c$ is $c$ times the logarithm of $x$. Logarithms in different bases differ only by a constant factor. <!-- D-009: code/checks/notation.py, Example 4 --> The natural logarithm of 2 is 0.693, so one nat is 1/0.693 = 1.443 bits, and a loss in nats is turned into bits by dividing by 0.693.

**Why probabilities are handled as logarithms.** The probability of a text is a product of many numbers below one, which quickly becomes too small to work with. Its logarithm is a sum. <!-- D-009: code/checks/notation.py, Example 4 --> The six-token text of [the destination chapter](#destination) has probability 0.040 x 0.010 x 0.150 x 0.400 x 0.600 x 0.571 = $8.222 \times 10^{-6}$. The base-2 logarithm of that product is -16.89, and so is the sum of the six base-2 logarithms. The total surprise of the text is 16.89 bits, or 11.71 nats: 2.815 bits, or 1.951 nats, per token. A **log-probability** (always zero or negative) and a **log-ratio** of two probabilities, both in [the chapter on instructions](#instructions), are this same move.

**Power laws and log scales.** A power law $y = c\,x^{k}$, with $c$ and $k$ constants, becomes a straight line when both sides are logged: $\log y = \log c + k \log x$. That is why [the chapter on scale](#scale) plots on log-log axes, where the fitted exponent is the slope. <!-- D-009: code/checks/notation.py, Example 4 --> With that chapter's exponent of 0.076, doubling the model multiplies the loss by $2^{-0.076}$ = 0.949, and a tenfold increase multiplies it by $10^{-0.076}$ = 0.839. A quantity that doubles every $T$ days grows by a factor of $2^{d/T}$ after $d$ days: with the frontier chapter's doubling time of 207 days, $2^{365/207}$ = 3.39 a year.

Used in: [the prediction chapter](#prediction), [the chapter on scale](#scale), [the chapter on training](#training), [the chapter on instructions](#instructions), [the chapter on retrieval and tools](#tools), [the evaluation chapter](#evaluation), and [the frontier chapter](#frontier).

## Probability, entropy, and perplexity

A **probability distribution** over a finite set of outcomes, such as the tokens of a vocabulary, is a list of numbers $p_i$, one per outcome, each between 0 and 1 and together summing to 1. $P(\ldots)$ is the probability of whatever is in the brackets, and $P(y \mid x)$, read "the probability of $y$ given $x$", is a **conditional probability**. A language model gives the probability of the next token given the text so far; the probability of a whole text is the product of these next-token probabilities, one per token ([the destination chapter](#destination)). [The chapter on instructions](#instructions) writes a model's probability of a response $y$ to a prompt $x$ as $\pi(y \mid x)$, following reinforcement learning, where $\pi$ names the model's behavior (its **policy**); it is not the number 3.14159. An **expected value** is an average weighted by probabilities, such as the expected score of a guess in [the evaluation chapter](#evaluation).

**Surprise and entropy.** The **surprise** of an outcome of probability $p$ is $-\log_2 p$ bits: 1 bit for an outcome with probability one half, more for rarer outcomes. **Entropy** is the average surprise of a distribution:

$$H = -\sum_i p_i \log_2 p_i$$

where $p_i$ is the probability of outcome $i$ and the sum runs over all outcomes. It is zero when one outcome is certain and largest when all are equally likely. <!-- D-009: code/checks/notation.py, Example 5 --> A fair die has an entropy of 2.585 bits. The prediction chapter's loaded die, which shows a six half the time and each other face a tenth of the time, has 2.161: a six carries 1 bit of surprise, any other face 3.322 bits.

**Cross-entropy and KL divergence.** The **cross-entropy** scores outcomes drawn from one distribution with the probabilities of another, usually a model's:

$$H(p, q) = -\sum_i p_i \log_2 q_i$$

where $p_i$ is the true probability of outcome $i$ and $q_i$ the probability the model gives it. On a long text, the average of $-\log_2 q$ over the tokens that actually occur estimates it; that average is the cross-entropy of [the prediction chapter](#prediction) and the loss of [the chapter on training](#training) (there in nats). <!-- D-009: code/checks/notation.py, Example 5 --> Rolls of the loaded die, scored by a model that believes the die is fair, cost 2.585 bits each, 0.424 more than the true entropy of 2.161. That excess, cross-entropy minus entropy, is the **Kullback-Leibler (KL) divergence** of the model from the truth. It is never negative and is zero only when the two distributions agree. It is what the KL penalty of [the chapter on instructions](#instructions) keeps small.

**Perplexity** turns a cross-entropy back into a number of choices:

$$PP = 2^{H}$$

where $H$ is the cross-entropy in bits per token; with $H$ in nats, the same number is $e^{H}$. <!-- D-009: code/checks/notation.py, Example 5 --> A fair die has perplexity 6.00 and the loaded die 4.47. The destination chapter's six-token text, at 2.815 bits per token, has perplexity $2^{2.815}$ = 7.04; at 1.951 nats per token, $e^{1.951}$ gives the same 7.04.

**Standard error.** A benchmark score is a proportion, so the binomial standard error of [the evaluation chapter](#evaluation) applies:

$$\text{SE} = \sqrt{\frac{p(1-p)}{n}}$$

where $p$ is the model's true accuracy and $n$ the number of questions. <!-- D-009: code/checks/notation.py, Example 5 --> At $p$ = 0.8 on 164 questions, SE is 0.0312, and a 95% interval, 1.96 standard errors each side, is plus or minus 6.12 percentage points. [The toolkit chapter](#toolkit) writes the standard error of a mean as $\sigma/\sqrt{n}$, where $\sigma$ is the standard deviation of a single observation; for a proportion, that standard deviation is $\sqrt{p(1-p)}$.

Used in: [the destination chapter](#destination), [the prediction chapter](#prediction), [the chapter on training](#training), [the generation chapter](#generation), [the chapter on instructions](#instructions), and [the evaluation chapter](#evaluation).

## Softmax and temperature

A model ends with one score per token, any real number, called a **logit** in many papers. The **softmax** turns a list of scores into a probability distribution:

$$p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$$

where $z_i$ is the score of item $i$, $e$ is the base of the natural logarithm, the sum in the denominator runs over every item $j$, and $p_i$ is the resulting probability of item $i$. It is the last step of multinomial logistic regression.

<!-- D-009: code/checks/notation.py, Example 6 --> The destination chapter's example:

| Token | Score | $e^{\text{score}}$ | Probability |
|---|---:|---:|---:|
| mat | 3.0 | 20.086 | 0.571 |
| floor | 2.0 | 7.389 | 0.210 |
| sofa | 1.5 | 4.482 | 0.127 |
| roof | 1.0 | 2.718 | 0.077 |
| dog | -1.0 | 0.368 | 0.010 |
| the | -2.0 | 0.135 | 0.004 |
| Total | | 35.178 | 1.000 |

Table: The softmax of the destination chapter's six scores.

Four properties come up again and again. The order of the scores is kept. A score higher by one makes an item $e$ times, about 2.718 times, as probable: "mat" against "floor". <!-- D-009: code/checks/notation.py, Example 6 --> Adding the same number to every score changes nothing (adding 10 to all six gives the same probabilities), so only differences between scores matter. And no item gets probability exactly zero unless its score is minus infinity, which is how a **mask** excludes positions in [the attention chapter](#attention) and [the anatomy chapter](#anatomy): scores of 1, 2, and minus infinity give weights of 0.269, 0.731, and 0.

**Temperature.** Dividing every score by a number $T$, the **temperature**, before the softmax reshapes the distribution:

$$p_i = \frac{e^{z_i / T}}{\sum_j e^{z_j / T}}$$

with the symbols as before. $T = 1$ is the plain softmax; a lower $T$ sharpens the distribution and a higher one flattens it, never changing the order. <!-- D-009: code/checks/notation.py, Example 6 --> On the scores above, "mat" gets 0.831 at $T = 0.5$, 0.571 at $T = 1$, and 0.375 at $T = 2$, and the entropy rises from 0.86 bits to 1.70 to 2.23, against 2.58 bits for six equally likely tokens.

**Softmax of two scores.** With only two items, the softmax depends only on the difference of the scores, and it is the logistic function of the next section applied to that difference. <!-- D-009: code/checks/notation.py, Example 6 --> The two router scores of 2.1 and 1.7 in [the chapter on the transformer since 2017](#since-2017) give weights of 0.599 and 0.401, and the logistic function of 2.1 - 1.7 = 0.4 is 0.599.

Used in: [the destination chapter](#destination), [the chapter on sequences](#seq2seq), [the attention chapter](#attention), [the anatomy chapter](#anatomy), [the generation chapter](#generation), and [the chapter on the transformer since 2017](#since-2017).

## The logistic function

The **logistic function**, or **sigmoid**, squashes any number into the range between 0 and 1:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

where $z$ is any real number, $e$ is the base of the natural logarithm, and $\sigma(z)$ is the result. <!-- D-009: code/checks/notation.py, Example 7 --> Some values: $\sigma(-2)$ = 0.119, $\sigma(-1)$ = 0.269, $\sigma(0)$ = 0.5, $\sigma(1)$ = 0.731, $\sigma(2)$ = 0.881. It is symmetric: $\sigma(-z) = 1 - \sigma(z)$, so 1 - 0.731 = 0.269. It is the link function of the reader's logistic regression and the activation of [the neuron chapter](#neuron), where the vote's weighted sum of 0.1 gives 0.525.

Its inverse is the **log-odds**: a probability $p$ corresponds to $z = \ln\big(p / (1 - p)\big)$, where $\ln$ is the natural logarithm. <!-- D-009: code/checks/notation.py, Example 7 --> A probability of 0.731 has odds of 0.731 to 0.269, which is 2.718 to 1, and log-odds of 1.000.

The chapters use it in four more places:

- **Comparing two scores.** The Bradley-Terry model of [the chapter on instructions](#instructions) gives the probability that response A is preferred to response B as $\sigma(r_A - r_B)$, the logistic function of the difference of their scores. Its training loss, the **log loss**, is minus the natural logarithm of the probability given to the response actually preferred. <!-- D-009: code/checks/notation.py, Example 7 --> With a score difference of 1 in the right direction it is $-\ln 0.731$ = 0.313; with no difference, 0.693.
- **Elo ratings.** [The evaluation chapter](#evaluation)'s Arena scores use the same curve with powers of 10 and a scale of 400 points. <!-- D-009: code/checks/notation.py, Example 7 --> A 400-point gap gives a win probability of 0.909, odds of 10 to 1; one unit on the natural log-odds scale is 400 divided by the natural log of 10, or 173.7 Elo points.
- **Gates.** The LSTM of [the chapter on networks with structure](#structure) and the SwiGLU layer of [the chapter on the transformer since 2017](#since-2017) use sigmoids as soft switches between 0 and 1. The **Swish** function there is $x\,\sigma(x)$, a number times its own sigmoid.
- **Task horizons.** [The frontier chapter](#frontier) fits a logistic regression of success on the logarithm of task length.

Two other activation functions appear alongside it. The **ReLU** of [the deep learning chapter](#deep-turn), $\max(0, z)$, keeps positive numbers and replaces negative ones with zero. The **tanh**, a stretched sigmoid, runs from -1 to 1.

## Symbols used in the book

Each symbol is listed with each meaning it has in the book and the chapter where that meaning first appears, in reading order. The same letter often means different things in different chapters, because the book keeps each source's notation; the chapter text always says which meaning is in force.

| Symbol | Meaning | First used |
|----------|------------------------------|--------|
| $A$ | the sounds a speech recognizer observes | [prediction](#prediction) |
| $A$ | LoRA's small $r \times k$ matrix | [adapting](#adapting) |
| $A_i$ | advantage: answer $i$'s reward as a z-score within its group | [frontier](#frontier) |
| $a$, $b$ | two vectors being compared | [embeddings](#embeddings) |
| $a_i$, $\bar{a}_i$ | entry $i$ of a vector, before and after normalization | [since-2017](#since-2017) |
| $B$ | LoRA's tall $d \times r$ matrix | [adapting](#adapting) |
| $B$ | memory bandwidth, in bytes per second | [local](#local) |
| $b$ | bias of a neuron ($b_1$, $b_2$: bias vectors of a layer) | [neuron](#neuron) |
| $b$, $k_1$ | the two settings of BM25 | [tools](#tools) |
| $b$ | bits stored per parameter | [local](#local) |
| $C$ | training compute, in floating-point operations | [scale](#scale) |
| $D$ | number of training tokens | [scale](#scale) |
| $d$ | dimension of a vector (model width; size of an attention head) | [attention](#attention) |
| $d_k$ | number of numbers in each key | [attention](#attention) |
| $d_{\text{model}}$ | width of the residual stream | [anatomy](#anatomy) |
| $d$ | number of rows of a weight matrix | [adapting](#adapting) |
| $d$ | a document | [tools](#tools) |
| $d$ | difference between two Arena scores | [evaluation](#evaluation) |
| $d$ | elapsed time in days | [frontier](#frontier) |
| $\text{df}_t$ | number of documents containing word $t$ | [tools](#tools) |
| $dl$, $avdl$ | a document's length, and the average length | [tools](#tools) |
| $E_i(x)$ | output of expert $i$ | [since-2017](#since-2017) |
| $e$ | base of the natural logarithm, about 2.718 | [destination](#destination) |
| $F(x)$ | the correction a residual block adds | [depth](#depth) |
| $f(z)$ | output of a ReLU | [deep-turn](#deep-turn) |
| $G$ | number of answers in a group | [frontier](#frontier) |
| $G(x)_i$ | the router's weight on expert $i$ | [since-2017](#since-2017) |
| $g(t)$ | new value offered to an LSTM cell at step $t$ | [structure](#structure) |
| $g_i$ | learned gain in RMS normalization | [since-2017](#since-2017) |

Table: Symbols, Latin letters A to G.

| Symbol | Meaning | First used |
|----------|------------------------------|--------|
| $H$ | entropy, or cross-entropy, in bits | [prediction](#prediction) |
| $H$, $H_0$ | time horizon after $d$ days, and at the start | [frontier](#frontier) |
| $h$ | a layer's output vector | [adapting](#adapting) |
| $h$ | a model's time horizon | [frontier](#frontier) |
| $i$, $j$ | index counting tokens, outcomes, or entries | [destination](#destination) |
| $i(t)$ | input gate of an LSTM cell at step $t$ | [structure](#structure) |
| $k_j$ | key of token $j$ | [attention](#attention) |
| $k$ | number of columns of a weight matrix | [adapting](#adapting) |
| $k$, $k!$ | number of examples, and its factorial | [prompting](#prompting) |
| $L$ | loss; $L(N)$, loss as a function of model size | [backprop](#backprop) |
| $L$ | largest integer allowed in quantization | [local](#local) |
| $M$ | bytes read per generated token | [local](#local) |
| $m$ | ALiBi's slope for one attention head | [since-2017](#since-2017) |
| $N$ | number of words or tokens in a text | [prediction](#prediction) |
| $N$ | number of parameters | [anatomy](#anatomy) |
| $N_c$, $\alpha_N$ | fitted constants of a scaling law | [scale](#scale) |
| $N$ | number of documents in a collection | [tools](#tools) |
| $N$ | number of disks in the Tower of Hanoi | [frontier](#frontier) |
| $n$ | number of inputs to a neuron | [neuron](#neuron) |
| $n$ | number of samples (later, of benchmark questions) | [toolkit](#toolkit) |
| $n$ | number of units that dropout can remove | [depth](#depth) |
| $n$ | the $n$ of n-gram | [prediction](#prediction) |
| $n$ | number of tokens in a sequence | [attention](#attention) |
| $n$ | length of a vector; number of experts | [since-2017](#since-2017) |
| $n_{\text{layer}}$ | number of transformer blocks | [anatomy](#anatomy) |
| $P(\ldots)$ | probability of what is in the brackets | [prediction](#prediction) |
| $P$ | probability that the higher-rated model wins | [evaluation](#evaluation) |
| $PP$ | perplexity | [prediction](#prediction) |
| $p_i$ | probability of token or outcome $i$ | [destination](#destination) |
| $p$ | a probability: of keeping or dropping a unit; a softmax weight; a true accuracy; a chance of success | [depth](#depth) |

Table: Symbols, Latin letters H to P.

| Symbol | Meaning | First used |
|----------|------------------------------|--------|
| $q$ | query vector | [attention](#attention) |
| $q_i$ | integer stored for weight $i$ | [local](#local) |
| $R(x, y)$ | reward after the KL penalty | [instructions](#instructions) |
| $r(x, y)$; $r_A$, $r_B$, $r_w$, $r_l$ | reward model's scores | [instructions](#instructions) |
| $r$ | rank of a LoRA update | [adapting](#adapting) |
| $r_i$ | reward of answer $i$ | [frontier](#frontier) |
| $\text{RMS}(\mathbf{a})$ | root mean square of a vector's entries | [since-2017](#since-2017) |
| $s(t)$ | value stored in an LSTM cell at step $t$ | [structure](#structure) |
| $s$ | scale shared by a group of quantized weights | [local](#local) |
| $\text{SE}$ | standard error | [evaluation](#evaluation) |
| $T$ | temperature | [generation](#generation) |
| $T$ | doubling time in days | [frontier](#frontier) |
| $t$ | time step | [structure](#structure) |
| $t$ | confidence threshold | [prompting](#prompting) |
| $t$ | a word (term) | [tools](#tools) |
| $t$ | time a task takes a skilled human | [frontier](#frontier) |
| $\text{tf}_{t,d}$, $tf$ | term frequency | [tools](#tools) |
| $V$ | second input matrix of a SwiGLU layer | [since-2017](#since-2017) |
| $v_j$ | value of token $j$ | [attention](#attention) |
| $W$ | the words a speaker chooses (with $A$) | [prediction](#prediction) |
| $W$, $W_1$, $W_2$ | weight matrices | [anatomy](#anatomy) |
| $W_0$, $\Delta W$ | a pretrained matrix, and a change to it | [adapting](#adapting) |
| $W_g$ | the router's weights | [since-2017](#since-2017) |
| $w$, $w_i$ | a weight; weight $i$ | [neuron](#neuron) |
| $w_1 \ldots w_N$ | the words of a text | [prediction](#prediction) |
| $w_i$, $w_i^{\text{RSJ}}$ | BM25 weight of query word $i$, and its inverse-document-frequency part | [tools](#tools) |

Table: Symbols, Latin letters Q to W.

| Symbol | Meaning | First used |
|----------|------------------------------|--------|
| $x$, $x_i$ | input; input $i$; one position's vector | [neuron](#neuron) |
| $x$, $y$ | a prompt and a response | [instructions](#instructions) |
| $y$ | output | [backprop](#backprop) |
| $z$ | weighted sum of a neuron | [neuron](#neuron) |
| $z_i$ | score (logit) of token $i$ | [destination](#destination) |
| $\alpha$ | momentum setting | [toolkit](#toolkit) |
| $\beta$ | strength of the KL penalty | [instructions](#instructions) |
| $\beta$ | fitted slope of a logistic regression | [frontier](#frontier) |
| $\Delta$ | a change in a quantity | [instructions](#instructions) |
| $\eta$ | learning rate | [backprop](#backprop) |
| $\theta_i$ | rotation per position of pair $i$ in RoPE | [since-2017](#since-2017) |
| $\pi(y \mid x)$ | a model's probability of response $y$ to prompt $x$ | [instructions](#instructions) |
| $\sigma(z)$ | logistic function | [neuron](#neuron) |
| $\sigma$ | standard deviation | [toolkit](#toolkit) |
| $\sum_j$ | sum over $j$ | [destination](#destination) |
| $a \cdot b$ | dot product (in two chapters, plain multiplication) | [embeddings](#embeddings) |
| $\lVert a \rVert$ | length of a vector | [embeddings](#embeddings) |
| $\otimes$ | entry-by-entry product | [since-2017](#since-2017) |
| $\log_2$, $\log_{10}$ | logarithm to base 2, to base 10 | [prediction](#prediction), [tools](#tools) |
| $\log$ | natural logarithm | [instructions](#instructions) |
| $\partial L / \partial w$ | derivative of the loss with respect to $w$ | [backprop](#backprop) |
| $\leftarrow$ | "replace with" | [backprop](#backprop) |
| $\max(0, z)$ | ReLU | [deep-turn](#deep-turn) |
| $\mid$ | "given" | [instructions](#instructions) |
| $\approx$ | approximately equal | [anatomy](#anatomy) |
| $\lvert w \rvert$; round | absolute value; nearest integer | [local](#local) |

Table: Symbols, Latin letters X to Z, Greek letters, and operators.
