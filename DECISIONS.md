# Decisions

The single record of every choice that shapes the books. How to use it is described in `AGENTS.md` under "Decisions and consistency".

Nothing here is permanent. Any decision can be reverted or superseded at any time.

Statuses:

- `active`: confirmed by the author
- `provisional`: a default chosen so work could continue; not yet confirmed by the author
- `reverted`: withdrawn, nothing replaces it
- `superseded by D-NNN`: replaced by a later decision

Entries are never rewritten or deleted. To change one, set its status and add a new entry.

## D-001 Two companion books
- Status: active
- Date: 2026-11-10
- Decision: The material is split into two books. Book 1 is concepts and history with maximum breadth: enough to be well informed about the state of the art and to know where to dig deeper. Book 2 is hands-on and goes a bit deeper and more technical, without trying to be exhaustive. Book 1 is the priority and must stand on its own. Book 2 assumes Book 1.
- Why: Book 1's reader wants understanding; some readers learn better by building. Keeping them separate lets Book 1 stay free of code.
- To revert: fold Book 2 back into a hands-on appendix of Book 1 and remove the Book 2 section of `OUTLINE.md`.

## D-002 Book 1 math: intuition only
- Status: active
- Date: 2026-11-10
- Decision: Book 1 explains with diagrams, analogies, and small worked numeric examples. No derivations. A formula appears only when it is the standard form the reader will meet elsewhere (softmax, attention, cross-entropy), always after the intuition, with every symbol explained and a worked example beside it.
- Why: The target reader wants to understand the machine, not reproduce the proofs.
- To revert: choose a new depth, then revisit every chapter goal in `OUTLINE.md` and any drafted chapter.

## D-003 Book 1 has no code
- Status: active
- Date: 2026-11-10
- Decision: No code listings, pseudocode, or shell commands in Book 1 chapters or appendices. All code lives in Book 2.
- Why: Keeps Book 1 readable by someone who does not want to program.
- To revert: remove the code-fence check in `tools/check.py` and decide where code may appear.

## D-004 Book 1 scope: core plus modern practice
- Status: active
- Date: 2026-11-10
- Decision: Book 1 runs from the perceptron through the transformer and GPT-style pretraining, then instruction tuning and RLHF, inference, quantization and local models, LoRA, RAG, and one dated survey chapter on the frontier. Target roughly 300-400 pages.
- Why: Enough to follow current LLM writing without becoming an encyclopedia.
- To revert: add or cut chapters in `OUTLINE.md`; re-check every "Depends on" line.

## D-005 Verification: research, draft, independent check
- Status: active
- Date: 2026-11-10
- Decision: For each chapter, primary sources are fetched and logged before drafting. After drafting, an agent that did not write the chapter re-checks every historical and quantitative claim against the fetched source. Then the author approves.
- Why: Errors caught after drafting have already shaped the narrative; model memory is not a source.
- To revert: rewrite the "Source and verification policy" section of `AGENTS.md`.

## D-006 Book 2 includes one short training run
- Status: active
- Date: 2026-11-10
- Decision: Book 2 builds a tiny GPT and trains it once, for minutes, on a small corpus. The purpose is to watch learning happen, not to produce a usable model. No tuning or scaling up. Everything practical after that uses a real open-weight model.
- Why: An untrained model only outputs noise, so without one run the reader never sees what Book 1 describes. A home-trained model is otherwise of no practical value next to local open-weight models.
- To revert: drop the `b2-train` chapter from `OUTLINE.md` and fix the chapters that depend on it.

## D-007 Book 2 stack: llama.cpp and Tau, versions pinned
- Status: active
- Date: 2026-11-10
- Decision: Book 2 runs local models with llama.cpp and uses Tau (the Hugging Face educational coding-agent project, PyPI package `tau-ai`) as the reference agent harness. Exact versions are pinned in the code and stated in the text, and are updated together.
- Why: Both are small enough to read and run on one machine.
- Unverified: that Tau works against llama.cpp's server. Tau documents support for custom OpenAI-compatible endpoints; this must be tested before `b2-tau` is researched.
- To revert: pick a replacement runtime or harness and update the Book 2 section of `OUTLINE.md`.

