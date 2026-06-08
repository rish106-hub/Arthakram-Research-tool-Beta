import React, { useState } from 'react'

export default function PerplexityTab({ sections }) {
  const [copied, setCopied] = useState(false)
  const content = sections['Perplexity Prompt'] || ''

  const handleCopy = () => {
    navigator.clipboard.writeText(content).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 2500)
    })
  }

  return (
    <div className="fade-in">
      <div className="perplexity-wrapper">
        <div className="perplexity-top-bar">
          <div className="perplexity-label">// Ready-to-use Perplexity Research Prompt</div>
          <button
            className={`btn-copy ${copied ? 'copied' : ''}`}
            onClick={handleCopy}
          >
            {copied ? '✓ Copied!' : '⎘ Copy Prompt'}
          </button>
        </div>

        <div className="perplexity-body">
          {content || 'Perplexity prompt not found. Please re-run the analysis.'}
        </div>

        <div className="perplexity-tip">
          <span>💡</span>
          <span>
            Paste this into <strong>Perplexity AI</strong> for niche-level research.
            Request specific numbers, named examples, and failure cases.
          </span>
        </div>
      </div>
    </div>
  )
}
