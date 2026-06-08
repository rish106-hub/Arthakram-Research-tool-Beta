/**
 * parseSections(markdown)
 * 
 * Splits a markdown string by ## headings into a map of
 * { "Section Title": "content under that heading" }
 */
export function parseSections(markdown) {
  const sections = {}
  // Split on lines that start with ## 
  const parts = markdown.split(/^## /m)
  parts.forEach(part => {
    if (!part.trim()) return
    const firstNewline = part.indexOf('\n')
    if (firstNewline === -1) return
    const heading = part.slice(0, firstNewline).trim()
    const content = part.slice(firstNewline + 1).trim()
    sections[heading] = content
  })
  return sections
}

/**
 * renderMd(text)
 * Returns __html for dangerouslySetInnerHTML using a tiny subset of markdown:
 * headers, bold, italic, bullets, line breaks.
 * We avoid importing a full marked.js dep in each component.
 */
export function renderMd(text) {
  if (!text) return ''
  let html = text
    // h3
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    // bold
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    // italic
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    // bullets
    .replace(/^[-*] (.+)$/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>\n?)+/g, m => `<ul>${m}</ul>`)
    // numbered list
    .replace(/^\d+\. (.+)$/gm, '<li>$1</li>')
    // blank lines → paragraph breaks
    .replace(/\n\n/g, '</p><p>')
    .replace(/\n/g, '<br/>')
  return `<div class="md-content"><p>${html}</p></div>`
}
