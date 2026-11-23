# Language as prediction (1948-2000) {#prediction}

<!-- D-002: intuition only; formulas (entropy, cross-entropy, perplexity) follow worked examples. D-003: no code; Shannon's sequences are shown as a figure. D-008: first chapter of the language thread; it jumps back to 1948. D-009: numbers from code/checks/prediction.py. D-014: figures from figures/prediction.py. D-025: concepts first, few names, few quotations. D-026: credit questions in the credit appendix. -->

The chapters so far followed one thread: how networks learn. This chapter starts the second thread, how language is modeled, and it starts earlier, in 1948. The two threads meet at the transformer.

[The destination chapter](#destination) described an LLM as a machine that computes, for every possible next token, the probability that it comes next. This chapter shows that predicting the next piece of text is an old, well-defined statistical problem, much older than neural networks. For decades its standard solution was counting: tally which words follow which in a large body of text, and turn the tallies into probabilities. The chapter follows that solution from its origin to its limits, and along the way introduces the measure that LLMs are still trained on and, as of 2026, still evaluated by [@jurafsky2026speech, p. 9].

## 1948: text as a random process

In 1948, Claude Shannon published "A Mathematical Theory of Communication" in the Bell System Technical Journal. He set meaning aside from the start: "These semantic aspects of communication are irrelevant to the engineering problem" [@shannon1948mathematical, p. 379]. That was a statement about engineering, not a claim that meaning is unimportant. What mattered for sending messages efficiently was that text is not random: E is a more common letter than Q, and TH a more common pair than XP [@shannon1948mathematical, p. 385].

Shannon described a source of text as a machine that "will choose successive symbols according to certain probabilities depending, in general, on preceding choices" [@shannon1948mathematical, p. 385], and the first example of such a source on his list was written language, such as English. That is next-symbol prediction, stated as the definition of a text source, in 1948.

He then built a ladder of such machines, each one using more of the past, and showed what each one writes [@shannon1948mathematical, p. 388]. Here are four rungs, with letters chosen:

- independently and with equal probability: "XFOML RXKHRJFFJUJ ZLPWCFWKCYJ FFJEYVKCQSGXYD QPAAMKBZAACIBZLHJQD";
- depending on the one letter before ("digram structure as in English"): "ON IE ANTSOUTINYS ARE T INCTORE ST BE S DEAMY ACHIN D ILONASIVE TUCOOWE AT TEASONARE FUSO TIZIN ANDY TOBE SEACE CTISBE";
- depending on the two letters before ("trigram structure"): "IN NO IST LAT WHEY CRATICT FROURE BIRS GROCID PONDENOME OF DEMONSTURES OF THE REPTAGIN IS REGOACTIONA OF CRE";

and, switching from letters to words, with each word depending on the one before: "THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHARACTER OF THIS POINT IS THEREFORE ANOTHER METHOD FOR THE LETTERS THAT THE TIME OF WHO EVER TOLD THE PROBLEM FOR AN UNEXPECTED".

Each step, Shannon noted, looks clearly more like ordinary English than the one before, and in the last sample he judged a stretch of ten words, "attack on an English writer that the character of this", quite reasonable [@shannon1948mathematical, pp. 388-389].

These are the models of this chapter. A sequence of $n$ consecutive symbols is an **n-gram**: a **unigram** is one, a **bigram** two, a **trigram** three. A model that predicts the next symbol from the previous $n - 1$ is an n-gram model. (Shannon called the bigram model "second-order" and the trigram model "third-order". Other writers count differently, so this book avoids "order" and uses the n-gram names.) The mathematics was older still. In 1913, Markov used such chains to predict whether the next letter of Pushkin's *Eugene Onegin* would be a vowel or a consonant [@jurafsky2026speech, pp. 21-22].

Shannon made his samples without a computer. For the letter bigram sample, the method was this: open a book at random, pick a letter at random on the page, and write it down. Then open the book at another page, read until that letter turns up, and write down the letter that follows it [@shannon1948mathematical, p. 389]. A book read this way is a table of probabilities that nobody had to write down.

### Measuring uncertainty in bits

Shannon also gave the measure that this chapter needs: how uncertain is the next symbol?

<!-- D-009: code/checks/prediction.py, Example 4 -->

Start with something simpler than English. A fair coin has two equally likely outcomes, and its uncertainty is 1 **bit**. A coin that lands heads 90% of the time is less uncertain, 0.469 bits. A fair six-sided die is more uncertain: 2.585 bits. A loaded die that lands six half the time, and each other face a tenth of the time, is in between: 2.161 bits. This measure is the **entropy** of the outcome, and in its standard form it is

$$H = -\sum_i p_i \log_2 p_i$$

where $p_i$ is the probability of outcome $i$, the sum runs over all possible outcomes, and $\log_2$ is the logarithm to base 2, which makes the unit the bit. Each outcome contributes its probability times its "surprise", $-\log_2 p_i$: a likely outcome is unsurprising, a rare one very surprising. Entropy is the average surprise. Shannon showed that it is zero only when the outcome is certain, and largest when all the outcomes are equally likely [@shannon1948mathematical, p. 394]. The word "bit" is short for binary digit [@shannon1948mathematical, p. 380].

For English, counting structure over up to about eight letters, Shannon put its redundancy at roughly 50 percent: about half of a text is fixed by the structure of the language, and the other half is the writer's free choice [@shannon1948mathematical, pp. 398-399]. He linked redundancy to crossword puzzles. With none, any grid of letters at all would be a crossword; with too much, the constraints would be so tight that no large crossword could be built [@shannon1948mathematical, p. 399].

## 1951: the guessing game

Three years later Shannon measured the entropy of English in a different way, with a human as the model. The method put to work what speakers of English already know about its statistics, by asking a person to predict each next letter of a text from the letters before it [@shannon1951prediction, p. 50].

The procedure was a game. A person sees a passage they do not know, one letter at a time, and guesses each next letter. If the guess is right, they are told so and go on to the next letter; if not, they are told the correct letter and go on [@shannon1951prediction, p. 54]. Spaces count as a 27th letter.

![Shannon's 1951 guessing game, redrawn from his printed record. A subject guessed a passage one letter at a time. Letters on blue were guessed right on the first try; letters on red (in bold) were missed and then shown to the subject. The middle dot stands for a space. The misses cluster at the beginnings of words.](../../figures/prediction-shannon-game.svg){#fig:prediction-shannon-game}

<!-- D-009: code/checks/prediction.py, Example 6 -->

Of 129 letters, 89, or 69%, were guessed correctly. As Shannon expected, most of the misses came at the starts of words and syllables, the points where the text has the most ways to go on [@shannon1951prediction, p. 55]. Once "ROO" was known, "M" followed easily; once the "SH" of "SHABBY" had been given, "ABBY" followed.

Shannon then made an observation that connects prediction to compression. The second line of his record, the dashes and the missed letters, contains the whole passage, provided you have a predictor that guesses exactly the same way: "To accomplish this we need an identical twin of the individual who produced the sequence" [@shannon1951prediction, p. 55]. A good predictor and a good compressor are the same thing. The better the guesses, the fewer letters need to be written down.

In a second version of the game, the subject kept guessing until right, and Shannon recorded how many guesses each letter took. Of 102 symbols, the subject guessed 79 right on the first guess [@shannon1951prediction, p. 56]. In a larger experiment with 100 short samples from one book, the subject was shown the preceding letters and guessed the next one. Allowing for some random ups and downs, the first guess was right more often the more of the text was known; in a similar test with 100 letters of preceding text, it was right 80 times out of 100 [@shannon1951prediction, pp. 57-58].

Shannon first computed what tables of letter frequencies alone could give, for a 26-letter alphabet without the space. The entropy fell as more statistics were used: 4.70 bits per letter if all letters were equally likely, 4.14 using single-letter frequencies, 3.56 using pairs of letters, and 3.3 using triples [@shannon1951prediction, p. 54]. He could go no further by counting, because no tables of frequencies were available for sequences of more than three letters [@shannon1951prediction, p. 52]. From the guessing counts, with a human predictor and 100 letters of context, he derived bounds of between 0.6 and 1.3 bits per letter (for an alphabet that includes the space) [@shannon1951prediction, p. 64]. Shannon summarized the result as "something of the order of one bit per letter" [@shannon1951prediction, p. 50], and stressed that the sampling error in these figures, which came from one subject and one book, was still considerable [@shannon1951prediction, p. 64].

One sentence in the paper describes, in 1951, what an LLM is trained to do: "A machine or person guessing in the best way would guess letters in the order of decreasing conditional probability" [@shannon1951prediction, p. 58].

## Counting: the n-gram language model

In the standard textbook sense, a language model is a probability distribution over the next word: it gives each word that might come next a probability. The same model can also give a probability to a whole sentence [@jurafsky2026speech, p. 1]. [The destination chapter](#destination) showed how the two are connected: the probability of a whole sentence is the product of the next-word probabilities, each given everything before it.

The difficulty is "everything before it". No collection of text, however large, contains every sentence beginning someone might write. People keep writing things that have never been written before, so a given context may never have occurred at all [@jurafsky2026speech, p. 3]. The n-gram model's answer is to forget most of the past: predict each word from only the last one or two. This simplification is called the **Markov assumption** [@jurafsky2026speech, p. 3]. Then the probabilities can be estimated by counting. The probability of a word given the word before it is the number of times the pair occurs, divided by the number of times the first word occurs.

<!-- D-009: code/checks/prediction.py, Example 1 -->

Here is the counting on a three-sentence corpus from the same textbook, with markers for the start and end of each sentence: "I am Sam", "Sam I am", "I do not like green eggs and ham" [@jurafsky2026speech, p. 4]. Two of the three sentences start with "I", so the probability that a sentence starts with "I" is 2/3. "I" occurs three times, followed twice by "am" and once by "do", so the probability of "am" after "I" is 2/3 and of "do" after "I" is 1/3. A naive Bayes text classifier does exactly this counting, with the order of the words thrown away. An n-gram model is the same counting with the order kept.

A model like this can also write, the way Shannon's book-opening did: pick each next word at random according to its probability, using the "ruler" of [the destination chapter](#destination). The longer the context, the more the output resembles real text, up to a point. Trained on Shakespeare, a 4-gram model produces sentences that are partly Shakespeare's own: the words "It cannot be but so" are copied straight from *King John* [@jurafsky2026speech, p. 12]. With long contexts and a small corpus, the table memorizes its training text. This is overfitting.

## IBM and the noisy channel

Statistical models of language fell out of favor in linguistics after 1957. That year, Chomsky argued in *Syntactic Structures* that "Colorless green ideas sleep furiously" and "Furiously sleep ideas green colorless" have both, in all likelihood, never been written, so that "in any statistical model for grammaticalness, these sentences will be ruled out on identical grounds as equally 'remote' from English. Yet (1), though nonsensical, is grammatical, while (2) is not" (quoted in [@liberman2010obituary, p. 596]; Chomsky's book was not read for this chapter). An obituary of Fred Jelinek, written in 2010, describes the effect: the argument persuasively weakened the case for n-gram approximations as models of syntax, and by the time Jelinek went to IBM in 1972, "the Information Theory bandwagon of the 1950s was lying forgotten in a ditch", at least in speech and language work [@liberman2010obituary, p. 596]. The same account names a second cause beside Chomsky: artificial-intelligence researchers of the time were promoting the view of intelligence as applied logic [@liberman2010obituary, p. 596]. Chomsky's own case was also broader than one example: he argued that a finite-state Markov process might serve engineers as a rule of thumb but could never be a full model of what a person knows about grammar [@jurafsky2026speech, p. 22].

The two-sentence argument, at least, has a precise target, and this chapter will return to it: models that give every unseen sentence a probability of zero.

Statistics came back through speech recognition. A speech recognition group at IBM started in early 1972, and Jelinek took charge of it later that year [@jelinek2009dawn, p. 484]. They framed recognition as Shannon would have, as "transmission through a noisy channel": a speaker chooses words $W$, the channel turns them into sounds $A$, and the recognizer picks the words that are most probable given the observed sounds [@jelinek2009dawn, p. 487]. By Bayes' rule, that means choosing the $W$ that maximizes the product of two probabilities. One is the probability of the sounds given the words, the **acoustic model**. The other is the probability of the words themselves, the language model. This is the pattern of Bayesian classification: a likelihood times a prior. Here the prior is a language model. In the same years, a lab at Carnegie Mellon was also using n-grams in its speech recognizers [@jurafsky2026speech, p. 22]. Where the terms "language model" and "perplexity" (a measure this chapter defines below) came from, and how the two labs' work relates, is set out in [the credit appendix](#credit-prediction).

Around 1978, the IBM group decided to recognize natural speech with a 5,000-word vocabulary, and to model English by trigrams [@jelinek2009dawn, pp. 488-489]. In a 2004 talk, Jelinek recalled a line from a 1988 workshop talk of his: "Whenever I fire a linguist our system performance improves". He added that the line had pointed up a situation that existed in speech recognition in the 1970s and in natural language processing in the 1980s, and the 2004 talk itself was titled "Some of my Best Friends are Linguists" [@jelinek2004friends, slides 2-3]. (The line circulates in other wordings; this is Jelinek's own.)

The same equation went to translation. In 1990, a group at IBM proposed translating by choosing the sentence that maximizes the product of a language model probability and a translation probability [@brown1990statistical, p. 79]. They tested what a trigram model alone knows about word order with a game of their own: cut a sentence into its words, drop them into a bag, and ask the model to put the sentence back together. Of 38 short sentences, a trigram model recovered 24 (63%) exactly [@brown1990statistical, p. 80]. Translation returns in [the chapter on reading and writing sequences](#seq2seq).

## The trouble with counting: zeros

Counting has a fatal weakness, and the numbers show how severe it is.

<!-- D-009: code/checks/prediction.py, Example 5 -->

In 1992, a study counted word sequences in 366 million words of English, with a vocabulary of 260,741 [@brown1992class, p. 470]. With that vocabulary there are about 68 billion possible word pairs. Only 14,494,217 of them actually occurred, about one possible pair in 4,700. Of the 18 million billion possible triples, 75 million occurred. And from the rate of sequences seen only once, the authors estimated that counting would give a probability of zero to 14.7 percent of the trigrams in a new sample of English text [@brown1992class, p. 470]. One trigram in seven in new text would never have been seen, even after 366 million words.

<!-- D-009: code/checks/prediction.py, Example 7 -->

A single novel shows the same thing at a smaller scale. Jane Austen's *Pride and Prejudice*, in the Project Gutenberg edition and counting lowercased words, has 128,565 words with a vocabulary of 6,729. That allows 45,279,441 possible word pairs, of which 56,767 occur: 0.125% of the table is filled, and 99.87% is zero.

![A corner of the word-pair table for Pride and Prejudice, for ten words of middling frequency (ranked 201st to 210th). Each cell counts how often the row word is followed directly by the column word. 98 of the 100 cells are zero.](../../figures/prediction-sparse-counts.svg){#fig:prediction-sparse-counts}

A zero is not merely an inaccuracy. Since the probability of a sentence is a product, one zero makes the whole sentence impossible. A small example shows it. Train a bigram model on three sentences, "John read Moby Dick", "Mary read a different book", and "She read a book by Cher". The model gives "John read a book" a probability of 0.0556, and "Cher read a book" a probability of exactly zero, because "Cher read" never occurred [@chen1998empirical, p. 5]. In speech recognition the consequence was concrete: if the speaker said such a word sequence, the recognizer was bound to get it wrong [@jelinek2009dawn, p. 489]. The same problem arises in naive Bayes, where one word never seen with a class drives that class's probability to zero.

## Smoothing

The remedy is **smoothing**: take a little probability from events that were seen often and give it to events never seen [@jurafsky2026speech, p. 14]. The name comes from the effect: smoothing tends to even out a distribution, raising low probabilities, zeros included, and lowering high ones [@chen1998empirical, p. 5].

The simplest version adds one to every count before dividing, as in the Laplace correction used in naive Bayes. In the Cher example, with every word in the corpus and the end-of-sentence marker counted in the vocabulary, **add-one smoothing** gives "Cher read a book" a small probability, 0.0000209, instead of zero. <!-- D-009: Example 2 --> But it takes too much from the frequent events. In a textbook example from a restaurant-query corpus, the probability of "to" after "want" falls from 0.66 to 0.26 when one is added to the counts of all 1,446 words of the vocabulary. The drop is so sharp because the many zero counts, together, receive too much of the probability [@jurafsky2026speech, p. 16].

The better idea is to fall back on less context when the longer context has not been seen. If a trigram never occurred, use the bigram; if the bigram never occurred either, use the single word's frequency. One version mixes the estimates for all context lengths with weights chosen on held-out data, a form of shrinkage toward a simpler model [@jurafsky2026speech, p. 17]. The authors of that 1992 count stated the trade-off in terms of reliability: as n grows, an n-gram model becomes more accurate, but its estimates, which must come from a limited training text, become less reliable [@brown1992class, p. 470]. More context means less bias and more variance.

Another version, **back-off**, uses the longer context when it has been seen and backs off to a shorter one otherwise. In 1987 Slava Katz of IBM published a back-off method that set aside probability for unseen sequences according to how many sequences had been seen exactly once [@katz1987estimation, p. 400]. It is the same estimate that gave the 14.7% above.

The most effective idea came from Reinhard Kneser and Hermann Ney in 1995, and is now called **Kneser-Ney smoothing**. When backing off to a single word, do not ask how frequent the word is; ask in how many different contexts it appears. Their example: "dollars" is very frequent in Wall Street Journal text but appears nearly always right after a number or one of a few country names, so after a word it has never followed, it should get a low probability, however common it is [@kneser1995improved, p. 181]. The same point can be made with "Francisco", which appears almost only after "San" [@chen1998empirical, p. 15].

In 1998, Stanley Chen and Joshua Goodman compared the main smoothing methods across several corpora and training-set sizes, and found that Kneser-Ney smoothing and its variants beat every other method they tested, with their own modified version the best every time [@chen1998empirical, p. 59]. Around 2000 that modified version became the usual baseline against which new n-gram models were measured [@jurafsky2026speech, p. 22]. Their study was also a lesson in method: earlier studies had pitted only a few methods against each other, usually two, on one or two bodies of text at a single training-set size, which made it hard to choose among the methods with any confidence [@chen1998empirical, pp. 2, 6].

Smoothing also answers Chomsky's particular challenge, on its own terms. In 2000, a simple model that shares statistics among words of similar behavior, grouping words into 16 classes, was trained on newspaper text. It rated "Colorless green ideas sleep furiously" about 200,000 times more probable than "Furiously sleep ideas green colorless" [@pereira2000formal, p. 1245]. Chomsky's two-sentence argument holds against a model that gives every unseen sequence a probability of zero. It fails against a model that generalizes from similar words. (His broader claim, about what a complete model of grammar needs, is a different question.) That idea, sharing what is known about one word with similar words, is the subject of [the next chapter](#embeddings).

## Measuring a language model: cross-entropy and perplexity

How do you tell which of two language models is better? Give each one text it has not seen, and measure how surprised it is. A better model predicts upcoming words better, so each word of the test set surprises it less [@jurafsky2026speech, p. 9].

<!-- D-009: code/checks/prediction.py, Example 3 -->

Take a five-word text, "red red red red blue", and two models of a language with three color words. Model A thinks all three are equally likely, 1/3 each. Model B thinks red has probability 0.8, and green and blue 0.1 each [@jurafsky2026speech, pp. 10-11]. Model A's average surprise is 1.585 bits per word, and model B's is 0.922 bits: model B predicted the text better.

That average surprise is the **cross-entropy** of the model on the text. In its standard form, for a text of $N$ words,

$$H = -\frac{1}{N} \log_2 P(w_1 w_2 \ldots w_N)$$

where $P(w_1 w_2 \ldots w_N)$ is the probability the model gives the whole text (the product of its next-word probabilities), and dividing by $N$ makes it a per-word average. Lower is better.

Language modelers usually report it in another form. The **perplexity** is 2 raised to the cross-entropy:

$$PP = 2^{H}$$

It reads as the number of equally likely choices the model is, in effect, choosing among at each step. Model A's perplexity is exactly 3, since it really is choosing uniformly among three words. Model B's is 1.895. Perplexity can also be thought of as the "weighted average branching factor" of a language [@jurafsky2026speech, pp. 10-11]. The six-token text from [the destination chapter](#destination), with its made-up probabilities, has a cross-entropy of 2.815 bits per token and a perplexity of 7.04: on average, the model was as unsure as if it were choosing among about seven tokens.

Why "cross"? Because the surprise is measured with the model's probabilities, while the text comes from the true source. Return to the loaded die, whose true entropy is 2.161 bits. A model that wrongly believes the die is fair scores its rolls at 2.585 bits each. The extra 0.424 bits is the cost of the wrong model, and it is never negative: cross-entropy is lowest when the model's probabilities match the source's [@goodfellow2016deep, p. 73]. This is Shannon's identical twin in another form. In terms of compression, a model that gives a text probability $p$ can be turned into a code that writes the text in $-\log_2 p$ bits, so cross-entropy is the number of bits per word the model needs to encode the text [@chen1998empirical, p. 7].

Here is what the numbers looked like for n-grams. Trained on 38 million words of the Wall Street Journal and tested on 1.5 million more, a unigram model had a perplexity of 962, a bigram model 170, and a trigram model 109 [@jurafsky2026speech, p. 10]. Typical n-gram perplexities on English ranged from about 50 to almost 1,000, depending on the text [@chen1998empirical, p. 7]. Perplexities can be compared only between models that share a vocabulary [@jurafsky2026speech, p. 10], a point that matters in [the chapter on tokens](#tokens). Small differences mattered in practice: for speech recognition, Chen and Goodman found, on their data, a word-error rate about 5.4 percentage points lower for every bit of cross-entropy saved [@chen1998empirical, p. 58].

This is the measure promised in [the destination chapter](#destination). Neural networks are trained to minimize the same quantity. A 2016 deep learning textbook notes that most modern neural networks are trained by maximum likelihood, and that this amounts to minimizing the cross-entropy between the training data and the model's distribution [@goodfellow2016deep, p. 174]. The first GPT paper wrote its training objective as the sum of the log-probabilities of each token given the tokens before it [@radford2018improving, p. 3]. Its perplexity is still on the scoreboard: in 2019, GPT-2 reported a perplexity of 35.76 on a standard test set where the best earlier result was 46.54, without training on that data set at all [@radford2019language, p. 5]. (GPT-2 read the test text as bytes, through "invertible de-tokenizers", rather than with the earlier models' word vocabulary, so the comparison is less direct than it looks; see the caution above [@radford2019language, pp. 4-5].) As of 2026, perplexity is still used to evaluate large language models as well as n-gram models [@jurafsky2026speech, p. 9].

## Where counting breaks

By 2000, smoothed n-gram models were mature and well understood. They had two limits that no amount of smoothing could remove.

The first is size. A table of contexts grows as the vocabulary raised to the length of the context. Yoshua Bengio and colleagues put a number on it in 2003: to model the joint distribution of 10 consecutive words with a vocabulary of 100,000, there are potentially 100,000^10 - 1 = 10^50 - 1 free parameters [@bengio2003neural, p. 1137]. That is why practical models used n-grams of at most three to five words, that is two to four words of context, and most predictions used much less [@bengio2003neural, p. 1139]. This is the **curse of dimensionality**: the number of different combinations of values a set of variables can take grows exponentially as variables are added [@goodfellow2016deep, p. 152].

The second is that an n-gram model has no idea that words resemble each other. To it, "cat" and "dog" are as different as "cat" and "furiously". Bengio and colleagues gave the example that matters: having "The cat is walking in the bedroom" in the training text ought to help a model rate "A dog was running in a room" as almost as likely [@bengio2003neural, p. 1139]. A counting model gets no such help. An n-gram model can be seen as a kind of nearest-neighbor lookup in which any two different words are the same distance apart, so a training example helps only if it repeats the context word for word [@goodfellow2016deep, p. 458].

Shannon's 1951 subject did not have this problem. A person guessing the next letter knows that "cat" and "dog" are both animals. [The next chapter](#embeddings) is about how to give a model that kind of knowledge: by representing each word not as an entry in a table but as a point in a space, where similar words are close together.

## What to carry forward

- Predicting the next symbol of text is an old problem. Shannon posed it in 1948, and in 1951 measured how predictable English is by having a person guess letters: about one bit per letter with 100 letters of context, by his estimate.
- An n-gram model predicts each word from the previous one or two, with probabilities estimated by counting. It is naive Bayes counting with word order kept.
- Counts are mostly zero. Even in 366 million words, about one trigram in seven of new text had never been seen, and a single zero makes a whole sentence impossible.
- Smoothing moves probability to unseen events. The best methods back off to shorter contexts, and Kneser-Ney smoothing (as modified by Chen and Goodman) was the standard around 2000.
- Entropy is average surprise in bits. Cross-entropy is a model's average surprise on real text, and perplexity is 2 to that power: the effective number of choices at each step. LLMs are trained to minimize cross-entropy and, as of 2026, are still evaluated by perplexity.
- Counting fails in two ways: the table grows as the vocabulary to the power of the context length, and words are unrelated symbols, so nothing learned about "cat" helps with "dog".
