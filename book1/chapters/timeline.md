# Timeline {#timeline}

<!-- D-005: compiled from the verified chapters, using their dates and citations; independent check pending. D-010: citations by bib key and page, chapters linked by ID. D-008: periods follow the book's parts. D-003: no code. -->

This appendix lists, in order, the main dated events that the chapters describe. Each entry gives the date as the chapter gives it, one line on what happened, the source the chapter cites, and, in italics, the chapter that tells the story. Nothing here goes beyond the chapters: an event appears only if a chapter states it, with the chapter's own citation.

A paper is dated as the chapter dates it, usually when it first appeared, which can be earlier than the journal or conference version the citation names. Where a chapter gives two dates, such as a preprint and a publication, both are shown. Where the chapters present a disagreement over who was first, each claimant's event is listed as the chapter gives it, and the timeline does not choose between them. The book's date is November 2026; the later entries describe a field that was still moving.

## Before 1970: the neuron and the statistics of text

1913
:   Markov predicts vowels and consonants in *Eugene Onegin* with a chain [@jurafsky2026speech, pp. 21-22]. *[Language as prediction](#prediction)*

1943
:   McCulloch and Pitts model the neuron as threshold logic [@mcculloch1943logical]. *[The artificial neuron](#neuron)*

1948
:   Shannon's "A Mathematical Theory of Communication" treats text as a random source [@shannon1948mathematical, p. 379]. *[Language as prediction](#prediction)*

1949
:   Hebb proposes that learning changes the strength of connections [@hebb1949organization, p. 62]. *[The artificial neuron](#neuron)*

1951
:   Robbins and Monro's stochastic approximation, the root of SGD [@robbins1951stochastic, p. 400]. *[The training loop](#toolkit)*

1951
:   Shannon's guessing game measures how predictable English is [@shannon1951prediction, p. 50]. *[Language as prediction](#prediction)*

1954
:   Harris's distributional hypothesis [@harris1954distributional, p. 146]. *[Words as vectors](#embeddings)*

1957
:   Firth: "You shall know a word by the company it keeps!" [@firth1957synopsis, p. 11]. *[Words as vectors](#embeddings)*

1958
:   Rosenblatt's perceptron learns from examples by error correction [@rosenblatt1958perceptron]. *[The artificial neuron](#neuron)*

8 July 1958
:   The New York Times reports the Navy's "embryo of an electronic computer" [@nyt1958navy; quoted in @olazaran1993sociological, p. 341]. *[The artificial neuron](#neuron)*

1960
:   Widrow and Hoff's ADALINE reduces a squared error [@widrow1960adaptive, p. 97]. *[The artificial neuron](#neuron)*

1964
:   Polyak's momentum method, as later authors credit it [@sutskever2013importance, p. 1140; @goodfellow2016deep, p. 292]. *[The training loop](#toolkit)*

1969
:   Minsky and Papert's *Perceptrons* [@minsky1969perceptrons]; the first major dip follows [@goodfellow2016deep, p. 14]. *[The artificial neuron](#neuron)*

## 1970-1989: learning in layers

Backpropagation was found several times. The entries from 1970 to 1986 list each finding as [Learning in layers](#backprop) presents it.

1970
:   Linnainmaa's thesis: reverse-mode automatic differentiation, not yet for networks [@griewank2012invented, p. 389; @schmidhuber2014deep, p. 11]. *[Learning in layers](#backprop)*

1974
:   Werbos's thesis: "preliminary, NN-specific discussion" [@schmidhuber2014deep, p. 11]. *[Learning in layers](#backprop)*

About 1978
:   IBM models English by trigrams for speech recognition [@jelinek2009dawn, pp. 488-489]. *[Language as prediction](#prediction)*

1980
:   Fukushima's neocognitron [@fukushima1980neocognitron, p. 193]. *[Networks with structure](#structure)*

1981
:   Werbos first applies backpropagation to neural networks, as Schmidhuber and the textbook date it [@schmidhuber2014deep, p. 11; @goodfellow2016deep, p. 221]. *[Learning in layers](#backprop)*

1985
:   Parker and LeCun independently derive similar procedures [@rumelhart1986internal, p. 322]. *[Learning in layers](#backprop)*

1986
:   Rumelhart, Hinton, and Williams show hidden units learning features; backpropagation becomes widely used [@rumelhart1986learning, p. 533; @goodfellow2016deep, p. 221]. *[Learning in layers](#backprop)*

1987
:   Katz's back-off smoothing for n-gram models [@katz1987estimation, p. 400]. *[Language as prediction](#prediction)*

1989
:   LeCun and colleagues' convolutional network reads zip codes [@lecun1989backpropagation]. *[Networks with structure](#structure)*

1989
:   Cybenko, and Hornik, Stinchcombe, and White: universal approximation [@cybenko1989approximation, p. 303; @hornik1989multilayer, p. 359]. *[Learning in layers](#backprop)*

## 1990-2005: structure, smoothing, and the second winter

1990
:   Elman's simple recurrent network predicts the next word [@elman1990finding, p. 183]. *[Networks with structure](#structure)*

1990
:   Deerwester and colleagues' latent semantic analysis [@deerwester1990indexing, p. 391]. *[Words as vectors](#embeddings)*

1990
:   Brown and colleagues at IBM propose statistical translation [@brown1990statistical, p. 79]. *[Language as prediction](#prediction)*

15 June 1991
:   Hochreiter's diploma thesis analyses vanishing gradients [@hochreiter1991untersuchungen]. *[Networks with structure](#structure)*

1994
:   Bengio, Simard, and Frasconi: a recurrent network is stable or trainable, "but not both" [@bengio1994learning, pp. 157-158]. *[Networks with structure](#structure)*

1994
:   Gage's byte pair encoding, for compression [@gage1994new]. *[Tokens](#tokens)*

1995
:   Cortes and Vapnik's soft-margin support vector machine [@cortes1995support, p. 273]. *[Networks with structure](#structure)*

1995
:   Kneser-Ney smoothing [@kneser1995improved, p. 181]. *[Language as prediction](#prediction)*

1995, 1997
:   Hochreiter and Schmidhuber's LSTM, submitted August 1995, published 1997 [@hochreiter1997long, p. 1780]. *[Networks with structure](#structure)*

1998
:   LeNet-5 and the MNIST dataset [@lecun1998gradient, pp. 9-10]. *[Networks with structure](#structure)*

1998
:   Chen and Goodman find Kneser-Ney variants best [@chen1998empirical, p. 59]. *[Language as prediction](#prediction)*

Until 2007
:   Kernel machines preferred; neural networks decline, in the textbook's account [@goodfellow2016deep, p. 17]. *[Networks with structure](#structure)*

2000
:   The LSTM forget gate [@goodfellow2016deep, p. 404; @schmidhuber2014deep, p. 19]. *[Networks with structure](#structure)*

2000, 2003
:   Bengio and colleagues' neural language model, conference [@bengio2000neural] and journal versions [@bengio2003neural, p. 1137]. *[Words as vectors](#embeddings)*

2002
:   Papineni and colleagues' BLEU score [@papineni2002bleu, p. 311]. *[Reading and writing sequences](#seq2seq)*

2003
:   Koehn, Och, and Marcu's phrase-based translation [@koehn2003statistical, p. 49]. *[Reading and writing sequences](#seq2seq)*

## 2006-2016: deep learning starts working

Two accounts of where deep learning began appear in [the turn](#deep-turn); both are listed.

1991 on
:   Schmidhuber: deep learning results "at least since 1991", the term "coined around 2006" [@schmidhuber2014deep, p. 21]. *[The turn](#deep-turn)*

2006
:   Hinton, Osindero, and Teh train deep networks one layer at a time [@hinton2006fast], the textbook's "breakthrough in 2006" [@goodfellow2016deep, p. 18]. *[The turn](#deep-turn)*

2007
:   "Large Language Models in Machine Translation": n-grams on 2 trillion tokens [@brants2007large, p. 858]. *[Scale](#scale)*

2008
:   Collobert and Weston train a network for its word vectors [@collobert2008unified, p. 5]. *[Words as vectors](#embeddings)*

2009
:   ImageNet [@deng2009imagenet, p. 1]. *[The turn](#deep-turn)*

2009
:   Raina, Madhavan, and Ng: GPUs up to 70 times faster [@raina2009large, p. 1]. *[The turn](#deep-turn)*

2009-2012
:   Deep networks cut speech recognition error rates [@hinton2012deep, p. 83]. *[The turn](#deep-turn)*

2010
:   Ciresan and colleagues: plain deep networks on a GPU, 0.35% MNIST error [@ciresan2010deep, p. 1]. *[The turn](#deep-turn)*

2010
:   Nair and Hinton's "rectified linear units" [@nair2010rectified, p. 1]. *[The turn](#deep-turn)*

2010
:   Glorot and Bengio on starting weights for deep networks [@glorot2010understanding, p. 249]. *[Making deep networks trainable](#depth)*

2010
:   Mikolov and colleagues' recurrent language model [@mikolov2010recurrent, p. 1045]. *[Reading and writing sequences](#seq2seq)*

2011
:   GPU convolutional networks from Schmidhuber's laboratory win image contests, in his account of the credit [@schmidhuber2014deep, pp. 23-24]. *[The turn](#deep-turn)*

2012
:   Schuster and Nakajima's WordPiece [@schuster2012japanese, pp. 5149-5150]. *[Tokens](#tokens)*

2012
:   Hinton and colleagues propose dropout [@hinton2012improving, p. 1]. *[Making deep networks trainable](#depth)*

2012
:   SuperVision (AlexNet) wins ImageNet: 16.4% top-5 error against 26.2% [@krizhevsky2012imagenet, p. 7]. *[The turn](#deep-turn)*

2013
:   Mikolov and colleagues' word2vec [@mikolov2013efficient, p. 4]. *[Words as vectors](#embeddings)*

2014
:   Pennington, Socher, and Manning's GloVe [@pennington2014glove, p. 1532]. *[Words as vectors](#embeddings)*

June 2014
:   Cho and colleagues' RNN Encoder-Decoder [@cho2014learning, p. 1724]. *[Reading and writing sequences](#seq2seq)*

September 2014
:   Bahdanau, Cho, and Bengio post attention, nine days before Sutskever and colleagues [@bahdanau2015neural, p. 1]. *[Reading and writing sequences](#seq2seq)*

September 2014
:   Sutskever, Vinyals, and Le's sequence-to-sequence LSTMs [@sutskever2014sequence, p. 1]. *[Reading and writing sequences](#seq2seq)*

2015
:   Kingma and Ba's Adam, published at ICLR [@kingma2015adam, p. 1]. *[The training loop](#toolkit)*

2015
:   Ioffe and Szegedy's batch normalization [@ioffe2015batch, p. 448]. *[Making deep networks trainable](#depth)*

May 2015
:   Srivastava, Greff, and Schmidhuber's highway networks [@srivastava2015highway, p. 1]. *[Making deep networks trainable](#depth)*

2015, 2016
:   Sennrich, Haddow, and Birch adapt BPE to translation: posted August 2015, published 2016 [@sennrich2016neural, p. 1716]. *[Tokens](#tokens)*

2015
:   Hinton, Vinyals, and Dean's distillation [@hinton2015distilling, p. 1]. *[Adapting a model](#adapting)*

2015
:   Dai and Le pretrain a whole recurrent network [@dai2015semi, p. 1]. *[Pretraining](#pretraining)*

November 2015
:   Google open-sources TensorFlow [@abadi2015tensorflow, p. 1]. *[The training loop](#toolkit)*

December 2015
:   ResNet wins ImageNet with 3.57% top-5 error [@he2015deep, pp. 1-2]; Schmidhuber calls it a version of the highway network [@schmidhuber2022annotated, p. 12]. *[Making deep networks trainable](#depth)*

2016
:   Ba, Kiros, and Hinton's layer normalization [@ba2016layer, p. 1]. *[Making deep networks trainable](#depth)*

2016
:   A neural system wins almost all language pairs at the WMT shared task [@koehn2017neural, p. 6]. *[Reading and writing sequences](#seq2seq)*

September 2016
:   Google's neural translation system [@wu2016google, p. 1], all Chinese-English traffic by 27 September [@le2016neural]. *[Reading and writing sequences](#seq2seq)*

## 2017: the transformer

January 2017
:   PyTorch first released [@paszke2019pytorch, p. 9]. *[The training loop](#toolkit)*

2017
:   Shazeer and colleagues' sparsely gated mixture of experts [@shazeer2017outrageously, p. 1]. *[The transformer since 2017](#since-2017)*

June 2017
:   Christiano and colleagues learn from human comparisons [@christiano2017deep, pp. 5-6]. *[Teaching models to follow instructions](#instructions)*

June 2017
:   "Attention Is All You Need": the transformer [@vaswani2017attention, p. 1]. *[Attention without recurrence](#attention)*

2017
:   Schulman and colleagues' PPO [@schulman2017proximal, p. 1]. *[Teaching models to follow instructions](#instructions)*

## 2018-2022: from transformer to assistant

January 2018
:   Liu and colleagues' decoder-only transformer [@liu2018generating, pp. 1, 5]. *[Anatomy of a transformer](#anatomy)*

January 2018
:   Howard and Ruder's ULMFiT [@howard2018universal, p. 330]. *[Pretraining](#pretraining)*

Early 2018
:   Peters and colleagues' ELMo, contextual word vectors [@peters2018deep, p. 2227]. *[Pretraining](#pretraining)*

2018
:   GLUE benchmark [@wang2019glue, p. 2]. *[Measuring models](#evaluation)*

2018
:   OpenAI: the largest training runs' compute doubles every 3.5 months [@amodei2018ai]. *[Scale](#scale)*

2018
:   Santurkar and colleagues dispute why batch normalization works [@santurkar2018how, p. 1]. *[Making deep networks trainable](#depth)*

2018
:   Kudo's unigram method [@kudo2018subword, p. 68] and SentencePiece [@kudo2018sentencepiece, p. 66]. *[Tokens](#tokens)*

June 2018
:   Radford and colleagues' GPT [@radford2018improving, p. 1]. *[Pretraining](#pretraining)*

October 2018
:   Devlin and colleagues post BERT [@devlin2019bert, p. 4171]. *[Pretraining](#pretraining)*

February 2019
:   GPT-2, up to 1.5 billion parameters [@radford2019language, p. 4]. *[Scale](#scale)*

2019
:   Sutton's "The Bitter Lesson" [@sutton2019bitter]. *[Scale](#scale)*

2019
:   Houlsby and colleagues' adapters [@houlsby2019parameter, p. 2790]. *[Adapting a model](#adapting)*

2019
:   T5's systematic comparison of pretraining objectives [@raffel2020exploring, pp. 19-20]. *[Pretraining](#pretraining)*

2019
:   Holtzman and colleagues: beam search degenerates; nucleus sampling [@holtzman2020curious, p. 1]. *[Generating text](#generation)*

2019
:   Shazeer's multi-query attention [@shazeer2019fast, p. 1]. *[The transformer since 2017](#since-2017)*

November 2019
:   Full GPT-2 released after a staged release [@openai2019sixmonth; @openai2019release]. *[Scale](#scale)*

January 2020
:   Kaplan and colleagues' scaling laws [@kaplan2020scaling, pp. 1, 7]. *[Scale](#scale)*

May 2020
:   GPT-3, 175 billion parameters [@brown2020language, p. 1]. *[Scale](#scale)*

May 2020
:   Lewis and colleagues name retrieval-augmented generation [@lewis2020retrieval, p. 1]. *[Giving models knowledge and tools](#tools)*

2020
:   Karpukhin and colleagues' dense passage retrieval [@karpukhin2020dense, p. 6771]. *[Giving models knowledge and tools](#tools)*

2020
:   Hendrycks and colleagues release MMLU [@hendrycks2021measuring, pp. 1, 3]. *[Measuring models](#evaluation)*

2021
:   Su and colleagues' rotary position embeddings [@su2021roformer, p. 4]. *[The transformer since 2017](#since-2017)*

2021
:   Hu and colleagues' LoRA [@hu2021lora, p. 2]. *[Adapting a model](#adapting)*

2021
:   Elhage and colleagues: the residual stream and induction heads [@elhage2021mathematical]. *[The frontier](#frontier)*

September 2021
:   Wei and colleagues define instruction tuning [@wei2022finetuned, p. 1]. *[Teaching models to follow instructions](#instructions)*

January 2022
:   Wei and colleagues name chain-of-thought prompting [@wei2022chain, p. 1]. *[Prompting and context](#prompting)*

January 2022
:   OpenAI announces InstructGPT [@openai2022aligning]; the paper follows in March [@ouyang2022training, p. 2]. *[Teaching models to follow instructions](#instructions)*

March 2022
:   Chinchilla: models of the time were undertrained [@hoffmann2022training, pp. 1, 11]. *[Scale](#scale)*

May 2022
:   Kojima and colleagues: "Let's think step by step" [@kojima2022large, p. 1]. *[Prompting and context](#prompting)*

2022
:   PaLM, 540 billion parameters [@chowdhery2022palm, p. 3]. *[Scale](#scale)*

2022
:   Wei and colleagues name emergent abilities [@wei2022emergent, p. 1]; disputed in 2023 [@schaeffer2023emergent, p. 1]. *[Scale](#scale)*

2022
:   Dao and colleagues' FlashAttention [@dao2022flashattention, p. 2]. *[The transformer since 2017](#since-2017)*

September 2022
:   Willison writes up prompt injection [@willison2022prompt]. *[Prompting and context](#prompting)*

October 2022
:   Yao and colleagues' ReAct [@yao2023react, pp. 1, 3]. *[Giving models knowledge and tools](#tools)*

30 November 2022
:   OpenAI announces ChatGPT [@openai2022chatgpt]. *[Teaching models to follow instructions](#instructions)*

December 2022
:   Bai and colleagues' Constitutional AI [@bai2022constitutional, pp. 1-2]. *[Teaching models to follow instructions](#instructions)*

## 2023-2026: the working landscape

24 February 2023
:   Meta releases LLaMA, 7 to 65 billion parameters [@meta2023llamablog]. *[Small models and local inference](#local)*

10 March 2023
:   llama.cpp starts [@llamacpp2023readme; @ollama2026docs]. *[Small models and local inference](#local)*

March 2023
:   OpenAI's GPT-4 report [@openai2023gpt4, p. 7]. *[Measuring models](#evaluation)*

April 2023
:   Chatbot Arena starts [@chiang2024chatbot, p. 2]. *[Measuring models](#evaluation)*

May 2023
:   Rafailov and colleagues' DPO [@rafailov2023direct, p. 1]. *[Teaching models to follow instructions](#instructions)*

30 May 2023
:   The Center for AI Safety's statement on extinction risk [@cais2023statement]. *[The frontier](#frontier)*

2023
:   Dettmers and colleagues' QLoRA [@dettmers2023qlora, p. 1]. *[Adapting a model](#adapting)*

June 2023
:   OpenAI's function calling [@openai2023functioncalling]. *[Giving models knowledge and tools](#tools)*

July 2023
:   Meta's Llama 2 [@meta2023llama2news; @touvron2023llama2, pp. 10-11]. *[Small models and local inference](#local)*

21 August 2023
:   GGUF, llama.cpp's file format [@llamacpp2023ggufpr]. *[Small models and local inference](#local)*

2023
:   Ainslie and colleagues' grouped-query attention [@ainslie2023gqa, p. 4896]. *[The transformer since 2017](#since-2017)*

September 2023
:   Mistral 7B [@jiang2023mistral, p. 1]. *[Small models and local inference](#local)*

October 2023
:   SWE-bench [@jimenez2024swebench, pp. 1-3]. *[The frontier](#frontier)*

December 2023
:   Gu and Dao's Mamba [@gu2023mamba, p. 1]. *[The transformer since 2017](#since-2017)*

December 2023, January 2024
:   Mixtral 8x7B: released December 2023 [@mistral2023mixtral], paper January 2024 [@jiang2024mixtral, p. 1]. *[The transformer since 2017](#since-2017)*

April 2024
:   Llama 3, 8 and 70 billion parameters [@grattafiori2024llama, p. 2; @huggingface2026api]. *[Small models and local inference](#local)*

July 2024
:   Llama 3.1 adds 405 billion, released 23 July [@meta2024llama31card]; the Llama 3 paper [@grattafiori2024llama, p. 2]. *[Small models and local inference](#local)*

12 September 2024
:   OpenAI announces o1, a reasoning model [@openai2024learning]. *[The frontier](#frontier)*

September 2024
:   Llama 3.2 adds 1 and 3 billion [@meta2024llama32card]. *[Small models and local inference](#local)*

October 2024
:   The OSI's Open Source AI Definition 1.0 [@osi2024osaid]. *[Small models and local inference](#local)*

October 2024
:   Anthropic releases computer use [@anthropic2024computeruse]. *[The frontier](#frontier)*

25 November 2024
:   Anthropic publishes the Model Context Protocol [@anthropic2024mcp]. *[Giving models knowledge and tools](#tools)*

December 2024
:   DeepSeek-V3, a 671-billion-parameter mixture of experts [@deepseekai2024deepseekv3, p. 1]. *[The transformer since 2017](#since-2017)*

January 2025
:   DeepSeek-R1 [@deepseekai2025r1, p. 1], revised January 2026 [@deepseekai2025r1v2]. *[The frontier](#frontier)*

January 2025
:   Humanity's Last Exam [@phan2025humanity, p. 4]. *[Measuring models](#evaluation)*

March 2025
:   METR proposes the time horizon [@kwa2025measuring, p. 1]. *[The frontier](#frontier)*

April 2025
:   Meta's Llama 4, its first mixtures of experts [@meta2025llama4]. *[The transformer since 2017](#since-2017)*

April 2025
:   Singh and colleagues criticize Chatbot Arena [@singh2025leaderboard, pp. 1, 10]; the organizers reply in May [@lmarena2025response]. *[Measuring models](#evaluation)*

April 2025
:   Narayanan and Kapoor's "AI as normal technology" [@narayanan2025normal]. *[The frontier](#frontier)*

June 2025
:   "The Illusion of Thinking" opens a dispute over puzzle tests [@shojaee2025illusion, pp. 1, 6]. *[The frontier](#frontier)*

February 2026
:   OpenAI stops reporting SWE-bench Verified [@openai2026swebenchretired]. *[The frontier](#frontier)*

November 2026
:   Anthropic releases one model as Claude Fable and Claude Mythos [@anthropic2026fable52]. *[The frontier](#frontier)*
