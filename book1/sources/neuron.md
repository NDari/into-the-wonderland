# Claim ledger: neuron

Chapter: `neuron` (Book 1, "The artificial neuron (1943-1969)").
Stage: verified, 2026-11-11 [D-005]. Locations added while drafting are logged as "Also used" under their claim.

All sources were fetched on 2026-11-11 and each claim was located in the fetched text or, for the scanned Widrow and Hoff paper, read on the page image. Page numbers are the printed page numbers of the source as read. Where only a PDF page is available, that is said. Quotes from scanned sources are given with OCR spacing and line-break hyphens repaired (for example "in depth" for "indepth"); spelling errors in the original, such as "sytem", are kept.

## Sources and how they were read

| Key | Read from | Notes |
|---|---|---|
| `mcculloch1943logical` | https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf | The 1990 reprint in *Bulletin of Mathematical Biology* 52, pp. 99-115. Its first-page footnote says "Reprinted from the Bulletin of Mathematical Biophysics, Vol. 5, pp. 115-133 (1943)". Pages cited are the reprint's. |
| `hebb1949organization` | https://archive.org/details/in.ernet.dli.2015.168156 (OCR text) | Title page: Wiley, New York, "COPYRIGHT, 1949". Page found from the running heads around the passage. |
| `rosenblatt1958perceptron` | https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf | Scan of *Psychological Review* 65(6), with a text layer. The printed page is PDF page + 385. |
| `widrow1960adaptive` | https://www-isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf | Scan with no text layer. Read as page images, and the quotes were cross-checked against Tesseract OCR of the same pages. Venue and pages from Olazaran's reference list, p. 424. |
| `olazaran1993sociological` | https://gwern.net/doc/ai/nn/1993-olazaran.pdf | First page footer: "ADVANCES IN COMPUTERS, VOL. 37 335 Copyright 1993 by Academic Press". The printed page is PDF page + 334. An authoritative secondary source: a published sociological history based on the literature and on interviews. |
| `goodfellow2016deep` | https://www.deeplearningbook.org/contents/intro.html and /contents/mlp.html | Authors and publisher from the site's citation entry. Pages from the web version's page markers. |
| `nyt1958brain` | not fetchable | "Electronic 'brain' teaches itself", New York Times, 13 July 1958, iv9:6 (Olazaran's reference list, p. 422). Source of the IBM 704 and ninety-seven-of-100 passage, quoted by Olazaran on pp. 341-342. |
| `nyt1958navy` | not fetchable | nytimes.com returns 403. Quoted through `olazaran1993sociological`, p. 341, which gives the reference as "New York Times, July 8, 25:2" (p. 422). |
| `minsky1969perceptrons` | not fetchable | A book still in copyright. Quoted through `olazaran1993sociological`; bibliographic details from its reference list, p. 422. |

Not fetched: Olazaran 1996 (*Social Studies of Science*, paywalled), and Nilsson's *The Quest for Artificial Intelligence* (the Stanford host was unreachable and the archive copy was rate-limited). Olazaran 1993 covers the same ground as Olazaran 1996 and is used instead.

## Sourced claims

### N1. McCulloch and Pitts (1943): a neuron as an all-or-none threshold unit, so nets of neurons can be described by logic
- Source: `mcculloch1943logical`
- Location: abstract, p. 99; assumptions, p. 101.
- Quotes: "Because of the "all-or-none" character of nervous activity, neural events and the relations among them can be treated by means of propositional logic." (p. 99). "At any instant a neuron has some threshold, which excitation must exceed to initiate an impulse." (p. 99). The five assumptions (p. 101): "(1) The activity of the neuron is an "all-or-none" process. (2) A certain fixed number of synapses must be excited within the period of latent addition in order to excite a neuron at any time, and this number is independent of previous activity and position on the neuron. (3) The only significant delay within the nervous sytem is synaptic delay. (4) The activity of any inhibitory synapse absolutely prevents excitation of the neuron at that time. (5) The structure of the net does not change with time."
- Note: assumption (5) matters for the chapter's story. The 1943 neuron does not learn; its connections are fixed. Inhibition is absolute veto, not a negative weight. The chapter should not present the 1943 unit as having adjustable, signed weights.

### N2. Hebb (1949): connections that take part in firing are strengthened
- Source: `hebb1949organization`
- Location: chapter 4, "The First Stage of Perception: Growth of the Assembly" (pp. 60-78 per the table of contents), p. 62.
- Quote: "When an axon of cell A is near enough to excite a cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A's efficiency, as one of the cells firing B, is increased."
- Also used: the title page gives "D. O. HEBB McGill University", the source for "of McGill University".
- Note: Hebb states it as an assumption ("The assumption can be precisely stated as follows"), a hypothesis about biology, not an algorithm.

### N3. Rosenblatt (1958): the perceptron, a hypothetical nervous system or machine, developed under Navy sponsorship and simulated on an IBM 704
- Source: `rosenblatt1958perceptron`
- Location: pp. 386, 387, 403.
- Quotes: "The theory has been developed for a hypothetical nervous system, or machine, called a perceptron." (p. 387). Footnote: "The development of this theory has been carried out at the Cornell Aeronautical Laboratory, Inc., under the sponsorship of the Office of Naval Research" (p. 386). "Bivalent systems similar to those illustrated in Fig. 12 have been simulated in detail in a series of experiments with the IBM 704 computer at the Cornell Aeronautical Laboratory." (p. 403). He calls his position "the empiricist, or "connectionist" position" (p. 387).
- Also used: "Stimuli impinge on a retina of sensory units (S-points)" and "Impulses are transmitted to a set of association cells (A-units)" (p. 389); the R-units (response units) appear on p. 390.
- Note: the 1958 perceptron has sensory points, association units, and response units with reinforcement. The textbook "single neuron with the perceptron learning rule" is a simplification of it. Olazaran (N6) describes that simplification as "the adjustable part of the original perceptron after removing the sensory-to-association fixed connections".

### N4. The 1958 press coverage
- Source: `nyt1958navy`, as quoted in `olazaran1993sociological`, p. 341.
- Correction from the independent check: Olazaran quotes two different articles here. The "walk, talk" block is cited as New York Times 1958a (8 July, p. 25); the IBM 704 block is cited as 1958b (13 July, section IV, p. 9). The chapter now cites `nyt1958navy` and `nyt1958brain` separately.
- Quote: "The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence . . . Later Perceptrons will be able to recognize people and call out their names and instantly translate speech in one language to speech and writing in another language, it was predicted." Also from the same article: "The concept of the Perceptron was demonstrated on the Weather Bureau's $2,000,000 IBM 704. In one experiment, the 704 computer was shown 100 squares situated at random either on the left or on the right side of a field. In 100 trials, it was able to 'say' correctly ninety-seven times whether the square was situated on the right or left."
- Also used: Olazaran's own comment, p. 342: "the perceptron was distinguishing between right and left, but it was not recognizing the squares as the same object".
- Note: the chapter must say the article is quoted through Olazaran. Attribute the prediction to the article ("it was predicted"), not to Rosenblatt.

### N5. The Mark I perceptron: hardware built at Cornell Aeronautical Laboratory, funded by the Office of Naval Research
- Source: `olazaran1993sociological`
- Location: p. 339.
- Quote: "At that time, a team of researchers started to build the Mark 1 perceptron at Cornell Aeronautical Laboratory (CAL, Buffalo, New York ...) funded by the Office of Naval Research (ONR). The perceptron was a feedforward neural network machine with one layer of adjustable connections."

### N6. Learning rules of 1960 and the perceptron convergence theorem
- Source: `olazaran1993sociological`
- Location: p. 340.
- Quotes: "Two learning algorithms for single-layer neural networks were developed in 1960, one by Rosenblatt (1960) himself, and the other one by Widrow and Hoff (1960)." "Rosenblatt's (1960, 1962a, ch. 5) "perceptron convergence theorem" showed that if a perceptron was physically capable of performing a classification task then that perceptron could be "taught" that task in a finite number of training cycles." He quotes Rosenblatt 1962, p. 111: "beginning from an arbitrary initial state, an error correction procedure . . . will always yield a solution to C(W) in finite time".
- Also, p. 345, Minsky on the theorem, quoted from Bernstein (1981): "Rosenblatt's conjecture turned out to be mathematically correct, in fact. . . However, I started to worry about what such a machine could not do."

### N7. Widrow and Hoff (1960): ADALINE, adjusting weights to reduce the error
- Source: `widrow1960adaptive`, read on the page images.
- Location: pp. 96-97.
- Quotes: "An adaptive pattern classification machine (called "Adaline", for adaptive linear) has been constructed for the purpose of illustrating adaptive behavior and artificial learning." "A photograph of this machine, which is about the size of a lunch pail, is shown in Fig. 2." Training patterns are set on "the 4x4 input switch array", and the machine's "total experience is stored in the values of the weights a0 ... a16" (p. 97). Its element: "a linear combination of the input signals is formed. The weights are the gains a1, a2, ..., which could have both positive and negative values. The output signal is +1 if this weighted sum is greater than a certain threshold, and -1 otherwise." (p. 96). Each gain is changed "in the direction which will diminish the error by an amount which reduces the error magnitude by 1/17. The 17 gains may be changed in any sequence, and after all changes are made, the error for the present input pattern is zero." (p. 97). The error is read by an operator on a meter, and "Electronic automation of this procedure will be discussed below" (p. 97). The threshold weight a0 has its "input ... permanently connected to a +1 source" (p. 96), so a1 to a16 serve the 16 switches.
- Also used: footnotes on p. 96 give both authors' affiliation as the Department of Electrical Engineering, Stanford University, with Hoff as "Doctoral student". The objective is "the minimization of the average number of errors" (p. 96). The Adaline procedure is analysed in section E: "The simple adaption procedure described in this paper minimizes" the mean square error (p. 98, symbols omitted), and "The method of searching that has proven most useful is the method of steepest descent" (p. 99). (On p. 97 the phrase "mean square error" belongs to section D, a different system, and is not the source for the Adaline claim.)
- Also: `goodfellow2016deep`, ch. 1, p. 14, links ADALINE to the modern method: "The training algorithm used to adapt the weights of the ADALINE was a special case of an algorithm called stochastic gradient descent." Also p. 14: "Slightly modified versions of the stochastic gradient descent algorithm remain the dominant training algorithms for deep learning models today." The chapter dates this to the book's 2016 publication. And p. 14: "Models based on the f(x, w) used by the perceptron and ADALINE are called linear models", the source for the textbook sense of "perceptron". Note: stochastic gradient descent is not defined until `toolkit`. If it is mentioned here, it is only to say that it returns later.
- Note: Olazaran (p. 340, footnote) contrasts the two rules: "LMS minimized error as summed over all the output units". "LMS" (least mean squares) is the usual name for the Widrow and Hoff rule.

### N8. XOR is not linearly separable, so a single-layer perceptron cannot compute it
- Sources: `olazaran1993sociological`, pp. 351-352; `goodfellow2016deep`, ch. 6, pp. 167-168.
- Quotes: "The typical example here is the exclusive-or function. The problem of the exclusive-or logical function is often shown in the simplest possible neural network: a device with two input units and one output unit" (Olazaran, p. 351). "This system can only realize linearly separable functions, and exclusive-or is not linearly separable." (Olazaran, p. 352). "When exactly one of these binary values is equal to 1, the XOR function returns 1. Otherwise, it returns 0." (Goodfellow et al., p. 167). "linear model is not able to represent the XOR function" (Goodfellow et al., p. 168).
- Note: the impossibility itself is also a mechanism claim. The worked example checks it numerically (see below).

### N9. Minsky and Papert (1969): what *Perceptrons* proved and what it only judged
- Source: `minsky1969perceptrons`, as quoted and analysed in `olazaran1993sociological`.
- Location: Olazaran pp. 358-359 (the two issues), p. 367 (the quotation), p. 348 (connectedness).
- Quotes: "I would like to distinguish two different issues in Minsky and Papert's arguments ... One is their work on the limitations of single-layer perceptrons. The other is their "intuitive judgement" (in their own words) about the possibility of developing a learning algorithm for multilayer perceptrons." (p. 358). "Some of the main problems of the single-layer perceptron analyzed in depth by Minsky and Papert, e.g., the parity and connectedness problems" (p. 359). Minsky and Papert 1969, pp. 231-232, as quoted on p. 367: "There is no reason to suppose that any of these virtues carry over to the many-layered version. Nevertheless, we consider it to be an important research problem to elucidate (or reject) our intuitive judgement that the extension is sterile."
- Note: XOR is the two-input case of parity. The chapter can say Minsky and Papert analysed parity, of which XOR is the smallest case. It should not say "Minsky and Papert proved perceptrons cannot do XOR" as if that were their discovery.

### N10. Disputed history: did *Perceptrons* cause the decline?
Two views, to be presented side by side and not adjudicated:
- **The common account:** `goodfellow2016deep`, ch. 1, p. 14: "Critics who observed these flaws in linear models caused a backlash against biologically inspired learning in general (Minsky and Papert, 1969). This was the first major dip in the popularity of neural networks." Also ch. 6, p. 221: "Critics including Marvin Minsky pointed out several of the flaws of the linear model family, such as its inability to learn the XOR function, which led to a backlash against the entire neural network approach."
- **The sociological account:** `olazaran1993sociological`, p. 358: "In popular versions of the history of neural networks, Minsky and Papert's Perceptrons study is usually taken as the proof that neural network research had so many problems that it was not worth pursuing, and that therefore it had to be abandoned. However, in my opinion, that common view" is too simple. His account (pp. 358-359) is that the single-layer limits were real results, the multilayer verdict was a judgment, and the problems became decisive because of how the community interpreted them, "not because of some intrinsic or necessary property".
- Also used: p. 346, Olazaran's account of the motive: symbolic AI researchers "saw neural network researchers' efforts to obtain funding for building more complex machines as a direct threat to their research interests. In this context, two of them, Marvin Minsky and Seymour Papert, decided to carry out a study that would show the limitations of neural networks beyond doubt." (The source sets the names off with dashes; they are written here with commas.) This is part of the sociological account and is attributed to Olazaran in the text. His sources include interviews; the table of contents lists "Appendix 1. List of Those Interviewed" (p. 335).
- Also used, Olazaran's timing argument: the main arguments "were well known by the mid-1960s and had critically affected the development of neural network research by then", and the book was "the 'final push,' so to speak, for the closure of the controversy" (p. 357). "that common view was the result of the closure of the perceptron controversy, and not its cause" (p. 358). The SRI group gave up perceptrons by the mid-1960s (p. 372, quoting Minsky).
- Also used: p. 352, "Early neural network researchers knew that a solution to some of the problems of single-layer networks was possible by introducing a layer of hidden units ... The problem was that no weight modification rule had been developed for multilayer networks". Parity and connectedness are defined on p. 361.
- Supporting detail, p. 373: a researcher at SRI recalls that moving from neural networks to symbolic AI meant selling a robot project to ARPA, "to some of the people who didn't like perceptrons".
- Also: Rosenblatt himself listed the "figure-ground" or "connectedness" problem as among the hardest open problems in 1962 (Olazaran, pp. 348-349, quoting Rosenblatt 1962).

### N11. The neuron in the long view: the first wave
- Source: `goodfellow2016deep`, ch. 1, p. 13, Figure 1.7 caption.
- Quote: "The first wave started with cybernetics in the 1940s-1960s, with the development of theories of biological learning (McCulloch and Pitts, 1943; Hebb, 1949) and implementations of the first models such as the perceptron (Rosenblatt, 1958)". (The source prints the year range with an en-dash; it is written here with a hyphen.)

## Independent check

2026-11-11. A separate agent that did not write the chapter fetched every source itself and checked every claim, quote, page, number, and figure.

- Confirmed: N1 to N11 apart from the items below. All worked-example numbers match `code/checks/neuron.py`, the figures regenerate byte-identically, and the mechanism explanations are correct.
- Errors found and fixed:
  1. The Widrow and Hoff misquote ("weightings" should be "weights").
  2. The IBM 704 passage came from a second New York Times article (13 July), not the 8 July one. It is now cited as `nyt1958brain`.
  3. A dropped comma in the Goodfellow et al. quote; the quote now runs to "enabling the training of a single neuron".
  4. "Mean square error" was cited to p. 97, where the phrase is about a different system. The citation is now pp. 98-99.
  5. The representation half of a claim needed Olazaran p. 352, not only p. 358.
- Warnings acted on:
  - Olazaran's timing argument (pp. 357-358) is added to the sociological account, and the SRI anecdote is dated to the mid-1960s, so the narrator no longer states the common account's chronology as agreed fact.
  - The point of disagreement is reframed as cause and timing.
  - "began" becomes "said".
  - The Mark I adjustable connections are reworded with pp. 339-340.
  - The textbook sense of "perceptron" is attributed to Goodfellow et al.
  - The p. 221 quote is restored with its antecedent.
  - Parity and connectedness are cited to pp. 359 and 361.
  - The Minsky quote is identified as from a 1981 New Yorker profile.
  - Hebb's rule is reworded closer to his causal wording.
  - Threshold is defined as minus the bias.
  - The softmax sentence is corrected.
  - "For a few epochs" becomes "from the first epoch to the second".
  - "Feedforward", "hidden units", and "cybernetics" are now glossed or avoided.
  - Perceptron and ADALINE are now bolded at their definitions.
- Re-checked after fixing: the writer located every new quote in the same fetched texts (Widrow-Hoff page images and OCR for pp. 96, 98, and 99; Olazaran pp. 341-342, 352, 357, 358, 361, and 372; Goodfellow et al. p. 13).
- Not verifiable: the two New York Times articles, *Perceptrons*, Bernstein's 1981 profile, and Rosenblatt 1962 are known only through Olazaran's quotations.

## Worked examples [D-009]

All computed by `code/checks/neuron.py` (standard library only). The weights and inputs are chosen for illustration; the arithmetic is exact.

- Example 1: a three-input weighted vote (sum +0.1, step output 1, sigmoid 0.525).
- Example 2: AND and OR with weights 1 and 1, biases -1.5 and -0.5.
- Example 3: the perceptron rule learning AND from zero: 10 mistakes over 5 epochs, none in epoch 6, final weights 2 and 1, bias -2.
- Example 4: the same rule on XOR: mistakes per epoch 2, 3, then 4 for every epoch through 20.
- Example 5: a grid of 15,625 weight and bias combinations: 364 compute AND, 650 compute OR, 0 compute XOR.
- Example 6: the AND neuron with a sigmoid (0.182, 0.378, 0.378, 0.622), and with everything multiplied by 10 (0.000, 0.007, 0.007, 0.993).
- Example 7: XOR from two layers: OR and AND feeding a neuron with weights +1 and -1 and bias -0.5.

## Figures [D-014]

Drawn by `figures/neuron.py`, which imports the check script so its numbers cannot drift.

- `figures/neuron-vote.svg`: Example 1 as a weighted vote.
- `figures/neuron-xor.svg`: AND, OR, and XOR on the four input points, with the boundary lines of Example 2.

## Terms defined in this chapter

For the glossary: artificial neuron, weight, bias, weighted sum, activation function, step function, threshold, sigmoid, parameters (from `destination`), AND, OR, perceptron, perceptron learning rule, epoch, perceptron convergence theorem, ADALINE, decision boundary, linearly separable, XOR, parity, connectedness.

## Scope notes for drafting

- Olazaran (p. 340) notes Rosenblatt's 1960 report also introduced a learning procedure. The text should credit the 1960 learning rules to both groups, not to the 1958 paper alone.
- The "first winter" is to be told through N10 only. A broader AI-winter story (for example the UK's 1973 Lighthill report) belongs to AI in general, has not been researched, and is out of scope here.
