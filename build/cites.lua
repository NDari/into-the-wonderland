-- Numbered citations with one reference list per chapter [D-024].
-- Runs before links.lua and book.lua. The book is split at its level-1
-- headings; each chapter goes through citeproc on its own, so numbering
-- starts at [1] in every chapter and its references follow it. Reference
-- anchors get the chapter ID in their name, so a source cited in several
-- chapters links to the right list each time.

-- Citeproc writes page ranges and some notes with en-dashes; the books use
-- plain hyphens throughout.
local function hyphens(el)
  local text = el.text:gsub("\u{2013}", "-"):gsub("\u{2014}", "-")
  if text ~= el.text then return pandoc.Str(text) end
end

local function chapter(blocks, meta, id)
  local sub = pandoc.utils.citeproc(pandoc.Pandoc(blocks, meta))
  local prefix = "ref-" .. id .. "-"
  local refs
  sub = sub:walk({
    Cite = function(c) return pandoc.Span(c.content, { class = "citation" }) end,
    Link = function(l)
      local key = l.target:match("^#ref%-(.+)$")
      if key then l.target = "#" .. prefix .. key; return l end
    end,
    Div = function(d)
      if d.identifier == "refs" then
        d.identifier = "refs-" .. id
        refs = d
        return d
      end
      local key = d.identifier:match("^ref%-(.+)$")
      if key then
        d.identifier = prefix .. key
        d.content = d.content:walk({ Str = hyphens })
        return d
      end
    end,
  })
  local out = sub.blocks
  if refs and #refs.content > 0 then
    -- citeproc appends the list as the last block; give it a heading.
    out:insert(#out, pandoc.Header(2, "References",
      { id = "references-" .. id, class = "unnumbered" }))
  end
  return out:walk({ Span = function(s)
    if s.classes:includes("citation") then return s:walk({ Str = hyphens }) end
  end })
end

function Pandoc(doc)
  local meta = {
    bibliography = doc.meta["cites-bibliography"],
    csl = doc.meta["cites-csl"],
    ["link-citations"] = true,
  }
  local groups, cur = {}, nil
  for _, block in ipairs(doc.blocks) do
    if not cur or (block.t == "Header" and block.level == 1) then
      local id = block.t == "Header" and block.identifier or ""
      if id == "" then id = tostring(#groups + 1) end
      cur = { id = id, blocks = pandoc.Blocks({}) }
      table.insert(groups, cur)
    end
    cur.blocks:insert(block)
  end
  local blocks = pandoc.Blocks({})
  for _, g in ipairs(groups) do
    blocks:extend(chapter(g.blocks, meta, g.id))
  end
  doc.blocks = blocks
  return doc
end
