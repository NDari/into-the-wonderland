# Ledger: further-reading

Chapter: `further-reading` (Book 1, appendix D, "Further reading").
Stage: verified, 2026-11-11 [D-005]. Compiled by a drafting agent from the verified chapters and ledgers; independent check recorded at the end.

## Method

- The reading list was chosen from sources already cited in the verified chapters. Every description of an entry (what it is, what it covers, page counts, versions, which free copy exists) was taken from the chapter that cites it or from the "Sources and how they were read" table and claim entries of that chapter's ledger. Nothing about a listed source comes from model memory.
- Five pages were fetched this session (2026-11-11) to support descriptions not in the ledgers: the landing pages of three textbooks, the download page of a fourth, and S. Keshav's "How to Read a Paper". They are logged under "Claims verified this session".
- Page counts are computed from the page ranges recorded in the ledgers (for example pp. 533-536 is four pages).
- **Free copies.** An entry is marked "Free" only when the ledger's "Read from" URL is a no-cost copy published by the authors (or their employer), the publisher, a preprint server (arXiv), an open repository or proceedings site (ACL Anthology, JMLR, PMLR, NeurIPS proceedings), or a public archive (Internet Archive). Copies on third-party personal or course pages (gwern.net, course readings, mirrors) are not marked, even though the ledgers read them: `olazaran1993sociological`, `griewank2012invented` (read from a mirror), `hochreiter1997long` (CMU course copy). The free copy is named by site or identifier, not by full URL [D-003].
- **Difficulty labels** (gentle, moderate, technical) are the drafting agent's editorial judgment, based on length, format (essay, letter, survey, paper, textbook), and the amount of mathematics recorded in the ledgers. They are not claims about the sources and need no citation.
- Book 2's description is taken only from the Book 2 section of `OUTLINE.md`, from [D-006] and [D-007], and from the parked question Q-06 in `DECISIONS.md` (framework, hardware target, length still open). The unverified point in [D-007] (whether Tau works against llama.cpp's server) is not stated in the appendix: the text says Tau is read "layer by layer" and does not promise that it runs against the local model.
- Not done: no new search for sources outside the book. No source was re-read for the entries except as noted below.

## Sources

Where each entry's description comes from. "Ledger" means `book1/sources/<id>.md`, with the claim or table row used.

### Textbooks and overviews

| Key | Description from | Notes |
|---|---|---|
| `goodfellow2016deep` | Own fetch (deeplearningbook.org) for parts, chapter list, free web version, and no PDF; count of citing chapters by search of `book1/chapters` (10 files) | Ledgers: neuron, backprop, structure, deep-turn, toolkit, pretraining, prediction, seq2seq, embeddings. |
| `jurafsky2026speech` (and `jurafsky2026embeddings`, `jurafsky2026transformers`, `jurafsky2026masked`, `jurafsky2026ir`) | Own fetch (web.stanford.edu/~jurafsky/slp3/) for "Volume I: Large Language Models", release of August 19, 2026, chapter titles; pretraining ledger for "History TBD." (ch. 9, p. 16); bib notes for "page numbers will move" | |
| `hastie2009elements` | attention and adapting ledgers (pp. 192, 534); own fetch of the download page for the free PDF | |
| `zhang2023dive` | attention ledger (AT26: soft database lookup, Nadaraya-Watson); own fetch of d2l.ai for the table of contents and code | |
| `lecun2015deep` | structure and deep-turn ledgers (pp. 436-444, "authoritative secondary source written by three participants"; T11 order of events); read from Hinton's site | |

### Part I

| Key | Description from | Notes |
|---|---|---|
| `olazaran1993sociological` | neuron ledger table ("a published sociological history based on the literature and on interviews"; 1958 press and Minsky and Papert quoted through it); backprop chapter (LeCun 1988 quote, p. 392) | Not marked free (gwern.net copy). |
| `rumelhart1986learning` | backprop ledger (pp. 533-536); backprop chapter ("persuasive ... demonstrations") | Free: Hinton's site. |
| `griewank2012invented` | backprop ledger (pp. 389-400; Linnainmaa 1970) | Not marked free (mirror). |
| `schmidhuber2014deep` | backprop and structure ledgers ("a participant with a known position in priority debates"); arXiv 1404.7828v4 | |
| `hochreiter1997long` | structure ledger (pp. 1735-1780; vanishing error; forget gate from Gers et al. 2000, not fetched) | Not marked free (course copy). |

