# The destination: an LLM in one picture {#destination}

<!-- D-002: intuition only; the one formula (softmax) follows its worked example. D-003: no code. D-008: destination first. D-009: numbers from code/checks/destination.py. D-014: figure from figures/pipeline.py. -->

Open a chat assistant, type a question, and a few seconds later a fluent answer appears, a word or so at a time. This book explains what happens in those few seconds and how the field arrived there. The explanation takes many chapters and reaches back to the first artificial neuron. Before it starts, this chapter shows you the whole machine at low resolution: every part named, none explained in depth. Each later chapter enlarges one part of the picture drawn here. When a later chapter feels like a detour, come back to this picture to see where you are.

The short version fits in two sentences. A large language model (LLM) is a program that reads a piece of text and computes, for every possible next piece of text, the probability that it comes next. To generate text, it picks one piece, appends it to the text, and does the same thing again.

The rest of the book is detail about those two sentences: what "a piece of text" is, how the probabilities are computed, where the program's numbers come from, and how a machine that only continues text came to answer questions.

## A classifier you already know

Start with something familiar. Multinomial logistic regression, also called softmax regression, takes a vector of features and outputs a probability for each of several classes. It computes one score per class, a weighted sum of the features, and then turns the scores into probabilities that are all positive and add up to one.

Now make three changes to it.

First, let the classes be the entries of a vocabulary: a fixed list of pieces of text, called **tokens**, that the model knows. GPT-2, a model OpenAI described in 2019, had a vocabulary of 50,257 tokens [@radford2019language, p. 4]. Llama 3.1, a family of models Meta published in 2024, has 128,000 [@grattafiori2024llama, p. 7]. So the classifier has tens of thousands of classes, or more than a hundred thousand, one per token.

Second, let the input be the text so far, and let the question always be the same: which token comes next? Training examples then come from ordinary text. Take any position in any document: the text before it is the input, and the token at that position is the correct class. Nobody has to label anything, because the text labels itself. This is called **self-supervised learning**, and it is the reason these models can learn from enormous amounts of text.

Third, do not design the features by hand. In the 2000s, much of the work of building a text classifier was choosing features: word counts, n-grams, hand-built indicators. In an LLM, the features that feed the final scoring step are computed by a large network whose numbers are learned along with everything else. Most of the model is this feature computation.

Finally, use the classifier repeatedly. Predict a next token, append it to the text, and predict again with the longer text as input. Writing a paragraph means running the classifier once for every token in it.

That gives the bridge from what you know: **an LLM is a very large classifier over a vocabulary, with learned features, applied again and again to its own output.** The description leaves a great deal out, and later chapters fill it in, but nothing in them will contradict it.

## A language model assigns probabilities to text

