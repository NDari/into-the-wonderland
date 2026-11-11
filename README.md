# Into the Wonderland

Two companion books that take a reader from the first artificial neuron to modern large language models (LLMs), covering both the ideas and the history that produced them [D-001]. *Into the Wonderland* is the working title for the pair [D-013].

- **Book 1 - Concepts and history.** For someone who knew data science as it was practiced in the 2000s and has not followed the field since. Intuition, diagrams, and worked numeric examples; no derivations [D-002] and no code [D-003]. A reader finishes it able to explain how an LLM works, name its parts, and read current writing about the field.
- **Book 2 - Building and running.** For a reader of Book 1 who wants to see the ideas run. A bit deeper and more technical. Build a tiny GPT and train it once [D-006], then run a real open-weight model with llama.cpp and study an agent harness, Tau [D-007].

Book 1 is the priority and stands on its own.

## Status

As of 2026-11-10: design and outline only. No chapter has been researched or drafted yet. `OUTLINE.md` lists every planned chapter and its current status.

## Who made this

Written and researched by Claude, Anthropic's AI model. Read, edited for prose, and double-checked by Naseer Dari.

The process, including how sources are verified and how decisions are tracked, is described in `how-these-books-were-made.md`.

## Layout

What exists today:

```
README.md                      this file
how-these-books-were-made.md   the process behind the books
AGENTS.md                      working rules for AI agents and humans
DECISIONS.md                   decision log and parked questions
OUTLINE.md                     both books: chapters, IDs, order, status
tools/check.py                 consistency checks
```

Chapters, source ledgers, the bibliography, figures, code, and the PDF build are added as the work reaches them. The planned locations are listed in `AGENTS.md` under "Repository layout".

## Checking consistency

```
python3 tools/check.py
```

Needs only Python 3 and its standard library. It exits with an error if, for example, a file still relies on a decision that has been reverted, a chapter depends on one that comes later, or a Book 1 chapter contains code. The full list of checks is in `AGENTS.md` under "Decisions and consistency".

## Working on the books

Any AI agent or human contributor should start with `AGENTS.md`. Nothing in this repository requires a particular tool or model.
