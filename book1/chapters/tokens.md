# Tokens: what the model actually sees (1994-2018) {#tokens}

<!-- D-002: intuition only; the only formula-like statement is "vocabulary = starting symbols + merges". D-003: no code; GPT-2's splitting pattern is described in words. D-009: numbers from code/checks/tokens.py. D-014: figures from figures/tokens.py. D-018: GPT-2's vocabulary files are downloaded and hash-checked, not committed. -->

[The destination chapter](#destination) said that an LLM never sees text, only a list of numbers, one per **token**, and that a token is "often a whole common word, and sometimes a piece of a rarer word". The last three chapters spoke of words as if the model read them. This chapter is about what it reads instead, how that list of pieces is built, and what follows from the choice: the price of using a model, the length of text it can take in, and some of its odder failures.

The reader knows "token" in an older sense: an occurrence of a word, as opposed to a **type**, a distinct word. "The cat saw the dog" has five tokens and four types. In this chapter, and in LLM writing generally, a token is one of the pieces a **tokenizer** cuts text into, and the **vocabulary** is the fixed list of possible pieces. Each piece in the vocabulary has a number, its **token ID**.

## The unknown-word problem

The models of the last three chapters had a vocabulary of whole words, and it had to be fixed in advance: the embedding table needs one row per word, and the output layer one score per word. Any word not on the list was replaced by a single "unknown" symbol, often written UNK. The reader will have done the same thing in a bag-of-words pipeline or an n-gram model.

For translation this was a real limit. Rico Sennrich, Barry Haddow, and Alexandra Birch put it plainly in 2015: "The vocabulary of neural models is typically limited to 30 000-50 000 words, but translation is an open-vocabulary problem" [@sennrich2016neural, p. 1715]. [The previous chapter](#seq2seq) showed what that cost: Bahdanau and colleagues' attention model matched the phrase-based system only on sentences without unknown words. Sennrich and colleagues looked at 100 rare words in their German training text and found that most could be translated in pieces: 56 were compounds, 21 names, 6 words borrowed from a common origin, and 5 built with a transparent prefix or suffix, such as English "sweetish" and German "süßlich" [@sennrich2016neural, p. 1716]. German compounds are the extreme case: their example, a word meaning "sewage treatment plant", is written as one word made of three parts, each common on its own [@sennrich2016neural, p. 1715].

## Words or characters

The obvious alternatives are characters. A vocabulary of characters is small and never meets an unknown word. The cost is length: the same text becomes a much longer sequence, and every extra step costs time and, for a recurrent network, more distance over which information has to travel. Sennrich and colleagues stated the tension: there are "strong incentives to minimize the vocabulary size of neural models to increase time and space efficiency", but "we also want a compact representation of the text itself, since an increase in text length reduces efficiency" [@sennrich2016neural, p. 1717].

<!-- D-009: code/checks/tokens.py, Example 7 -->

Their own counts on about 100 million words of German show the trade-off [@sennrich2016neural, p. 1720]. Split into words, the text has 1,750,000 distinct types, and the test set still contains 1,079 unknown words. Split into characters, it has 3,000 types and no unknowns, but 550 million tokens, 5.5 times as many. The 2000s tools the reader may know, such as splitting compounds by frequency or morphological analysis, "only moderately reduce vocabulary size, and do not solve the unknown word problem" [@sennrich2016neural, p. 1719]. The method this chapter is about gave 63,000 types, no unknowns, and 112 million tokens, only 12% more than whole words [@sennrich2016neural, p. 1720].

Characters do work, just slowly. In Google's 2016 translation system, a model that read and wrote single characters scored 38.01 BLEU on English to French, close to the best model's 38.95, but took 1.0530 seconds per sentence to translate against 0.2118 [@wu2016google, p. 16], about five times as long. "These models are rather slow to train and slow to use as the sequences are much longer" [@wu2016google, p. 16].

## Byte pair encoding

The method that won came from data compression. In 1994, Philip Gage published in *The C Users Journal* "a simple general-purpose data compression algorithm, called Byte Pair Encoding (BPE)" [@gage1994new]. The idea fits in one sentence: "replace common pairs of bytes by single bytes" [@gage1994new]. Find the most frequent pair of adjacent bytes, replace every occurrence with a byte value not used in the data, record the substitution in a table, and repeat.

<!-- D-009: code/checks/tokens.py, Example 1 -->

Gage's example is the string ABABCABCD. The most frequent pair is AB; replace it with an unused symbol X to get XXCXCD. Now XC is the most frequent pair; replace it with Y to get XYYD [@gage1994new]. The table of substitutions is enough to undo the process. Because a new symbol can itself be part of a later pair (Y stands for XC, which is ABC), the method "adapts exponentially to patterns": a run of 1,024 identical bytes "is reduced to a single byte after only ten pair substitutions" [@gage1994new]. Gage's aim was a small, fast decompressor. His algorithm had nothing to do with language.

In 2015, Sennrich and colleagues borrowed it: "We adapt byte pair encoding (BPE) (Gage, 1994), a compression algorithm, to the task of word segmentation" [@sennrich2016neural, p. 1716]. Their paper was first posted in August 2015 and published in 2016. The adaptation works on words instead of bytes, in two stages.

**Learning the merges.** Start with every word in the training text written as a sequence of characters, plus a special end-of-word marker. Count every pair of adjacent symbols, weighting each word by how often it occurs. Merge the most frequent pair into a new symbol everywhere, and record the merge. Repeat for a chosen number of merges [@sennrich2016neural, p. 1717]. Pairs are never counted across the boundary between two words [@sennrich2016neural, p. 1717]. The vocabulary is then the starting characters plus one new symbol per merge: "The final symbol vocabulary size is equal to the size of the initial vocabulary, plus the number of merge operations, the latter is the only hyperparameter of the algorithm" [@sennrich2016neural, p. 1717].

**Applying the merges.** To cut any word, new or old, split it into characters and replay the learned merges, in the order they were learned [@sennrich2016neural, p. 1718]. A word seen often in training ends up as one symbol. A rare word ends up as a few pieces. A word never seen at all still comes out as something, because in the worst case it stays as single characters. Nothing is unknown, except a character never seen in training.

<!-- D-009: code/checks/tokens.py, Examples 2 and 3 -->

Sennrich and colleagues printed a toy corpus in their paper: "low" 5 times, "lower" twice, "newest" 6 times, and "widest" 3 times [@sennrich2016neural, p. 1718]. The figure below runs ten merges on it. At the start, the eleven symbols are the ten letters that occur plus the end-of-word marker, written here as </w>. The pairs e+s, s+t, and t+</w> each occur 9 times (6 in "newest", 3 in "widest"). When pairs tie, this book's script takes the first one it meets, reading the words in order, so the first merge is e+s. Then es+t, then est+</w>, which makes "est at the end of a word" a single symbol. Then l+o and lo+w, which make "low", and so on. After ten merges, the vocabulary has 11 + 10 = 21 symbols.

![Ten BPE merges learned on the toy corpus printed by Sennrich and colleagues. Each row shows the pair merged, how often it occurred, and the corpus afterward; </w> marks the end of a word. Where pairs tie, the first one met is taken, so another tie-break would give a different but equally valid table. The last line applies the merges to "lowest", which is not in the corpus.](../../figures/tokens-bpe-merges.svg){#fig:tokens-bpe-merges}

Now apply the merges to "lowest", which the corpus does not contain. A vocabulary of the four training words would call it unknown. BPE cuts it into "low" and "est</w>", both learned pieces, and the model can use what it learned about each. "Slowest" becomes s, low, est</w>. The end-of-word marker is what keeps the "est" that ends a word apart from the "est" inside a word like "estate".

In translation, the gains were real but modest. Sennrich and colleagues' subword systems beat a word-level system with a back-off dictionary "by up to 1.1 and 1.3 BLEU" on English to German and English to Russian [@sennrich2016neural, p. 1715], with a clearer improvement on rare words [@sennrich2016neural, p. 1720]. A character-bigram system did as well on BLEU [@sennrich2016neural, p. 1720], and the authors called their choice of vocabulary size "somewhat arbitrary" [@sennrich2016neural, p. 1723]. What BPE offered was a fixed vocabulary of tens of thousands of pieces, no unknown words, and text barely longer than with whole words. The University of Edinburgh's attentional translation systems, which did well at the 2016 shared task of [the previous chapter](#seq2seq), were trained this way [@sennrich2016edinburgh, p. 371].

## Other recipes for the same idea

BPE has relatives, and the reader will meet their names.

**WordPiece** was developed at Google in 2012 by Mike Schuster and Kaisuke Nakajima for Japanese and Korean voice search, where words are not separated by spaces and the vocabulary is effectively unlimited [@schuster2012japanese, pp. 5149-5150]. It also starts from single characters and repeatedly joins two units, but it chooses the join "that increases the likelihood on the training data the most" under a language model, rather than the most frequent pair [@schuster2012japanese, p. 5150]. That language model was an n-gram model with Katz back-off [@schuster2012japanese, p. 5151], the machinery of [the prediction chapter](#prediction). So subword units first appeared in a pipeline the reader would recognize. Google's 2016 translation system used WordPiece, splitting "Jet makers feud" into "_J et _makers _fe ud", where "_" marks the start of a word, and found "a total vocabulary of between 8k and 32k wordpieces" worked well [@wu2016google, p. 7]. BERT, a model of a later chapter, used WordPiece with 30,000 tokens [@devlin2019bert, p. 4174].

The **unigram language model** method, from Taku Kudo in 2018, runs the other way: start from a large set of candidate pieces and repeatedly remove the ones whose loss hurts the fit least, until the vocabulary is the size wanted [@kudo2018subword, p. 68]. Each piece gets a probability, and a word can be cut in several ways, of which the most probable is used.

**SentencePiece**, by Kudo and John Richardson (2018), is a software tool, not a third algorithm: it implements both BPE and the unigram method [@kudo2018sentencepiece, p. 66]. Its contribution is to work on raw text without first splitting it into words, which matters for languages written without spaces. It treats the space as an ordinary symbol, written "▁", so that the original text can be restored exactly from the pieces [@kudo2018sentencepiece, p. 67].

## Bytes, not characters

One problem remained. "Characters" means the characters of every writing system: Latin, Cyrillic, Arabic, Chinese, emoji. A tokenizer that starts from characters must either include them all or call the rare ones unknown, and including them all would mean, in the GPT-2 authors' count, "a base vocabulary of over 130,000 before any multi-symbol tokens are added" [@radford2019language, p. 4].

<!-- D-009: code/checks/tokens.py, Example 6 -->

The way out is the byte. Text is stored on a computer in an encoding called **UTF-8**, which writes each character as a sequence of one to four bytes [@yergeau2003utf8, p. 4]. An English letter takes one byte; "привет", Russian for "hello", has 6 characters and 12 bytes; "東京", Tokyo, has 2 characters and 6 bytes; an emoji takes 4. There are only 256 possible byte values, and every text is a sequence of them.

OpenAI's GPT-2 (2019) built its tokenizer on bytes. Its authors noted that BPE implementations usually worked on Unicode characters, while "a byte-level version of BPE only requires a base vocabulary of size 256" [@radford2019language, p. 4]. Running BPE naively on bytes produced wasteful merges, such as separate tokens for "dog." "dog!" and "dog?", so they stopped merges from crossing between letters, digits, and punctuation, with an exception for spaces [@radford2019language, p. 4]. In the released code, text is first cut into pieces: a run of letters with an optional space in front, a run of digits with an optional space, a run of other symbols, and runs of spaces [@openai2019gpt2code]. BPE then works inside each piece.

<!-- D-009: code/checks/tokens.py, Example 4 -->

That design explains GPT-2's odd-looking vocabulary size. The released files contain the 256 single bytes, 50,000 learned merges, and one special token marking the end of a text: 256 + 50,000 + 1 = 50,257 [@openai2019gpt2code], the number [the destination chapter](#destination) quoted. It also explains the leading space. Because a space attaches to the word after it, " cat" with a space is a different token from "cat" without one. The token IDs in the destination chapter's figure, described there as illustrative, are in fact GPT-2's: "The cat sat on the" is 464, 3797, 3332, 319, 262.

![One sentence cut three ways: into words and punctuation, into characters, and by GPT-2's tokenizer, with each token's ID beneath it. ␣ marks a space. Common words are single tokens, each carrying the space before it; the rare name and the number are split into pieces.](../../figures/tokens-three-ways.svg){#fig:tokens-three-ways}

The figure shows the sentence "The tokenizer read Kierkegaard in 1843." Split into words and punctuation, it is 7 pieces; into characters, 39. GPT-2 cuts it into 11 tokens. Common words, with their leading spaces, are single tokens. "Tokenizer" becomes "token" and "izer". The philosopher's name becomes "Kier", "ke", and "gaard", and the year becomes "18" and "43".

<!-- D-009: code/checks/tokens.py, Example 5 -->

The size of the vocabulary sets the trade-off directly. Using only GPT-2's first merges shows it on the same sentence: with no merges, just the 256 bytes and the end token, the sentence is 39 tokens, one per byte; with the first 100 merges, 26; with 1,000, 18; with 10,000, 14; with all 50,000, 11. Each merge adds a row to the embedding table and a score to the output layer, and saves some length on every text that contains the merged pair.

## Special tokens

Not every token comes from text. A **special token** is a vocabulary entry with its own ID that marks structure rather than content. GPT-2's one special token, "<|endoftext|>", has the last ID, 50,256 [@openai2019gpt2code]. GPT-3, which kept GPT-2's tokenizer [@brown2020language, p. 8], used it to separate unrelated documents packed into one training sequence, "giving the language model the information necessary to infer that context separated by the end of text token is unrelated" [@brown2020language, p. 43]. When a model generates this token, generation stops, as [the destination chapter](#destination) described.

Other systems define others. SentencePiece reserves IDs for an unknown symbol, the beginning and end of a sequence, and padding [@kudo2018sentencepiece, p. 68]. BERT starts every input with "[CLS]", separates two sentences with "[SEP]", and hides words behind "[MASK]" during training [@devlin2019bert, p. 4174]. Meta's code for Llama 3 (2024) reserves 256 IDs for special tokens, including ones that mark where each turn of a conversation begins and ends [@meta2024llama3code]; chat models, the subject of later chapters, are built on such markers.

## Vocabulary sizes over time

There is no single "typical" vocabulary size, only snapshots. Word-level translation models used 30,000 to 50,000 words (as of 2015) [@sennrich2016neural, p. 1715]. Google's translation system used 8,000 to 32,000 wordpieces (2016) [@wu2016google, p. 7]. GPT-2 had 50,257 tokens (2019) [@radford2019language, p. 4]. Llama 3 has 128,000 (2024), combining "100K tokens from the tiktoken tokenizer with 28K additional tokens to better support non-English languages" [@grattafiori2024llama, p. 7]. OpenAI's published tokenizer library, as of 2026-11, maps GPT-3.5 and GPT-4 to a vocabulary of about 100,000 tokens and its later models, from GPT-4o on, to about 200,000 [@openai2026tiktoken].

The direction is toward larger vocabularies, and the Llama 3 paper says why. Its new tokenizer "improves compression rates on a sample of English data from 3.17 to 3.94 characters per token. This enables the model to "read" more text for the same amount of training compute" [@grattafiori2024llama, p. 7]. <!-- D-009: code/checks/tokens.py, Example 7 --> Going from 3.17 to 3.94 characters per token means the same English text needs about 20% fewer tokens.

## What follows from tokens

**Cost and limits are counted in tokens.** A model's context window, the most text it can handle at once, is a number of tokens, and so is its output limit [@openai2026tokens]. As of 2026-11, the two vendors checked for this book price their models per million tokens, with input and output priced separately [@openai2026pricing; @anthropic2026pricing]. OpenAI's rule of thumb for English is that "1 token is approximately 4 characters" and "approximately three-quarters of a word", which it calls estimates [@openai2026tokens]. Because the count depends on the tokenizer, changing the tokenizer changes the price of the same text. Anthropic notes, as of 2026-11, that the tokenizer of its newer models "produces approximately 30% more tokens for the same text" [@anthropic2026pricing].

**Other languages pay more.** A tokenizer trained mostly on English text learns merges for English. Aleksandar Petrov and colleagues measured how many tokens the same sentences need in different languages, translated from one set of 2,000 sentences [@petrov2023language, p. 3]. With the tokenizer of ChatGPT and GPT-4 (as of 2023), Italian needed 1.64 times as many tokens as English, Bulgarian 2.64, Arabic 3.04, and Shan, a language of Myanmar, 15.05 [@petrov2023language, p. 3]. Under GPT-2's tokenizer, the Bulgarian word "защо" ("why") takes 6 tokens for 4 letters, because some letters are split into their two bytes [@petrov2023language, p. 2]; <!-- D-009: code/checks/tokens.py, Example 4 --> this book's script reproduces it. The consequences are concrete: users of some languages pay more for the same task, wait longer, and fit less text into the context window [@petrov2023language, p. 2]. The GPT-3 authors suspected the same cause behind weak translation into Romanian, "due to reusing the byte-level BPE tokenizer of GPT-2 which was developed for an almost entirely English training dataset" [@brown2020language, p. 16]. Llama 3's 28,000 added tokens were a response.

**Spelling is hard to see.** GPT-2 gives " strawberry" a single ID. The model receives a number, not ten letters; it can know the letters only if training taught it. GPT-3's authors tested tasks that rearrange letters and found that "None of the models can reverse the letters in a word", noting that such tasks require "pulling apart" tokens that cover "significant fractions of a word" [@brown2020language, pp. 23-24]. Yet models learn a good deal about spelling anyway: Ayush Kaushal and Kyle Mahowald found that token embeddings "robustly encode character-level information" [@kaushal2022tokens, p. 2487].

**Numbers are cut unevenly.** <!-- D-009: code/checks/tokens.py, Examples 4 and 7 --> GPT-2's tokenizer cuts "1234567" into 123, 45, and 67, and of the thousand strings from "000" to "999", 777 are single tokens and the rest are not. The pieces do not line up with place value. Rodrigo Nogueira and colleagues observed that a T5 model, trained on small sets of examples, failed to learn addition of long numbers when "132" might become "1" and "32" while "232" became "23" and "2" [@nogueira2021investigating, p. 4]. Model builders responded with rules. LLaMA (2023) split "all numbers into individual digits" [@touvron2023llama, p. 2]. The tokenizer of GPT-3.5 and GPT-4 has tokens for every 1-, 2-, and 3-digit string and cuts long numbers into threes from the left [@singh2024tokenization, p. 2], so "1234567" becomes 123, 456, 7. Aaditya Singh and DJ Strouse found that forcing the threes to start from the right, by writing numbers with commas, raised GPT-3.5's accuracy on their addition problems from 75.6% to 97.8% (models of March 2023) [@singh2024tokenization, p. 1], and that the gap shrank in larger models [@singh2024tokenization, p. 1].

For both spelling and arithmetic, tokenization is a measurable cause of difficulty, not the only one. Character-level digits did not solve Nogueira and colleagues' problem either [@nogueira2021investigating, p. 1], and larger models partly overcome the tokenizer's quirks.

**Some tokens are barely seen.** The tokenizer is trained before the model, often on different text. A piece of text that was frequent in the tokenizer's data can become a token and then almost never occur in the model's training data. Such "glitch tokens", "tokens present in the tokenizer vocabulary but that are nearly or entirely absent during model training", can make models behave strangely [@land2024fishing, p. 11631]. The best known, " SolidGoldMagikarp", is a single token in GPT-2's vocabulary, ID 43,453.

## Why not just bytes?

If BPE causes these problems, why not feed models raw bytes or characters? Character models work, as the translation results showed, but they make sequences several times longer, and longer sequences cost more computation. GPT-2's authors noted in 2019 that "current byte-level LMs are not competitive with word-level LMs on large scale datasets" [@radford2019language, p. 4]. As of 2024, research on models without tokenizers was active, but its techniques "have not been widely adopted", and "the vast majority of contemporary models still rely on subword tokenization" [@land2024fishing, p. 11631].

## What to carry forward

- A model reads token IDs, not text. A tokenizer, trained separately and fixed before the model is trained, cuts text into tokens from a fixed vocabulary.
- Whole words leave unknown words; characters make text long. Subword units are the compromise: frequent words whole, rare words in pieces, nothing unknown.
- Byte pair encoding began as a 1994 compression method and was adapted to words in 2015: merge the most frequent adjacent pair, repeat, then replay the merges on new text. Vocabulary size is the number of starting symbols plus the number of merges.
- WordPiece and the unigram method are relatives; SentencePiece is a tool that implements BPE and the unigram method on raw text.
- GPT-2's byte-level BPE starts from the 256 byte values, so it can represent any text: 256 bytes + 50,000 merges + 1 end-of-text token = 50,257.
- Special tokens mark structure: end of text, separators, conversation turns.
- Vocabularies have grown, from tens of thousands to about 200,000, to fit more text per token. Token counts set cost, speed, and how much fits in a context window, and they fall unevenly across languages.
- Tokenization makes spelling and arithmetic harder in measurable ways, though it is not the only cause of failures there.