In its older and more general sense, a **language model** is anything that assigns a probability to a piece of text. The idea is much older than neural networks; [the chapter on prediction](#prediction) traces its history.

There is a standard way to get the probability of a whole text from next-token predictions. Take the probability of the first token, multiply by the probability of the second token given the first, then by the probability of the third given the first two, and so on to the end. The GPT-2 paper writes the probability of a text in exactly this form and cites work from 1980 and 2003 for it [@radford2019language, p. 2].

Here it is with made-up probabilities for a six-token text.

<!-- D-009: code/checks/destination.py, Example 2 -->

| Next token | Given the text so far | Probability | Running product |
|:---|:---|---:|---:|
| The | (start of text) | 0.040 | 0.04 |
| cat | The | 0.010 | 0.0004 |
| sat | The cat | 0.150 | 0.00006 |
| on | The cat sat | 0.400 | 0.000024 |
| the | The cat sat on | 0.600 | 0.0000144 |
| mat | The cat sat on the | 0.571 | 0.0000082 |

Table: The probability of a short text as a chain of next-token predictions. The probabilities are invented; the products are computed.

Two things are worth noticing. The probability of any particular text is tiny and shrinks with every token, which is expected: there is an astronomical number of possible texts, and they share a total probability of one. And a model that produces good next-token probabilities can do two different jobs. It can score a given text, by multiplying down the column as above. Or it can generate a new text, by choosing a token at each row instead of being given one. A chat assistant uses the second job.

## The pipeline, box by box

![The pipeline of a large language model at low resolution. Text is cut into tokens, tokens become vectors, the layers update the vectors, the output layer scores every entry in the vocabulary, the scores become probabilities, and one token is picked and appended to the text. Shaded boxes contain learned parameters. The token IDs are the ones GPT-2's tokenizer gives this text. The probabilities match the worked example in this chapter, and the last box shows the most probable token; the text also shows a random draw.](../../figures/pipeline-destination.svg){#fig:destination-pipeline}

This figure returns throughout the book, with one box enlarged at a time. Follow it from the top left.

**Text.** The input is the text so far. In a chat, that is the conversation up to this point. In the figure, it is "The cat sat on the".

**Tokens.** The text is cut into tokens. A token is often a whole common word, and sometimes a piece of a rarer word, a punctuation mark, or a word with the space before it attached. The cutting is done by a separate procedure, the **tokenizer**, which is fixed before the model is trained. Why not use whole words? Because any fixed list of words eventually meets a word it does not contain, while pieces can spell anything. Why not single characters? Because texts would become very long sequences. Tokens are a compromise between the two, and the compromise has side effects. [The chapter on tokens](#tokens) covers how a vocabulary is built and what follows from it.

**Token IDs.** Every token in the vocabulary has a number, its position in the list. From this point on, the model never sees text, only these numbers. (The IDs in the figure are the ones GPT-2's tokenizer gives "The cat sat on the"; [the chapter on tokens](#tokens) shows how they arise.)

**Vectors.** Each token ID selects one row of a large table, the **embedding table**. A row is a **vector**: a list of numbers, from a few hundred to more than ten thousand long. OpenAI's 2018 GPT model turned each token into 768 numbers [@radford2018improving, p. 5]; the largest GPT-2 used 1,600 [@radford2019language, p. 4]; the largest Llama 3.1 uses 16,384 [@grattafiori2024llama, p. 7]. These vectors are called **embeddings**. Each token's vector is also combined with information about its position in the text, because the layers that follow would otherwise have no sense of word order; in the 2018 GPT model this is a second table, of position vectors [@radford2018improving, p. 3]. Before training, the vectors in these tables are random. Training moves them, and [the chapter on embeddings](#embeddings) shows how tokens that are used in similar ways end up with similar vectors.

Why turn an ID into a vector at all? An ID is only a name: token 3797 is no more like token 3798 than like token 7. A vector can express resemblance as closeness, so what the model learns about one token can carry over to tokens with nearby vectors. If you know latent semantic analysis, this is the same move as replacing a word by its coordinates in a reduced space, except that the coordinates are learned for the task of prediction rather than computed from a co-occurrence matrix.

**Layers.** The vectors then pass through a stack of layers, which is where most of the computation happens. In OpenAI's GPT models, and in later models such as Llama 3.1, the layers are **transformer** blocks [@radford2018improving, p. 3; @grattafiori2024llama, p. 1], a design published in 2017 that is built on a mechanism called attention [@vaswani2017attention, p. 10]. Each block does two things. First, the vector at every position gathers information from the vectors at its own position and the positions before it; this is attention, and it is how information about "cat" and "sat" can reach the position of "the". Second, each vector is processed on its own by a small network. The block's output is a new vector for every position, the same length as before, and the next block continues from there. The largest GPT-2 stacked 48 blocks [@radford2019language, p. 4]. After the last block, the vector at the final position carries what the model has computed about what should come next. [The chapter on attention](#attention) and [the chapter on the transformer's anatomy](#anatomy) open this box.

**Scores.** The output layer takes that final vector and computes one score for every entry in the vocabulary: 50,257 scores for GPT-2. The raw scores are called **logits**. This is the logistic regression step from the start of the chapter, a weighted sum per class.

**Probabilities.** The scores are turned into probabilities. Here is the computation on a toy vocabulary of six tokens, with made-up scores for the next token after "The cat sat on the". A real model would score every token in its vocabulary.

<!-- D-009: code/checks/destination.py, Example 1 -->

| Token | Score | e raised to the score | Probability |
|:---|---:|---:|---:|
| mat | 3.0 | 20.086 | 0.571 |
| floor | 2.0 | 7.389 | 0.210 |
| sofa | 1.5 | 4.482 | 0.127 |
| roof | 1.0 | 2.718 | 0.077 |
| dog | -1.0 | 0.368 | 0.010 |
| the | -2.0 | 0.135 | 0.004 |
| **Total** | | **35.178** | **1** |

Table: From scores to probabilities on a toy vocabulary. The scores are invented; everything else is computed. The probabilities shown add up to 0.999 only because of rounding.

Each score is passed through the exponential function, which makes every value positive and keeps the order. Each result is then divided by the total, so the values add up to one. Two consequences are worth seeing in the numbers. A score that is higher by one makes a token about 2.7 times as likely: "mat" (0.571) against "floor" (0.210). And no token ever gets a probability of exactly zero; even "dog" keeps one percent.

This is the **softmax** function, the same one that ends multinomial logistic regression. Written in its standard form:

$$p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$$

Here $z_i$ is the score of token $i$, $e$ is the base of the natural logarithm (about 2.718), the sum in the denominator runs over every token $j$ in the vocabulary, and $p_i$ is the resulting probability of token $i$.

**Pick one.** The model's work ends with the probabilities. Choosing a token from them is a separate step, called **sampling**. The simplest rule is to take the most probable token, "mat". A common alternative is to draw at random in proportion to the probabilities. Line the tokens up as bands on a ruler from 0 to 1: "mat" covers 0 to 0.571, "floor" from 0.571 to 0.781, "sofa" from 0.781 to 0.908, and so on. Draw a random number between 0 and 1 and take the token whose band it lands in. A draw of 0.80 lands in the band for "sofa", so this time the model writes "sofa". The random draw is why the same question can get different answers. Settings such as temperature reshape the probabilities before the draw; [the chapter on generation](#generation) covers them.

**Append and repeat.** The picked token is appended to the text, and the whole pipeline runs again on "The cat sat on the sofa" to choose the token after that. This continues until the model picks a special token reserved to mean "end of text", or until a length limit is reached. Every new token needs its own pass through every layer. Producing text this way, one token at a time with each one fed back as input, is called **autoregressive** generation; the GPT-3 paper describes GPT-3 as "an autoregressive language model" [@brown2020language, p. 1].

**The context window.** A model can take only a limited number of tokens as input at once. That limit is its **context window**: 1,024 tokens for GPT-2 [@radford2019language, p. 4], 2,048 for GPT-3 [@brown2020language, p. 8], and up to 128K for Llama 3.1, where K means 1,024, so 131,072 tokens [@grattafiori2024llama, pp. 3, 10]. Text beyond the window does not reach the model at all. In a chat, the context window is the model's entire working memory: any instructions, the conversation so far, any documents pasted in, and the reply being written must all fit inside it.

## Parameters: what is learned

The shaded boxes in the figure contain the model's **parameters**: numbers that are set by training. They are the rows of the embedding table, the weights inside every layer, and the weights of the output layer. The arrangement of the boxes, called the **architecture**, is chosen by the model's designers and does not change. Training fills in the numbers. In regression terms, the architecture is the form of the model and the parameters are its coefficients. Parameters are also called **weights**, and the two words are often used interchangeably.

The "large" in "large language model" refers to the number of parameters. The largest GPT-2 had 1.5 billion [@radford2019language, p. 1]. GPT-3 had 175 billion [@brown2020language, p. 1]. Llama 3.1 comes in versions with 8, 70, and 405 billion [@grattafiori2024llama, p. 2]. There is no official threshold at which a language model becomes large.

To make those counts concrete, multiply them by the space each parameter takes. A number stored in 32 bits takes 4 bytes; in 16 bits, 2 bytes.

<!-- D-009: code/checks/destination.py, Example 3 -->

| Model | Parameters | At 32 bits each | At 16 bits each |
|:---|---:|---:|---:|
| GPT-2 (largest) | 1.5 billion | 6 GB | 3 GB |
| Llama 3.1 8B | 8 billion | 32 GB | 16 GB |
| GPT-3 | 175 billion | 700 GB | 350 GB |
| Llama 3.1 405B | 405 billion | 1,620 GB | 810 GB |

Table: Storage needed for the parameters alone (1 GB is a billion bytes). This is arithmetic on the published parameter counts, not a statement about how any of these models was actually stored or run.

That is the space for the parameters alone, before any working memory needed to run the model. [The chapter on local inference](#local) shows how models are made to fit on ordinary computers by storing each parameter in fewer bits.

## Training and inference

A model's life has two phases.

**Training** sets the parameters. The model is shown text, and at every position it computes probabilities for the next token. These are compared with the token that actually comes next, and every parameter is adjusted slightly in the direction that would have made the actual token more probable. This is repeated over an enormous amount of text: 300 billion tokens for GPT-3 [@brown2020language, p. 8] and 15.6 trillion for the largest Llama 3.1 [@grattafiori2024llama, p. 3]. The number that measures how wrong the predictions were is called the **loss**; [the chapter on prediction](#prediction) introduces the standard one. The method that works out the adjustment for every parameter at once is backpropagation, the subject of [the chapter on learning in layers](#backprop). This first, general phase is called **pretraining**, and its result is a **base model**. Pretraining takes a very large amount of computation, and it is done rarely.

**Inference** is using the trained model: running the pipeline in the figure to produce text. During inference the parameters do not change. A model does not learn from a conversation the way it learned during training. Whatever it "knows" about the conversation is the text in its context window, and nothing else. One consequence is that the parameters contain nothing from after the text the model was trained on, a limit discussed in [the chapter on knowledge and tools](#tools).

If you have used the fit-then-predict workflow of a 2000s statistics package, this split is familiar: fit rarely, at great cost, and then predict many times, cheaply by comparison.

## The model and the product

A base model is good at one thing: continuing text in a way that resembles its training data. That is not the same as being an assistant. The Llama 3 paper says so directly: "The pre-trained language model has a rich understanding of language but it does not yet follow instructions or behave in the way we would expect an assistant to" [@grattafiori2024llama, p. 3]. Given a question, a base model may continue with whatever plausibly follows such a question in its training text, which might be an answer, or might be more questions.

A second phase of training closes the gap. The model is trained further on examples of instructions paired with good responses written by people, and then on human judgments of which responses are better. The InstructGPT paper of 2022 laid this out as three steps: supervised fine-tuning, which is further training on demonstrations of good responses; training a separate reward model to predict which responses people rank higher; and reinforcement learning against that reward model, which means adjusting the model to produce responses the reward model scores well, rather than copying given answers [@ouyang2022training, p. 3]. [The chapter on following instructions](#instructions) explains each step. Its abstract opens with the motivation: "Making language models bigger does not inherently make them better at following a user's intent." In the paper's human evaluations, on its own collection of prompts, outputs from a 1.3-billion-parameter instruction-tuned model were preferred to outputs from the 175-billion-parameter GPT-3 [@ouyang2022training, p. 1]. The instruction-tuned model is still the same pipeline. Only its parameters have changed [@ouyang2022training, p. 3]. Even a conversation is just text to it: the turns are laid out as one document with markers for who is speaking, and the model continues that document from the point where the assistant's turn begins [@grattafiori2024llama, p. 16].

On 30 November 2022 OpenAI announced ChatGPT, describing it as "a sibling model to InstructGPT", fine-tuned (trained further, starting) from a model in what it called its GPT-3.5 series, and trained with reinforcement learning from human feedback, "using the same methods as InstructGPT, but with slight differences in the data collection setup" [@openai2022chatgpt].

The name points to a last distinction. A **chat product** is a model plus software around it: the interface, instructions written by the provider that the user does not see, rules about what to display, and possibly tools, such as a web search, that the software runs when the model's output asks for them. The same name is often used for both the product and the models behind it. When you read about an LLM, it helps to ask which one is meant: the parameters, or the system built around them.

## How the rest of the book fills in the picture

The book does not walk through the pipeline from left to right. It follows the history, because each part was invented to solve a problem left by the parts before it. The history runs in two threads that meet in the middle. <!-- D-008 -->

- **How networks learn.** [The artificial neuron](#neuron), [learning in layers](#backprop), [networks with structure](#structure), [the deep learning turn](#deep-turn), [the training loop](#toolkit), and [making deep networks trainable](#depth). These explain the shaded boxes: what a layer computes, and how training finds good parameters.
- **How language is modeled.** [Prediction](#prediction), [words as vectors](#embeddings), [reading and writing sequences](#seq2seq), and [tokens](#tokens). These explain the first boxes of the figure and the idea of next-token prediction itself. This thread steps back in time: it starts decades before the first thread ends.
- **The threads meet.** [Attention](#attention) and [the anatomy of a transformer](#anatomy) open the "Layers" box.
- **From transformer to LLM.** [Pretraining](#pretraining), [scale](#scale), [how an LLM is trained](#training), and [generating text](#generation).
- **From LLM to assistant.** [Following instructions](#instructions), [prompting and context](#prompting), [adapting a model](#adapting), and [knowledge and tools](#tools).
- **The working landscape.** [The transformer since 2017](#since-2017), [small models and local inference](#local), [measuring models](#evaluation), and [the frontier](#frontier).

The next chapter goes back to the first artificial neuron, long before there was enough text or computing power for anything in this chapter.

## What to carry forward

- An LLM computes a probability for every token in its vocabulary as the next token, picks one, appends it, and repeats.
- The pipeline: text, tokens, token IDs, vectors, layers, scores, probabilities, a picked token, and back to the text.
- The final step is the softmax of multinomial logistic regression, over tens or hundreds of thousands of classes.
- Parameters are the learned numbers inside the embedding table, the layers, and the output layer. "Large" means billions of them.
- Training sets the parameters, at great cost, before the model is used. Inference uses them, unchanged, for every token generated.
- A base model continues text. Further training on human demonstrations and preferences turns it into an assistant. A chat product is that model plus the software around it.
