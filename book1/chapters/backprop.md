# Learning in layers (1970-1989) {#backprop}

<!-- D-002: intuition only; the one formula (the update rule) follows its worked example. D-003: no code. D-008: second chapter of the "how networks learn" thread. D-009: numbers from code/checks/backprop.py. D-014: figures from figures/backprop.py. D-025: concepts first, few names, few quotations. D-026: credit questions in the credit appendix. -->

[The previous chapter](#neuron) ended with a network that could compute XOR: two neurons in a middle layer feeding a third. The weights in that network were set by hand. The perceptron rule could not have found them, because it needs to know the correct output of every neuron it adjusts, and nobody tells the middle neurons what their correct output is. In 1969 no one in neural-network research had a practical way to train such a network.

This chapter is about the way that was found, called **backpropagation**. It is how the networks in the rest of this book are trained, LLMs included. The idea turns out to be a careful use of two older ideas: fitting a model by minimizing a squared error, and the chain rule of calculus. It was found several times before it came into wide use, and the chapter ends with what a network trained this way can and cannot be expected to do.

## Who is to blame?

A neuron that is not an input and not an output is a **hidden unit**, and a set of hidden units side by side is a **hidden layer**. In 1986 the paper that made backpropagation famous stated the difficulty plainly: hidden units make learning more interesting but also harder, because the task specifies neither their actual nor their desired states [@rumelhart1986learning, p. 533]. At the output, you can compare what the network said with what it should have said. At a hidden unit, there is nothing to compare with.

Rosenblatt's perceptron had units between its input and its output, but their incoming connections were fixed by hand. By the same paper's account, that made them not true hidden units: with their inputs fixed, what they computed followed entirely from the input, and they learned no representations of their own [@rumelhart1986learning, p. 533].

The general question, which part of a system deserves credit or blame for its success or failure, has a name: the fundamental **credit assignment problem**, a phrase traced to Minsky in 1963 [@schmidhuber2014deep, p. 4]. For a layered network the problem is concrete: when the output is wrong, how much should each weight deep inside the network change, and in which direction?

The answer comes in three steps. First, measure the error with a single number. Second, reduce that number by walking downhill. Third, work out which way is downhill for every weight at once.

## Step one: a number for how wrong

A **loss function** is a single number that measures how wrong a model's outputs are on the training data. Learning becomes the task of making that number small. The most common loss is an old one: the squared error of least-squares regression. The 1986 paper used exactly this, a total error that adds up the squared differences between the actual and desired outputs over every training case and every output unit [@rumelhart1986learning, p. 534].

Here is the smallest possible example. Fit the line $y = w x$, with one adjustable weight $w$ and no intercept, to three points: (1, 2), (2, 4), and (3, 7). The loss is the **mean squared error**: for each point, take the difference between the prediction $w x$ and the true $y$, square it, and average the three squares.

<!-- D-009: code/checks/backprop.py, Example 1 -->

At $w = 0$ every prediction is 0 and the mean squared error is 23.0. The least-squares answer, which a statistics package would compute in one step, is $w = 2.214$, where the error is 0.119. Plotted against $w$, the error is a bowl with its lowest point at 2.214.

## Step two: walking downhill

A statistics package solves least squares exactly. A neural network has no such formula, so it uses a method that only needs local information: at the current weight, which way is downhill, and how steep is it?

The steepness of the loss with respect to a weight is the derivative of the loss with respect to that weight. With many weights, the list of all these derivatives, one per weight, is the **gradient**. In the example there is only one weight, and at $w = 0$ the gradient is -20.667. The negative sign says that increasing $w$ decreases the error. **Gradient descent** takes a step in the downhill direction, of a size proportional to the gradient, and repeats. The size of the steps is set by a number called the **learning rate**.

![Gradient descent on the bowl-shaped error of the line-fitting example, starting from w = 0, with three learning rates. With 0.02 the steps are too short and progress is slow. With 0.1 the second step is already close to the bottom. With 0.25 each step overshoots the bottom by more than the last, and the error grows.](../../figures/backprop-bowl.svg){#fig:backprop-bowl}

With a learning rate of 0.1, the first step takes $w$ from 0 to 2.07, and after ten steps it has reached 2.214, the least-squares answer. With 0.02, ten steps reach only 1.934. With 0.25, the steps overshoot: $w$ goes to 5.17, then -1.72, then 7.46, and after ten steps it is at -37.1, with an error over 7,000. Choosing the learning rate is the first practical skill of training a network, and it has not gone away.

Written in its standard form, one step of gradient descent is

$$w \leftarrow w - \eta \, \frac{\partial L}{\partial w}$$

where $w$ is a weight, $L$ is the loss, $\frac{\partial L}{\partial w}$ is the derivative of the loss with respect to that weight (its entry in the gradient), $\eta$ (the Greek letter eta) is the learning rate, and the arrow means "replace with". In a network with many weights, every weight takes its own step at once, each using its own entry in the gradient.

This is the bridge to classical statistics: *training a network by gradient descent on a loss is the same idea as fitting a regression, with many more knobs and no closed-form answer.* For a single layer of linear units it is literally the same problem. The 1986 PDP chapter put it in terms of the error surface: without hidden units the error surface is a bowl with a single lowest point, so gradient descent is sure to reach the best weights [@rumelhart1986internal, p. 324]. The ADALINE of [the previous chapter](#neuron), minimizing a mean squared error, was doing this in 1960.

## Step three: passing the blame backward

Gradient descent needs the gradient for every weight, including the weights into hidden units. Two obstacles stand in the way.

The first is the step function. Its output jumps from 0 to 1 and is flat everywhere else, so a small change in a weight usually changes nothing, and the gradient is zero almost everywhere. The fix is the sigmoid from [the previous chapter](#neuron): it is smooth, so every small change in a weight makes a small change in the output, and the derivative exists everywhere. The sigmoid's slope has a convenient form: at any point it equals the sigmoid's output times one minus that output.

The second obstacle is the real one: a hidden weight affects the error only indirectly, through everything downstream of it. The chain rule of calculus handles exactly this. If a weight affects a hidden unit, which affects the output, which affects the error, then the effect of the weight on the error is the product of the effects along that chain. (If a weight affects the error along several paths, the effects of the separate paths add up.)

Backpropagation organizes the chain rule so that nothing is computed twice. It runs in two passes.

- The **forward pass** runs the network on an input, from the inputs to the output, and records every unit's value along the way.
- The **backward pass** starts at the output. It computes how much the error would change if the output unit's weighted sum changed: call this the output's *blame*. It then passes the blame back to each hidden unit, in proportion to the weight connecting them and scaled by the hidden unit's own slope. Each weight's gradient is then the blame at the unit it feeds times the value flowing into it.

Here is one complete step, on a network of two inputs, two hidden units, and one output, all with sigmoid activations. The starting weights are small values chosen for illustration. The input is (1, 0), and the correct XOR output is 1.

![One step of backpropagation on a 2-2-1 network for the input (1, 0). Values flow forward: the hidden units output 0.646 and 0.378, and the output is 0.614 where 1 was wanted. Blame flows backward: -0.0916 at the output, then -0.0147 at the upper hidden unit (through the weight +0.7) and +0.0108 at the lower one (through the weight -0.5). The hidden biases are +0.1 and -0.2, and the output bias is +0.2.](../../figures/backprop-network.svg){#fig:backprop-network}

<!-- D-009: code/checks/backprop.py, Example 2 -->

**Forward.** The upper hidden unit's weighted sum is 0.5 times 1, plus -0.4 times 0, plus its bias 0.1, which is +0.600; the sigmoid turns that into 0.646. The lower hidden unit's sum is -0.500, giving 0.378. The output unit combines them with weights +0.7 and -0.5 and its bias +0.2, for a sum of +0.463 and an output of 0.614. The error for this case, half the squared difference from the wanted 1, is 0.0746. (The half is a convention of the 1986 papers that makes the slopes tidier.)

**Backward.** The output's blame is -0.0916. The sign says the output's sum should go up. The upper hidden unit receives blame -0.0147: it feeds the output through a positive weight, so it too should go up. The lower hidden unit receives +0.0108: it feeds the output through a negative weight, so for the output to rise, this unit should go down. Neither hidden unit was ever told what its correct value was. The blame told it which way to move.

**Update.** With a learning rate of 0.5, each weight moves against its gradient.

| Weight | Before | Gradient | After |
|:---|---:|---:|---:|
| Upper hidden to output | +0.700 | -0.0591 | +0.7296 |
| Lower hidden to output | -0.500 | -0.0346 | -0.4827 |
| Output bias | +0.200 | -0.0916 | +0.2458 |
| Input 1 to upper hidden | +0.500 | -0.0147 | +0.5073 |
| Upper hidden bias | +0.100 | -0.0147 | +0.1073 |
| Input 1 to lower hidden | -0.300 | +0.0108 | -0.3054 |
| Lower hidden bias | -0.200 | +0.0108 | -0.2054 |

Table: One update with learning rate 0.5. The weights from input 2 do not change, because input 2 was 0 in this example and so contributed nothing to the error. After the update, the output for (1, 0) rises from 0.614 to 0.631.

The gradients can be checked by brute force: nudge each weight by a tiny amount, rerun the network, and measure how the error changes. For this example the two methods agree to about ten decimal places. The difference is cost. Nudging needs a separate forward pass for every weight, and a large language model has billions of weights (see [the destination chapter](#destination)). Backpropagation gets all the gradients from one forward pass and one backward pass. Computing the derivatives backward costs essentially the same as running the network forward [@schmidhuber2014deep, p. 11]. That efficiency is what makes training large networks possible at all.

## Training a network to compute XOR

One update is not learning. Learning is many updates. Here the network sees all four XOR cases, adds up their gradients, and takes one step: a "sweep" through the data (one epoch, in the terms of [the previous chapter](#neuron)), which is how the 1986 Nature letter trained its examples [@rumelhart1986learning, pp. 534-535]. The weights start at random values between -1 and 1, and the learning rate is 2.0.

<!-- D-009: code/checks/backprop.py, Example 3 -->

![Total error while the 2-2-1 network learns XOR from a random start. For nearly 300 sweeps the error sits near 0.5 and barely moves; then it falls quickly. It first drops below 0.45 at sweep 296, and every output is on the correct side of one half from sweep 312.](../../figures/backprop-curve.svg){#fig:backprop-curve}

| Sweeps | Total error |
|---:|---:|
| 0 | 0.5195 |
| 100 | 0.5000 |
| 500 | 0.0112 |
| 1,000 | 0.0022 |
| 5,000 | 0.0003 |

Table: Training error over time for one random start. After 5,000 sweeps the outputs for (0, 0), (0, 1), (1, 0), and (1, 1) are 0.012, 0.989, 0.987, and 0.010.

The network has found its own way to compute XOR. Nobody chose its hidden features; they emerged from the blame passed back to them. That is what the 1986 paper claimed as the method's central achievement: the hidden units, which belong to neither the input nor the output, come to represent features that matter in the task [@rumelhart1986learning, p. 533].

Two features of the run deserve attention. The first is the long flat stretch at the start, where the error sits near 0.5 and the network seems to learn nothing for nearly 300 sweeps; then it drops sharply, and the network has solved XOR by sweep 312. A reader of loss curves learns not to judge a run by its first few hundred steps. The second is that this was one random start out of many possible ones. Repeating the experiment from 100 different random starts, 78 solved XOR within 5,000 sweeps and 22 had not.

## Valleys, plateaus, and a broken symmetry

A bowl has one lowest point. The error surface of a network with hidden units does not have to be a bowl. The 1986 PDP chapter said so directly: with hidden units the error surface no longer curves upward everywhere, so gradient descent risks getting stuck in local minima [@rumelhart1986internal, p. 324]. A **local minimum** is a point lower than everything near it but not the lowest point overall; gradient descent, which only ever looks at the slope where it stands, cannot tell the difference.

The authors' answer was empirical. Their chapter's main empirical contribution, they wrote, was to show that local minima, a seemingly fatal problem, did not matter in a wide variety of learning tasks [@rumelhart1986internal, p. 324]. Of the hundreds of times they had trained networks on XOR, only two runs had stuck in a local minimum and failed [@rumelhart1986internal, p. 331]. The 22 failures in the experiment above are far more than that. The settings differ (the 1986 work used additional techniques, such as a "momentum" term that smooths the steps [@rumelhart1986internal, p. 330], which returns in [the chapter on the training loop](#toolkit)), and a run that has not solved XOR after 5,000 sweeps may be stuck on a plateau rather than in a true local minimum. The lesson is not that the 1986 claim was wrong. It is that whether training succeeds depends on choices beyond the method itself: the learning rate, the starting weights, and the number of sweeps.

Starting weights matter in a second, stranger way. Start every weight at the same value, 0.5, and train as before.

<!-- D-009: code/checks/backprop.py, Example 4 -->

After 5,000 sweeps the two hidden units are still exact copies of each other, and the network outputs 0.017, 0.666, 0.666, and 0.667 for the four cases: it has not solved XOR, and it never will. Two identical hidden units receive identical blame, so they make identical changes, and they stay identical forever. The network is effectively stuck with one hidden unit, and one hidden unit is not enough. The PDP chapter named the problem: a network whose weights all start equal can never reach a solution that needs them to differ [@rumelhart1986internal, p. 330]. The fix is to start from small random weights, the rule the 1986 letter gave for breaking the symmetry [@rumelhart1986learning, p. 535]; for its symmetry-detecting network, the starting weights were drawn at random, uniformly between -0.3 and 0.3 [@rumelhart1986learning, p. 534]. Every network in this book starts the same way, with random numbers, which is why [the destination chapter](#destination) said an embedding table starts out random.

## 1986: backpropagation at work

Backpropagation became widely used after two publications in 1986 [@goodfellow2016deep, p. 221] by David Rumelhart, Geoffrey Hinton, and Ronald Williams [@rumelhart1986learning, p. 533]. One was a four-page letter in *Nature*, "Learning representations by back-propagating errors". Its abstract describes back-propagation as a procedure that trains networks of neuron-like units by adjusting their connection weights, over and over, to shrink the difference between the output the network gives and the output it should give [@rumelhart1986learning, p. 533]. The other was a long chapter in the *Parallel Distributed Processing* volumes, which called the method the **generalized delta rule** and worked through many examples, XOR among them [@rumelhart1986internal, pp. 322, 330-331].

What made the work persuasive was less the mathematics than the demonstrations [@schmidhuber2014deep, p. 11; @goodfellow2016deep, p. 221]. The networks learned problems that single-layer networks could not, and their hidden units could be inspected and found to represent sensible features. One network in the Nature letter learned to detect mirror symmetry in a row of six inputs, which took 1,425 sweeps through all 64 possible inputs [@rumelhart1986learning, p. 534]. The authors were also explicit about what they were not claiming: they wrote that the procedure, as it stood, was not a plausible account of how brains learn [@rumelhart1986learning, p. 536].

## Found more than once

The method was older than these papers, and it had been found several times, in different fields. In optimal control, gradient methods for multi-stage systems, computed by applying the chain rule backward stage by stage, had been discussed since at least the early 1960s [@schmidhuber2014deep, p. 11; @goodfellow2016deep, p. 221]. In 1970, a master's thesis described efficient backpropagation for arbitrary networks of calculations, without reference to neural networks; its author used it to estimate the effect of rounding errors in computations, not to train networks [@schmidhuber2014deep, p. 11; @griewank2012invented, p. 389]. That general method, computing the derivatives of any sequence of calculations by running backward through it, is now called the **reverse mode of automatic differentiation** [@schmidhuber2014deep, p. 11], and under that name it returns in [the chapter on the training loop](#toolkit). A 1974 doctoral thesis included a preliminary discussion of the method for neural networks, though the thesis applied it to an example from political science [@schmidhuber2014deep, p. 11; @olazaran1993sociological, pp. 392, 394], and in 1981 its author proposed it for training neural networks [@schmidhuber2014deep, p. 11; @goodfellow2016deep, p. 221]. In 1985 two more researchers, LeCun among them, found similar procedures independently, as the 1986 papers themselves noted [@rumelhart1986internal, p. 322; @rumelhart1986learning, p. 535].

Who should count as its inventor depends on what is counted, and [the credit appendix](#credit-backprop) sets out the accounts.

## What a layered network can represent

Backpropagation answered how to train a layered network. A second question remained: how much can such a network represent at all? Two papers in 1989 answered it.

The first showed that a network with just one hidden layer, using any continuous sigmoid-shaped activation, can approximate any decision region as closely as desired [@cybenko1989approximation, p. 303]. The second proved a similar result in more general form: a network with one hidden layer of units using any squashing function can approximate any Borel measurable function, from numbers in any fixed number of dimensions to numbers in another, as accurately as desired, given enough hidden units [@hornik1989multilayer, p. 359]. (A **squashing function** is one like the sigmoid, which squeezes any number into a fixed range. "Borel measurable" covers, for practical purposes, any function one would meet.) This result is known as the **universal approximation theorem** [@goodfellow2016deep, p. 194].

It is easy to read too much into it, and both papers warned against doing so. The first said it had shown only that such networks exist; still open was whether they were feasible, that is, how many hidden units a given quality of approximation needs [@cybenko1989approximation, p. 313]. The second said that, given its result, failures in applications can be put down to inadequate learning, too few hidden units, or a relation between input and target that is partly random rather than deterministic, and that its results were silent on how many units a given accuracy requires [@hornik1989multilayer, p. 360]. A 2016 textbook sums it up: a single hidden layer can represent any function, but it may have to be impractically large, and training may fail to find its weights or to generalize [@goodfellow2016deep, p. 195].

A statistician has seen this pattern before. A polynomial of high enough degree can pass through any set of points with distinct x values, and that fact says nothing about whether the fitted polynomial is any good. The universal approximation theorem says that suitable weights exist. It does not say that gradient descent will find them, how many hidden units are needed, or that the result will do well on data it was not trained on. Those three questions, learnability, size, and generalization, are the practical questions of the rest of this book.

## Where this leaves us

By 1989 the field had what it lacked in 1969: a way to train networks with hidden layers, and a theorem saying such networks can approximate essentially any function. It also had a list of practical troubles. Training could stall on plateaus or settle in poor solutions. It depended on the learning rate and the starting weights. And the theorem promised nothing about how big a network had to be.

[The next chapter](#structure) follows what happened when researchers applied these networks to real data, images and sequences, and found that plain layered networks were not enough. Two structural ideas came out of that period, both about using the same weights in many places. A new obstacle also appeared, and it was severe enough that, by around 2000, much of machine learning had moved on to other methods.

## What to carry forward

- A hidden unit has no target value of its own. Backpropagation solves the credit assignment problem by computing, for every weight, how the error would change if that weight changed.
- Training means minimizing a loss function, such as the squared error, by gradient descent: repeated small steps downhill, with the step size set by the learning rate. For a single linear layer this is least-squares regression fitted iteratively.
- Backpropagation is the chain rule organized into a forward pass and a backward pass. It gets every gradient for about the cost of running the network twice.
- Training can stall or fail. Starting weights must be random to break the symmetry between hidden units, and the learning rate must be neither too small nor too large.
- The method was found several times between the 1960s and 1985, in different fields. Rumelhart, Hinton, and Williams's 1986 papers made it widely used by showing that hidden units learn useful features.
- The universal approximation theorem (1989) says one hidden layer can approximate any reasonable function, given enough units. It says nothing about how many units, whether training will find the weights, or whether the result will generalize.
