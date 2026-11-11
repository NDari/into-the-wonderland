# Claim ledger: tools

Chapter: `tools` (Book 1, chapter 21, "Giving models knowledge and tools").
Stage: verified, 2026-11-11 [D-005]. Research by a helper agent; drafted by a drafting agent from this ledger; independent check recorded at the end.
Every source below was fetched on 2026-11-11 and each claim was located in the fetched text (pdftotext, plain and `-layout`, on publisher, ACL Anthology, PMLR, or arXiv PDFs, all with text layers; Markdown or HTML for vendor pages). Lewis et al. Fig. 2 and Table 3 (p. 7) were checked on the page image. Page numbers are the printed page numbers of the source as read; the offset from PDF page to printed page is given in the table. Where a source prints an en-dash or em-dash (page ranges, "9%-19%", "Retrieval-Augmented", parenthetical dashes), it is written here with a hyphen or replaced by a comma. Arrows printed in sources are written as "->" or in words. Numbers labelled "computed" were produced in this session by a throwaway script (`scripts/toy.py` in the scratchpad), not by `code/checks/tools.py`; the chapter's numbers come from that script, whose output matches these where both exist [D-009].

Vendor documentation is primary for the vendor's own products and is date-stamped "as of 2026-11". Vendor blog posts are primary for what the vendor announced and when, and for the vendor's own reported experiments, but those experiments are not peer reviewed and are labelled as such.

## Sources and how they were read

| Key | Read from | Notes |
|---|---|---|
| `lewis2020retrieval` | https://arxiv.org/pdf/2005.11401v4 | arXiv v4 (12 Apr 2021); v1 22 May 2020; arXiv comment "Accepted at NeurIPS 2020"; NeurIPS 2020 proceedings page fetched (title and "Advances in Neural Information Processing Systems 33 (NeurIPS 2020)"). Printed page = PDF page (pp. 1-19). Fig. 2 and Table 3 read on the page image (p. 7). |
| `guu2020realm` | https://arxiv.org/pdf/2002.08909v1 | arXiv v1 (10 Feb 2020), Google Research. No printed page numbers; pages cited are PDF pages. PMLR page fetched: ICML 2020, PMLR 119:3929-3938, title there "Retrieval Augmented Language Model Pre-Training". |
| `khandelwal2020generalization` | https://arxiv.org/pdf/1911.00172v2 | arXiv v2 (15 Feb 2020), header "Published as a conference paper at ICLR 2020"; v1 1 Nov 2019. Printed page = PDF page. Optional source. |
| `karpukhin2020dense` | https://aclanthology.org/2020.emnlp-main.550.pdf | Footer: EMNLP 2020, pages 6769-6781, November 16-20, 2020. Printed page = PDF page + 6768. Table 2 read in the `-layout` extraction. |
| `robertson2009probabilistic` | https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf | Authors' copy; first page prints "Foundations and Trends in Information Retrieval Vol. 3, No. 4 (2009) 333-389", DOI 10.1561/1500000019. Printed page = PDF page + 330. Equations (3.3), (3.12)-(3.15) read in the `-layout` extraction (pp. 349, 359-360). Crossref gives different volume and pages (TLD7). |
| `sparckjones1972statistical` | https://www.staff.city.ac.uk/~sbrp622/idfpapers/ksj_orig.pdf | The 2004 reprint (Journal of Documentation 60(5), 493-502), "previously from" J. Doc. 28(1) 1972 pp. 11-21. No printed page numbers; pages cited are PDF pages of the reprint (pp. 1-9). DOIs of both from Crossref. |
| `jurafsky2026ir` | https://web.stanford.edu/~jurafsky/slp3/11.pdf | SLP3 chapter 11 "Information Retrieval and Retrieval-Augmented Generation", "Draft of August 19, 2026" (PDF creation date the same). Printed page = PDF page. Authoritative secondary (textbook). |
| `reimers2019sentence` | https://aclanthology.org/D19-1410.pdf | Footer: EMNLP-IJCNLP 2019, Hong Kong. Printed page = PDF page + 3981 (pp. 3982-3992). |
| `muennighoff2023mteb` | https://aclanthology.org/2023.eacl-main.148.pdf | Footer: EACL 2023, pages 2014-2037, May 2-6, 2023. Printed page = PDF page + 2013. |
| `malkov2020efficient` | https://arxiv.org/pdf/1603.09320v4 | arXiv v4 (14 Aug 2018); v1 30 Mar 2016. Journal: IEEE TPAMI 42(4) 824-836, 2020, DOI 10.1109/TPAMI.2018.2889473 (Crossref). Printed page = PDF page of the arXiv copy. Only the abstract and introduction were used. |
| `johnson2021billion` | https://arxiv.org/pdf/1702.08734v1 | arXiv v1 (28 Feb 2017), Facebook AI Research. Journal: IEEE Transactions on Big Data 7(3) 535-547, issue dated 2021, DOI 10.1109/TBDATA.2019.2921572 (Crossref). Printed page = PDF page of the arXiv copy. |
| `gao2023enabling` | https://aclanthology.org/2023.emnlp-main.398.pdf | Footer: EMNLP 2023, pages 6465-6488, December 6-10, 2023. Printed page = PDF page + 6464. |
| `liu2023evaluating` | https://aclanthology.org/2023.findings-emnlp.467.pdf | Footer: Findings of EMNLP 2023, pages 7001-7025. Printed page = PDF page + 7000. |
| `liu2024lost` | https://aclanthology.org/2024.tacl-1.9.pdf | TACL vol. 12, pp. 157-173, 2024 (printed on p. 157). Printed page = PDF page + 156. Author list checked against arXiv 2307.03172 metadata. |
| `schick2023toolformer` | https://arxiv.org/pdf/2302.04761v1 | arXiv v1 (9 Feb 2023), Meta AI Research. No printed page numbers; pages cited are PDF pages. |
| `yao2023react` | https://arxiv.org/pdf/2210.03629v3 | arXiv v3 (10 Mar 2023), header "Published as a conference paper at ICLR 2023"; v1 6 Oct 2022. Printed page = PDF page. Tables 1 and 2 read in the `-layout` extraction (pp. 5-6). |
| `nakano2021webgpt` | https://arxiv.org/pdf/2112.09332v3 | arXiv v3 (1 Jun 2022); v1 17 Dec 2021. OpenAI. Printed page = PDF page. |
| `karpas2022mrkl` | https://arxiv.org/pdf/2205.00445v1 | arXiv v1 (1 May 2022; PDF dated May 3, 2022), AI21 Labs. Printed page = PDF page. Optional source. |
| `greshake2023not` | https://arxiv.org/pdf/2302.12173v2 | arXiv v2 (5 May 2023); v1 23 Feb 2023. Venue (AISec '23, pp. 79-90, DOI 10.1145/3605764.3623985, issued 26 Nov 2023) from Crossref; workshop version not read. Printed page = PDF page of the arXiv copy. |
| `cheng2024dated` | https://arxiv.org/pdf/2403.12958v2 | arXiv v2 (17 Sep 2024), header "Published as a conference paper at COLM 2024"; v1 19 Mar 2024. Abstract used. |
| `grattafiori2024llama` (existing key) | https://arxiv.org/pdf/2407.21783v3 | As in `book1/sources/destination.md`. Printed page = PDF page. Section 4.3.5 "Tool Use" pp. 24-25 used here. |
| `openai2023gpt4` (existing key) | https://arxiv.org/pdf/2303.08774v6 | As in `book1/sources/generation.md`. Printed page = PDF page. p. 10 and its footnote 10 used. |
| `meta2024llama31card` | https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md | Model card, main branch, read 2026-11-11. |
| `openai2023chatgptplugins` | https://openai.com/index/chatgpt-plugins/ | Dated March 23, 2023; banner "This launch post is outdated." HTML, text extracted. |
| `openai2023functioncalling` | https://openai.com/index/function-calling-and-other-api-updates/ | Dated June 13, 2023 (with a July 20, 2023 update note). HTML, text extracted. |
| `anthropic2024tooluse` | https://www.anthropic.com/news/tool-use-ga | Dated May 30, 2024. HTML. |
| `anthropic2024mcp` | https://www.anthropic.com/news/model-context-protocol | "Published Nov 25, 2024". HTML. |
| `anthropic2024contextual` | https://www.anthropic.com/news/contextual-retrieval | "Published Sep 19, 2024". HTML. Vendor experiments, not peer reviewed. |
| `mcp2024specification` | https://modelcontextprotocol.io/specification/2024-11-05/index.md | First published spec version; index page only. |
| `mcp2026specification` | https://modelcontextprotocol.io/specification/latest.md and .../2026-07-28/server/tools.md | "latest" resolved to version 2026-07-28 (schema path `schema/2026-07-28/schema.ts`). As of 2026-11. |
| `anthropic2026tooluse` | https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md | As of 2026-11-11. |
| `anthropic2026howtooluse` | https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works.md | As of 2026-11-11. |
| `anthropic2026definetools` | https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use.md (serves "Define tools", url .../define-tools) | As of 2026-11-11. |
| `anthropic2026models` | https://platform.claude.com/docs/en/about-claude/models/overview.md | As of 2026-11-11. |
| `anthropic2026embeddings` | https://platform.claude.com/docs/en/build-with-claude/embeddings.md | As of 2026-11-11. |
| `anthropic2026stopreasons` (existing key) | as in `book1/sources/generation.md` | Not re-fetched; `anthropic2026howtooluse` carries the tool-use loop quotes. |
| `openai2026functioncalling` | https://developers.openai.com/api/docs/guides/function-calling (HTML and `.md`) | As of 2026-11-11. |
| `openai2026retrieval` | https://developers.openai.com/api/docs/guides/retrieval.md | As of 2026-11-11. |
| `openai2026models` | https://developers.openai.com/api/docs/models | As of 2026-11-11. HTML, text extracted. |
| `openai2026embeddings` | https://developers.openai.com/api/docs/guides/embeddings.md | Title "Vector embeddings". As of 2026-11-11. |

Existing keys this chapter will also cite without new reading: `deerwester1990indexing` (LSA, via `embeddings`), `devlin2019bert` (BERT, via `pretraining`), `anthropic2026contextwindows`, `anthropic2026glossary` (context window as working memory, via `generation`), `openai2026chatcreate`.

### Not fetched

- Robertson and Walker (1994), "Some simple effective approximations to the 2-Poisson model", SIGIR '94, pp. 232-241: the original BM25 paper. Known only through `robertson2009probabilistic` (reference [46], p. 388; "the original BM25 [46] was a little more complicated than that of Equation (3.15)", p. 361). If the chapter names 1994 as BM25's date, cite Robertson and Zaragoza for it, or fetch the original.
- Robertson et al., "Okapi at TREC-3" (1994/1995): not fetched.
- Salton's tf-idf and vector space papers (1968, 1975, 1988): not fetched; tf-idf is cited from `jurafsky2026ir` and the idf idea from `sparckjones1972statistical`.
- Manning, Raghavan, Schutze, *Introduction to Information Retrieval* (2008): the nlp.stanford.edu IR-book pages did not respond in this session; not used.
- Lee, Chang, Toutanova (2019), ORQA, and Chen et al. (2017), DrQA: cited inside Lewis, REALM and DPR; not fetched.
- Izacard and Grave (2021), Fusion-in-Decoder; Borgeaud et al. (2022), RETRO: not fetched (candidates if the author wants more of the 2020-2022 retrieval history).
- Microsoft's Bing Chat announcement (February 2023): not fetched; Bing Chat is mentioned only via `greshake2023not` and `liu2023evaluating`.
- MCP governance (any move of MCP to a foundation): the governance page was fetched but says nothing about a foundation; no claim made. See "Leads".
- Toolformer's NeurIPS 2023 version: not checked.
- Voyage AI's own model pages and blog: not fetched; dimensions come from Anthropic's page (`anthropic2026embeddings`).
- A current MTEB leaderboard snapshot: not fetched (the leaderboard is a moving web app; the paper is cited instead).

## Sourced claims

### A. What the weights cannot know: the knowledge cutoff

### TL1. A trained model is static; its knowledge is fixed at training time
- Sources: `jurafsky2026ir`, `lewis2020retrieval`, `guu2020realm`.
- SLP3 ch. 11, p. 2: "A final issue with using large language models to answer knowledge questions is that they are static; they were pretrained once, at a particular time. This means that LLMs cannot talk about about rapidly changing information (like something that happened last week) since they won't have up-to-date information from after their release data." (the doubled "about" and "release data" are in the source). Also p. 2, proprietary data: "prompting a large language model to answer from its pretrained parameters doesn't allow us to ask questions about proprietary data". And hallucination: "Large language models hallucinate. A hallucination is a response that is not faithful to the facts of the world."
- Lewis et al., p. 1: pre-trained models learn knowledge "without any access to an external memory, as a parameterized implicit knowledge base", but "They cannot easily expand or revise their memory, can't straightforwardly provide insight into their predictions, and may produce "hallucinations"".
- REALM, p. 1 (PDF page): knowledge "is stored implicitly in the parameters of a neural network, requiring ever-larger networks to cover more facts"; "storage space is limited by the size of the network".
- Note: `destination` already promised this chapter: "the parameters contain nothing from after the text the model was trained on" (destination.md, line 127). `generation` defined hallucination; reuse its terms.

### TL2. Published cutoffs are dated, and lag the release
- Sources: `grattafiori2024llama`, `meta2024llama31card`, `openai2023gpt4`.
- Llama 3, p. 4 (already in `book1/sources/training.md`): "We create our dataset for language model pre-training from a variety of data sources containing knowledge until the end of 2023." p. 14: "added more recent web data in the later stages of pre-training to advance the model's knowledge cut-off".
- Llama 3.1 model card: table column "Knowledge cutoff" = "December 2023" for 8B, 70B, 405B; "Data Freshness: The pretraining data has a cutoff of December 2023."; "Model Release Date: July 23, 2024."
- GPT-4 Technical Report, p. 10: "GPT-4 generally lacks knowledge of events that have occurred after the vast majority of its pre-training data cuts off in September 2021, and does not learn from its experience." Footnote 10: "The pre-training and post-training data contain a small amount of more recent data".
- Note: the gap between cutoff and release for Llama 3.1 is about seven months (December 2023 to 23 July 2024; computed). A model is then used for months or years after release, so the gap a user meets grows. Say so as arithmetic, not as a sourced general rule.

