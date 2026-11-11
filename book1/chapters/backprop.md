# Learning in layers (1970-1989) {#backprop}

<!-- D-002: intuition only; the one formula (the update rule) follows its worked example. D-003: no code. D-008: second chapter of the "how networks learn" thread. D-009: numbers from code/checks/backprop.py. D-014: figures from figures/backprop.py. -->

[The previous chapter](#neuron) ended with a network that could compute XOR: two neurons in a middle layer feeding a third. The weights in that network were set by hand. The perceptron rule could not have found them, because it needs to know the correct output of every neuron it adjusts, and nobody tells the middle neurons what their correct output is. In 1969 no one in neural-network research had a practical way to train such a network.

This chapter is about the way that was found, called **backpropagation**. It is how the networks in the rest of this book are trained, LLMs included. The idea turns out to be a careful use of two things the reader already knows: fitting a model by minimizing a squared error, and the chain rule of calculus. The history of who found it first is tangled, and the chapter ends with what a network trained this way can and cannot be expected to do.

## Who is to blame?

A neuron that is not an input and not an output is a **hidden unit**, and a set of hidden units side by side is a **hidden layer**. The difficulty with hidden units was stated plainly by the authors of the paper that made backpropagation famous: learning "becomes more interesting but more difficult when we introduce hidden units whose actual or desired states are not specified by the task" [@rumelhart1986learning, p. 533]. At the output, you can compare what the network said with what it should have said. At a hidden unit, there is nothing to compare with.

Rosenblatt's perceptron had units between its input and its output, but their incoming connections were fixed by hand. As the same paper puts it, they "are not true hidden units because their input connections are fixed by hand, so their states are completely determined by the input vector: they do not learn representations" [@rumelhart1986learning, p. 533].

The general question, which part of a system deserves credit or blame for its success or failure, has a name. Schmidhuber's survey of the field calls it "the fundamental **credit assignment problem**", a phrase it traces to Minsky in 1963 [@schmidhuber2014deep, p. 4]. For a layered network the problem is concrete: when the output is wrong, how much should each weight deep inside the network change, and in which direction?

The answer comes in three steps. First, measure the error with a single number. Second, reduce that number by walking downhill. Third, work out which way is downhill for every weight at once.

## Step one: a number for how wrong

A **loss function** is a single number that measures how wrong a model's outputs are on the training data. Learning becomes the task of making that number small. The reader has met the most common loss already: the squared error of least-squares regression. The 1986 paper used exactly this, a total error that adds up the squared differences between the actual and desired outputs over every training case and every output unit [@rumelhart1986learning, p. 534].

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

This is the bridge from the reader's own toolkit: *training a network by gradient descent on a loss is the same idea as fitting a regression, with many more knobs and no closed-form answer.* For a single layer of linear units it is literally the same problem. The authors of the 1986 PDP chapter put it in terms of the error surface: "without hidden units, the error surface is shaped like a bowl with only one minimum, so gradient descent is guaranteed to find the best set of weights" [@rumelhart1986internal, p. 324]. The ADALINE of [the previous chapter](#neuron), minimizing a mean squared error, was doing this in 1960.

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

The gradients can be checked by brute force: nudge each weight by a tiny amount, rerun the network, and measure how the error changes. For this example the two methods agree to about ten decimal places. The difference is cost. Nudging needs a separate forward pass for every weight, and a large language model has billions of weights (see [the destination chapter](#destination)). Backpropagation gets all the gradients from one forward pass and one backward pass. In Schmidhuber's words, in this method "the costs of forward activation spreading essentially equal the costs of backward derivative calculation" [@schmidhuber2014deep, p. 11]. That efficiency is what makes training large networks possible at all.

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

The network has found its own way to compute XOR. Nobody chose its hidden features; they emerged from the blame passed back to them. That is what the 1986 paper claimed as the method's central achievement: "internal 'hidden' units which are not part of the input or output come to represent important features of the task domain" [@rumelhart1986learning, p. 533].

Two features of the run deserve attention. The first is the long flat stretch at the start, where the error sits near 0.5 and the network seems to learn nothing for nearly 300 sweeps; then it drops sharply, and the network has solved XOR by sweep 312. A reader of loss curves learns not to judge a run by its first few hundred steps. The second is that this was one random start out of many possible ones. Repeating the experiment from 100 different random starts, 78 solved XOR within 5,000 sweeps and 22 had not.

## Valleys, plateaus, and a broken symmetry

A bowl has one lowest point. The error surface of a network with hidden units does not have to be a bowl. The 1986 PDP chapter says so directly: with hidden units "the error surface is not concave upwards, so there is the danger of getting stuck in local minima" [@rumelhart1986internal, p. 324]. A **local minimum** is a point lower than everything near it but not the lowest point overall; gradient descent, which only ever looks at the slope where it stands, cannot tell the difference.

The authors' answer was empirical. They called the danger "apparently fatal" and reported that it was "irrelevant in a wide variety of learning tasks" [@rumelhart1986internal, p. 324]. On XOR they wrote that in training it "hundreds of times ... In only two cases has the system encountered a local minimum and thus been unable to solve the problem" [@rumelhart1986internal, p. 331]. The 22 failures in the experiment above are far more than that. The settings differ (the 1986 work used additional techniques, such as a "momentum" term that smooths the steps [@rumelhart1986internal, p. 330], which returns in [the chapter on the training toolkit](#toolkit)), and a run that has not solved XOR after 5,000 sweeps may be stuck on a plateau rather than in a true local minimum. The lesson is not that the 1986 claim was wrong. It is that whether training succeeds depends on choices beyond the method itself: the learning rate, the starting weights, and the number of sweeps.

Starting weights matter in a second, stranger way. Start every weight at the same value, 0.5, and train as before.

<!-- D-009: code/checks/backprop.py, Example 4 -->

After 5,000 sweeps the two hidden units are still exact copies of each other, and the network outputs 0.017, 0.666, 0.666, and 0.667 for the four cases: it has not solved XOR, and it never will. Two identical hidden units receive identical blame, so they make identical changes, and they stay identical forever. The network is effectively stuck with one hidden unit, and one hidden unit is not enough. The PDP chapter names the problem: "If all weights start out with equal values and if the solution requires that unequal weights be developed, the system can never learn" [@rumelhart1986internal, p. 330]. The fix is to start from small random weights. The 1986 letter states the rule plainly, "To break symmetry we start with small random weights" [@rumelhart1986learning, p. 535]; for its symmetry-detecting network, "the initial weights were random and were uniformly distributed between -0.3 and 0.3" [@rumelhart1986learning, p. 534]. Every network in this book starts the same way, with random numbers, which is why [the destination chapter](#destination) said an embedding table starts out random.

## 1986: the paper that made it work

Backpropagation became widely used after two publications in 1986 [@goodfellow2016deep, p. 221] by David Rumelhart and Ronald Williams of the University of California, San Diego, and Geoffrey Hinton, then at Carnegie-Mellon University [@rumelhart1986learning, p. 533]. One was a four-page letter in *Nature*, "Learning representations by back-propagating errors". Its abstract describes "a new learning procedure, back-propagation, for networks of neurone-like units", which "repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the difference between the actual output vector of the net and the desired output vector" [@rumelhart1986learning, p. 533]. The other was a long chapter in the *Parallel Distributed Processing* volumes, which called the method "the **generalized delta rule**" and worked through many examples, XOR among them [@rumelhart1986internal, pp. 322, 330-331].

What made the work persuasive was less the mathematics than the demonstrations [@schmidhuber2014deep, p. 11; @goodfellow2016deep, p. 221]. The networks learned problems that single-layer networks could not, and their hidden units could be inspected and found to represent sensible features. One network in the Nature letter learned to detect mirror symmetry in a row of six inputs, which took "1,425 sweeps through the set of 64 possible input vectors" [@rumelhart1986learning, p. 534]. The authors were also explicit about what they were not claiming: "The learning procedure, in its current form, is not a plausible model of learning in brains" [@rumelhart1986learning, p. 536].

## Who invented backpropagation?

The 1986 papers themselves noted that Parker and Le Cun had found similar procedures independently [@rumelhart1986internal, p. 322; @rumelhart1986learning, p. 535], and later historians have traced the method back much further. The answer depends on what "inventing backpropagation" is taken to mean. Here is the sequence as the sources give it.

- **Control theory, 1960s.** Gradient methods for multi-stage systems, computed by applying the chain rule backward stage by stage, were "discussed at least since the early 1960s" in optimal control, by Kelley, Bryson, and others [@schmidhuber2014deep, p. 11; @goodfellow2016deep, p. 221].
- **Linnainmaa, 1970.** The general, efficient method for computing the derivatives of any sequence of calculations by running backward through it is now called the **reverse mode of automatic differentiation**. Griewank, in a history of that field, recounts that Seppo Linnainmaa of Helsinki "says the idea came to him on a sunny afternoon in a Copenhagen park in 1970", and that he used it to estimate the effect of rounding errors in computations, not to train networks [@griewank2012invented, p. 389]. Griewank adds that Ostrowski had used the idea some five years earlier in chemical engineering [@griewank2012invented, p. 389]. Schmidhuber's survey says that efficient backpropagation in general networks "apparently was first described" in Linnainmaa's 1970 master's thesis, "albeit without reference to NNs" (neural networks) [@schmidhuber2014deep, p. 11].
- **Werbos, 1974 and 1981.** Paul Werbos, a doctoral student in applied mathematics at Harvard in the early 1970s, considered applying a technique for propagating derivatives backward, which he called "dynamic feedback", to neural-network-like problems [@olazaran1993sociological, p. 392]. In the thesis itself he applied it to an example from political science, not to neural networks [@olazaran1993sociological, p. 394]. Schmidhuber describes the 1974 thesis as "preliminary, NN-specific discussion" and dates the first neural-network application of efficient backpropagation to Werbos in 1981 [@schmidhuber2014deep, p. 11]; Goodfellow and colleagues also credit Werbos (1981) with proposing it for training networks [@goodfellow2016deep, p. 221]. In an interview with Olazaran, Werbos recalled that his thesis committee doubted the work and that Minsky, whom he consulted, was discouraging [@olazaran1993sociological, pp. 392-393]. Minsky, interviewed separately, recalled the idea as "certainly trivial" and not practical, adding that "you usually get stuck at a local minimum" [@olazaran1993sociological, pp. 393-394]. These are two participants' recollections, decades later.
- **Parker and LeCun, 1985.** The PDP chapter itself notes that "Parker (1985) has independently derived a similar generalization" and that "Le Cun (1985) has also studied a roughly similar learning scheme" [@rumelhart1986internal, p. 322].
- **Rumelhart, Hinton, and Williams, 1986.** In the textbook account, the idea "was finally developed in practice after being independently rediscovered in different ways", and the PDP chapter "contributed greatly to the popularization of back-propagation" [@goodfellow2016deep, p. 221]. Schmidhuber's survey, which states that one of its goals is "to assign credit to those who contributed to the present state of the art" [@schmidhuber2014deep, p. 1], agrees on the role of the 1986 work: it "significantly contributed to the popularisation" of backpropagation, "experimentally demonstrating the emergence of useful internal representations in hidden layers" [@schmidhuber2014deep, p. 11].

None of these accounts disputes the chronology. They differ in emphasis: whether the credit belongs to the first statement of the mathematics, to its first proposal for neural networks, or to the work that showed it working and made the field adopt it. LeCun, one of the independent discoverers, made the deflationary point in 1988: "back-propagation is little more than an extremely judicious application of the chain rule and gradient descent" [quoted in @olazaran1993sociological, p. 392]. The reverse mode of automatic differentiation, under that name, returns in [the chapter on the training toolkit](#toolkit).

## What a layered network can represent

Backpropagation answered how to train a layered network. A second question remained: how much can such a network represent at all? Two papers in 1989 answered it.

Cybenko showed "that arbitrary decision regions can be arbitrarily well approximated by continuous feedforward neural networks with only a single internal, hidden layer and any continuous sigmoidal nonlinearity" [@cybenko1989approximation, p. 303]. Kurt Hornik, Maxwell Stinchcombe, and Halbert White proved a similar result in more general form: "standard multilayer feedforward networks with as few as one hidden layer using arbitrary squashing functions are capable of approximating any Borel measurable function from one finite dimensional space to another to any desired degree of accuracy, provided sufficiently many hidden units are available" [@hornik1989multilayer, p. 359]. (A **squashing function** is one like the sigmoid, which squeezes any number into a fixed range. "Borel measurable" covers, for practical purposes, any function one would meet.) This result is known as the **universal approximation theorem** [@goodfellow2016deep, p. 194].

It is easy to read too much into it, and both papers warned against doing so. Cybenko wrote: "we have focused only on existence. The important questions that remain to be answered deal with feasibility, namely how many terms in the summation (or equivalently, how many neural nodes) are required" [@cybenko1989approximation, p. 313]. Hornik and colleagues argued that, given their result, failures in practice must come from elsewhere: "inadequate learning, inadequate numbers of hidden units, or the presence of a stochastic rather than a deterministic relation between input and target". And they added: "Our results do not address the issue of how many units are needed to attain a given degree of approximation" [@hornik1989multilayer, p. 360]. The modern textbook summary is blunt: "a feedforward network with a single layer is sufficient to represent any function, but the layer may be infeasibly large and may fail to learn and generalize correctly" [@goodfellow2016deep, p. 195].

A statistician has seen this pattern before. A polynomial of high enough degree can pass through any set of points with distinct x values, and that fact says nothing about whether the fitted polynomial is any good. The universal approximation theorem says that suitable weights exist. It does not say that gradient descent will find them, how many hidden units are needed, or that the result will do well on data it was not trained on. Those three questions, learnability, size, and generalization, are the practical questions of the rest of this book.

## Where this leaves us

By 1989 the field had what it lacked in 1969: a way to train networks with hidden layers, and a theorem saying such networks can approximate essentially any function. It also had a list of practical troubles. Training could stall on plateaus or settle in poor solutions. It depended on the learning rate and the starting weights. And the theorem promised nothing about how big a network had to be.

[The next chapter](#structure) follows what happened when researchers applied these networks to real data, images and sequences, and found that plain layered networks were not enough. Two structural ideas came out of that period, both about using the same weights in many places. A new obstacle also appeared, and it was severe enough that, by the reader's own era, much of machine learning had moved on to other methods.

## What to carry forward

- A hidden unit has no target value of its own. Backpropagation solves the credit assignment problem by computing, for every weight, how the error would change if that weight changed.
- Training means minimizing a loss function, such as the squared error, by gradient descent: repeated small steps downhill, with the step size set by the learning rate. For a single linear layer this is least-squares regression fitted iteratively.
- Backpropagation is the chain rule organized into a forward pass and a backward pass. It gets every gradient for about the cost of running the network twice.
- Training can stall or fail. Starting weights must be random to break the symmetry between hidden units, and the learning rate must be neither too small nor too large.
- The method was found several times between the 1960s and 1985, in different fields. Rumelhart, Hinton, and Williams's 1986 papers made it widely used by showing that hidden units learn useful features.
- The universal approximation theorem (1989) says one hidden layer can approximate any reasonable function, given enough units. It says nothing about how many units, whether training will find the weights, or whether the result will generalize.
