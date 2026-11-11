# Claim ledger: local

Chapter: `local` (Book 1, "Small models and local inference").
Stage: drafted, 2026-11-11 [D-005]. Research by a helper agent; drafted by a drafting agent from this ledger; independent check pending.
Research for this chapter was done by a helper agent in one session. Every source below was fetched on 2026-11-11 and each claim was located in the fetched copy. Papers were read with pdftotext (plain and `-layout`) from arXiv PDFs; one table (Phi-3, p. 6) was read on the page image. Repository documents were read as raw files from GitHub at the commit given; web pages were converted to text and searched. Model metadata (parameter counts, licences, gating) was read from the Hugging Face model API. Current-practice claims are stamped "as of 2026-11". Where a source prints an en-dash or em-dash (for example "Mistral 7B - Instruct", "7-billion-parameter", page ranges), it is written here with a hyphen. Numbers marked "computed" were run once in this session in a scratch script and must be re-produced by `code/checks/local.py` [D-009].

## Sources and how they were read

Papers (printed page = PDF page unless stated):

| Key | Read from | Notes |
|---|---|---|
| `dettmers2022llmint8` (new) | https://arxiv.org/pdf/2208.07339v2 | arXiv v2, 10 Nov 2022 (v1 15 Aug 2022); arXiv comment "Published at NeurIPS 2022. Camera-ready version". No printed page numbers; pages are PDF pages. |
| `frantar2023gptq` (new) | https://arxiv.org/pdf/2210.17323v2 | arXiv v2, 22 Mar 2023 (v1 31 Oct 2022); header "Published as a conference paper at ICLR 2023". Printed page = PDF page. Tables 3, 4, 5, 6 read in `-layout` text. |
| `lin2024awq` (new) | https://arxiv.org/pdf/2306.00978v6 | arXiv v6, 25 Apr 2026 (v1 1 Jun 2023). Footnote p. 1: "Proceedings of the 7th MLSys Conference, Santa Clara, CA, USA, 2024". Pages are PDF pages. Earlier versions not read; numbers may differ there. |
| `mitchell2019model` (existing in the working tree) | https://arxiv.org/pdf/1810.03993v2 | arXiv v2, 14 Jan 2019; carries the FAT* '19 copyright block and DOI 10.1145/3287560.3287596. Pages are PDF pages of the arXiv copy. Same version as the key's note. |
| `jiang2023mistral` (existing in the working tree) | https://arxiv.org/pdf/2310.06825v1 | arXiv v1, 10 Oct 2023 (only version). Printed page = PDF page. |
| `jiang2024mixtral` (existing in the working tree) | https://arxiv.org/pdf/2401.04088v1 | arXiv v1, 8 Jan 2024 (only version). |
| `bai2023qwen` (new) | https://arxiv.org/pdf/2309.16609v1 | arXiv v1, 28 Sep 2023. |
| `yang2025qwen3` (new) | https://arxiv.org/pdf/2505.09388v1 | arXiv v1, 14 May 2025. |
| `gemmateam2024gemma` (new) | https://arxiv.org/pdf/2403.08295v4 | arXiv v4, 16 Apr 2024 (v1 13 Mar 2024); title page dated 2024-02-21. |
| `gemmateam2025gemma3` (new) | https://arxiv.org/pdf/2503.19786v1 | arXiv v1, 25 Mar 2025; title page dated 2025-03-12. Table 3 read in `-layout` text. |
| `deepseekai2024llm` (new) | https://arxiv.org/pdf/2401.02954v1 | arXiv v1, 5 Jan 2024. |
| `deepseekai2025r1` (existing in the working tree; its note records v1) | https://arxiv.org/pdf/2501.12948v1 and https://arxiv.org/pdf/2501.12948v2 | Claims located in v1 (22 Jan 2025), whose pages are cited; v2 (4 Jan 2026) was read first and its pages are given for reference only. |
| `abdin2024phi3` (new) | https://arxiv.org/pdf/2404.14219v4 | arXiv v4, 30 Aug 2024 (v1 22 Apr 2024). Table on p. 6 read on the page image. |
| `touvron2023llama` (existing) | https://arxiv.org/pdf/2302.13971 | v1 (only version). |
| `touvron2023llama2` (existing) | https://arxiv.org/pdf/2307.09288 | v2. |
| `grattafiori2024llama` (existing) | https://arxiv.org/pdf/2407.21783 | v3, 23 Nov 2024. Printed page = PDF page. |
| `pope2022efficiently` (existing) | https://arxiv.org/pdf/2211.05102v1 | v1. |

Repository and project documents (primary for their own projects):

| Key | Read from | Notes |
|---|---|---|
| `llamacpp2026readme` (new) | https://github.com/ggml-org/llama.cpp, `README.md` | Last commit touching the file 85822a7ab9cb (2026-11-10). Repository metadata from the GitHub API: created 2023-03-10, licence MIT, description "LLM inference in C/C++". |
| `llamacpp2023readme` (new) | `README.md` at commits b85028522d6e (2023-03-10 22:09 UTC) and 1a0a74300f35 (2023-03-12) | The launch-week README. The first commit creating it is 775328064e69 (2023-03-10 19:47 UTC). |
| `llamacpp2026quantize` (new) | `tools/quantize/README.md` (last commit ad1b88ca0d37, 2026-06-05) and `tools/quantize/quantize.cpp` (last commit 71a6a114bca2, 2026-11-11) | The README's tables and the `QUANT_OPTIONS` list in the C++ file. |
| `ggml2026quanttypes` (new) | `ggml/src/ggml-common.h` (last commit 85c55223caf0, 2026-08-31) and `src/llama-quant.cpp` (last commit bcb0152876e8, 2026-11-06), both in ggml-org/llama.cpp | Block layouts of quantization types; rules for which tensors a mixed type such as Q4_K_M keeps at higher precision. |
| `llamacpp2026bench` (new) | `tools/llama-bench/README.md` (last commit f39148a953e5, 2026-10-09) | Example benchmark outputs. |
| `llamacpp2023ggufpr` (new) | https://github.com/ggml-org/llama.cpp/pull/2398 (GitHub API) | Title "GGUF", merged 2023-08-21T20:07:43Z by ggerganov, merge commit 6381d4e110bd. |
| `llamacpp2026server` (existing) | `tools/server/README.md` | Same last commit as the existing key, 08f945ffb5c3 (2026-11-09). |
| `ggml2026gguf` (new) | https://github.com/ggml-org/ggml, `docs/gguf.md` | Last commit cd6d2b75f5d3 (2026-11-08). The spec document was first added 2023-11-01 (commit 54cec9f619d7, "gguf : add file format specification (#302)"). |
| `safetensors2026readme` (new) | https://github.com/huggingface/safetensors, `README.md` | Last commit 62e4d8b86063 (2026-04-15). |
| `ollama2026docs` (new) | https://github.com/ollama/ollama: `README.md` (51e7030f9442, 2026-11-06), `docs/faq.mdx` (33a3afa604b4, 2026-10-13), `docs/import.mdx` (98acec40ae2b, 2026-09-15) | |
| `mlx2026readme` (new) | https://github.com/ml-explore/mlx `README.md` (9bfc476d72dc, 2025-10-13) and https://github.com/ml-explore/mlx-lm `README.md` (47e43a4526d4, 2026-09-24) | |
| `huggingface2026hub` (new) | https://github.com/huggingface/hub-docs: `docs/hub/index.md` (5924f53455e1, 2026-11-06), `docs/hub/models-the-hub.md` (43b6254cb8e6, 2025-04-01) | Source of the rendered pages at https://huggingface.co/docs/hub. |
| `huggingface2026modelcards` (new) | hub-docs `docs/hub/model-cards.md` (610ed94de60a, 2026-11-09) | |
| `huggingface2026gated` (new) | hub-docs `docs/hub/models-gated.md` (83a805d00d61, 2026-10-23) | |
| `huggingface2026gguf` (new) | hub-docs `docs/hub/gguf.md` (03cb41aadd63, 2026-01-28) | |
| `huggingface2024pickle` (new) | hub-docs `docs/hub/security-pickle.md` (810aeb31d2e4, 2024-03-14) | |
| `huggingface2026api` (new) | https://huggingface.co/api/models/{repo} for the repos listed in LC26 | Read 2026-11-11. Each repo's revision SHA is recorded in LC26. Also `config.json` for Qwen/Qwen3-8B, mistralai/Mistral-7B-v0.1, microsoft/Phi-3-mini-4k-instruct, and the README (model card) of deepseek-ai/DeepSeek-R1, deepseek-ai/DeepSeek-V3, microsoft/Phi-3-mini-4k-instruct. |
| `meta2023llamav1` (new) | https://github.com/meta-llama/llama, branch `llama_v1` (head 57b0eb62de06, 2023-03-07): `README.md`, `MODEL_CARD.md`, `LICENSE` | The original LLaMA release repository (then facebookresearch/llama). |
| `meta2023llama2license` (new) | meta-llama/llama `LICENSE` (main, last commit 7c0a08ec24ce, 2023-07-21) | "LLAMA 2 COMMUNITY LICENSE AGREEMENT". |
| `meta2024llama3license` (new) | meta-llama/llama3 `LICENSE` (last commit dab0ae890fd0, 2024-04-15) | "META LLAMA 3 COMMUNITY LICENSE AGREEMENT", includes the Acceptable Use Policy text. |
| `meta2024llama31license` (new) | meta-llama/llama-models `models/llama3_1/LICENSE` (last commit 1f0feb795a41, 2024-07-23) | "LLAMA 3.1 COMMUNITY LICENSE AGREEMENT". |
| `meta2024llama32card` (new) | meta-llama/llama-models `models/llama3_2/MODEL_CARD.md` (last commit 4a9ff6aede5c, 2024-10-24) | The Hugging Face copy is gated and was not read. |

Web pages:

| Key | Read from | Notes |
|---|---|---|
| `osi2024osaid` (new) | https://opensource.org/ai/open-source-ai-definition | "Open Source AI Definition - 1.0". Page metadata: published 2024-10-28, modified 2026-08-26. |
| `osi2025openweights` (new) | https://opensource.org/ai/open-weights | OSI explainer page; metadata published 2025-01-29, modified 2025-08-22. No author named. |
| `osi2025faq` (new) | https://opensource.org/ai/faq | "The Open Source AI Definition 1.0 FAQs"; metadata published 2025-01-21, modified 2025-06-17. |
| `maffulli2023llama` (new) | https://opensource.org/blog/metas-llama-2-license-is-not-open-source | OSI blog, "July 20, 2023", "OSI opinion", by Stefano Maffulli; title on the page "Meta's LLaMa license is not Open Source". |
| `meta2023llamablog` (new) | Internet Archive snapshot https://web.archive.org/web/20230802205159/https://ai.meta.com/blog/large-language-model-llama-meta-ai/ | The live page returned HTTP 400 to this machine. Dated "February 24, 2023". The snapshot carries a later banner pointing to Llama 2. |
| `meta2023llama2news` (new) | https://about.fb.com/news/2023/07/llama-2/ | Meta Newsroom, "Meta and Microsoft Introduce the Next Generation of Llama", July 18, 2023. |
| `zuckerberg2024open` (new) | https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/ | "Open Source AI is the Path Forward", by Mark Zuckerberg, July 23, 2024 (page also shows January 27, 2025, presumably an update date). Advocacy by an interested party. |
| `mistral2023mistral7b` (new) | https://mistral.ai/news/announcing-mistral-7b | "Mistral 7B", September 27, 2023, by Mistral team. |
| `mistral2023mixtral` (new) | https://mistral.ai/news/mixtral-of-experts | "Mixtral of experts", December 11, 2023, by Mistral team. |
| `google2026gemmaterms` (new) | https://ai.google.dev/gemma/terms and https://ai.google.dev/gemma/apache_2 | "Gemma Terms of Use", "Last modified: April 1, 2026". The page says it is deprecated in favour of gemma.ai (not fetched). Its link "Gemma 4 license" goes to the second URL, which reproduces the Apache License 2.0. |
| `apache2004license` (new) | https://www.apache.org/licenses/LICENSE-2.0.txt | Apache License, Version 2.0, January 2004. |
| `apple2024m4pro` (new) | https://www.apple.com/newsroom/2024/10/apple-introduces-m4-pro-and-m4-max/ | Apple press release, October 30, 2024. Vendor figures. |
| `apple2025m5` (new) | https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/ | Apple press release, October 15, 2025. |
| `apple2026mbpspecs` (new) | https://www.apple.com/macbook-pro/specs/ (redirected to .../liquid-retina-xdr-display/specs/) | Technical specifications as served on 2026-11-11. Changes with each product update. |
| `nvidia2025blackwell` (new) | https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf | "NVIDIA RTX Blackwell GPU Architecture", V1.1; PDF metadata 2025-05-12; 57 pages. Printed page = PDF page. Vendor figures. |
| `nvidia2026rtx5090` (new) | https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ and .../40-series/rtx-4090/ | Product spec pages (memory size and type only; no bandwidth printed). |
| `amd2026ryzen9950x` (new) | https://www.amd.com/en/products/processors/desktops/ryzen/9000-series/amd-ryzen-9-9950x.html | Spec page; launch date 08/15/2024. No bandwidth printed. |

