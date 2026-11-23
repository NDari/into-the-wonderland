# Claim ledger: backprop

Chapter: `backprop` (Book 1, "Learning in layers (1970-1989)").
Stage: verified, 2026-11-11 [D-005]. Locations added while drafting are logged as "Also used".

All sources were fetched on 2026-11-11 and each claim was located in the fetched text. Quotes from scanned sources are given with OCR spacing and line-break hyphens repaired.

## Sources and how they were read

| Key | Read from | Notes |
|---|---|---|
| `rumelhart1986learning` | https://www.cs.utoronto.ca/~hinton/absps/naturebp.pdf | A scan with no text layer, OCR'd with Tesseract. Header: "NATURE VOL. 323 9 OCTOBER 1986". The letter starts on p. 533, partway down the first scanned page (the top of that page ends the previous article). PDF pages 1-4 = pp. 533-536. |
| `rumelhart1986internal` | https://gwern.net/doc/ai/nn/fully-connected/1986-rumelhart.pdf | Chapter 8 of the PDP volume, "Learning internal representations by error propagation". A scan with a text layer. Printed page = PDF page + 317 (pp. 318-362). The book's title page is not in the scan. |
| `schmidhuber2014deep` | https://arxiv.org/pdf/1404.7828v4 | A survey by a participant in the history (an authoritative secondary source, with a known position in priority debates). Page numbers are the PDF's own. |
| `griewank2012invented` | https://papers.baulab.info/papers/also/Griewank-2012.pdf (the EMIS mirror was unreachable) | *Documenta Mathematica*, Extra Volume ISMP (2012), pp. 389-400. Printed page = PDF page + 388. Authoritative secondary: a history of automatic differentiation by one of its main researchers. |
| `cybenko1989approximation` | https://documents.epfl.ch/groups/i/ip/ipg/www/2015-2016/Reading%20Group%20on%20Deep%20Neural%20Nets/Cybenko_MCSS.pdf | Header: "Math. Control Signals Systems (1989) 2:303-314". Printed page = PDF page + 302. |
| `hornik1989multilayer` | https://cognitivemedium.com/magic_paper/assets/Hornik.pdf | Header (OCR-damaged): "Neural Networks, Vol. 2, pp. 359-366, 1989". Printed page = PDF page + 358. |
| `olazaran1993sociological` | as in `book1/sources/neuron.md` | Printed page = PDF page + 334. |
| `goodfellow2016deep` | https://www.deeplearningbook.org/contents/mlp.html | Pages from the web version's page markers. The publisher (MIT Press) is from the site's home page ("An MIT Press book"), not the chapter page. |

Not fetched: Werbos's 1974 Harvard thesis, Linnainmaa's 1970 thesis (in Finnish) and his 1976 paper, and Parker 1985 and LeCun 1985. All are described here through `griewank2012invented`, `schmidhuber2014deep`, `olazaran1993sociological`, and `goodfellow2016deep`, and the chapter must say so.

## Sourced claims

### B1. The problem: how to adjust weights into hidden units ("credit assignment")
- `schmidhuber2014deep`, p. 4: "Which modifiable components of a learning system are responsible for its success or failure? What changes to them improve performance? This has been called the fundamental credit assignment problem (Minsky, 1963)."
- `rumelhart1986learning`, p. 533: learning "becomes more interesting but more difficult when we introduce hidden units whose actual or desired states are not specified by the task." And on the perceptron: "In perceptrons, there are 'feature analysers' between the input and output that are not true hidden units because their input connections are fixed by hand, so their states are completely determined by the input vector: they do not learn representations."
- `olazaran1993sociological`, p. 392: "The error made by the units in the output layer is easy to calculate. ... The main problem is therefore to calculate the derivatives of the error with respect to the outputs of the hidden units."