### TL3. Cutoffs as vendors state them now (as of 2026-11)
- Sources: `anthropic2026models`, `openai2026models`.
- Anthropic models overview (as of 2026-11-11): rows "Reliable knowledge cutoff" and "Training data cutoff", both "Jun 2026" for Claude Fable 5.2, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5. Definition in the notes: "Reliable knowledge cutoff: The date through which the model's knowledge is most extensive and reliable. Training data cutoff (under Additional details) is the broader range of data used."
- OpenAI models page (as of 2026-11-11): "Knowledge cutoff Apr 30, 2026" for gpt-6-astra and gpt-6.1-sol; "Jun 1, 2026" for gpt-6.1-terra; "May 18, 2026" for gpt-6-luna.
- Note: two vendors, two definitions. Anthropic distinguishes a "reliable" cutoff from the data cutoff; OpenAI gives one date. Use these only as dated examples. Do not name a "current" model without "as of 2026-11".

### TL4. The effective cutoff is not the reported one
- Source: `cheng2024dated`, abstract (p. 1).
- Quotes: "Large Language Models (LLMs) are often paired with a reported cutoff date, the time at which training data was gathered." "We define the notion of an effective cutoff, which is distinct from the LLM's reported cutoff and differs between sub-resources." "we find that effective cutoffs often drastically differ from reported cutoffs." Two reasons: "(1) temporal misalignments of CommonCrawl data due to non-trivial amounts of old data in new dumps; and (2) complications in LLM deduplication schemes involving semantic duplicates and lexical near-duplicates."
- Note: pairs with GPT-4's "vast majority" wording and Anthropic's two cutoff rows: a cutoff is a fuzzy edge, not a wall. Studied on open models (Pythia, OLMo, etc.); do not generalize the size of the effect to closed models.

### TL5. The two things a model alone cannot do: know new facts, and act
- Sources: `openai2023chatgptplugins`, `anthropic2026howtooluse`, `grattafiori2024llama`, `karpas2022mrkl`.
- OpenAI, ChatGPT plugins (23 March 2023): "Language models today, while useful for a variety of tasks, are still limited. The only information they can learn from is their training data. This information can be out-of-date and is one-size fits all across applications. Furthermore, the only thing language models can do out-of-the-box is emit text. This text can contain useful instructions, but to actually follow these instructions you need another process." Plugins give "access to information that is too recent, too personal, or too specific to be included in the training data."
- Anthropic, How tool use works (as of 2026-11): tool use fits "Fresh or external data. Current prices, today's weather, the contents of a database. Anything outside the training data or specific to your system needs a tool to fetch it." and "Actions with side effects. ... The model can describe these actions, but only a tool can perform them."
- Llama 3, p. 24: "Llama 3 is trained to use Brave Search to answer questions about recent events that go beyond its knowledge cutoff or that require retrieving a particular piece of information from the web."
- MRKL, p. 13: LMs' limitations: "a lack of current and/or proprietary information, and an inability to reason symbolically when needed."
- Note: this is the chapter's two-part spine: retrieval puts missing text into the context window; tools let the surrounding program do things. Both work only through text in the context window (`generation`).

### B. The bridge: classical information retrieval

### TL6. Information retrieval vocabulary; sparse and dense retrieval
- Source: `jurafsky2026ir`, p. 3.
- "Information retrieval or IR is the name of the field encompassing the retrieval of all manner of media based on user information needs." "The IR task we consider is called ad hoc retrieval, in which a user poses a query to a retrieval system, which then returns an ordered set of documents from some collection. A document refers to whatever unit of text the system indexes and retrieves (web pages, scientific papers, news articles, or even shorter passages like paragraphs)." "There are two classes of IR systems, based on the two classes of vectors that are used to represent queries and documents: sparse vectors and dense vectors." "In sparse retrieval, we represent documents and queries with count vectors, weighted by tf-idf or BM25."
- Also p. 5: the term-document matrix of four Shakespeare plays (counts of battle, good, fool, wit), "if two documents have similar words their column vectors will tend to be similar."
- Note: the reader of 2000s data science knows this; the chapter's bridge sentence in the outline ("classical information retrieval with learned vectors in place of keyword scores") rests here.

### TL7. tf-idf, and the idea of inverse document frequency (1972)
- Sources: `jurafsky2026ir`, `sparckjones1972statistical`.
- SLP3, pp. 5-6: "Tf-idf (the '-' here is a hyphen, not a minus sign) is the product of two terms, the term frequency tf and the inverse document frequency idf." tf: "1 + log10 count(t, d) if count(t, d) > 0, 0 otherwise" (Eq. 11.4), with "a word appearing 100 times in a document doesn't make that word 100 times more likely to be relevant". idf: "idf_t = log10 (N / df_t)" (Eq. 11.5), "where N is the total number of documents in the collection, and df_t is the number of documents in which term t occurs"; "the lowest weight of 0 is assigned to terms that occur in every document." tf-idf(t, d) = tf_t,d x idf_t (Eq. 11.6). Example idf values over 37 Shakespeare plays: Romeo df 1 idf 1.57; salad 2, 1.27; Falstaff 4, 0.967; forest 12, 0.489; battle 21, 0.246; wit 34, 0.037; fool 36, 0.012; good 37, 0; sweet 37, 0.
- Sparck Jones 1972 (reprint, PDF p. 6): "we should treat matches on non-frequent terms as more valuable than ones on frequent terms, without disregarding the latter altogether. The natural solution is to correlate a term's matching value with its collection frequency." Weight: "Let f(n) = m such that 2^(m-1) < n <= 2^m. Then where there are N documents in the collection, the weight of a term which occurs n times is f(N) - f(n) + 1. For the Cranfield collection with 200 documents, for example, this means that a term occurring ninety times has weight 2, while one occurring three times has weight 7." Abstract (p. 1): "terms should be weighted according to collection frequency, so that matches on less frequent, more specific, terms are of greater value than matches on frequent terms."
- SLP3 attributes idf to "(Sparck Jones, 1972)" (p. 6).
- Note: Sparck Jones's weight is a base-2 logarithm in integer steps, the same idea as log(N/n). The arithmetic of her two examples is in the D-009 list (item 3).

### TL8. BM25: tf-idf with saturation and length normalization
- Source: `robertson2009probabilistic`.
- p. 334: "The best-known instantiation of the model is the BM25 term-weighting and document-scoring function." "The model has been developed in stages over a period of about 30 years, with a precursor in 1960."
- idf form, p. 349 (Eq. 3.3): with no relevance information the Robertson/Sparck Jones weight becomes "a close approximation to classical idf": w_i^IDF = log((N - n_i + 0.5) / (n_i + 0.5)), with "N - Size of the whole collection; n_i - Number of documents in the collection containing t_i".
- Saturation, p. 356: "any one term's contribution to the document score cannot exceed a saturation point (the asymptotic limit), however, frequently it occurs in the document. This turns out to be a very valuable property".
- Length normalization, p. 359: verbosity vs scope hypotheses ("Some authors are simply more verbose than others"; "Some authors have more to say"); B := (1 - b) + b (dl / avdl), 0 <= b <= 1 (Eq. 3.12); "setting b = 1 will perform full document-length normalisation, while b = 0 will switch normalisation off."
- The formula, p. 360 (Eq. 3.15): w_i^BM25(tf) = tf / (k1 ((1 - b) + b dl/avdl) + tf) x w_i^RSJ. "This is the classic BM25 term-weighting and document-scoring function. ... the full document score is obtained by summing these term-weights over the (original or expanded) set of query terms."
- p. 360: "the BM25 weight looks very much like a traditional tf*idf weight - a product of two components, one based on tf and one on idf. However, there is one significant difference. The tf component involves the saturation function". Parameters: "the model provides no guidance on how these should be set"; experiments "suggest that in general values such as 0.5 < b < 0.8 and 1.2 < k1 < 2 are reasonably good in many circumstances." p. 361: "However, there is also evidence that optimal values do depend on other factors".
- Variants, p. 361: "the original BM25 [46] was a little more complicated than that of Equation (3.15)"; "A common variant is to add a (k1 + 1) component to the numerator of the saturation function. This is the same for all terms, and therefore does not affect the ranking produced." "A common combination would be b = 0.5 and k1 = 2."
- Origin: reference [46] is "S. E. Robertson and S. Walker, "Some Simple Effective Approximations to the 2-Poisson Model for Probabilistic Weighted Retrieval," in Proceedings of the 17th Annual International ACM SIGIR Conference ..., pp. 232-241, ACM/Springer, 1994." (p. 388). The 1994 paper itself was not fetched.
- DPR's settings (`karpukhin2020dense` p. 6773, footnote 9): "Lucene implementation. BM25 parameters b = 0.4 (document length normalization) and k1 = 0.9 (term frequency scaling) are tuned using development sets." (outside the survey's suggested range; TLD6).
- Note: a formula is allowed by D-002 only in standard form with every symbol explained. The saturation idea is clearer as numbers (D-009 item 4) than as the formula; recommend numbers in text and, at most, the formula once.

### TL9. The inverted index: why keyword search is fast
- Sources: `jurafsky2026ir`, `karpukhin2020dense`.
- SLP3, p. 9: "The data structure for this task is the inverted index ... An inverted index, given a query term, gives a list of documents that contain the term. It consists of two parts, a dictionary and the postings." "(Any document that contains none of the query terms will have a score of 0 and can be ignored.)" Stop lists: "high-frequency terms (often function words like the, a, to) carry little semantic weight"; "In modern IR systems, the use of stop lists is much less common ... much of their function is already handled by IDF weighting".
- DPR, p. 6769, footnote 1: "Retrieval in open-domain QA is usually implemented using TF-IDF or BM25 (Robertson and Zaragoza, 2009), which matches keywords efficiently with an inverted index and can be seen as representing the question and context in high-dimensional, sparse vectors (with weighting)."

### TL10. The weakness of keywords, and the dense alternative
- Sources: `karpukhin2020dense`, `openai2026retrieval`, `anthropic2024contextual`.
- DPR, p. 6769: "the dense, latent semantic encoding is complementary to sparse representations by design. For example, synonyms or paraphrases that consist of completely different tokens may still be mapped to vectors close to each other. Consider the question "Who is the bad guy in lord of the rings?", which can be answered from the context "Sala Baker is best known for portraying the villain Sauron in the Lord of the Rings trilogy." A term-based system would have difficulty retrieving such a context, while a dense retrieval system would be able to better match "bad guy" with "villain" and fetch the correct context."
- OpenAI Retrieval guide (as of 2026-11): for the query "When did we go to the moon?": "The first lunar landing occurred in July of 1969." Keyword Similarity 0%, Semantic Similarity 65%; "The first man on the moon was Neil Armstrong." 27%, 43%; "When I ate the moon cake, it was delicious." 40%, 28%. "(Keyword similarity uses intersection over union; semantic similarity uses cosine similarity with text-embedding-3-small.)" "Notice how the most relevant result contains none of the words in the search query."
- The reverse weakness, Anthropic (19 Sep 2024): "While embedding models excel at capturing semantic relationships, they can miss crucial exact matches." Example: "Suppose a user queries "Error code TS-999" in a technical support database. An embedding model might find content about error codes in general, but could miss the exact "TS-999" match." DPR Appendix C (p. 6780): BM25 "sensitive to highly selective keywords and phrases, but cannot capture lexical variations or semantic relationships well. In contrast, DPR excels at semantic representation, but might lack sufficient capacity to represent salient phrases which appear rarely." Table 7: "The salient phrase "Thoros of Myr" is critical, and DPR is unable to capture it."
- Bridge to `embeddings`: LSA (Deerwester et al. 1990) was a dense, low-rank answer to the same synonym problem for document retrieval; the embeddings chapter already reports its mixed results. The DPR authors use the phrase "latent semantic encoding". Do not claim DPR descends from LSA; the link is the problem, not a lineage.
- Note: the OpenAI keyword percentages could not be reproduced by plain intersection over union of lowercased words (TLD5); quote them as OpenAI's.

### C. Dense retrieval and embedding models

### TL11. Dense passage retrieval (Karpukhin et al., 2020): two BERT encoders and a dot product
- Source: `karpukhin2020dense`.
- Abstract (p. 6769): "Open-domain question answering relies on efficient passage retrieval to select candidate contexts, where traditional sparse vector space models, such as TF-IDF or BM25, are the de facto method. In this work, we show that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework."
- p. 6771: "DPR applies a different encoder E_Q(.) that maps the input question to a d-dimensional vector, and retrieves k passages of which vectors are the closest to the question vector. We define the similarity between the question and the passage using the dot product of their vectors: sim(q, p) = E_Q(q)^T E_P(p). (1)" "the similarity function needs to be decomposable so that the representations of the collection of passages can be pre-computed." "we use two independent BERT (Devlin et al., 2019) networks (base, uncased) and take the representation at the [CLS] token as the output, so d = 768." "During inference time, we apply the passage encoder E_P to all the passages and index them using FAISS (Johnson et al., 2017) offline."
- Training (p. 6770): "the embedding is optimized for maximizing inner products of the question and relevant passage vectors, with an objective comparing all pairs of questions and passages in a batch."
- Similarity choice (p. 6774): "Besides dot product, cosine and Euclidean L2 distance are also commonly used as decomposable similarity functions. We test these alternatives and find that L2 performs comparable to dot product, and both of them are superior to cosine."
- Corpus (p. 6772): "the English Wikipedia dump from Dec. 20, 2018"; "We then split each article into multiple, disjoint text blocks of 100 words as passages, serving as our basic retrieval units ... which results in 21,015,324 passages in the end. Each passage is also prepended with the title of the Wikipedia article where the passage is from, along with an [SEP] token." Preprocessing "removes semi-structured data, such as tables, infoboxes, lists, as well as the disambiguation pages."
- Note: BERT and [CLS] are defined in `pretraining` (devlin2019bert); this is the first place the book uses BERT as an encoder of whole passages. Bridge: the dot product of `attention` and the cosine of `embeddings`; DPR found cosine slightly worse, which is a nuance worth one sentence, not a rule.