### Part II

| Key | Description from | Notes |
|---|---|---|
| `krizhevsky2012imagenet` | deep-turn ledger T16 (p. 2: sections "sorted according to our estimation of their importance"; 3.1 ReLU, 3.2 multiple GPUs); paginated 1-9 | |
| `russakovsky2015imagenet` | deep-turn ledger T13, T23 (2010-2014, human-error estimate from annotator A1, caveats); table row (arXiv v3, 43 pages; journal pagination differs) | |
| `baydin2018automatic` | toolkit ledger and chapter (p. 13 worked example; p. 18 frameworks); JMLR 1-43 | |
| `he2015deep` | depth chapter (degradation not overfitting, p. 1); deep-turn table (12 pages); depth chapter for the highway-network claim (`schmidhuber2022annotated`, p. 12) | |

### Part III

| Key | Description from | Notes |
|---|---|---|
| `shannon1948mathematical` | prediction ledger (Part I pp. 379-423; section 3 on p. 388); prediction chapter (ladder of approximations) | Free: Internet Archive. |
| `jelinek2009dawn` | prediction ledger ("first-hand account by the head of the IBM group ... written 25 to 35 years after the events"; pp. 483-494); chapter (1972; trigrams) | |
| `bengio2003neural` | embeddings ledger (pp. 1137-1155); chapter (curse of dimensionality, p. 1137) | |
| `mikolov2013efficient` | embeddings ledger and chapter (simpler models, analogy test) | |
| `levy2015improving` | embeddings chapter (quote, p. 211); ledger (TACL 3, pp. 211-225) | |
| `sutskever2014sequence` | seq2seq ledger (paginated 1-9) and chapter | |
| `bahdanau2015neural` | seq2seq ledger (arXiv v7, pp. 1-15) and chapter (fixed-length bottleneck) | |
| `sennrich2016neural` | tokens ledger (pp. 1715-1725); tokens chapter (BPE into GPT-2) | |

### Part IV

| Key | Description from | Notes |
|---|---|---|
| `vaswani2017attention` | attention ledger (arXiv v7 of 2 Aug 2023, pp. 1-15 with appendix; v1-v7 and NeurIPS PDF compared); anatomy ledger (header "NIPS 2017") | |
| `elhage2021mathematical` | anatomy ledger AN13, AND4 (residual stream; HTML, Transformer Circuits Thread) | The appendix says "the name this book uses", not that the paper coined it (AND4: Kaplan et al. 2020 used the term first). |

### Part V

| Key | Description from | Notes |
|---|---|---|
| `radford2018improving` | anatomy, pretraining ledgers (pp. 1-12; output layer added for fine-tuning) | |
| `devlin2019bert` | tokens ledger (pp. 4171-4186); pretraining chapter (masked words); `bommasani2021opportunities` p. 5 quote from pretraining chapter | |
| `brown2020language` | scale ledger (pp. 1-75); training ledger (sections 2.1-2.3, pp. 8-9); evaluation ledger (section 4, pp. 29-32) | |
| `kaplan2020scaling`, `hoffmann2022training` | scale ledger (pp. 1-30; pp. 1-36); scale chapter (quote, p. 1) | |
| `wei2022emergent`, `schaeffer2023emergent` | scale chapter (quotes, p. 7 and p. 1) | |
| `sutton2019bitter`, `brooks2019better` | scale ledger (author sites) and chapter ("moving the human intellectual work") | |
| `grattafiori2024llama` | training, scale, tools ledgers (sections 3.1-3.4, 4.3.5 read across chapters) | |

### Part VI

