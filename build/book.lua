-- Book layout [D-021]: chapter numbers, part pages, title page and contents.
-- The Typst (PDF) output gets the full layout; EPUB gets plain headings.
-- build/build.py passes the numbers and parts from OUTLINE.md as metadata
-- (book-chapters, book-parts, book-title, ...), so nothing is hard-coded here.

local stringify = pandoc.utils.stringify

local function typst_inlines(inlines)
  local text = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), "typst")
  return (text:gsub("%s+$", ""))
end

local function quoted(s)
  return '"' .. s:gsub("\\", "\\\\"):gsub('"', '\\"') .. '"'
end

local function heading(body, label, supplement, ident)
  local numbering = label and ("(..n) => " .. quoted(label)) or "none"
  local raw = string.format("#heading(level: 1, numbering: %s, supplement: [%s])[%s]",
    numbering, supplement, body)
  if ident and ident ~= "" then raw = raw .. " <" .. ident .. ">" end
  return pandoc.RawBlock("typst", raw)
end

-- EPUB and other formats: plain headings, with the number in the title and
-- each part as its own short section. The reader's software builds the
-- title page and contents from the metadata.
local function plain(doc, chapters, parts)
  local blocks = {}
  for _, block in ipairs(doc.blocks) do
    local id = block.t == "Header" and block.level == 1 and block.identifier
    if id and parts[id] then
      local part = parts[id]
      local text = part.label and (stringify(part.label) .. ": " .. stringify(part.title))
        or stringify(part.title)
      table.insert(blocks, pandoc.Header(1, text, { class = "part" }))
    end
    if id and chapters[id] and chapters[id].label then
      block.content:insert(1, pandoc.Str(stringify(chapters[id].label) .. ". "))
    end
    table.insert(blocks, block)
  end
  doc.blocks = blocks
  return doc
end

function Pandoc(doc)
  local meta = doc.meta
  local chapters = meta["book-chapters"] or {}
  local parts = meta["book-parts"] or {}
  if FORMAT ~= "typst" then return plain(doc, chapters, parts) end
  local blocks = {}

  if meta["book-title"] then
    table.insert(blocks, pandoc.RawBlock("typst", string.format([[
#set page(numbering: none)
#v(1fr)
#align(center)[
  #text(size: 30pt, weight: "bold")[%s]
  #v(1em)
  #text(size: 16pt)[%s]
  #v(3em)
  #text(size: 11pt, fill: luma(90))[%s]
]
#v(2fr)
#pagebreak()
#set page(numbering: "i")
#counter(page).update(1)
#outline(title: [Contents], depth: 1)
#set page(numbering: "1")
#counter(page).update(1)]],
      typst_inlines(meta["book-title"]), typst_inlines(meta["book-subtitle"]),
      typst_inlines(meta["book-date"]))))
  end

  for _, block in ipairs(doc.blocks) do
    local id = block.t == "Header" and block.level == 1 and block.identifier
    if id and parts[id] then
      local part = parts[id]
      local label = part.label and stringify(part.label) or nil
      table.insert(blocks, heading(typst_inlines(part.title), label, "Part"))
    end
    if id and chapters[id] then
      local chap = chapters[id]
      local label = chap.label and stringify(chap.label) or nil
      table.insert(blocks, heading(typst_inlines(block.content), label, stringify(chap.kind), id))
    else
      table.insert(blocks, block)
    end
  end
  doc.blocks = blocks
  return doc
end
