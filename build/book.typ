// Book layout [D-021], included in the Typst preamble by build/build.py.
// Chapter and part headings come from build/book.lua, which marks parts
// with the supplement [Part] and gives chapters a fixed number from OUTLINE.md.

// Space around section headings: a blank line below, more above.
#show heading.where(level: 2): set block(above: 2.2em, below: 1.1em)
#show heading.where(level: 3): set block(above: 1.8em, below: 1em)
#show heading.where(level: 4): set block(above: 1.6em, below: 0.9em)

// Tables: long ones may continue on the next page; cells are set ragged
// right and a little smaller so narrow columns stay readable.
#show figure.where(kind: table): set block(breakable: true)
#show table: set par(justify: false)
#show table: set text(size: 9pt)

// Figures: a tall drawing is scaled down so its caption fits on the page.
#show image: it => layout(size => {
  let natural = measure(it, width: size.width)
  if natural.height > 4.6in { image(it.source, height: 4.6in, alt: it.alt) } else { it }
})

// Chapters, parts and the reference list each start on a new page.
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  if it.supplement == [Part] {
    v(1fr)
    align(center, block({
      if it.numbering != none {
        text(size: 13pt, tracking: 0.12em, upper(counter(heading).display(it.numbering)))
        v(1.2em)
      }
      text(size: 24pt, weight: "bold", hyphenate: false, it.body)
    }))
    v(2fr)
    pagebreak(weak: true)
  } else {
    v(2.5cm)
    if it.numbering != none {
      text(size: 11pt, tracking: 0.12em, fill: luma(90),
        upper[#it.supplement #counter(heading).display(it.numbering)])
      v(0.8em)
    }
    block(below: 2.4em, text(size: 21pt, weight: "bold", hyphenate: false, it.body))
  }
}

// Running head: the chapter title, except on pages where a chapter starts.
#set page(header: context {
  let p = here().page()
  if query(heading.where(level: 1)).any(h => h.location().page() == p) { return }
  let prev = query(heading.where(level: 1).before(here()))
  if prev.len() == 0 or prev.last().supplement == [Part] { return }
  set text(size: 8.5pt, fill: luma(110))
  align(right, prev.last().body)
})

// Contents: parts in bold with space above them.
#show outline.entry.where(level: 1): it => {
  if it.element.supplement == [Part] {
    v(1.2em, weak: true)
    strong(it)
  } else {
    it
  }
}