| Key | Description from | Notes |
|---|---|---|
| `ouyang2022training` | instructions ledger (arXiv v1, 68 pp.); destination chapter (three steps, p. 3) | |
| `rafailov2023direct` | instructions chapter (quote, p. 1) | |
| `casper2023open` | instructions ledger (32 authors) and chapter ("fundamental", pp. 6-7, 9) | |
| `wei2022chain` | prompting chapter (definition; three explanations pp. 5-6; 56.9% p. 20; "state-of-the-art" p. 1) | Per the independent check: arXiv v1 (28 Jan 2022) uses only LaMDA 137B and has no PaLM results, no "state of the art", and no 56.9%; v2 (6 Apr 2022) first adds PaLM 540B (58.1%); the wording and 56.9% are from the final version, v6. The appendix says "in the paper's final version" and no longer dates the claim to January 2022. |
| `hu2021lora` | adapting chapter | |
| `lewis2020retrieval` | tools chapter (named RAG; closed-book/open-book p. 5) | |
| `yao2023react` | tools chapter (quote pp. 1, 3; failure counts) | |
| `greshake2023not` | prompting and tools chapters | |

### Part VII

| Key | Description from | Notes |
|---|---|---|
| `frantar2023gptq` | local chapter (round-to-nearest fails "at higher rates", p. 2; 3-bit result, p. 7) | |
| `osi2024osaid` | local ledger (published 2024-10-28) and chapter (requirements) | |
| `liang2023holistic` | evaluation chapter (79.1% vs 30.2%, p. 9); ledger (TMLR 08/2023) | |
| `chiang2024chatbot`, `singh2025leaderboard`, `lmarena2025response` | evaluation chapter and ledger | |
| `sajadieh2026ai` | evaluation ledger (April 2026, 425 pp.; aggregates other evaluators' results, pp. 94-95; saturation, p. 78) | |
| `deepseekai2025r1v2`, `deepseekai2025r1` | frontier ledger table (v2 86 pages; v1 vs v2 "15.6% to 71.0%" vs "77.9%"); FR12 (limitations) | |
| `kwa2025measuring` | frontier ledger table (v4 10 Jul 2026, footer "Preprint. Under review.") | |
| `bengio2026international`, `narayanan2025normal` | frontier chapter (quotes; "over 100 experts") | |

### How to read a paper and a model card

| Key | Used for | From |
|---|---|---|
| `keshav2007read` | the three passes | Own fetch; see below. Now in `references.bib`. |
| `hendrycks2021measuring` | MMLU random baseline 25% (p. 5); GPT-3 43.9% (p. 2) | evaluation ledger EV7 note; evaluation chapter |
| `openai2023gpt4` | GSM8K 92.0% with training-set mixing (pp. 7, 29) | evaluation chapter |
| `kingma2015adam` | nine versions; v1 and v9 headers | toolkit ledger table row |
| `deepseekai2025r1`, `deepseekai2025r1v2` | the changed number | frontier ledger table row |
| `radford2019language`, `openai2019gpt2code` | 117M vs 124M | anatomy chapter |
| `russakovsky2015imagenet` | arXiv vs journal pagination | deep-turn ledger table row |
| `wang2019glue`, `wang2019superglue` | "beyond the capabilities"; passed by July 2019 | evaluation chapter. Per the independent check, the GLUE sentence is in arXiv v2 (18 Sep 2018) as well as v3, so "In 2018" holds. |
| `sajadieh2026ai` | "often remain useful for only a few years" (p. 78) | evaluation chapter |
| `lawsen2025comment`, `shojaee2025illusion` | dispute and reply in v3 | frontier chapter and ledger FR17 |
| `mitchell2019model` | definition (p. 1); template (p. 3), "May not be possible to provide in practice" | evaluation and local chapters |
| `huggingface2026modelcards`, `huggingface2026hub`, `huggingface2026gated`, `huggingface2026api` | card as README; uploads by others; gated access; inherited license | local chapter |
| `openai2024o1card` | example of a system card, dated December 2024 | frontier ledger table ("title page dated December 5, 2024") |
| `meta2024llama31card` | knowledge cutoff December 2023, release 23 July 2024 | tools chapter |
| `qwen2026qwen38card`, `mistral2026large4card`, `moonshot2026kimik31card` | cards with no release date (as of 2026-11-11) | frontier ledger table ("No release date stated"); frontier chapter |
| `meta2024llama32card` | context length on the card, not the name; last commit 2024-10-24 | local chapter; local ledger table row |

## Claims verified this session

All fetched 2026-11-11 with curl into the scratchpad; text extracted with Python (HTML) or pdftotext (PDF).

### FD1. Keshav, "How to Read a Paper" (2007)
- Source: `keshav2007read`, http://ccr.sigcomm.org/online/files/p83-keshavA.pdf (2 pages; SHA-256 e3d97831bc19b60af9798bb6f0619b18bb886c0afb6ad3fc7a8b2f97512d32f7). Footer of each page: "ACM SIGCOMM Computer Communication Review", page number (83, 84), "Volume 37, Number 3, July 2007". Author line: "S. Keshav, David R. Cheriton School of Computer Science, University of Waterloo".
- p. 83, abstract: "this skill is rarely taught"; introduction: "Learning to efficiently read a paper is a critical but rarely taught skill."
- p. 83, first pass: "This pass should take about five to ten minutes and consists of the following steps: 1. Carefully read the title, abstract, and introduction 2. Read the section and sub-section headings, but ignore everything else 3. Read the conclusions 4. Glance over the references". The five Cs: "Category: What type of paper is this? ... Context: Which other papers is it related to? ... Correctness: Do the assumptions appear to be valid? ... Contributions: What are the paper's main contributions? ... Clarity: Is the paper well written?"
- p. 83, second pass: "read the paper with greater care, but ignore details such as proofs"; "Look carefully at the figures, diagrams and other illustrations in the paper. Pay special attention to graphs. Are the axes properly labeled? Are results shown with error bars, so that conclusions are statistically significant?"
- p. 84: "The second pass should take up to an hour."
- p. 84, third pass: "The key to the third pass is to attempt to virtually re-implement the paper"; "This pass can take about four or five hours for beginners, and about an hour for an experienced reader."
- Used: the three-pass paragraph of "How to read a machine-learning paper".

### FD2. Deep Learning web site
- Source: https://www.deeplearningbook.org/ (landing page).
- Quotes: "An MIT Press book"; "The online version of the book is now complete and will remain available online for free."; "Can I get a PDF of this book? No, our contract with MIT Press forbids distribution of too easily copied electronic formats of the book." Table of contents: "1 Introduction", "Part I: Applied Math and Machine Learning Basics" (chapters 2-5: Linear Algebra; Probability and Information Theory; Numerical Computation; Machine Learning Basics), "Part II: Modern Practical Deep Networks" (6-12: Deep Feedforward Networks; Regularization; Optimization; Convolutional Networks; Sequence Modeling: Recurrent and Recursive Nets; Practical Methodology; Applications), "Part III: Deep Learning Research" (13-20, including Representation Learning and Deep Generative Models).

### FD3. Speech and Language Processing web site
- Source: https://web.stanford.edu/~jurafsky/slp3/ (landing page).
- Quotes: "Speech and Language Processing (3rd ed. draft) Dan Jurafsky and James H. Martin"; "Here's our August 19, 2026 release!"; "Volume I: Large Language Models" (chapters 1-8, including "3: N-gram Language Models", "5: Embeddings", "7: Transformers and Pretraining", "8: Post-training"); "Volume II: Advanced LLM Topics and Tools" (including "9: Masked Language Models", "11: Information Retrieval and RAG", "12: Agents [not written yet]"); "When will the book be finished? Don't ask." The page offers the chapters and a single PDF of the whole draft.

### FD4. The Elements of Statistical Learning download page
- Source: https://hastie.su.domains/ElemStatLearn/ (a frameset; content in main.html).
- Quote (main.html): "The Elements of Statistical Learning: Data Mining, Inference, and Prediction. Second Edition February 2009 Trevor Hastie Robert Tibshirani Jerome Friedman ... Download the book PDF (corrected 12th printing Jan 2017)".

### FD5. Dive into Deep Learning web site
- Source: https://d2l.ai/ (landing page, "Dive into Deep Learning 1.0.3 documentation").
- Table of contents includes "3.4. Linear Regression Implementation from Scratch", "3.5. Concise Implementation of Linear Regression", chapters 7-10 on convolutional and recurrent networks, "11. Attention Mechanisms and Transformers" (11.1 "Queries, Keys, and Values" to 11.9 "Large-Scale Pretraining with Transformers"), "12. Optimization Algorithms". Header links: "PyTorch", "MXNet", "Notebooks".

## Open points for the independent check

- Confirm the "Free" markings against the policy in Method (Shannon's Internet Archive copy is marked free; the third-party copies are not).
- The appendix uses `keshav2007read`, which is now in `references.bib`.
- The appendix runs longer than the outline's "~4 pp" budget (see the build note in the drafting report).

## Independent check (further-reading appendix)

2026-11-11. A separate agent checked the appendix's entries and sourced claims against the verified chapters, ledgers, and sources. Its report shows it consulted the arXiv version histories of `wei2022chain` and `wang2019glue`, the pagination of Shannon's July 1948 installment, Google DeepMind's model-card listings, and `references.bib`, and checked the reading list's counts and descriptions. Its corrections were applied by a third agent.

- Errors found and fixed:
  1. Chain-of-thought was dated "January 2022" with "state-of-the-art accuracy" at 56.9%, but arXiv v1 (28 Jan 2022) has neither the phrase, PaLM, nor 56.9%; now "In 2022, chain-of-thought prompting of the 540-billion-parameter PaLM ... 56.9% in the paper's final version".
  2. Shannon: "Part I as a whole runs to 45 pages" was wrong (the July 1948 installment, pp. 379-423, holds Part I and the start of Part II on p. 406); now "The July 1948 installment, the half this book read, runs to 45 pages".
  3. "The prompt format alone can move a score by tens of points" overstated HELM p. 9 (format and number of examples both changed); now "How the prompt is built, its format and how many examples it shows"; the HELM entry now says "depending on how the question was put into the prompt".
  4. "A model offered only as a service has no downloadable card" was wrong as of 2026-11 (Google DeepMind lists model cards for service-only models); now "has no repository; its maker may publish a technical report, a document it calls a model card, or a 'system card'". `openai2024o1card` confirmed in `references.bib` (title page 5 December 2024).
- Warnings acted on: "about fifty works in some forty entries"; Deep Learning has "an introduction and nineteen chapters in three parts"; "Many papers in this field appear first on arXiv"; "some PDFs print no page numbers, and proceedings PDFs often number from 1 rather than as in the bound volume"; "As of 2026-11" in place of "As of this writing"; full titles for `devlin2019bert`, `rafailov2023direct`, `greshake2023not`, `frantar2023gptq`, and `chiang2024chatbot`, taken from `references.bib`; stale notes about `keshav2007read` updated (it is now in `references.bib`).
- Not changed: the optional April 2022 sentence (PaLM 540B at 58.1% in v2) was not added.
- Could not verify: the checker did not re-fetch the descriptions that rest only on ledgers (Olazaran, Griewank, Hochreiter, Schmidhuber's content, Elhage, Lewis, Yao, Frantar, Grattafiori, Ouyang, Rafailov, Casper, Sutton and Brooks content, the International AI Safety Report and Narayanan quotes, the Hugging Face docs, and the Llama, Qwen, Mistral and Kimi cards); they agree with the verified chapters and ledgers. The GPT-4 report and SuperGLUE page numbers were checked against the chapters only.

## Style pass (2026-11-11)

Reader call-outs made generic per D-023.

- "This appendix is for the reader who wants to go further." -> "This appendix is a guide to going further."
- "whose main ideas this book has prepared you for;" -> "whose main ideas this book has covered;"
- "The reference this book's reader may already own, cited here" -> "A reference text on statistical learning, cited here"
- "Because of the code it suits a Book 2 reader best." -> "Because of the code it pairs best with Book 2."
- "a glance at the references; after it you should know what kind of paper it is," -> "a glance at the references; it should establish what kind of paper it is,"
- "For this book's reader, the first two passes are usually enough," -> "For the purposes of this book, the first two passes are usually enough,"