## D-008 Book 1 structure: destination first, then two parallel histories
- Status: provisional
- Date: 2026-11-10
- Decision: Book 1 opens with the whole LLM at low resolution, then follows a chronological spine. The history of how networks learn (to 2016) and the history of how language is modeled (1948 to 2016) are told as two separate threads that meet at the transformer.
- Why: Each thread stays coherent. The cost is one jump back in time at the start of the language thread.
- To revert: interleave the two threads strictly by date in `OUTLINE.md` and re-check every "Depends on" line.

## D-009 Worked-example numbers are computed
- Status: provisional
- Date: 2026-11-10
- Decision: Every number in a worked example in either book is produced by a script in `code/checks/` so it can be re-run.
- Why: With no derivations in Book 1, the numeric examples carry the math and must be right.
- To revert: remove the rule from `AGENTS.md`.

## D-010 Source format: Pandoc Markdown, chapters addressed by ID
- Status: provisional
- Date: 2026-11-10
- Decision: Chapters are Pandoc Markdown with `[@key]` citations and one shared `references.bib`. Each chapter has a stable ID (its filename and its ID in `OUTLINE.md`). Chapter order and numbers come from `OUTLINE.md` at build time, so chapters refer to each other by ID, never by a hard-coded number.
- Why: Plain text, diffable, and chapters can be split or reordered without breaking references.
- To revert: choose another format; update the citation check in `tools/check.py` and the layout in `AGENTS.md`.

## D-011 Book 1 keeps a short chapter on measuring models
- Status: provisional
- Date: 2026-11-10
- Decision: Book 1 includes a short evaluation chapter (`evaluation`), although the scope chosen in D-004 did not list one.
- Why: Reading a model card or leaderboard requires the vocabulary.
- To revert: remove `evaluation` from `OUTLINE.md` and fold what is essential into `scale` and `local`.

## D-012 The author is the first reader
- Status: active
- Date: 2026-11-10
- Decision: For now the books are written for the author, who is learning parts of this field while writing. Work proceeds in small steps with few decisions at a time, and every decision stays revertible.
- Why: The author wants to discover what works along the way rather than fix a plan up front.
- To revert: rewrite the "Working mode" section of `AGENTS.md`.

## D-013 Working title: Into the Wonderland
- Status: active
- Date: 2026-11-10
- Decision: The working title is "Into the Wonderland". It covers the pair of books; the two books keep their descriptive names (Book 1 - Concepts and history, Book 2 - Building and running) as subtitles.
- Why: Chosen by the author.
- To revert: replace the title in `README.md` and `AGENTS.md`.

## D-014 Figures are matplotlib scripts
- Status: active
- Date: 2026-11-11
- Decision: Every figure in either book, plots and diagrams alike, is drawn by a Python script using matplotlib. The script lives in `figures/` and writes an SVG next to itself. Numbers in a figure come from the same computation as the matching `code/checks/` script [D-009]. Figures that recur across chapters, such as the pipeline diagram, come from one script with options, so every version shares one layout.
- Why: matplotlib is already installed, needs no other tool, and produces vector output that any PDF engine can use, so the choice does not wait on Q-03. Diagrams take more code than in a dedicated tool; that is accepted.
- To revert: choose another tool, redraw every file in `figures/`, and update the figure rule in `AGENTS.md`.

## D-015 PDF build: Pandoc with Typst
- Status: active
- Date: 2026-11-11
- Decision: PDFs are built by `build/build.py`, which runs Pandoc with Typst as the PDF engine, resolves citations with Pandoc's built-in citeproc, and writes to `out/`. Links to chapters that are not part of a build become plain text, so a single chapter or a partly written book can always be built. The author installed Pandoc 3.11 and Typst 0.15.1 for this.
- Why: Typst is far smaller than a LaTeX installation and fast, and it reads the SVG figures directly [D-014]. Pandoc already handles the chapter format [D-010].
- To revert: choose another engine, change the `--pdf-engine` line in `build/build.py`, and check that figures, tables, and formulas still render.

