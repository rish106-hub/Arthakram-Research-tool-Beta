import React from 'react'
import { renderMd } from '../../utils/parseMarkdown.js'

export default function QuickBriefTab({ sections, onGoToPerplexity }) {
  const brief = sections['Quick Brief'] || ''

  // Parse the 3 lines out of the Quick Brief section
  const problemMatch = brief.match(/Problem in one line[:\s*]*(.+)/i)
  const directionMatch = brief.match(/Proposed direction in one line[:\s*]*(.+)/i)
  const nextStepMatch = brief.match(/Immediate next step[:\s*]*(.+)/i)

  // Fallback: try to extract from Core Problem if Quick Brief wasn't parsed
  const coreProblem = sections['Core Problem'] || ''

  const problem = problemMatch?.[1]?.replace(/^\*+|\*+$/g, '').trim()
    || coreProblem.split('\n')[0]?.slice(0, 200) || 'Unable to parse — view Strategic Advice tab.'
  const direction = directionMatch?.[1]?.replace(/^\*+|\*+$/g, '').trim()
    || 'See Strategic Advice tab for recommendations.'
  const nextStep = nextStepMatch?.[1]?.replace(/^\*+|\*+$/g, '').trim()
    || 'Open the Perplexity Prompt tab and run the research brief.'

  return (
    <div className="fade-in">
      <div className="quick-brief-grid">
        <div className="brief-card">
          <div className="brief-icon">🔴</div>
          <div style={{ flex: 1 }}>
            <div className="brief-card-label red">The Problem</div>
            <div className="brief-card-text">{problem}</div>
          </div>
        </div>

        <div className="brief-card">
          <div className="brief-icon">🟠</div>
          <div style={{ flex: 1 }}>
            <div className="brief-card-label orange">Proposed Direction</div>
            <div className="brief-card-text">{direction}</div>
          </div>
        </div>

        <div className="brief-card">
          <div className="brief-icon">✅</div>
          <div style={{ flex: 1 }}>
            <div className="brief-card-label green">Your Immediate Next Step</div>
            <div className="brief-card-text">{nextStep}</div>
          </div>
        </div>
      </div>

      <div className="quick-brief-cta">
        <div className="quick-brief-cta-text">
          <strong>Ready to research?</strong> The Perplexity Prompt is pre-built — just copy and paste it.
        </div>
        <button className="btn-primary" onClick={onGoToPerplexity}
          style={{ padding: '10px 22px', fontSize: '0.85rem' }}>
          Get Perplexity Prompt →
        </button>
      </div>
    </div>
  )
}
