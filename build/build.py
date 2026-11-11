#!/usr/bin/env python3
"""Build PDFs with Pandoc and Typst [D-015].

Usage:
  python3 build/build.py                one PDF of every Book 1 chapter that has a file
  python3 build/build.py <id> [<id>...] one PDF of the named chapters, in outline order

Output goes to out/. Chapter order, chapter numbers and parts come from
OUTLINE.md [D-010]. Links to chapters that are not in the build become plain
text (see links.lua). Layout is in book.typ and book.lua [D-021]: every build
numbers its chapters; a whole-book build adds a title page, contents and part
pages.
Needs pandoc (3.x) and typst on the PATH; Python standard library only.
"""
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
BOOK_HEAD = re.compile(r"^## Book (\d+)\b(?: - (.+))?")
CHAP_HEAD = re.compile(r"^#### (?:([0-9A-Z]+)\. )?.*\{#([a-z0-9-]+)\}\s*$")
PART_HEAD = re.compile(r"^### (?:(.+?) - )?(.+)$")


def outline_order():
    """Return [(book, id)] in the order of OUTLINE.md."""
    return [(b, c) for b, c, _, _ in outline_entries()]


def outline_entries():
    """Return [(book, id, number, part)] in the order of OUTLINE.md.

    number is the printed chapter number or letter (None if unnumbered);
    part is the (label, title) of the ### heading the chapter sits under.
    """
    entries, book, part = [], None, None
    for line in (ROOT / "OUTLINE.md").read_text(encoding="utf-8").splitlines():
        head = BOOK_HEAD.match(line)
        if head:
            book, part = int(head.group(1)), None
        elif line.startswith("## "):
            book = None
        elif book and (sec := PART_HEAD.match(line)):
            part = (sec.group(1), sec.group(2))
        elif book and (chap := CHAP_HEAD.match(line)):
            entries.append((book, chap.group(2), chap.group(1), part))
    return entries


def book_subtitle(book):
    for line in (ROOT / "OUTLINE.md").read_text(encoding="utf-8").splitlines():
        head = BOOK_HEAD.match(line)
        if head and int(head.group(1)) == book:
            return f"Book {book}: {head.group(2)}" if head.group(2) else f"Book {book}"
    return f"Book {book}"


def layout_metadata(chosen, whole_book):
    """Chapter numbers and part pages for book.lua [D-021]."""
    entries = {c: (n, p) for _, c, n, p in outline_entries()}
    chapters, parts, seen = {}, {}, set()
    for book, cid in chosen:
        number, part = entries[cid]
        if number:
            kind = "Chapter" if number.isdigit() else "Appendix"
            chapters[cid] = {"label": number, "kind": kind}
        else:
            chapters[cid] = {"kind": "Chapter"}
        # A part page before the first chapter of each part; none for front matter.
        if whole_book and part and part not in seen and part[1] != "Front matter":
            seen.add(part)
            label, title = part
            parts[cid] = {"title": title, **({"label": label} if label else {})}
    meta = {"book-chapters": chapters, "book-parts": parts,
            # A 6 x 9 in book page, about 65 characters to a line.
            "papersize": "us-trade", "margin": {"x": "0.8in", "top": "0.9in", "bottom": "0.85in"}}
    if whole_book:
        meta["book-title"] = "Into the Wonderland"  # working title [D-013]
        meta["book-subtitle"] = book_subtitle(chosen[0][0])
        meta["book-date"] = f"Working draft, {datetime.date.today().isoformat()}"
    return meta


def main(args):
    order = outline_order()
    known = {cid for _, cid in order}
    unknown = [a for a in args if a not in known]
    if unknown:
        sys.exit(f"unknown chapter ID(s): {', '.join(unknown)}")
    if args:
        chosen = [(b, c) for b, c in order if c in args]
        name = args[0] if len(args) == 1 else "selection"
    else:
        chosen = [(b, c) for b, c in order if b == 1]
        name = "book1"
    chosen = [(b, c) for b, c in chosen
              if (ROOT / f"book{b}" / "chapters" / f"{c}.md").exists()]
    files = [ROOT / f"book{b}" / "chapters" / f"{c}.md" for b, c in chosen]
    if not files:
        sys.exit("no chapter files to build")
    if len({f.parent for f in files}) > 1:
        sys.exit("chapters from different books must be built separately")
    OUT.mkdir(exist_ok=True)
    target = OUT / f"{name}.pdf"
    meta = OUT / f"{name}-layout.json"
    meta.write_text(json.dumps(layout_metadata(chosen, not args), indent=1), encoding="utf-8")
    cmd = [
        "pandoc", *map(str, files),
        "--metadata-file", str(meta),
        "--include-in-header", str(ROOT / "build" / "book.typ"),
        "--lua-filter", str(ROOT / "build" / "links.lua"),
        "--lua-filter", str(ROOT / "build" / "book.lua"),
        "--citeproc", "--bibliography", str(ROOT / "references.bib"),
        "--resource-path", str(files[0].parent),
        "-M", "link-citations=true",
        "-M", "reference-section-title=References",
        "--pdf-engine", "typst",
        "-o", str(target),
    ]
    subprocess.run(cmd, check=True)
    print(f"wrote {target.relative_to(ROOT)} from {len(files)} chapter file(s)")


if __name__ == "__main__":
    main(sys.argv[1:])