### B2. Rumelhart, Hinton, and Williams (1986): back-propagation
- `rumelhart1986learning`, p. 533 (abstract): "We describe a new learning procedure, back-propagation, for networks of neurone-like units. The procedure repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the difference between the actual output vector of the net and the desired output vector. As a result of the weight adjustments, internal 'hidden' units which are not part of the input or output come to represent important features of the task domain". And: "The ability to create useful new features distinguishes back-propagation from earlier, simpler methods such as the perceptron-convergence procedure."
- Affiliations (p. 533): Rumelhart and Williams at the Institute for Cognitive Science, University of California, San Diego; Hinton at the Department of Computer Science, Carnegie-Mellon University.
- Total error (p. 534): the error compares "the actual and desired output vectors for every case"; it is a sum of squared differences over cases and output units (equation 3).
- An example (p. 534, Fig. 1 caption): a network that detects mirror symmetry; "The learning required 1,425 sweeps through the set of 64 possible input vectors ... The initial weights were random and were uniformly distributed between -0.3 and 0.3."
- Also used, p. 535: "An alternative scheme, which we used in the research reported here, is to accumulate dE/dw over all the input-output cases before changing the weights"; "t is incremented by 1 for each sweep through the whole set"; "To break symmetry we start with small random weights. Variants on the learning procedure have been discovered independently by David Parker (personal communication) and by Yann Le Cun".
- Their caveat on brains (p. 536): "The learning procedure, in its current form, is not a plausible model of learning in brains."

### B3. The PDP chapter: the generalized delta rule, XOR, local minima, symmetry breaking
- `rumelhart1986internal`, p. 322: "We call this the generalized delta rule. From other considerations, Parker (1985) has independently derived a similar generalization, which he calls learning-logic. Le Cun (1985) has also studied a roughly similar learning scheme."
- p. 319: XOR "cannot be performed by networks without hidden units with which to create their own internal representations of the input patterns."
- p. 324, on the error surface: "without hidden units, the error surface is shaped like a bowl with only one minimum, so gradient descent is guaranteed to find the best set of weights. With hidden units, however, ... the error surface is not concave upwards, so there is the danger of getting stuck in local minima. The main theoretical contribution of this chapter is to show that there is an efficient way of computing the derivatives. The main empirical contribution is to show that the apparently fatal problem of local minima is irrelevant in a wide variety of learning tasks."
- p. 330, symmetry breaking: "If all weights start out with equal values and if the solution requires that unequal weights be developed, the system can never learn." (Hence random starting weights.)
- p. 330, momentum: "In most of our simulations a was about 0.9" (a is the momentum coefficient; "The momentum filters out the high curvature").
- p. 331, XOR in practice: they trained networks to "solve the XOR problem hundreds of times ... In only two cases has the system encountered a local minimum and thus been unable to solve the problem."
- Also `rumelhart1986learning`, p. 535: "experience with many tasks shows that the network very rarely gets stuck in poor local minima that are significantly worse than the global minimum."

