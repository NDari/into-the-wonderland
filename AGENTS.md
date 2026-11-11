# AGENTS.md

Guidance for AI agents (and humans) working in this repository.

## What this repo is

The source of two companion books that take a reader from early neural networks to modern large language models (LLMs) [D-001].

- **Book 1 (the priority):** concepts and history, with maximum breadth. A reader finishes it well informed about the state of the art and knows where to dig deeper. It stands on its own.
- **Book 2:** hands-on, a bit deeper and more technical, not exhaustive. The reader builds a tiny GPT, trains it once, then works with a real local model and an agent harness. It assumes Book 1.

Working title: *Into the Wonderland* [D-013].

## Working mode

The author is the first reader and is learning parts of this field while writing [D-012]. Work like a REPL session: one small step, look at the result, choose the next step.

- **Small steps.** Do the one thing asked, show the result, stop. Do not run ahead into the next chapter or phase.
- **Few decisions at a time.** Ask a question only when the next step is blocked by it, and ask one or two at most. Otherwise choose a sensible default, record it in `DECISIONS.md` as `provisional`, say so, and continue.
- **Everything is revertible.** No decision is final. Never describe one as settled for good.
- **The author is learning too.** Do not assume they know the literature. Explain unfamiliar terms in conversation as they come up. If the author is confused by a draft, that is a defect in the draft.
- **The outline is a living document.** It changes as the books are written. Scope changes go into `OUTLINE.md` first, then into the chapters.

## The readers

**Book 1** is written for someone who was comfortable with data science as practiced in the 2000s and has not followed the field since.

Assume they know:

- Undergraduate linear algebra, calculus, probability, and statistics
- Linear and logistic regression, decision trees, SVMs, k-means, PCA, naive Bayes
- Train/test splits, cross-validation, overfitting, regularization
- Possibly the multilayer perceptron and backpropagation as a "1990s technique", and n-gram language models

Assume they do not know: deep learning after roughly 2006, GPUs for ML, automatic differentiation, embeddings, attention, transformers, tokenization, or any LLM-era vocabulary.

**Book 2** is written for someone who has read Book 1, programs comfortably, and wants to see the ideas run.

## What the reader can do after finishing

Book 1:

1. Explain how an LLM works end to end: text, tokens, embeddings, transformer layers, next-token probabilities, generated text.
2. Name each part of the system, say why it exists, and say what problem it solved historically.
3. Read current LLM writing (papers, model cards, technical posts) without getting lost in terminology.

Book 2:

4. Build and train a tiny GPT, run and configure an open-weight model locally, and understand how an agent harness drives a model.

Every chapter must serve at least one of these. Material that serves none is out of scope.

## Editorial principles

- **History serves understanding.** Introduce each idea through the problem it solved and what came before it.
- **Bridge from what the reader knows.** Anchor new ideas in 2000s concepts where an honest link exists (logistic regression to a neuron, n-grams to neural language models, PCA/LSA to embeddings).
- **Define every term at first use** and add it to the glossary. Never use jargon before it is introduced.
- **No hype.** State what a technique does, what it cost, and where it fails.
- **Date-stamp fast-moving claims.** Anything about "current" models, sizes, tools, or practice carries an explicit "as of YYYY-MM".
- **One running thread.** Notation and terminology stay consistent across both books. Book 2 chapters name the Book 1 chapters they make concrete.

## Current rules

Each rule cites the decision behind it. `DECISIONS.md` holds the reasoning and how to revert.

Book 1:

- Intuition only: diagrams, analogies, worked numeric examples; no derivations; formulas only in their standard form with every symbol explained [D-002].
- No code, pseudocode, or shell commands anywhere in Book 1 [D-003].
- Scope is core plus modern practice, roughly 300-400 pages [D-004], including a short chapter on measuring models [D-011].
- Structure: the destination first, then two parallel histories that meet at the transformer [D-008].

Book 2:

- A bit deeper and more technical than Book 1, not exhaustive [D-001].
- One short training run, for understanding only [D-006].
- llama.cpp for local models, Tau as the reference harness; exact versions pinned in code and stated in text, updated together [D-007].
- All code is run before it is printed. Printed output is real output.

Both books:

- Verification is research, then draft, then an independent check [D-005]. See the policy below.
- Every number in a worked example is produced by a script in `code/checks/` [D-009].
- Every figure is drawn by a matplotlib script in `figures/` that writes an SVG next to itself [D-014].
- PDFs are built with `python3 build/build.py` (Pandoc with Typst) into `out/` [D-015].
- Chapters are Pandoc Markdown with `[@key]` citations and a shared `references.bib` [D-010].
- Chapters refer to each other by ID, never by a hard-coded number. Order and numbers come from `OUTLINE.md` [D-010].

## Decisions and consistency

The goal is that a change to one decision shows up everywhere it matters, so the books stay a cohesive whole.

