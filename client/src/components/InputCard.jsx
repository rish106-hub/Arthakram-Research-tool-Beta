import React, { useRef } from 'react'

export default function InputCard({ onAnalyse, loading }) {
  const textareaRef = useRef(null)

  const handleKeyDown = (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault()
      onAnalyse(textareaRef.current.value)
    }
  }

  const handleClick = () => {
    onAnalyse(textareaRef.current.value)
  }

  return (
    <div className="input-card">
      <label className="input-label" htmlFor="problemInput">// Problem Statement</label>
      <textarea
        id="problemInput"
        ref={textareaRef}
        className="problem-textarea"
        disabled={loading}
        placeholder={"Paste your case competition problem statement here...\n\nExample: How can a D2C specialty coffee brand in Tier-2 Indian cities acquire its first 1,000 loyal customers within 6 months with a budget of ₹20 lakhs?"}
        onKeyDown={handleKeyDown}
      />
      <div className="input-footer">
        <div className="shortcut-hint">
          Press <span className="key-badge">⌘</span>
          <span style={{ margin: '0 2px' }}>+</span>
          <span className="key-badge">Enter</span>
          &nbsp;to analyse
        </div>
        <div className="btn-row">
          <button className="btn-pdf" disabled title="Coming in Phase 2">
            Upload PDF — Soon
          </button>
          <button
            className="btn-analyse"
            onClick={handleClick}
            disabled={loading}
          >
            {loading ? '⏳ Analysing...' : '⚡ Analyse'}
          </button>
        </div>
      </div>
    </div>
  )
}
