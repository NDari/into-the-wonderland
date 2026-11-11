-- Pandoc filter: keep links to chapters that are in this build, and turn
-- links to chapters that are not (not drafted yet, or left out of a
-- single-chapter build) into plain text, so the PDF still builds [D-015].

local ids = {}

local function collect(el)
  if el.identifier and el.identifier ~= "" then
    ids[el.identifier] = true
  end
end

local function unlink(el)
  local target = el.target:match("^#(.+)$")
  if target and not ids[target] then
    return pandoc.Span(el.content)
  end
end

-- Typst renders an apostrophe after a digit as a prime ("Llama 2's" would
-- print as a foot mark), so pass those apostrophes through as raw text.
local APOS = "\u{2019}"

local function apostrophes(el)
  if not el.text:find("%d" .. APOS) then
    return nil
  end
  local out, rest = {}, el.text
  while true do
    local i, j = rest:find("%d" .. APOS)
    if not i then break end
    table.insert(out, pandoc.Str(rest:sub(1, i)))
    table.insert(out, pandoc.RawInline("typst", APOS))
    rest = rest:sub(j + 1)
  end
  if rest ~= "" then table.insert(out, pandoc.Str(rest)) end
  return out
end

return {
  { Header = collect, Div = collect, Span = collect, Figure = collect },
  { Link = unlink },
  { Str = apostrophes },
}
