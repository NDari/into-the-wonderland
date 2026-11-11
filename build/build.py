#!/usr/bin/env python3
"""Build PDFs with Pandoc and Typst [D-015].

Usage:
  python3 build/build.py                one PDF of every Book 1 chapter that has a file
  python3 build/build.py <id> [<id>...] one PDF of the named chapters, in outline order

Output goes to out/. Chapter order comes from OUTLINE.md [D-010]. Links to
chapters that are not in the build become plain text (see links.lua).
Needs pandoc (3.x) and typst on the PATH; Python standard library only.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
BOOK_HEAD = re.compile(r"^## Book (\d+)\b")
CHAP_HEAD = re.compile(r"^#### .*\{#([a-z0-9-]+)\}\s*$")


def outline_order():
    """Return [(book, id)] in the order of OUTLINE.md."""
    order, book = [], None
    for line in (ROOT / "OUTLINE.md").read_text(encoding="utf-8").splitlines():
        head = BOOK_HEAD.match(line)
        if head:
            book = int(head.group(1))
        elif line.startswith("## "):
            book = None
        elif book and (chap := CHAP_HEAD.match(line)):
            order.append((book, chap.group(1)))
    return order


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
    files = [ROOT / f"book{b}" / "chapters" / f"{c}.md" for b, c in chosen]
    files = [f for f in files if f.exists()]
    if not files:
        sys.exit("no chapter files to build")
    if len({f.parent for f in files}) > 1:
        sys.exit("chapters from different books must be built separately")
    OUT.mkdir(exist_ok=True)
    target = OUT / f"{name}.pdf"
    cmd = [
        "pandoc", *map(str, files),
        "--lua-filter", str(ROOT / "build" / "links.lua"),
        "--citeproc", "--bibliography", str(ROOT / "references.bib"),
        "--resource-path", str(files[0].parent),
        "-M", "link-citations=true",
        "--pdf-engine", "typst",
        "-o", str(target),
    ]
    subprocess.run(cmd, check=True)
    print(f"wrote {target.relative_to(ROOT)} from {len(files)} chapter file(s)")


if __name__ == "__main__":
    main(sys.argv[1:])
