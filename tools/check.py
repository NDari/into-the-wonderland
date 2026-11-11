#!/usr/bin/env python3
"""Consistency checks for the book repository.

Usage: python3 tools/check.py [repo_root]

Exits 0 when there are no errors. Warnings do not fail the run.

A check that enforces a decision names its ID in a comment. If that decision
is later reverted or superseded, this file is reported as holding a stale
reference, which is the reminder to update or remove the check.
"""
import re
import sys
from pathlib import Path

ROOT = (Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent).resolve()

SKIP_DIRS = {".git", "out", ".venv", "__pycache__", "node_modules"}
TEXT_SUFFIXES = {".md", ".py", ".bib", ".txt", ".yaml", ".yml", ".toml", ".sh", ".fish", ".tex", ".typ"}
STATUSES = ["outlined", "researched", "drafted", "verified", "approved"]

DEC_HEAD = re.compile(r"^## (D-\d{3}) (.+)$")
DEC_STATUS = re.compile(r"^- Status: (active|provisional|reverted|superseded by (D-\d{3}))\s*$")
DEC_REF = re.compile(r"\bD-\d{3}\b")
BOOK_HEAD = re.compile(r"^## Book (\d+)\b")
CHAP_HEAD = re.compile(r"^#### (?:(\d+|[A-Z])\. )?(.+?) \{#([a-z0-9-]+)\}\s*$")
FIELD = re.compile(r"^- \*\*(Status|Depends on|Builds on):\*\*\s*(.*)$")
ID_REF = re.compile(r"`([a-z0-9-]+)`")
FENCE = re.compile(r"^\s*(```|~~~)", re.M)
CITE_GROUP = re.compile(r"\[([^\[\]]*@[^\[\]]*)\]")
CITE_KEY = re.compile(r"(?<![\w.])@([A-Za-z0-9][\w:-]*)")
BIB_KEY = re.compile(r"^@\w+\{\s*([^,\s]+)\s*,", re.M)

errors = []
warnings = []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def rel(path):
    return str(path.relative_to(ROOT))


def text_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        yield path


def check_dashes(files):
    # Built from code points so this file never contains the characters it bans.
    bad = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")
    for path in files:
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if bad.search(line):
                err(f"{rel(path)}:{n}", "em-dash or en-dash found")


def parse_decisions():
    """Return {id: status}. Status is the full status string."""
    path = ROOT / "DECISIONS.md"
    if not path.exists():
        err("DECISIONS.md", "file is missing")
        return {}
    decisions = {}
    fields = {}
    current = None
    order = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        head = DEC_HEAD.match(line)
        if head:
            current = head.group(1)
            if current in decisions:
                err(f"DECISIONS.md:{n}", f"duplicate decision {current}")
            decisions[current] = None
            fields[current] = set()
            order.append(current)
            continue
        if line.startswith("#"):
            current = None
            continue
        if current is None:
            continue
        if line.startswith("- Status:"):
            status = DEC_STATUS.match(line)
            if status:
                decisions[current] = status.group(1)
            else:
                err(f"DECISIONS.md:{n}", f"{current} has an invalid status line")
        for name in ("Date", "Decision"):
            if line.startswith(f"- {name}:"):
                fields[current].add(name)
    for i, dec in enumerate(order, 1):
        if dec != f"D-{i:03d}":
            err("DECISIONS.md", f"decision IDs are not sequential at {dec} (expected D-{i:03d})")
            break
    for dec, status in decisions.items():
        if status is None:
            err("DECISIONS.md", f"{dec} has no valid Status line")
        elif status.startswith("superseded by"):
            target = status.split()[-1]
            if target not in decisions:
                err("DECISIONS.md", f"{dec} is superseded by unknown {target}")
        for name in ("Date", "Decision"):
            if name not in fields[dec]:
                err("DECISIONS.md", f"{dec} has no '{name}' line")
    return decisions


def check_decision_refs(files, decisions):
    live = {d for d, s in decisions.items() if s in ("active", "provisional")}
    cited = set()
    for path in files:
        if path.name == "DECISIONS.md" and path.parent == ROOT:
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for ref in DEC_REF.findall(line):
                if ref not in decisions:
                    err(f"{rel(path)}:{n}", f"cites unknown decision {ref}")
                elif ref not in live:
                    err(f"{rel(path)}:{n}", f"stale reference: {ref} is {decisions[ref]}")
                else:
                    cited.add(ref)
    for dec in sorted(live - cited):
        warn("DECISIONS.md", f"{dec} is live but cited nowhere, so nothing reflects it")