Not fetched:
- The live Meta AI blog pages (ai.meta.com) refused this machine (HTTP 400); the LLaMA announcement was read in the Internet Archive; the Llama 2 announcement was read on Meta's newsroom instead (`meta2023llama2news`). The Llama 3 and Llama 3.1 launch blog posts were not read; the licence files and the paper carry the dates used here.
- The leak of the original LLaMA weights in March 2023, which the reader may have heard of: no primary source was fetched. Do not mention it, or fetch a primary account first.
- The OSI's OSAID 1.0 press release and the earlier draft versions of the definition; the "Checklist" and "Endorsements" pages.
- Heather Meeker's "Open Weights Definition" (2023), named in `osi2025openweights`: not fetched.
- The Gemma Prohibited Use Policy, the Llama 3.1 Acceptable Use Policy (the Llama 3 policy text is inside `meta2024llama3license`), and the DeepSeek-V3 "Model License" text (only the model card's summary was read).
- The Qwen (2023) licence: the 2023 report does not state a licence in the passages read; do not attach one. Qwen3's Apache 2.0 is stated in `yang2025qwen3` p. 1.
- The DeepSeek-V3 technical report (arXiv 2412.19437): sizes come from the Hugging Face model card instead.
- Gemma 4 announcement or model card: only the terms page's link and the Hugging Face API metadata were read (LC10, LC26). What the "E" in "E2B" means was not checked.
- llama.cpp pull requests on k-quants (#1684) and importance matrices (#4861), listed in `llamacpp2026quantize`: not read. The base perplexity behind the "+0.1754 ppl" style figures is therefore unknown (LCD4).
- Intel CPU spec pages (ark) refused this machine (HTTP 403).
- JEDEC DDR5 specification: not fetched; the 64-bit channel width needed to turn "2 channels of DDR5-5600" into a bandwidth is not sourced (LC53).
- Later work arguing that LLM.int8()'s outlier features depend on training choices rather than appearing at a fixed scale: known only as a lead (LCD5).
- Discussions in the llama.cpp repository comparing tokens per second across Apple chips (for example discussion #4167): leads only, not read.

## Sourced claims

### A. What "open" means

### LC1. The OSI's Open Source AI Definition 1.0 (October 2024)
- Source: `osi2024osaid` (published 2024-10-28).
- Quotes: "An Open Source AI is an AI system made available under terms and in a way that grant the freedoms 1 to: Use the system for any purpose and without having to ask for permission. Study how the system works and inspect its components. Modify the system for any purpose, including to change its output. Share the system for others to use with or without modifications, for any purpose." Footnote 1: "These freedoms are derived from the Free Software Definition."
- "A precondition to exercising these freedoms is to have access to the preferred form to make modifications to the system." That form "must include all the elements below": "Data Information: Sufficiently detailed information about the data used to train the system so that a skilled person can build a substantially equivalent system." ... "Code: The complete source code used to train and run the system." ... "Parameters: The model parameters, such as weights or other configuration settings. Parameters shall be made available under OSI-approved terms."
- On weights: "AI weights are the set of learned parameters that overlay the model architecture to produce an output from a given input." "'Open Source models' and 'Open Source weights' must include the data information and code used to derive those parameters."
- Note: Data Information is a description of the data, not necessarily the data itself; the definition allows "unshareable data" to be described rather than released (see LC3, LCD1).

### LC2. The OSI on "open weights"
- Source: `osi2025openweights` (published 2025-01-29).
- Quotes: "Open Weights refer to the final weights and biases of a trained neural network." "When AI developers share these parameters under an OSI Approved License, they empower others to fine-tune, adapt, or deploy the model for their own projects." "However, Open Weights differ significantly from Open Source AI because they do not include: Training code ... Training dataset ... Comprehensive data transparency". "While Open Weights stand out as more transparent than purely proprietary AI, they still lack several key elements of Open Source AI." Limitations listed: "Lack of reproducibility", "Data opacity", "Regulatory hurdles", "Limited community collaboration".
- Note: this is the OSI's own explainer, not part of the definition. Its definition of open weights includes an OSI-approved licence, which most "open-weight" models do not have (LC6 to LC10): in common use the term is looser (LCD1).

### LC3. Which models met the OSAID in the OSI's validation (and which did not)
- Source: `osi2025faq`.
- Quote: "The list of models that passed the Validation phase are: Pythia (Eleuther AI), OLMo (AI2), Amber and CrystalCoder (LLM360), and T5 (Google). A few others that were analyzed would probably pass if they changed their licenses/legal terms, for example, BLOOM (BigScience), Starcoder2 (BigCode), and Falcon (TII). Those that have been analyzed and don't pass because they lack required components and/or their legal agreements are incompatible with the Open Source principles include Llama2 (Meta), Grok (X/Twitter), Phi-2 (Microsoft), and Mixtral (Mistral). These results should be seen as part of the definitional process, a learning moment; they are not certifications of any kind."
- On training data, the FAQ records disagreement: "Some people believe that full, unfettered access to all training data (with no distinction of its kind) is paramount, arguing that anything less would compromise the full reproducibility of AI systems, transparency and security. This approach would relegate Open Source AI to a niche of AI trainable only on open data."
- Note: Mixtral is Apache-2.0 licensed (LC16) yet failed: a permissive weights licence alone does not make a model Open Source AI in the OSI's sense. Pythia and OLMo already have keys (`biderman2023pythia`, `groeneveld2024olmo`) from the `training` chapter.

### LC4. The OSI's objection to calling Llama 2 "open source" (July 2023)
- Source: `maffulli2023llama` (July 20, 2023).
- Quotes: "Unfortunately, the tech giant has created the misunderstanding that LLaMa 2 is "open source" - it is not." "Meta is confusing "open source" with "resources available to some users under some conditions," two very different things." "Meta's license for the LLaMa models and code does not meet this standard; specifically, it puts restrictions on commercial use for some users (paragraph 2) and also restricts the use of the model and software for certain purposes (the Acceptable Use Policy)." (Source prints an en-dash before "it is not".)
- Note: this predates OSAID 1.0 and judges the licence against the older Open Source Definition (for software).

### LC5. Meta's own framing: "open source"
- Sources: `meta2023llama2news`, `zuckerberg2024open`.
- `meta2023llama2news` (July 18, 2023): "Today, we're introducing the availability of Llama 2, the next generation of our open source large language model." "Llama 2 is free for research and commercial use." "We've been blown away by the huge demand for Llama 1 from researchers - with more than 100,000 requests for access to the large language model". "We're including model weights and starting code for the pretrained model and conversational fine-tuned versions too." (Source prints an em-dash before "with more than".)
- `zuckerberg2024open` (July 23, 2024): "We're releasing Llama 3.1 405B, the first frontier-level open source AI model, as well as new and improved Llama 3.1 70B and 8B models." Reasons given for organisations wanting such models: "We need to train, fine-tune, and distill our own models." "We need to control our own destiny and not get locked into a closed vendor." "We need to protect our data. Many organizations handle sensitive data that they need to secure and can't send to closed models over cloud APIs." "Open source addresses these issues by enabling you to run the models wherever you want." "We need a model that is efficient and affordable to run."
- Note: the reasons are useful for the "why run a model yourself" section, but they come from the company releasing the model; attribute them.

### B. Licences

### LC6. Llama 2 Community License (July 2023)
- Source: `meta2023llama2license`.
- Header: "Llama 2 Version Release Date: July 18, 2023".
- Clause 1.b.v: "You will not use the Llama Materials or any output or results of the Llama Materials to improve any other large language model (excluding Llama 2 or derivative works thereof)."
- Clause 2, "Additional Commercial Terms": "If, on the Llama 2 version release date, the monthly active users of the products or services made available by or for Licensee, or Licensee's affiliates, is greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta, which Meta may grant to you in its sole discretion".
- Clause 1.b.iv incorporates the Acceptable Use Policy by reference.

### LC7. Meta Llama 3 Community License (April 2024)
- Source: `meta2024llama3license`.
- Header: "Meta Llama 3 Version Release Date: April 18, 2024". Clause 1.b.i: distributors must "prominently display "Built with Meta Llama 3"" and "If you use the Llama Materials to create, train, fine tune, or otherwise improve an AI model, which is distributed or made available, you shall also include "Llama 3" at the beginning of any such AI model name." Clause 1.b.v: the same "will not use ... to improve any other large language model" restriction as Llama 2. Clause 2: the same 700 million monthly active users threshold.

### LC8. Llama 3.1 Community License (July 2024)
- Source: `meta2024llama31license`.
- Header: "Llama 3.1 Version Release Date: July 23, 2024".
- Grant (1.a): "You are granted a non-exclusive, worldwide, non-transferable and royalty-free limited license under Meta's intellectual property or other rights owned by Meta embodied in the Llama Materials to use, reproduce, distribute, copy, create derivative works of, and make modifications to the Llama Materials."
- 1.b.i: display "Built with Llama"; "If you use the Llama Materials or any outputs or results of the Llama Materials to create, train, fine tune, or otherwise improve an AI model, which is distributed or made available, you shall also include "Llama" at the beginning of any such AI model name."
- Clause 2: "If, on the Llama 3.1 version release date, the monthly active users of the products or services made available by or for Licensee, or Licensee's affiliates, is greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta, which Meta may grant to you in its sole discretion, and you are not authorized to exercise any of the rights under this Agreement unless or until Meta otherwise expressly grants you such rights."
- Note (checked by searching the file): the Llama 3.1 licence has no clause forbidding use of outputs to improve other models; that clause (1.b.v) is in the Llama 2 and Llama 3 licences only. 3.1 instead requires the "Llama" name prefix. The 700M test is measured on the version release date.

### LC9. Apache 2.0 and the models released under it
- Sources: `apache2004license`, `mistral2023mistral7b`, `jiang2023mistral`, `jiang2024mixtral`, `yang2025qwen3`, `huggingface2026api`.
- Apache 2.0, section 2: "each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form."
- Mistral 7B blog: "We're releasing Mistral 7B under the Apache 2.0 license, it can be used without restrictions." Paper p. 1: "Our models are released under the Apache 2.0 license."
- Mixtral paper p. 1: "Both the base and instruct models are released under the Apache 2.0 license." p. 2: "free for academic and commercial usage".
- Qwen3 report p. 1: "all Qwen3 models are publicly accessible under Apache 2.0."
- Hugging Face metadata (2026-11-11): licence `apache-2.0` for mistralai/Mistral-7B-v0.1, mistralai/Mixtral-8x7B-v0.1, Qwen/Qwen3-8B, Qwen/Qwen3-0.6B, Qwen/Qwen2.5-7B-Instruct, google/gemma-4-E2B-it.
- Note: Apache 2.0 is an OSI-approved software licence; it says nothing about training data (LC3: Mixtral failed the OSAID validation).

### LC10. Gemma Terms of Use; Gemma 4 under Apache 2.0 (as of 2026-11)
- Source: `google2026gemmaterms` ("Last modified: April 1, 2026").
- Scope line: "The terms below apply to Gemma models listed in the Appendix at bottom of this page. For Gemma 4 terms, see the Gemma 4 license." The Appendix lists Gemma 1, 1.1, 2, 3, 3n and variants. The "Gemma 4 license" link opens a page reproducing the Apache License 2.0; Hugging Face lists google/gemma-4-E2B-it as `apache-2.0` (LC26).
- 3.1: redistributors "must include the use restrictions referenced in Section 3.2 as an enforceable provision in any agreement ... governing the use and/or distribution of Gemma or Model Derivatives". 3.2: "You must not use any of the Gemma Services: for the restricted uses set forth in the Gemma Prohibited Use Policy ... or in violation of applicable laws and regulations. To the maximum extent permitted by law, Google reserves the right to restrict (remotely or otherwise) usage of any of the Gemma Services that Google reasonably believes are in violation of this Agreement." 3.3: "Google claims no rights in Outputs you generate using Gemma."
- Note: the 2024 Gemma paper calls the models "open models" (LC18); the terms are custom, with use restrictions. Say "as of 2026-11" for Gemma 4.

### LC11. DeepSeek's licences
- Source: `huggingface2026api` (model cards of deepseek-ai/DeepSeek-R1, revision 56d4cbbb4d29, and deepseek-ai/DeepSeek-V3, revision e815299b0bcb).
- DeepSeek-R1 card, section 7: "This code repository and the model weights are licensed under the MIT License. DeepSeek-R1 series support commercial use, allow for any modifications and derivative works, including, but not limited to, distillation for training other LLMs." The distilled Qwen-based models "are derived from Qwen-2.5 series, which are originally licensed under Apache 2.0 License"; "DeepSeek-R1-Distill-Llama-8B is derived from Llama3.1-8B-Base and is originally licensed under llama3.1 license." and "DeepSeek-R1-Distill-Llama-70B is derived from Llama3.3-70B-Instruct and is originally licensed under llama3.3 license."
- Note: a distilled model inherits obligations from its base model's licence; a reader choosing a "DeepSeek" small model may in fact be bound by Meta's or Alibaba's terms.
- DeepSeek-V3 card, section 7: "This code repository is licensed under the MIT License. The use of DeepSeek-V3 Base/Chat models is subject to the Model License. DeepSeek-V3 series (including Base and Chat) supports commercial use."

### LC12. Gated downloads on Hugging Face
- Sources: `huggingface2026gated`, `huggingface2026api`.
- Quote: "the Hub allows model authors to enable access requests for their models. When enabled, users must submit an access request to access the model files, which shares their Hugging Face information (username and email address) with the model authors unless the authors opted out of collecting it." "A model with access requests enabled is called a gated model."
- API (2026-11-11): `gated: manual` for meta-llama/Llama-3.1-8B, -8B-Instruct, -70B, -405B, Llama-3.2-1B, -3B, google/gemma-3-4b-it, google/gemma-2b; `gated: False` for the Mistral, Qwen, Gemma 4, DeepSeek-R1, and Phi-3 repositories listed in LC26.

### C. The open-weight lineage

### LC13. LLaMA (February 2023): research-only weights by request
- Sources: `meta2023llamablog`, `touvron2023llama`, `meta2023llamav1`.
- Blog (February 24, 2023): "As part of Meta's commitment to open science, today we are publicly releasing LLaMA (Large Language Model Meta AI), a state-of-the-art foundational large language model designed to help researchers advance their work in this subfield of AI. Smaller, more performant models such as LLaMA enable others in the research community who don't have access to large amounts of infrastructure to study these models". "We are making LLaMA available at several sizes (7B, 13B, 33B, and 65B parameters)". "To maintain integrity and prevent misuse, we are releasing our model under a noncommercial license focused on research use cases. Access to the model will be granted on a case-by-case basis to academic researchers; those affiliated with organizations in government, civil society, and academia; and industry research laboratories around the world."
- Paper p. 1: "We release all our models to the research community." p. 1: "We believe that this model will help democratize the access and study of LLMs, since it can be run on a single GPU." p. 10: "some of the models are relatively small and can be run on a single GPU."
- Repository (`llama_v1` branch): README: "In order to download the checkpoints and tokenizer, fill this google form"; "Once your request is approved, you will receive links to download". MODEL_CARD.md: "License: Non-commercial bespoke license"; "LLaMA was trained between December. 2022 and Feb. 2023." The code's LICENSE file is the GNU GPL v3.
- Note: so "open" in February 2023 meant: inference code under GPL, weights by application for non-commercial research.

### LC14. Llama 2 (July 2023): weights for commercial use too
- Sources: `meta2023llama2news` (LC5), `touvron2023llama2`, `meta2023llama2license` (LC6).
- Paper p. 4: "We are releasing the following models to the general public for research and commercial use". p. 35: "We make Llama 2 available for both research and commercial use ... Those who use Llama 2 must comply with the terms of the provided license and our Acceptable Use Policy". p. 7 (already used in `scale`): "the pretraining costs do not need to be incurred by others".
- Earlier public releases, p. 3: "There have been public releases of pretrained LLMs (such as BLOOM (Scao et al., 2022), LLaMa-1 (Touvron et al., 2023), and Falcon (Penedo et al., 2023)) that match the performance of closed pretrained competitors like GPT-3 ... and Chinchilla ..., but none of these models are suitable substitutes for closed "product" LLMs, such as ChatGPT, BARD, and Claude."
- Note: the open-weight story does not start in 2023. GPT-2's full weights (November 2019, `openai2019release`) and BLOOM (2022, `lescao2022bloom`) are already in the book.

### LC15. Mistral 7B (September 2023)
- Sources: `mistral2023mistral7b`, `jiang2023mistral`.
- Blog (September 27, 2023): "Mistral 7B is a 7.3B parameter model that: Outperforms Llama 2 13B on all benchmarks; Outperforms Llama 1 34B on many benchmarks". Licence: LC9.
- Paper p. 1: "Mistral 7B outperforms the best open 13B model (Llama 2) across all evaluated benchmarks, and the best released 34B model (Llama 1) in reasoning, mathematics, and code generation." Uses grouped-query attention and sliding-window attention. Table 1 (p. 2): dim 4096, n_layers 32, head_dim 128, n_heads 32, n_kv_heads 8, window_size 4096, context_len 8192, vocab_size 32000.
- Knowledge limit (p. 4): "On the Knowledge benchmarks, Mistral 7B's performance achieves a lower compression rate of 1.9x, which is likely due to its limited parameter count that restricts the amount of knowledge it can store." Fig. 5 caption (p. 5): "Mistral 7B largely outperforms Llama 2 13B on all evaluations, except on knowledge benchmarks, where it is on par (this is likely due to its limited parameter count, which limits the amount of knowledge it can compress)."
- Note: "compression rate" here is Mistral's term for "equivalent Llama 2 size divided by 7B" (p. 4: on reasoning it "mirrored performance that one might expect from a Llama 2 model with more than 3x its size"). The paper's own reading, a hypothesis ("likely").

### LC16. Mixtral 8x7B (December 2023): a mixture of experts with open weights
- Sources: `mistral2023mixtral`, `jiang2024mixtral`.
- Blog (December 11, 2023): "Mixtral 8x7B, a high-quality sparse mixture of experts model (SMoE) with open weights. Licensed under Apache 2.0." "Concretely, Mixtral has 46.7B total parameters but only uses 12.9B parameters per token. It, therefore, processes input and generates output at the same speed and for the same cost as a 12.9B model."
- Paper p. 1: "each token has access to 47B parameters, but only uses 13B active parameters during inference." p. 4: "The memory costs for serving Mixtral are proportional to its sparse parameter count, 47B, which is still smaller than Llama 2 70B." Also p. 4: the routing adds overhead; SMoEs "are more suitable for batched workloads".
- Note: for local use this is the key point: memory scales with total parameters, per-token reading (and so speed at batch size 1) with active parameters. The blog's "same speed ... as a 12.9B model" is the vendor's simplification; the paper itself qualifies it. Mixture-of-experts is explained in `since-2017`; here only its memory/speed consequence.

### LC17. Qwen (September 2023) and Qwen3 (2025)
- Sources: `bai2023qwen`, `yang2025qwen3`.
- Qwen report p. 3: "we are pleased to present and release the initial version of our LLM series, QWEN." Table 1 (p. 7): sizes 1.8B, 7B, 14B, trained on 2.2T, 2.4T, 3.0T tokens. p. 9: "despite having a relatively small number of parameters, QWEN-1.8B is capable of competitive performance on certain tasks and even outperforms larger models in some instances."
- Qwen3 p. 2: "Qwen3 is a collection of open-weight large language models". p. 3: "The Qwen3 series includes 6 dense models, namely Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B, Qwen3-8B, Qwen3-14B, and Qwen3-32B, and 2 MoE models, Qwen3-30B-A3B and Qwen3-235B-A22B. The flagship model, Qwen3-235B-A22B, has a total of 235B parameters with 22B activated ones." Table 1 (p. 3): context length 32K for 0.6B and 1.7B, 128K for 4B and above. Licence: LC9.

### LC18. Gemma (February 2024) and Gemma 3 (March 2025)
- Sources: `gemmateam2024gemma`, `gemmateam2025gemma3`.
- Gemma p. 1: "Gemma, a family of lightweight, state-of-the art open models built from the research and technology used to create Gemini models." "We release two sizes of models (2 billion and 7 billion parameters), and provide both pretrained and fine-tuned checkpoints." "Gemma comes in two sizes: a 7 billion parameter model for efficient deployment and development on GPU and TPU, and a 2 billion parameter model for CPU and on-device applications." p. 3: trained on 3T and 6T tokens.
- Gemma 3 p. 1: "a multimodal addition to the Gemma family of lightweight open models, ranging in scale from 1 to 27 billion parameters." "These models are designed to run on standard consumer-grade hardware such as phones, laptops, and high-end GPUs." "We also change the architecture of the model to reduce the KV-cache memory that tends to explode with long context." p. 2: "Gemma 3 models support context length of 128K tokens, with the exception of the 1B model that has 32K." Quantized checkpoints: LC39.

### LC19. DeepSeek (2024-2025), and distilled small models
- Sources: `deepseekai2024llm`, `deepseekai2025r1`, `huggingface2026api`.
- DeepSeek LLM p. 1: "we introduce DeepSeek LLM, a project dedicated to advancing open-source language models with a long-term perspective", in "two prevalent used opensource configurations, 7B and 67B" (source text as extracted).
- DeepSeek-R1, arXiv v1 (the version the existing key `deepseekai2025r1` records; pages are PDF pages): abstract (p. 1): "To support the research community, we open-source DeepSeek-R1-Zero, DeepSeek-R1, and six dense models (1.5B, 7B, 8B, 14B, 32B, 70B) distilled from DeepSeek-R1 based on Qwen and Llama." p. 11: "The base models we use here are Qwen2.5-Math-1.5B, Qwen2.5-Math-7B, Qwen2.5-14B, Qwen2.5-32B, Llama-3.1-8B, and Llama-3.3-70B-Instruct." "For distilled models, we apply only SFT and do not include an RL stage". p. 16: "DeepSeek-R1-Distill-Qwen-1.5B outperforms GPT-4o and Claude-3.5-Sonnet on math benchmarks with 28.9% on AIME and 83.9% on MATH."
- The same claims were first read in v2 (4 January 2026) at different pages: v2 p. 2 ("we have distilled several smaller models and made them publicly available"), Table 6 p. 35 (base models), p. 61 (the 1.5B math result). Cite v1 pages with the existing key.
- DeepSeek-V3 card: "671B total parameters with 37B activated for each token"; "The total size of DeepSeek-V3 models on HuggingFace is 685B, which includes 671B of the Main Model weights and 14B of the Multi-Token Prediction (MTP) Module weights."
- Note: distillation itself belongs to `adapting`; here only "small models made from a large one". The 1.5B math claim is narrow (two math benchmarks, against GPT-4o and Claude 3.5 Sonnet, v1 p. 16; v2 p. 61 calls them "non-reasoning baselines"); do not generalise it.

### LC20. Llama 3 and 3.1 (2024): sizes, release, architecture
- Source: `grattafiori2024llama`.
- p. 2: "We are publicly releasing all three Llama 3 models under an updated version of the Llama 3 Community License". Table 3 (p. 7): 8B: 32 layers, model dimension 4,096, FFN 14,336, 32 attention heads, 8 key/value heads; 70B: 80, 8,192, 28,672, 64, 8; 405B: 126, 16,384, 53,248, 128, 8; vocabulary 128,000.
- p. 51: "When using a BF16 number representation for the model parameters, Llama 3 405B does not fit in the GPU memory of a single machine with 8 Nvidia H100 GPUs." See LC41.

### LC21. Llama 3.2 (October 2024): 1B and 3B for devices
- Source: `meta2024llama32card`.
- "Model Release Date: Oct 24, 2024". Table: "1B (1.23B)", "3B (3.21B)", context length 128k; "Llama 3.2 Quantized (text only)" rows: same sizes, context length 8k. "Llama 3.2 1B and 3B models are expected to be deployed in highly constrained environments, such as mobile devices." "quantized models can be adapted for a variety of on-device use-cases with limited compute resources." Quantization details: LC40.

### LC22. Phi-3-mini (April 2024): "locally on your phone"
- Source: `abdin2024phi3`.
- Title: "Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone". Abstract: "phi-3-mini, a 3.8 billion parameter language model trained on 3.3 trillion tokens".
- p. 3: "Thanks to its small size, phi3-mini can be quantized to 4-bits so that it only occupies ≈ 1.8GB of memory. We tested the quantized model by deploying phi-3-mini on iPhone 14 with A16 Bionic chip running natively on-device and fully offline achieving more than 12 tokens per second."
- Weakness: LC59.

### D. Hugging Face and model cards

### LC23. The Hugging Face Hub (as of 2026-11)
- Source: `huggingface2026hub`.
- index.md (commit of 2026-11-06): "The Hugging Face Hub is the reference AI platform for open ML. It hosts over 3M models, 1M datasets, and 2M AI apps (Spaces), all open and publicly available."
- models-the-hub.md: "The Model Hub is where the members of the Hugging Face community can host all of their model checkpoints for simple storage, discovery, and sharing."
- Note: the count is Hugging Face's own, self-description ("the reference AI platform") included; say "Hugging Face says it hosts over three million models (as of 2026-11)". "All open and publicly available" sits awkwardly with gated models (LC12) and private repositories; do not repeat it.

### LC24. Model cards on the Hub
- Source: `huggingface2026modelcards`.
- "Model cards are files that accompany the models and provide handy information. Under the hood, model cards are simple Markdown files with additional metadata." "You can find a model card as the README.md file in any model repo." The card "should describe: the model; its intended uses & potential limitations, including biases and ethical considerations as detailed in Mitchell, 2018; the training params and experimental info ...; which datasets were used to train your model; the model's evaluation results". The YAML metadata supports filtering and "Displaying the model's license".

### LC25. Mitchell et al. (2019): the model card proposal
- Source: `mitchell2019model`.
- Abstract (p. 1): "we propose a framework that we call model cards, to encourage such transparent model reporting. Model cards are short documents accompanying trained machine learning models that provide benchmarked evaluation in a variety of conditions, such as across different cultural, demographic, or phenotypic groups ... Model cards also disclose the context in which models are intended to be used, details of the performance evaluation procedures, and other relevant information."
- Fig. 1 (p. 3) lists sections: Model Details ("Person or organization developing model - Model date - Model version - Model type - ... - Paper or other resource for more information - Citation details - License - ..."), Intended Use, Factors, Metrics, Evaluation Data, Training Data, Quantitative Analyses, Ethical Considerations, Caveats and Recommendations.
- Note: the original LLaMA model card (LC13) uses these exact headings ("Model date", "Model version", "Model type", "Paper or resources for more information", "License", "Primary intended uses", "Out-of-scope use cases"): a concrete example for the reader.

### LC26. Exact parameter counts and metadata from the Hub (read 2026-11-11)
- Source: `huggingface2026api` (field `safetensors.total`, licence from `cardData`, `gated`, `createdAt`, revision `sha`).

| Repository | Parameters | Stored as | Licence | Gated | Revision |
|---|---:|---|---|---|---|
| meta-llama/Llama-3.2-1B | 1,235,814,400 | BF16 | llama3.2 | manual | 4e20de362430 |
| meta-llama/Llama-3.2-3B | 3,212,749,824 | BF16 | llama3.2 | manual | 13afe5124825 |
| microsoft/Phi-3-mini-4k-instruct | 3,821,079,552 | BF16 | mit | no | f39ac1d28e92 |
| google/gemma-3-4b-it | 4,300,079,472 | BF16 | gemma | manual | 093f9f388b31 |
| google/gemma-4-E2B-it | 5,123,178,051 | BF16 | apache-2.0 | no | 4adf15748de9 |
| mistralai/Mistral-7B-v0.1 | 7,241,732,096 | BF16 | apache-2.0 | no | 27d67f1b5f57 |
| Qwen/Qwen2.5-7B-Instruct | 7,615,616,512 | BF16 | apache-2.0 | no | a09a35458c70 |
| meta-llama/Llama-3.1-8B | 8,030,261,248 | BF16 | llama3.1 | manual | d04e592bb4f6 |
| Qwen/Qwen3-8B | 8,190,735,360 | BF16 | apache-2.0 | no | b968826d9c46 |
| mistralai/Mixtral-8x7B-v0.1 | 46,702,792,704 | BF16 | apache-2.0 | no | fc7ac94680e3 |
| meta-llama/Llama-3.1-70B | 70,553,706,496 | BF16 | llama3.1 | manual | 349b2ddb53ce |
| meta-llama/Llama-3.1-405B | 405,853,388,800 | BF16 | llama3.1 | manual | b906e4dc842a |
| deepseek-ai/DeepSeek-R1 | 684,489,845,504 | mostly F8_E4M3 (680.6B), some BF16 | mit | no | 56d4cbbb4d29 |

- Also: Qwen/Qwen3-0.6B 751,632,384 (apache-2.0); meta-llama/Llama-3.1-8B-Instruct 8,030,261,248 (same count as the base model).
- Configs: Qwen3-8B: 36 layers, 32 query heads, 8 key/value heads, head dimension 128. Mistral-7B-v0.1: 32 layers, 32 heads, 8 key/value heads, hidden 4096 (head dimension 128), `max_position_embeddings` 32768. Phi-3-mini-4k-instruct: 32 layers, hidden 3072, 32 heads, 32 key/value heads (no grouping; head dimension 96), `max_position_embeddings` 4096.
- Note: the "8B" Llama is 8.03 billion; the "7B" Mistral is 7.24 billion (the blog says 7.3B). Names round. DeepSeek-R1's count includes the 14B MTP module (LC19). Gemma 4 "E2B" has 5.1 billion stored parameters: do not explain the "E" without a source.

### E. Reading a model's name

### LC27. The GGUF naming convention
- Source: `ggml2026gguf`.
- "GGUF follow a naming convention of `[<Sidecar>]<BaseName><SizeLabel><FineTune><Version><Encoding><Type><Shard>.gguf` where each component is delimitated by a `-` if present. Ultimately this is intended to make it easier for humans to at a glance get the most important details of a model. It is not intended to be perfectly parsable in the field due to the diversity of existing gguf filenames."
- SizeLabel: "Parameter weight class (useful for leader boards) represented as `<expertCount>x<count><scale-prefix>`", with B for billion, M for million. FineTune: "A descriptive name for the model fine tuning goal (e.g. Chat, Instruct, etc...)". Encoding: "Indicates the weights encoding scheme that was applied to the model." Shard: "`<ShardNum>-of-<ShardTotal>`".
- Worked example in the spec: "`Mixtral-8x7B-v0.1-KQ2.gguf`: Model Name: Mixtral, Expert Count: 8, Parameter Count: 7B, Version Number: v0.1, Weight Encoding Scheme: KQ2". Another: `Phi-3-mini-3.8B-ContextLength4k-instruct-v1.0.gguf` parses to SizeLabel "3.8B-ContextLength4k", FineTune "instruct".
- Note: the Book 1 chapter can show names as text without being code [D-003]: e.g. "Llama-3.1-8B-Instruct-Q4_K_M". Keep them in running text or a table, not a code block.

### LC28. Base and instruct, size and active size in names
- Sources: `huggingface2026api`, `meta2023llamav1`, `grattafiori2024llama`, `yang2025qwen3`, `huggingface2026api` (Phi-3 card).
- The Hub carries both meta-llama/Llama-3.1-8B and meta-llama/Llama-3.1-8B-Instruct (same parameter count, LC26). Llama 3 paper p. 1: "pre-trained and post-trained versions of the 405B parameter language model". Gemma p. 1: "pretrained and fine-tuned checkpoints".
- LLaMA model card, "Out-of-scope use cases": "LLaMA is a base, or foundational, model. As such, it should not be used on downstream applications without further risk evaluation and mitigation. In particular, our model has not been trained with human feedback, and can thus generate toxic or offensive content, incorrect information or generally unhelpful answers."
- Active parameters in names: Qwen3-235B-A22B "has a total of 235B parameters with 22B activated ones" (Qwen3 p. 3).
- Context length in names: the Phi-3-mini card: "The model belongs to the Phi-3 family with the Mini version in two variants 4K and 128K which is the context length (in tokens) that it can support."
- Note: "8x7B" is not 56B. Mixtral has 46.7B parameters; 8 x 7.24 = 57.9 (computed) overstates its memory. The reason is in `jiang2024mixtral` p. 1: "Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts)", and p. 2: "the feedforward blocks are replaced by Mixture-of-Expert layers", so only the feed-forward part is multiplied by eight. A good warning example; the mechanism belongs to `since-2017`, here only "the name misleads".

### LC29. Context length in the card is not a fixed property of a name
- Sources: `meta2024llama32card`, `gemmateam2025gemma3`, `jiang2023mistral`, `huggingface2026api`.
- Llama 3.2 1B/3B: context length 128k; the quantized releases of the same sizes: 8k (LC21). Gemma 3: 128K, except 1B at 32K. Mistral 7B: paper Table 1 "context_len 8192"; Hugging Face config `max_position_embeddings` 32768 (LCD7).
- Note: the useful reader lesson: read the card, not the name.

### F. Quantization

### LC30. llama.cpp's own definition of quantization and how loss is measured (as of 2026-11)
- Source: `llamacpp2026quantize` (README).
- "This tool takes a GGUF input model file, typically in a high-precision format like F32 or BF16, and converts it to a quantized format. Quantization reduces the precision of model weights (e.g., from 32-bit floats to 4-bit integers), which shrinks the model's size and can speed up inference. This process however, may introduce some accuracy loss which is usually measured in Perplexity (ppl) and/or Kullback-Leibler Divergence (kld). This can be minimized by using a suitable imatrix file." (Source prints an en-dash in "Kullback-Leibler".)
- "--allow-requantize allow requantizing tensors that have already been quantized. Warning: This can severely reduce quality compared to quantizing from 16bit or 32bit".
- Note: "imatrix" (importance matrix) is calibration data that weights the rounding by how much each weight matters; the same idea as AWQ's (LC38). Mention only by idea. Perplexity is defined in `prediction`; KL divergence would need a definition if used (it can be skipped).

### LC31. Bits per weight, size, and speed by quantization type for Llama 3.1 8B
- Source: `llamacpp2026quantize` (README, table headed "meta-llama/Llama-3.1-8B").
- Selected rows (bits/weight; size in GiB; text generation t/s @ 128):
  - F16: 16.0005; 14.96; 29.17 ± 0.04
  - Q8_0: 8.5008; 7.95; 50.93 ± 0.08
  - Q6_K: 6.5633; 6.14; 58.67 ± 3.13
  - Q5_K_M: 5.7036; 5.33; 67.23 ± 1.08
  - Q4_K_M: 4.8944; 4.58; 71.93 ± 1.52
  - Q4_K_S: 4.6672; 4.36; 76.71 ± 0.20
  - Q3_K_M: 3.9960; 3.74; 71.68 ± 0.22
  - Q2_K: 3.1593; 2.95; 79.85 ± 0.20
  - IQ1_S: 2.0042; 1.87; 79.73 ± 0.79
- The table also gives "prompt processing t/s @ 512" (e.g. F16 923.49, Q4_K_M 821.81).
- Note: the README does not say what hardware produced the speeds (LCD4). Use the bits/weight and sizes; use the speeds only as a relative pattern (LCM 6). Sizes are GiB (2^30 bytes); the book uses GB = 10^9 bytes (`destination`).

### LC32. Perplexity cost by type, per llama.cpp's tool (as of 2026-11)
- Source: `llamacpp2026quantize` (`quantize.cpp`, list `QUANT_OPTIONS`).
- Entries: "Q8_0 ... 7.96G, +0.0026 ppl @ Llama-3-8B"; "Q6_K ... 6.14G, +0.0217 ppl @ Llama-3-8B"; "Q5_K_M ... 5.33G, +0.0569 ppl @ Llama-3-8B"; "Q4_K_M ... 4.58G, +0.1754 ppl @ Llama-3-8B"; "Q4_K_S ... 4.37G, +0.2689 ppl"; "Q4_0 ... 4.34G, +0.4685 ppl"; "Q3_K_M ... 3.74G, +0.6569 ppl"; "Q3_K_S ... 3.41G, +1.6321 ppl"; "Q2_K ... 2.96G, +3.5199 ppl @ Llama-3-8B"; "F16 ... 14.00G, +0.0020 ppl @ Mistral-7B"; "BF16 ... 14.00G, -0.0050 ppl @ Mistral-7B"; "F32 ... 26.00G @ 7B".
- Note: these are increases in perplexity over an unstated baseline, on an unstated text, for Llama 3 8B (not 3.1). Usable as "llama.cpp's own tool lists ..." with the pattern: tiny at 8 and 6 bits, small at 5 and 4, growing fast below 4. Do not convert to percentages without the base (LCD4).

### LC33. What a quantized block holds (llama.cpp's block layouts)
- Source: `ggml2026quanttypes` (`ggml-common.h`).
- Q4_0: `#define QK4_0 32`; struct `block_q4_0` = `ggml_half d; // delta` plus `uint8_t qs[QK4_0 / 2]; // nibbles / quants`: 32 weights stored as 4-bit numbers plus one 16-bit scale.
- Q8_0: `block_q8_0` = one 16-bit scale `d` plus `int8_t qs[QK8_0]` (32 eight-bit numbers).
- K-quants: `#define QK_K 256` (a super-block of 256 weights). Comments: Q4_K "8 blocks of 32 elements each // weight is represented as x = a * q + b // Effectively 4.5 bits per weight"; Q6_K "weight is represented as x = a * q // 16 blocks of 16 elements each // Effectively 6.5625 bits per weight"; Q2_K "Effectively 2.625 bits per weight"; Q3_K "Effectively 3.4375"; Q5_K "Effectively 5.5". Q4_K stores its per-block "scales and mins, quantized with 6 bits" and two 16-bit super-block scales.
- Note: this is the "group-wise scale" idea in its plainest form: each group of 32 shares one scale, which costs 16/32 = 0.5 extra bits per weight. Computed checks in LCM 2.

### LC34. Why Q4_K_M is 4.89 bits, not 4.5: a mix of types
- Source: `ggml2026quanttypes` (`src/llama-quant.cpp`).
- For `LLAMA_FTYPE_MOSTLY_Q4_K_M` the default type is `GGML_TYPE_Q4_K`; the output tensor (and tied token embeddings) is raised to `GGML_TYPE_Q6_K`; the attention value tensors and the feed-forward "down" tensors get `GGML_TYPE_Q6_K` on layers where `use_more_bits` is true, defined as `i_layer < n_layers/8 || i_layer >= 7*n_layers/8 || (i_layer - n_layers/8)%3 == 2` (the first and last eighth of layers and every third layer between).
- README Q4_K_S row 4.6672 vs Q4_K_M 4.8944 bits/weight (LC31).
- Note: say "the M variant keeps a few sensitive tensors at 6 bits"; the exact rule is too detailed for Book 1. Book 2 [D-007] can show it.

### LC35. Memory for Llama 3.1 at Q4_K_M, per llama.cpp
- Source: `llamacpp2026quantize` (README, "Memory/Disk Requirements").
- "As the models are currently fully loaded into memory, you will need adequate disk space to save them and sufficient RAM to load them. At the moment, memory and disk requirements are the same. For example (Llama 3.1):" 8B: original 32.1 GB, Q4_K_M 4.9 GB; 70B: 280.9 GB, 43.1 GB; 405B: 1,625.1 GB, 249.1 GB.
- Note: "original size" here is 32-bit (8.03B x 4 bytes = 32.1 GB, computed); the 70B and 405B rows do not exactly match 4 bytes x the Hub's counts (LCD3). The "memory = disk" statement counts weights only, not the KV cache.

### LC36. LLM.int8() (2022): 8 bits without loss, and outlier features
- Source: `dettmers2022llmint8`.
- Abstract (p. 1): "We develop a procedure for Int8 matrix multiplication for feed-forward and attention projection layers in transformers, which cut the memory needed for inference by half while retaining full precision performance. With our method, a 175B parameter 16/32-bit checkpoint can be loaded, converted to Int8, and used immediately without performance degradation." "...for the emergent outliers, we also include a new mixed-precision decomposition scheme, which isolates the outlier feature dimensions into a 16-bit matrix multiplication while still more than 99.9% of values are multiplied in 8-bit." "...making it possible to use OPT-175B/BLOOM on a single server with consumer GPUs."
- The rounding rule (p. 3): "Absmax quantization scales inputs into the 8-bit range [-127, 127] by multiplying with s_xf16 which is 127 divided by the absolute maximum of the entire tensor."
- Outliers (p. 2): "large features with magnitudes up to 20x larger than in other dimensions first appear in about 25% of all transformer layers and then gradually spread to other layers as we scale transformers to 6B parameters. At around 6.7B parameters, a phase shift occurs, and all transformer layers and 75% of all sequence dimensions are affected by extreme magnitude features. These outliers are highly systematic: at the 6.7B scale, 150,000 outliers occur per sequence, but they are concentrated in only 6 feature dimensions across the entire transformer." p. 4: "the small number of large magnitude feature dimensions (≈0.1%) are represented in 16-bit precision while the other 99.9% of values are multiplied in 8-bit." p. 17: "the outlier magnitude is 3-20x larger than the largest magnitude of other feature dimensions".
- Speed (p. 18): "Overall Int8 inference is slightly slower but close to the millisecond latency per token compared to 16-bit inference." GPTQ p. 8 agrees: LLM.int8() "reduces memory costs but has the same runtime as the FP16 baseline".
- Note: the outliers are in activations (the hidden states), not in the weights. Measured on OPT models (LCD5). The reader-level point: one huge number in a group forces a coarse scale on all the others; keeping the few big ones in higher precision rescues the rest.

### LC37. GPTQ (2022-2023): 3-4 bits for 175B models in hours; small models suffer more
- Source: `frantar2023gptq`.
- Abstract (p. 1): "GPTQ can quantize GPT models with 175 billion parameters in approximately four GPU hours, reducing the bitwidth down to 3 or 4 bits per weight, with negligible accuracy degradation relative to the uncompressed baseline ... allowing us for the first time to execute an 175 billion-parameter model inside a single GPU for generative inference." p. 1: "the parameters of GPT3-175B occupy 326GB (counting in multiples of 1024) of memory when stored in a compact float16 format."
- Baseline (p. 2): "only basic variants of round-to-nearest quantization ... have been applied at the scale of GPT-175B; while this works well for low compression targets, e.g., 8-bit weights, they fail to preserve accuracy at higher rates."
- Size dependence (p. 7): "One interesting trend ... is that larger models generally (with the exception of OPT-66B) appear easier to quantize." Table 3 (OPT, WikiText2 perplexity): 125M full 27.65, 4-bit RTN 37.28, 4-bit GPTQ 31.12; 175B full 8.34, RTN 10.54, GPTQ 8.37; at 3 bits RTN on 175B gives 7.3e3. Table 4 (BLOOM): 560M full 22.42, 4-bit GPTQ 24.03; 176B full 8.11, 4-bit GPTQ 8.21.
- Groups (p. 7): "group-size 1024 (≈ 0.02 extra bits) improves perplexities by about 0.2 on average and group-size 128 (≈ 0.15 extra bits) by another 0.1".
- Fit (p. 8): 3-bit OPT-175B "takes approximately 63GB of memory, including the embeddings and the output layer, which are kept in full FP16 precision. Additionally, storing the complete history of keys and values for all layers ... consumes another ≈ 9GB for the maximum of 2048 tokens. Hence, we can actually fit the entire quantized model into a single 80GB A100 GPU".
- Speed (p. 8): "For language generation, the model processes and outputs one token at-a-time ... compute is dominated by matrix-vector products. Unlike matrix-matrix products, these are primarily limited by memory bandwidth." Table 6: per-token latency, batch size 1: A100 80GB, FP16 230 ms (5 GPUs) vs 3-bit 71 ms (1 GPU), 3.24x; A6000 48GB, 589 ms (8 GPUs) vs 130 ms (2 GPUs), 4.53x. "More accessible GPUs, such as the NVIDIA A6000, have much lower memory bandwidth, so this strategy is even more effective".
- Note: GPTQ rounds weights one at a time and adjusts the not-yet-rounded weights to compensate, using a small calibration set (the "approximate second-order information" of p. 1). Book 1 can say that much in words, no derivation [D-002].

### LC38. AWQ (2023-2024): protect the weights that see big activations
- Source: `lin2024awq`.
- p. 2: "Our method is based on the observation that weights are not equally important for LLMs' performance. There is a small fraction (0.1%-1%) of salient weights; skipping the quantization of these salient weights will significantly reduce the quantization loss (Table 1). To find the salient weight channels, the insight is that we should refer to the activation distribution instead of the weight distribution". Fig. 2 (p. 3): on OPT-6.7B at INT3, round-to-nearest PPL 43.2; keeping 1% salient weights in FP16, PPL 13.0; AWQ's scaling, PPL 13.0. p. 7: "We used a group size of 128 throughout the work".
- Why weight-only (p. 2): it "not only reduces the hardware barrier (requiring a smaller memory size) but also speeds up the token generation (remedies memory-bound workload)." p. 6: "The 4090 GPU has a peak computation throughput of 165 TFLOPS and a memory bandwidth of 1TB/s. Therefore, any workload with arithmetic intensity (the ratio of FLOPs to memory access) less than 165 is memory bounded on 4090 GPUs. Notably, when executed in FP16, the generation stage for on-device LLMs has arithmetic intensity≈1." Fig. 3 (p. 5), Llama-2-7B on RTX 4090: context stage, 200 tokens, 10 ms; generation, 20 tokens, 310 ms; "W4A16 quantization can effectively improve the arithmetic intensity by 4x."
- Motivation (p. 1): "running LLMs locally on edge devices can reduce the cloud computing cost and protect users' privacy." "On-device usage eliminates delays caused by sending data to a cloud server and enables LLMs to operate offline". p. 11: "TinyChat even democratizes LLM deployment on extremely resource-constrained Raspberry Pi 4B, achieving 0.7 tokens/s for 7B models."

### LC39. Gemma 3's published memory table and quantization-aware training
- Source: `gemmateam2025gemma3`, p. 3.
- "we also provide quantized versions of our models in different standard formats. These versions are obtained by finetuning each model for a small number of steps, typically 5,000, using Quantization Aware Training (QAT)". "Based on the most popular open source quantization inference engines (e.g. llama.cpp), we focus on three weight representations: per-channel int4, per-block int4, and switched fp8."
- Table 3, "Memory footprints (in GB) comparison between raw (bfloat16) and quantized checkpoints for weights and KV caching (+KV) at 32,768 context size, quantized in 8 bits." Columns bf16 / Int4 / Int4 blocks=32 / SFP8: 1B 2.0 / 0.5 / 0.7 / 1.0, +KV 2.9 / 1.4 / 1.6 / 1.9; 4B 8.0 / 2.6 / 2.9 / 4.4, +KV 12.7 / 7.3 / 7.6 / 9.1; 12B 24.0 / 6.6 / 7.1 / 12.4, +KV 38.9 / 21.5 / 22.0 / 27.3; 27B 54.0 / 14.1 / 15.3 / 27.4, +KV 72.7 / 32.8 / 34.0 / 46.1.
- Note: a model developer's own "size x quantization -> memory" table, including the cache. The best external anchor for the chapter's key figure (LCD6 on how the raw column was computed). Quantization-aware training means fine-tuning with the rounding in the loop so the model learns to tolerate it; that is training, so mention only (hand-off to `adapting`).

### LC40. Llama 3.2: quantized small models on a phone, and what naive rounding costs a 1B model
- Source: `meta2024llama32card`.
- Scheme: "All linear layers in all transformer blocks are quantized to a 4-bit groupwise scheme (with a group size of 32) for weights and 8-bit per-token dynamic quantization for activations." "The classification layer is quantized to 8-bit per-channel".
- Instruction-tuned table, MMLU (5-shot): 1B bf16 49.3, "Vanilla PTQ" 43.3, SpinQuant 47.3, QLoRA 49.0; 3B bf16 63.4, 60.5, 62, 62.4; Llama 3.1 8B 69.4. "**for comparison purposes only. Model not released." (for Vanilla PTQ).
- Inference table ("ExecuTorch framework ... ARM CPU as a backend using Android OnePlus 12 device"): 1B BF16 decode 19.2 tokens/s, model file 2358 MB, memory (RSS) 3,185 MB; 1B SpinQuant 50.2 (2.6x), 1083 MB, 1,921 MB; 3B BF16 7.6, 6129 MB, 7,419 MB; 3B SpinQuant 19.7 (2.6x), 2435 MB, 3,726 MB. Footnote: "Decode (tokens/second) is for how quickly it keeps generating."
- Note: "PTQ" = post-training quantization (rounding after training, like GPTQ); Meta's "QLoRA" here is quantization-aware training plus LoRA (the card says "we refer this method as QLoRA" because it resembles Dettmers et al. 2023). `adapting` owns LoRA and QLoRA; here only the outcome: rounding a 1B model naively lost 6 MMLU points, training with rounding in the loop lost almost none.

### LC41. Quantization at the large end: Llama 3 405B in FP8
- Source: `grattafiori2024llama`, pp. 51-52.
- p. 52: "we apply FP8 quantization to most matrix multiplications inside the model. In particular, we quantize most parameters and activations in the feedforward network layers in the model, which account for roughly 50% of the inference compute time. We do not quantize parameters in the self-attention layers of the model." "We find that the quality of Llama 3 405B is sensitive to certain types of quantization": "we do not perform quantization in the first and last Transformer layers"; "High-perplexity tokens such as dates can lead to large activation values."
- Note: quantization is not only a hobbyist trick; developers use it in their own serving. Keep to one sentence.

### LC42. Quantizing the KV cache too (as of 2026-11)
- Sources: `llamacpp2026server`, `ollama2026docs`.
- llama.cpp server: "`-ctk, --cache-type-k TYPE` KV cache data type for K, allowed values: f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1 (default: f16)".
- Ollama FAQ: "`OLLAMA_KV_CACHE_TYPE` - The quantization type for the K/V cache. Default is `f16`." "`q8_0` - 8-bit quantization, uses approximately 1/2 the memory of `f16` with a very small loss in precision, this usually has no noticeable impact on the model's quality". "`q4_0` - 4-bit quantization, uses approximately 1/4 the memory of `f16` with a small-medium loss in precision that may be more noticeable at higher context sizes." "Models that have a high GQA count (e.g. Qwen2) may see a larger impact on precision from quantization than models with a low GQA count."
- Note: no command names in Book 1 [D-003]; say "local runtimes can also store the cache in 8 or 4 bits".

### G. File formats

### LC43. GGUF (2023): one file with weights and metadata
- Sources: `ggml2026gguf`, `llamacpp2023ggufpr`, `huggingface2026gguf`.
- Spec: "GGUF is a file format for storing models for inference with GGML and executors based on GGML. GGUF is a binary format that is designed for fast loading and saving of models, and for ease of reading. Models are traditionally developed using PyTorch or another framework, and then converted to GGUF for use in GGML." "It is a successor file format to GGML, GGMF and GGJT, and is designed to be unambiguous by containing all the information needed to load a model." Desired features include "Single-file deployment", "mmap compatibility: models can be loaded using mmap for fast loading and saving", "Full information: all information needed to load a model is contained in the model file". "The key difference between GGJT and GGUF is the use of a key-value structure for the hyperparameters (now referred to as metadata), rather than a list of untyped values."
- Metadata keys include `general.license` ("License of the model, expressed as a SPDX license expression"), `[llm].context_length` ("length of the context (in tokens) that the model was trained on"), `tokenizer.chat_template` ("a Jinja template that specifies the input format expected by the model"), and `general.file_type` ("the type of the majority of the tensors in the file"). Header: magic "GGUF"; version "Must be `3` for version described in this spec".
- Date: llama.cpp pull request #2398, "GGUF", merged 2023-08-21: "This is a breaking change, meaning that all existing `ggml` models will no longer be compatible after merging." The specification document was added to the ggml repository on 2023-11-01.
- Hugging Face: "GGUF was developed by @ggerganov who is also the developer of llama.cpp, a popular C/C++ LLM inference framework." "unlike tensor-only file formats like safetensors - which is also a recommended model format for the Hub - GGUF encodes both the tensors and a standardized set of metadata." (Source prints an en-dash before "which".)

### LC44. safetensors, and why not pickle
- Sources: `safetensors2026readme`, `huggingface2024pickle`.
- safetensors: "This repository implements a new simple format for storing tensors safely (as opposed to pickle) and that is still fast (zero-copy)." Format: "8 bytes: N, an unsigned little-endian 64-bit integer, containing the size of the header"; "N bytes: a JSON UTF-8 string representing the header", a dict of tensor names to dtype, shape, and offsets; "Rest of the file: byte-buffer." "The main rationale for this crate is to remove the need to use pickle on PyTorch which is used by default." "Pickle: Unsafe, runs arbitrary code".
- Hugging Face: "Pickle is a widely used serialization format in ML. Most notably, it is the default format for PyTorch model weights. There are dangerous arbitrary code execution attacks that can be perpetrated when you load a pickle file."
- Note: the reader-level point: a downloaded model file is data you run; older formats could carry code. Do not date "PyTorch default" beyond the doc's 2024 commit.

### H. Local runtimes (as of 2026-11)

### LC45. llama.cpp's start (March 2023)
- Source: `llamacpp2023readme` (and GitHub API: repository created 2023-03-10).
- README of 2023-03-10: "Inference of Facebook's LLaMA model in pure C/C++". "The main goal is to run the model using 4-bit quantization on a MacBook." Features: "Plain C/C++ implementation without dependencies", "Apple silicon first-class citizen", "4-bit quantization support", "Runs on the CPU". "This was hacked in an evening - I have no idea if it works correctly." "So far, I've tested just the 7B model." The printed "typical" run (7B, file `ggml-model-q4_0.bin`): "model size = 4017.27 MB" and "predict time = 31378.77 ms / 61.41 ms per token". Limitations: "in theory, you should be able to run 65B on a 64GB MacBook"; "I don't know yet how much the quantization affects the quality of the generated text".
- README of 2023-03-12 adds: "Please do not make conclusions about the models based on the results from this implementation." and "another demo of running both LLaMA-7B and whisper.cpp on a single M1 Pro MacBook".
- Note: the machine for the 61.41 ms run is not stated (only that it is arm64 Darwin); do not attach "M1 Pro" to it. 61.41 ms/token is about 16 tokens per second (computed). The sampling line in the same output, "temp = 0.800000, top_k = 40, top_p = 0.950000", matches the defaults the `generation` chapter quotes for today's server: a small continuity the drafter may use.

### LC46. llama.cpp today (as of 2026-11)
- Source: `llamacpp2026readme`.
- "The main goal of llama.cpp is to enable LLM (and VLM) inference with minimal setup and state-of-the-art performance on a wide range of hardware - locally and in the cloud." Features: "Apple silicon is a first-class citizen"; "1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory use"; "Custom CUDA kernels for running LLMs on NVIDIA GPUs (support for AMD GPUs via HIP and Moore Threads GPUs via MUSA)"; "CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity". "The llama.cpp project is build on top of the ggml library." Badge: "License: MIT". (Source prints an en-dash before "locally".)
- Server (`llamacpp2026server`): context size "default: 0, 0 = loaded from model"; layers kept in GPU memory "default: auto"; `--fit` "whether to adjust unset arguments to fit in device memory ... default: 'on'".
- Note: Book 2 pins a version and shows commands [D-007]; Book 1 states only what the tool is and does.

### LC47. Ollama (as of 2026-11)
- Source: `ollama2026docs`.
- README: "Start building with open models. Access the latest releases locally or in the cloud with complete privacy." "Supported backends: llama.cpp project founded by Georgi Gerganov." Import doc: "Ollama does not quantize GGUF models during import. Prepare and quantize them first with a GGUF tool such as llama.cpp's llama-quantize." It can also import "Safetensors weights".
- FAQ: "By default, Ollama uses a context window size of 4096 tokens." Example status line: "llama3:70b ... 42 GB 100% GPU"; "48%/52% CPU/GPU means the model was loaded partially onto both the GPU and into system memory". "By default models are kept in memory for 5 minutes before being unloaded."
- Note: Ollama's README now also advertises cloud use; describe it as "a popular wrapper around llama.cpp that downloads and runs models". The 42 GB for a 70B model matches 4-bit arithmetic (LCM 1).

### LC48. MLX (as of 2026-11)
- Source: `mlx2026readme`.
- MLX: "MLX is an array framework for machine learning on Apple silicon, brought to you by Apple machine learning research." "Unified memory: A notable difference from MLX and other frameworks is the unified memory model. Arrays in MLX live in shared memory. Operations on MLX arrays can be performed on any of the supported device types without transferring data."
- mlx-lm: "MLX LM is a Python package for generating text and fine-tuning large language models on Apple silicon with MLX." "Integration with the Hugging Face Hub to easily use thousands of LLMs with a single command." "Support for quantizing and uploading models to the Hugging Face Hub." "The default model for generation and chat is mlx-community/Llama-3.2-3B-Instruct-4bit."
- Note: unified memory is why a Mac with a large memory can hold models that do not fit on a consumer GPU (memory sizes in LC50). MLX's README states the shared-memory design; the comparison with GPU memory sizes is this ledger's inference, label it.

### I. Hardware and speed

### LC49. Generating one token means reading every weight
- Sources: `pope2022efficiently`, `frantar2023gptq`, `lin2024awq`, and `generation` chapter (`shazeer2019fast`, `kwon2023efficient`).
- Pope et al. p. 1: "The large memory footprint gives rise to a large amount of memory traffic to load the parameters and KV cache from high-bandwidth memory (HBM) into the compute cores for each step, and hence a large total memory bandwidth required to meet a given latency target."
- GPTQ p. 8 and AWQ p. 6: generation is "primarily limited by memory bandwidth"; arithmetic intensity "≈1" in FP16 on an RTX 4090 (LC37, LC38).
- Note: this is the basis of the estimate tokens/s ≤ bandwidth / bytes read per token (LCM 4). The `generation` chapter already made the memory-bound point; this chapter adds the arithmetic.

### LC50. Memory bandwidth of consumer machines (vendor figures, dated)
- Sources: `apple2024m4pro`, `apple2025m5`, `apple2026mbpspecs`, `nvidia2025blackwell`, `nvidia2026rtx5090`.
- Apple (October 30, 2024): "M4 supports up to 32GB of unified memory and has higher memory bandwidth of 120GB/s." "M4 Pro supports up to 64GB of fast unified memory and 273GB/s of memory bandwidth". "M4 Max supports up to 128GB of fast unified memory and up to 546GB/s of memory bandwidth ... This allows developers to easily interact with large language models that have nearly 200 billion parameters."
- Apple (October 15, 2025): "M5 offers unified memory bandwidth of 153GB/s, providing a nearly 30 percent increase over M4 and more than 2x over M1."
- Apple MacBook Pro specifications as served 2026-11-11: "Apple M6 chip ... Up to 170GB/s memory bandwidth" ("16GB unified memory (153GB/s memory bandwidth)", "24GB or 32GB unified memory (170GB/s memory bandwidth)"); "Apple M5 Pro chip ... 307GB/s memory bandwidth"; "Apple M5 Max chip ... 460GB/s" (32-core GPU) and "614GB/s" (40-core GPU); M5 Max "48GB, 64GB, or 128GB unified memory".
- NVIDIA whitepaper V1.1: p. 13: "The GeForce RTX 5090 ships with 28 Gbps GDDR7 memory and delivers 1.792 TB/sec peak memory bandwidth". Table 1 (pp. 14-15): RTX 3090 936 GB/sec, RTX 4090 1008 GB/sec, RTX 5090 1792 GB/sec; memory 24 GB, 24 GB, 32 GB. Table 4 (pp. 49-50): RTX 4080 16 GB GDDR6X, 716.8 GB/sec; RTX 5080 16 GB, 960 GB/sec. Product pages: RTX 5090 "32 GB GDDR7", RTX 4090 "24 GB GDDR6X".
- Note: "peak" bandwidth is a ceiling; real decoding reaches a fraction (LCM 5). Apple's "nearly 200 billion parameters" is a marketing claim consistent with 4-bit arithmetic (computed: 200B x 0.5 bytes = 100 GB < 128 GB), but it says nothing about speed. Date-stamp every figure. The M6 entry is from a live spec page and will change.

### LC51. A desktop CPU's memory system (for the CPU-versus-GPU contrast)
- Source: `amd2026ryzen9950x`.
- "System Memory Type DDR5"; "Memory Channels 2"; "Max Memory Speed 2x1R DDR5-5600"; "Launch Date 08/15/2024".
- Note: no bandwidth is printed. 2 channels x 5600 million transfers/s x 8 bytes = 89.6 GB/s needs the 64-bit channel width, which was not sourced (Not fetched). If the drafter wants a CPU number, either source the width or say "under 100 GB/s" only after sourcing. Alternatively contrast GPU vs Apple unified memory only.

### LC52. Tokens per second in primary documents
- Sources: `llamacpp2026bench`, `llamacpp2026quantize`, `meta2024llama32card`, `abdin2024phi3`, `lin2024awq`, `llamacpp2023readme`.
- llama-bench README: "The results are given in average tokens per second (t/s) and standard deviation." "The measurements with llama-bench do not include the times for tokenization and for sampling." Its CSV example names the hardware: "AMD Ryzen 7 7800X3D 8-Core Processor", "NVIDIA GeForce RTX 4080", model `Qwen2.5-7B-Instruct-Q4_K_M.gguf`, model_size 4677120000 bytes, 7615616512 parameters: prompt processing (512 tokens) 7285.68 t/s, text generation (128 tokens) 119.92 t/s (test time 2025-04-24).
- Its offload example (7B Q4_0, 3.56 GiB, CUDA, hardware not named): text generation 13.45 t/s with 10 layers on the GPU, 54.78 with 32, 131.66 with all 35. CPU-only threads example: 4.05 t/s with 1 thread, 16.71 with 8, 16.41 with 32.
- Others: Llama 3.2 on a OnePlus 12 phone (LC40); Phi-3-mini on an iPhone 14, "more than 12 tokens per second" (LC22); Raspberry Pi 4B, 0.7 tokens/s for 7B (LC38); llama.cpp's first run, 61.41 ms per token (LC45).
- Note: CPU generation stops improving after about 8 threads in that example: consistent with a memory-bandwidth limit, but the README does not say so (interpretation; label it). Partial offload helps little until nearly all layers are on the GPU: the slowest part sets the pace.

### J. What small models are and are not good at

### LC53. Size still matters on hard tasks (Llama 3, 2024)
- Source: `grattafiori2024llama`, Table 2 (p. 3), post-trained models.
- 8B / 70B / 405B: MMLU (5-shot) 69.4 / 83.6 / 87.3; HumanEval 72.6 / 80.5 / 89.0; GSM8K 84.5 / 95.1 / 96.8; MATH 51.9 / 68.0 / 73.8; GPQA 32.8 / 46.7 / 51.1; MGSM 68.9 / 86.9 / 91.6. Same table: Mistral 7B MMLU 61.1, Gemma 2 9B 72.3.
- Note: benchmark names need one-line glosses (`evaluation` defines them later; say "a test of X"). The gap is largest on the hardest tests (MATH, GPQA).

### LC54. Very small models (Llama 3.2, 2024)
- Source: `meta2024llama32card`, base pretrained table: MMLU (5-shot) 1B 32.2, 3B 58, Llama 3.1 8B 66.7; ARC-Challenge 32.8 / 69.1 / 79.7; SQuAD 49.2 / 67.7 / 77. Intended uses: "assistant-like chat and agentic applications like knowledge retrieval and summarization, mobile AI powered writing assistants and query and prompt rewriting."
- Note: Meta's own suggested uses for 1B/3B are narrow tasks; summarisation scores (TLDR9+) are flat across 1B, 3B, 8B in the instruction-tuned table (16.8, 19.0, 17.2), a fair example of "small is enough for some jobs".

### LC55. Knowledge is the first casualty (Mistral 7B, Phi-3)
- Sources: `jiang2023mistral` (LC15), `abdin2024phi3`.
- Phi-3 p. 9, "Weakness": "while phi-3-mini model achieves similar level of language understanding and reasoning ability as much larger models, it is still fundamentally limited by its size for certain tasks. The model simply does not have the capacity to store too much "factual knowledge", which can be seen for example with low performance on TriviaQA. However, we believe such weakness can be resolved by augmentation with a search engine."
- Table p. 6 (read on the page image): MMLU Phi-3-mini (3.8b) 68.8, Mistral (7b) 61.7, Llama-3-In (8b) 66.5, Mixtral (8x7b) 70.5, GPT-3.5 71.4; TriviaQA 64.0, 75.2, 67.7, 82.2, 85.8.
- Note: a clean illustration: the 3.8B model beats the 7B one on a reasoning-heavy test and loses on trivia recall. Both are the developers' own evaluations. Hand-off to `tools` (retrieval as the fix).

### LC56. Small models are hurt more by rounding
- Sources: `frantar2023gptq` (LC37), `meta2024llama32card` (LC40).
- Note: GPTQ: "larger models generally ... appear easier to quantize" (p. 7); OPT-125M perplexity +12.5% at 4-bit GPTQ vs +0.4% for OPT-175B (computed from Table 3). Llama 3.2 1B lost 6 MMLU points to naive rounding. So the cheapest model to run is also the most fragile to squeeze.

### LC57. Why people run models locally (attributed)
- Sources: `lin2024awq` (cost, privacy, offline: LC38), `zuckerberg2024open` (control, data, cost: LC5), `abdin2024phi3` ("fully offline", LC22), `meta2023llamablog` (research access), `touvron2023llama2` p. 7 (costs not incurred again).
- Note: present as reasons given by the sources, with no claim that local is cheaper in general (no source compares costs).

## Disputed or inconsistent points

### LCD1. What "open" means
- **Strict (OSI).** Open Source AI requires the four freedoms and the preferred form for modification: data information, complete code, and parameters under OSI-approved terms (LC1). In the OSI's validation, Pythia, OLMo, Amber, CrystalCoder, and T5 passed; Llama 2, Grok, Phi-2, and Mixtral did not (LC3). The OSI calls weights-only releases "Open Weights" and says they "stop short" (LC2), and in 2023 said Llama 2's licence is "not Open Source" (LC4).
- **Inside the strict camp, a further dispute:** the OSAID requires a description of training data, not the data; the FAQ records that "some people believe that full, unfettered access to all training data ... is paramount" (LC3).
- **Meta's usage.** Meta calls Llama "open source" (LC5) while its licences restrict very large companies (700M MAU), attach an acceptable-use policy, and (Llama 2 and 3) forbid using outputs to improve other models (LC6 to LC8).
- **Permissive licences, closed data.** Mistral, Qwen3, Gemma 4 (Apache 2.0), Phi-3, and DeepSeek-R1 (MIT) give broad rights to the weights (LC9 to LC11) but not the training data; Mixtral still failed the OSAID validation.
- **Suggested wording:** "This book says open-weight for any model whose trained parameters can be downloaded and run, and names the licence when it matters. Open source, in the sense the Open Source Initiative defined in 2024, asks for more: the code that trained the model and enough information about its data to rebuild it. Few large models meet that bar." Avoid calling Llama "open source" in the book's own voice; quote Meta when reporting Meta's view.

### LCD2. Mixtral's size
- Blog: 46.7B total, 12.9B per token (LC16). Paper: 47B and 13B. Hub: 46,702,792,704 (LC26). The name "8x7B" suggests 56B. Use 46.7 billion and 12.9 billion with the blog, or "about 47 and 13" with the paper; cite which.

### LCD3. Sizes and units in llama.cpp's README
- The memory table is in GB and the quantization table in GiB (LC31, LC35); 1 GiB = 1.074 GB (computed). The book's `destination` chapter uses GB = 10^9 bytes. Convert, and say which.
- "Original size" 32.1 GB for 8B equals 4 bytes x 8,030,261,248 (computed 32.12 GB), but 280.9 GB for 70B and 1,625.1 GB for 405B do not equal 4 bytes x the Hub's counts (282.2 GB and 1,623.4 GB, computed). The cause is not stated. Prefer computing from the Hub's counts and the README's bits-per-weight, and cite the README table only as a cross-check.

### LCD4. llama.cpp's perplexity and speed figures lack context
- `QUANT_OPTIONS` perplexity increments are for "Llama-3-8B" (not 3.1), F16/BF16 lines for "Mistral-7B"; no baseline perplexity, text, or date (LC32). The README's speed table has no hardware (LC31). The underlying measurements are presumably in the linked pull requests (not read). Use the numbers as llama.cpp's own indicative figures, stated as such, and not as percentages.

### LCD5. Do outlier features "emerge" at 6.7B?
- LLM.int8() reports a "phase shift" at about 6.7B parameters in OPT models (LC36). Later work (lead only, not fetched) argued the outliers depend on training choices. Say "in the models they studied" and do not present 6.7B as a law.

### LCD6. Gemma 3's raw sizes are rounded
- Table 3's bf16 column (LC39) equals nominal size x 2 bytes (1B 2.0, 4B 8.0, 12B 24.0, 27B 54.0), while Table 1's parameter counts give 7.77 GB for 4B without the vision encoder or 8.60 GB with it (computed). Treat the table as approximate; do not use it to back out exact counts.

### LCD7. Mistral 7B's context length
- Paper Table 1: context_len 8192, sliding window 4096 (LC15). Hub config: `max_position_embeddings` 32768 (LC26). Neither the paper nor the config read here explains the difference. Avoid stating a context length for Mistral 7B.

### LCD8. "Mitchell, 2018"
- Hugging Face's docs cite "Mitchell, 2018" (the arXiv v1 year); the paper is FAT* 2019 (LC25). Cite 2019.

### LCD9. "Same speed as a 12.9B model"
- Mistral's blog says Mixtral "processes input and generates output at the same speed and for the same cost as a 12.9B model"; the paper (p. 4) notes routing overhead and that SMoEs suit batched workloads (LC16). Prefer the paper's qualified statement.

## Mechanism claims to check numerically at drafting [D-009]

Suggested script: `code/checks/local.py` (standard library only), imported by `figures/local.py` [D-014]. The arithmetic below was run once in a scratch script in this session; the script must reproduce it from the sourced inputs, not from these printed results.

Inputs to hard-code with their sources:
- Parameter counts (LC26): Llama 3.2 1B 1,235,814,400; Llama 3.2 3B 3,212,749,824; Phi-3-mini 3,821,079,552; Mistral 7B 7,241,732,096; Llama 3.1 8B 8,030,261,248; Qwen3-8B 8,190,735,360; Mixtral 46,702,792,704; Llama 3.1 70B 70,553,706,496.
- Bits per weight: from block layouts (LC33) for pure types: F16 16, Q8_0 8.5, Q6_K 6.5625, Q4_0 4.5; from the README's Llama 3.1 8B table (LC31) for mixes: Q5_K_M 5.7036, Q4_K_M 4.8944, Q3_K_M 3.9960, Q2_K 3.1593. Label the mixes as "measured on Llama 3.1 8B; other models differ slightly".
- Architecture for the KV cache: Llama 3.1 8B (32 layers, 8 KV heads, head dim 4096/32 = 128; LC20), Llama 3.1 70B (80, 8, 128), Qwen3-8B (36, 8, 128), Phi-3-mini (32, 32, 96; LC26). Formula as in `generation`: bytes per token = 2 (key and value) x layers x KV heads x head dimension x bytes per number.
- Bandwidths (LC50): M4 120, M5 153, M4 Pro 273, M4 Max 546, RTX 4080 716.8, RTX 4090 1008, RTX 5090 1792 GB/s.

1. **Weights memory table (the key figure).** bytes = parameters x bits per weight / 8, in GB (10^9). Computed: Llama 3.1 8B: F16 16.06, Q8_0 8.53, Q6_K 6.59, Q5_K_M 5.73, Q4_K_M 4.91, Q4_0 4.52, Q3_K_M 4.01, Q2_K 3.17. Llama 3.2 1B: 2.47 / 1.31 / 1.01 / 0.88 / 0.76 / 0.70 / 0.62 / 0.49. Llama 3.2 3B: 6.43 / 3.41 / 2.64 / 2.29 / 1.97 / 1.81 / 1.60 / 1.27. Mistral 7B: 14.48 / 7.69 / 5.94 / 5.16 / 4.43 / 4.07 / 3.62 / 2.86. Qwen3-8B: 16.38 / 8.70 / 6.72 / 5.84 / 5.01 / 4.61 / 4.09 / 3.23. Mixtral: 93.41 / 49.62 / 38.31 / 33.30 / 28.57 / 26.27 / 23.33 / 18.44. Llama 3.1 70B: 141.11 / 74.96 / 57.88 / 50.30 / 43.16 / 39.69 / 35.24 / 27.86.
   Cross-checks to assert: Llama 3.1 8B F16 = 14.96 GiB and Q4_K_M = 4.58 GiB (README, LC31; computed 14.958 and 4.576); 8B at 32 bits = 32.1 GB (README, LC35; computed 32.12); 70B Q4_K_M 43.16 vs README 43.1 GB; Ollama's "llama3:70b 42 GB" is of the same order (different quantization, unstated); Phi-3's "≈1.8GB" at 4 bits vs 3.82e9 x 4.5/8 = 2.15 GB at Q4_0 (the report's figure is lower: its exact format is not stated; do not force agreement, report both).
2. **Group-scale overhead.** Q4_0: (32 x 4 + 16) / 32 = 4.5 bits; Q8_0: (32 x 8 + 16) / 32 = 8.5; Q4_K: 144 bytes per 256 weights = 4.5 (2 + 2 + 12 + 128 bytes); Q6_K: 210 bytes per 256 = 6.5625; Q2_K 84 bytes = 2.625; Q3_K 110 bytes = 3.4375; Q5_K 176 bytes = 5.5. GPTQ's "group-size 128 (≈ 0.15 extra bits)": 16/128 = 0.125 for the scale alone, (16 + 3)/128 = 0.148 with a 3-bit zero point (the latter is an assumption about GPTQ's storage; say "about" and cite the paper's figure).
3. **KV cache per token and per context (16-bit).** Llama 3.1 8B: 131,072 bytes/token (matches `generation`); 8K tokens 1.07 GB, 32K 4.29 GB, 128K 17.18 GB. Llama 3.1 70B: 327,680 bytes; 32K 10.74 GB. Qwen3-8B: 147,456 bytes; 32K 4.83 GB. Phi-3-mini (no grouped keys and values): 393,216 bytes; its full 4K window 1.61 GB, close to its whole 4-bit weights. With an 8-bit cache (q8_0, 8.5 bits): Llama 3.1 8B 69,632 bytes/token (Ollama's "approximately 1/2", LC42).
   Total memory column for the figure: weights + KV cache at a stated context (suggest 8K and 32K) + a stated, labelled allowance for working memory (no source gives one; either omit or label it as an assumption).
4. **Bandwidth-bound estimate (label as an upper bound, not a prediction).** tokens/s ≤ bandwidth / bytes read per token, with bytes read ≈ weight bytes (+ KV cache bytes at the current context). Llama 3.1 8B Q4_K_M (4.91 GB): M4 24, M5 31, M4 Pro 56, M4 Max 111, RTX 4080 146, RTX 4090 205, RTX 5090 365 tokens/s; at F16 (16.06 GB): M5 9.5, RTX 4090 63, RTX 5090 112. Llama 3.1 70B Q4_K_M (43.1 GB): M4 Max 12.7 (fits in 128 GB), RTX 5090 not applicable (does not fit in 32 GB). Mixtral Q4_K_M: memory 28.6 GB but bytes per token about 12.9e9 x 4.8944 / 8 = 7.9 GB (active parameters only, ignoring that shared layers are counted once: approximate).
5. **Check the bound against a measured number.** llama-bench's RTX 4080 example (LC52): 716.8 GB/s / 4.67712 GB = 153.3 tokens/s ceiling; measured 119.9: 78% of the ceiling (computed). The KV cache at 128 tokens is negligible here.
6. **Speed scales inversely with size (llama.cpp README, hardware unstated).** size (GiB converted to GB) x tokens/s gives an implied bandwidth that should be roughly constant if decoding is bandwidth-bound: F16 469, Q8_0 435, Q6_K 387, Q4_K_M 354, Q2_K 253, IQ1_S 160 GB/s (computed). The fall at small sizes shows other costs (unpacking the bits) taking over. Phone (LC40): 2358 MB x 19.2 = 45.3 GB/s, 1083 x 50.2 = 54.4, 6129 x 7.6 = 46.6, 2435 x 19.7 = 48.0 (computed): roughly constant, consistent with a bandwidth limit (the card does not state the phone's bandwidth). llama.cpp's first run: 4017.27 MB at 61.41 ms/token = 16.3 tokens/s, implied 65 to 69 GB/s depending on MB = 10^6 or 2^20 (machine unstated: do not present as a bandwidth measurement).
7. **Rounding demo (worked example).** A group of, say, 8 or 32 made-up weights with a fixed seed; absmax 4-bit rounding (scale = max |w| / 7, integers -7..7, as a simplification of Q4_0, which the drafter should describe as "like" llama.cpp's, not identical); print the stored integers, scale, reconstructed values, and mean absolute error. Then insert one outlier 20 times larger (LC36's "up to 20x") and show the error on the other weights jump. Then split into two groups with their own scales and show it recover. Purely illustrative numbers [D-002].
8. **Source arithmetic.** GPTQ relative perplexity increases at 4-bit: OPT-125M 12.5%, OPT-175B 0.4%, BLOOM-560M 7.2%, BLOOM-176B 1.2%. Llama 3.2 1B MMLU: 49.3 - 43.3 = 6.0 points (vanilla PTQ), 49.3 - 49.0 = 0.3 (QAT + LoRA). GPTQ Table 6 speedups 230/71 = 3.24, 589/130 = 4.53. Llama 3.2 phone: SpinQuant file 1083/2358 = 46% of BF16, decode 50.2/19.2 = 2.6x. Apple's "nearly 200 billion parameters": 200e9 x 4/8 = 100 GB of weights. 61.41 ms/token = 16.3 tokens/s.
9. **GiB and GB.** 1 GiB = 1.0737 GB; 4.58 GiB = 4.92 GB.

## Figures planned [D-014]

- `figures/local-memory.svg` (the outline's key figure, "a table mapping model size and quantization level to memory needed, computed"): best printed as a table in the chapter (Pandoc table, numbers from `code/checks/local.py`, as `destination` did) and optionally drawn as a heat-map grid: rows Llama 3.2 1B, 3B, Llama 3.1 8B, (Mixtral), Llama 3.1 70B; columns F16, Q8_0, Q6_K, Q5_K_M, Q4_K_M, Q3_K_M, Q2_K; cell = GB of weights; a second line or panel adds the KV cache at 8K and 32K tokens. Mark cells against two memory sizes the reader might own (for example 16 GB and 32 GB, from LC50's product configurations), as "fits / does not fit, before working memory". Caption: weights only unless stated; bits per weight for mixed types measured on Llama 3.1 8B; as of 2026-11.
- `figures/local-groups.svg`: the rounding demo of mechanism item 7: three small strips (original weights; rounded with one scale and an outlier; rounded with two groups) with the error printed. Illustrative.
- `figures/local-bandwidth.svg` (optional): bars of the bandwidth-bound tokens/s for one model (Llama 3.1 8B Q4_K_M) across the devices of item 4, with the one measured RTX 4080 point (item 5, different model of similar size, label it) shown as a dot. Caption must say "upper bound from peak bandwidth; real speeds are lower".
- `figures/local-tradeoff.svg` (optional): llama.cpp's own size vs perplexity-increase points (LC32) for Llama-3-8B, as a scatter with labels. Only if the drafter accepts LCD4's caveat in the caption.

## Scope notes for drafting

- **Hand-offs.**
  - From `destination`: the parameters x bytes table (32 and 16 bits); this chapter adds the lower-bit columns and must use the same GB convention.
  - From `generation`: prefill and decode, the KV cache and its size formula (Llama 3 8B, 131,072 bytes per token), memory-bound decoding (Shazeer, Pope, Kwon), and llama.cpp's sampling defaults. Do not re-explain; build on them.
  - From `training`: float16 and bfloat16 (ranges, spacing). Here: going below 16 bits.
  - From `anatomy`: parameter counts per layer; grouped key-value heads (Llama 3's 8 KV heads) as the reason the cache is small.
  - From `scale`: LLaMA's "smaller models trained longer"; Llama 2's "costs need not be incurred by others", which this chapter takes up.
  - To/with `adapting` (researched in parallel): LoRA, QLoRA (4-bit training), distillation. This chapter owns inference quantization only; mention QLoRA only as "the same rounding used during fine-tuning, see `adapting`", and Meta's "QLoRA" label for Llama 3.2 (LC40) with a pointer.
  - To `since-2017`: mixture-of-experts mechanics, grouped-query attention, sliding windows. Here: only the memory/speed consequences. The working tree's references.bib gained `deepseekai2024deepseekv3` (the V3 report, read in v2 by other research) during this session; for "671B total, 37B active" the drafter may cite it instead of the model card, after locating the numbers in that report (not done here).
  - Keys that appeared in the working tree during this session and are reused rather than duplicated: `mitchell2019model`, `jiang2023mistral`, `jiang2024mixtral`, `deepseekai2025r1` (v1 pages, LC19), `dettmers2023qlora` (pointer to `adapting` only). If any of them is not committed when drafting starts, take its entry from the working tree's references.bib.
  - To `tools`: retrieval as the remedy for small models' missing facts (LC55).
  - To `evaluation`: benchmark names and contamination. Here: name tests as "a test of X" and note they are developers' own figures.
  - To Book 2 (`b2-setup`, `b2-llamacpp`, `b2-chat`): installation, commands, file downloads, flags, pinned llama.cpp version [D-007]. Book 1 has no commands, no flags, no code blocks [D-003]; tool names (llama.cpp, Ollama, MLX) and file names (as plain text) are fine.
- **What not to say.**
  - Not "open source" for Llama in the book's voice (LCD1); not that Apache-licensed weights make a model "open source AI" in the OSI's sense.
  - Not that LLaMA (2023) was the first open-weight LLM (GPT-2 2019, BLOOM 2022; LC14 note).
  - Not that the original LLaMA weights were public: access was by application, non-commercial (LC13). Do not mention the leak without a source.
  - Not that Llama 3.1's licence forbids training other models on its outputs (that was Llama 2 and 3; LC8).
  - Not "4-bit means 4 bits per weight" for llama.cpp files: Q4_0 is 4.5, Q4_K_M about 4.9 (LC33, LC34).
  - Not that quantization is free: cost grows below about 4 bits and is larger for small models (LC32, LC37, LC40).
  - Not that the "8x7B" model needs 56B worth of memory, nor that it runs as fast as a 13B model in every setting (LC28, LCD9).
  - Not a tokens-per-second figure for a device without saying it is a bound or citing a measurement with its hardware (LC52, LCD4).
  - Not that llama.cpp's first run was on an M1 Pro (LC45).
  - Not that small models "know" less in general; say what the sources show: lower scores on knowledge tests, attributed by the developers to limited capacity (LC15, LC55).
  - Not the Gemma terms as current for Gemma 4 (LC10).
  - Not the Hugging Face "all open and publicly available" phrase (LC23).
- **Terms to define at first use (and add to the glossary).** open-weight model; closed (API-only) model; licence (in the model sense); acceptable use policy; gated download; model hub; model card; base model vs instruct (instruction-tuned) model; quantization; bits per weight; group (block) and scale; outlier; round-to-nearest; calibration data; post-training quantization vs quantization-aware training (one sentence); GGUF; safetensors; runtime (inference engine); memory bandwidth; unified memory; VRAM (GPU memory); offloading (splitting layers between GPU and CPU); tokens per second; mixture of experts (if not yet defined, point to `since-2017`); active parameters.
- **Formulas allowed (standard form, every symbol explained) [D-002].** memory for weights = parameters x bits per weight / 8 bytes; KV cache = 2 x layers x KV heads x head dimension x bytes per number x tokens (from `generation`); decode speed ≤ memory bandwidth / bytes read per token; absmax rounding: stored integer = round(w / s), with s = max |w| / (largest integer); reconstruction w ≈ s x integer. No derivations, no GPTQ algebra.
- **Bridges.** Quantization is the same idea as binning a continuous variable or storing a JPEG at lower quality: fewer distinct values, small loss. Group-wise scales are like standardising each column separately rather than the whole table. Outliers: one extreme value stretching a min-max scaling, familiar from feature scaling in the 2000s. Decode speed limited by memory bandwidth: like a database query bound by disk reads rather than CPU. Model cards: the documentation of a published dataset or model, formalised (Mitchell et al.).
- **Date stamps (as of 2026-11).** Hub counts; licence terms (Gemma 4, Llama versions); llama.cpp features and quantization list; Ollama defaults; MLX; hardware bandwidths and product memory sizes (each with its announcement date); tokens/s measurements (with test date where given: llama-bench example 2025-04-24). Licences quote their own "release date" lines.
- **Reader questions to anticipate.** "Will a model run on my laptop?" (memory table + KV cache + bandwidth bound). "Which file do I download?" (name anatomy; Q4_K_M is a common middle choice according to llama.cpp's own example; Book 2 for practice). "Is it legal to use at work?" (licence summary; not legal advice). "Is a local model as good as ChatGPT?" (LC53 to LC55, dated, no hype).

## Leads not used as sources

- llama.cpp GitHub discussions with community benchmark tables (for example "Performance of llama.cpp on Apple Silicon M-series", discussion #4167): useful for a sense of real tokens/s, but forum data; not read, not citable [D-005].
- Wikipedia pages on LLaMA, GGUF, and memory bandwidth: leads for dates; every date used here comes from a primary source instead.
- Heather Meeker's Open Weights Definition (2023), named by the OSI (LC2): not fetched.
- Later papers on whether outlier features are emergent or a training artifact (LCD5): not fetched.
- k-quant and importance-matrix pull requests in llama.cpp (#1684, #4861): would give the measurement context for LC32; not read.
- The OSI's OSAID endorsements list and the Model Openness Framework (Linux Foundation): alternative "openness" scales, not read.
- Third-party GGUF repositories on Hugging Face (for example TheBloke's, named in `huggingface2026gguf`): examples of naming in the wild, not needed.

## Worked examples used in the chapter

All produced by `code/checks/local.py` [D-009] (standard library only; it imports `code/checks/generation.py` and asserts that its KV-cache size for Llama 3 8B, 131,072 bytes per token, is the same). Each worked number in `book1/chapters/local.md` carries a `<!-- D-009: code/checks/local.py, Example N -->` comment.

- Example 1, block layouts: Q4_0 (32 x 4 + 16) / 32 = 4.5 bits per weight; Q8_0 8.5; k-quant super-blocks (Q4_K 144 bytes per 256 = 4.5, Q6_K 6.5625); groups of 8 with a 16-bit scale = 6 bits; Q4_K_M 4.89 and Q4_K_S 4.67 (README values rounded); bits per weight as printed (16.00, 8.50, 6.56, 5.70, 4.89, 4.00, 3.16). Used in "Quantization" and the tables.
- Example 2, rounding demo: eight made-up weights (0.12, -0.31, 0.05, 0.27, -0.08, 0.19, -0.22, 0.02), absmax to integers -7..7: scale 0.0443, integers 3, -7, 1, 6, -2, 4, -5, 0, mean error on the first seven 0.007 against mean size 0.177; with the last weight replaced by 6.2 (20 x 0.31): scale 0.886, all seven round to 0, error 0.177; outlier kept aside: error 0.007; two groups of four: the group without the outlier unharmed, its three neighbours lost. Used in "Quantization", "Outliers", and `local-groups.svg`.
- Example 3, weights memory: the main table (seven models x seven types, Hub counts LC26 x bits LC31/LC33 / 8); 8B at 16 and 32 bits (16.06, 32.12 GB); cross-checks against the README (14.96 GiB, 4.58 GiB, 43.16 vs 43.1 GB); Phi-3-mini at Q4_0 2.15 GB and at exactly 4 bits 1.91 GB (report: about 1.8); 200B at 4 bits = 100 GB. Used in "How much memory", "The memory table", `local-memory.svg` (a).
- Example 4, KV cache: bytes per token for Llama 3.1 8B (131,072), Qwen3-8B (147,456), Llama 3.1 70B (327,680), Phi-3-mini (393,216); at 8,192 and 32,768 tokens; Phi-3-mini's 4,096-token window 1.61 GB; Llama 3.1 8B with an 8-bit cache at 32K, 2.28 GB. Used in the KV table and following paragraph.
- Example 5, totals: Q4_K_M weights plus 16-bit cache at 8K and 32K (8B 9.21 GB, Qwen3-8B 9.84, 70B 53.90 at 32K). KV table and `local-memory.svg` (b).
- Example 6, mixture of experts: 8 x Mistral 7B = 57.9 billion vs Mixtral 46.7; Q4_K_M 28.57 GB in memory, about 7.89 GB read per token (active parameters only, approximate).
- Example 7, bandwidth bound: Llama 3.1 8B Q4_K_M on seven devices (24, 31, 56, 111, 146, 205, 365 tokens/s); F16 does not fit the 16 GB RTX 4080, RTX 5090 bound 112; 70B Q4_K_M bound 12.6 (M4 Max), 6.3 (M4 Pro); Mixtral on M4 Max 69 vs 19; 8B at a 32K cache on RTX 4090, 205 to 109. "How fast" section and `local-bandwidth.svg`.
- Example 8, measurements: RTX 4080 llama-bench, bound 153.3, measured 119.92 = 78%; prompt/generation ratio about 61; README F16 vs Q4_K_M size ratio 3.27, speed ratio 2.47; phone file 46%, decode 2.6x; llama.cpp's first run 16.3 tokens/s; offload and thread examples quoted as printed.
- Example 9, cost of rounding: GPTQ OPT-125M +12.5%, OPT-175B +0.4% (BLOOM figures printed, not used); Llama 3.2 MMLU costs 6.0 and 0.3 (1B), 2.9 and 1.0 (3B). GPTQ Table 6 speedups printed but cut from the chapter for length.
- Example 10, small vs large: Phi-3-mini vs Mistral 7B, MMLU +7.1, TriviaQA -11.2 (Llama 3 differences printed, not used).

## Figures

Drawn by `figures/local.py` [D-014], which imports `code/checks/local.py`; same rcParams, colours, and `save()` (metadata Date None, `svg.hashsalt`) as `figures/adapting.py`. Each was rendered with rsvg-convert and checked for overlaps and clipping.

- `figures/local-memory.svg` (the outline's key figure): (a) heat map of weights in GB, seven models x seven llama.cpp types, shaded in bands up to 16, 32, 64, 128, and over 128 GB; (b) stacked bars for Llama 3.1 8B, Qwen3-8B, and Llama 3.1 70B at Q4_K_M plus a 16-bit KV cache at 8K and 32K tokens. No working-memory allowance (author decision). The band edges are the drafter's choice, tied in the caption to memory sizes named in the chapter (16 GB cards and laptops, 64 and 128 GB Macs).
- `figures/local-groups.svg`: the rounding demo of Example 2 in three strips (no outlier; outlier with one scale; outlier kept aside in 16 bits). Illustrative.
- `figures/local-bandwidth.svg`: upper bounds for Llama 3.1 8B at Q4_K_M across seven devices, with the one measurement whose hardware is named (llama-bench, RTX 4080, Qwen2.5-7B-Instruct Q4_K_M) as a dot labelled with its own bound.
- Not drawn: `local-tradeoff.svg` (size vs perplexity increase), left out because of LCD4 and length; the perplexity increments appear in prose only.

## Terms defined in the chapter

Bold at first use, for the glossary: closed model; open-weight model; license; acceptable use policy; gated (model); model hub; model card; mixture of experts; active parameters; round-to-nearest; group (llama.cpp's block); scale; bits per weight; outliers; calibration data; post-training quantization; quantization-aware training; VRAM; unified memory; offloading; safetensors; GGUF; base model; instruct model (instruction-tuned model); runtime (inference engine); memory bandwidth. Runtime names (llama.cpp, Ollama, MLX) are bold as paragraph heads, not as glossary terms. Not re-defined: quantization (`adapting`), KV cache and prefill/decode (`generation`), perplexity (`prediction`), grouped key-value heads (`anatomy`). Not defined in the ledger's term list and not used: tokens per second as a term (used plainly), "dense" (quoted from Qwen3 only).

## Drafting notes

How the disputes were handled:
- LCD1 (what "open" means): presented Meta's usage (Llama 2 newsroom quote), the OSI's 2023 objection, OSAID 1.0's requirements, the OSI validation list (with its "not certifications" caveat), and the dispute inside the strict camp over training data. The book's own term follows D-020; Llama is never called open source in the book's voice. Zuckerberg's 2024 "first frontier-level open source AI model" quote was cut for length; Zuckerberg is quoted only for reasons to run models, flagged as an interested party.
- LCD2 (Mixtral's size): 46.7 billion (Hub, blog) and "only uses 12.9B parameters per token" (blog); the paper's "47B" appears inside its memory-cost quote.
- LCD3 (README units and sizes): all sizes computed from Hub counts and bits per weight in GB (10^9); the README's 14.96 GiB, 4.58 GiB, 32.1 GB, and 43.1 GB are used only as cross-checks, with the GiB conversion stated. The 70B and 405B 32-bit mismatches are not mentioned in the chapter.
- LCD4 (llama.cpp's perplexity and speed figures): perplexity increments given as llama.cpp's own, for Llama 3 8B (not 3.1), baseline and text unstated, not converted to percentages. The README speed table is used only as a relative pattern, with "hardware it does not state"; the reading that unpacking bits costs time is labelled as a presumption.
- LCD5 (outliers at 6.7B): "in the models they studied", OPT named, "not a law". The later work questioning emergence is not mentioned (not fetched).
- LCD6 (Gemma 3's rounded raw sizes): only the 4-bit 4B figures (2.6 GB, 7.3 GB with an 8-bit cache at 32,768 tokens) are used; the bf16 column is not.
- LCD7 (Mistral 7B context): no context length is stated for Mistral 7B.
- LCD8 (Mitchell year): cited as 2019 (`mitchell2019model`).
- LCD9 (Mixtral "same speed"): the blog's claim is quoted and followed by the paper's qualification (routing overhead, "more suitable for batched workloads").

Author decisions followed: computed memory table plus figure from the same numbers; KV cache at fixed 8K and 32K tokens in a separate small table (three models, because the ledger gives configurations only for Llama 3.1 8B/70B, Qwen3-8B, and Phi-3-mini, and Phi-3-mini's window is 4K); no working-memory allowance, stated in text and captions; tokens per second only as labelled upper bounds (dated vendor bandwidths) or as measurements with named hardware (llama-bench RTX 4080), and no machine attached to llama.cpp's first run; mixture-of-experts memory vs active reading, "8x7B" not 56B; no mention of the LLaMA weight leak; date stamps on products, licenses, Hub counts, bandwidths, and runtime defaults.

The drafter did not re-fetch sources; every claim is taken from this ledger as recorded. Interpretations in the chapter that go beyond a source and are labelled as such: the compiled-program analogy for open weights; unified memory letting a Mac hold models that do not fit consumer graphics cards (stated as "by this chapter's arithmetic"); CPU threads plateauing as consistent with a memory limit; unpacking bits as the reason speed stops improving below 4 bits; "the slowest part sets the pace" for offloading. Glosses added by the drafter without a source: KL divergence (one clause), TFLOPS as trillion operations per second, TriviaQA as "a test of trivia questions", MATH as "a test of mathematics problems", MMLU as "a broad multiple-choice test" with a pointer to `evaluation`.

Left out (sourced but cut for length, or not sourced): LLM.int8()'s speed (slightly slower than 16-bit); GPTQ's Table 6 speed-ups and group-size results beyond the 0.15-bit figure (also cut); AWQ's RTX 4090 timing figure; Llama 3 405B's FP8 details beyond one sentence; the Gemma terms' "no rights in Outputs" clause; Llama 2's "free for research and commercial use" line; the 2023 README's "Please do not make conclusions" line; Ollama's 42 GB 70B example and its GQA warning on cache quantization; DeepSeek-V3 sizes; Gemma 3's KV-cache architecture change; desktop CPU bandwidth (LC51; channel width not sourced); the M6 MacBook entries (only the M5 Max 614 GB/s is used); what "E" in Gemma 4's "E2B" means (not sourced); what "-it" in Gemma names means (not sourced). No TODO-VERIFY markers; no new bib keys.
