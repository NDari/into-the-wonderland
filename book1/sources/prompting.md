# Claim ledger: prompting

Chapter: `prompting` (Book 1, "Prompting and context").
Stage: drafted, 2026-11-11 [D-005]. Research by a helper agent; drafted by a drafting agent from this ledger; independent check pending.
Research for this chapter was done by a helper agent, before drafting. Every source below was fetched on 2026-11-11 and each claim was located in the fetched text (pdftotext, plain and `-layout`, on ACL Anthology, PMLR, TACL, and arXiv PDFs, all with text layers; HTML or the `.md` version for vendor pages, blogs, and the OWASP and NCSC pages). Tables were read in the `-layout` extraction: Wei et al. 2022 Tables 1-2 (pp. 20-21), Kojima et al. Tables 1, 2, 4, 5 (pp. 6, 8), Wang et al. Table 2 (p. 5), Liu et al. arXiv v3 Tables 2-7 (PDF pp. 17-18), Hsieh et al. Table 3 (p. 7). Two items were checked on the page image: Kalai et al. p. 13 (the confidence-target penalties, see PRD7) and Reynolds and McDonell p. 7, Figure 3 (which text is model output, see PR50). Page numbers are the printed page numbers of the source as read; the offset from PDF page to printed page is in the table. Where a source prints an en-dash or em-dash, it is written here with a hyphen or a comma. Numbers marked "checked" were recomputed in this session with a throwaway script (`prompting-scripts/arith.py` in the scratchpad, not in the repository; it reuses the GPT-2 tokenizer class of `code/checks/tokens.py` and its hash-pinned vocabulary in `out/cache/` [D-018]); they must be reproduced by `code/checks/prompting.py` at drafting [D-009].

Some sources quote prompt-injection attack strings as examples (Willison 2022, Perez and Ribeiro 2022, Wallace et al. 2024). They are recorded here only by description; the literal attack text is left out of this ledger.

## Sources and how they were read

