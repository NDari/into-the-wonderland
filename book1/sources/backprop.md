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
