# The artificial neuron (1943-1969) {#neuron}

<!-- D-002: intuition only; formulas (weighted sum, sigmoid) follow worked examples. D-003: no code. D-008: first chapter of the "how networks learn" thread. D-009: numbers from code/checks/neuron.py. D-014: figures from figures/neuron.py. D-025: concepts first, few names, few quotations. D-026: credit questions in the credit appendix. -->

The picture in [the destination chapter](#destination) had a box labeled "Layers", where most of an LLM's computation happens. Open that box far enough and you find a very large number of small, identical computing units, each doing something simple. This chapter is about that unit: what it computes, how a single one can learn, and why the first wave of work on it ran into a wall in 1969.

The story runs from 1943 to 1969, and almost all of it concerns a single unit, or a single layer of them. That restriction is the point of the chapter. A single unit can do surprisingly much, and its limits are exact and easy to see. Those limits shaped the field for the next two decades.

## A neuron as a weighted vote

An **artificial neuron** takes several numbers as input and produces one number as output. It works like a weighted vote.

Each input has a weight, a number saying how much that input counts and in which direction. A positive weight means "this input argues for firing"; a negative weight means "this input argues against". The neuron multiplies each input by its weight and adds up the results. It then adds one more number, the **bias**, which sets how easily the neuron fires regardless of its inputs. The total is the **weighted sum**. Finally the neuron passes the weighted sum through an **activation function**, which decides the output. The oldest choice is the **step function**: output 1 if the weighted sum is above zero, and 0 otherwise. Put the other way round, the neuron fires when its weighted inputs, before the bias is added, come to more than minus the bias. That amount is the neuron's **threshold**: a bias of -0.1 means a threshold of 0.1.

Here is one neuron with three inputs.

![One artificial neuron as a weighted vote. Each input is multiplied by its weight, the results are summed with the bias, and the neuron outputs 1 because the total is above zero. The numbers match the table below.](../../figures/neuron-vote.svg){#fig:neuron-vote}

<!-- D-009: code/checks/neuron.py, Example 1 -->

| Input | Value | Weight | Contribution |
|:---|---:|---:|---:|
| 1 | 1 | +0.6 | +0.6 |
| 2 | 0 | +0.9 | 0.0 |
| 3 | 1 | -0.4 | -0.4 |
| Bias | | | -0.1 |
| **Weighted sum** | | | **+0.1** |

Table: A weighted vote. Input 2 has the largest weight but is off, so it contributes nothing. The sum is just above zero, so the neuron outputs 1.

Written in its standard form, the weighted sum of a neuron with $n$ inputs is

$$z = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b$$

where $x_1$ to $x_n$ are the inputs, $w_1$ to $w_n$ are their weights, $b$ is the bias, and $z$ is the weighted sum. The output is the activation function applied to $z$.

The weights and the bias are the neuron's parameters, in exactly the sense of [the destination chapter](#destination): the numbers that learning will set. Everything that follows in this book, up to models with hundreds of billions of parameters, is built from this unit or close relatives of it.

## The link to logistic regression

A weighted sum plus an intercept is also the core of a standard statistical model. Replace the step function with the **sigmoid** (the logistic function), which turns any number into a value between 0 and 1:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Here $z$ is the weighted sum, $e$ is the base of the natural logarithm (about 2.718), and $\sigma(z)$ is the output. A large positive $z$ gives an output near 1, a large negative $z$ gives an output near 0, and $z = 0$ gives exactly 0.5.

A weighted sum of the inputs, plus an intercept, passed through the sigmoid: that is the prediction function of logistic regression. **A neuron with a sigmoid activation is logistic regression.** The weights are the coefficients, and the bias is the intercept. For the weighted vote above, whose sum was +0.1, the sigmoid gives 0.525: just over one half, a hesitant yes where the step gave a flat 1. The step function is what you get if you take the sigmoid's output and cut it at one half.

The difference between the two traditions lies elsewhere: in how the weights are found. A statistician fits logistic regression by maximum likelihood. The early neuron builders set weights by hand, or with simple learning rules of their own, described below. Making the two meet, so that a whole network of neurons can be fitted the way a regression is fitted, is the subject of [the chapter on learning in layers](#backprop).

The bridge also connects to the end of [the destination chapter](#destination). The softmax that turns an LLM's scores into probabilities is the many-class version of the same idea. The final step of a language model is a very wide layer of weighted sums, one per vocabulary entry, turned into probabilities together by the softmax.

## 1943: a neuron as a piece of logic

In 1943 Warren McCulloch and Walter Pitts published a mathematical model of a neuron [@mcculloch1943logical]. Their starting point was a fact of biology: a nerve cell either fires or does not. Because nervous activity is all-or-none in this way, they argued, neural events and the relations among them can be treated with propositional logic [@mcculloch1943logical, p. 99]. In other words, if a neuron is either on or off, it can be treated as a statement that is either true or false, and a network of neurons can be analyzed as a piece of logic.

Their model neuron fires only when at least a certain fixed number of its excitatory inputs are active at once [@mcculloch1943logical, p. 101]. That fixed number is a threshold. With it, single neurons compute the basic operations of logic. Take a neuron with two inputs, each counting 1.

- If it needs both inputs on to fire, it computes **AND**.
- If it needs only one, it computes **OR**.

In the weighted-vote form of the previous section, both are a neuron with weights of 1 and a bias that sets the threshold.

<!-- D-009: code/checks/neuron.py, Example 2 -->

| Input 1 | Input 2 | AND sum | AND | OR sum | OR |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | -1.5 | 0 | -0.5 | 0 |
| 0 | 1 | -0.5 | 0 | +0.5 | 1 |
| 1 | 0 | -0.5 | 0 | +0.5 | 1 |
| 1 | 1 | +0.5 | 1 | +1.5 | 1 |

Table: AND and OR computed by one threshold neuron, with both weights equal to 1. Only the bias differs: -1.5 for AND, -0.5 for OR.

<!-- D-009: code/checks/neuron.py, Example 6 -->

The same AND neuron with a sigmoid in place of the step gives 0.182, 0.378, 0.378, and 0.622 for the four rows: the right ordering, but hesitant. Multiply both weights and the bias by 10 and the outputs become 0.000, 0.007, 0.007, and 0.993. The larger the weights, the more the sigmoid behaves like a step.

Two features of the 1943 model separate it from everything later in this chapter. First, inhibition was not a negative weight. In their model, any active inhibitory input absolutely prevented the neuron from firing at that moment: a veto, not a vote against [@mcculloch1943logical, p. 101]. Second, and more important, the model did not learn. One of its stated assumptions is that the structure of the network does not change over time [@mcculloch1943logical, p. 101]. A McCulloch-Pitts network computes whatever its designer wired it to compute.

## 1949: learning as a change in connections

Where could learning come from? In 1949 D. O. Hebb proposed an answer in terms of connections between nerve cells:

> When an axon of cell A is near enough to excite a cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A's efficiency, as one of the cells firing B, is increased. [@hebb1949organization, p. 62]

Hebb stated this as an assumption about biology, not as an algorithm. But it contains the idea every later learning rule shares: what is learned is stored in the strengths of connections, and experience changes those strengths. In the language of this book, learning means changing the weights.

Hebb's rule strengthens a connection when one cell repeatedly takes part in firing another. It does not ask whether the result was right. The rules that made machines learn tasks, a decade later, added exactly that: a comparison with the correct answer.

## 1958: the perceptron

In 1958 Frank Rosenblatt published his theory of the perceptron [@rosenblatt1958perceptron]. He presented the perceptron as a hypothetical nervous system, or machine [@rosenblatt1958perceptron, p. 387], and he placed his theory in what he called the empiricist, or "connectionist", position: the view that what a brain knows is held in its connections [@rosenblatt1958perceptron, p. 387]. The work was sponsored by the US Office of Naval Research [@rosenblatt1958perceptron, p. 386].

The perceptron had layers of units with distinct roles: a retina of sensory units, association cells that receive impulses from it, and response units that give the answer [@rosenblatt1958perceptron, pp. 389-390]. Rosenblatt reported that systems of this kind had been simulated in detail, in a series of experiments on an IBM 704 computer [@rosenblatt1958perceptron, p. 403]. A hardware version, the Mark I perceptron, was then built with Navy funding: a feedforward network built as a machine, in which only one layer of connections could be adjusted [@olazaran1993sociological, p. 339]. ("Feedforward" means that signals flow in one direction only, from input to output, with no loops.) In the Mark I, the only adjustable connections were those into the response units; later analysis studied that adjustable part on its own, with the fixed connections in front of it removed [@olazaran1993sociological, pp. 339-340].

One layer of adjustable connections is the version that survives in textbooks. A 2016 deep learning textbook describes the perceptron as the model that enabled the training of a single neuron [@goodfellow2016deep, p. 13], and groups it with ADALINE (below) as a linear model [@goodfellow2016deep, p. 14]. The rest of this chapter uses **perceptron** in that sense: a single threshold neuron whose weights are learned from examples.

The perceptron drew attention far beyond research. A New York Times report of 8 July 1958 said: "The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence" [@nyt1958navy; quoted in @olazaran1993sociological, p. 341]. A second Times article, five days later, described the actual demonstration on an IBM 704: shown 100 squares placed at random on the left or the right of a field, the machine correctly indicated, 97 times in 100 trials, which side the square was on [@nyt1958brain; quoted in @olazaran1993sociological, pp. 341-342].

The gap between those two passages is the story of this chapter in miniature. What the machine did was real and new: it learned a task from examples. What was predicted for it was a different thing entirely. As a history of the episode points out, in the left-right experiment the perceptron was telling right from left, but it was not recognizing the squares as the same object [@olazaran1993sociological, p. 342].

## How a perceptron learns

A perceptron learns from labeled examples, the same kind of training data used in ordinary classification. Start with all weights and the bias at zero. Show the perceptron one example and compare its output with the correct answer. Then:

- If the output is right, change nothing.
- If the output is 0 but should be 1, add each input to its weight and add 1 to the bias. Every input that was on now counts more in favor of firing.
- If the output is 1 but should be 0, subtract each input from its weight and subtract 1 from the bias.

Go through the examples in turn, and repeat. One pass through all the training examples is called an **epoch**. This is the **perceptron learning rule**, in its simplest form. It is an error-correction rule: it acts only on mistakes, and it moves the weights in the direction that would have reduced the mistake.

Here is the rule learning AND from scratch, with the four examples shown in the same order in every epoch. Only the steps where the perceptron made a mistake are listed, since the others change nothing.

<!-- D-009: code/checks/neuron.py, Example 3 -->

| Epoch | Example | Output | Correct | Change | Weight 1 | Weight 2 | Bias |
|---:|:---|---:|---:|:---|---:|---:|---:|
| 1 | (1, 1) | 0 | 1 | add | 1 | 1 | +1 |
| 2 | (0, 0) | 1 | 0 | subtract | 1 | 1 | 0 |
| 2 | (0, 1) | 1 | 0 | subtract | 1 | 0 | -1 |
| 2 | (1, 1) | 0 | 1 | add | 2 | 1 | 0 |
| 3 | (0, 1) | 1 | 0 | subtract | 2 | 0 | -1 |
| 3 | (1, 0) | 1 | 0 | subtract | 1 | 0 | -2 |
| 3 | (1, 1) | 0 | 1 | add | 2 | 1 | -1 |
| 4 | (1, 0) | 1 | 0 | subtract | 1 | 1 | -2 |
| 4 | (1, 1) | 0 | 1 | add | 2 | 2 | -1 |
| 5 | (0, 1) | 1 | 0 | subtract | 2 | 1 | -2 |

Table: The perceptron learning rule on AND, starting from zero, where a weighted sum of exactly zero counts as "not above zero". Mistakes per epoch: 1, 3, 3, 2, 1, and then none in epoch 6.

The weights wander. A correction for one example undoes part of the correction for another, and from the first epoch to the second the number of mistakes even goes up. But in the sixth epoch the perceptron gets all four examples right, and the rule stops changing anything. The final weights, 2 and 1 with a bias of -2, are not the ones chosen by hand in the previous section, but they compute the same function. A problem usually has many solutions, and the rule finds one of them.

Was this luck? No. Rosenblatt proved that it was not, in what became known as the **perceptron convergence theorem**. It showed that any classification task a perceptron was physically capable of performing, it could be taught in a finite number of training cycles [@olazaran1993sociological, p. 340]. If a set of weights that does the job exists, the error-correction rule will find one in a finite number of steps, whatever the starting point. The condition at the start of that sentence turns out to carry all the weight.

Learning rules for single-layer networks appeared from two groups in 1960, one from Rosenblatt and one from Widrow and Hoff [@olazaran1993sociological, p. 340]. Even Rosenblatt's critics accepted the theorem. Marvin Minsky, quoted in a 1981 magazine profile, recalled that Rosenblatt's conjecture had in fact turned out to be mathematically correct, but that he had started to worry about what such a machine could not do [@olazaran1993sociological, p. 345].

## 1960: ADALINE

In 1960 Bernard Widrow and Marcian Hoff built a learning machine of their own. They called it "Adaline" (usually written **ADALINE** today), for "adaptive linear", and described it as "about the size of a lunch pail" [@widrow1960adaptive, p. 97]. Its neuron was the same weighted vote: it formed a weighted sum of the input signals, with weights that could be positive or negative, and output +1 if the sum was greater than a certain threshold and -1 otherwise [@widrow1960adaptive, p. 96]. Patterns were set on a 4-by-4 grid of switches, and the machine's total experience was stored in the values of its weights, a0 to a16: sixteen weights for the switches and one for the threshold [@widrow1960adaptive, p. 97].

Training ADALINE was a manual procedure in 1960. An operator set a pattern, read the error on a meter, and turned each of the 17 weights in the direction that diminished the error, by enough to reduce its size by 1/17, so that after all 17 adjustments the error for that pattern was zero [@widrow1960adaptive, p. 97]. Two features set this apart from the perceptron rule. The correction is spread across all the weights according to how far off the answer was, not applied as a fixed step only when the final answer is wrong. And Widrow and Hoff analyzed the procedure as a search, by the method of steepest descent, for the weights that minimize the mean square of the error [@widrow1960adaptive, pp. 98-99]: the same quantity that least-squares regression minimizes.

That second feature turned out to be the more important. The algorithm used to train ADALINE was a special case of one called stochastic gradient descent, and, according to a 2016 textbook, slightly modified versions of that algorithm were still the dominant training algorithms for deep learning models [@goodfellow2016deep, p. 14]. Stochastic gradient descent returns in [the chapter on the training loop](#toolkit).

## What a single neuron cannot do

Go back to the weighted sum of a two-input neuron, $w_1 x_1 + w_2 x_2 + b$. The neuron fires on one side of the line where that sum equals zero, and stays silent on the other. That line is the neuron's **decision boundary**. With more inputs it is a flat plane or its higher-dimensional equivalent, but the idea is the same: a single neuron splits its input space with one straight cut. A task it can solve is called **linearly separable**: the examples labeled 1 and those labeled 0 can be separated by one straight cut.

AND and OR are linearly separable. Now consider **XOR**, "exclusive or": the output is 1 when exactly one of the two inputs is 1, and 0 otherwise [@goodfellow2016deep, p. 167].

![Decision boundaries of a single neuron. For AND and OR, one straight line puts the filled points (output 1) on one side and the hollow points (output 0) on the other. For XOR, the two filled points sit on opposite corners, and no straight line separates them from the hollow ones. The AND and OR lines use the weights from the table of AND and OR above.](../../figures/neuron-xor.svg){#fig:neuron-xor}

Look at the XOR panel. The two points that should give 1 sit on opposite corners of the square, and so do the two that should give 0. Any straight line that puts both filled corners on one side puts at least one hollow corner with them. You can see why without algebra. A line that keeps (0, 0) on the silent side but puts (0, 1) and (1, 0) on the firing side has to cross between them and the origin; the far corner (1, 1) then lies even further onto the firing side. So a single neuron cannot compute XOR: it can only realize linearly separable functions, and XOR is not linearly separable [@olazaran1993sociological, p. 352].

Two computations confirm it.

<!-- D-009: code/checks/neuron.py, Examples 4 and 5 -->

First, a search. Trying every combination of two weights and a bias between -3 and 3, in steps of 0.25, gives 15,625 candidate neurons. Of these, 364 compute AND and 650 compute OR. None computes XOR.

Second, the learning rule. Run the perceptron rule on XOR exactly as it was run on AND. It makes 2 mistakes in the first epoch, 3 in the second, and then 4 in every epoch after that, through the twentieth. It never settles, because there is nothing for it to settle on. The convergence theorem is not broken: its condition, that a solution exists, does not hold.

XOR is not an exotic case. It is the smallest example of a pattern that a single straight cut cannot capture. The fix is to stack neurons: one layer computes intermediate features, and the next combines them. Take the OR neuron and the AND neuron from earlier, and feed both outputs into a third neuron with weights +1 and -1 and a bias of -0.5. It fires when OR is on and AND is off, which is exactly XOR. <!-- D-009: code/checks/neuron.py, Example 7 --> The hard question was not whether layered networks could represent such functions, but whether a learning rule could be found for them [@olazaran1993sociological, pp. 352, 358]. The error-correction rule needs to know the correct output of each neuron it adjusts, and for the neurons in the middle, later called hidden units, no training example says what that is.

## 1969: *Perceptrons*

In 1969 Marvin Minsky and Seymour Papert published *Perceptrons: An Introduction to Computational Geometry* [@minsky1969perceptrons]. A history of the perceptron controversy distinguishes two different issues in the book's arguments. One was its work on the limitations of single-layer perceptrons. The other was what Minsky and Papert called their "intuitive judgement" about whether a learning algorithm could be developed for multilayer perceptrons [@olazaran1993sociological, p. 358].

The first was mathematics. Minsky and Papert analyzed in depth what single-layer perceptrons can and cannot compute, including the **parity** problem (does the input contain an odd number of active points?) and the **connectedness** problem (is a figure in one piece?) [@olazaran1993sociological, pp. 359, 361]. XOR is parity with two inputs. Connectedness was not a new worry: in 1962 Rosenblatt had listed it, as the "figure-ground" problem, among the hardest open problems for perceptrons [@olazaran1993sociological, pp. 348-349].

The second was a judgment. About networks with more than one layer, Minsky and Papert wrote:

> There is no reason to suppose that any of these virtues carry over to the many-layered version. Nevertheless, we consider it to be an important research problem to elucidate (or reject) our intuitive judgement that the extension is sterile. [@minsky1969perceptrons, pp. 231-232; quoted in @olazaran1993sociological, p. 367]

"Sterile" was not a theorem. It was a forecast about a problem nobody had yet solved: how to train the layers of hidden units.

## What happened next

Interest in neural networks fell away in this period, the first major drop in their popularity [@goodfellow2016deep, p. 14]. How far *Perceptrons* caused that decline, and when it set in, is disputed, and [the credit appendix](#credit-neuron) sets out the two accounts. Either way, the technical problem left open was clear: networks with hidden layers could represent far more than a single neuron, and nobody had a practical way to train them.

## Where this leaves us

By 1969 the field had its basic unit and its basic limit. In the long view of a 2016 deep learning textbook, this closes the first of the field's waves, dated to the 1940s-1960s: a wave that began with theories of biological learning, those of McCulloch and Pitts and of Hebb, and with implementations of the first models, such as the perceptron, which enabled the training of a single neuron [@goodfellow2016deep, p. 13].

The next step needed two things that this chapter has set up. The first is the idea from ADALINE: treat learning as reducing a smooth measure of error, such as the mean squared error, rather than correcting right-or-wrong mistakes. The second is the sigmoid from the bridge section: a smooth activation, so that a small change in a weight makes a small change in the output, and the effect of each weight on the error can be computed. Put together across many layers, they give backpropagation, the subject of [the next chapter](#backprop).

## What to carry forward

- An artificial neuron computes a weighted sum of its inputs plus a bias, then applies an activation function. Its weights and bias are its parameters.
- With a sigmoid activation, a neuron is logistic regression. With a step, it is a linear classifier that outputs 0 or 1.
- McCulloch and Pitts (1943) modeled neurons as threshold logic, with fixed connections. Hebb (1949) proposed that learning changes connection strengths.
- The perceptron (Rosenblatt, 1958) learned from examples by error correction. The convergence theorem guarantees success whenever a solution exists. ADALINE (Widrow and Hoff, 1960) reduced a squared error instead, an early form of the method used to train modern networks.
- A single neuron draws one straight boundary, so it cannot compute XOR. Layers of neurons can, but in 1969 no one knew how to train them.
- *Perceptrons* (Minsky and Papert, 1969) proved limits of single-layer networks and judged multilayer ones "sterile". How far it caused the decline that followed is disputed.