### B4. Priority: the method existed before 1986 (disputed history; present, do not adjudicate)
- `griewank2012invented`, p. 389: the reverse mode "has been suggested by several people from various fields since the late 1960s, if not earlier. Seppo Linnainmaa (Lin76) of Helsinki says the idea came to him on a sunny afternoon in a Copenhagen park in 1970. He used it as a tool for estimating the effects of arithmetic rounding errors on the results of complex expressions. Gerardi Ostrowski (OVB71) discovered and used it some five years earlier in the context of certain process models in chemical engineering."
- `griewank2012invented`, p. 390: "Motivated by the special case of back-propagation in neural networks, Paul Werbos (Wer82) compared the forward and reverse propagation of derivatives".
- `schmidhuber2014deep`, p. 11: "Explicit, efficient error backpropagation (BP) in arbitrary, discrete, possibly sparsely connected, NN-like networks apparently was first described in a 1970 master's thesis (Linnainmaa, 1970, 1976), albeit without reference to NNs. BP is also known as the reverse mode of automatic differentiation (Griewank, 2012), where the costs of forward activation spreading essentially equal the costs of backward derivative calculation." (Also used: the last clause supports the chapter's statement about cost.) "Compare some preliminary, NN-specific discussion (Werbos, 1974, section 5.5.1) ... To my knowledge, the first NN-specific application of efficient BP as above was described in 1981 (Werbos, 1981, 2006). Related work was published several years later (Parker, 1985; LeCun, 1985, 1988). A paper of 1986 significantly contributed to the popularisation of BP for NNs (Rumelhart et al., 1986), experimentally demonstrating the emergence of useful internal representations in hidden layers." Also: gradient methods for "multi-stage, NN-related systems" had "been discussed at least since the early 1960s" in control (Kelley 1960, Bryson 1961, and others).
- `goodfellow2016deep`, ch. 6, p. 221: "Efficient applications of the chain rule based on dynamic programming began to appear in the 1960s and 1970s, mostly for control applications ... but also for sensitivity analysis (Linnainmaa, 1976). Werbos (1981) proposed applying these techniques to training artificial neural networks. The idea was finally developed in practice after being independently rediscovered in different ways (LeCun, 1985; Parker, 1985; Rumelhart et al., 1986a). The book Parallel Distributed Processing presented the results of some of the first successful experiments with back-propagation in a chapter (Rumelhart et al., 1986b) that contributed greatly to the popularization of back-propagation".
- `olazaran1993sociological`, p. 392: "it seems that the first attempt to apply something similar to back-propagation to neural network research was Paul Werbos'. ... In the early 1970s, Paul Werbos was carrying out Ph.D. research in applied mathematics at Harvard University." He called his technique "dynamic feedback" (Werbos, 1974). Footnote 39 quotes LeCun (1988): "back-propagation is little more than an extremely judicious application of the chain rule and gradient descent". Pp. 392-393: Werbos's account, from Olazaran's interview, of resistance from his Harvard committee and a discouraging meeting with Minsky. This is one participant's recollection and must be attributed as such.
- Also used: p. 394, Werbos's thesis applied dynamic feedback to a political-science example: "Werbos did not apply his dynamic feedback algorithm to neural networks in his thesis". pp. 393-394, Minsky's own interview account: "It's certainly trivial. The idea is how you do gradient descent. I didn't consider it practical" and "you usually get stuck at a local minimum".
- Also used: `schmidhuber2014deep` p. 1 (Preface): "One of its goals is to assign credit to those who contributed to the present state of the art."
- Note: the sources agree on the sequence (control theory in the 1960s; Linnainmaa 1970 for general reverse-mode differentiation; Werbos 1974 and 1981 for neural networks; Parker and LeCun 1985; Rumelhart, Hinton, and Williams 1986 for the demonstration that made it widely used). They differ in emphasis and in what counts as "inventing" it. The chapter should give the sequence with attributions and let the reader see that "who invented backprop" depends on what is meant.

### B5. Universal approximation, and what it does not promise
- `cybenko1989approximation`, p. 303 (abstract): "we show that arbitrary decision regions can be arbitrarily well approximated by continuous feedforward neural networks with only a single internal, hidden layer and any continuous sigmoidal nonlinearity."
- `cybenko1989approximation`, p. 313: "we have focused only on existence. The important questions that remain to be answered deal with feasibility, namely how many terms in the summation (or equivalently, how many neural nodes) are required to yield an approximation of a given quality?"
- `hornik1989multilayer`, p. 359 (abstract): "standard multilayer feedforward networks with as few as one hidden layer using arbitrary squashing functions are capable of approximating any Borel measurable function from one finite dimensional space to another to any desired degree of accuracy, provided sufficiently many hidden units are available."
- `hornik1989multilayer`, p. 360: "failures in applications can be attributed to inadequate learning, inadequate numbers of hidden units, or the presence of a stochastic rather than a deterministic relation between input and target. Our results do not address the issue of how many units are needed to attain a given degree of approximation."
- `goodfellow2016deep`, ch. 6, p. 195: "a feedforward network with a single layer is sufficient to represent any function, but the layer may be infeasibly large and may fail to learn and generalize correctly."
- Also used: `goodfellow2016deep` p. 194 names it "the universal approximation theorem (Hornik et al., 1989; Cybenko, 1989)".
- Note: the theorem is about representation, not learning. It does not say gradient descent will find the weights, how many units are needed, or that the network will generalize.

## Worked examples [D-009]

All computed by `code/checks/backprop.py` (standard library only). Every backpropagated gradient is checked against finite differences.

- Example 1: fitting y = w x to (1, 2), (2, 4), (3, 7) by gradient descent. Least-squares w = 2.214 (error 0.119). At w = 0: error 23.0, gradient -20.667. Learning rate 0.1 reaches 2.214 in 10 steps; 0.02 reaches 1.934; 0.25 diverges (w = -37.1 after 10 steps).
- Example 2: one forward pass, backward pass, and update on the 2-2-1 network for input (1, 0). Output 0.614, error 0.0746, blame -0.0916 at the output, -0.0147 and +0.0108 at the hidden units. Finite-difference gap 1.5e-11. Output after the update: 0.631.
- Example 3: full-batch training on XOR, learning rate 2.0, start uniform in [-1, 1], seed 1. Errors 0.5195, 0.5000, 0.0112, 0.0022, 0.0003 at 0, 100, 500, 1000, 5000 sweeps. Error below 0.45 at sweep 296; solved at sweep 312. From 100 random starts, 78 solve XOR within 5,000 sweeps.
- Example 4: equal starting weights (0.5): the hidden units stay identical, and outputs are 0.017, 0.666, 0.666, 0.667.

## Figures [D-014]

Drawn by `figures/backprop.py`, which imports the check script.

- `figures/backprop-bowl.svg`: Example 1 with three learning rates.
- `figures/backprop-network.svg`: Example 2's forward values and backward blame.
- `figures/backprop-curve.svg`: Example 3's training error.

## Terms defined in this chapter

For the glossary: backpropagation, hidden unit, hidden layer, credit assignment problem, loss function, mean squared error, gradient, gradient descent, learning rate, forward pass, backward pass, sweep (an epoch of full-batch training), local minimum, generalized delta rule, reverse mode of automatic differentiation (named), universal approximation theorem, squashing function.

## Independent check

2026-11-11. A separate agent that did not write the chapter fetched all eight sources itself and checked every claim, quote, page, number, and figure. The priority dispute was judged fairly handled.

- Confirmed: B1 to B5 as logged. All numbers match `code/checks/backprop.py` (including that XOR stays solved from sweep 312 to 5,000), and the figures regenerate byte-identically.
- Errors found and fixed: (1) the "sweep" training scheme is stated on p. 535, not only in the p. 534 caption; now pp. 534-535. (2) the summary dated the method's discovery from 1970, while the body traces it to the 1960s; now "between the 1960s and 1985".
- Warnings acted on: sweep tied to epoch; "no practical way" scoped to neural-network research; citations added for wide adoption, for the demonstrations, and for the theorem's name; "did not claim to be first" replaced by the papers' own acknowledgment of Parker and Le Cun; "sometimes heatedly" dropped; Schmidhuber characterized by his own stated goal; "apparently" restored; Werbos "considered applying", with the thesis's political-science application; Minsky's own recollection added beside Werbos's; the -0.3 to 0.3 range tied to the symmetry network, with the general rule from p. 535; PDP pages corrected to 322 and 330-331; the Hornik quote reframed and his actual caveat quoted; gradient defined as the list of derivatives; chain rule notes that paths add; "approximate" replaces "represent"; distinct x values for the polynomial; "NNs" expanded; italics instead of bold for the bridge sentence; credit assignment problem, generalized delta rule, and squashing function bolded; "billions of weights" pointed to `destination`; an unsourced "stalls are common" removed; and the forward claim that convolution and recurrence are "still inside every LLM" removed.
- Re-checked after fixing: the writer located the new quotes in the same fetched texts (Nature p. 535 OCR; Olazaran pp. 393-394; Schmidhuber p. 1; Goodfellow et al. p. 194).
- Not verifiable by design: Werbos 1974, Linnainmaa 1970/1976, Parker 1985, LeCun 1985 and 1988, known through the secondary sources named in B4.

## Scope notes for drafting

- Bridge: the delta rule for a linear unit is least-squares regression fitted by gradient descent (`rumelhart1986internal`, p. 324: "the error surface is shaped like a bowl with only one minimum"). The reader knows least squares.
- Learning rate, epoch, loss function, forward pass, gradient: define in this chapter. Stochastic gradient descent and minibatches belong to `toolkit`.
- Hidden units must use a smooth activation (sigmoid) for the derivatives to exist. This links back to `neuron`.

## Consistency pass (2026-11-11)

Editorial pass to make the chapters agree with each other; no sourced fact, quote, number, or citation changed except where noted.

- No change needed. Its bold terms are first uses; `toolkit` drops its re-bold of "reverse mode". The false "multilayer perceptron of the backpropagation chapter" reference is in `anatomy` (this chapter never uses the phrase) and is fixed there.

## Style pass (2026-11-11)

Reader call-outs made generic per D-023.

- "two things the reader already knows" -> "two older ideas"
- "The reader has met the most common loss already" -> "The most common loss is an old one"
- "the bridge from the reader's own toolkit" -> "the bridge to classical statistics"
- "by the reader's own era" -> "by around 2000"

## Story pass (2026-11-22)

Rewritten per D-025 (concepts first, few names, few quotations) and D-026 (credit questions to the `credit` appendix). No claim was added; every citation key and page of the earlier text is still cited, in the chapter or in the appendix entry (checked by script against the committed version). Quotation marks (the `"` character) fell from 94 to 12, and the 12 left are a title, short terms, and an HTML comment; the chapter fell from 4,369 to 3,918 words.

- Moved to `credit` (section "Learning in layers", drafted in the scratch file for the author to paste): the bulleted priority list of "Who invented backpropagation?" (control theory with Kelley and Bryson; Griewank's account of Linnainmaa's Copenhagen afternoon and of Ostrowski five years earlier, p. 389; Schmidhuber's "apparently was first described" and "preliminary, NN-specific discussion", p. 11, and his stated goal of assigning credit, p. 1; Goodfellow et al. on Werbos 1981, "finally developed in practice" and "contributed greatly", p. 221; the PDP chapter's Parker and Le Cun sentences, p. 322); the "None of these accounts disputes the chronology" paragraph; LeCun's 1988 "little more than an extremely judicious application" (via Olazaran p. 392); Werbos's and Minsky's interview recollections (Olazaran pp. 392-393, 393-394). The appendix also quotes the Nature abstract's "a new learning procedure" (p. 533, B2), which the chapter no longer quotes.
- Kept in the chapter, as story: a short neutral account under a renamed heading, "Found more than once" (was "Who invented backpropagation?", itself a credit question): optimal control in the 1960s, the 1970 thesis (without "first"), the 1974 and 1981 work, the two 1985 findings noted by the 1986 papers, and the definition of the reverse mode of automatic differentiation (glossary entry points here). It ends with one sentence linking to `#credit-backprop`. The intro's "The history of who found it first is tangled" became "It was found several times before it came into wide use".
- Names dropped from the prose, the citation now carrying them: Schmidhuber (credit assignment p. 4; cost p. 11); Cybenko, and Hornik, Stinchcombe, and White (now "the first" and "the second" of "two papers in 1989"); Linnainmaa, Werbos, Parker, Griewank, Ostrowski, Kelley, Bryson, Olazaran (all to the appendix; none is named in a later chapter's prose, only in `timeline` and `further-reading`, which keep names). Institutions dropped: University of California, San Diego and Carnegie-Mellon (p. 533 still cited for the authorship). Kept: Rosenblatt, Minsky (for the 1963 phrase; recurs from `neuron`), Rumelhart, Hinton, and Williams (`embeddings` refers back to them by name), LeCun (recurs in `structure`).
- Quotations turned into close paraphrase, same source and page: rumelhart1986learning p. 533 (hidden units "more interesting but more difficult"; perceptron units "not true hidden units"; hidden units "come to represent important features of the task domain"; the abstract's description of the procedure), p. 534 ("1,425 sweeps"; weights "uniformly distributed between -0.3 and 0.3"), p. 535 ("To break symmetry"), p. 536 (not a plausible model of brains); rumelhart1986internal p. 324 (the bowl; "not concave upwards"; "apparently fatal ... irrelevant", now with "main empirical contribution" restored from the same sentence), p. 330 (equal weights "can never learn"), p. 331 (XOR "hundreds of times", two local minima), p. 322 ("the generalized delta rule", now a bold term without quotes); schmidhuber2014deep p. 4 ("fundamental credit assignment problem") and p. 11 (costs "essentially" equal, hedge kept); cybenko1989approximation p. 303 (decision regions) and p. 313 ("focused only on existence", feasibility); hornik1989multilayer p. 359 (the theorem; "stochastic" now "random rather than deterministic") and p. 360 (failures "can be attributed to", now "can be put down to"; the number of units); goodfellow2016deep p. 195 (one layer sufficient but may be infeasibly large; "a single layer" written as "one hidden layer", which is the textbook's meaning in context, and moved from "The modern textbook summary is blunt" into the narrator's voice with the same citation).
- Quotations kept, because the wording itself is the point: the title "Learning representations by back-propagating errors"; the short terms "sweep", "momentum", "replace with", "Borel measurable".
- Dropped as unneeded: nothing beyond the names and institutions above. Every bold term (including credit assignment problem, generalized delta rule, reverse mode of automatic differentiation, squashing function, universal approximation theorem) keeps its definition in the chapter.
- Not done here, for the author: `book1/chapters/timeline.md` says its 1970-1986 entries list each finding "as [Learning in layers](#backprop) presents it"; the names now live in the appendix, so that sentence may want to point at `#credit-backprop` too.

## Independent check (story pass, 2026-11-22)

A separate agent compared every changed, cited sentence of the chapter and of the `credit` entry (scratch draft `credit-backprop.md`) with the old text (`git show HEAD`) and the quotes in B1 to B5. Every claim touched by the rewrite has its quote in this ledger, so the check was made against the ledger only; no source was re-fetched. A script confirmed that every (key, page) cited in the old chapter, page ranges expanded, is still cited in the chapter or the appendix, and none was added; only schmidhuber2014deep p. 1 and olazaran1993sociological p. 393 now live in the appendix alone. Bold terms, glossary entries pointing here, figures, worked examples and their D-009 comments, and cross-chapter links are all kept; the only link added is `#credit-backprop`. No dropped name is referred back to by a later chapter's prose (`timeline` and `further-reading` keep names).

- Errors fixed in the chapter:
  1. The Goodfellow et al. summary (p. 195) had moved into the narrator's voice as "In short, ...". Its "enough to represent any function" is looser than the two theorems ("approximate"), which the chapter otherwise keeps careful, so the attribution is restored without the name: "A 2016 textbook sums it up: ...".
  2. Hornik et al.'s "stochastic rather than a deterministic relation" (p. 360) had become "random rather than deterministic", which reads as no relation at all. Now "partly random rather than deterministic".
  3. "They counted it as their main empirical contribution to show that ..." was awkward; now "Their chapter's main empirical contribution, they wrote, was to show that ..." (p. 324, same sentence of the source).
- Errors fixed in the `credit` draft:
  1. Griewank says Ostrowski "discovered and used it" (p. 389); the draft (and the old chapter) said only "had used the idea", which weakens one claimant. Now "had discovered and used it some five years earlier, in process models in chemical engineering".
  2. Schmidhuber's "To my knowledge" (p. 11), the hedge on his dating of the first neural-network application to Werbos 1981, had been dropped (also in the old chapter). Restored as a parenthesis: ("to my knowledge", it adds).
  3. Balance: Goodfellow et al.'s view of the 1985 work ("independently rediscovered") was given, but not Schmidhuber's, which differs in emphasis. Added, from the B4 quote on the same page: he calls Parker's and LeCun's 1985 work "related work" published "several years later" (p. 11).
- Confirmed: the appendix presents every claimant named in the sources (control theory with Kelley and Bryson, Ostrowski, Linnainmaa, Werbos, Parker, LeCun, Rumelhart, Hinton, and Williams), each with citations, and picks no winner. The chapter's "Found more than once" sequence uses no "first" and ends with one neutral sentence and the appendix link.
- Left as is, for the author:
  - The heading "1986: the paper that made it work" (unchanged by this pass) is mildly a credit judgment and speaks of one paper where the section describes two; "1986: the papers that made it widely used" would match the sources (Goodfellow et al. "finally developed in practice"; Schmidhuber "significantly contributed to the popularisation").
  - Several paraphrases are near verbatim without quotation marks (the bowl, p. 324; "apparently fatal problem ... irrelevant", p. 324; "1,425 sweeps through the set of 64 possible input vectors", p. 534; the Hornik abstract, p. 359; the Goodfellow summary, p. 195). Each is attributed and cited; whether to loosen the wording or restore quotation marks is a style choice.
  - The appendix says the later histories "agree on the sequence" and, a paragraph later, that none "disputes the chronology"; one of the two could go. Griewank alone mentions Ostrowski, which is an addition rather than a disagreement.
  - Olazaran's own hedged view (p. 392, "it seems that the first attempt to apply something similar to back-propagation to neural network research was Paul Werbos'") is in B4 but not in the appendix; it could be added beside the other accounts.
  - The `timeline` pointer noted at the end of the Story pass entry.
- The Story pass entry above is accurate. Its quotation-mark count (94 to 12) and word counts (4,369 to 3,918) were re-counted and match the text before this check.
- Follow-up (2026-11-22, at the coordinator's request): four of the items above were done. The near-verbatim paraphrases were reworded against the B1 to B5 quotes (pp. 533, 534, 536 of the Nature letter; pp. 324, 330, 331 of the PDP chapter; Cybenko pp. 303, 313; Hornik pp. 359, 360; Goodfellow et al. p. 195). The heading is now "1986: backpropagation at work" (nothing linked to its old anchor). The duplicate "agree on the sequence" is gone from the appendix, which now quotes Olazaran's hedged view of Werbos (p. 392). The `timeline` item stays for the author.
