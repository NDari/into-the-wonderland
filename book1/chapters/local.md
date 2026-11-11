# Small models and local inference {#local}

<!-- D-002: intuition only; formulas for weight memory, absmax rounding, and the decoding speed bound, every symbol explained; the KV-cache formula is the generation chapter's. D-003: no code, commands, or flags; model and file names appear as plain text. D-007: installing and running a model, with pinned versions, is Book 2's. D-009: numbers from code/checks/local.py, which reuses code/checks/generation.py. D-014: figures from figures/local.py. D-020: "open-weight" in the book's own voice; "open source" only in the OSI's sense or inside a quotation. -->

The models of the last few chapters were described as if they lived in data centers, reached through a vendor's service. Many do. But many others have been released as files that anyone can download, and some run on a laptop or a phone. In the Llama 2 paper's words, quoted in [the chapter on scale](#scale), releasing trained weights means "the pretraining costs do not need to be incurred by others" [@touvron2023llama2, p. 7].

This chapter gives the knowledge needed to choose such a model and to read its name and its file: what "open" means and what licenses allow; where the models came from and where they are found; how much memory a model needs, and how quantization, introduced in [the chapter on adapting](#adapting), shrinks it; the files and programs that run models; how fast they generate on ordinary hardware; and what small models do well and badly. Installing and running a model are left to Book 2, which pins the versions it uses.

## Why run a model yourself

A **closed model** is reached only through its maker's service: the user sends text and receives text, and the weights never leave the vendor's computers. An **open-weight model** is one whose trained parameters can be downloaded and run on one's own hardware. <!-- D-020 -->

The sources give several reasons to run one. The authors of AWQ, a quantization method described below, wrote that "running LLMs locally on edge devices can reduce the cloud computing cost and protect users' privacy", and that it "enables LLMs to operate offline" [@lin2024awq, p. 1]. Mark Zuckerberg, whose company releases such models and so is an interested party, said organizations "need to train, fine-tune, and distill our own models" and "can't send to closed models over cloud APIs" their sensitive data [@zuckerberg2024open]. And as [the chapter on adapting](#adapting) found, as of 2026-11 the two closed-model vendors it checked offer little self-serve fine-tuning, which leaves fine-tuning mostly to open-weight models. Whether running a model locally is cheaper than paying for a service depends on the hardware and the use; no source used here compares the two.

## What "open" means

The word "open" is contested. Meta announced Llama 2 in July 2023 as "the next generation of our open source large language model" [@meta2023llama2news]. Two days later the Open Source Initiative (OSI), judging the license by its own definition of open-source software, replied that "Meta is confusing "open source" with "resources available to some users under some conditions," two very different things", because the license restricts commercial use for some users and forbids certain uses [@maffulli2023llama].

In October 2024 the OSI published its Open Source AI Definition 1.0. It asks that anyone be free to "Use the system for any purpose and without having to ask for permission", and to study, modify, and share it, which requires the parameters, "The complete source code used to train and run the system", and "Sufficiently detailed information about the data used to train the system so that a skilled person can build a substantially equivalent system" [@osi2024osaid]. The OSI calls a release of weights alone "Open Weights", which "lack several key elements of Open Source AI" [@osi2025openweights]. In software terms, an open-weight model is something like a program distributed as a compiled file without its source code: it can be run, and with effort changed, but not rebuilt.

While writing the definition, the OSI checked models against it. Pythia, OLMo, Amber, CrystalCoder, and T5 passed; Llama 2, Grok, Phi-2, and Mixtral did not, with the caution that these results "are not certifications of any kind" [@osi2025faq]. Mixtral has a permissive license, yet failed: a generous license for the weights is not enough. The strict camp has its own dispute: the definition asks for a description of the training data, not the data, while "Some people believe that full, unfettered access to all training data ... is paramount" [@osi2025faq].

This book takes no side in the naming dispute. It says open-weight for any model whose trained parameters can be downloaded, names the license when it matters, and uses "open source" only in the OSI's sense or in quotation. By the OSI's standard, few large models are open source.

## Licenses

A downloadable model comes with a **license**: its maker's terms for who may use the weights, for what, and on what conditions. The models in this chapter fall into three groups (as of 2026-11). This is orientation, not legal advice; the license file is what binds.

**Standard permissive licenses.** The Apache License 2.0, written for software, grants a "perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license" to copy, modify, and distribute [@apache2004license]. Mistral 7B and Mixtral use it [@mistral2023mistral7b; @jiang2024mixtral, p. 1], and so do "all Qwen3 models" [@yang2025qwen3, p. 1]. Phi-3-mini and DeepSeek-R1 use the MIT license, another permissive one [@huggingface2026api].

**Custom licenses with conditions.** Meta's Llama "community licenses" change from version to version. The Llama 2 license of July 2023 requires any company whose products had, on the release date, more than "700 million monthly active users" to ask Meta for a license, which "Meta may grant to you in its sole discretion"; it forbids using the model "or any output or results" of it "to improve any other large language model"; and it incorporates an **acceptable use policy**, a list of forbidden uses [@meta2023llama2license]. The Llama 3 license of April 2024 keeps these and adds that a distributed model built or improved with Llama 3 must have "Llama 3" at the start of its name [@meta2024llama3license]. The Llama 3.1 license of July 2024 keeps the 700-million-user test but drops the clause about improving other models; a distributed model built with Llama 3.1 or its outputs must instead start its name with "Llama" [@meta2024llama31license]. Google's Gemma Terms of Use, for Gemma models up to Gemma 3 (and 3n), require anyone who redistributes a model to pass on its use restrictions, and reserve Google's right "to restrict (remotely or otherwise) usage" it believes breaks the terms [@google2026gemmaterms].

**Terms that move.** As of 2026-11, Google's terms page sends Gemma 4 to a separate license, which is Apache 2.0 [@google2026gemmaterms; @huggingface2026api]. Terms can also be inherited: DeepSeek's card notes that "DeepSeek-R1-Distill-Llama-8B is derived from Llama3.1-8B-Base and is originally licensed under llama3.1 license" [@huggingface2026api]. A model with DeepSeek's name can carry Meta's conditions.

Some downloads require a request. On Hugging Face, the site described below, a **gated** model's files can be downloaded only after an access request, which shares the user's "username and email address" with the model's authors [@huggingface2026gated]. As of 2026-11-11, Meta's Llama 3.1 and 3.2 and Google's Gemma 3 repositories were gated; the other repositories named here were not [@huggingface2026api].

## A short history of open weights

Releasing weights did not begin in 2023. OpenAI published the full GPT-2 in November 2019, as [the chapter on scale](#scale) told [@openai2019release], and BLOOM, of [the chapter on training](#training), was one of several earlier "public releases of pretrained LLMs"; none, the Llama 2 paper added, were "suitable substitutes for closed "product" LLMs, such as ChatGPT, BARD, and Claude" [@touvron2023llama2, p. 3].

The run of releases this chapter follows began with Meta's LLaMA, on February 24, 2023, at "several sizes (7B, 13B, 33B, and 65B parameters)" [@meta2023llamablog]. It was not freely downloadable: it came under "a noncommercial license focused on research use cases", with access "granted on a case-by-case basis" [@meta2023llamablog], by filling in a form [@meta2023llamav1]. Its selling point was that it "can be run on a single GPU" [@touvron2023llama, p. 1]. By July, Meta reported "more than 100,000 requests for access" [@meta2023llama2news]. Llama 2, that July, was released "to the general public for research and commercial use" [@touvron2023llama2, p. 4]. Others followed, many of them small. Mistral AI's Mistral 7B (September 2023) beat Llama 2 13B "across all evaluated benchmarks", by its makers' account [@jiang2023mistral, p. 1]; its Mixtral 8x7B (December 2023) was a mixture of experts, explained below [@mistral2023mixtral]. Qwen (September 2023) came at 1.8, 7, and 14 billion parameters [@bai2023qwen, pp. 3, 7]. Google's Gemma (February 2024) included a 2-billion-parameter model "for CPU and on-device applications" [@gemmateam2024gemma, p. 1], and Microsoft's 3.8-billion-parameter Phi-3-mini (April 2024) came in a report subtitled "A Highly Capable Language Model Locally on Your Phone" [@abdin2024phi3, p. 1]. Llama 3 (April 2024) and 3.1 (July 2024) came at 8, 70, and 405 billion parameters [@meta2024llama3license; @meta2024llama31license; @grattafiori2024llama, p. 2], and Llama 3.2 (October 2024) added 1- and 3-billion-parameter models for "highly constrained environments, such as mobile devices" [@meta2024llama32card]. DeepSeek-R1 (January 2025) came with "six dense models (1.5B, 7B, 8B, 14B, 32B, 70B) distilled from DeepSeek-R1 based on Qwen and Llama" [@deepseekai2025r1, p. 1]; Gemma 3 (March 2025) ranged from 1 to 27 billion parameters, for "phones, laptops, and high-end GPUs" [@gemmateam2025gemma3, p. 1]; Qwen3 (May 2025) offered six standard ("dense") models from 0.6 to 32 billion parameters and two mixtures of experts, the largest with 235 billion [@yang2025qwen3, p. 3].

The makers' own words vary: Gemma's report says "open models", Qwen3's "open-weight", DeepSeek's "open-source" [@gemmateam2024gemma, p. 1; @yang2025qwen3, p. 2; @deepseekai2024llm, p. 1]. The list stops at 2025 because this chapter's sources do.

## Where models live: the hub and the model card

A **model hub** is a website that hosts model files with their documentation. The largest is Hugging Face's, where "members of the Hugging Face community can host all of their model checkpoints for simple storage, discovery, and sharing"; as of 2026-11, Hugging Face says it hosts over three million models [@huggingface2026hub]. Since any member can upload, the hub holds versions made by others next to a maker's own.

Each model comes with a **model card**, its documentation. Margaret Mitchell and colleagues proposed the idea in 2019: "short documents accompanying trained machine learning models that provide benchmarked evaluation in a variety of conditions", which also "disclose the context in which models are intended to be used" [@mitchell2019model, p. 1]. Their template has sections for the model's details (developer, date, version, type, license), intended use, evaluation, training data, ethical considerations, and caveats [@mitchell2019model, p. 3]. On Hugging Face, the card is the README file of the model's repository, with metadata that include the license [@huggingface2026modelcards].

The original LLaMA card followed that template, down to its license ("Non-commercial bespoke license") [@meta2023llamav1]. A card is where to find a model's exact size, context length, license, and intended uses, and the makers' own benchmark scores, which [the chapter on measuring models](#evaluation) teaches the reader to read with care.

## How much memory: parameters times bits

The first question about any model is whether it fits. [The destination chapter](#destination) gave the arithmetic for the weights:

$$\text{memory for the weights, in bytes} = \frac{N \times b}{8}$$

where $N$ is the number of parameters and $b$ the number of bits each is stored in, on average; dividing by 8 turns bits into bytes. As in that chapter, 1 GB is a billion bytes.

<!-- D-009: code/checks/local.py, Example 3 --> Names round. Hugging Face lists Llama 3.1 8B with 8,030,261,248 parameters and Mistral 7B with 7,241,732,096 [@huggingface2026api]. In the 16-bit numbers of [the chapter on training](#training), the 8B model's weights take 16.06 GB; in 32-bit numbers, 32.12 GB, matching the 32.1 GB in llama.cpp's documentation [@llamacpp2026quantize].

One kind of model breaks the rule that the name gives the size. A **mixture of experts** is a model whose feed-forward part, in each layer, is split into several alternative blocks, called experts, of which each token uses only a few; [the chapter on the transformer since 2017](#since-2017) explains how. Mixtral 8x7B "has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts)" [@jiang2024mixtral, p. 1]. <!-- D-009: code/checks/local.py, Example 6 --> Eight copies of Mistral 7B would be 57.9 billion parameters, but only the feed-forward blocks are multiplied. Mixtral has 46.7 billion parameters [@huggingface2026api], and "only uses 12.9B parameters per token" [@mistral2023mixtral]: its **active parameters**. Memory follows the total: "The memory costs for serving Mixtral are proportional to its sparse parameter count, 47B" [@jiang2024mixtral, p. 4]. The active count matters for speed, below.

## Quantization: fewer bits per weight

The models named here are published in 16-bit numbers [@huggingface2026api], but they can be run in fewer. In the words of llama.cpp, a program described below, quantization "shrinks the model's size and can speed up inference", but "may introduce some accuracy loss" [@llamacpp2026quantize]. The reader has done something similar when binning a continuous variable, or saving a photograph as a lower-quality JPEG: fewer distinct values, a small loss.

The simplest scheme is **round-to-nearest** with a shared scale. Take a **group** of weights (llama.cpp calls it a block), stretch it so that the largest in absolute value lands on the largest integer allowed, round every weight to the nearest integer, and store the integers plus the stretch factor. Tim Dettmers and colleagues described this for 8 bits in 2022: it "scales inputs into the 8-bit range [-127, 127]" using "127 divided by the absolute maximum of the entire tensor" [@dettmers2022llmint8, p. 3]. In symbols:

$$q_i = \operatorname{round}\!\left(\frac{w_i}{s}\right), \qquad s = \frac{\max_j |w_j|}{L}, \qquad w_i \approx s \, q_i$$

Here $w_i$ is one weight in the group; $\max_j |w_j|$ is the largest absolute value in the group; $L$ is the largest integer allowed (127 for 8 bits, 7 in the example below); $s$ is the **scale**, one number shared by the group; and $q_i$ is the integer stored. To use the weight, the runtime multiplies back, $s$ times $q_i$.

<!-- D-009: code/checks/local.py, Example 2 --> Take eight made-up weights: 0.12, -0.31, 0.05, 0.27, -0.08, 0.19, -0.22, and 0.02, rounded to integers from -7 to 7 (a simplification of llama.cpp's simplest 4-bit format, not identical to it). The scale is 0.31 / 7 = 0.0443; the stored integers are 3, -7, 1, 6, -2, 4, -5, and 0; multiplying back gives 0.133, -0.310, 0.044, 0.266, -0.089, 0.177, -0.221, and 0.000. The average error on the first seven is 0.007, against an average size of 0.177 (panel (a) of the figure below).

The scale costs space, so the honest measure of a format is **bits per weight**: everything stored, scales included, divided by the number of weights. <!-- D-009: code/checks/local.py, Example 1 --> In the example, eight 4-bit integers and one 16-bit scale make 6 bits per weight. Real formats use larger groups: llama.cpp's simplest 4-bit format, Q4_0, stores 32 weights as 4-bit numbers with one 16-bit scale [@ggml2026quanttypes], 4.5 bits per weight; its 8-bit Q8_0 is 8.5. A "4-bit" file is not 4 bits per weight.

Groups are used, rather than one scale per matrix, for the reason the reader standardized each column of a data table separately: one range fits no values well. Smaller groups fit better but need more scales; llama.cpp's later formats, the k-quants, nest groups inside "super-blocks" of 256 weights and store the groups' scales in fewer bits [@ggml2026quanttypes].

Most llama.cpp files also mix formats. The type Q4_K_M stores most weights in the 4-bit k-quant but keeps the output layer, and some attention and feed-forward matrices in the first and last eighths of the layers and in every third layer between, at 6 bits [@ggml2026quanttypes]. <!-- D-009: code/checks/local.py, Example 1 --> Measured on Llama 3.1 8B, Q4_K_M averages 4.89 bits per weight, Q4_K_S 4.67, Q3_K_M 4.00, and Q2_K 3.16 [@llamacpp2026quantize]. The names are labels, not bit counts.

## Outliers, and smarter rounding

Rounding works when the numbers in a group are of similar size. One large value spoils it, as one extreme value spoils a min-max scaling of a feature.

![Rounding eight made-up weights to 4-bit integers (-7 to 7) with a shared scale. Each box shows the weight (above), the stored integer (inside), and the value rebuilt from it (below). (a) The scale fits the group. (b) One weight 20 times larger than the others sets the scale, and every other weight rounds to zero. (c) Keeping that weight aside in 16 bits lets the other seven keep their own scale. Illustrative numbers.](../../figures/local-groups.svg){#fig:local-groups}

<!-- D-009: code/checks/local.py, Example 2 --> Replace the last weight with 6.2, twenty times the largest of the others. The scale becomes 6.2 / 7 = 0.886, every other weight is less than half of that, and all seven round to zero: their average error is 0.177, their whole average size. There are two remedies. Keep the few large values aside in 16 bits and round the rest with their own scale, and the error returns to 0.007. Or use smaller groups, which confine the damage: in two groups of four, the group without the large value is unharmed, though its three neighbors are still lost.

Real models have such values. In their 2022 paper LLM.int8(), Dettmers and colleagues found, in the models they studied, "large features with magnitudes up to 20x larger than in other dimensions", spreading through the layers as models grew until, "At around 6.7B parameters, a phase shift occurs" [@dettmers2022llmint8, p. 2]. These **outliers** were in the activations, the intermediate values computed as text passes through the network, concentrated in a few dimensions. Keeping those dimensions, about 0.1% of the values, in 16 bits and the rest in 8 [@dettmers2022llmint8, p. 4] meant that "a 175B parameter 16/32-bit checkpoint can be loaded, converted to Int8, and used immediately without performance degradation" [@dettmers2022llmint8, p. 1]. The 6.7-billion threshold is a finding about the models measured, a family called OPT, not a law.

Below 8 bits, plain rounding loses accuracy. Elias Frantar and colleagues noted in 2022 that round-to-nearest "works well for low compression targets, e.g., 8-bit weights" but fails "at higher rates" [@frantar2023gptq, p. 2]: at 3 bits, the perplexity (the measure of [the prediction chapter](#prediction)) of the largest OPT model went from 8.34 to about 7,300 [@frantar2023gptq, p. 7]. Their method, GPTQ, rounds a layer's weights in turn and adjusts the not-yet-rounded ones to make up for each error, guided by "approximate second-order information" from a small sample of text [@frantar2023gptq, p. 1]. Such a sample, used to tune the rounding rather than to train, is called **calibration data**. GPTQ quantized a 175-billion-parameter model "in approximately four GPU hours, reducing the bitwidth down to 3 or 4 bits per weight, with negligible accuracy degradation" [@frantar2023gptq, p. 1].

In 2023, Ji Lin and colleagues brought the outlier idea to weights. Their AWQ rests on the observation "that weights are not equally important": "a small fraction (0.1%-1%) of salient weights" matters most, and to find them "we should refer to the activation distribution instead of the weight distribution" [@lin2024awq, p. 2]. On an OPT model of 6.7 billion parameters rounded to 3 bits, perplexity was 43.2 with round-to-nearest and 13.0 with 1% of the weights kept in 16 bits; AWQ's own method, which rescales those weights instead of keeping them apart, also reached 13.0 [@lin2024awq, p. 3]. llama.cpp's documentation, as of 2026-11, says its own loss "can be minimized by using a suitable imatrix file", an importance matrix [@llamacpp2026quantize].

All of these round a model after training: **post-training quantization**. The alternative, **quantization-aware training**, continues training briefly with the rounding in the loop, so the model learns to tolerate it. Google did this for Gemma 3's quantized versions, "typically 5,000" steps [@gemmateam2025gemma3, p. 3], and Meta for quantized Llama 3.2, combined with the LoRA of [the chapter on adapting](#adapting) [@meta2024llama32card]. Nor is quantization only a hobbyist's trick: Meta ran most of its 405-billion-parameter model's feed-forward computation in 8-bit numbers [@grattafiori2024llama, p. 52].

## What rounding costs

llama.cpp measures the loss "in Perplexity (ppl) and/or Kullback-Leibler Divergence" [@llamacpp2026quantize], the second a measure of how far the rounded model's probabilities move from the original's. Its tool, as of 2026-11, lists perplexity increases for Llama 3 8B of 0.0026 at Q8_0, 0.0217 at Q6_K, 0.0569 at Q5_K_M, 0.1754 at Q4_K_M, 0.6569 at Q3_K_M, and 3.5199 at Q2_K, over a baseline and on a text it does not state [@llamacpp2026quantize]. Without the baseline these cannot be turned into percentages, but the pattern is plain: almost nothing at 8 and 6 bits, small at 5 and 4, growing fast below 4. They are llama.cpp's own indicative figures for one model.

Small models pay more. GPTQ's authors noted that "larger models generally (with the exception of OPT-66B) appear easier to quantize" [@frantar2023gptq, p. 7]. <!-- D-009: code/checks/local.py, Example 9 --> At 4 bits, the perplexity of a 125-million-parameter OPT model rose 12.5%, that of the 175-billion one 0.4% [@frantar2023gptq, p. 7]. Meta's Llama 3.2 card shows the same on a modern model. On MMLU, a broad multiple-choice test that [the chapter on measuring models](#evaluation) describes, the instruction-tuned 1B model scored 49.3 in 16 bits, 43.3 after plain post-training rounding, and 49.0 with quantization-aware training [@meta2024llama32card]: plain rounding cost 6.0 points, and Meta did not release that version. For the 3B model the costs were 2.9 and 1.0 points [@meta2024llama32card]. The cheapest model to run is also the most fragile to squeeze.

## The memory table

Putting the pieces together gives the chapter's main table.

<!-- D-009: code/checks/local.py, Example 3 -->

| Model | Billion parameters | F16 | Q8_0 | Q6_K | Q5_K_M | Q4_K_M | Q3_K_M | Q2_K |
|--------------|---------:|------:|------:|------:|---------:|---------:|---------:|------:|
| Bits per weight | | 16.00 | 8.50 | 6.56 | 5.70 | 4.89 | 4.00 | 3.16 |
| Llama 3.2 1B | 1.24 | 2.5 | 1.3 | 1.0 | 0.9 | 0.8 | 0.6 | 0.5 |
| Llama 3.2 3B | 3.21 | 6.4 | 3.4 | 2.6 | 2.3 | 2.0 | 1.6 | 1.3 |
| Phi-3-mini | 3.82 | 7.6 | 4.1 | 3.1 | 2.7 | 2.3 | 1.9 | 1.5 |
| Llama 3.1 8B | 8.03 | 16.1 | 8.5 | 6.6 | 5.7 | 4.9 | 4.0 | 3.2 |
| Qwen3-8B | 8.19 | 16.4 | 8.7 | 6.7 | 5.8 | 5.0 | 4.1 | 3.2 |
| Mixtral 8x7B | 46.70 | 93.4 | 49.6 | 38.3 | 33.3 | 28.6 | 23.3 | 18.4 |
| Llama 3.1 70B | 70.55 | 141 | 75.0 | 57.9 | 50.3 | 43.2 | 35.2 | 27.9 |

Table: Memory for the weights alone, in GB (a billion bytes): parameter counts from Hugging Face (read 2026-11-11) [@huggingface2026api] times bits per weight, divided by 8. Bits per weight for F16, Q8_0, and Q6_K come from llama.cpp's block layouts; those for the mixed types were measured by llama.cpp on Llama 3.1 8B, and other models differ slightly [@ggml2026quanttypes; @llamacpp2026quantize]. Not included: the KV cache and the runtime's working memory.

<!-- D-009: code/checks/local.py, Example 3 --> The table agrees with llama.cpp's own figures where they overlap: 14.96 GiB in 16 bits and 4.58 GiB at Q4_K_M for Llama 3.1 8B (a GiB is $2^{30}$ bytes, about 1.074 GB), and 43.1 GB for the 70B model at Q4_K_M [@llamacpp2026quantize]. Phi-3's report gives "≈ 1.8GB" for its 4-bit model [@abdin2024phi3, p. 3], less than the table; the report does not name its format, and exactly 4 bits per weight would give 1.91 GB.

![Memory needed by the models of the table. (a) The weights alone, in GB, at each llama.cpp type, shaded against memory sizes a reader may own: up to 16 GB (a 16 GB graphics card), 32 GB, 64 GB, and 128 GB (the most Apple's M4 Max offered in 2024). (b) Three models at Q4_K_M with a 16-bit KV cache at 8K and 32K tokens of context. Computed for this chapter; parameter counts as of 2026-11-11; no allowance for the runtime's own working memory.](../../figures/local-memory.svg){#fig:local-memory}

The weights are not the whole bill. The KV cache of [the chapter on generation](#generation) grows with the context: per token, 2 (a key and a value) times the number of layers, times the number of key-value heads, times the dimension of each head, times the bytes per number.

<!-- D-009: code/checks/local.py, Examples 4 and 5 -->

| Model | Cache per token | 8K tokens | 32K tokens | Q4_K_M weights plus 32K cache |
|--------------|---------------:|----------:|----------:|------------------:|
| Llama 3.1 8B | 131,072 bytes | 1.07 GB | 4.29 GB | 9.21 GB |
| Qwen3-8B | 147,456 bytes | 1.21 GB | 4.83 GB | 9.84 GB |
| Llama 3.1 70B | 327,680 bytes | 2.68 GB | 10.74 GB | 53.90 GB |

Table: The KV cache in 16-bit numbers at fixed context lengths of 8,192 and 32,768 tokens. Layers, key-value heads, and head dimensions from the Llama 3 paper [@grattafiori2024llama, p. 7] and Qwen3-8B's configuration file [@huggingface2026api]. The other models of the memory table are left out because this chapter's sources do not give their configurations.

<!-- D-009: code/checks/local.py, Example 4 --> These models keep the cache small by sharing each key and value among several query heads, the grouping of [the anatomy chapter](#anatomy). Phi-3-mini does not: it has as many key-value heads as query heads, 32 [@huggingface2026api], and stores 393,216 bytes per token, three times as much as the larger Llama 3.1 8B; its full 4,096-token window takes 1.61 GB, against 2.34 GB of weights at Q4_K_M. Runtimes can also store the cache in 8 or 4 bits, though as of 2026-11 llama.cpp's server and Ollama, both described below, use 16 by default [@llamacpp2026server; @ollama2026docs]; Ollama's documentation calls the loss "very small" at 8 bits and "small-medium" at 4 [@ollama2026docs]. For Llama 3.1 8B at 32K tokens, an 8-bit cache takes 2.28 GB instead of 4.29.

The context length is a setting: as of 2026-11, llama.cpp's server by default takes it from the model file, while Ollama uses 4,096 tokens [@llamacpp2026server; @ollama2026docs]. A maker's own table makes the same point: Google gives, for Gemma 3 4B at 32,768 tokens with an 8-bit cache, 2.6 GB for 4-bit weights and 7.3 GB with the cache [@gemmateam2025gemma3, p. 3]. And every runtime needs some memory of its own beyond weights and cache; no source used here gives a general figure, so the tables add none.

Whether a model fits depends on where it runs. A graphics card has its own memory, **VRAM**: 16 GB on NVIDIA's RTX 4080, 24 GB on the RTX 4090, 32 GB on the RTX 5090 [@nvidia2025blackwell, pp. 14-15, 49-50]. Apple's chips use **unified memory**, one pool shared by the processor and the graphics unit; Apple's machine-learning library describes how "Arrays in MLX live in shared memory" and can be used by any device "without transferring data" [@mlx2026readme]. The M4 Max of 2024 offers up to 128 GB [@apple2024m4pro]. So the weights of Llama 3.1 70B at Q4_K_M (43.2 GB) fit on none of those graphics cards, but do fit in a 64 GB or 128 GB Mac. Apple's claim that the M4 Max handles models "that have nearly 200 billion parameters" [@apple2024m4pro] fits the arithmetic (100 GB at 4 bits), but says nothing about speed. A model too big for VRAM can still run by **offloading**: keeping some layers on the graphics card and the rest in ordinary memory, run by the main processor, which llama.cpp calls "CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity" [@llamacpp2026readme]. The price is in the section on speed.

## Model files

A model on the hub is a set of files, and the format matters for safety and convenience.

Pickle, a general format for saving Python objects, was in 2024, in Hugging Face's words, "the default format for PyTorch model weights", and loading one can trigger "dangerous arbitrary code execution attacks" [@huggingface2024pickle]: a pickle file can carry instructions as well as numbers. The **safetensors** format is "a new simple format for storing tensors safely (as opposed to pickle) and that is still fast": a short header listing each tensor's name, number type, shape, and position, then the raw numbers [@safetensors2026readme]. It is data only, like a data file with a header row. The repositories named in this chapter publish their weights this way, in 16-bit numbers, except DeepSeek-R1, mostly in 8-bit [@huggingface2026api].

Runtimes built on llama.cpp use **GGUF**, introduced on August 21, 2023 as a deliberate break: "all existing ggml models will no longer be compatible after merging" [@llamacpp2023ggufpr]. Its specification calls it "a file format for storing models for inference with GGML", the library llama.cpp is built on, "designed to be unambiguous by containing all the information needed to load a model" [@ggml2026gguf]. Beside the quantized weights, one GGUF file holds the license, the context length "that the model was trained on", a template that "specifies the input format expected by the model", and the quantization type of most of the tensors [@ggml2026gguf]; in Hugging Face's words, "unlike tensor-only file formats like safetensors", GGUF "encodes both the tensors and a standardized set of metadata" [@huggingface2026gguf]. Models are "traditionally developed using PyTorch or another framework, and then converted to GGUF" [@ggml2026gguf], and llama.cpp's tool turns such a file, "typically in a high-precision format like F32 or BF16", into a quantized one [@llamacpp2026quantize].

## Reading a model's name

GGUF's specification proposes a naming convention: a base name, a size label, a fine-tuning label, a version, the encoding, a file type, and, for models split across files, a shard number such as part 1 of 3. It warns that the convention "is not intended to be perfectly parsable in the field" [@ggml2026gguf]. Its own example is Mixtral-8x7B-v0.1-KQ2: model name Mixtral, expert count 8, parameter count 7B, version 0.1, encoding KQ2 [@ggml2026gguf]. A typical name the reader will meet, Llama-3.1-8B-Instruct-Q4_K_M, reads as follows.

| Part | Example | What it says | Caution |
|------------------|--------------|------------------------|-------------------------------------|
| Family and version | Llama-3.1 | the maker's model line | the license can change between versions |
| Size label | 8B | parameters, rounded | the exact count is on the card |
| Variant | Instruct | base or instruction-tuned | "Chat" and other labels are used too |
| Encoding | Q4_K_M | quantization type | not the bits per weight |

Table: Reading a model file name, following the GGUF naming convention [@ggml2026gguf].

**Size.** For a mixture of experts the label may give the expert count, as in 8x7B, which is not 56 billion parameters, or total and active parameters, as in Qwen3-235B-A22B, which "has a total of 235B parameters with 22B activated ones" [@yang2025qwen3, p. 3]. Labels are not always parameter counts: as of 2026-11, Google's gemma-4-E2B-it stores 5.12 billion parameters [@huggingface2026api]; what its label means is for its card to explain.

**Variant.** A **base model** has only been pretrained: it continues text. The LLaMA card warns that it "has not been trained with human feedback, and can thus generate toxic or offensive content, incorrect information or generally unhelpful answers" [@meta2023llamav1]. An **instruct model** (instruction-tuned model) has been further trained to follow instructions and converse, the subject of [the chapter on following instructions](#instructions). Both have the same size: Hugging Face lists Llama-3.1-8B and Llama-3.1-8B-Instruct with the same 8,030,261,248 parameters [@huggingface2026api]. For chatting, the reader wants the instruct version.

**Context length.** Some names include it: Phi-3-mini comes in "two variants 4K and 128K which is the context length (in tokens) that it can support" [@huggingface2026api]. But the name is not the authority: Llama 3.2 1B and 3B support 128K tokens, while Meta's own quantized versions of them support 8K [@meta2024llama32card]. Read the card.

**Encoding.** The quantization type, as in the tables above. Other tools use plainer labels: the default model of Apple's MLX tools, as of 2026-11, is mlx-community/Llama-3.2-3B-Instruct-4bit [@mlx2026readme], a repository named by its owner and then the model.

## Runtimes

A **runtime**, or inference engine, is the program that loads the weights and runs the loop of [the chapter on generation](#generation). Three are common for local use, as of 2026-11.

**llama.cpp** started on March 10, 2023, two weeks after LLaMA, as "Inference of Facebook's LLaMA model in pure C/C++" by Georgi Gerganov [@llamacpp2023readme; @ollama2026docs]. "The main goal is to run the model using 4-bit quantization on a MacBook", the first README said, adding "This was hacked in an evening - I have no idea if it works correctly"; it "Runs on the CPU", the main processor [@llamacpp2023readme]. <!-- D-009: code/checks/local.py, Example 8 --> Its printed example ran the 7-billion-parameter LLaMA, 4,017 MB at 4 bits, at 61.41 ms per token, about 16 tokens per second, on a machine the README does not name, with the sampling settings (temperature 0.8, top-k 40, top-p 0.95) that [the chapter on generation](#generation) quoted as llama.cpp's defaults today [@llamacpp2023readme]. As of 2026-11, llama.cpp aims at inference "with minimal setup and state-of-the-art performance on a wide range of hardware", supports quantization from 1.5 to 8 bits, runs on Apple chips and on NVIDIA and AMD graphics cards, can split a model between processor and graphics card, and is released under the MIT license [@llamacpp2026readme]. Book 2 uses it.

**Ollama** is a popular program that downloads and runs models with llama.cpp underneath: its README lists "llama.cpp project founded by Georgi Gerganov" among its "Supported backends" [@ollama2026docs]. As of 2026-11 it keeps a model in memory for five minutes after use and reports where a model was loaded, for example "48%/52% CPU/GPU" for a model split between ordinary memory and the graphics card; its README now also offers models "locally or in the cloud" [@ollama2026docs].

**MLX** is "an array framework for machine learning on Apple silicon, brought to you by Apple machine learning research"; its companion, MLX LM, generates text with models from the Hugging Face hub, fine-tunes them, and quantizes them [@mlx2026readme].

These runtimes differ in interface and in the files they read, but they share this chapter's arithmetic: the same weights, the same cache, the same memory.

## How fast: reading every weight

[The chapter on generation](#generation) explained that decoding is limited by memory traffic rather than arithmetic: each new token requires reading every weight, and the KV cache, from memory, to do only a little arithmetic with each number. AWQ's authors made it concrete for the RTX 4090: with "a peak computation throughput of 165 TFLOPS and a memory bandwidth of 1TB/s" (165 trillion operations per second), any task with fewer than 165 operations per memory access is limited by memory, and generating text in 16 bits does about one [@lin2024awq, p. 6]. It is like a database query that waits on the disk, not the processor.

That gives a ceiling. The **memory bandwidth** of a machine is the number of bytes per second its memory can deliver to the processor. Then

$$\text{tokens per second} \le \frac{B}{M}$$

where $B$ is the memory bandwidth in bytes per second and $M$ the bytes read per token: the weights, plus the KV cache so far. This is an upper bound, not a prediction: real systems reach a fraction of a vendor's peak bandwidth and have other costs. It also shows why quantization speeds up generation: fewer bytes per weight, fewer bytes to read. In AWQ's words, weight-only quantization "speeds up the token generation (remedies memory-bound workload)" [@lin2024awq, p. 2].

![Upper bounds on decoding speed for Llama 3.1 8B at Q4_K_M (4.91 GB of weights), from each device's peak memory bandwidth as published by its maker, with the KV cache ignored. The dot is the one measurement here with named hardware: llama.cpp's benchmark example, for a similar-sized model on the RTX 4080, at 78% of its bound. Real speeds are lower than the bounds. Bandwidths: Apple, October 2024 and October 2025; NVIDIA, whitepaper of 2025.](../../figures/local-bandwidth.svg){#fig:local-bandwidth}

<!-- D-009: code/checks/local.py, Example 7 --> The figure applies the bound to Llama 3.1 8B at Q4_K_M with vendors' figures: Apple's M4 at 120 GB/s, M4 Pro at 273, and M4 Max at up to 546 (announced October 2024) [@apple2024m4pro], and M5 at 153 (October 2025) [@apple2025m5]; NVIDIA's RTX 4080 at 716.8 GB/s, RTX 4090 at 1,008, and RTX 5090 at 1,792 [@nvidia2025blackwell, pp. 14-15, 49-50]. The bounds run from 24 tokens per second on the M4 to 365 on the RTX 5090. In 16 bits, the model does not fit in the RTX 4080's 16 GB, and the RTX 5090's bound falls to 112. For Llama 3.1 70B at Q4_K_M, the bound is 12.6 tokens per second on the M4 Max and 6.3 on a 64 GB M4 Pro. As of 2026-11, Apple's MacBook Pro specifications list up to 614 GB/s, for the M5 Max [@apple2026mbpspecs]; such figures change with every product.

<!-- D-009: code/checks/local.py, Example 8 --> How close do real systems come? llama.cpp's benchmarking documentation reports one run with named hardware, an NVIDIA RTX 4080 with an AMD Ryzen 7 7800X3D processor, tested on April 24, 2025: Qwen2.5-7B-Instruct at Q4_K_M, a 4.68 GB file, generated 119.92 tokens per second, not counting tokenization and sampling [@llamacpp2026bench]. The bound for that file on that card is 153.3; the run reached 78% of it. The same run read its 512-token prompt at 7,285.68 tokens per second [@llamacpp2026bench], about 61 times faster, because a prompt's tokens pass through the network together.

<!-- D-009: code/checks/local.py, Example 8 --> Speed follows size. On a OnePlus 12 phone, Meta's 4-bit Llama 3.2 1B, in a file 46% the size of the 16-bit one, generated 50.2 tokens per second against 19.2, 2.6 times as fast [@meta2024llama32card]. Not exactly, though: in llama.cpp's table for Llama 3.1 8B, on hardware it does not state, Q4_K_M generated 71.93 tokens per second against 29.17 for 16 bits [@llamacpp2026quantize], 2.47 times faster from a file 3.27 times smaller, and below about 4 bits speed hardly improves; presumably, though the table does not say, unpacking the bits starts to cost as much as reading them.

<!-- D-009: code/checks/local.py, Example 8 --> Offloading is costly, because the slowest part sets the pace. In llama.cpp's benchmark documentation (a 7-billion-parameter model at 4 bits, hardware not named), generation ran at 13.45 tokens per second with 10 of 35 layers on the graphics card, 54.78 with 32, and 131.66 with all 35 [@llamacpp2026bench]. On the main processor alone, another example went from 4.05 tokens per second with one thread to 16.71 with eight, and no faster with 32 [@llamacpp2026bench]: consistent with a memory limit, though the documentation does not say so.

<!-- D-009: code/checks/local.py, Examples 6 and 7 --> For a mixture of experts, memory follows the total parameters and the reading per token the active ones. At Q4_K_M, Mixtral needs 28.6 GB in memory but reads only about 7.9 GB per token (an approximation from its 12.9 billion active parameters): on an M4 Max, a bound of 69 tokens per second, against 19 if every weight were read. Mistral AI's announcement said Mixtral generates "at the same speed and for the same cost as a 12.9B model" [@mistral2023mixtral]; the paper is more careful, noting that choosing experts adds overhead and that such models "are more suitable for batched workloads" [@jiang2024mixtral, p. 4]. <!-- D-009: code/checks/local.py, Example 7 --> Long contexts slow things too, since the cache is read for every token: with 32K tokens of cache, Llama 3.1 8B at Q4_K_M reads 9.21 GB per token, and the RTX 4090's bound falls from 205 to 109.

Small devices work, slowly: Phi-3-mini at 4 bits ran on an iPhone 14 at "more than 12 tokens per second" [@abdin2024phi3, p. 3], and a 7-billion-parameter model on a Raspberry Pi 4B at 0.7 [@lin2024awq, p. 11].

## Will it run?

In short: take the exact parameter count from the card; choose a quantization type (llama.cpp's own documentation uses Q4_K_M as its example [@llamacpp2026quantize]) and multiply by its bits per weight, divided by 8; add the KV cache for the context needed; leave room for the runtime. If the total fits in VRAM or a Mac's unified memory, the bandwidth divided by the bytes read per token bounds the speed. If it fits only with offloading, expect much less.

## What small models are and are not good at

Fitting is not the same as being good enough. Smaller models score lower, and the gap is widest on the hardest tests. In Meta's evaluations of its instruction-tuned Llama 3 models, the 8-billion-parameter model scored 69.4 on MMLU against 83.6 for the 70-billion one and 87.3 for 405 billion; on MATH, a test of mathematics problems, 51.9, 68.0, and 73.8 [@grattafiori2024llama, p. 3]. Among pretrained models, Llama 3.2 1B scored 32.2 on MMLU, 3B 58, and Llama 3.1 8B 66.7; Meta's suggested uses for the 1B and 3B models are narrow: "assistant-like chat and agentic applications like knowledge retrieval and summarization, mobile AI powered writing assistants and query and prompt rewriting" [@meta2024llama32card]. On a summarization test in the same card, the 1B, 3B, and 8B instruction-tuned models scored about the same (16.8, 19.0, and 17.2) [@meta2024llama32card]: for some jobs, small is enough.

What small models lose first, according to their makers, is stored facts. Mistral 7B "largely outperforms Llama 2 13B on all evaluations, except on knowledge benchmarks, where it is on par", which its authors put down, as "likely", to "its limited parameter count, which limits the amount of knowledge it can compress" [@jiang2023mistral, p. 5]. Phi-3's report is blunter: the model "simply does not have the capacity to store too much "factual knowledge", which can be seen for example with low performance on TriviaQA", a test of trivia questions [@abdin2024phi3, p. 9]. <!-- D-009: code/checks/local.py, Example 10 --> In its table, the 3.8-billion-parameter Phi-3-mini scored 68.8 on MMLU, 7.1 points above Mistral 7B, but 64.0 on TriviaQA, 11.2 points below [@abdin2024phi3, p. 6]. The proposed remedy is "augmentation with a search engine" [@abdin2024phi3, p. 9]: giving the model facts in its input, the subject of [the chapter on knowledge and tools](#tools).

A small model can also be trained for one strength. DeepSeek reported that its 1.5-billion-parameter distilled model "outperforms GPT-4o and Claude-3.5-Sonnet on math benchmarks with 28.9% on AIME and 83.9% on MATH" [@deepseekai2025r1, p. 16]: two mathematics tests, a narrow result. All these numbers are the makers' own evaluations of their own models; [the chapter on measuring models](#evaluation) explains why such numbers deserve caution.

## What to carry forward

- An open-weight model's parameters can be downloaded and run locally. "Open source" in the OSI's 2024 sense also requires the training code and enough information about the data to rebuild the model; few large models meet it.
- Licenses differ and change between versions: Apache 2.0 or MIT for some models, Meta's and Google's own terms with conditions for others. A distilled model can inherit its base model's license.
- The current run of downloadable models began with LLaMA in February 2023, by application and for research; GPT-2 (2019) and BLOOM (2022) came earlier. Models are found on hubs such as Hugging Face and documented by model cards.
- Memory for the weights is parameters times bits per weight, divided by 8. Names round; a mixture of experts needs memory for all its parameters ("8x7B" is 46.7 billion, not 56).
- Quantization rounds weights to a few levels with a scale shared by each small group. Real formats cost more bits than their names say (Q4_0 is 4.5, Q4_K_M about 4.9). Outliers spoil shared scales; LLM.int8(), GPTQ, and AWQ keep important values precise, compensate, or rescale.
- Rounding costs little at 8 to 4 bits and more below; small models suffer most. Quantization-aware training reduces the loss.
- The KV cache grows with the context and can rival the quantized weights; runtimes also need working memory of their own.
- safetensors and GGUF store data, not code; GGUF also carries the metadata a runtime needs. llama.cpp (2023) is the engine under many tools; Ollama wraps it; MLX serves Apple machines.
- Decoding speed is bounded by memory bandwidth divided by the bytes read per token; real systems reach a fraction of it. Offloading costs a lot. A mixture of experts reads only its active parameters per token.
- Small models trail on hard tests and stored facts and match larger ones on some narrow tasks, by their makers' own scores (2024-2025).
