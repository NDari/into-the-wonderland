# Further reading {#further-reading}

<!-- D-002: no derivations and no formulas. D-003: no code, commands, or flags; where a free copy exists it is named by its site or identifier, as plain text. D-005: every description of a source comes from the verified chapters and their ledgers, or from a copy fetched for this appendix (logged in book1/sources/further-reading.md); difficulty labels are this book's judgment. D-006, D-007: the pointer to Book 2 states only what OUTLINE.md states. D-010: citations with page numbers; chapters linked by ID. D-020: "open-weight" in the book's own voice. -->

This appendix is for the reader who wants to go further. It has four parts: a reading list, ordered like the book; advice on reading a machine-learning paper; advice on reading a model card; and a note on what Book 2 covers.

## A reading list

The list is selective: about forty works, almost all of them sources this book has already cited, chosen because each is either a good next step or a landmark worth reading in the original. Each description says what the work is and how hard it is, using three labels, which are this book's judgment:

- **Gentle:** readable with this book alone.
- **Moderate:** a research paper or textbook chapter whose main ideas this book has prepared you for; skip the mathematics on a first reading.
- **Technical:** long, mathematical, or written for specialists.

**Free** marks a copy published at no cost by the authors, the publisher, a preprint server, or a public archive, at the address where this book's research read it in 2026-11. Addresses change. Where the free copy and the published version differ, the description says so.

### Textbooks and overviews

**Deep Learning**, by Ian Goodfellow, Yoshua Bengio, and Aaron Courville [@goodfellow2016deep]. A textbook of deep learning as it stood in 2016, cited in ten of this book's chapters: twenty chapters in three parts, from linear algebra, probability, and machine-learning basics, through feedforward, convolutional, and recurrent networks, regularization, and optimization, to research topics such as representation learning and generative models. It was published in 2016, the year before the transformer. *Technical*: it keeps the derivations this book leaves out. Free: deeplearningbook.org, as web pages only (the authors say their contract with MIT Press rules out a PDF).

**Speech and Language Processing**, by Dan Jurafsky and James H. Martin [@jurafsky2026speech]. A textbook of language processing whose third edition is a living draft, with a first volume titled "Large Language Models". This book cites five of its chapters, from the release of August 19, 2026: n-gram language models, embeddings, transformers and pretraining, masked language models, and information retrieval with retrieval-augmented generation [@jurafsky2026speech; @jurafsky2026embeddings; @jurafsky2026transformers; @jurafsky2026masked; @jurafsky2026ir]. It is unfinished: in one chapter the historical notes read "History TBD." [@jurafsky2026masked, p. 16]. Chapter and page numbers move between drafts, so note the draft date when you cite it. *Moderate.* Free: web.stanford.edu/~jurafsky/slp3.

**The Elements of Statistical Learning**, by Trevor Hastie, Robert Tibshirani, and Jerome Friedman, 2nd edition [@hastie2009elements]. The reference this book's reader may already own, cited here for principal components as the best low-rank approximation and for the kernel-weighted average, ideas this book connects to [LoRA](#adapting) and to [attention](#attention). *Technical.* Free: the corrected 12th printing (2017) as a PDF from the authors' site, hastie.su.domains.

**Dive into Deep Learning**, by Aston Zhang, Zachary Lipton, Mu Li, and Alexander Smola [@zhang2023dive]. A textbook that pairs each idea with an implementation in code, from linear regression through convolutional and recurrent networks to attention, transformers, and optimization. This book used its attention chapter, which presents attention as a soft database lookup and as kernel regression. Because of the code it suits a Book 2 reader best. *Moderate.* Free: d2l.ai.

