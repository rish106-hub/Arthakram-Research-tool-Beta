import React from 'react'

const TAG_CLASS = {
  'MARKET': 'tag-market',
  'CUSTOMER': 'tag-customer',
  'FINANCIAL': 'tag-financial',
  'STRATEGIC': 'tag-strategic',
  'OPERATIONAL': 'tag-operational',
  'RISK': 'tag-risk',
}

/**
 * Parse research angles — each line like:
 * "1. [MARKET] What is the actual CAC..."
 * or just bullet points
 */
function parseAngles(text) {
  const lines = text.split('\n').filter(l => l.trim())
  return lines.map(line => {
    const tagMatch = line.match(/\[([A-Z]+)\]/)
    const tag = tagMatch ? tagMatch[1] : null
    const clean = line
      .replace(/^\d+\.\s*/, '')
      .replace(/^[-*]\s*/, '')
      .replace(/\[[A-Z]+\]\s*/, '')
      .replace(/^[-–—]\s*/, '')
      .trim()
    return { tag, text: clean }
  }).filter(a => a.text.length > 5)
}

/**
 * Parse working hypotheses — 3 "We believe..." blocks
 */
function parseHypotheses(text) {
  // Try to split on numbered patterns or "We believe"
  const blocks = text.split(/\n(?=\d+\.|\*\*\d|\bWe believe)/i).filter(b => b.trim())
  if (blocks.length === 0) {
    // fallback: just split by double newline
    return text.split(/\n\n+/).filter(b => b.trim()).slice(0, 3).map(b => ({ full: b }))
  }
  return blocks.slice(0, 3).map(block => {
    const conditionMatch = block.match(/This would be false if[:\s]+(.+)/i)
    const condition = conditionMatch ? conditionMatch[1].trim() : null
    const main = block.replace(/This would be false if[:\s]+.+/i, '').trim()
    return { full: main, condition }
  })
}

export default function DeckBlueprintTab({ sections }) {
  const anglesText = sections['Research Angles'] || ''
  const hypothesesText = sections['Working Hypotheses'] || ''

  const angles = parseAngles(anglesText)
  const hypotheses = parseHypotheses(hypothesesText)

  return (
    <div className="fade-in">
      {/* Research Angles */}
      <div className="deck-section">
        <div className="deck-section-title">
          <span>📊</span> Research Angles
          <span style={{ fontSize: '0.75rem', color: 'var(--text-dim)', fontFamily: 'Fira Code, monospace', fontWeight: 400 }}>
            — prioritised from most to least critical
          </span>
        </div>
        <div className="angles-grid">
          {angles.length > 0 ? angles.map((a, i) => (
            <div className="angle-card" key={i}>
              {a.tag && (
                <span className={`angle-tag ${TAG_CLASS[a.tag] || 'tag-default'}`}>
                  {a.tag}
                </span>
              )}
              <span className="angle-text">{a.text}</span>
            </div>
          )) : (
            <div style={{ color: 'var(--text-muted)', fontSize: '0.88rem' }}>
              No research angles found. Check the Strategic Advice tab.
            </div>
          )}
        </div>
      </div>

      {/* Working Hypotheses */}
      <div className="deck-section">
        <div className="deck-section-title">
          <span>🧪</span> Working Hypotheses
          <span style={{ fontSize: '0.75rem', color: 'var(--text-dim)', fontFamily: 'Fira Code, monospace', fontWeight: 400 }}>
            — test these before anything else
          </span>
        </div>
        <div className="hypothesis-cards">
          {hypotheses.map((h, i) => (
            <div className="hypothesis-card" key={i}>
              <div className="hypothesis-num">Hypothesis {String(i + 1).padStart(2, '0')}</div>
              <div className="hypothesis-text">{h.full}</div>
              {h.condition && (
                <div className="hypothesis-condition">
                  ⚠ This would be false if: {h.condition}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