def parse_outline():
    """Return the list of chapters in book order."""
    path = ROOT / "OUTLINE.md"
    if not path.exists():
        err("OUTLINE.md", "file is missing")
        return []
    chapters = []
    book = None
    current = None
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            head = BOOK_HEAD.match(line)
            book = int(head.group(1)) if head else None
            current = None
            continue
        if book is None:
            continue
        if line.startswith("#### "):
            head = CHAP_HEAD.match(line)
            if not head:
                err(f"OUTLINE.md:{n}", "chapter heading has no {#id}")
                current = None
                continue
            current = {
                "book": book, "label": head.group(1), "title": head.group(2),
                "id": head.group(3), "line": n, "status": None,
                "Depends on": [], "Builds on": [],
            }
            chapters.append(current)
            continue
        field = FIELD.match(line)
        if field and current is not None:
            name, value = field.group(1), field.group(2).strip()
            if name == "Status":
                current["status"] = value
            else:
                ids = ID_REF.findall(value)
                if not ids and value.rstrip(".") != "none":
                    err(f"OUTLINE.md:{n}", f"'{name}' must list chapter IDs in backticks, or 'none'")
                current[name] = ids
    return chapters


def check_outline(chapters):
    index = {}
    for pos, ch in enumerate(chapters):
        where = f"OUTLINE.md:{ch['line']}"
        if ch["id"] in index:
            err(where, f"duplicate chapter ID '{ch['id']}'")
        else:
            index[ch["id"]] = pos
        if ch["status"] not in STATUSES:
            err(where, f"'{ch['id']}' has missing or invalid Status ({ch['status']})")
    for book in sorted({ch["book"] for ch in chapters}):
        numbers = [ch["label"] for ch in chapters if ch["book"] == book and ch["label"] and ch["label"].isdigit()]
        if numbers != [str(i) for i in range(1, len(numbers) + 1)]:
            err("OUTLINE.md", f"Book {book} chapter numbers are not sequential: {', '.join(numbers)}")
        letters = [ch["label"] for ch in chapters if ch["book"] == book and ch["label"] and ch["label"].isalpha()]
        if letters != [chr(ord("A") + i) for i in range(len(letters))]:
            err("OUTLINE.md", f"Book {book} appendix letters are not sequential: {', '.join(letters)}")
    for pos, ch in enumerate(chapters):
        where = f"OUTLINE.md:{ch['line']}"
        for name in ("Depends on", "Builds on"):
            for ref in ch[name]:
                if ref not in index:
                    err(where, f"'{ch['id']}' {name.lower()} unknown chapter '{ref}'")
                elif name == "Depends on" and index[ref] >= pos:
                    err(where, f"'{ch['id']}' depends on '{ref}', which does not come earlier")


def check_chapter_files(chapters):
    bib_path = ROOT / "references.bib"
    bib_keys = set(BIB_KEY.findall(bib_path.read_text(encoding="utf-8"))) if bib_path.exists() else None
    for book in sorted({ch["book"] for ch in chapters}):
        folder = ROOT / f"book{book}" / "chapters"
        ids = {ch["id"] for ch in chapters if ch["book"] == book}
        if folder.is_dir():
            for path in sorted(folder.glob("*.md")):
                if path.stem not in ids:
                    err(rel(path), f"no chapter with ID '{path.stem}' in Book {book} of OUTLINE.md")
    for ch in chapters:
        if ch["status"] not in STATUSES:
            continue
        path = ROOT / f"book{ch['book']}" / "chapters" / f"{ch['id']}.md"
        stage = STATUSES.index(ch["status"])
        if not path.exists():
            if stage >= STATUSES.index("drafted"):
                err("OUTLINE.md", f"'{ch['id']}' is {ch['status']} but {rel(path)} does not exist")
            continue
        if stage < STATUSES.index("drafted"):
            warn(rel(path), f"file exists but OUTLINE.md status is still '{ch['status']}'")
        text = path.read_text(encoding="utf-8")
        if stage >= STATUSES.index("verified") and "TODO-VERIFY" in text:
            err(rel(path), f"status is '{ch['status']}' but TODO-VERIFY markers remain")
        # D-003: Book 1 has no code.
        if ch["book"] == 1 and FENCE.search(text):
            err(rel(path), "Book 1 chapter contains a fenced code block")
        # D-010: every citation key resolves in references.bib.
        for group in CITE_GROUP.findall(text):
            for key in CITE_KEY.findall(group):
                if bib_keys is None:
                    err(rel(path), f"cites @{key} but references.bib does not exist")
                elif key not in bib_keys:
                    err(rel(path), f"cites @{key}, which is not in references.bib")


def main():
    files = list(text_files())
    check_dashes(files)
    decisions = parse_decisions()
    check_decision_refs(files, decisions)
    chapters = parse_outline()
    check_outline(chapters)
    check_chapter_files(chapters)

    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"ERROR: {line}")
    live = sum(1 for s in decisions.values() if s in ("active", "provisional"))
    print(f"{len(files)} files, {len(decisions)} decisions ({live} live), {len(chapters)} chapters: "
          f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