## D-016 Computer vision in Book 1: brief
- Status: provisional
- Date: 2026-11-11
- Decision: Book 1 covers convolution and weight sharing in a few pages of `structure`, and the ImageNet story in `deep-turn`, and no more. Images appear only where they explain an idea that LLMs use (weight sharing, learned features, the 2012 turn).
- Why: The book's subject is language models. Convolution matters here mainly as the first example of weight sharing, the idea that recurrence and attention also rely on.
- To revert: widen `structure` or add a vision chapter in `OUTLINE.md`, and re-check the "Depends on" lines.

## D-017 Split the training toolkit into two chapters
- Status: provisional
- Date: 2026-11-11
- Decision: The planned `toolkit` chapter becomes two chapters. `toolkit` ("The training loop") covers tensors, minibatches and stochastic gradient descent, momentum, RMSProp and Adam, learning-rate schedules and warmup, gradient clipping, hyperparameters, early stopping, loss curves, automatic differentiation, and frameworks. A new chapter, `depth` ("Making deep networks trainable"), covers initialization, dropout, batch and layer normalization, residual connections, and a closing section on reading a training recipe.
- Why: The research for `toolkit` found at least 13 concepts that each need a definition, a mechanism, a short history, and a worked example, plus four disputes: 22-26 pages at the density of the drafted chapters, against a 16-page budget. The two halves answer different questions and share little vocabulary.
- To revert: merge `depth` back into `toolkit` in `OUTLINE.md`, apply the cuts listed in the Q-04 notes of `book1/sources/toolkit.md`, and point every link to `#depth` back to `#toolkit`.

## D-018 External data for worked examples: downloaded, hash-checked, not committed
- Status: active
- Date: 2026-11-11 (proposed provisional; confirmed by the author the same day)
- Decision: When a worked example or figure needs a public dataset (so far *Pride and Prejudice* from Project Gutenberg for `prediction`, and the GloVe 6B word vectors for `embeddings`), the check script downloads it on first run into `out/cache/`, which is not committed. It verifies the file against a SHA-256 hash recorded in the script and in the chapter's ledger, and stops if the hash differs, so the printed numbers can never silently change. The data itself is never committed.
- Why: The GloVe file is 171 MB (inside an 862 MB zip), far too big for the repository. Downloading with a pinned hash keeps every number reproducible [D-009] without bloating the history. The cost is that the first run needs network access and time.
- To revert: commit small derived subsets instead (the GloVe vectors are PDDL-licensed, so this is allowed), and point the scripts at them.

# Open questions

Parked, not blocking. Each is raised only when its trigger arrives.

## Q-01 Working titles
- Decide when: any time; required for the PDF build.
- Resolved: 2026-11-10 by D-013.

## Q-02 How figures are produced
- Decide when: before the first Book 1 chapter is drafted. Book 1 leans on diagrams.
- Resolved: 2026-11-11 by D-014.

## Q-03 PDF engine
- Decide when: writing the build script. No PDF tooling is installed on the author's machine yet.
- Resolved: 2026-11-11 by D-015.

## Q-04 Split `toolkit` into two chapters?
- Decide when: researching `toolkit`. It carries a lot of vocabulary for its size.
- Resolved: 2026-11-11 by D-017 (provisional).

## Q-05 How much computer vision in Book 1?
- Decide when: researching `structure`. Currently a few pages there and the ImageNet story in `deep-turn`.
- Resolved: 2026-11-11 by D-016 (provisional).

## Q-06 Book 2 framework and hardware target
- Decide when: starting Book 2. NumPy, PyTorch, or both; CPU only or a consumer GPU.

## Q-07 A LoRA fine-tuning chapter in Book 2?
- Decide when: starting the "Run" stage of Book 2.

## Q-08 Topics not currently covered
- Decide when: any time. Candidates: reinforcement learning background, diffusion models, business and policy history, AI safety in more depth.

## Q-09 One glossary or one per book?
- Decide when: drafting the first Book 2 chapter.
