# How these books were made

This document describes the process as it stands on 2026-11-11. At this date one chapter (`destination`) has been approved by the author, eighteen more have been independently verified, and six are drafted and in verification. It is updated whenever practice changes, so that it stays a true account and not a plan.

## Who does what

- **Claude** (Anthropic's AI model) researches and writes the text, keeps the outline and decision log, and runs the checks. The first sessions used Claude Fable 5.2; the first four chapters were researched, drafted, and verified with Claude Opus 5.5. Claude works with helper agents: separate instances that research a chapter's sources, draft a chapter from its ledger, apply a check's corrections, or check a draft independently.
- **Naseer Dari** (the author) sets the direction, makes the decisions, reads every chapter, edits the prose, double-checks the content, and is the only one who can mark a chapter approved. The author directs version control: commits and pushes are made by Claude only when the author asks.

The author is the first reader and is learning parts of the field while the books are written [D-012]. If a draft confuses the author, the draft is at fault.

## How the work proceeds

In small steps, like a session at an interactive prompt: do one thing, look at the result, choose the next thing. There is no master plan fixed in advance.

- One step at a time. Nothing is written ahead of what was asked for.
- When the author asks for several chapters at once, they go through the stages in order, with work overlapping: one chapter's sources can be researched while another is drafted or checked. The author then reads them together.
- Few decisions at a time. A question is put to the author only when the next step is blocked by it. Otherwise a sensible default is chosen, recorded as provisional, and work continues.
- Every decision can be reverted.
- The outline is a living document and changes as the books are written.

## The life of a chapter

Each chapter moves through five stages. Its current stage is recorded in `OUTLINE.md`.

1. **Outlined.** The chapter has a goal, a list of concepts, the history it covers, candidate sources, and the earlier chapters it depends on.
2. **Researched.** The sources for its planned claims have been fetched and read, and each claim is logged in the chapter's ledger with where it was found. Research may be done by a helper agent; the ledger says who did what. For the earlier chapters the writer spot-checked the key claims in the same sources before drafting; from Part VI on, that check is left to the verification stage.
3. **Drafted.** The chapter is written against those sources. Any claim not yet checked carries a visible `TODO-VERIFY` marker. Most chapters were drafted by Claude in the main session; from Part VI on, several were drafted in parallel by drafting agents working only from the ledger, each recorded in its ledger.
4. **Verified.** A separate pass, by an agent that did not write the chapter, fetches the sources again on its own and checks every historical and quantitative claim, quote, page number, and worked-example number against them. The writer, or a helper agent given the report, fixes what it finds, and the check and the fixes are recorded in the chapter's ledger. No markers remain.
5. **Approved.** The author has read it, edited it, and signed off.

## How sources are handled

The rule is research first, then draft, then an independent check [D-005].

- **What needs a source:** who did what and when; any number (sizes, dates, results, costs); quotes and attributions; specifics of a named paper, model, or tool.
- **What counts as a source:** first the original paper, official documentation, or a first-hand account. Then textbooks, surveys, and established histories. Blogs, Wikipedia, and forum posts are used only as leads, never as the sole citation.
- **How sources are read:** papers are downloaded and converted to plain text, and each claim is located by searching that text, so the ledger quotes what the source actually says. When a publisher's site refuses automated access, the page is read from an Internet Archive snapshot, and the ledger says so. Scanned papers without a text layer are read as page images and run through OCR (Tesseract) so that quotes can be searched and cross-checked. When a primary source cannot be obtained at all (a paywalled newspaper archive, a book still in copyright), it is quoted through a published history that quotes it, and both the ledger and the text say so.
- **What "verified" means:** the source was fetched during the working session and the specific claim was found in it. What the model remembers is not a source.
- **Numbers in worked examples** are produced by scripts that can be re-run, not estimated [D-009]. When a script needs a public dataset (so far a Project Gutenberg novel and the GloVe word vectors), it downloads the file on first run, checks it against a recorded hash, and stops if the hash differs. The data itself is not stored in the repository [D-018].
- **Disputed history** is presented as disputed, with each side cited.
- **Fast-moving facts** carry an explicit "as of" date and are re-checked before each PDF build, along with pinned software versions.

The dates and names in `OUTLINE.md` are from the model's memory and are marked there as unverified. They are checked when each chapter reaches the research stage.

## Decisions and decision markers

Every choice that shapes the books is recorded in `DECISIONS.md` with an ID, a date, the reasoning, and how to undo it.

Each decision has a status:

- `active`: confirmed by the author
- `provisional`: a default chosen so work could continue, not yet confirmed
- `reverted`: withdrawn
- `superseded by D-NNN`: replaced by a later decision

**Markers.** Wherever a file depends on a decision, it cites the ID in square brackets, as this document does. In chapter files the marker is an HTML comment so that it does not appear in print. The markers make it possible to find every place a decision reaches.

**Changing a decision.** Old entries are never rewritten. The old entry's status is changed, a new entry is added if something replaces it, and then every file that cites the old ID is updated. The consistency check reports any file still citing a decision that is no longer live, so nothing is left behind.

**Parked questions.** Choices that do not need to be made yet are listed at the end of `DECISIONS.md`, each with the moment at which it should be raised.

## Keeping the whole consistent

A script, `tools/check.py`, is run after every change. It checks, among other things:

- every cited decision exists and is still live, and every live decision is cited somewhere
- chapter IDs are unique, and each chapter depends only on chapters that come before it
- chapter files match the outline
- Book 1 contains no code [D-003]
- no chapter marked verified or approved still carries a `TODO-VERIFY` marker
- every citation resolves to an entry in the bibliography [D-010]

Chapters have stable IDs and refer to each other by ID, never by number [D-010]. Numbers are assigned from the outline when the PDF is built, so a chapter can be split or moved without breaking references.

The script cannot judge prose. Terminology, notation, and tone are kept consistent by a read-through: when a chapter is verified, after any decision change that touches drafted chapters, and before any PDF build.

## Tools

Plain text files in a git repository. Chapters are Pandoc Markdown with a shared bibliography [D-010]. The consistency check needs only Python 3. Figures are drawn by Python scripts with matplotlib, so each one can be regenerated [D-014]. PDFs are produced by Pandoc with Typst as the typesetting engine [D-015].

The working rules for anyone contributing, human or AI, are in `AGENTS.md`. They do not depend on any particular tool or model.