1. **`DECISIONS.md` is the single record.** Every choice that shapes the books has an entry with an ID. Parked questions live there too, each with a trigger for when to raise it.
2. **Cite the ID wherever a file depends on a decision**, in the form `[D-002]`. This applies to this file, `OUTLINE.md`, and scripts. In chapter files use an HTML comment (`<!-- D-002 -->`) so it does not print.
3. **To change or revert a decision:**
   1. Do not rewrite the old entry. Set its status to `reverted` or `superseded by D-NNN`, and add the new entry if there is one.
   2. Search the repo for the old ID. Every hit is a place that depends on it.
   3. Update each hit: both the content and the ID.
   4. Run the check until it passes.
4. **Run `python3 tools/check.py` after every change.** It must exit with no errors. It verifies:
   - no em-dashes or en-dashes in any text file
   - the decision log is well formed
   - every cited decision ID exists and is still live (a reference to a reverted or superseded decision is an error)
   - every live decision is cited somewhere
   - chapter IDs in `OUTLINE.md` are unique, numbering is sequential, statuses are valid
   - every "Depends on" points to an existing, earlier chapter; every "Builds on" points to an existing chapter
   - chapter files match the outline; no orphans; drafted chapters exist
   - Book 1 chapter files contain no code blocks [D-003]
   - chapters marked `verified` or `approved` contain no `TODO-VERIFY`
   - every citation key exists in `references.bib` [D-010]
5. **What the script cannot check:** terminology, notation, tone, and whether prose still agrees with a changed decision. That needs a cohesion read by an agent: at each chapter's verification stage, after any decision change that touches drafted chapters, and before any PDF build.

When a new rule becomes mechanically checkable, add a check for it and cite the decision in a comment.

## Workflow

There is no fixed gate between outline and writing. A chapter is started when the author asks for it.

### Chapter lifecycle

`outlined -> researched -> drafted -> verified -> approved`

Each chapter's status is recorded in `OUTLINE.md`. Only the author moves a chapter to `approved`. One stage per step: finish a stage, report, and wait.

## Source and verification policy

Per [D-005].

**What needs a source:**

- Historical claims: who, what, when, in what order
- Quantitative claims: parameter counts, dataset sizes, benchmark results, costs, dates
- Quotes and attributions
- Specifics of a named paper, model, system, or tool

Explanations of mechanisms do not need a citation per sentence, but the math must be checked (confirmed numerically by a script, per [D-009]).

**Source hierarchy:**

1. Primary: the original paper, official documentation or model card, a first-hand account by the people involved
2. Authoritative secondary: textbooks, survey papers, established histories
3. Everything else (blogs, Wikipedia, forum posts): leads only, never the sole citation

**What "verified" means:** the source was fetched in the working session and the specific claim was located in it. Model memory is not a source. Each verified claim is logged in the chapter's ledger with: bib key, URL, access date, location in the source, and the supporting quote or a close paraphrase.

**When verification happens:**

1. Before drafting (`researched`): gather and fetch sources for the chapter's planned claims.
2. While drafting: every sourced claim gets a citation; anything not yet checked gets a `TODO-VERIFY` marker. Never invent a citation to fill a gap.
3. After drafting (`verified`): an independent pass, by an agent that did not write the chapter, checks each claim against its source.
4. Before a PDF build: re-check all "as of" claims and all pinned versions.

**Disputed history** (for example, priority for backpropagation): present the dispute and cite each side. Do not pick a winner silently.

## Repository layout

Only the top-level `.md` files and `tools/check.py` exist so far. The rest is created when first needed.

```
README.md               project overview and current layout
how-these-books-were-made.md  the process, for readers
AGENTS.md               this file
DECISIONS.md            decision log and parked questions
OUTLINE.md              both books: chapters, IDs, order, status
book1/chapters/<id>.md  one file per chapter, named by chapter ID
book1/sources/<id>.md   per-chapter claim ledger
book2/chapters/<id>.md
book2/sources/<id>.md
book2/code/             runnable code for Book 2, versions pinned
references.bib          shared bibliography
figures/                diagrams and plots, with the code that generates them
code/checks/            scripts that produce the numbers in worked examples
tools/check.py          consistency checks
build/                  PDF build script and templates
```

## Rules for agents

- **No git write operations.** The author handles all staging, commits, branches, and pushes. Read-only git commands are fine.
- **No em-dashes or en-dashes** anywhere: prose, code, or comments. Use a hyphen or rephrase.
- **Do not write ahead.** See "Working mode".
- **Verify, do not assert.** Do not state that a source says something, or that code runs, without having checked it in this session. Say plainly what is unverified.
- **Keep `README.md` and `how-these-books-were-made.md` current.** At the end of every working session, before the author commits, update both so they match the repo: status, layout, process, and decisions. `README.md` lists only what exists; `how-these-books-were-made.md` describes what is actually done, not what is planned.
- **Minimal diffs.** When revising, change what the task needs; do not restyle untouched prose.
- **No new dependencies or tools** without asking first.
- **Commands for the author's terminal** must be fish-compatible; local installs use `pacman` or `paru`.
