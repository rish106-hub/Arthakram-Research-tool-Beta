import React, { useState } from 'react'
import QuickBriefTab from './tabs/QuickBriefTab.jsx'
import AdviceTab from './tabs/AdviceTab.jsx'
import DeckBlueprintTab from './tabs/DeckBlueprintTab.jsx'
import PerplexityTab from './tabs/PerplexityTab.jsx'

const TABS = [
  { id: 'brief', icon: '⚡', label: 'Quick Brief' },
  { id: 'advice', icon: '🧠', label: 'Strategic Advice' },
  { id: 'deck', icon: '📊', label: 'Deck Blueprint' },
  { id: 'perplexity', icon: '🔍', label: 'Perplexity Prompt' },
]

export default function ResultsView({ sections, onReset }) {
  const [activeTab, setActiveTab] = useState('brief')

  return (
    <div className="results-view">
      {/* Top bar */}
      <div className="results-meta">
        <div className="results-title">
          <div className="results-title-badge">
            <span className="results-title-dot" />
            Research Complete
          </div>
          <span className="results-title-text">Your brief is ready</span>
        </div>
        <button className="btn-outline" onClick={onReset}>
          ↺ New Analysis
        </button>
      </div>

      {/* Tab bar */}
      <div className="tab-bar" role="tablist">
        {TABS.map(t => (
          <button
            key={t.id}
            className={`tab-btn ${activeTab === t.id ? 'active' : ''}`}
            onClick={() => setActiveTab(t.id)}
            role="tab"
            aria-selected={activeTab === t.id}
          >
            <span className="tab-icon">{t.icon}</span>
            {t.label}
          </button>
        ))}
      </div>

      {/* Tab content */}
      {activeTab === 'brief' && (
        <QuickBriefTab
          sections={sections}
          onGoToPerplexity={() => setActiveTab('perplexity')}
        />
      )}
      {activeTab === 'advice' && <AdviceTab sections={sections} />}
      {activeTab === 'deck' && <DeckBlueprintTab sections={sections} />}
      {activeTab === 'perplexity' && <PerplexityTab sections={sections} />}
    </div>
  )
}
