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

return {
  { Header = collect, Div = collect, Span = collect, Figure = collect },
  { Link = unlink },
}