### TL12. DPR's results against BM25
- Source: `karpukhin2020dense`, Table 2 (p. 6773), abstract, p. 6770.
- Abstract: "our dense retriever outperforms a strong Lucene-BM25 system greatly by 9%-19% absolute in terms of top-20 passage retrieval accuracy".
- Table 2, "Top-20 & Top-100 retrieval accuracy on test sets, measured as the percentage of top 20/100 retrieved passages that contain the answer." Top-20, BM25 vs DPR (single-dataset training): NQ 59.1 vs 78.4; TriviaQA 66.9 vs 79.4; WQ 55.0 vs 73.2; TREC 70.9 vs 79.8; SQuAD 68.8 vs 63.2. Top-100: NQ 73.7 vs 85.4; TriviaQA 76.7 vs 85.0; WQ 71.1 vs 81.4; TREC 84.1 vs 89.1; SQuAD 80.0 vs 77.2. BM25 + DPR top-20: NQ 76.6, TriviaQA 79.8, WQ 71.0, TREC 85.2, SQuAD 71.5.
- p. 6773: "With the exception of SQuAD, DPR performs consistently better than BM25 on all datasets. The gap is especially large when k is small (e.g., 78.4% vs. 59.1% for top-20 accuracy on Natural Questions)." SQuAD reasons: "the annotators wrote questions after seeing the passage. As a result, there is a high lexical overlap between passages and questions, which gives BM25 a clear advantage. Second, the data was collected from only 500+ Wikipedia articles".
- p. 6770: DPR "outperforms BM25 by a large margin (65.2% vs. 42.9% in Top-5 accuracy)" and end-to-end QA "41.5% vs. 33.3%" over ORQA on open Natural Questions.
- Combination (p. 6773): "BM25+DPR, using a linear combination of their scores as the new ranking function ... BM25(q,p) + λ . sim(q, p) ... We used λ = 1.1".
- Note: "top-20 accuracy" means the answer string appears in at least one of the 20 passages; define it in plain words. The "9%-19%" range covers four of five datasets; on the fifth, BM25 wins (computed gaps: 19.3, 12.5, 18.2, 8.9, -5.6; D-009 item 7).

### TL13. What dense retrieval costs and saves
- Source: `karpukhin2020dense`, p. 6775.
- "With the help of FAISS in-memory index for real-valued vectors, DPR can be made incredibly efficient, processing 995.0 questions per second, returning top 100 passages per question. In contrast, BM25/Lucene (implemented in Java, using file index) processes 23.7 questions per second per CPU thread." Hardware: "Intel Xeon CPU E5-2698 v4 @ 2.20GHz and 512GB memory."
- "Computing dense embeddings on 21-million passages is resource intensive, but can be easily parallelized, taking roughly 8.8 hours on 8 GPUs. However, building the FAISS index on 21-million vectors on a single server takes 8.5 hours. In comparison, building an inverted index using Lucene is much cheaper and takes only about 30 minutes in total."
- Note: the two speed figures are not like-for-like (whole server vs per CPU thread; in-memory vs file index). Present as the authors' 2020 measurements, not a general ratio.

### TL14. Why not compare the question with every passage directly: cross-encoders vs bi-encoders
- Sources: `reimers2019sentence`, `jurafsky2026ir`.
- Reimers and Gurevych, p. 3982: "BERT uses a cross-encoder: Two sentences are passed to the transformer network and the target value is predicted." "Finding in a collection of n = 10 000 sentences the pair with the highest similarity requires with BERT n.(n-1)/2 = 49 995 000 inference computations. On a modern V100 GPU, this requires about 65 hours." Quora: "answering a single query would require over 50 hours."
- p. 3983: with SBERT "finding the most similar sentence pair in a collection of 10,000 sentences is reduced from 65 hours with BERT to the computation of 10,000 sentence embeddings (~5 seconds with SBERT) and computing cosine-similarity (~0.01 seconds). By using optimized index structures, finding the most similar Quora question can be reduced from 50 hours to a few milliseconds (Johnson et al., 2017)."
- SLP3, p. 14: "the bi-encoder. In this architecture we can encode the documents in the collection only one time by using two separate encoder models, one to encode the query and one to encode the document." "The bi-encoder is much cheaper than a full query/document encoder, but is also less accurate, since its relevance decision can't take full advantage of all the possible meaning interactions between all the tokens in the query and the tokens in the document."
- Note: this is why retrieval is two-stage in many systems (fast vector search, then a slower reranker); `anthropic2024contextual` reports a reranking step (TL30). Keep reranking to one sentence.

### TL15. Sentence embeddings (Sentence-BERT, 2019)
- Source: `reimers2019sentence`.
- Abstract (p. 3982): "we present Sentence-BERT (SBERT), a modification of the pretrained BERT network that use siamese and triplet network structures to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity." Footnote 2: "With semantically meaningful we mean that semantically similar sentences are close in vector space."
- p. 3982: common practice was "to average the BERT output layer (known as BERT embeddings) or by using the output of the first token (the [CLS] token). As we will show, this common practice yields rather bad sentence embeddings, often worse than averaging GloVe embeddings".
- p. 3984: "SBERT adds a pooling operation to the output of BERT / RoBERTa to derive a fixed sized sentence embedding. ... The default configuration is MEAN." "SBERT can be tuned in less than 20 minutes".
- Note: "embedding model" in current practice means a model trained like this: text in, one vector out, trained so that cosine (or dot product) means relevance. Bridge to `embeddings`: GloVe averages are a real (weak) baseline in the paper; the toy example (D-009 item 1) uses them for exactly that reason.

### TL16. Measuring embedding models: MTEB (2022-2023)
- Source: `muennighoff2023mteb`.
- Abstract (p. 2014): "MTEB spans 8 embedding tasks covering a total of 58 datasets and 112 languages. Through the benchmarking of 33 models on MTEB, we establish the most comprehensive benchmark of text embeddings to date. We find that no particular text embedding method dominates across all tasks. This suggests that the field has yet to converge on a universal text embedding method". "MTEB comes with open-source code and a public leaderboard".
- p. 2014: the 8 tasks: "Bitext mining, classification, clustering, pair classification, reranking, retrieval, STS and summarization."
- p. 2020: "We find that performance strongly correlates with model size ... A majority of MTEB tasks are dominated by multi-billion parameter models. However, these come at a significant cost".
- Note: hand-off to `evaluation` (benchmarks, leaderboards). Here: one paragraph, so the reader knows what "tops MTEB" in a model card means. Date-stamp: results are 2022-2023.

### TL17. Embedding models in products (as of 2026-11)
- Sources: `anthropic2026embeddings`, `openai2026embeddings`.
- Anthropic (as of 2026-11-11): "Anthropic does not offer its own embedding model. One embeddings provider with a wide variety of models and capabilities is Voyage AI by MongoDB." Voyage 4 models: "Context length 32,000", "Embedding dimension 1024 (default), 256, 512, 2048" (voyage-4-large, voyage-4, voyage-4-lite, voyage-code-4); voyage-4-nano "2048 (default)", "Open-weight model (Apache 2.0 license)".
- Normalization: "Voyage AI embeddings are normalized to length 1, which means that: Cosine similarity is equivalent to dot-product similarity, although the latter can be computed more quickly. Cosine similarity and Euclidean distance result in identical rankings."
- Query vs document: "For all retrieval tasks and use cases (for example, RAG), use the input_type parameter to specify whether the input text is a query or document." With it, the query is prefixed "Represent the query for retrieving supporting documents: " and a document "Represent the document for retrieval: ".
- Storage: "float: Each returned embedding is a list of 32-bit (4-byte) single-precision floating-point numbers. This is the default"; "int8 and uint8: ... 8-bit (1-byte) integers"; binary: "The length of the returned list of integers is 1/8 of the actual dimension of the embedding." Quantization reduces "storage, memory, and costs by 4x and 32x, respectively."
- OpenAI (as of 2026-11-11): "By default, the length of the embedding vector is 1536 for text-embedding-3-small or 3072 for text-embedding-3-large." Shortening: developers "can shorten embeddings (i.e. remove some numbers from the end of the sequence)".
- Note: the product names are for the D-009 memory arithmetic and as dated examples. No code, parameter names in code font, or API calls in Book 1 [D-003]: "a setting that marks text as a query or a document" is enough.

### D. Finding the nearest vectors fast

### TL18. Retrieval as maximum inner product search, done approximately
- Sources: `lewis2020retrieval`, `jurafsky2026ir`.
- Lewis et al., p. 3: "Calculating top-k(p_eta(.|x)), the list of k documents z with highest prior probability p_eta(z|x), is a Maximum Inner Product Search (MIPS) problem, which can be approximately solved in sub-linear time".
- SLP3, p. 16: "For dense vector algorithms finding the set of dense document vectors that have the highest dot product with a dense query vector is an instance of the problem of nearest neighbor search. Modern systems therefore make use of approximate nearest neighbor vector search algorithms like Faiss (Johnson et al., 2017)." p. 21 (summary): "FAISS is an approximate nearest neighbor vector search algorithm".
- Note: "approximate" means the search may miss some true nearest neighbours in exchange for speed; FAISS reports this as recall ("R@10", TL20). Brute-force cost for DPR's index: 21,015,324 x 768 = about 16.1 billion multiply-adds per query (computed, D-009 item 5).

### TL19. HNSW (2016, journal 2020): a layered graph you walk down
- Source: `malkov2020efficient`, p. 1 (arXiv v4).
- Abstract: "We present a new approach for the approximate K-nearest neighbor search based on navigable small world graphs with controllable hierarchy (Hierarchical NSW, HNSW)." "Hierarchical NSW incrementally builds a multi-layer structure consisting from hierarchical set of proximity graphs (layers) for nested subsets of the stored elements. The maximum layer in which an element is present is selected randomly with an exponentially decaying probability distribution." "Starting search from the upper layer together with utilizing the scale separation boosts the performance compared to NSW and allows a logarithmic complexity scaling." "Similarity of the algorithm to the skip list structure allows straightforward balanced distributed implementation."
- Introduction: "Hierarchical NSW algorithm can be seen as an extension of the probabilistic skip list structure [27] with proximity graphs instead of the linked lists."
- Note: Lewis et al. used it: "build a single MIPS index using FAISS [23] with a Hierarchical Navigable Small World approximation for fast retrieval [37]" (p. 4). For the reader: an analogy to a road map with motorways at the top and side streets at the bottom (an analogy, not from the paper; label it so). Dates: arXiv v1 30 March 2016; journal 2020.

### TL20. FAISS (2017): similarity search at a billion vectors
- Source: `johnson2021billion` (arXiv v1).
- Abstract (p. 1): "We propose a design for k-selection that operates at up to 55% of theoretical peak performance, enabling a nearest neighbor implementation that is 8.5x faster than prior GPU state of the art." "Our implementation enables the construction of a high accuracy k-NN graph on 95 million images from the Yfcc100M dataset in 35 minutes, and of a graph connecting 1 billion vectors in less than 12 hours on 4 Maxwell Titan X GPUs. We have open-sourced our approach".
- p. 1: "Such applications must deal with the curse of dimensionality [46], rendering both exhaustive search or exact indexing for non-exhaustive search impractical on billion-scale databases." "To handle huge datasets that do not fit in RAM, several approaches employ an internal compressed representation of the vectors using an encoding."
- p. 9 (8.5x detail): "with m = 8 bytes per vector, R@10 = 0.376 in 17.7 µs per query vector, versus their reported R@10 = 0.35 in 150 µs per query vector."
- Note: the paper's examples are images; DPR (p. 6771) calls FAISS "an extremely efficient, open-source library for similarity search and clustering of dense vectors, which can easily be applied to billions of vectors." Use FAISS as the name the reader will meet; one sentence on compression ("a few bytes per vector instead of hundreds") ties to the memory arithmetic.

### E. Retrieval-augmented generation