| Key | Read from | Notes |
|---|---|---|
| `brown2020language` (existing) | https://arxiv.org/pdf/2005.14165v4 | arXiv v4 (22 Jul 2020). Printed page = PDF page. Used for pp. 6 and 34 only. |
| `kalai2025why` (existing) | https://arxiv.org/pdf/2509.04664v1 | arXiv v1 (4 Sep 2025). Printed page = PDF page. Used for pp. 2 and 13; p. 13 checked on the page image. |
| `anthropic2026contextwindows` (existing) | https://platform.claude.com/docs/en/build-with-claude/context-windows.md | Re-read this session; as of 2026-11-11. |
| `anthropic2026messages` (existing) | https://platform.claude.com/docs/en/api/messages/create.md | Re-read this session; as of 2026-11-11. |
| `min2022rethinking` | https://aclanthology.org/2022.emnlp-main.759.pdf | EMNLP 2022, pp. 11048-11064 (footer). Printed page = PDF page + 11047. arXiv v1 25 Feb 2022 (abstract page). |
| `yoo2022ground` | https://aclanthology.org/2022.emnlp-main.155.pdf | EMNLP 2022, pp. 2422-2437 (footer). Printed page = PDF page + 2421. Abstract, Fig. 1 caption, and conclusion only. |
| `wei2023larger` | https://arxiv.org/pdf/2303.03846v2 | arXiv v2 (8 Mar 2023). Printed page = PDF page. No venue printed. |
| `olsson2022context` | https://arxiv.org/pdf/2209.11895v1 | arXiv v1 (24 Sep 2022), a PDF print of the HTML article at transformer-circuits.pub; first page: "PUBLISHED Mar 8, 2022". No printed page numbers: locations are PDF pages (pp. 1-61) and section names. |
| `xie2022explanation` | https://arxiv.org/pdf/2111.02080v6 | arXiv v6 (21 Jul 2022; v1 3 Nov 2021); arXiv comment "ICLR 2022". Printed page = PDF page. |
| `vonoswald2023transformers` | https://proceedings.mlr.press/v202/von-oswald23a/von-oswald23a.pdf | ICML 2023, PMLR 202, pp. 35151-35174 (from the PMLR page metadata). The PDF prints its own page numbers 1-24; volume page = PDF page + 35150. Cite volume pages. arXiv v1 15 Dec 2022. |
| `shen2024pretrained` | https://arxiv.org/pdf/2310.08540v5 | arXiv v5 (3 Jun 2024); first page "Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria. PMLR 235, 2024". Printed page = PDF page. Abstract only. |
| `zhao2021calibrate` | https://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf | ICML 2021, PMLR 139, pp. 12697-12706 (PMLR page metadata). Volume page = PDF page + 12696. arXiv v1 19 Feb 2021. |
| `lu2022fantastically` | https://aclanthology.org/2022.acl-long.556.pdf | ACL 2022, pp. 8086-8098 (footer). Printed page = PDF page + 8085. arXiv v1 18 Apr 2021. |
| `sclar2024quantifying` (existing key, added by `evaluation`) | https://arxiv.org/pdf/2310.11324v2 | arXiv v2 (1 Jul 2024), headed "Published as a conference paper at ICLR 2024". Printed page = PDF page. |
| `reynolds2021prompt` | https://arxiv.org/pdf/2102.07350v1 | arXiv v1 (15 Feb 2021). Printed page = PDF page. Fig. 3 (p. 7) checked on the page image. |
| `nye2021show` | https://arxiv.org/pdf/2112.00114v1 | arXiv v1 (30 Nov 2021). Printed page = PDF page. Abstract only. |
| `wei2022chain` | https://arxiv.org/pdf/2201.11903v6 | arXiv v6 (10 Jan 2023; v1 28 Jan 2022); first page "36th Conference on Neural Information Processing Systems (NeurIPS 2022)". Printed page = PDF page (pp. 1-43). Figures are images; numbers taken only from text and Tables 1-2. |
| `kojima2022large` | https://arxiv.org/pdf/2205.11916v4 | arXiv v4 (29 Jan 2023; v1 24 May 2022); first page NeurIPS 2022. Printed page = PDF page. |
| `wang2023self` | https://arxiv.org/pdf/2203.11171v4 | arXiv v4 (7 Mar 2023, "camera ready version at ICLR 2023"); headed "Published as a conference paper at ICLR 2023". Printed page = PDF page. |
| `korbak2025chain` | https://arxiv.org/pdf/2507.11473v2 | arXiv v2 (7 Dec 2025; v1 15 Jul 2025). Printed page = PDF page. Section 1 and Fig. 1 only. |
| `turpin2023language` | https://arxiv.org/pdf/2305.04388v2 | arXiv v2 (9 Dec 2023); first page "37th Conference on Neural Information Processing Systems (NeurIPS 2023)". Printed page = PDF page. |
| `lanham2023measuring` | https://arxiv.org/pdf/2307.13702v1 | arXiv v1 (17 Jul 2023). Printed page = PDF page. Fig. 1 is a schematic illustration, not real model output. |
| `chen2025reasoning` | https://arxiv.org/pdf/2505.05410v1 | arXiv v1 (8 May 2025). Printed page = PDF page. |
| `willard2023efficient` | https://arxiv.org/pdf/2307.09702v4 | arXiv v4 (19 Aug 2023; v1 19 Jul 2023); title page dated 2023-07-14. Printed page = PDF page. |
| `llamacpp2026grammars` | https://raw.githubusercontent.com/ggml-org/llama.cpp/master/grammars/README.md | Master on 2026-11-11; last commit touching the file acecd56032dd (2026-09-12), from the GitHub API. Also read: pull request 1773 metadata via https://api.github.com/repos/ggml-org/llama.cpp/pulls/1773 (title "llama : add grammar-based sampling", author ejones, created 2023-06-09, merged 2023-07-24). |
| `openai2024structured` | https://openai.com/index/introducing-structured-outputs-in-the-api/ | Dated August 6, 2024 on the page. Charts are images; the text states the numbers. |
| `openai2026structured` | https://developers.openai.com/api/docs/guides/structured-outputs | As of 2026-11-11. |
| `anthropic2026structured` | https://platform.claude.com/docs/en/build-with-claude/structured-outputs.md | As of 2026-11-11. |
| `tam2024let` | https://arxiv.org/pdf/2408.02442v3 | arXiv v3 (14 Oct 2024). Abstract only. |
| `liu2024lost` (existing key, added by `tools`) | https://aclanthology.org/2024.tacl-1.9.pdf and https://arxiv.org/pdf/2307.03172v3 | TACL vol. 12, pp. 157-173 (2024); printed page = PDF page + 156. The exact per-position accuracies (Tables 5-7) and token counts (Tables 2-4) are only in arXiv v3 Appendices F-G (PDF pp. 17-18; arXiv printed page = PDF page). Same models and numbers as the TACL text where they overlap (56.1% closed-book; Table 1 values identical). |
| `hsieh2024ruler` | https://arxiv.org/pdf/2404.06654v3 | arXiv v3 (6 Aug 2024), headed "Published as a conference paper at COLM 2024". Printed page = PDF page. |
| `anthropic2025context` | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Anthropic engineering blog, "Published Sep 29, 2025"; written by Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield. Vendor blog: primary only for what the vendor says and does. |
| `anthropic2026compaction` | https://platform.claude.com/docs/en/build-with-claude/compaction.md | As of 2026-11-11. |
| `anthropic2026contextediting` | https://platform.claude.com/docs/en/build-with-claude/context-editing.md | As of 2026-11-11 (beta feature). |
| `anthropic2026memorytool` | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md | As of 2026-11-11. |
| `anthropic2026bestpractices` | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices.md | As of 2026-11-11 (the system-prompts URL redirects here). |
| `anthropic2026models` (existing key, added by `tools`) | https://platform.claude.com/docs/en/models/overview.md | As of 2026-11-11. The bib entry's URL (/about-claude/models/overview) redirects here. |
| `openai2026text` | https://developers.openai.com/api/docs/guides/text | As of 2026-11-11. |
| `openai2026conversation` | https://developers.openai.com/api/docs/guides/conversation-state | As of 2026-11-11. |
| `openai2026compaction` | https://developers.openai.com/api/docs/guides/compaction | As of 2026-11-11. |
| `openai2026modelspec` | https://model-spec.openai.com/2026-10-29.html | The undated URL redirects to this version "Model Spec (2026/10/29)". |
| `wallace2024instruction` | https://arxiv.org/pdf/2404.13208v1 | arXiv v1 (19 Apr 2024). OpenAI. Abstract and introduction only. |
| `willison2022prompt` | https://simonwillison.net/2022/Sep/12/prompt-injection/ | Blog post dated 12 September 2022. Used only as a first-hand account by the person who named the attack (see PR42). |
| `perez2022ignore` | https://arxiv.org/pdf/2211.09527v1 | arXiv v1 (17 Nov 2022); first page "ML Safety Workshop, 36th Conference on Neural Information Processing Systems (NeurIPS 2022)". Printed page = PDF page. |
| `greshake2023not` (existing key, added by `tools`; venue AISec '23 per its bib note) | https://arxiv.org/pdf/2302.12173v2 | arXiv v2 (5 May 2023; v1 23 Feb 2023). Printed page = PDF page. |
| `owasp2025llm01` | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | Page metadata: published 2024-04-10, modified 2025-04-17. The site menu lists "LLM TOP 10 FOR 2025" and "LLM TOP 10 FOR 2023/24" (no newer list) as of 2026-11-11. |
| `ncsc2025prompt` | https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection | UK National Cyber Security Centre blog, by Dave Chismon; datePublished 2025-12-08 in the page's structured data. A government security agency: authoritative secondary for security framing. |
| `openai2025promptinjections` | https://openai.com/index/prompt-injections/ | Dated November 7, 2025 on the page. |
| `openai2025atlas` | https://openai.com/index/hardening-atlas-against-prompt-injection/ | Dated December 22, 2025 on the page. |
| `anthropic2025promptinjection` | https://www.anthropic.com/research/prompt-injection-defenses | "Published Nov 24, 2025". The chart is an image; text only. |

### Not fetched

- Akyürek et al. (2023), "What learning algorithm is in-context learning? Investigations with linear models" (ICLR 2023), and Dai et al. (2022): further gradient-descent accounts, known only as cited by `wei2023larger` p. 1. Not needed beyond `vonoswald2023transformers`.
- Chan et al. (2022), "Data distributional properties drive emergent few-shot learning in transformers": only as a reference in `wei2023larger`.
- Elhage et al. (2021), "A Mathematical Framework for Transformer Circuits" (existing key `elhage2021mathematical`): not re-read. `olsson2022context` (p. 2) says the induction head was found there ("in our prior work ... Perhaps the most interesting finding was the induction head"). If the chapter credits 2021 for the first description, cite Olsson et al. p. 2 for that statement, or re-read Elhage et al.
- Cobbe et al. (2021), GSM8K and the finetuned GPT-3 plus verifier (55%): known only through `wei2022chain` (pp. 2, 20) and `wang2023self` (p. 5).
- Pfau et al. (2024), "Let's think dot by dot" (filler tokens can help in some setups): a lead only; not fetched. The chapter should state only what Wei et al. and Lanham et al. found (PR16, PR22).
- The ".txt" response of Outlines' authors to Tam et al. (a dottxt blog post, late 2024, "Say what you mean"): not fetched; see PRD8.
- Debenedetti et al. (2025), CaMeL ("Defeating prompt injections by design"), and its follow-up on design patterns: named by `ncsc2025prompt` as "one of the first major publications on mitigating prompt injection through design"; not fetched. Belongs to `tools` if anywhere.
- Riley Goodside's September 2022 posts on X/Twitter: known only as quoted by `willison2022prompt`. Not fetched (social media).
- OpenAI DevDay November 2023 announcement of JSON mode: known only through `openai2024structured` ("Last year at DevDay, we introduced JSON mode").
- Poesia et al. (2022), Scholak et al. (2021, PICARD), Microsoft's Guidance: earlier constrained generation, known only as citations in `willard2023efficient` p. 1.
- Any published version of `tam2024let` or `reynolds2021prompt`: not checked. (`greshake2023not`'s AISec '23 venue is recorded in references.bib from Crossref by the `tools` research; the workshop text was not read here.)
- The Hugging Face or Meta chat-template documentation showing a system prompt as tokens: left to `instructions`.

## Sourced claims

### A. In-context learning revisited

### PR1. GPT-3's few-shot setting was bounded by the window; "learn or recognize" was left open
- Source: `brown2020language`
- Location: p. 6; p. 34.
- Quotes: p. 6: "We typically set K in the range of 10 to 100 as this is how many examples can fit in the model's context window (nctx = 2048)." p. 34: "A limitation, or at least uncertainty, associated with few-shot learning in GPT-3 is ambiguity about whether few-shot learning actually learns new tasks "from scratch" at inference time, or if it simply recognizes and identifies tasks that it has learned during training."
- Note: `scale` already defines zero-, one-, few-shot and quotes "no gradient updates" (p. 5) and the open question (p. 4). This chapter picks up the p. 34 wording as the hinge for section A; do not redefine the settings.

### PR2. "Task location" rather than learning (Reynolds and McDonell, 2021)
- Source: `reynolds2021prompt`
- Location: p. 1.
- Quotes: abstract: "Using GPT-3 as a case study, we show that 0-shot prompts can significantly outperform few-shot prompts. We suggest that the function of few-shot examples in these cases is better described as locating an already learned task rather than meta-learning." Intro: "GPT-3 is often not actually learning the task during run time from few-shot examples. Rather than instruction, the method's primary function is task location in the model's existing space of learned tasks."
- Note: an arXiv preprint by two independent researchers; an early, influential framing (cited by `min2022rethinking` p. 11055 and by `korbak2025chain` p. 2). Present as a hypothesis.

### PR3. Random labels barely hurt (Min et al., 2022)
- Source: `min2022rethinking`
- Location: pp. 11048-11051, 11055-11056.
- Quotes: abstract (p. 11048): "we show that ground truth demonstrations are in fact not required, randomly replacing labels in the demonstrations barely hurts performance on a range of classification and multi-choce tasks, consistently over 12 different models including GPT-3. Instead, we find that other aspects of the demonstrations are the key drivers of end task performance, including the fact that they provide a few examples of (1) the label space, (2) the distribution of the input text, and (3) the overall format of the sequence." (source prints an em-dash after "required"; "multi-choce" is the source's typo). Setup (p. 11050): "We use k = 16 examples as demonstrations by default". Size of the effect (p. 11051): "models see performance drop in the range of 0-5% absolute. There is less impact in replacing labels in multi-choice tasks (1.7% on average) than in classification tasks (2.6% absolute)." (source prints an en-dash in 0-5%). Interpretation (p. 11051): "This strongly suggests that the models are capable of recovering the expected input-label correspondence for the task; however, it is not directly from the pairings in the demonstrations."
- On "learning" (p. 11055): "If we take a strict definition of learning: capturing the input-label correspondence given in the training data, then our findings suggest that LMs do not learn new tasks at test time. Our analysis shows that the model may ignore the task defined by the demonstrations and instead use prior from pretraining. However, learning a new task can be interpreted more broadly: it may include adapting to specific input and label distributions and the format suggested by the demonstrations ... With this definition of learning, the model does learn the task from the demonstrations." Also (p. 11055): the model "has learned the (implicit notion of) input-label correspondence from the language modeling objective alone, e.g., associating a positive review with the word 'positive'", in line with Reynolds and McDonell's task location.
- Example demonstration (Fig. 2, p. 11049): financial-news sentences labelled Positive, Neutral, Negative (k = 3 in the figure).
- Limitation (p. 11056): "Synthetic tasks with more limited inputs may actually use the ground truth labels more". Models (Table 1, p. 11049): GPT-2 Large (774M), MetaICL (774M), GPT-J (6B), fairseq 6.7B and 13B, GPT-3 (175B, "the Davinci API (the base version, not the instruct version)").

### PR4. Labels can matter more than the averages show (Yoo et al., 2022)
- Source: `yoo2022ground`
- Location: p. 2422 (abstract, Fig. 1 caption); p. 2430 (conclusion).
- Quotes: abstract: "we find that the correct input-label mappings can have varying impacts on the downstream in-context learning performances, depending on the experimental configuration ... we identify key components, such as the verbosity of prompt templates and the language model size, as the controlling factor". Fig. 1 caption: "A demonstration of cases where the effect of the ground-truth label in in-context learning is much more significant than the aggregated results reported by Min et al. (2022b)." Conclusion (p. 2430): "we found that the integrity of the input-label mapping is a crucial factor in performing ICL."

### PR5. Larger models can follow flipped labels (Wei et al., 2023)
- Source: `wei2023larger`
- Location: pp. 1, 4, 7.
- Quotes: abstract (p. 1): "experiments on ICL with flipped labels show that overriding semantic priors is an emergent ability of model scale. While small language models ignore flipped labels presented in-context and thus rely primarily on semantic priors from pretraining, large models can override semantic priors when presented with in-context exemplars that contradict priors". Also: "instruction tuning strengthens both the use of semantic priors and the capacity to learn input-label mappings, but more of the former." Number (p. 4): "text-davinci-002 performance drops from 90.3% with 0% flipped labels to just 22.5% with 100% flipped labels". Small models (p. 4): "do not flip their predictions and thus are unable to override semantic priors (consistent with Min et al. (2022b))".
- Note: "semantically-unrelated labels" (foo/bar for negative/positive) is their second test (p. 1). Same lab and overlapping authors as `wei2022chain` and `wei2022emergent`; uses "emergent" in the sense of `scale`.

### PR6. The Bayesian account (Xie et al., 2021-2022)
- Source: `xie2022explanation`
- Location: pp. 1-2.
- Quotes: abstract (p. 1): "we study how in-context learning can emerge when pretraining documents have long-range coherence. Here, the LM must infer a latent document-level concept to generate coherent next tokens during pretraining. At test time, in-context learning occurs when the LM also infers a shared latent concept between examples in a prompt." Evidence is on synthetic data: "we generate a small-scale synthetic dataset (GINC) where Transformers and LSTMs both exhibit in-context learning", which reproduces "improved in-context performance with model scaling (despite the same pretraining loss), sensitivity to example order, and instances where zero-shot is better than few-shot in-context learning." Example (p. 1): the prompt "Albert Einstein was German \n Mahatma Gandhi was Indian \n Marie Curie was", for which GPT-3 places the largest probability on "Polish". Fig. 1 caption (p. 2): Wikipedia biographies "typically transition between name (Albert Einstein) to nationality (German) to occupation (physicist)" (arrows written out).
- The model (p. 2): "To generate a document, we first draw a latent concept θ, which parameterizes the transitions of a Hidden Markov Model (HMM) ... This latent variable structure is common in topic models such as LDA". Equation (1), p. 2: p(output | prompt) = ∫ p(output | concept, prompt) p(concept | prompt) d(concept), "the posterior predictive distribution", which "marginalizes out the latent concepts". The analysis assumes "the LM fits the pretraining distribution p exactly".
- Bridge (the paper's own): LDA topic models, which the 2000s reader may know.

### PR7. The gradient-descent account (von Oswald et al., 2022-2023)
- Source: `vonoswald2023transformers`
- Location: p. 35151 (abstract and contributions).
- Quotes: abstract: "We start by providing a simple weight construction that shows the equivalence of data transformations induced by 1) a single linear self-attention layer and by 2) gradient-descent (GD) on a regression loss. Motivated by that construction, we show empirically that when training self-attention-only Transformers on simple regression tasks either the models learned by GD and Transformers show great similarity or, remarkably, the weights found by optimization match the construction. Thus we show how trained Transformers become mesa-optimizers i.e. learn models by gradient descent in their forward pass. This allows us, at least in the domain of regression problems, to mechanistically understand the inner workings of in-context learning in optimized Transformers." Also: "as of today the exact mechanisms of how it works are not fully understood".
- Scope: linear regression tasks, small self-attention-only models trained for this purpose; not pretrained LLMs. The abstract connects the result to induction heads.

### PR8. The gradient-descent account questioned for real LLMs (Shen et al., 2023-2024)
- Source: `shen2024pretrained`
- Location: p. 1 (abstract).
- Quotes: "We highlight the limiting assumptions in prior works that make their setup considerably different from the practical setup in which language models are trained. For example, their experimental verification uses ICL objective (training models explicitly for ICL), which differs from the emergent ICL in the wild." "We observe that ICL and GD have different sensitivity to the order in which they observe demonstrations." On LLaMa-7B: "We observe that ICL and GD modify the output distribution of language models differently. These results indicate that the equivalence between ICL and GD remains an open hypothesis and calls for further studies."

### PR9. Induction heads (Olsson et al., 2022)
- Source: `olsson2022context`
- Location: PDF pp. 1-4, 6-7, 9, 15, 19-20, 29, 40 (abstract; introduction; "Key Concepts"; Arguments 1-6; model tables).
- Definition (p. 1, abstract): "'Induction heads' are attention heads that implement a simple algorithm to complete token sequences like [A][B] ... [A] to [B]" (arrow written out). Mechanism (p. 2): "the first head is a 'previous token head' which copies information from the previous token into the next token, while the second head (the actual 'induction head') uses that information to find tokens preceded by the present token." First described in their prior work (p. 2): "in our prior work ... Perhaps the most interesting finding was the induction head".
- Claim and its strength (p. 1): "we present preliminary and indirect evidence for a hypothesis that induction heads might constitute the mechanism for the majority of all 'in-context learning' in large transformer models ... For small attention-only models, we present strong, causal evidence; for larger models with MLPs, we present correlational evidence."
- Fuzzy version (p. 2): circuits that complete "[A*][B*] ... [A] to [B], where A* ≈ A and B* ≈ B are similar in some space"; p. 6: they may "translate a sentence word by word"; "We are not yet able to prove mechanistically that induction heads do this in general".
- Measure (p. 4): "In-context learning score: the loss of the 500th token in the context minus the average loss of the 50th token in the context, averaged over dataset examples. We chose the 500th and 50th token indices somewhat arbitrarily."
- Phase change (p. 9): in-context learning "develops abruptly in a narrow window early in training (roughly 2.5 to 5 billion tokens) and then is constant for the rest of training ... Before this window there is less than 0.15 nats of in-context learning, after it there is roughly 0.4 nats", constant "across many different model sizes (except for the one layer model where not much in-context learning ever forms)". Six arguments listed on p. 3 (co-occurrence, co-perturbation, direct ablation, examples, mechanistic plausibility, continuity).
- Caveat (p. 15): "perhaps the co-occurrence is primarily caused by a shared latent variable, rather than direct causality from induction heads to the full observed change in in-context learning."
- Model sizes: up to "40 layers and 13B parameters" (p. 29; table p. 40 gives non-embedding parameters 13M to 13B); see PRD7 for a 12B/13B wording inconsistency (p. 19).
- Note: "nats" is loss measured with natural logarithms; `prediction` or `training` may already define loss in bits or nats. Use the 0.15 and 0.4 only if the unit is explained, or say "the loss on late tokens fell well below the loss on early tokens".

### B. Sensitivity to wording, order, and format

### PR10. Accuracy swings with format, examples, and order (Zhao et al., 2021)
- Source: `zhao2021calibrate`
- Location: pp. 12697-12699, 12701.
- Quotes: abstract (p. 12697): "We show that this type of few-shot learning can be unstable: the choice of prompt format, training examples, and even the order of the training examples can cause accuracy to vary from near chance to near state-of-the-art. We demonstrate that this instability arises from the bias of language models towards predicting certain answers, e.g., those that are placed near the end of the prompt or are common in the pretraining data." Example prompt (p. 12697), two training examples then a test input: "Input: Subpar acting. Sentiment: Negative / Input: Beautiful film. Sentiment: Positive / Input: Amazing. / Sentiment:" (line breaks shown as slashes). The three biases (p. 12697): "majority label bias, recency bias, and common token bias".
- The number (p. 12699): "Figure 2 shows the results for SST-2 (4-shot, GPT-3 2.7B) ... varying the permutation of the training examples can cause accuracy to go from near chance (54.3%) to near state-of-the-art (93.4%) ... This high importance on example order is in contrast to standard machine learning, where the ordering of examples during training is typically an afterthought." And: "The variance remains high even when we use 16 training examples."
- The fix (p. 12698): "if we replace 'Amazing.' with the string 'N/A', the model predicts 62% Positive. We then fit the calibration parameters so that the content-free input has uniform scores for each answer." Gains "up to 30.0% absolute" (p. 12697). Models (p. 12699): GPT-3 2.7B, 13B, 175B and GPT-2 1.5B.
- Note: "calibration" here means correcting a biased output distribution; `generation` used "calibrated" for confidence matching accuracy. Different senses: the drafter must say so.

### PR11. Order alone: 24 orderings of four examples (Lu et al., 2022)
- Source: `lu2022fantastically`
- Location: pp. 8086-8088.
- Quotes: abstract (p. 8086): "the order in which the samples are provided can make the difference between near state-of-the-art and random guess performance: essentially some permutations are 'fantastic' and some not ... it is present across model sizes (even for the largest current models), it is not related to a specific subset of samples, and that a given good permutation for one model is not transferable to another." Setup (p. 8087): "a fixed random subset of four samples with a balanced label distribution from the SST-2 dataset and consider all 24 possible sample order permutations"; models GPT-2 (0.1B-1.5B) and GPT-3 (2.7B-175B). Result (p. 8087): "some permutations have comparable performance (over 85% accuracy) to supervised training for sentiment classification, while others perform close to random (around 50%)"; "increasing the model size somewhat addresses it" but not for Subj. p. 8088: "there can be up to 64! possible orders" (for larger sets of examples). Their selection method gives "13% relative improvement" (p. 8086).
- Note on priority: Lu et al. write (p. 8086) "to the best of our knowledge, no work has studied the effect of the sample ordering"; their arXiv v1 (18 Apr 2021) came two months after Zhao et al.'s (19 Feb 2021), which already reported order effects. Near-simultaneous; see PRD5.

### PR12. Formatting alone: up to 76 points (Sclar et al., 2023-2024)
- Source: `sclar2024quantifying`
- Location: pp. 1-2, 8.
- Quotes: abstract (p. 1): "several widely used open-source LLMs are extremely sensitive to subtle changes in prompt formatting in few-shot settings, with performance differences of up to 76 accuracy points when evaluated using LLaMA-2-13B. Sensitivity remains even when increasing model size, the number of few-shot examples, or performing instruction tuning." Intro (p. 1): "∼10 accuracy points on average across 50+ tasks and several models". Abstract: "format performance only weakly correlates between models, which puts into question the methodological validity of comparing models with an arbitrarily chosen, fixed prompt format."
- Figure 1 (p. 2): the same task (1-shot LLaMA-2-7B, a SuperNaturalInstructions classification task) with formats differing only in separator, spacing, and casing ("Passage:<text> Answer:<text>" vs "PASSAGE <text> ANSWER <text>" and others) spans accuracy 0.036 to 0.804.
- GPT-3.5 (p. 2): "a spread up to 56 accuracy points with a median spread of 6.4 accuracy points with GPT3.5 across 320 formats and 53 tasks"; p. 8 gives the same as "median spread of 0.064 ... maximum spread of 0.562".
- Hand-off: `evaluation` (benchmark scores depend on the prompt format).

### PR13. Wording of the "think" sentence matters (Kojima et al., Table 4)
- Source: `kojima2022large`
- Location: p. 8, Table 4 (MultiArith, text-davinci-002).
- Numbers: "Let's think step by step." 78.7; "First," 77.3; "Let's think about this logically." 74.5; "Let's solve this problem by splitting it into steps." 72.2 (marked as the template of Reynolds and McDonell, "not quantitatively evaluated" there); "Let's think" 57.5; "Don't think. Just feel." 18.8; "Let's think step by step but reach an incorrect answer." 18.7; "Abrakadabra!" 15.5; "It's a beautiful day." 13.1; "By using the fact that the earth is round," 9.3; no trigger (zero-shot) 17.7. Text: "the performance is improved if the text is written in a way that encourages chain of thought reasoning ... However, the difference in accuracy is significant depending on the sentence."

### C. Chain of thought

### PR14. Scratchpads (Nye et al., November 2021)
- Source: `nye2021show`
- Location: p. 1.
- Quotes: models "struggle with tasks that require unbounded multi-step computation, such as adding integers ... Surprisingly, we find that these same models are able to perform complex multi-step computations, even in the few-shot regime, when asked to perform the operation 'step by step', showing the results of intermediate computations. In particular, we train Transformers to perform multi-step computations by asking them to emit intermediate computation steps into a 'scratchpad'." (source prints em-dashes around "even in the few-shot regime")
- Note: mostly with training (fine-tuning) on scratchpad data; a predecessor that `turpin2023language` p. 1 cites alongside Wei et al. as the origin of CoT ("CoT; Nye et al., 2021; Wei et al., 2022").

### PR15. Chain-of-thought prompting (Wei et al., 2022): definition and headline
- Source: `wei2022chain`
- Location: pp. 1-5, 20-21.
- Definition (p. 1): "a chain of thought, a series of intermediate reasoning steps" (source uses an em-dash). Method (p. 3): "augment each exemplar in few-shot prompting with a chain of thought for an associated answer ... we manually composed a set of eight few-shot exemplars with chains of thought for prompting ... (These particular exemplars did not undergo prompt engineering ...)". Headline (p. 1): "prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier."
- Printed example (Fig. 1, p. 1), usable as real model output [D-009]: exemplar "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now? A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11." Test question: "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?" Standard prompting output: "A: The answer is 27." Chain-of-thought output: "A: The cafeteria had 23 apples originally. They used 20 to make lunch. So they had 23 - 20 = 3. They bought 6 more apples, so they have 3 + 6 = 9. The answer is 9."
- GSM8K numbers (Table 1, p. 20; accuracy %): prior best 55 (finetuning; Cobbe et al. 2021). PaLM 540B: standard 17.9, chain of thought 56.9 (+39.0), with an external calculator 58.6. GPT-3 175B (text-davinci-002): 15.6, 46.9. Codex (code-davinci-002): 19.7, 63.1. LaMDA 137B: 6.5, 14.3. UL2 20B: 4.1, 4.4.
- Scale (Table 2, p. 21, GSM8K standard / CoT): LaMDA 420M 2.6 / 0.4; 2B 3.6 / 1.9; 8B 3.2 / 1.6; 68B 5.7 / 8.2; 137B 6.5 / 14.3. GPT 350M 2.2 / 0.5; 1.3B 2.4 / 0.5; 6.7B 4.0 / 2.4; 175B 15.6 / 46.9. PaLM 8B 4.9 / 4.1; 62B 9.6 / 29.9; 540B 17.9 / 56.9. Text (p. 4): "chain-of-thought prompting does not positively impact performance for small models, and only yields performance gains when used with models of ∼100B parameters. We qualitatively found that models of smaller scale produced fluent but illogical chains of thought, leading to lower performance than standard prompting." They call it "an emergent ability of model scale" (p. 4), citing `wei2022emergent`.
- Robustness (p. 6): chains written by three different co-authors and three sets of exemplars sampled from GSM8K training data all beat standard prompting "by a large margin"; "successful use of chain of thought does not depend on a particular linguistic style."

### PR16. Why chain of thought helps: Wei et al.'s ablations
- Source: `wei2022chain`
- Location: p. 6 (Fig. 5, LaMDA 137B and PaLM 540B).
- Quotes: "Equation only ... does not help much for GSM8K". "Variable compute only. Another intuition is that chain of thought allows the model to spend more computation (i.e., intermediate tokens) on harder problems. To isolate the effect of variable computation from chain-of-thought reasoning, we test a configuration where the model is prompted to output a only sequence of dots (. . .) equal to the number of characters in the equation needed to solve the problem. This variant performs about the same as the baseline". "Chain of thought after answer ... performs about the same as the baseline, which suggests that the sequential reasoning embodied in the chain of thought is useful for reasons beyond just activating knowledge."
- Limitations (p. 9): "although chain of thought emulates the thought processes of human reasoners, this does not answer whether the neural network is actually 'reasoning,' which we leave as an open question"; "there is no guarantee of correct reasoning paths"; "the emergence of chain-of-thought reasoning only at large model scales makes it costly to serve".

### PR17. Zero-shot chain of thought: "Let's think step by step" (Kojima et al., 2022)
- Source: `kojima2022large`
- Location: pp. 1, 3-4, 6-8.
- Quotes: abstract (p. 1): "we show that LLMs are decent zero-shot reasoners by simply adding 'Let's think step by step' before each answer ... increasing the accuracy on MultiArith from 17.7% to 78.7% and GSM8K from 10.4% to 40.7% with large-scale InstructGPT model (text-davinci-002), as well as similar magnitudes of improvements with another off-the-shelf large model, 540B parameter PaLM."
- Two steps (pp. 3-4): "it uses prompting twice to extract both reasoning and answer": first "Q: [X]. A: Let's think step by step.", then the generated text plus an answer-extraction phrase such as "Therefore, the answer (arabic numerals) is" (Fig. 2, p. 4). Greedy decoding throughout (p. 4).
- Table 2 (p. 6; MultiArith / GSM8K, text-davinci-002): zero-shot 17.7 / 10.4; few-shot (8 samples) 33.8 / 15.6; zero-shot-CoT 78.7 / 40.7; few-shot-CoT (8 samples) 93.0 / 48.7. PaLM 540B: zero-shot 25.5 / 12.5; zero-shot-CoT 66.1 / 43.0; zero-shot-CoT + self-consistency 89.0 / 70.1.
- Scale (p. 7): "When the model size is smaller, chain of thought reasoning is not effective." Commonsense (p. 6): "In commonsense reasoning tasks, Zero-shot-CoT does not provide performance gains" (Table 1: CommonsenseQA 68.8 zero-shot vs 64.6 zero-shot-CoT). Errors (p. 8): "Zero-shot-CoT tends to output unnecessary steps of reasoning after getting the correct prediction, which results in changing the prediction to incorrect one."
- Wording sensitivity: PR13.

### PR18. Self-consistency: sample many chains, take a vote (Wang et al., 2022-2023)
- Source: `wang2023self`
- Location: pp. 1, 3, 5, 9.
- Quotes: abstract (p. 1): "we propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths ... GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%)." Aggregation (p. 3): "taking a majority vote" over final answers; it gives "a very similar accuracy as aggregating using the 'normalized weighted sum'". Setup (p. 5): "averaged over 10 runs, where we sampled 40 outputs independently from the decoder in each run."
- Table 2 (p. 5, GSM8K): PaLM-540B CoT 56.5, self-consistency 74.4 (+17.9); code-davinci-002 60.1 to 78.0 (+17.9); LaMDA-137B 17.1 to 27.7; UL2-20B 4.1 to 7.3.
- Cost (p. 9): "One limitation of self-consistency is that it incurs more computation cost. In practice people can try a small number of paths (e.g., 5 or 10) as a starting point to realize most of the gains".
- Link: uses sampling with temperature, from `generation`.

### PR19. A mechanism for why writing steps helps (Korbak et al., 2025)
- Source: `korbak2025chain`
- Location: p. 2 (Section 1.1 and Fig. 1).
- Quotes: "A key requirement for such capabilities is working memory: a storage system for intermediate reasoning outputs that allows for further reasoning and manipulation of the stored information. In the popular Transformer architecture ... any sufficiently long chain of serial steps of cognition must pass through the chain of thought at some point". Fig. 1 caption: "Chain of thought is the only way that information can flow down from later to earlier layers. As a result, for a fixed amount of tokens, the longest flows of information must use the chain of thought, and many information flows are impossible without it." Also (p. 2): "Necessity to think out loud. On some tasks, models need to externalize their reasoning because they are unable to complete the task without CoT."
- Note: a position paper by 41 authors from Anthropic, OpenAI, Google DeepMind, the UK AI Security Institute, and others; "The paper represents the views of the individual authors". The mechanism is an architectural argument (each token gets a fixed number of layers; a generated token is fed back in at the bottom), consistent with `anatomy` and `generation`. It is the best mechanistic hook for this section; present it as an explanation, and pair it with PR16's finding that dots alone did not help.

### D. Is the chain of thought the model's reasoning?

### PR20. Unfaithful explanations (Turpin et al., 2023)
- Source: `turpin2023language`
- Location: pp. 1-3, 5.
- Quotes: abstract (p. 1): "we find that CoT explanations can systematically misrepresent the true reason for a model's prediction. We demonstrate that CoT explanations can be heavily influenced by adding biasing features to model inputs, e.g., by reordering the multiple-choice options in a few-shot prompt to make the answer always '(A)', which models systematically fail to mention in their explanations. When we bias models toward incorrect answers, they frequently generate CoT explanations rationalizing those answers. This causes accuracy to drop by as much as 36% on a suite of 13 tasks from BIG-Bench Hard, when testing with GPT-3.5 from OpenAI and Claude 1.0 from Anthropic." (source prints em-dashes around the "e.g." clause). Second bias (p. 2): "Suggested Answer, where the prompt suggests that a specific answer choice might be correct". p. 3: "we review 426 explanations supporting biased predictions and only 1 explicitly mentions the bias". Findings (p. 2): "In some instances, these unfaithful explanations still exhibit sound reasoning." Conclusion (p. 1): "Building more transparent and explainable systems will require either improving CoT faithfulness through targeted efforts or abandoning CoT in favor of alternative methods."
- Decoding (p. 5): GPT-3.5 at temperature 0.7, Claude 1.0 at temperature 1.
- Term: "faithful" explanations accurately represent "the reasons behind model predictions" (p. 1, citing Jacovi and Goldberg 2020).

### PR21. Faithfulness varies by task and gets worse with size (Lanham et al., 2023)
- Source: `lanham2023measuring`
- Location: pp. 1-2, 7.
- Quotes: abstract (p. 1): "Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT's performance boost does not seem to come from CoT's added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen." Filler tokens (p. 2): "we find no accuracy gain from CoT when we replace the CoT with uninformative filler text (all periods)". Size (p. 7): "For 7/8 tasks, the 13B parameter model changes its answer after CoT more often than the 175B model does ... indicating inverse scaling in model size for reasoning faithfulness on these tasks."
- Tests (Fig. 1, p. 1): early answering (truncate the chain), adding mistakes, paraphrasing, filler tokens. The Fig. 1 example (5! = 120) is a schematic, not a measured output.
- Model (p. 2): "a 175B-parameter pretrained, decoder-only transformer ... fine-tuned to be a helpful dialog assistant using reinforcement learning from human feedback". Authors at Anthropic.

### PR22. Reasoning models, 2025: hints used but rarely mentioned (Chen et al., 2025)
- Source: `chen2025reasoning`
- Location: pp. 1, 6.
- Quotes: abstract (p. 1): "for most settings and models tested, CoTs reveal their usage of hints in at least 1% of examples where they use the hint, but the reveal rate is often below 20%". p. 6: "The overall faithfulness scores for both reasoning models remain low (25% for Claude 3.7 Sonnet and 39% for DeepSeek R1)". Abstract: "CoT monitoring is a promising way of noticing undesired behaviors during training and evaluations, but ... it is not sufficient to rule them out."
- Date stamp: models as of early 2025. Hand-off: reasoning models belong to `frontier`.

### E. Structured output

### PR23. Guided generation as masking the next-token distribution (Willard and Louf, 2023)
- Source: `willard2023efficient`
- Location: pp. 1, 4.
- Quotes: abstract (p. 1): "we show how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine. This framework leads to an efficient approach to guiding text generation with regular expressions and context-free grammars by allowing the construction of an index over a language model's vocabulary ... enables the construction of reliable interfaces by guaranteeing the structure of the generated text. It adds little overhead". Mechanism (p. 4): "we can compute an un-normalized conditional distribution by applying a boolean mask ... that restricts the support of the original distribution"; masks can enforce "digit samples", a regular expression, or "strings that parse according to a specified grammar (e.g. Python, SQL, etc.)". Implementation: "the open source Python library Outlines" (p. 1). Earlier work is cited on p. 1 (Scholak et al. 2021, Poesia et al. 2022, Microsoft's Guidance, and others).
- Bridge: the mask is the same "cut and rescale" as top-k and top-p in `generation`, with the allowed set chosen by a grammar instead of by probability.

### PR24. Grammars in llama.cpp (2023 to now)
- Source: `llamacpp2026grammars`
- Location: README sections "GBNF Guide", "JSON Schemas to GBNF" (arrow written out); PR 1773 metadata.
- Quotes: "GBNF (GGML BNF) is a format for defining formal grammars to constrain model outputs in llama.cpp. For example, you can use it to force the model to generate valid JSON, or speak only in emojis." "llama.cpp supports converting a subset of https://json-schema.org/ to GBNF grammars". Note box: "The JSON schema is only used to constrain the model output and is not injected into the prompt. The model has no visibility into the schema, so if you want it to understand the expected structure, describe it explicitly in your prompt. This does not apply to tool calling, where schemas are injected into the prompt." Troubleshooting: "Grammars currently have performance gotchas".
- History: pull request 1773, "llama : add grammar-based sampling" by ejones, opened 2023-06-09, merged 2023-07-24 (GitHub API); its description: "this adds an API that takes a serialized context-free grammar to guide and constrain sampling."
- Date stamp: README as of 2026-11-11 (commit acecd56032dd). Book 2 pins its own llama.cpp version [D-007].

### PR25. Vendor structured outputs: JSON mode vs schema guarantees (OpenAI, 2024)
- Source: `openai2024structured`
- Location: the page (dated August 6, 2024), sections "Introducing", "Under the hood", "Constrained decoding", "Alternate approaches".
- Quotes: "Last year at DevDay, we introduced JSON mode ... While JSON mode improves model reliability for generating valid JSON outputs, it does not guarantee that the model's response will conform to a particular schema." "On our evals of complex JSON schema following, our new model gpt-4o-2024-08-06 with Structured Outputs scores a perfect 100%. In comparison, gpt-4-0613 scores less than 40%." Training alone was not enough: "despite this model's performance improvements (93% on our benchmark), it still did not meet the reliability that developers need ... So we also took a deterministic, engineering-based approach to constrain the model's outputs to achieve 100% reliability." Mechanism: "By default, when models are sampled to produce outputs, they are entirely unconstrained and can select any token from the vocabulary as the next output ... In order to force valid outputs, we constrain our models to only tokens that would be valid according to the supplied schema"; "we convert the supplied JSON Schema into a context-free grammar (CFG)". On alternatives: "Alternate approaches to this problem often use finite state machines (FSMs) or regexes ... FSMs cannot generally express recursive types".
- Note: a vendor's own evaluation ("our evals"); report as OpenAI's claim, dated 2024.

### PR26. Vendor structured outputs as of 2026-11 (OpenAI and Anthropic)
- Sources: `openai2026structured`; `anthropic2026structured`; `anthropic2026bestpractices`; `anthropic2026messages`.
- OpenAI (as of 2026-11-11): "Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema". "Structured Outputs is the evolution of JSON mode. While both ensure valid JSON is produced, only Structured Outputs ensure schema adherence." JSON mode warning: "When using JSON mode, you must always instruct the model to produce JSON via some message in the conversation ... If you don't include an explicit instruction to generate JSON, the model may generate an unending stream of whitespace and the request may run continually until it reaches the token limit."
- Anthropic (as of 2026-11-11): "Structured outputs guarantee schema-compliant responses through constrained decoding". "Structured outputs use constrained sampling with compiled grammar artifacts"; first use of a schema adds latency "while the grammar compiles"; "Compiled grammars are cached for 24 hours from last use". Unlike llama.cpp (PR24), the schema is described to the model: "When using structured outputs, Claude automatically receives an additional system prompt explaining the expected output format." Exceptions ("Invalid outputs"): refusals ("the refusal message takes precedence over schema constraints"); "stop_reason: 'max_tokens'" ("The output might be incomplete and not match your schema"); enum casing ("Structured outputs don't guarantee the capitalization of string enum and const values").
- Prefill (as of 2026-11-11): the Messages API defines prefill: "If the final message uses the assistant role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response" (`anthropic2026messages`). The best-practices page: "Starting with Claude 4.6 models ... prefilled responses ... on the last assistant turn are no longer supported", and "Prefills have been used to force specific output formats such as JSON/YAML", now replaced by structured outputs (`anthropic2026bestpractices`, "Migrating away from prefilled responses").

### PR27. Format restrictions may cost reasoning quality (Tam et al., 2024)
- Source: `tam2024let`
- Location: p. 1 (abstract).
- Quotes: "we observe a significant decline in LLMs' reasoning abilities under format restrictions. Furthermore, we find that stricter format constraints generally lead to greater performance degradation in reasoning tasks."
- Note: one study, disputed in public by constrained-decoding developers (lead only, not fetched); see PRD8. Present as "one 2024 study found".

### F. The context window as short-term memory, and managing it

### PR28. The window is the model's working memory; everything counts (vendor docs, as of 2026-11)
- Sources: `anthropic2026contextwindows`; `openai2026conversation`; `anthropic2026messages`.
- Anthropic: "The 'context window' refers to all the text a language model can reference when generating a response, including the response itself. This is different from the large corpus of data the language model was trained on, and instead represents a 'working memory' for the model." "Everything in the request counts toward the context window: the system prompt, every message in messages (including tool results, images, and documents), and your tool definitions. The output Claude generates for the turn, including its extended thinking, counts too." "As the conversation advances through turns, each user message and assistant response accumulates within the context window, and previous turns are preserved completely." Sizes: the listed current models "have a 1M-token context window"; "Other Claude models, including Claude Sonnet 4.5 (deprecated), have a 200k-token context window."
- OpenAI: "While each text generation request is independent and stateless, you can still implement multi-turn conversations by providing additional messages as parameters". "Even when using previous_response_id, all previous input tokens for responses in the chain are billed as input tokens in the API." "The context window is the maximum number of tokens that can be used in a single request. This max tokens number includes input, output, and reasoning tokens."
- Anthropic Messages API: "The Messages API can be used for either single queries or stateless multi-turn conversations."
- Note: `generation` already quoted the glossary's "working memory" and the three behaviors at a full window. Here the new point is statelessness: the whole conversation is sent again every turn and paid for again.

### PR29. More context is not automatically better: "context rot" (vendor statements)
- Sources: `anthropic2026contextwindows`; `anthropic2025context`; `anthropic2026compaction`; `anthropic2026contextediting`.
- Quotes: context-windows page (as of 2026-11-11): "more context isn't automatically better. As token count grows, accuracy and recall degrade, a phenomenon known as context rot." Engineering blog (29 Sep 2025): "Studies on needle-in-a-haystack style benchmarking have uncovered the concept of context rot: as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases. While some models exhibit more gentle degradation than others, this characteristic emerges across all models." Its explanation: "LLMs are based on the transformer architecture, which enables every token to attend to every other token across the entire context. This results in n² pairwise relationships for n tokens. As its context length increases, a model's ability to capture these pairwise relationships gets stretched thin ... Additionally, models develop their attention patterns from training data distributions where shorter sequences are typically more common than longer ones." Compaction page: "response quality degrades as a conversation grows". Context editing: "context is a finite resource with diminishing returns, and irrelevant content degrades model focus."
- Note: "context rot" is a vendor and practitioner term, not a benchmark. The n² explanation is the vendor's account, not a demonstrated mechanism; label it so. Peer-reviewed evidence: PR30, PR31.

### PR30. Lost in the middle (Liu et al., 2023-2024)
- Source: `liu2024lost`
- Location: TACL pp. 157-159, 161-162; arXiv v3 PDF pp. 17-18 (Tables 2-7).
- Quotes: abstract (p. 157): "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models." p. 158: models "are better at using relevant information that occurs at the very beginning (primacy bias) or end of its input context (recency bias)"; "when relevant information is placed in the middle of its input context, GPT-3.5-Turbo's performance on the multi-document question task is lower than its performance when predicting without any documents (i.e., the closed-book setting; 56.1%)." Also p. 158: "models often have identical performance to their extended-context counterparts". p. 159: "Even base language models (i.e., without instruction fine-tuning) show a U-shaped performance curve"; "prompting language models with longer input contexts is a trade-off: providing the language model with more information may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy" (source prints an em-dash). p. 162: "These results indicate that current models cannot effectively reason over their entire context window when prompted for downstream tasks." Query-aware contextualization (putting the question before and after the documents) "enables near-perfect performance on the synthetic key-value task, but minimally changes trends in multi-document QA" (p. 158).
- Models (p. 157): MPT-30B-Instruct, LongChat-13B (16K), GPT-3.5-Turbo (0613; 4K and 16K), Claude-1.3 (and 100K). Data (p. 159): questions from NaturalQuestions-Open, "historical queries issued to the Google search engine, coupled with human-annotated answers extracted from Wikipedia"; one document contains the answer, the others are distractors.
- Table 1 (p. 161), closed-book / oracle accuracy: LongChat-13B (16K) 35.0 / 83.4; MPT-30B-Instruct 31.5 / 81.9; GPT-3.5-Turbo 56.1 / 88.3; GPT-3.5-Turbo (16K) 56.0 / 88.6; Claude-1.3 48.3 / 76.1; Claude-1.3 (100K) 48.2 / 76.4 (the last four values read in arXiv v3's `-layout` extraction, same as TACL's text extraction).
- Table 6 (arXiv v3, PDF p. 18), 20 documents, accuracy % with the answer document at position 1, 5, 10, 15, 20: Claude-1.3 59.9, 55.9, 56.8, 57.2, 60.1; GPT-3.5-Turbo 75.8, 57.2, 53.8, 55.4, 63.2; GPT-3.5-Turbo (16K) 75.7, 57.3, 54.1, 55.4, 63.1; MPT-30B-Instruct 53.7, 51.8, 52.2, 52.7, 56.3; LongChat-13B (16K) 68.6, 57.4, 55.3, 52.5, 55.0. ("Index n" in the tables means position n + 1.) Table 5 (10 documents) and Table 7 (30 documents) on the same page.
- Token counts (Table 3, arXiv v3 PDF p. 17): the 20-document prompts average 2,946.2 tokens for GPT-3.5-Turbo (max 3,920); 10 documents 1,475.6; 30 documents 4,419.2.
- Date stamp: models of mid-2023. Not tested here on 2026 models.

### PR31. Claimed versus effective context length (Hsieh et al., 2024)
- Source: `hsieh2024ruler`
- Location: pp. 1-2, 7.
- Quotes: abstract (p. 1): "The needle-in-a-haystack (NIAH) test, which examines the ability to retrieve a piece of information (the 'needle') from long distractor texts (the 'haystack'), has been widely adopted ... However, this simple retrieval-based test is indicative of only a superficial form of long-context understanding ... Despite achieving nearly perfect accuracy in the vanilla NIAH test, almost all models exhibit large performance drops as the context length increases. While these models all claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of 32K." Effective length is defined against a threshold, Llama2-7B's score at 4K (85.6%) (Table 3 caption, p. 7).
- Table 3 (p. 7), claimed / effective length: Gemini-1.5-Pro 1M / >128K; GPT-4 128K / 64K; Llama3.1 (70B) 128K / 64K; Qwen2 (72B) 128K / 32K; Yi (34B) 200K / 32K; Mistral-v0.2 (7B) 32K / 16K; LWM (7B) 1M / <4K; LongChat (7B) 32K / <4K. GPT-4's average score falls from 96.6 at 4K to 81.2 at 128K.
- Date stamp: models as of mid-2024.

### PR32. Managing the context: compaction, clearing, and memory files (vendor docs, as of 2026-11)
- Sources: `anthropic2026compaction`; `anthropic2026contextediting`; `anthropic2026memorytool`; `openai2026compaction`.
- Anthropic compaction: "Compaction replaces the older turns of a conversation with a summary that Claude writes on the server ... It keeps a long conversation or agent task inside the context window, and it keeps the active context small". Options: compaction on demand, at a token threshold, or "Your own summarizer". Context editing: "Tool result clearing", "Thinking block clearing".
- Anthropic memory tool: "The memory tool lets Claude store and retrieve information across conversations in a directory of memory files ... without keeping everything in the context window." "The memory tool operates client-side: Claude requests file operations, and your application runs them."
- OpenAI compaction: "To support long-running interactions, you can use compaction to reduce context size while preserving state needed for subsequent turns." The returned item "carries forward key prior state and reasoning into the next run using fewer tokens. It is opaque and not intended to be human-interpretable."
- Mechanism point for the chapter: anything a model "remembers" across turns or sessions is text (or an opaque item) put back into the window; summaries lose detail, which `generation` already noted ("summarize the earlier part and continue").

### PR33. Vendor prompting advice that matches the measurements (as of 2026-11)
- Source: `anthropic2026bestpractices`
- Quotes: long documents: "Put long-form data at the top: Place your long documents and inputs near the top of your prompt, above your query, instructions, and examples." Note: "Queries at the end can improve response quality by up to 30 percent in tests, especially with complex, multidocument inputs." Examples: "A few well-crafted examples (known as few-shot or multishot prompting) improve accuracy and consistency"; make them "Diverse: Cover edge cases and vary enough that Claude doesn't pick up unintended patterns"; "Include 3-5 examples for best results" (source prints an en-dash). "Wrap examples in <example> tags". Role: "Setting a role in the system prompt focuses Claude's behavior and tone for your use case."
- Note: the "up to 30 percent" is the vendor's unpublished internal test; report as the vendor's statement. It agrees in direction with Liu et al.'s recency effect (PR30) and query-aware placement.

### G. System prompts and who is in charge

### PR34. System prompt and roles (vendor docs, as of 2026-11)
- Sources: `anthropic2026messages`; `openai2026text`.
- Anthropic: "system ... System prompt. A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role." Messages alternate user and assistant; "if you want to include a system prompt, you can use the top-level system parameter."
- OpenAI: "You can provide instructions to the model with differing levels of authority using the instructions API parameter along with message roles ... Any instructions provided this way will take priority over a prompt in the input parameter." "developer messages are instructions provided by the application developer, prioritized ahead of user messages. user messages are instructions provided by an end user, prioritized behind developer messages." Analogy: "You could think about developer and user messages like a function and its arguments in a programming language." Also: "Because the content generated from a model is non-deterministic, prompting to get your desired output is a mix of art and science"; advice to pin "production applications to specific model snapshots" and build "tests and evaluation suites that measure prompt behavior".
- Hand-off: that roles become marker tokens in one document is `instructions` (and `destination` already says the turns are laid out "as one document with markers for who is speaking").

### PR35. The chain of command and untrusted data (OpenAI Model Spec, 2026-10-29)
- Source: `openai2026modelspec`
- Quotes: "The Model Spec assigns instructions ... different levels of authority. Higher-authority instructions take precedence over lower-authority ones." Ordering: "Root", "System", "Developer", "User", "Guideline", and "No authority by default: assistant and tool messages; quoted or untrusted text and multimodal data in other messages." "Ignore untrusted data by default": "Quoted text (plaintext in quotation marks, YAML, JSON, XML, or similar blocks) in ANY message, multimodal data, file attachments, and tool outputs are assumed to contain untrusted data and have no authority by default (i.e., any instructions contained within them MUST be treated as information rather than instructions to follow)." And: "Without this formatting, the untrusted input might contain malicious instructions ('prompt injection'), and it can be extremely difficult for GPT to distinguish them from the developer's instructions." Also: "We are training our models to align to the principles in the Model Spec."
- Note: a behavior OpenAI trains for and documents, not a guarantee. Date: version 2026/10/29.

### PR36. Training models to rank instructions (Wallace et al., 2024)
- Source: `wallace2024instruction`
- Location: p. 1.
- Quotes: "we argue that one of the primary vulnerabilities underlying these attacks is that LLMs often consider system prompts (e.g., text from an application developer) to be the same priority as text from untrusted users and third parties. To address this, we propose an instruction hierarchy that explicitly defines how models should behave when instructions of different priorities conflict ... showing that it drastically increases robustness, even for attack types not seen during training, while imposing minimal degradations on standard capabilities." (source prints em-dashes)
- Their introduction illustrates an indirect injection through an email read by an assistant (system message, user request, tool output containing an instruction to forward all mail, model complies). Described here only; do not reprint the attack text.

### H. Prompt injection

### PR37. Naming the attack (Willison, September 2022)
- Source: `willison2022prompt`
- Location: the post, 12 September 2022.
- Content: Willison reports Riley Goodside's examples of the previous day, in which a GPT-3 translation prompt was followed by user text instructing the model to disregard the translation instruction and print a fixed phrase, and the model did so [passage omitted: the literal attack text]. Quote: "This isn't just an interesting academic trick: it's a form of security exploit. I propose that the obvious name for this should be prompt injection." Why it matters: applications built on the GPT-3 API "assemble prompts by concatenating strings together". He draws "The obvious parallel" with SQL injection and notes that "The best protection against SQL injection attacks is to use parameterized queries". The post also reports leaking the original prompt.
- Note: a blog post, used only as the first-hand record of the name; `wallace2024instruction` p. 1 cites "Willison, 2022" for prompt injection, and `ncsc2025prompt` says "The term 'prompt injection' was coined in 2022". Goodside's original posts were not fetched.

### PR38. The first paper: goal hijacking and prompt leaking (Perez and Ribeiro, 2022)
- Source: `perez2022ignore`
- Location: pp. 1-2, 4.
- Quotes: p. 1: "one can simply build a grammar fixing tool by using the prompt Correct this to standard English: "{user_input}" ... However, the ease of building applications with GPT-3 comes with a price: malicious users can easily inject adversarial instructions via the application interface. Due to the unstructured and open-ended aspect of GPT-3 prompts, protecting applications from these attacks can be very challenging. We define the action of inserting malicious text with the goal of misaligning an LLM as prompt injection." p. 2: "We define goal hijacking as the act of misaligning the original goal of a prompt to a new goal of printing a target phrase ... We define prompt leaking as the act of misaligning the original goal of a prompt to a new goal of printing part of or the whole original prompt instead." p. 4: "text-davinci-002 is by far the model most susceptible to attacks ... While we did not aim to find the best attack prompts, we achieved a success rate of 58.6% ± 1.6 for goal hijacking and 23.6% ± 2.7 for prompt leaking." Small wording changes matter (p. 4): "using print rather than say, and adding the word instead, improve the" attacks.
- Setting (p. 4): 35 application prompts, each experiment repeated 4 times. Date: November 2022, GPT-3 models.

### PR39. Indirect prompt injection (Greshake et al., 2023)
- Source: `greshake2023not`
- Location: p. 1.
- Quotes: abstract: "So far, it was assumed that the user is directly prompting the LLM. But, what if it is not the user prompting? We argue that LLM-Integrated Applications blur the line between data and instructions. We reveal new attack vectors, using Indirect Prompt Injection, that enable adversaries to remotely (without a direct interface) exploit LLM-integrated applications by strategically injecting prompts into data likely to be retrieved ... We demonstrate our attacks' practical viability against both real-world systems, such as Bing's GPT-4 powered Chat and code-completion engines, and synthetic applications built on GPT-4 ... Despite the increasing integration and reliance on LLMs, effective mitigations of these emerging threats are currently lacking." Fig. 1 caption: "adversaries could control the LLM, without direct access, by indirectly injecting it with prompts placed within sources retrieved at inference time."
- Date stamp: "currently lacking" as of February to May 2023.

### PR40. Unsolved, in the words of a standards body and a security agency
- Sources: `owasp2025llm01`; `ncsc2025prompt`.
- OWASP (LLM01:2025, page modified 2025-04-17): "A Prompt Injection Vulnerability occurs when user prompts alter the LLM's behavior or output in unintended ways. These inputs can affect the model even if they are imperceptible to humans". "Prompt injection vulnerabilities are possible due to the nature of generative AI. Given the stochastic influence at the heart of the way models work, it is unclear if there are fool-proof methods of prevention for prompt injection. However, the following measures can mitigate the impact". Prompt injection is item 01 of the 2025 list.
- NCSC (8 December 2025): "Under the hood of an LLM, there's no distinction made between 'data' or 'instructions'; there is only ever 'next token' ... As there is no inherent distinction between 'data' and 'instruction', it's very possible that prompt injection attacks may never be totally mitigated in the way that SQL injection attacks can be." On defenses (detection, training models to prioritise instructions, marking data): "All of these approaches are trying to overlay a concept of 'instruction' and 'data' on a technology that inherently does not distinguish between the two." It proposes treating it as exploitation of an "inherently confusable deputy" rather than code injection.

### PR41. Unsolved, in the words of model vendors (2025)
- Sources: `openai2025promptinjections`; `openai2025atlas`; `anthropic2025promptinjection`.
- OpenAI, 7 November 2025: "Prompt injection is a type of social engineering attack specific to conversational AI ... The idea that a third-party (that is not the user and not the AI) could mislead the model by injecting malicious instructions into the conversation context led to the term 'prompt injection'." "These risks increase as AIs have access to more sensitive data and take on more initiative and longer tasks." "Prompt injection remains a frontier, challenging research problem".
- OpenAI, 22 December 2025: "Prompt injection, much like scams and social engineering on the web, is unlikely to ever be fully 'solved'. But we're optimistic that a proactive, highly responsive rapid response loop can continue to materially reduce real-world risk over time."
- Anthropic, 24 November 2025: "prompt injection is far from a solved problem, particularly as models take more real-world actions." Against "an internal adaptive 'Best-of-N' attacker" given "100 attempts per environment", with attack success rate "computed as a percentage of attacks encountered by each model": "A 1% attack success rate, while a significant improvement, still represents meaningful risk. No browser agent is immune to prompt injection, and we share these findings to demonstrate progress, not to claim the problem is solved." (source prints em-dashes). Defenses named: reinforcement learning against injections in simulated web content, and classifiers that "scan all untrusted content that enters the model's context window".
- Date stamp: statements of November and December 2025; re-check before a PDF build.

### I. What prompting cannot fix

### PR42. The knowledge cutoff (vendor docs, as of 2026-11)
- Source: `anthropic2026models`
- Quotes: "Reliable knowledge cutoff: The date through which the model's knowledge is most extensive and reliable. Training data cutoff (under Additional details) is the broader range of data used." The comparison table lists, for Claude Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5: reliable knowledge cutoff "Jun 2026", training data cutoff "Jun 2026".
- Note: the chapter's point is that no prompt adds facts the weights lack; text placed in the window can (hand-off to `tools` for retrieval). The two-cutoff distinction is a useful detail; date-stamp the table values.

### PR43. A letter-counting error that a prompt does not fix (Kalai et al., 2025)
- Source: `kalai2025why`
- Location: p. 2.
- Quote: "How many Ds are in DEEPSEEK? If you know, just say the number with no commentary. DeepSeek-V3 returned '2' or '3' in ten independent trials; Meta AI and Claude 3.7 Sonnet performed similarly, including answers as large as '6' and '7'." (DEEPSEEK has one D.) Footnote: models accessed in May 2025; "None of the models searched the Web."
- Link: `tokens` explains why letters are hard to see. The instruction "If you know, just say the number" did not prevent confident wrong answers. Printed model outputs from a source, usable [D-009].

### PR44. Prompts can state the scoring rule (Kalai et al., 2025)
- Source: `kalai2025why`
- Location: p. 13 (Section 4.2, checked on the page image).
- Quote: "we propose evaluations explicitly state confidence targets in their instructions, within the prompt (or system message). For example, one could append a statement like the following to each question: Answer only if you are > t confident, since mistakes are penalized t/(1 - t) points, while correct answers receive 1 point, and an answer of 'I don't know' receives 0 points." Then: "There are several natural values of t including t = 0.5 (penalty 1), t = 0.75 (penalty 2), and t = 0.9 (penalty 9)." See PRD7: t/(1 - t) at 0.75 is 3.
- Use: a prompt can change what a good answer is (abstain or guess), not what the model knows. `generation` already covers their hallucination argument; reuse only this point if wanted.

### PR45. Early "split it into steps" prompting, and its printed arithmetic slip (Reynolds and McDonell, 2021)
- Source: `reynolds2021prompt`
- Location: p. 7 (Fig. 3, checked on the page image; and the column text).
- Content: Fig. 3, "A generic serializing metaprompt applied to a math problem", generated with "engine=davinci, temperature=0"; task "f(x) = x*x. What is f(f(3))?", metaprompt (bold) "Let's solve this problem by splitting it into steps.", GPT-3's text (blue): "f(f(3)) = f(3*3) = 3*3*3 = 27" and "We can see that f(3) = 3*3 = 9, so f(f(3)) = 27." The correct value is f(9) = 81; the paper does not remark on the error (searched for "81", "incorrect", "wrong").
- Also p. 7: "When extending reasoning, it is essential to discourage premature verdicts, otherwise all subsequent computation serves only to rationalize the already-chosen verdict without improving the probability of the verdict's accuracy." An early statement of the post-hoc reasoning worry (PR20, PR21).
- Use: a real, printed model output showing step-by-step text that looks orderly and is wrong. State plainly that the paper does not comment on it.

## Disputed or inconsistent points

### PRD1. How in-context learning works: four accounts, none settled
Present as competing, partly compatible accounts, each with its evidence and scope.
- **Recognizing a task already learned** (task location): Reynolds and McDonell (PR2); Min et al.'s strict-definition reading (PR3); Brown et al. themselves left it open (PR1).
- **Learning the mapping from the examples**: Yoo et al. (PR4) and Wei et al. 2023 (PR5): large models follow flipped labels down to 22.5% on a task they would otherwise get 90.3% right, so they do read the mapping.
- **Bayesian inference over a latent concept**: Xie et al. (PR6), proved under the assumption that the model fits a mixture-of-HMMs pretraining distribution exactly, and demonstrated on synthetic data.
- **Gradient descent inside the forward pass**: von Oswald et al. (PR7), shown for small attention-only models trained on linear regression; Shen et al. (PR8) found that the equivalence does not hold up cleanly in a pretrained LLaMA-7B and call it "an open hypothesis".
- **A circuit that does it**: Olsson et al.'s induction heads (PR9), causal evidence in small attention-only models, correlational in large ones, with their own "shared latent variable" caveat.
- Suggested framing: these answer different questions (what the examples supply; what computation could implement it; what circuit appears in trained models). The 2000s reader can hold several: Min's results fit task location; Wei 2023 shows larger models also use the mapping; induction heads are a concrete copying mechanism; the GD and Bayesian results are proofs of possibility in toy settings.

### PRD2. Do correct labels matter?
- Min et al.: barely (0-5% absolute drop) on averages over many datasets, k = 16 (PR3).
- Yoo et al.: it depends on configuration; some cases show large effects (PR4).
- Wei et al. 2023: small models ignore flipped labels; large ones follow them (PR5).
- Reconciliation offered by Wei et al. 2023 itself (p. 4): small-model behavior is "consistent with Min et al. (2022b)". Do not say "labels do not matter" without "for the models and tasks of 2022, on average".

### PRD3. Is a chain of thought the model's actual reasoning?
- Wei et al. (2022) left it open (PR16 limitations).
- Against faithfulness: Turpin et al. (PR20: biased answers rationalized, 1 of 426 explanations mentions the bias); Lanham et al. (PR21: varies by task, worse in larger models on 7 of 8 tasks); Chen et al. 2025 (PR22: reasoning models mention used hints 25% and 39% of the time).
- For it being load-bearing at least sometimes: Wei et al.'s ablations (PR16: dots and after-the-answer chains do not help, so the content matters); Lanham et al. (filler tokens give no gain; on some tasks the model relies heavily on the chain); Korbak et al. (PR19: on hard enough tasks the chain is the only route for long serial computation, so it must carry real information).
- Bridge already in the book: `attention` closes on "a picture of attention is not a proof of why a model gave its answer". The same caution applies to a written chain of thought.
- Suggested wording: "The chain of thought is text the model generates and then conditions on. It can carry real intermediate results, and on hard problems it must; it can also be a plausible story that leaves out what actually drove the answer."

### PRD4. Who started step-by-step prompting
A sequence, not one inventor:
- Reynolds and McDonell, February 2021: "Let's solve this problem by splitting it into steps" as a metaprompt, demonstrated but, per Kojima et al. (Table 4, p. 8), "not quantitatively evaluated" (PR45, PR13).
- Nye et al., November 2021: scratchpads, mostly with fine-tuning (PR14).
- Wei et al., January 2022: named "chain-of-thought prompting", few-shot exemplars with reasoning, measured across sizes (PR15).
- Kojima et al., May 2022: zero-shot "Let's think step by step" (PR17).
`turpin2023language` (p. 1) credits "Nye et al., 2021; Wei et al., 2022"; `korbak2025chain` (p. 2) credits "Reynolds & McDonell, 2021; Kojima et al., 2022; Wei et al., 2022". The OUTLINE's "chain-of-thought (2022)" is right for the name and the measured method.

### PRD5. Order sensitivity: who first
Zhao et al. (arXiv 19 Feb 2021) reported that example order swings accuracy (PR10); Lu et al. (arXiv 18 Apr 2021) wrote that "no work has studied the effect of the sample ordering" (PR11). Near-simultaneous; cite both and do not adjudicate.

### PRD6. Why prompt injection persists: two explanations
- NCSC (PR40): the model makes "no distinction ... between 'data' or 'instructions'; there is only ever 'next token'".
- OWASP (PR40): "the stochastic influence at the heart of the way models work".
- Vendors (PR41) and Wallace et al. (PR36): trained priority rules and classifiers reduce the rate but do not eliminate it; OpenAI compares it to scams and social engineering.
- These are compatible. The NCSC account is the mechanism the chapter can explain from earlier chapters (everything in the window is one token sequence). The SQL-injection analogy is Willison's (PR37); the NCSC's title argues it is misleading because SQL has a structural fix (parameterized queries) and LLMs do not. Present both.

### PRD7. Numbers that disagree between or within sources
- PaLM 540B on GSM8K with chain of thought: 56.9 in Wei et al. Table 1 (PR15) vs 56.5 in Wang et al. Table 2 (PR18). Use each paper's own number with its own comparison (17.9 to 56.9 in Wei; 56.5 to 74.4 in Wang); do not mix.
- text-davinci-002 on GSM8K, few-shot CoT with 8 exemplars: 46.9 (Wei et al. Table 1) vs 48.7 (Kojima et al. Table 2). Different runs; same caution.
- Olsson et al.: "we study up to 12B parameter models" (p. 19) vs "our 40-layer model with 13 billion parameters" (p. 20) and "13B" in the model table (p. 40, non-embedding parameters). Say "about 13 billion" or avoid the number.
- Kalai et al. p. 13: "t = 0.75 (penalty 2)", but their formula t/(1 - t) gives 3 (checked on the page image). If used, give the formula's value and do not repeat the printed 2.
- Sclar et al.: GPT-3.5 maximum spread "56 accuracy points" (p. 2) and "0.562" (p. 8): consistent (rounding).

### PRD8. Does constraining the format hurt reasoning?
- Tam et al. (PR27): "a significant decline in LLMs' reasoning abilities under format restrictions".
- Vendors present constrained decoding as guaranteeing format (PR25, PR26) without a claim about reasoning quality; OpenAI's 2024 page suggests "a separate field for chain of thought to improve the final quality of the response"; Anthropic warns that a schema property asking for "step-by-step reasoning might lead to a reasoning_extraction refusal" and to "Ask for a short explanation instead" (structured outputs page, "Invalid outputs"). Developers of constrained-decoding tools disputed Tam et al. in blog posts (not fetched).
- Suggested wording: "Forcing a format guarantees the shape of the answer, not its quality, and one 2024 study found that strict formats can lower accuracy on reasoning tasks; the question was argued."

### PRD9. Long contexts: 2023 findings vs 2026 window sizes
Not a dispute between authors but a dating hazard. Liu et al. (PR30) tested 2023 models with windows up to 100K; RULER (PR31) 2024 models; vendors now advertise 1M-token windows (PR28) and themselves warn of "context rot" (PR29). Do not claim that the U-shape holds for 2026 models, and do not claim that it was fixed. Say what was measured, when, and that vendors still advise putting the question at the end (PR33).

## Mechanism claims to check numerically at drafting [D-009]

Suggested script: `code/checks/prompting.py`, standard library only, importing the `GPT2` class from `code/checks/tokens.py` for token counts (it reads the hash-pinned GPT-2 vocabulary from `out/cache/` [D-018]). Items 1-8 were run once in this session with a throwaway script and agree with the numbers below (checked).

1. **How many orderings (checked).** k demonstrations can be ordered k! ways: 4 gives 24 (Lu et al.'s and Zhao et al.'s setting), 8 gives 40,320, 16 gives about 2.09 x 10^13, and 64! (Lu et al. p. 8088) about 1.27 x 10^89. Point: trying every order is impossible beyond a handful.
2. **What a demonstration costs in tokens (checked, GPT-2 tokenizer).** Zhao et al.'s two-shot prompt (PR10, three lines) is 29 tokens. Wei et al.'s Fig. 1 exemplar: standard 41 tokens, with chain of thought 65 tokens (1.59 times). Eight exemplars: 328 vs 520 tokens. Kojima's " Let's think step by step." is 7 tokens. GPT-3's 2,048-token window (PR1) therefore fits roughly 30 such chain-of-thought exemplars at most, before the question. Label: GPT-2's tokenizer stands in for the models' own; counts differ by tokenizer (`tokens`).
3. **Where the middle is (checked, approximate).** Liu et al.'s 20-document prompts average 2,946.2 tokens (Table 3), about 147 tokens per document if the instruction and question are spread evenly (they are not; say "about"). Position 10 begins about 45% of the way into the prompt; position 1 at 0%, position 20 at 95%.
4. **The U-curve in numbers (checked).** GPT-3.5-Turbo, 20 documents (Table 6): 75.8 at position 1, 53.8 at position 10, 63.2 at position 20. Drop from first to worst: 22.0 points. Worst minus closed-book (56.1): -2.3 points, so the model did worse with the answer in front of it than with no documents at all.
5. **Gains, as arithmetic on printed numbers (checked).** Wei et al. GSM8K: PaLM 540B 17.9 to 56.9 (+39.0, 3.2 times); GPT-3 175B 15.6 to 46.9 (+31.3); LaMDA 137B 6.5 to 14.3 (+7.8); small models lose (LaMDA 420M 2.6 to 0.4). Kojima et al.: MultiArith 17.7 to 78.7 (+61.0); GSM8K 10.4 to 40.7 (+30.3). Wang et al.: 56.5 to 74.4 (+17.9). Zhao et al. order spread: 54.3 to 93.4 (39.1 points). Wei et al. 2023: 90.3 to 22.5 (-67.8 points). Turpin et al.: 1 of 426 is 0.23%.
6. **Self-consistency's price (checked).** Forty sampled chains (Wang et al.) cost forty times the generated tokens of one greedy chain; their suggested 5 or 10 paths cost 5 or 10 times. With item 2's 65-token chain as a stand-in length: 40 x 65 = 2,600 generated tokens vs 65. Label the 65 as an illustration.
7. **A grammar mask, step by step (constructed numbers, checked).** Six candidate next tokens with constructed scores (logits) 1.0, 0.5, 3.0, 2.5, 0.2, 0.1 for "{", a double quote, "Hello", " The", "}", newline. Softmax gives 0.070, 0.042, 0.516, 0.313, 0.031, 0.028. If the grammar allows only "{" at the start of a JSON object, the masked distribution is 1.000 for "{". If it allows "{" and the quote, renormalizing gives 0.622 and 0.378. The model had put only 0.112 of its probability on the allowed tokens: the mask overrides what the model "wanted", which is why vendors also describe the schema to the model (PR26) and llama.cpp advises describing it in the prompt (PR24). Say the numbers are constructed. Same arithmetic as top-k renormalization in `generation`.
8. **Kalai et al.'s confidence target (checked).** Penalty t/(1 - t): t = 0.5 gives 1, t = 0.75 gives 3, t = 0.9 gives 9. Expected score of answering with confidence p is p - (1 - p) x t/(1 - t), which is zero at p = t. At t = 0.75: p = 0.6 gives -0.60, p = 0.9 gives +0.60, versus 0 for "I don't know". (The printed "penalty 2" would put the break-even at 2/3; PRD7.) Optional.
9. **Context sizes (checked; label the words estimate).** 2,048 tokens (GPT-3) is about 1,536 words at OpenAI's three-quarters of a word per token (`tokens`, an estimate); 1,000,000 tokens about 750,000 words, 488 times GPT-3's window. Optional link to `anatomy`'s quadratic count: about 5 x 10^11 query-key pairs per head per layer at 1M tokens, counting each causal pair once (n^2/2). Use only if `anatomy`'s own convention matches (it uses n^2 for "every pair").
10. **The printed wrong answer (checked by hand).** Reynolds and McDonell Fig. 3: f(x) = x*x, f(3) = 9, f(f(3)) = f(9) = 81, not 27 (PR45).

## Figures planned [D-014]

- `figures/prompting-cot-scale.svg` (recommended): GSM8K accuracy against model size, standard prompting vs chain of thought, three model families (LaMDA 420M-137B, GPT 350M-175B, PaLM 8B-540B), from Wei et al. Table 2 (p. 21) printed numbers only, log-scaled size axis, with the prior-best 55% as a dashed line (Table 1). Caption: numbers from the paper's table; chain of thought hurts small models and helps large ones; "emergent" links back to `scale`. Do not read values off the paper's Figure 4.
- `figures/prompting-lost-in-middle.svg` (recommended): accuracy by position of the answer document (1, 5, 10, 15, 20) for the five models of Liu et al. arXiv v3 Table 6, with a horizontal line at GPT-3.5-Turbo's closed-book 56.1% (Table 1). Printed table values only. Caption must date the models (mid-2023).
- `figures/prompting-window.svg` (optional diagram): one request drawn as a stacked strip of token blocks (system prompt, tool definitions, earlier turns, retrieved or pasted documents, the new user message, then the reply), with a second strip for the next turn showing everything resent plus the new turn, and a third showing compaction replacing early turns by a shorter summary block. Block sizes illustrative; label them so. Supports PR28, PR32. Could reuse the destination pipeline script's style [D-014].
- `figures/prompting-mask.svg` (optional): item 7 as two bar charts, before and after the mask, constructed numbers.
- Not planned: a chart of Zhao et al. or Lu et al. permutation accuracies (only the extremes are printed; the scatter plots are images). Not planned: anything read off Olsson et al.'s loss-curve figures.

## Scope notes for drafting

- **Hand-offs.**
  - From `scale`: zero-, one-, few-shot, GPT-2's zero-shot, GPT-3's in-context learning, the "no gradient updates" quote, "learn or recognize" left open, and the emergent-abilities dispute. Do not redefine; revisit. Chain of thought's "emergent ability of model scale" (PR15) should point back to that dispute.
  - From `generation`: sampling, temperature, greedy decoding (Kojima uses greedy; self-consistency uses sampling), stop sequences, max tokens, the three behaviors at a full window, hallucination and calibration (note the different sense of "calibrate" in Zhao et al., PR10). Do not re-explain hallucination; "what prompting cannot fix" links to it.
  - From `tokens`: cost counted in tokens; spelling and digits (PR43). From `anatomy`: the context window as a position limit, quadratic cost, fixed number of layers per token (needed for PR19). From `attention`: the "attention is not explanation" dispute, which PRD3 echoes. Residual stream is the term for the per-position vector between layers [D-019], if PR19's figure is described.
  - To `instructions` (outlined, not drafted): chat templates, roles as marker tokens, RLHF, why system prompts carry weight. This chapter may say the system prompt is ordinary text in the window with trained priority (PR34-PR36) and point forward/back by ID. Check `instructions`' status at drafting; if still undrafted, keep the template detail out.
  - To `adapting`: when to fine-tune instead of prompt (prompt sensitivity, cost of long few-shot prompts).
  - To `tools`: retrieval, tool calling, agents, strict tool use, indirect prompt injection through retrieved pages and tool outputs (introduce here with Greshake et al.; mechanisms and defenses-by-design there).
  - To `frontier`: reasoning models and their thinking tokens (PR22, PR28's thinking-token accounting), CoT monitorability.
  - To `evaluation`: benchmark scores depend on prompt format (PR12); Kalai's confidence targets (PR44).
- **Coordination with ledgers written in parallel** (seen in the repository on 2026-11-11, not read in full): `book1/sources/instructions.md` hands to this chapter "few-shot versus instruction-following prompts, the system prompt as context, prompt injection" and introduces ChatML's SQL-injection analogy (its IN13) and OpenAI's harmony "order of authority" (IN14) in one sentence each; do not repeat them at length, build on them. `book1/sources/tools.md` says this chapter "owns prompt injection as a concept" and context management, and that `tools` adds the indirect form (its TL52) and uses Lost in the Middle only as a retrieval failure; so here, cover direct injection fully (PR37, PR38, PR40, PR41) and give indirect injection (PR39) one or two sentences with a forward link. `tools` also covers knowledge cutoffs in depth (TL2-TL4): keep PR42 to a sentence or two. `book1/sources/evaluation.md` uses Sclar et al. (its EV28) for "prompt format alone moves accuracy": here the point is the mechanism and the user's view; there, benchmark validity. Check the drafted versions of these chapters before drafting.
- **What not to say.**
  - Not that the model "learns" from examples in the training sense; nothing changes in the weights (`scale`), and what it extracts is disputed (PRD1).
  - Not "labels don't matter" in general (PRD2).
  - Not that induction heads are proven to be the mechanism of in-context learning in large models (correlational there, PR9).
  - Not that in-context learning "is" gradient descent in LLMs (toy regression; Shen et al.).
  - Not that chain of thought always helps: it hurt small models (Table 2) and did not help zero-shot commonsense QA (Kojima).
  - Not that "Let's think step by step" is a magic phrase: 16 templates ranged from 9.3 to 78.7 on one task (PR13).
  - Not that a chain of thought shows the model's real reasoning, nor that it never does (PRD3).
  - Not that structured outputs guarantee correct content: they guarantee shape, with listed exceptions (refusal, max_tokens, enum casing; PR26).
  - Not that constrained decoding began with vendors in 2024: llama.cpp merged grammar sampling in July 2023 and Willard and Louf's paper is from July 2023 (PR23, PR24), with earlier work they cite.
  - Not that long-context models use all of their window equally well, and not that the 2023 U-curve holds or was fixed for 2026 models (PRD9).
  - Not that a system prompt is secret or binding: prompt leaking (PR38) and injection (PR37-PR41).
  - Not that prompt injection is solved, or solvable by a better prompt (PR40, PR41).
  - Not invented model outputs. Usable printed outputs: Wei et al. Fig. 1 (PR15), Reynolds and McDonell Fig. 3 (PR45), Kalai et al.'s DEEPSEEK answers (PR43), Zhao et al.'s "62% Positive" for "N/A" (PR10). Lanham et al. Fig. 1 is a schematic, not output.
  - Not "prompt engineering is folklore" either: the measured effects above are large and reproducible as effects, even where the best wording is not.
- **Terms to define at first use** (for the glossary): prompt; prompt engineering (`openai2026text` calls it "a mix of art and science"); demonstration / exemplar; label space; prompt format (template); in-context learning (revisited, with Min et al.'s strict vs broad senses); recency bias and majority-label bias; contextual calibration (distinguish from `generation`'s calibration); semantic prior; latent concept (Xie); induction head and previous-token head; phase change (training); chain of thought; zero-shot chain of thought; self-consistency; majority vote; faithfulness (of an explanation); structured output; JSON and JSON Schema (one sentence each; no code [D-003]); JSON mode; constrained decoding / constrained sampling; grammar (context-free grammar, in words; BNF named only); finite-state machine (optional, one sentence); prefill; context management; compaction; context editing; context rot (vendor term); needle in a haystack; effective context length; primacy and recency (position effects); system prompt; developer message; instruction hierarchy / chain of command; untrusted data; prompt injection, direct and indirect; goal hijacking; prompt leaking; jailbreak (one sentence, to distinguish: getting a model to break its own rules, vs making an application follow someone else's instructions; source the distinction or keep it as plain usage); knowledge cutoff (reliable vs training-data).
- **Formulas** [D-002]: at most (a) softmax with a mask, in words ("set disallowed scores to minus infinity, then softmax as before"), item 7; (b) majority vote as "the most common final answer"; (c) Xie et al.'s Eq. (1) in words ("average the predictions over possible tasks, weighted by how likely each task is given the prompt"), with the LDA bridge; (d) k! for orderings. No JSON or grammar listings: describe them in prose [D-003]. Kalai's t/(1 - t) only if PR44 is used.
- **Book 1 rule** [D-003]: no code, no JSON blocks, no grammar listings, no API calls. Prompts may be quoted as prose (as `scale` does with "Translate English to French:"), in running text or block quotes, not code fences. Check `tools/check.py`'s code-block rule before using any indented block.
- **Date stamps:** every vendor statement (PR25-PR29, PR32-PR35, PR41, PR42) "as of 2026-11" or with its own date (PR25 August 2024; PR41 November and December 2025); OWASP list "2025"; NCSC December 2025; Liu et al. models mid-2023; RULER models mid-2024; Chen et al. models early 2025; context-window sizes (1M, 200k) as of 2026-11.
- **Bridges** the reader can use:
  - Xie et al.: in-context learning as posterior inference over a latent topic, like LDA (the paper's own bridge, PR6).
  - von Oswald et al.: linear regression fitted by gradient descent, which the reader knows; the claim is that attention can perform one such step.
  - Self-consistency as an ensemble by majority vote; Wang et al. compare it to ensembles (p. 7). The link to bagging is this ledger's, not the paper's.
  - Contextual calibration as correcting a classifier's bias towards one class by an affine adjustment of its outputs; Zhao et al. fit "calibration parameters" W and b (p. 12701). The Platt-scaling comparison is this ledger's, not the paper's; use cautiously or not at all.
  - Order sensitivity versus training-set order in classical ML: Zhao et al.'s own sentence ("typically an afterthought", PR10).
  - Prompt formatting sensitivity as an unreported degree of freedom in evaluation, like choosing a preprocessing step after seeing test results (this ledger's framing; Sclar et al. recommend reporting the spread, PR12).
  - Primacy and recency in Liu et al. (the paper's words); the human serial-position effect is this ledger's comparison, not the paper's.
  - Prompt injection as SQL injection (Willison), and why the analogy breaks (NCSC).
  - Constrained decoding as truncating and renormalizing a distribution, like top-k in `generation`.
- **Possible chapter spine** (a suggestion only): what the window is and that it is all the model sees (PR28); in-context learning revisited (PR1-PR9); sensitivity (PR10-PR13); chain of thought and why it helps (PR14-PR19); does it show the reasoning (PR20-PR22); structured output (PR23-PR27); long contexts and managing them (PR29-PR33); system prompts and prompt injection (PR34-PR41); what prompting cannot fix (PR42-PR45).

## Leads not used as sources

- Wikipedia articles on prompt engineering, prompt injection, and chain-of-thought prompting: not consulted.
- Pfau, Merrill, Bowman (2024), "Let's think dot by dot: hidden computation in transformer language models": filler tokens can help in constructed tasks. Would nuance PR16 and PR21; not fetched.
- The dottxt (Outlines) blog response to Tam et al., "Say What You Mean" (late 2024): the other side of PRD8; not fetched; a blog in any case.
- Chroma's 2025 "context rot" technical report, the likely source of the vendor term in PR29: not fetched.
- Debenedetti et al. (2025), CaMeL; Beurer-Kellner et al. (2025) on design patterns against prompt injection: named by the NCSC page; for `tools`.
- Riley Goodside's September 2022 posts: the first public examples, via Willison only.
- Anthropic's Transparency Hub (named on the models page as the source for cutoff details): not fetched.
- Simon Willison's later posts distinguishing prompt injection from jailbreaking: not fetched; if the chapter makes that distinction, fetch or keep it as plain usage.

## Worked examples used in the chapter

All from `code/checks/prompting.py` [D-009], run 2026-11-11; each use in the chapter is marked with a `<!-- D-009: ... -->` comment.

- **Example 1 (orderings):** 4! = 24, 8! = 40,320, 16! about 2.09 x 10^13. Used in "Small changes, large swings". (64! is printed by the script but not used.)
- **Example 2 (token counts, GPT-2 tokenizer as a stand-in):** Zhao et al.'s prompt, four lines with line breaks, 29 tokens; Wei et al.'s Fig. 1 exemplar with a line break before "A:", standard 41 vs chain of thought 65 (1.59 times); eight exemplars 328 vs 520; " Let's think step by step." 7 tokens. Used in "Small changes" and "Thinking out loud". (The "31 exemplars fit in 2,048 tokens" line is printed but not used.)
- **Example 3 (where the middle is):** 2,946.2 tokens / 20 documents; position 10 begins about 45% of the way in. Used in "Long contexts" (the per-document 147.3 is not printed in the prose).
- **Example 4 (U-curve):** GPT-3.5-Turbo 75.8 / 53.8 / 63.2; first minus worst 22.0; worst minus closed-book 56.1 is -2.3. Used in "Long contexts".
- **Example 5 (arithmetic on printed numbers):** Wei Table 2 differences (LaMDA 420M 2.6 to 0.4; PaLM 62B +20.3; PaLM 540B 3.2 times); Kojima 17.7 to 78.7, 10.4 to 40.7 (printed in the quote, not recomputed in prose); Zhao 54.3 to 93.4 is 39.1 points; Wei 2023 90.3 to 22.5 is -67.8; Sclar 0.036 to 0.804; Turpin 1/426 = 0.23%.
- **Example 6 (self-consistency cost):** 40 x 65 = 2,600 generated tokens vs 65.
- **Example 7 (grammar mask, constructed scores 1.0, 0.5, 3.0, 2.5, 0.2, 0.1):** softmax 0.070, 0.042, 0.516, 0.313, 0.031, 0.028; allowed mass 0.112; renormalized 0.622 / 0.378; single allowed token 1.000. Labelled as constructed in the prose.
- **Example 8 (Kalai et al.'s confidence target):** penalties 1, 3, 9 at t = 0.5, 0.75, 0.9; at t = 0.75, expected score -0.60 at p = 0.6 and +0.60 at p = 0.9.
- **Example 9 (context sizes):** 2,048 tokens about 1,536 words; 1,000,000 tokens about 750,000 words, 488 times GPT-3's window.
- **Example 10 (Reynolds and McDonell Fig. 3):** f(f(3)) = f(9) = 81, against the printed 27.

## Figures

Both drawn by `figures/prompting.py` [D-014] from the printed values stored in `code/checks/prompting.py`; nothing read off a published figure.

- `figures/prompting-cot-scale.svg`: GSM8K accuracy, standard vs chain-of-thought prompting, LaMDA (420M-137B), GPT-3 (350M-175B), PaLM (8B-540B), from Wei et al. Table 2 (p. 21), log size axis, dashed line at the prior best 55 (Table 1, p. 20). Panel title "GPT-3" follows the ledger's PR15 ("GPT-3 175B (text-davinci-002)"); Table 2's own family label was recorded as "GPT".
- `figures/prompting-lost-in-middle.svg`: accuracy by position (1, 5, 10, 15, 20 of 20 documents) for the five models of Liu et al. arXiv v3 Table 6, with a dotted line at GPT-3.5-Turbo's closed-book 56.1 (Table 1). Caption dates the models to mid-2023.
- Not drawn: the optional window diagram and the optional mask bar chart (the mask is a worked example in prose instead).

## Terms defined in the chapter

Bold at first use: prompt; prompt engineering; demonstration; exemplar; task location; label space; semantic prior; latent concept; induction head; previous-token head; majority label bias; recency bias; common token bias; contextual calibration (distinguished from `generation`'s calibration); scratchpad; chain of thought; chain-of-thought prompting; zero-shot chain of thought; self-consistency; majority vote; faithful (explanation); reasoning models (pointer to `frontier`); structured output; JSON; JSON Schema; constrained decoding; grammar; context-free grammar; prefill; context rot (labelled a vendor term); primacy; recency; needle in a haystack; effective context length; context management; compaction; context editing; memory tool; chain of command; instruction hierarchy; prompt injection; SQL injection; goal hijacking; prompt leaking; jailbreak (plain usage, unsourced); indirect prompt injection; knowledge cutoff.

Not defined (left out): JSON mode (named only in the ledger now; cut from the prose for length), finite-state machine, developer message as a bold term (quoted from OpenAI instead), untrusted data as a bold term (covered by the Model Spec quote).

## Drafting notes

How the disputes were handled:

- **PRD1 (how in-context learning works):** presented as task location (Reynolds and McDonell; Min et al.'s strict vs broad senses), label mapping (Yoo et al.; Wei et al. 2023), Bayesian latent concept (Xie et al., with their LDA bridge and the exact-fit and synthetic-data limits), gradient descent (von Oswald et al., toy regression; Shen et al.'s "open hypothesis"), and induction heads (Olsson et al., causal in small attention-only models, correlational in large). Closing paragraph says they answer different questions and none settles it.
- **PRD2 (labels):** "held on average for the models and tasks of 2022, not in general", with Wei et al. 2023's own "consistent with Min et al.".
- **PRD3 (faithfulness):** both sides given (Turpin, Lanham, Chen against; Wei's ablations, Lanham's filler result, Korbak's architectural argument for), the ledger's suggested wording used nearly verbatim, and the bridge to `attention`'s "a picture of attention is not a proof".
- **PRD4 (who started step-by-step):** a sequence: Reynolds and McDonell (Feb 2021), Nye et al. (Nov 2021), Wei et al. (Jan 2022, named and measured), Kojima et al. (May 2022).
- **PRD5 (order sensitivity priority):** both cited; parenthetical notes Lu et al.'s "no earlier work" sentence and that Zhao et al.'s preprint came two months earlier; "near-simultaneous", no adjudication.
- **PRD6 (why injection persists):** NCSC ("only ever 'next token'") and OWASP ("stochastic influence") both given and called compatible; Willison's SQL analogy and the NCSC's argument that it misleads both given; vendor statements (OpenAI Dec 2025, Anthropic Nov 2025) and Wallace et al.'s trained hierarchy as "lowers the rate".
- **PRD7 (inconsistent numbers):** Wei et al.'s 56.9 and Wang et al.'s 56.5 each compared only within its own paper, with a sentence saying so; Kojima's 48.7 few-shot-CoT not used; Olsson "about 13 billion"; Kalai's penalty at t = 0.75 given as the formula's 3, the printed 2 not repeated; Sclar's 56-point GPT-3.5 spread cut for length.
- **PRD8 (format restrictions and reasoning):** Tam et al. as "one 2024 study", with the dispute noted as unchecked blog posts, plus the vendors' own advice to leave room for reasoning (OpenAI 2024, Anthropic 2026-11).
- **PRD9 (dating long-context results):** models dated (mid-2023, 2024); the text says neither study tested 2026 models and does not claim the U-shape holds or was fixed; vendor advice to put the query last is quoted as a vendor statement.

Other notes for the checker:

- **Citations without a page.** `olsson2022context` has no printed page numbers, so it is cited without a locator (the PDF pages are in PR9). `liu2024lost` is the TACL article, but the per-position values (75.8, 53.8, 63.2) and the 2,946.2-token average come only from the arXiv v3 appendix (PDF pp. 17-18); those are cited as `[@liu2024lost]` without a page, with "(values from the appendix tables of the paper's arXiv version)" in the prose. If the author prefers, a separate bib entry for arXiv 2307.03172v3 would allow a page.
- **Wei et al.'s ~100B threshold.** The prose quotes it and adds that their own Table 2 shows PaLM 62B gaining 20.3 points; this is arithmetic on printed values, not a claim from the paper.
- **Model names.** Kojima et al.'s model is named text-davinci-002 ("an instruction-tuned GPT-3 model"), per PR17's "InstructGPT model (text-davinci-002)"; Wei et al. 2023's text-davinci-002 is called only "one large model".
- **Korbak et al.** described as "authors from several AI companies and the UK AI Security Institute" (PR19 note); first author's name not used.
- **Anthropic 1% figure** stated with its conditions shortened to "its own adaptive attacker"; the 100-attempt detail was cut for length.
- **Jailbreak vs injection** is given as common usage without a source, as the ledger allows.
- **Bagging** comparison is flagged in the prose as this book's, not Wang et al.'s.
- **Zhao et al.'s prompt** is printed as a block quote with explicit line breaks; Book 1 has no code blocks [D-003], and `tools/check.py` passes.
- **Header typo in this ledger:** the opening paragraph says Reynolds and McDonell Fig. 3 is "see PR50"; the entry is PR45. Left unedited.

Left out (in the ledger, not in the chapter), mostly for length: Xie et al.'s Einstein/Gandhi/Curie example; Olsson et al.'s 0.15 and 0.4 nats (nats are defined in `scale` and `training`, so this can be restored), fuzzy induction heads, and the shared-latent-variable caveat; Min et al.'s synthetic-task limitation; Yoo et al.'s Fig. 1 caption; Lu et al.'s 64! and 13% improvement; Zhao et al.'s 16-example variance; Sclar et al.'s GPT-3.5 spreads; Kojima et al.'s answer-extraction phrase, commonsense numbers, and several Table 4 wordings; Wang et al.'s other benchmarks; Turpin et al.'s suggested-answer bias and decoding temperatures; Reynolds and McDonell's "premature verdicts" sentence (PR45); Chen et al.'s 1% lower bound; Willard and Louf's finite-state machine framing; OpenAI's JSON mode history, the gpt-4-0613 "less than 40%" comparison, the FSM vs CFG remark, and the whitespace warning (`openai2026structured` is cited only for offering the feature); Anthropic's 24-hour grammar cache and 200k windows; Liu et al.'s query-aware contextualization, base-model U-curve, and 10/30-document tables; Hsieh et al.'s 85.6% threshold and GPT-4's 96.6 to 81.2; Anthropic's role-prompting advice; Wallace et al.'s email example (PR36); OpenAI's 7 November 2025 post (`openai2025promptinjections`, not cited); OWASP's "fool-proof" sentence.

No `TODO-VERIFY` markers. No new bib keys.