**"Deep learning"**, by Yann LeCun, Yoshua Bengio, and Geoffrey Hinton [@lecun2015deep]. A nine-page review in *Nature* by three participants in the history, written in 2015, soon after the events of [the chapter on the deep learning turn](#deep-turn): representation learning, convolutional and recurrent networks, and the order of events as its authors saw it. *Gentle to moderate.* Free: on Hinton's website at the University of Toronto.

### Part I: Neural networks before deep learning

For [the artificial neuron](#neuron), [learning in layers](#backprop), and [networks with structure](#structure).

**"A Sociological History of the Neural Network Controversy"**, by Mikel Olazaran [@olazaran1993sociological]. A published history of the perceptron controversy, based on the literature and on interviews, from Rosenblatt's perceptron and the press around it to *Perceptrons* and the 1980s revival. This book quotes the 1958 newspapers and Minsky and Papert through it. *Gentle.*

**"Learning representations by back-propagating errors"**, by David Rumelhart, Geoffrey Hinton, and Ronald Williams [@rumelhart1986learning], with Andreas Griewank's history of reverse-mode differentiation [@griewank2012invented] and Jürgen Schmidhuber's survey [@schmidhuber2014deep]. The four-page letter that made backpropagation famous, through its demonstrations. Griewank's twelve pages and Schmidhuber's much longer survey trace how much of the method predates 1986, from Linnainmaa's 1970 thesis on. [The chapter on backpropagation](#backprop) presents that priority dispute without settling it; Schmidhuber writes as a participant with a known position in it. *Gentle* (the letter), *moderate* (Griewank), *technical* (the survey). Free: the letter on Hinton's website; the survey on arXiv (1404.7828).

**"Long Short-Term Memory"**, by Sepp Hochreiter and Jürgen Schmidhuber [@hochreiter1997long]. The paper that introduced the gated memory cell, with its analysis of why error signals vanish across long gaps in time. The forget gate came later, from other work; see [the structure chapter](#structure). Forty-six pages. *Technical.*

### Part II: Deep learning starts working

For [the turn](#deep-turn), [the training loop](#toolkit), and [making deep networks trainable](#depth).

**"ImageNet Classification with Deep Convolutional Neural Networks"**, by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton [@krizhevsky2012imagenet]. The nine-page paper behind the 2012 result. Its authors ranked their design choices by importance, with the ReLU first and training across two GPUs second [@krizhevsky2012imagenet, p. 2]. *Moderate.* Free: NeurIPS proceedings.

**"ImageNet Large Scale Visual Recognition Challenge"**, by Olga Russakovsky and colleagues [@russakovsky2015imagenet]. The organizers' account of the challenge from 2010 to 2014: how the images were collected and labeled, the rules, the winners, and an estimate of human error that rests on one trained annotator, with its caveats stated. Read it to see how a benchmark is built. *Moderate.* Free: arXiv (1409.0575), whose 43 pages are numbered differently from the journal version.

**"Automatic Differentiation in Machine Learning: a Survey"**, by Atılım Güneş Baydin and colleagues [@baydin2018automatic]. The family of techniques of which backpropagation is one case, with a worked backward pass, and how frameworks record a computation to differentiate it. *Moderate to technical.* Free: jmlr.org.

**"Deep Residual Learning for Image Recognition"**, by Kaiming He and colleagues [@he2015deep]. The paper that found deeper plain networks training worse, not from overfitting, and added the residual connections every transformer block uses. [The depth chapter](#depth) presents the claim that highway networks came first. Twelve pages. *Moderate.* Free: arXiv (1512.03385).

### Part III: Teaching machines language

For [prediction](#prediction), [embeddings](#embeddings), [sequences](#seq2seq), and [tokens](#tokens).

**"A Mathematical Theory of Communication"**, by Claude Shannon [@shannon1948mathematical]. The founding paper of information theory. Its third section builds a series of approximations to English, each using more of the preceding text: the idea behind n-gram models [@shannon1948mathematical, p. 388]. Part I as a whole runs to 45 pages, mostly mathematics. *Gentle* (that section), *technical* (the rest). Free: Internet Archive, in its scans of the *Bell System Technical Journal*.

**"The Dawn of Statistical ASR and MT"**, by Frederick Jelinek [@jelinek2009dawn]. A first-hand account by the head of the IBM group that brought statistics, and trigram language models, to speech recognition and translation from 1972; written decades after the events. Twelve pages. *Gentle.* Free: ACL Anthology (J09-4004).

**"A Neural Probabilistic Language Model"**, by Yoshua Bengio and colleagues [@bengio2003neural]. The model that learned a vector for every word along with the predictor, to escape the curse of dimensionality: the bridge from [prediction](#prediction) to [embeddings](#embeddings). Nineteen pages. *Moderate.* Free: jmlr.org.

**"Efficient Estimation of Word Representations in Vector Space"**, by Tomas Mikolov and colleagues [@mikolov2013efficient], with Omer Levy, Yoav Goldberg, and Ido Dagan's "Improving Distributional Similarity with Lessons Learned from Word Embeddings" [@levy2015improving]. The first word2vec paper, with its simpler models and its analogy test; then the study that found much of the advantage came from "system design choices and hyperparameter optimizations, rather than the embedding algorithms themselves" [@levy2015improving, p. 211]. The second is a lesson in reading any comparison. *Moderate.* Free: arXiv (1301.3781); ACL Anthology (Q15-1016).

**"Sequence to Sequence Learning with Neural Networks"**, by Ilya Sutskever, Oriol Vinyals, and Quoc Le [@sutskever2014sequence], and **"Neural Machine Translation by Jointly Learning to Align and Translate"**, by Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio [@bahdanau2015neural]. The encoder-decoder that squeezes a sentence into one vector, and the attention that removed that bottleneck. Nine and fifteen pages. *Moderate.* Free: NeurIPS proceedings; arXiv (1409.0473).

**"Neural Machine Translation of Rare Words with Subword Units"**, by Rico Sennrich, Barry Haddow, and Alexandra Birch [@sennrich2016neural]. Byte-pair encoding turned from a compression trick into a way to build a vocabulary of word pieces, the method [the tokens chapter](#tokens) follows into GPT-2 and later models. Eleven pages. *Moderate.* Free: ACL Anthology (P16-1162).

### Part IV: The transformer

For [attention](#attention) and [the anatomy of a transformer](#anatomy).

**"Attention Is All You Need"**, by Ashish Vaswani and colleagues [@vaswani2017attention]. The transformer paper: fifteen pages with the appendix. After [attention](#attention) and [anatomy](#anatomy), its description of the model and its tables are within reach. This book read the seventh arXiv version, posted in 2023. *Moderate.* Free: arXiv (1706.03762).

**"A Mathematical Framework for Transformer Circuits"**, by Nelson Elhage and colleagues [@elhage2021mathematical]. An interpretability paper that treats each layer as reading from and writing to the **residual stream**, the name this book uses for the vector that runs between layers. <!-- D-019 --> A web article. *Technical* in places. Free: transformer-circuits.pub.

### Part V: From transformer to LLM

For [pretraining](#pretraining), [scale](#scale), [training](#training), and [generation](#generation).

**"Improving Language Understanding by Generative Pre-Training"**, by Alec Radford and colleagues [@radford2018improving]. GPT: pretrain a transformer decoder as a language model, then fine-tune it with a small task layer. Twelve pages. *Moderate.* Free: OpenAI's site.

**"BERT"**, by Jacob Devlin and colleagues [@devlin2019bert]. Pretraining a transformer encoder by filling in hidden words; afterwards, in one report's words, "using BERT has become the norm" [@bommasani2021opportunities, p. 5]. Sixteen pages. *Moderate.* Free: ACL Anthology (N19-1423).

**"Language Models are Few-Shot Learners"**, by Tom Brown and colleagues [@brown2020language]. GPT-3 and in-context learning. Its 75 pages are mostly results; read the description of models, data, and training [@brown2020language, pp. 8-9] and the section on contamination [@brown2020language, pp. 29-32]. *Moderate.* Free: arXiv (2005.14165).

**"Scaling Laws for Neural Language Models"**, by Jared Kaplan and colleagues [@kaplan2020scaling], and **"Training Compute-Optimal Large Language Models"**, by Jordan Hoffmann and colleagues [@hoffmann2022training]. The power laws that turned scale into a plan, and the revision that found large models "significantly undertrained" [@hoffmann2022training, p. 1]. Read them as a pair. Thirty and 36 pages. *Technical.* Free: arXiv (2001.08361; 2203.15556).

**"Emergent Abilities of Large Language Models"**, by Jason Wei and colleagues [@wei2022emergent], and **"Are Emergent Abilities of Large Language Models a Mirage?"**, by Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo [@schaeffer2023emergent]. Abilities that seem to appear suddenly with scale, and the argument that many such jumps come from how tasks are scored. Wei and colleagues had already called that explanation "at best an incomplete explanation" [@wei2022emergent, p. 7]. Read both. *Moderate.* Free: arXiv (2206.07682); NeurIPS proceedings.

**"The Bitter Lesson"**, by Richard Sutton [@sutton2019bitter], with Rodney Brooks's reply, "A Better Lesson" [@brooks2019better]. A short essay arguing that general methods that use computation win in the long run, and a critic's answer that the human work has moved, not gone. *Gentle.* Free: on each author's website.

**"The Llama 3 Herd of Models"**, by Aaron Grattafiori and colleagues [@grattafiori2024llama]. A full modern training report from an open-weight developer: data, architecture, scaling-law fits, infrastructure, the training recipe, and post-training. Long; read it by section. *Moderate to technical.* Free: arXiv (2407.21783).

### Part VI: From LLM to assistant

For [instructions](#instructions), [prompting](#prompting), [adapting](#adapting), and [knowledge and tools](#tools).

**"Training language models to follow instructions with human feedback"**, by Long Ouyang and colleagues [@ouyang2022training]. InstructGPT: supervised fine-tuning, a reward model, and reinforcement learning, summarized on one page [@ouyang2022training, p. 3]. Sixty-eight pages. *Moderate.* Free: arXiv (2203.02155).

**"Direct Preference Optimization"**, by Rafael Rafailov and colleagues [@rafailov2023direct]. Preference training reduced to "a simple classification loss" [@rafailov2023direct, p. 1]. The introduction is readable; the derivation is *technical*. Free: arXiv (2305.18290).

**"Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback"**, by Stephen Casper and 31 co-authors [@casper2023open]. A survey of what goes wrong with learning from human ratings, marking some problems as "fundamental". *Gentle to moderate.* Free: arXiv (2307.15217).

**"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"**, by Jason Wei and colleagues [@wei2022chain]. Few-shot examples that show their working, and tests of three explanations for why it helps. *Moderate.* Free: arXiv (2201.11903).

**"LoRA: Low-Rank Adaptation of Large Language Models"**, by Edward Hu and colleagues [@hu2021lora]. The low-rank bet of [the chapter on adapting](#adapting), in its original form. *Moderate.* Free: arXiv (2106.09685).

**"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"**, by Patrick Lewis and colleagues [@lewis2020retrieval]. The paper that named RAG, with its "closed-book" and "open-book" models [@lewis2020retrieval, p. 5]. *Moderate.* Free: arXiv (2005.11401).

**"ReAct: Synergizing Reasoning and Acting in Language Models"**, by Shunyu Yao and colleagues [@yao2023react]. Reasoning and actions interleaved in "multiple thought-action-observation steps" [@yao2023react, p. 3], the pattern of the agent loop, with a count of how the loop fails. *Moderate.* Free: arXiv (2210.03629).

**"Not What You've Signed Up For"**, by Kai Greshake and colleagues [@greshake2023not]. Indirect prompt injection: instructions hidden in content that an application retrieves for its model. *Moderate.* Free: arXiv (2302.12173).

### Part VII: The working landscape

For [the transformer since 2017](#since-2017), [local models](#local), [measuring models](#evaluation), and [the frontier](#frontier). Everything in this section ages fastest.

**"GPTQ"**, by Elias Frantar and colleagues [@frantar2023gptq]. Why simple rounding breaks down when large models are compressed hard, and a method that does better. *Technical.* Free: arXiv (2210.17323).

**The Open Source AI Definition, version 1.0**, by the Open Source Initiative [@osi2024osaid]. A short definition (October 2024) of what "open source" requires of an AI system: weights, code, and detailed information about the training data. It is the reason this book says "open-weight" in its own voice. <!-- D-020 --> *Gentle.* Free: opensource.org.

**"Holistic Evaluation of Language Models"**, by Percy Liang and colleagues [@liang2023holistic]. HELM: many models, many metrics, one set of conditions. It shows how much the conditions matter, with one model scoring 79.1% or 30.2% on the same test depending on the prompt format [@liang2023holistic, p. 9]. Long. *Moderate.* Free: arXiv (2211.09110).

**"Chatbot Arena"**, by Wei-Lin Chiang and colleagues [@chiang2024chatbot], with "The Leaderboard Illusion", by Shivalika Singh and colleagues [@singh2025leaderboard], and the organizers' reply [@lmarena2025response]. How the best-known preference leaderboard works, a 2025 critique of its practices, and the answer. Read all three before trusting, or dismissing, a rank. *Moderate.* Free: arXiv (2403.04132; 2504.20879); news.lmarena.ai.

**The AI Index 2026 Annual Report**, by Sha Sajadieh and colleagues at Stanford [@sajadieh2026ai]. A yearly report of 425 pages; this book used its pages on benchmarks, which collect other evaluators' results with their sources. A place to look numbers up, then follow them back to where they came from. *Gentle,* by section. Free: hai.stanford.edu.

**"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"**, by DeepSeek-AI [@deepseekai2025r1v2]. A reasoning model trained by reinforcement learning on checkable answers, with its authors' own list of limitations. The revision of January 2026 runs to 86 pages and changes some numbers of the first version (see below). *Technical* in places. Free: arXiv (2501.12948).

**"Measuring AI Ability to Complete Long Software Tasks"**, by Thomas Kwa and colleagues at METR [@kwa2025measuring]. The time-horizon measure and its trend. As of its fourth version (July 2026) it is a preprint under review. *Moderate.* Free: arXiv (2503.14499).

**International AI Safety Report 2026**, by Yoshua Bengio and others [@bengio2026international], with Arvind Narayanan and Sayash Kapoor's "AI as Normal Technology" [@narayanan2025normal]. A synthesis by over a hundred experts that "does not make specific policy recommendations" [@bengio2026international], and an essay that argues against visions that treat AI as "akin to a separate species" [@narayanan2025normal]. Read both, as [the frontier chapter](#frontier) does. *Gentle.* Free: internationalaisafetyreport.org; knightcolumbia.org.

## How to read a machine-learning paper

Most papers are not read from start to finish, and should not be. The computer scientist S. Keshav, in a two-page note on a skill he calls "rarely taught", suggests three passes [@keshav2007read, p. 83]. The first, five to ten minutes, covers the title, abstract, and introduction, the section headings, the conclusions, and a glance at the references; after it you should know what kind of paper it is, what it builds on, whether its assumptions look valid, what it claims to contribute, and whether it is clearly written [@keshav2007read, p. 83]. The second, up to an hour, reads with more care but skips proofs, and looks closely at the figures: "Are the axes properly labeled? Are results shown with error bars, so that conclusions are statistically significant?" [@keshav2007read, pp. 83-84]. The third, "about four or five hours for beginners", tries "to virtually re-implement the paper" [@keshav2007read, p. 84]. For this book's reader, the first two passes are usually enough, and four questions do most of the work on the second.

**What is the baseline?** A result is a comparison, and a **baseline** is the score it is compared with (see [the chapter on measuring models](#evaluation)). Find the table that carries the main claim and read its rows before its text. A score means little without its floor: MMLU's random baseline is 25%, because each question has four choices [@hendrycks2021measuring, p. 5], so GPT-3's 43.9% in 2020 [@hendrycks2021measuring, p. 2] was well above chance and well below expert level. Ask whether the competitors were run under the same conditions or their numbers copied from other papers, and whether the baseline is a strong one.

**What was measured, on what data?** Note the benchmark, the number of questions, the prompt, the number of examples shown, and the scoring rule. On 164 problems, a score of 80% carries an interval of about six points either way (from [the chapter on measuring models](#evaluation)), so smaller gaps are not differences. The prompt format alone can move a score by tens of points [@liang2023holistic, p. 9]. And ask whether the model could have seen the test: GPT-4's 92.0% on grade-school math problems came with part of that benchmark's training set mixed into its training [@openai2023gpt4, pp. 7, 29].

**Which version am I reading?** Most papers in this field appear first on **arXiv**, a preprint server where authors post papers before, or without, peer review, and revise them in numbered versions. The first page often says which stage a version is at. Adam's arXiv page lists nine versions: the first, from December 2014, is headed "Under review as a conference paper at ICLR 2015", the ninth, from January 2017, "Published as a conference paper at ICLR 2015" [@kingma2015adam]. Numbers change between versions. DeepSeek-R1-Zero's accuracy on a mathematics competition rose "from 15.6% to 71.0%" in the paper's first version [@deepseekai2025r1, pp. 3, 6] and "from an initial 15.6% to 77.9%" in the revision almost a year later [@deepseekai2025r1v2, p. 4]. Corrections also arrive outside the paper: GPT-2's paper gave its smallest model 117 million parameters, and OpenAI later said its "original parameter counts were wrong" and listed the model as 124M [@radford2019language, p. 4; @openai2019gpt2code]. Say which version you read, with its date. A published version is not always the latest: the transformer paper appeared at the NIPS conference (now NeurIPS) in 2017, and its seventh arXiv version dates from 2023.

**Which page?** Page numbers belong to a version. The ImageNet challenge paper is numbered 1 to 43 on arXiv and differently in the journal [@russakovsky2015imagenet]; many proceedings PDFs print no page numbers at all; a living textbook's pages move with each draft [@jurafsky2026speech]. When you quote, give the version and the page in it, as this book does.

**"State of the art" carries a date.** The phrase means the best published result on a particular test at a particular time, nothing more. In 2018 GLUE's authors wrote that "solving GLUE is beyond the capabilities of current models and methods"; by July 2019 the best score had passed the crowdworkers' human baseline [@wang2019glue, pp. 7-8; @wang2019superglue, p. 1]. In January 2022, chain-of-thought prompting gave "state-of-the-art accuracy" on grade-school math at 56.9% [@wei2022chain, pp. 1, 20]; the GPT-4 report of 2023 gave 92.0% [@openai2023gpt4, p. 7]. The AI Index of 2026 observes that even tests designed to be harder "often remain useful for only a few years" [@sajadieh2026ai, p. 78]. Read every "state of the art" as "the best these authors knew of, on this test, on this date".

Three habits complete the list. **Notice who is speaking**: a company's report is a primary source for what the company did, and a claim that its model is better is the makers' account until others check it. **Look for the reply**: many results in this book came with a published challenge, such as the emergence dispute [@schaeffer2023emergent], the Arena critique and answer [@singh2025leaderboard; @lmarena2025response], or the dispute over whether reasoning models collapse on hard puzzles, where a critic's comment, not peer reviewed, drew replies in the original paper's third version [@lawsen2025comment; @shojaee2025illusion]. **Prefer surveys and textbooks for orientation**, then go to the original for the claim.

## How to read a model card

A **model card**, in Margaret Mitchell and colleagues' 2019 proposal, is a short document that comes with a trained model, gives "benchmarked evaluation in a variety of conditions", and discloses "the context in which models are intended to be used" [@mitchell2019model, p. 1]. Their template has sections for model details (developer, date, version, type, license), intended use, metrics, evaluation data, training data, quantitative analyses, ethical considerations, and caveats [@mitchell2019model, p. 3]. On Hugging Face the card is the README of the model's repository, with metadata that include the license [@huggingface2026modelcards]. A model offered only as a service has no downloadable card; the nearest documents are technical reports and "system cards", such as the OpenAI o1 System Card of December 2024 [@openai2024o1card]. [The chapter on local models](#local) and [the chapter on measuring models](#evaluation) explain the parts; what follows is a checklist, as of 2026-11.

- **Who published it?** Anyone can upload to a hub, so copies and variants made by others sit next to the maker's own [@huggingface2026hub]. Start from the maker's repository.
- **Which model, and when?** The exact name and version, the release date, and the **knowledge cutoff**, the date after which the model has seen little or no text. Meta's card for Llama 3.1 gives both: December 2023 and July 23, 2024 [@meta2024llama31card]. Not every card does: several large open-weight models on Hugging Face in 2026-11 gave no release date on their cards [@qwen2026qwen38card; @mistral2026large4card; @moonshot2026kimik31card].
- **Under what license?** The license file binds, not the summary; terms change between versions of the same family; and a model derived from another can inherit its license, as a distilled DeepSeek model inherits Meta's [@huggingface2026api]. Some repositories are **gated**: the files come only after a request that shares your username and email address with the authors [@huggingface2026gated].
- **How big, and how long a context?** The exact parameter count, and for a mixture of experts both total and active parameters. The context length is on the card; the file name is not the authority [@meta2024llama32card].
- **For what use?** Intended uses and out-of-scope uses, and whether this is a base model or an instruction-tuned one.
- **Evaluated how?** The questions of [the chapter on measuring models](#evaluation): which benchmarks, and are any saturated; how many questions; what prompt, how many examples, and what scoring; were competitors run the same way; was contamination checked, and could anyone outside check it; and what the authors say the scores do not show.
- **Trained on what?** Mitchell and colleagues' template already marked training data "May not be possible to provide in practice" [@mitchell2019model, p. 3]. For large models the description is often an outline, or absent.
- **Read as of when?** Cards are edited after release: the Llama 3.2 card read for this book was last changed in October 2024, a month after the models came out [@meta2024llama32card]. Note the date you read it.

## Where Book 2 picks up

Book 2, *Building and running*, is the hands-on companion. As of this writing it exists as an outline; its framework, hardware target, and length are still open. It is planned in three stages. <!-- D-007 -->

1. **Build.** Set up the tools with pinned versions; write a small byte-pair-encoding tokenizer and compare it with a real one; learn tensors, automatic differentiation, and a training loop on a tiny network; implement one attention head, then multi-head attention with causal masking; and assemble a small GPT and count its parameters. Then train it once, briefly, on a small corpus, to watch the loss fall and the samples improve: for understanding, not for use. <!-- D-006 -->
2. **Run.** Install llama.cpp, choose and download an open-weight model, and understand its file, its quantization level, and the memory it needs; then sampling settings, chat templates, the system prompt, and the local server, each tied back to a mechanism from this book; then a minimal retrieval setup with a local embedding model.
3. **Harness.** Write the smallest possible agent loop by hand, in which the model requests a tool, the program runs it, and the result goes back in; then read a real harness, Tau, layer by layer, to see what a production-shaped harness adds. <!-- D-007 -->

Each Book 2 chapter names the chapters of this book it makes concrete. The exact versions of llama.cpp and Tau will be pinned in Book 2's code and stated in its text.