### TL21. REALM (February 2020): retrieval inside pretraining
- Source: `guu2020realm` (PDF pages).
- Abstract (p. 1): "we augment language model pre-training with a latent knowledge retriever, which allows the model to retrieve and attend over documents from a large corpus such as Wikipedia, used during pre-training, fine-tuning and inference. For the first time, we show how to pre-train such a knowledge retriever in an unsupervised manner, using masked language modeling as the learning signal and backpropagating through a retrieval step that considers millions of documents." "we outperform all previous methods by a significant margin (4-16% absolute accuracy), while also providing qualitative benefits such as interpretability and modularity."
- p. 2: "a retrieval that improves the language model's perplexity is helpful and should be rewarded, while an uninformative retrieval should be penalized." Example: to fill "the [MASK] at the top of the pyramid", the retriever should select "The pyramidion on top allows for less material higher up the pyramid".
- p. 6: "Our knowledge corpus is derived from the December 20, 2018 snapshot of English Wikipedia. Documents are greedily split into chunks of up to 288 BERT wordpieces, resulting in just over 13 million retrieval candidates."
- Table 1 (p. 7), NaturalQuestions exact match: REALM 39.2 (pretrained on Wikipedia) and 40.4 (on CC-News); ORQA 33.3; T5 (11b) 34.5.
- Note: REALM came first (10 Feb 2020 vs RAG's 22 May 2020) and Lewis et al. cite it (p. 1). It was built on masked language modelling (`pretraining`), and extracted answers rather than generating them. Credit: TLD1.

### TL22. RAG (Lewis et al., May 2020): parametric and non-parametric memory
- Source: `lewis2020retrieval`.
- Abstract (p. 1): "We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG), models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever." "Pre-trained models with a differentiable access mechanism to explicit non-parametric memory have so far been only investigated for extractive downstream tasks."
- p. 1: "Hybrid models that combine parametric memory with non-parametric (i.e., retrieval-based) memories [20, 26, 48] can address some of these issues because knowledge can be directly revised and expanded, and accessed knowledge can be inspected and interpreted."
- Retriever (p. 3): "We use a pre-trained bi-encoder from DPR to initialize our retriever and to build the document index." "We refer to the document index as the non-parametric memory." Generator: "We use BART-large [32], a pre-trained seq2seq transformer [58] with 400M parameters. To combine the input x with the retrieved content z when generating from BART, we simply concatenate them." "We refer to the BART generator parameters theta as the parametric memory henceforth."
- Corpus (p. 4): "we use the December 2018 dump. Each Wikipedia article is split into disjoint 100-word chunks, to make a total of 21M documents. We use the document encoder to compute an embedding for each document, and build a single MIPS index using FAISS [23] with a Hierarchical Navigable Small World approximation for fast retrieval [37]. During training, we retrieve the top k documents for each query. We consider k in {5, 10} for training".
- Two variants (abstract): "one which conditions on the same retrieved passages across the whole generated sequence, and another which can use different passages per token." Fig. 1 caption (p. 2): "For final prediction y, we treat z as a latent variable and marginalize over seq2seq predictions given different documents."
- Training (Fig. 1 caption): "We combine a pre-trained retriever (Query Encoder + Document Index) with a pre-trained seq2seq model (Generator) and fine-tune end-to-end." Appendix G (p. 18): the document encoder is not trained ("although we do not train the document encoder ourselves"); 626M trainable parameters.
- Note: the name "RAG" comes from this paper; today's usage (retrieve, paste into the prompt of a separately trained LLM) is looser (TLD2). "Parametric" will be familiar to a statistician; the bridge is honest: parametric vs non-parametric models (a fixed set of weights vs a method that keeps the data, like k-nearest neighbours).

### TL23. RAG's results
- Source: `lewis2020retrieval`, Table 1 (p. 6) and text.
- Open-domain QA exact match, test (Table 1): NQ: T5-11B (closed book) 34.5; T5-11B+SSM 36.6; REALM 40.4; DPR 41.5; RAG-Token 44.1; RAG-Sequence 44.5. TQA, WQ, CT also given (RAG-Seq. 56.8/68.0, 45.2, 52.2).
- p. 5: "On all four open-domain QA tasks, RAG sets a new state of the art (only on the T5-comparable split for TQA)." "RAG combines the generation flexibility of the "closed-book" (parametric only) approaches and the performance of "open-book" retrieval-based approaches."
- p. 6: "RAG can generate correct answers even when the correct answer is not in any retrieved document, achieving 11.8% accuracy in such cases for NQ, where an extractive model would score 0%."
- p. 6: "Qualitatively, we find that RAG models hallucinate less and generate factually correct text more often than BART."
- Appendix G (p. 19): "T5-large (770M parameters), which achieves a score of 28.9 EM on Natural Questions [52], substantially below the 44.5 that RAG-Sequence achieves".
- Note: "closed book" vs "open book" is the authors' own vivid pair; use it. Date-stamp: 2020 results on 2018 Wikipedia.

### TL24. Updating knowledge by swapping the index
- Source: `lewis2020retrieval`, pp. 7-8.
- "An advantage of non-parametric memory models like RAG is that knowledge can be easily updated at test time. Parametric-only models like T5 or BART need further training to update their behavior as the world changes." "we build an index using the DrQA [5] Wikipedia dump from December 2016 and compare outputs from RAG using this index to the newer index from our main results (December 2018). We prepare a list of 82 world leaders who had changed between these dates and use a template "Who is {position}?" (e.g. "Who is the President of Peru?")". "RAG answers 70% correctly using the 2016 index for 2016 world leaders and 68% using the 2018 index for 2018 world leaders. Accuracy with mismatched indices is low (12% with the 2018 index and 2016 leaders, 4% with the 2016 index and 2018 leaders). This shows we can update RAG's world knowledge by simply replacing its non-parametric memory."
- Note: this is the cleanest experiment for "retrieval is the cure for the cutoff". The percentages match 57, 56, 10, and 3 of 82 (computed, D-009 item 8); the paper does not print the counts.

### TL25. The key figure's printed example: one RAG trace
- Source: `lewis2020retrieval`, Fig. 2 and Table 3 (p. 7, checked on the page image).
- Fig. 2 caption: "RAG-Token document posterior p(z_i|x, y_i, y_-i) for each generated token for input "Hemingway" for Jeopardy generation with 5 retrieved documents. The posterior for document 1 is high when generating "A Farewell to Arms" and for document 2 when generating "The Sun Also Rises"." The figure prints two of the five retrieved passages: "Document 1: his works are considered classics of American literature ... His wartime experiences formed the basis for his novel "A Farewell to Arms" (1929) ..." and "Document 2: ... artists of the 1920s "Lost Generation" expatriate community. His debut novel, "The Sun Also Rises", was published in 1926." The generated tokens on the x-axis read: "The Sun Also Rises" is a novel by this author of "A Farewell to Arms".
- Table 3 (MS-MARCO input "define middle ear"): BART "?The middle ear is the part of the ear between the middle ear and the nose." (marked factually incorrect); RAG-T "The middle ear is the portion of the ear internal to the eardrum."; RAG-S "The middle ear includes the tympanic cavity and the three ossicles."
- Note: a real, printed input, retrieved passages, and output from the RAG paper: usable in the key figure as a quoted example without inventing any model output [D-009]. See "Figures planned".

### TL26. A textbook statement of "basic RAG" with a separate LLM (2026)
- Source: `jurafsky2026ir`, pp. 16-18.
- p. 17: "The idea of retrieval-augmented generation is to condition on the retrieved passages, jointly with some prompt text, for example like "Based on these texts, answer this question:". Thus given a document collection D and a user query q, the most basic RAG algorithm is: 1. Call a retriever to return R(q) = d1 ... dk, the top-k relevant passages from D 2. Create a prompt that includes q and the retrieved passages 3. Call an LLM with the prompt". Schematic prompt: "retrieved passage 1 / retrieved passage 2 / ... / retrieved passage k / Based on these texts, answer this question: What year was the premiere of The Magic Flute?"
- p. 17: "In the RAG paradigm described so far, a search is always run and then retrieved passages are combined with the user's question in a prompt. But in actual applications, we may not want to run retrieval for every user turn. ... In agent-based RAG, the system decides when to call a retrieval agent and for which collection." (p. 18).
- p. 2: "Basing our answers on retrieved documents ... helps ensure that the answer is grounded in facts from some curated dataset. And the system can give the user the answer accompanied by the context of the passage or document it came from."
- Anthropic (19 Sep 2024): "RAG is a method that retrieves relevant information from a knowledge base and appends it to the user's prompt". Steps: "Break down the knowledge base (the "corpus" of documents) into smaller chunks of text, usually no more than a few hundred tokens; Use an embedding model to convert these chunks into vector embeddings that encode meaning; Store these embeddings in a vector database ... At runtime ... the most relevant chunks are added to the prompt sent to the generative model."
- When not to retrieve (Anthropic, same post): "If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt". (dated September 2024; context windows have since grown, `generation` GN25; TLD8).
- Note: this "paste into the prompt" form is what the reader will meet in practice and what Book 2's `b2-retrieval` builds.

### TL27. kNN-LM (2019-2020, optional): retrieval of next-word examples
- Source: `khandelwal2020generalization`.
- Abstract (p. 1): "We introduce kNN-LMs, which extend a pre-trained neural language model (LM) by linearly interpolating it with a k-nearest neighbors (kNN) model." "our kNN-LM achieves a new state-of-the-art perplexity of 15.79 - a 2.9 point improvement with no additional training." Fig. 1 (p. 2): "A datastore is constructed with an entry for each training set token, and an encoding of its leftward context." Table 1 (p. 4): base LM test perplexity 18.65; +kNN-LM 16.12; +kNN-LM + continuous cache 15.79.
- p. 4: "building the cache with 103M entries takes roughly two hours on a single CPU."
- Note: optional. Shows the reader's own k-nearest-neighbours method inside a language model; perplexity is from `prediction`. The 2.9 vs 2.86 is rounding (18.65 - 15.79 = 2.86, computed).

### TL28. Dense vs keyword retrieval inside RAG
- Source: `lewis2020retrieval`, p. 7 and Table 6 (p. 8).
- "We compare RAG's dense retriever to a word overlap-based BM25 retriever [53]. ... For FEVER, BM25 performs best, perhaps since FEVER claims are heavily entity-centric and thus well-suited for word overlap-based retrieval. Differentiable retrieval improves results on all other tasks, especially for Open-Domain QA, where it is crucial." Table 6 (dev), NQ exact match: RAG-Token-BM25 29.7, RAG-Sequence-BM25 31.8; RAG-Token 43.5, RAG-Sequence 44.0.

### F. Chunking

### TL29. Chunk sizes in the research systems
- Sources: `karpukhin2020dense`, `lewis2020retrieval`, `guu2020realm`, `jurafsky2026ir`.
- DPR (p. 6772): "disjoint text blocks of 100 words as passages, serving as our basic retrieval units", 21,015,324 passages, each "prepended with the title of the Wikipedia article". RAG (p. 4): "disjoint 100-word chunks". REALM (p. 6): "chunks of up to 288 BERT wordpieces", "just over 13 million".
- SLP3, p. 13: "Usually the retrieval step is not done on an entire document. Instead documents are broken up into smaller passages, such as non-overlapping fixed-length chunks of say 100 tokens, and the retriever encodes and retrieves these passages rather than entire documents. The query and document have to be made to fit in the BERT 512-token window".
- Note: two reasons for chunking, both in the sources: the encoder has a fixed input window (SLP3), and the retrieval unit must be small enough to be specific and to fit several into the prompt (ALCE, TL35: "With a 4K context window, we can at most safely fit k = 5 passages"). DPR's title prepending is an early form of "add context to the chunk" (TL30).

### TL30. Chunking in products, and what chunking loses (as of 2026-11; 2024)
- Sources: `openai2026retrieval`, `anthropic2024contextual`.
- OpenAI (as of 2026-11-11): "By default, max_chunk_size_tokens is set to 800 and chunk_overlap_tokens is set to 400, meaning every file is indexed by being split up into 800-token chunks, with 400-token overlap between consecutive chunks." Limits: "max_chunk_size_tokens must be between 100 and 4096 inclusive"; "chunk_overlap_tokens must be non-negative and should not exceed max_chunk_size_tokens / 2." "When you add a file to a vector store it will be automatically chunked, embedded, and indexed."
- Anthropic (19 Sep 2024): "In traditional RAG, documents are typically split into smaller chunks for efficient retrieval. While this approach works well for many applications, it can lead to problems when individual chunks lack sufficient context." Example: question "What was the revenue growth for ACME Corp in Q2 2023?"; chunk "The company's revenue grew by 3% over the previous quarter." "this chunk on its own doesn't specify which company it's referring to or the relevant time period". Their remedy prepends generated context: "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter." "The choice of chunk size, chunk boundary, and chunk overlap can affect retrieval performance".
- Anthropic's reported results (vendor experiments, "1 minus recall@20", average over their domains with "Gemini Text 004" embeddings): "Contextual Embeddings reduced the top-20-chunk retrieval failure rate by 35% (5.7% -> 3.7%)"; with Contextual BM25 "by 49% (5.7% -> 2.9%)"; with reranking "by 67% (5.7% -> 1.9%)".
- Note: no primary peer-reviewed source on chunk size was found in this session; the defensible statements are (a) the research systems used about 100 words, (b) one vendor's default is 800 tokens with 400 overlap (as of 2026-11), (c) chunks lose surrounding context, with one vendor's example and its own measured effect. "Overlap" is new vocabulary: define it as consecutive chunks sharing some text so a sentence cut at a boundary appears whole in one of them.

### TL31. Hybrid search: keywords and vectors together
- Sources: `anthropic2024contextual`, `openai2026retrieval`, `karpukhin2020dense`.
- Anthropic (2024): "By leveraging both BM25 and embedding models, traditional RAG systems can provide more comprehensive and accurate results, balancing precise term matching with broader semantic understanding." Steps include "Combine and deduplicate results ... using rank fusion techniques". Also: "BM25 works by building upon the TF-IDF ... concept ... BM25 refines this by considering document length and applying a saturation function to term frequency".
- OpenAI (as of 2026-11): ranking options let one "control how reciprocal rank fusion balances semantic embedding matches vs. sparse keyword matches."
- DPR (2020): BM25 + 1.1 x DPR score (TL12).
- Note: the book's bridge pays off here: the reader's 2000s keyword scores did not disappear; current systems combine them with learned vectors.

### G. Grounding and citations

### TL32. WebGPT (December 2021): browsing, with references collected on the way
- Source: `nakano2021webgpt`.
- Abstract (p. 1): "We fine-tune GPT-3 to answer long-form questions using a text-based web-browsing environment, which allows the model to search and navigate the web." "To make human evaluation of factual accuracy easier, models must collect references while browsing in support of their answers." "This model's answers are preferred by humans 56% of the time to those of our human demonstrators, and 69% of the time to the highest-voted answer from Reddit."
- Table 1 (p. 3), "Actions the model can take. If a model generates any other text, it is considered to be an invalid action.": "Search <query>" "Send <query> to the Bing API and display a search results page"; "Clicked on link <link ID>"; "Find in page: <text>"; "Quote: <text>" "If <text> is found in the current page, add it as a reference"; "Scrolled down <1, 2, 3>"; "Back"; "End: Answer".
- p. 2: TruthfulQA "Our model's answers are true 75% of the time, and are both true and informative 54% of the time, outperforming our base model (GPT-3), but falling short of human performance."
- p. 11: "references are far from a panacea. Our current procedure incentivizes models to cherry-pick references that they expect labelers to find convincing, even if those references do not reflect a fair assessment of the evidence." p. 9: "WebGPT still sometimes quotes from highly unreliable sources". p. 11, risks of live web access: "if the model had access to forms, it could edit Wikipedia to construct a reliable-looking reference."
- Note: WebGPT is both an early agent loop (the model emits text commands; the environment executes them) and an early grounding-with-citations system. It is the bridge between this section and section H. Its actions are plain text the program parses: the same idea as Toolformer and ReAct.

### TL33. Citations in a RAG answer (textbook)
- Source: `jurafsky2026ir`, pp. 17-18.
- Fig. 11.13 caption: "Some generations include a knowledge citation that can help the user decide whether to trust the generation, or follow up if they are interested." p. 18: "it is generally useful for LLMs to give the user evidence for any factual statement. This can be in the form of knowledge citations, such as URLs of a trusted source or citation references to particular literature." Example: "Q: Which films have Gong Li as a member of their cast? A: The Story of Qiu Ju [1], Farewell My Concubine [2], The Monkey King 2 [3], Mulan [3], Saturday Fiction [3]".
- Note: the Gong Li example is from ALCE (Fig. 3, `gao2023enabling` p. 6468); cite the primary if used.

### TL34. Measuring citations: ALCE (2023)
- Source: `gao2023enabling`.
- Abstract (p. 6465): "our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability." "We propose ALCE, the first benchmark for Automatic LLMs' Citation Evaluation." "on the ELI5 dataset, even the best models lack complete citation support 50% of the time."
- p. 6468: "citation recall, which determines if the output is entirely supported by cited passages, and (2) citation precision, which identifies any irrelevant citations." Checked automatically with an NLI model ("TRUE"): a statement's citation recall is 1 "if and only if there is at least one citation ... and" the cited passages entail it.
- p. 6466 findings: "a closed-book model (generating answers without accessing any retrieved documents) with post-hoc citing achieves good correctness but much worse citation quality"; "interactive retrieval approaches (Yao et al., 2023; Schick et al., 2023) ... do not improve the performance on this challenging benchmark"; "incorporating more retrieved passages in context does not help ChatGPT but improves GPT-4 performance." Challenges: "(1) the retrieval quality is crucial to the final performance and has substantial room for improvement; (2) LLMs' limited context window restricts the number of passages they can incorporate; (3) current LLMs struggle to synthesize multiple documents in context without being distracted by irrelevant ones".
- p. 6469: "With a 4K context window, we can at most safely fit k = 5 passages. ... top-5 retrieved passages can only cover 56.8% percent of the answers in ASQA."
- Note: "NLI" (natural language inference) needs a one-line definition if used: a model that judges whether one text supports another. Date-stamp: 2023 models (ChatGPT, GPT-4).

### TL35. Citations in deployed generative search (February-March 2023)
- Source: `liu2023evaluating`.
- Abstract (p. 7001): "We conduct human evaluation to audit four popular generative search engines - Bing Chat, NeevaAI, perplexity.ai, and YouChat". "responses from existing generative search engines are fluent and appear informative, but frequently contain unsupported statements and inaccurate citations: on average, a mere 51.5% of generated sentences are fully supported by citations and only 74.5% of citations support their associated sentence."
- p. 7002: "citation precision is inversely correlated with perceived utility (r = -0.96); the responses that seem more helpful are often those with inaccurate citations". Hypothesis: "generative search engines often copy or closely paraphrase from their cited webpages". "This facade of trustworthiness increases the potential for existing generative search engines to mislead users."
- p. 7004: "Responses were scraped between late February and late March 2023." ChatGPT and Bard not evaluated "because they do not provide in-line citations for their responses (as of March 2023)".
- Note: must be date-stamped (early 2023 systems, several now discontinued or renamed). The lesson that survives the date: a citation marker is a claim, not a proof; check that the cited text says what the answer says.

### TL36. More retrieved text is not always used well (2023-2024)
- Source: `liu2024lost`.
- p. 158 (Fig. 1 caption): "Changing the location of relevant information (in this case, the position of the passage that answers an input question) within the language model's input context results in a U-shaped performance curve - models are better at using relevant information that occurs at the very beginning (primacy bias) or end of its input context (recency bias), and performance degrades significantly when models must access and use information located in the middle of its input context."
- p. 159: "model performance saturates long before retriever recall saturates, indicating that current models fail to effectively use additional retrieved documents - using 50 documents instead of 20 retrieved documents only marginally improves performance (~1.5% for GPT-3.5-Turbo and ~1% for claude-1.3)."
- Note: date-stamp the models (2023). Hand-off: `prompting` owns context management; this chapter uses it only as a RAG failure mode. Do not state that current models still show the U-shape without a newer source.

### H. Tools: structured text the program acts on

### TL37. Toolformer (February 2023): a tool call is text
- Source: `schick2023toolformer` (PDF pages).
- Abstract (p. 1): "LMs can teach themselves to use external tools via simple APIs". "Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each API." Tools: "a calculator, a Q&A system, a search engine, a translation system, and a calendar."
- Fig. 1 (p. 1) examples, printed inline in text: "The New England Journal of Medicine is a registered trademark of [QA("Who is the publisher of The New England Journal of Medicine?") -> Massachusetts Medical Society] the MMS."; "Out of 1400 participants, 400 (or [Calculator(400 / 1400) -> 0.29] 29%) passed the test."
- p. 2: "We require that inputs and outputs for each API can be represented as text sequences. This allows seamless insertion of API calls into any given text, using special tokens to mark the start and end of each such call." Footnote 1: "In practice, we use the token sequences " [", "]" and "->" to represent "<API>", "</API>" and "->", respectively. This enables our approach to work without modifying the existing LM's vocabulary."
- Inference (p. 4): "When generating text with M after finetuning with our approach, we perform regular decoding until M produces the "->" token, indicating that it next expects the response for an API call. At this point, we interrupt the decoding process, call the appropriate API to get a response, and continue the decoding process after inserting both the response and the </API> token."
- Training filter (Fig. 2, p. 2): "We then execute these API calls and filter out all calls which do not reduce the loss L_i over the next tokens."
- Model (p. 2): "a pretrained GPT-J model ... with 6.7B parameters, achieves much stronger zero-shot results, clearly outperforming a much larger GPT-3 model".
- Limitations (p. 11): "the inability of Toolformer to use tools in a chain (i.e., using the output of one tool as an input for another tool)"; no interactive use; "we found models trained with Toolformer to often be sensitive to the exact wording of their input when deciding whether or not to call an API".
- Note: the clearest statement of the chapter's core mechanism: generation pauses at a marker, the program runs something, the result is pasted into the text, generation resumes. It is the stop reason of `generation` (stop at "->") in research form.

### TL38. MRKL (May 2022, optional): a router over modules
- Source: `karpas2022mrkl`, pp. 1, 4.
- Abstract: "we define a flexible architecture with multiple neural models, complemented by discrete knowledge and reasoning modules. We describe this neuro-symbolic architecture, dubbed the Modular Reasoning, Knowledge and Language (MRKL, pronounced "miracle") system". p. 4: "a MRKL system consists of an extendable set of modules, which we term 'experts', and a router that routes every incoming natural language input to a module that can best respond to the input".
- Note: optional, one sentence at most; shows the "LLM plus calculator plus database" idea was in industry papers before ChatGPT.

### TL39. Tools in deployed assistants (2023 onward), dated
- Sources: `openai2023chatgptplugins`, `openai2023functioncalling`, `anthropic2024tooluse`, `grattafiori2024llama`.
- ChatGPT plugins, 23 March 2023: "We've implemented initial support for plugins in ChatGPT. Plugins are tools designed specifically for language models". Plugin developers' documentation "lists the enabled plugins in the prompt shown to the language model as well as documentation to instruct the model how to use each." First plugins by "Expedia, FiscalNote, Instacart, KAYAK, Klarna, Milo, OpenTable, Shopify, Slack, Speak, Wolfram, and Zapier"; OpenAI hosted "a web browser and code interpreter" and open-sourced "a knowledge base retrieval plugin". Browsing "retrieves content from the web using the Bing search API".
- Function calling, 13 June 2023: "Developers can now describe functions to gpt-4-0613 and gpt-3.5-turbo-0613, and have the model intelligently choose to output a JSON object containing arguments to call those functions." "These models have been fine-tuned to both detect when a function needs to be called (depending on the user's input) and to respond with JSON that adheres to the function signature." Example: "What's the weather like in Boston?" to "get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')".
- Anthropic, 30 May 2024: "Tool use, which enables Claude to interact with external tools and APIs, is now generally available across the entire Claude 3 model family on the Anthropic Messages API, Amazon Bedrock, and Google Cloud's Vertex AI."
- Open weights, Llama 3 (2024), p. 24: "We train Llama 3 to interact with the following tools: Search engine ... Python interpreter ... Mathematical computational engine" (Wolfram Alpha, p. 25). p. 25: "If a query requires multiple tool calls, the model can write a step-by-step plan, call the tools in sequence, and do reasoning after each tool call." "we rely on human annotations and preferences to teach Llama 3 to use tools" (unlike Toolformer).
- Note: the outline's "tool use in deployed assistants (2023 onward)" is supported by these four dated items. Keep product names to the minimum; date every one.

### TL40. Tool definitions are text in the prompt
- Sources: `openai2026functioncalling`, `anthropic2026definetools`, `anthropic2026tooluse`.
- OpenAI (as of 2026-11): "Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model's context limit and are billed as input tokens."
- Anthropic (as of 2026-11), "Tool use system prompt": "When you call the Claude API with the tools parameter, the API constructs a special system prompt from the tool definitions, tool configuration, and any user-specified system prompt." The printed template begins "In this environment you have access to a set of tools you can use to answer the user's question." and includes "Here are the functions available in JSONSchema format: {{ TOOL DEFINITIONS IN JSON SCHEMA }}".
- Anthropic tool use overview (as of 2026-11): extra tokens come from "The tools parameter in API requests (tool names, descriptions, and schemas)", "tool_use content blocks in API requests and responses" and "tool_result content blocks in API requests"; plus a fixed tool-use system prompt, e.g. "Claude Opus 5.5 | 286 tokens".
- A tool definition (Anthropic example): name "get_weather", description "Get the current weather in a given location", and an input schema with a required "location" string and an optional "unit" that must be "celsius" or "fahrenheit".
- Note: the key fact for the reader: the model never sees the tool's code, only a name, a description, and a description of the arguments, all as tokens in its context window (`generation`, `tokens`). This also explains why many tools cost context and money. No JSON in Book 1 [D-003]: describe the definition in words or as a small labelled diagram box, not as code.

### TL41. The loop: the model asks, the program runs, the result goes back in
- Sources: `anthropic2026howtooluse`, `openai2026functioncalling`; existing `anthropic2026stopreasons`.
- Anthropic (as of 2026-11): "Tool use is a contract between your application and the model. You specify what operations are available and what shape their inputs and outputs take; Claude determines when and how to call them. The model never runs anything on its own. It emits a structured request, your code (or Anthropic's servers) runs the operation, and the result flows back into the conversation." "Claude never receives your implementation; it only receives the schema you provided and the result you returned."
- The loop: "Client-executed tools ... require your application to drive a loop. The model can't run your code, so every tool call is a round trip: the model asks, you execute, you report back, the model continues." Steps: "1. Send a request with your tools array and the user message. 2. Claude responds with stop_reason: "tool_use" and one or more tool_use blocks. 3. Run each tool. Format the outputs as tool_result blocks. 4. Send a new request containing the original messages, the assistant's response, and a user message with the tool_result blocks. 5. Repeat from step 2 while stop_reason is "tool_use"." "The loop exits on any other stop reason".
- OpenAI (as of 2026-11): "Tool calling is a multi-step conversation between your application and a model via the OpenAI API. The tool calling flow has five high level steps: Make a request to the model with tools it could call; Receive a tool call from the model; Execute code on the application side with input from the tool call; Make a second request to the model with the tool output; Receive a final response from the model (or more tool calls)". Definitions: "A function call or tool call refers to a special kind of response we can get from the model if it examines a prompt, and then determines that in order to follow the instructions in the prompt, it needs to call one of the tools we made available to it." Example output "The weather in Paris today is 25C." after a tool output "{"temperature": "25", "unit": "C"}".
- Note: this is the outline's "structured text the surrounding program acts on". The hook from `generation` ("tool_use" as a stop reason) is redeemed here. Both vendors' example is the weather; the chapter can use a weather example in prose without quoting code.

### TL42. When a tool is called, and when it is not
- Sources: `anthropic2026tooluse`, `anthropic2026howtooluse`.
- Overview (as of 2026-11): "With the default tool_choice of {"type": "auto"}, Claude determines on each turn whether to call a tool or respond directly. It calls a tool when the request maps to that tool's described capability and the answer isn't already in context. It responds directly for stable knowledge, creative tasks, and conversational turns." "This boundary is steerable through your system prompt."
- How tool use works: tool use does not fit when "The model can answer from training alone." "Every tool call is at least one extra round trip".
- Note: the decision to call a tool is itself next-token prediction over the vocabulary of the chat format; that framing is an inference, consistent with TL37 and TL40, not a vendor statement. Label it as such if used.

### TL43. Guaranteed argument shape (as of 2026-11)
- Sources: `openai2026functioncalling`, `anthropic2026tooluse`.
- OpenAI: "Setting strict to true will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode." "Under the hood, strict mode works by leveraging our structured outputs feature".
- Anthropic: "Add strict: true to your custom tool definitions to ensure Claude's tool calls always match your schema exactly."
- Note: hand-off to `prompting` (structured output). Here one sentence: the shape of a call can be enforced; whether the call is the right one cannot.

### I. The agent loop

### TL44. ReAct (October 2022): thoughts, actions, observations
- Source: `yao2023react`.
- Abstract (p. 1): "we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments."
- p. 3: "we mainly focus on the setup where a frozen large language model, PaLM-540B ..., is prompted with few-shot in-context examples to generate both domain-specific actions and free-form language thoughts for task solving". "we alternate the generation of thoughts and actions so that the task-solving trajectory consists of multiple thought-action-observation steps."
- Action space (p. 4): "(1) search[entity], which returns the first 5 sentences from the corresponding entity wiki page if it exists, or else suggests top-5 similar entities from the Wikipedia search engine, (2) lookup[string], which would return the next sentence in the page containing string, simulating Ctrl+F functionality on the browser. (3) finish[answer], which would finish the current task with answer." "this action space ... is significantly weaker than state-of-the-art lexical or neural retrievers."
- Results, Table 1 (p. 5), PaLM-540B prompting: HotpotQA exact match: Standard 28.7, CoT 29.4, CoT-SC 33.4, Act 25.7, ReAct 27.4, CoT-SC -> ReAct 34.2, ReAct -> CoT-SC 35.1; Fever accuracy: 57.1, 56.3, 60.4, 58.9, 60.9, 64.6, 62.0. p. 6: "ReAct outperforms CoT on Fever (60.9 vs. 56.3) and slightly lags behind CoT on HotpotQA (27.4 vs. 29.4)."
- Abstract: on ALFWorld and WebShop "ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples."
- Trace example (Appendix, p. 16, HotpotQA, Act-only prompt): question "What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?"; "Search[Colorado orogeny]" -> "The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas."; "Lookup[eastern sector]" -> "(Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny."; "Search[High Plains]" ...
- Note: ReAct alone did not beat chain-of-thought on HotpotQA; its advantage was groundedness and the combination. Say this; do not present ReAct as a straight win. "Chain-of-thought" is introduced in `prompting` (earlier chapter); use its term.

### TL45. How the loop fails (ReAct's own analysis)
- Source: `yao2023react`, Table 2 and text (p. 6, `-layout`).
- 200 HotpotQA trajectories labelled by hand ("we randomly sampled 50 trajectories with correct and incorrect answers ... from ReAct and CoT respectively"). Failure modes, ReAct vs CoT: "Reasoning error ... (including failing to recover from repetitive steps)" 47% vs 16%; "Search result error: Search return empty or does not contain useful information" 23% vs -; "Hallucination" 0% vs 56%; "Label ambiguity" 29% vs 28%. Success: "False positive: Hallucinated reasoning trace or facts" 6% vs 14%.
- Text: "Hallucination is a serious problem for CoT, resulting in much higher false positive rate than ReAct (14% vs. 6%) in success mode, and make up its major failure mode (56%)." "there is one frequent error pattern specific to ReAct, in which the model repetitively generates the previous thoughts and actions". "Non-informative search, which counts for 23% of the error cases, derails the model reasoning and gives it a hard time to recover and reformulate thoughts."
- Note: the ReAct failure column sums to 99% (rounding; computed). This gives the chapter its sober "failure modes" numbers for agents: loops and bad retrievals, not only hallucination.

### TL46. The loop in today's products (as of 2026-11)
- Source: `anthropic2026howtooluse`.
- Server-side loop: "Server-executed tools run their own loop inside Anthropic's infrastructure. A single request from your application might trigger several web searches or code executions before a response comes back." "This internal loop has an iteration limit. If the model is still iterating when it hits the cap, the response comes back with stop_reason: "pause_turn" instead of "end_turn"."
- Note: an iteration cap is the product version of ReAct's step limit ("We set 7 and 5 steps for HotpotQA and FEVER respectively", `yao2023react` p. 5). Agents as long-running systems belong to `frontier`.

### J. A standard for connecting tools: the Model Context Protocol

### TL47. MCP announced (25 November 2024)
- Source: `anthropic2024mcp`.
- "Today, we're open-sourcing the Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments." "Every new data source requires its own custom implementation, making truly connected systems difficult to scale. MCP addresses this challenge." "developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers." Three components: "The Model Context Protocol specification and SDKs; Local MCP server support in the Claude Desktop apps; An open-source repository of MCP servers". "pre-built MCP servers for popular enterprise systems like Google Drive, Slack, GitHub, Git, Postgres, and Puppeteer."
- Note: OpenAI's plugin post (March 2023) had predicted "We expect that open standards will emerge to unify the ways in which applications expose an AI-facing interface." (`openai2023chatgptplugins`). A neat, sourced before-and-after.

### TL48. What MCP specifies (versions 2024-11-05 and 2026-07-28)
- Sources: `mcp2024specification`, `mcp2026specification`.
- Both index pages (2024-11-05 and 2026-07-28): "The protocol uses JSON-RPC 2.0 messages to establish communication between: Hosts: LLM applications that initiate connections; Clients: Connectors within the host application; Servers: Services that provide context and capabilities". "MCP takes some inspiration from the Language Server Protocol, which standardizes how to add support for programming languages across a whole ecosystem of development tools."
- 2026-07-28 index: servers offer "Resources: Context and data, for the user or the AI model to use; Prompts: Templated messages and workflows for users; Tools: Functions for the AI model to execute". Security: "Tools represent arbitrary code execution and must be treated with appropriate caution." "descriptions of tool behavior such as annotations should be considered untrusted, unless obtained from a trusted server." "Hosts must obtain explicit user consent before invoking any tool".
- Tools page (2026-07-28): "Tools in MCP are designed to be model-controlled, meaning that the language model can discover and invoke tools automatically based on its contextual understanding and the user's prompts." "For trust & safety and security, there SHOULD always be a human in the loop with the ability to deny tool invocations." Discovery and use: "To discover available tools, clients send a tools/list request"; "To invoke a tool, clients send a tools/call request".
- Note: for the reader: MCP standardizes the plumbing between the program and the tools (TL41); it does not change the model's side, which still sees tool descriptions as text and emits calls as text. Version history (2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28, from the site index `llms.txt`) shows it is still moving; date-stamp everything.

### TL49. MCP across vendors (as of 2026-11)
- Sources: `openai2026functioncalling`, `anthropic2026tooluse`.
- OpenAI: built-in tools "enable the model to search the web, run code, access the functionality of an MCP server, and more." Anthropic: "To connect to Model Context Protocol (MCP) servers, see the MCP connector."
- Note: supports "MCP is supported beyond its originator" as of 2026-11. Do not claim it is "the" industry standard without a source that says so.

### K. Failure modes

### TL50. Retrieval errors
- Sources: `yao2023react` (23% of ReAct errors from non-informative search, TL45); `karpukhin2020dense` (SQuAD, rare phrases, TL10, TL12); `lewis2020retrieval`; `anthropic2024contextual` (chunks without context, TL30); `liu2024lost` (unused passages, TL36); `gao2023enabling` ("the retrieval quality is crucial", TL34).
- Lewis et al., Appendix H (p. 19), "Retrieval Collapse": "for some tasks such as story generation [11], the retrieval component would "collapse" and learn to retrieve the same documents regardless of the input. In these cases, once retrieval had collapsed, the generator would learn to ignore the documents, and the RAG model would perform equivalently to BART."
- Note: a retrieval system can fail by finding nothing relevant, finding a passage that lacks context, finding the right passage but placing it where the model uses it poorly, or retrieving relevant text that the model then ignores or misstates (TL34, TL35).

### TL51. Tool misuse: wrong or invented arguments, loops, sensitivity to wording
- Sources: `anthropic2026tooluse`, `schick2023toolformer`, `yao2023react`, `nakano2021webgpt`.
- Anthropic (as of 2026-11): "If the user's prompt doesn't include enough information to fill all the required parameters for a tool, Claude Opus is much more likely to recognize that a parameter is missing and ask for it. Claude Sonnet might ask ... But it might also infer a reasonable value." Example: asked "What's the weather?" without a location, the model "might guess values you didn't supply", shown as a call with location "New York, NY". "This behavior is not guaranteed".
- Toolformer (p. 11): "sensitive to the exact wording of their input when deciding whether or not to call an API". ReAct: repeated thoughts and actions (TL45). WebGPT (p. 3): "If a model generates any other text, it is considered to be an invalid action."
- Note: the reader-facing point: the program executes whatever well-formed call the model writes; a wrong but valid call is still run. This is why vendors and MCP recommend confirmation for actions with side effects (TL52).

### TL52. Prompt injection through retrieved text and tool results
- Sources: `greshake2023not`, `openai2023functioncalling`, `openai2023chatgptplugins`, `mcp2026specification`.
- Greshake et al., abstract (p. 1): "We argue that LLM-Integrated Applications blur the line between data and instructions. We reveal new attack vectors, using Indirect Prompt Injection, that enable adversaries to remotely (without a direct interface) exploit LLM-integrated applications by strategically injecting prompts into data likely to be retrieved." "We demonstrate our attacks' practical viability against both real-world systems, such as Bing's GPT-4 powered Chat and code-completion engines, and synthetic applications built on GPT-4. We show how processing retrieved prompts can act as arbitrary code execution, manipulate the application's functionality, and control how and if other APIs are called." "effective mitigations of these emerging threats are currently lacking." p. 1: "Augmenting LLMs with retrieval blurs the line between data and instructions."
- p. 4: Edge's Bing Chat sidebar could read the current page; "We found that any prompts/instructions written on a page (while being invisible to the user) can be effectively injected and affect the model."
- OpenAI, 13 June 2023: "a proof-of-concept exploit illustrates how untrusted data from a tool's output can instruct the model to perform unintended actions. We are working to mitigate these and other risks. Developers can protect their applications by only consuming information from trusted tools and by including user confirmation steps before performing actions with real-world impact, such as sending an email, posting online, or making a purchase."
- OpenAI, 23 March 2023: red teamers "discovered ways for plugins - if released without safeguards - to perform sophisticated prompt injection, send fraudulent and spam emails, bypass safety restrictions, or misuse information sent to the plugin."
- MCP (2026-07-28): annotations "untrusted, unless obtained from a trusted server"; "human in the loop" (TL48).
- Note: coordinate with `prompting`, which owns prompt injection as a concept (outline concepts list). This chapter adds the indirect form: the attacker writes into a web page, document, or tool result that the system later pastes into the context. The mechanism is the one the reader now knows: everything in the context window is text, and the model has no built-in channel separating instructions from data. Date-stamp mitigations ("as of 2026-11, no complete defence is claimed by the sources read"; Greshake 2023 says "currently lacking").

## Disputed or inconsistent points

### TLD1. Who introduced retrieval-augmented generation?
- **REALM first (February 2020):** retrieval inside pretraining, masked language modelling, extractive answers (`guu2020realm`).
- **RAG named and generalized it (May 2020):** generative seq2seq model with a DPR retriever; Lewis et al. say earlier hybrid models "have so far been only investigated for extractive downstream tasks" and cite REALM and ORQA (p. 1).
- **Earlier retrieve-then-read QA:** DrQA (2017) and ORQA (2019), cited by both; not fetched.
- **kNN-LM (November 2019):** retrieval during language modelling, without a generator reading passages.
- Suggested wording: "The idea of letting a model look things up in a text collection had several near-simultaneous versions around 2019-2020. The name retrieval-augmented generation comes from a 2020 paper by Patrick Lewis and colleagues at Facebook AI Research, which combined a learned retriever with a model that writes its answer." Do not call Lewis et al. the inventors of retrieval for language models.

### TLD2. What "RAG" means
- **Narrow (Lewis et al. 2020):** a retriever and a generator fine-tuned together end to end, with the retrieved document as a latent variable marginalized over (Fig. 1 caption).
- **Broad (current practice, SLP3 2026, Anthropic 2024):** retrieve passages with any method and paste them into the prompt of a separately trained LLM, no joint training ("Create a prompt that includes q and the retrieved passages", SLP3 p. 17).
- Suggested handling: introduce the 2020 paper, then say plainly that the term now covers the simpler paste-into-the-prompt pattern, which is what Book 2 builds.

### TLD3. Lewis et al.'s index size: 728 or 768 dimensions?
- Lewis et al. Appendix G (p. 19): "21M 728 dimensional vectors, consisting of 15.3B values."
- DPR, whose encoder RAG uses (p. 3: "a pre-trained bi-encoder from DPR"), states "d = 768" (DPR p. 6771); BERT-base's hidden size is 768.
- Computed: 21M x 728 = 15.29 billion (matches "15.3B"); 21,015,324 x 768 = 16.14 billion. The "728" is very likely a typo carried into the product. Use DPR's 768 and 21,015,324 for the memory arithmetic (D-009 item 6) and do not print "15.3B" as a check of it.

### TLD4. Is dense retrieval better than BM25?
- **Yes, mostly (DPR 2020):** 9-19 points top-20 on four of five datasets; RAG ablation: dense better on all tasks but FEVER.
- **No, sometimes:** SQuAD (BM25 68.8 vs DPR 63.2, high lexical overlap); FEVER in RAG; rare salient phrases ("Thoros of Myr"); exact identifiers ("TS-999", Anthropic 2024).
- **Both:** BM25 + DPR (DPR Table 2), hybrid search and rank fusion in products (TL31).
- Suggested wording: "Learned vectors find paraphrases that keywords miss; keywords find exact names and codes that vectors blur. Systems that work well usually use both."

### TLD5. OpenAI's keyword-similarity percentages cannot be reproduced
- OpenAI (as of 2026-11) prints keyword similarity 0%, 27%, 40% "using intersection over union".
- Computed with lowercase word sets: 1/15 = 6.7%, 2/13 = 15.4%, 3/13 = 23.1% (all words); 0/8 = 0%, 1/6 = 16.7%, 1/5 = 20.0% (a small stop list removed). Neither reproduces 27% and 40%; the tokenization behind OpenAI's figures is not stated.
- Handling: if the moon example is used, compute our own keyword numbers in `code/checks/tools.py` and quote OpenAI's semantic-similarity percentages as theirs (a trained embedding model the book cannot run [D-009]); do not print OpenAI's keyword numbers as if checked.

### TLD6. BM25 parameter values
- Robertson and Zaragoza (2009, p. 360): "0.5 < b < 0.8 and 1.2 < k1 < 2" reasonably good in many circumstances; a common published combination "b = 0.5 and k1 = 2" (p. 361).
- DPR (2020): b = 0.4, k1 = 0.9, "tuned using development sets" (p. 6773).
- The survey's "reasonably good in many circumstances" runs across the page break, so it is cited as pp. 360-361.
- SLP3 (p. 9): "Manning et al. (2008) suggest reasonable values are k = [1.2,2] and b = 0.75." (Corrected at the independent check: the research pass had recorded that k1 = 1.2, b = 0.75 were found in no source read.)
- Handling: if the worked example uses k1 = 1.2 and b = 0.75, say that b is inside the survey's range and k1 at its lower edge, citing pp. 360-361, and that SLP3 reports Manning et al. suggesting b = 0.75 (p. 9); not "the default".

### TLD7. Bibliographic details of the BM25 survey
- The PDF's first page: Foundations and Trends in Information Retrieval Vol. 3, No. 4 (2009) 333-389, DOI 10.1561/1500000019.
- Crossref for the same DOI: volume 4, issue 1-2, pages 1-174, issued 17 Sep 2009.
- Handling: cite the volume and pages printed on the document read (3(4) 333-389); the Crossref record looks wrong. Low stakes.

### TLD8. When to retrieve and when to paste everything
- Anthropic (Sep 2024): under "200,000 tokens (about 500 pages)", "just include the entire knowledge base in the prompt".
- Liu et al. (2023-2024): models use the middle of long contexts poorly; more passages help little past 20.
- ALCE (2023): more passages help GPT-4 but not ChatGPT.
- Handling: present as a trade-off that depends on the model and has moved over time (context windows in `generation` GN25 are now up to 1M tokens, as of 2026-11). No firm threshold.

### TLD9. Do citations make answers trustworthy?
- **Help:** WebGPT (references let labelers judge accuracy; "Transparency", p. 11); SLP3 (citations "can help the user decide whether to trust the generation").
- **Limits:** WebGPT's own "cherry-pick" warning; ALCE (about half of ELI5 answers not fully supported, 2023); Liu et al. (51.5% and 74.5%, early 2023; utility inversely correlated with citation precision).
- Suggested wording: "A citation lets a reader check a claim. It does not check the claim for them."

### TLD10. Is ReAct better than chain-of-thought?
- On HotpotQA, ReAct alone 27.4 vs CoT 29.4 (worse); on Fever 60.9 vs 56.3 (better); combinations best (35.1 and 64.6). Fewer hallucinations, more reasoning errors and loops (TL44, TL45).
- Handling: report both directions; the authors themselves recommend the combination.

## Mechanism claims to check numerically at drafting [D-009]

Suggested script: `code/checks/tools.py`. Items 1 and 2 need only the standard library; item 1's optional GloVe part reuses `code/checks/embeddings.py`'s loader and the hash-checked GloVe file in `out/cache/` [D-018] (import, do not copy). All numbers below were computed once in this session with a throwaway script.

1. **Toy retrieval for the key figure (moon example).** Query "When did we go to the moon?"; passages D1 "The first lunar landing occurred in July of 1969.", D2 "The first man on the moon was Neil Armstrong.", D3 "When I ate the moon cake, it was delicious." (sentences quoted from `openai2026retrieval`). Lowercase word tokens.
   - Raw word-count cosine: D1 0.126, D2 0.342, D3 0.378 (moon cake ranks first).
   - tf-idf cosine with SLP3 Eqs. 11.4-11.6 over these three passages (N = 3, log10): D1 0.000, D2 0.061, D3 0.426 (moon cake first; the lunar landing scores zero because it shares no word with the query except "the", whose idf is 0).
   - Averaged GloVe 6B 50-d word vectors, cosine: all words D1 0.790, D2 0.896, D3 0.902 (moon cake still first); with a small stop list removed D1 0.651, D2 0.795, D3 0.621 (the moon-landing sentences now beat the cake). cos(moon, lunar) = 0.683; cos(moon, cake) = 0.315.
   - OpenAI's trained embedding model (their figures, not reproducible here): D1 65%, D2 43%, D3 28%.
   - The honest story the numbers tell: word overlap ranks the cake first; averaged word vectors know "lunar" is near "moon" but are swamped by small words; a model trained for retrieval puts the lunar landing first. Use a slightly larger toy corpus (6-10 passages) if idf over three documents looks too artificial; the script should print the corpus and every score.
2. **tf-idf by hand on the toy corpus (optional table).** Print df, idf, and the tf-idf vector for the query and each passage, so the figure can show one row of arithmetic.
3. **Sparck Jones's 1972 weights.** f(n) = m with 2^(m-1) < n <= 2^m; weight = f(N) - f(n) + 1. N = 200: f(200) = 8; n = 90: f = 7, weight 2; n = 3: f = 2, weight 7 (matches the printed example). Compare log2(200/90) = 1.15 and log2(200/3) = 6.06: the same idea in integer steps.
4. **BM25 saturation and length normalization** (k1 = 1.2, b = 0.75, inside the recommended range, TLD6). Term-frequency part tf / (k1 B + tf) with dl = avdl (B = 1): tf 1, 2, 3, 5, 10, 100 give 0.455, 0.625, 0.714, 0.806, 0.893, 0.988 (approaching 1); with the (k1 + 1) numerator variant: 1.000, 1.375, 1.571, 1.774, 1.964, 2.174 (approaching 2.2), same ranking. Length: tf = 3 in a document half the average length (B = 0.625) gives 0.800; average length 0.714; twice average (B = 1.75) 0.588. Contrast: raw tf grows without bound (3, 10, 100); SLP3's log tf grows slowly without a ceiling (1 + log10 100 = 3).
5. **idf at DPR scale** (N = 21,015,324 passages). Robertson-Sparck Jones idf log((N - n + 0.5)/(n + 0.5)), natural log: n = 1: 16.46; 10: 14.51; 1,000: 9.95; 100,000: 5.34; 1,000,000: 3.00; 10,000,000: 0.10. SLP3's log10(N/n): 7.32, 6.32, 4.32, 2.32, 1.32, 0.32. A word in nearly half the passages is worth almost nothing. Also brute-force search cost: 21,015,324 x 768 = 16,139,768,832 multiply-adds per query.
6. **Index memory arithmetic (N vectors x dimensions x bytes).** DPR/RAG index: 21,015,324 x 768 = 16,139,768,832 numbers; 32-bit floats 64.56 GB; 16-bit 32.28 GB; 8-bit 16.14 GB; 1-bit 2.02 GB. Lewis's printed figure (TLD3): 21M x 728 = 15.29 billion. A company knowledge base of 1,000,000 chunks at Voyage's default 1,024 dimensions: 4.10 GB float32, 1.02 GB int8, 0.128 GB binary (the 4x and 32x of `anthropic2026embeddings`); at OpenAI's 1,536 dimensions: 6.14 GB float32. Compare with the model sizes in `destination` (Llama 3 8B, 16 GB at 16 bits): the index of all of 2018 Wikipedia is larger than a small model.
7. **DPR's top-20 gaps.** DPR minus BM25: NQ 19.3, TriviaQA 12.5, WQ 18.2, TREC 8.9, SQuAD -5.6. The abstract's "9%-19%" is the range of the first four.
8. **RAG world-leader percentages as counts of 82.** 70% = 57/82 (69.5%), 68% = 56/82 (68.3%), 12% = 10/82 (12.2%), 4% = 3/82 (3.7%); each is the unique count that rounds to the printed percentage. Counts are inferred, not printed.
9. **SBERT's pair count.** 10,000 x 9,999 / 2 = 49,995,000 (matches the printed figure); 65 hours / 49,995,000 = about 4.7 ms per pair. Versus 10,000 embeddings plus one similarity matrix.
10. **Chunking with overlap (OpenAI's default as of 2026-11).** A 5,000-token document, 800-token chunks, 400-token overlap: chunk starts 0, 400, ..., 4,000, then a final chunk 4,400-5,000: 12 chunks, 9,400 tokens stored (1.88 times the document). Disjoint 100-word passages: 21,015,324 passages is about 2.1 billion words of Wikipedia text (an upper bound, since the last passage of an article may be shorter; inference, label it).
11. **Contextual retrieval percentages (vendor figures, arithmetic only).** (5.7 - 3.7)/5.7 = 35.1%; (5.7 - 2.9)/5.7 = 49.1%; (5.7 - 1.9)/5.7 = 66.7%: matches the printed 35%, 49%, 67%.
12. **Small consistency checks.** kNN-LM: 18.65 - 15.79 = 2.86 (abstract rounds to 2.9). ReAct Table 2 ReAct failure column 47 + 23 + 0 + 29 = 99 (rounding); CoT 16 + 56 + 28 = 100. Llama 3.1: cutoff December 2023, release 23 July 2024: about 7 months.
13. **Tool-definition overhead (optional, as of 2026-11).** One vendor adds a fixed 286-token system prompt for tools (Claude Opus 5.5), plus the tokens of every tool's name, description and schema; at the `tokens` chapter's rule of thumb, a page of tool descriptions costs as much context as a page of conversation. If used, compute any token counts with the tokenizer already used in `tokens` (no new dependency), or state them only as the vendor's numbers.

## Figures planned [D-014]

- `figures/tools-rag.svg` (the outline's key figure: "a RAG request traced from question to retrieved passages to answer"). Recommended design, with no invented model output [D-009]:
  - Left to right: (1) the question; (2) the index (passages as vectors, drawn as a few labelled dots or a table); (3) the scores for each passage under two methods (tf-idf cosine and a learned retriever), numbers from mechanism item 1, with the top passage highlighted; (4) the assembled prompt as text boxes in SLP3's schematic order (passages, then "Based on these texts, answer this question:", then the question; `jurafsky2026ir` p. 17); (5) the model, then the answer.
  - For the answer box, two honest options: (a) use Lewis et al.'s printed Hemingway trace (TL25) as the worked case throughout: input "Hemingway", two of five retrieved passages as printed, output "The Sun Also Rises" is a novel by this author of "A Farewell to Arms", citing Fig. 2, p. 7; the retrieval scores are then not available (the paper prints only the per-token document posterior heat map), so the score panel would show the moon toy instead and the two halves must be labelled as different examples; or (b) keep the moon toy throughout and leave the answer box as the prompt's open end with a caption saying the model continues from there (no answer printed). Option (a) is more vivid; option (b) is simpler and cleaner. The drafter should pick one and say why.
  - Book 1 has no code [D-003]: draw the prompt as labelled boxes of English text, not JSON or an API call.
- `figures/tools-loop.svg`: the tool-use loop as a cycle: user message -> model -> (stop reason "tool use": a call with a tool name and arguments, drawn as a filled form, not code) -> program runs the tool -> result appended to the conversation -> model -> ... -> final answer (stop reason "end of turn"). Annotate the ReAct names (thought, action, observation) on the same cycle. A diagram, no data. Labels from TL41 and TL44.
- `figures/tools-bm25.svg` (optional): term-frequency contribution vs tf for raw tf, 1 + log10 tf (SLP3), and BM25's tf/(k1 + tf) (k1 = 1.2), from mechanism item 4, showing saturation. A line plot of computed numbers.
- `figures/tools-index-memory.svg` (optional): bar chart of mechanism item 6 (float32, float16, int8, binary for DPR's 21M x 768 index), with Llama 3 8B's 16 GB as a reference line from `destination`.
- Do not reproduce Lewis et al. Fig. 2's heat map, ReAct Fig. 1, or vendor diagrams; describe and cite.

## Scope notes for drafting

- **Hand-offs in.** From `embeddings`: cosine (with its one formula), word vectors, GloVe (and the D-018 cache), LSA for document retrieval with its mixed 1990 results, "the reader who has done document retrieval will know the cosine". From `pretraining`: BERT, encoder-only models, [CLS], masked language modelling, fine-tuning. From `generation`: the context window as working memory, stop reasons including "tool_use" (mention only there), hallucination and its definitions, the promise that "grounding and retrieval" are mitigations. From `training`: Llama 3's "knowledge until the end of 2023" and "advance the model's knowledge cut-off". From `destination`: "the parameters contain nothing from after the text the model was trained on", model memory sizes. From `tokens`: token counts as the unit of cost and context. From `prompting` (outlined, earlier): chain-of-thought, structured output, prompt injection, context management; check what it actually says when this chapter is drafted. From `adapting` (outlined, earlier): "choosing between prompting, retrieval, and fine-tuning"; this chapter should not repeat that comparison, only point back to it. From `instructions`: chat format and system prompt as plain tokens (tool definitions are inserted there, TL40).
- **Hand-offs out.** To `frontier`: agents and long-running tasks, computer use, multi-agent systems, reasoning models that call tools during long thinking; this chapter introduces the loop only (outline). To `evaluation`: MTEB and leaderboards (one paragraph here), benchmark contamination. To `local`: running an embedding model locally, memory of an index alongside a model. To Book 2: `b2-retrieval` (a minimal local RAG over a few documents with a local embedding model), `b2-agent-loop` (the smallest loop by hand), `b2-tau` (a production-shaped harness, Tau, per D-007). Book 1 can say "Book 2 builds both"; do not name versions here.
- **What not to say.**
  - Not that RAG eliminates hallucination; Lewis et al. say "hallucinate less" (qualitative), ALCE and Liu et al. show unsupported statements remain (TLD9).
  - Not that Lewis et al. invented retrieval for language models (TLD1); not that "RAG" today means the 2020 architecture (TLD2).
  - Not that dense retrieval always beats BM25 (TLD4); not "k1 = 1.2, b = 0.75 are the defaults" (TLD6).
  - Not that the model "runs" or "calls" a tool by itself; it writes a request that the program may run (TL41). Use "requests", "asks for", or "emits a call".
  - Not that tool definitions are hidden from the context window or free; they are tokens (TL40).
  - Not that a citation proves a claim (TLD9).
  - Not that MCP is "the" universal standard, or that any vendor guarantees safety against prompt injection; MCP's own spec says the protocol "cannot enforce these security principles" (index page, "Implementation Guidelines").
  - Not that a model's knowledge stops sharply at its stated cutoff (TL4); not a single number for "how far behind" models are.
  - Not that ReAct beat chain-of-thought across the board (TLD10).
  - Not Lewis's "728 dimensional" or "15.3B values" as a check (TLD3).
  - Not OpenAI's keyword-similarity percentages as checked numbers (TLD5).
  - No code, JSON, API parameter names in code font, or shell commands [D-003]. "Stop reason" and "tool use" are words; the snake_case strings are not printed.
  - No product claims without "as of 2026-11" (TL3, TL17, TL30, TL40-TL43, TL46, TL48, TL49).
- **Terms to define at first use** (for the glossary): knowledge cutoff (reported vs effective; "reliable knowledge cutoff" as one vendor's term); information retrieval; query, document, collection; term frequency; inverse document frequency; tf-idf; BM25 (saturation, length normalization); inverted index; sparse vs dense retrieval; top-k accuracy (or recall at k); bi-encoder (dual encoder) and cross-encoder; reranking (one line); embedding model (sentence embedding); vector database / vector store; nearest neighbour search; approximate nearest neighbour (ANN); maximum inner product search (optional); HNSW (name only); FAISS (name only); retrieval-augmented generation (RAG); parametric vs non-parametric memory; closed-book vs open-book; chunk, chunking, chunk overlap; hybrid search (rank fusion, one line); grounding; citation (citation recall and precision, optional); verifiability; tool (function); tool call (function call); tool definition (name, description, arguments, schema in words); tool result; tool-use loop; agent; ReAct (thought, action, observation); Model Context Protocol (host, client, server; tools, resources); prompt injection (direct recalled from `prompting`; indirect new here); human in the loop.
- **Formulas allowed** [D-002]: cosine is already given in `embeddings` (reuse, do not restate in full). tf-idf in SLP3's standard form (tf x idf with idf = log(N/df)) once, with every symbol explained, after the worked numbers. BM25 at most once, in Robertson and Zaragoza's Eq. 3.15 form, every symbol explained, or better in words plus the item 4 numbers. The dot-product similarity sim(q, p) = E_Q(q) . E_P(p) only in words ("the dot product of the question's vector and the passage's vector"). No RAG marginalization formula, no SLP3 product formula.
- **Book 1 rule** [D-003]: no code. All numbers via `code/checks/tools.py`.
- **Date stamps.** TL2 (2021, 2023, 2024); TL3 (as of 2026-11); TL4 (2024); TL5 (2023; as of 2026-11); TL10 (as of 2026-11; 2024); TL11-TL13 (2020); TL14-TL15 (2019); TL16 (2022-2023); TL17 (as of 2026-11); TL19-TL20 (2016-2020; 2017-2021); TL21-TL28 (2019-2020); TL26 (SLP3 draft August 2026; Anthropic September 2024); TL29 (2020); TL30 (as of 2026-11; September 2024); TL32 (2021); TL34-TL36 (2023, models of 2023); TL37-TL39 (2022-2024); TL40-TL43, TL46, TL48-TL49 (as of 2026-11); TL47 (November 2024); TL52 (2023; as of 2026-11).
- **Bridges the reader can use** (honest links only): document retrieval with tf-idf and cosine, which the 2000s reader may have done, is exactly sparse retrieval (TL6-TL9); LSA (from `embeddings`) as the earlier dense answer to synonyms (TL10, link by problem, not lineage); k-nearest neighbours, the reader's classifier, is what vector search does at scale (TL18-TL20, TL27); parametric vs non-parametric models, a statistics distinction, is Lewis et al.'s own vocabulary (TL22); the index swap is like refitting nothing and changing the lookup table (TL24); a tool call is like a function signature the model fills in (OpenAI's 2023 "get_current_weather(location, unit)", TL39, described in words); the agent loop is a read-eval-print loop the reader may know from interactive statistics software (analogy, label it; D-012's own REPL framing makes it natural); prompt injection is the old database lesson of mixing data and commands (SQL injection) in a new setting (analogy, not in the sources read; label it as the writer's analogy or find a source).
- **Length and emphasis.** About 14 pages. Suggested weight: the cutoff and the two gaps (1 p); classical IR bridge with tf-idf and BM25 (2-3 pp); dense retrieval, embedding models, vector search, memory arithmetic (2-3 pp); RAG history and the key figure (2-3 pp); chunking and grounding with citations (2 pp); tools, the loop, ReAct, MCP (3 pp); failure modes (1-2 pp). kNN-LM, MRKL, HNSW internals, MTEB details, strict mode, and contextual retrieval numbers are optional and can be cut first.

## Leads not used as sources

- Wikipedia articles on tf-idf, Okapi BM25, HNSW, and RAG: not consulted.
- Voyage AI blog posts linked from `anthropic2026embeddings` (Voyage 4, January 2026): not fetched.
- Pinecone's "vector similarity guide" linked from `anthropic2026embeddings`: a vendor blog lead, not used.
- MCP governance pages and SEPs listed in `llms.txt` (SEP-932 and others): not read; any statement about MCP's governance or a foundation needs a fetched primary source.
- Anthropic's "Effective harnesses for long-running agents" (26 Nov 2025), linked from the contextual retrieval page: a `frontier` lead.
- OpenAI's "Agents API" and "tool search" docs, and Anthropic's "tool search", "Managed Agents", and "MCP connector" pages: seen as links only; `frontier` or Book 2 leads.
- Dahl et al. (2024) on legal hallucination rates (69% to 88%), cited by SLP3 p. 2: not fetched; do not repeat the numbers without it.
- Matryoshka representation learning (arXiv 2205.13147), linked by OpenAI for shortenable embeddings: not fetched.
- The OpenAI 2023 function-calling post's "proof-of-concept exploit" link: not followed.

## Worked examples used in the chapter

All from `code/checks/tools.py` [D-009]. Where the ledger's throwaway computations (above) cover the same quantity, the script's output matches them.

- Example 1: the moon query and OpenAI's three sentences (quoted from `openai2026retrieval`, as of 2026-11), lowercased word tokens. Raw word-count cosine D1 0.126, D2 0.342, D3 0.378. tf-idf (SLP3 Eqs. 11.4-11.6, N = 3, log10): idf of "the" 0, "moon" 0.176, "when" 0.477; cosines D1 0.000, D2 0.061, D3 0.426. Averaged GloVe 6B 50d (via `code/checks/embeddings.py`'s hash-checked loader, D-018): all words 0.790, 0.896, 0.902; with a 16-word stop list chosen for this example (a, an, and, at, did, i, in, is, it, of, on, the, to, was, we, when; leaves "go" and "moon" of the query) 0.651, 0.795, 0.621. GloVe cosines moon-lunar 0.683, moon-cake 0.315. OpenAI's 65%, 43%, 28% printed as quoted figures, not computed. Top two by the stop-listed GloVe column: D2, D1 (used in the key figure).
- Example 2: Spärck Jones's weights, N = 200: n = 90 gives 2, n = 3 gives 7 (the printed values); log2(200/90) = 1.15 and log2(200/3) = 6.06 computed but not printed in the chapter.
- Example 3: BM25 term-frequency part, k1 = 1.2, b = 0.75: 0.455, 0.625, 0.714, 0.806, 0.893, 0.988 for tf 1, 2, 3, 5, 10, 100 (chapter uses 1, 3, 10, 100); 1 + log10 tf gives 3.000 at 100; tf = 3 at half, average, twice the average length: 0.800, 0.714, 0.588.
- Example 4: idf at DPR scale (not used in the chapter text).
- Example 5: 21,015,324 x 768 = 16,139,768,832 (about 16.1 billion); 64.56 GB (32-bit), 32.28 GB (16-bit), 16.14 GB (8-bit), 2.02 GB (1-bit); 1,000,000 x 1,024: 4.10 GB float32, 1.02 GB int8 (0.128 GB binary computed, not printed). The comparison with Llama 3 8B's 16.1 GB uses the figure printed in `generation`.
- Example 6: DPR minus BM25 top-20: +19.3, +12.5, +18.2, +8.9, -5.6 (the chapter's table).
- Example 7: 70%, 68%, 12%, 4% of 82 are uniquely 57, 56, 10, 3; the chapter prints 57 and 56, labelled as inferred.
- Example 8: 10,000 x 9,999 / 2 = 49,995,000 (matches the printed figure); 4.7 ms per pair computed, not printed.
- Example 9: 5,000 tokens, 800-token chunks, 400 overlap: 12 chunks, 9,400 tokens stored, 1.88 times the document.
- Example 10: ReAct failure column 99 (printed as "sums to 99 through rounding"); Llama 3.1 cutoff to release about 7 months; contextual retrieval 35.1%, 49.1%, 66.7% (not printed; the chapter quotes 5.7% to 1.9% only).

## Figures

- `figures/tools-rag.svg` (key figure, option b of "Figures planned"): question; a score table for D1-D3 under tf-idf and averaged GloVe with stop words removed (both from Example 1) and OpenAI's trained model (quoted, labelled "their figures" and "not computed"); top two shaded per column; the middle column is traced; the prompt assembled in SLP3's schematic order (passages, then "Based on these texts, answer this question:", then the question; `jurafsky2026ir` p. 17); the last box says only that the model writes its answer from the question plus these passages. No model output is drawn. Option b was chosen per the author's provisional decision; the Hemingway trace (option a) is quoted in prose instead.
- `figures/tools-bm25.svg`: (a) raw count, 1 + log10 count, and BM25's term-frequency part (k1 = 1.2, average length) against the count; (b) BM25 at half, average and twice the average document length (b = 0.75), with the tf = 3 values. From Example 3.
- `figures/tools-loop.svg`: the tool-use loop as a diagram (no data): context window as a stack of text (system instructions, tool definitions, user request, model's request, tool result); model; two stops ("end of turn", "tool use" with a filled-in request drawn as a form: tool "weather lookup", place "Paris"); the program checks, may ask the user, runs the tool and appends the result. ReAct's names (thought, action, observation) annotated. Labels from TL41 and TL44; the weather example follows the vendors' own (TL39, TL40). No JSON or code.
- `tools-index-memory.svg` (optional in the plan) was not drawn; the memory numbers are in prose.

## Terms defined in the chapter

retrieval; tool (both in the introduction); knowledge cutoff; effective cutoff; information retrieval; query; document; inverse document frequency (idf); term frequency (tf); tf-idf; BM25; saturation; length normalization; inverted index; sparse retrieval; stop list; dense passage retrieval (DPR); top-20 accuracy; hybrid search; cross-encoder; bi-encoder; reranker; embedding model; nearest neighbour search; approximate nearest neighbour search; HNSW; FAISS; vector database / vector store; retrieval-augmented generation (RAG); parametric memory; non-parametric memory; closed-book; open-book; chunk; chunking; overlap; grounded; citation; verifiability; citation recall; citation precision; API (one line); JSON (recalled from `prompting`); tool definition; tool call; tool result; agent; ReAct; thought; action; observation; Model Context Protocol (MCP); host; client; server; human in the loop; prompt injection and its indirect form are recalled from `prompting`, not redefined.

## Drafting notes

- TLD1: REALM (February 2020) presented first, with kNN-LM (one sentence); RAG introduced with the ledger's suggested wording ("The name ... comes from a paper ..."); "REALM picked its answer out of the retrieved text" cited to Lewis et al. p. 1 ("extractive"). DrQA and ORQA not mentioned (not fetched).
- TLD2: both meanings given; the chapter says the simple paste-into-the-prompt version is what the reader will usually meet and what Book 2 builds.
- TLD3: Lewis's "728" and "15.3B" not used; memory arithmetic uses DPR's 768 and 21,015,324.
- TLD4: both directions, with DPR's table (four wins, one loss), Appendix C's opposite weaknesses, the TS-999 example, and the ledger's suggested sentence; the RAG-internal BM25 ablation (TL28) was cut for length.
- TLD5: OpenAI's keyword percentages not printed; the chapter's own keyword scores (count cosine and tf-idf) are computed; OpenAI's semantic percentages quoted as theirs.
- TLD6: b = 0.75 is described as inside the survey's range and k1 = 1.2 as at its lower edge, because the survey's inequalities are strict (1.2 < k1 < 2); SLP3's report of Manning et al. suggesting b = 0.75 added at the independent check; never called defaults. DPR's tuned b = 0.4, k1 = 0.9 also given.
- TLD7: not relevant to the prose (bibliographic only).
- TLD8: Anthropic's 2024 threshold quoted and balanced with "more text is not always used well"; no firm threshold; no current context-window size stated (`generation`'s text does not give one to point to).
- TLD9: handled with the ledger's suggested sentence after WebGPT, ALCE and Liu et al.
- TLD10: both directions with numbers and the combinations.
- Other choices: k = 1.2 boundary noted above. The RAG figure follows the author's decision (option b). Indirect prompt injection only; direct injection is pointed to `prompting`. The SQL-injection analogy suggested in "Bridges" was not used (the `prompting` ledger records an NCSC page arguing the two differ). The REPL analogy is used and labelled as the book's. The "decision to call is next-token prediction" framing (TL42 note) is labelled as the book's inference. "Agent" is defined from general usage, not from a source, and points to `frontier`. "Many systems" for two-stage reranking softened to "Some systems" (no source for prevalence). FAISS described through DPR's p. 6771 wording rather than as "the" library. HNSW introduced as the method RAG used, not as "widely used".
- ReAct's Colorado orogeny example is described as a demonstration the authors placed in the prompt (Act-only prompt, p. 16), not as model output.
- Left out for length: kNN-LM numbers (perplexity 18.65 to 16.12), REALM's own Table 1 and pyramidion example (REALM's 40.4 appears only through Lewis et al.'s Table 1), RAG's 11.8% and T5-large comparison, RAG's BM25 ablation (TL28), DPR's speed and indexing-time figures (TL13), MTEB's dataset counts, Voyage context length and query/document setting, OpenAI's rank-fusion setting, MRKL, WebGPT's TruthfulQA results, ALCE's post-hoc citing finding, Liu et al.'s r = -0.96 (stated qualitatively), Llama 3's step-by-step tool plans, ALFWorld/WebShop results, MCP version list, the vendor's contextual retrieval intermediate figures (35% and 49%), idf at DPR scale (Example 4), and the optional index-memory figure.
- No `TODO-VERIFY` markers; no new bib keys.
- Forward and backward references not checked against final text: `prompting` (direct prompt injection, lost in the middle, structured output, chain of thought), `instructions` (system prompt), `evaluation` (leaderboards), `frontier` (agents) were drafted in parallel or not yet drafted.

## Independent check (tools chapter)

2026-11-11. A separate agent re-fetched every source (the two 2023 OpenAI posts through the Internet Archive), checked arXiv dates, names and affiliations, recomputed every number independently, and regenerated all three figures (byte-identical).

- Errors found and fixed:
  1. The SLP3 quotation "a word appearing 100 times ..." and the 1 + log10 tf definition are on p. 6, not p. 5; citation corrected.
  2. "Tool use" was called one of the stop reasons of `generation`, which lists three endings and never mentions tool use; now "a way of stopping beyond those in the chapter on generation".
  3. The injection paragraph misstated `prompting` (which defines prompt injection as text that turns a model against the builder's intent, and already defines indirect prompt injection with Greshake et al.); it now recalls both and does not redefine the indirect form.
  4. The lunar landing was said to contain "none of the words in the search query", contradicting the chapter's own count (it shares "the"); now "shares no word with the question except "the"".
  5. "No source ... gives a rule for chunk size" omitted that the Anthropic post twice says chunks are "usually no more than a few hundred tokens"; added.
  6. Anthropic's 5.7% to 1.9% is the share of relevant chunks missing from the top 20 results (1 minus recall@20), not the share of searches; reworded.
- Warnings acted on: the BM25 settings sentence separates b (inside the range) from k1 (lower edge), cites pp. 360-361, and adds SLP3's report that Manning et al. suggest b = 0.75 (p. 9), with TLD6 corrected; RAG's fixed document encoder cited to pp. 4, 18; ReAct's worked example to pp. 16-17; ReAct's 29% category is "right but did not match the label's wording"; Liu et al. checked answers the engines gave in that period, not the engines; the reranker sentence describes a cheap first pass by keywords or vectors and cites SLP3 p. 14; SLP3 p. 16 now cited only for approximate nearest neighbour search, with "may miss a few" left as uncited explanation; "which" added before "incrementally builds"; "Systems that work well usually use both" replaced by "Many systems use both", cited to the Anthropic post (which calls a RAG system combining embeddings and BM25 "standard" and "traditional"), and DPR's own BM25 plus DPR result described as helping on some data sets and not others (Table 2), with the summary bullet changed to "many systems combine them"; JSON points to `prompting`, and the weather function is "one of" the 2023 post's examples; the human-confirmation sentence cites `openai2023functioncalling` and `mcp2026specification`; Anthropic's 286 tokens date-stamped and stated for its current models in the default setting; Cheng et al. cited pp. 1, 5 for "open-weight models whose training data is public or described" (D-020); "it is hard to match" replaces "it cannot be matched"; the embeddings chapter "took up" the problem with latent semantic analysis; RAG's affiliations given in full (Facebook AI Research, University College London, New York University); the Spärck Jones quotation is attributed to the abstract of the 2004 reprint.
- Could not verify: the live 2023 openai.com posts (read through the Internet Archive only; whether the weather function was the main example); whether the 1972 original of Spärck Jones's paper carried the abstract quoted (the chapter now attributes the wording to the 2004 reprint); forward and backward references to chapters drafted in parallel (`prompting`, `instructions`, `evaluation`, `frontier`) against their final text.

## Consistency pass (2026-11-11)

- "Retrieval" in the opening no longer bold; it now says "as the chapter on adapting described it" (`adapting` bolds it first).
- "knowledge cutoff" no longer bold; links back to `prompting`, which defines it first.
- **query** keeps its bold with "(here a search request, not the attention vector of the attention chapter)" (glossary finding (c)).
- **Saturation** keeps its bold with "(of a word's count, not the saturated units of the deep-turn chapter)" (glossary finding (c)).
- "leaderboard" glossed at first use, "a public ranking of methods by score" (`evaluation` defines it later; glossary finding (b)).
- **agent** keeps its bold with "(a looser sense than the reinforcement-learning agent of the chapter on following instructions)" (glossary finding (c)).
- American spelling: neighbour/neighbours to neighbor/neighbors (five places, including the bold terms "nearest neighbor search" and "approximate nearest neighbor"), "grey" to "gray" (loop figure caption), "hand-labelled" to "hand-labeled", "defence" to "defense" (twice).
- Not changed: indirect prompt injection was already unbolded by the independent check.

## Style pass (2026-11-11)

Reader call-outs made generic per D-023.

- "from the keyword search the reader may have done in the 2000s," -> "from the keyword search of the 2000s,"
- "A reader who built a document search in the 2000s did this:" -> "A document search built in the 2000s did this:"
- "the reader's k-nearest-neighbors classifier without the vote." -> "the k-nearest-neighbors classifier without the vote."
- "Their terms will be familiar to a statistician." -> "Their terms come from statistics."
- "A reader who has used an interactive statistics package knows the shape:" -> "An interactive statistics package has the same shape:"
- "Its keyword form is the reader's own: tf-idf" -> "Its keyword form predates neural networks: tf-idf"
