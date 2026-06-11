import React from 'react'

const STEPS = [
  { name: 'Building Quick Brief', desc: 'Condensing the problem into 3 actionable lines' },
  { name: 'Stripping Core Problem', desc: 'Removing noise, finding the one sentence that matters' },
  { name: 'First Principles', desc: 'Breaking assumptions, finding what\'s actually true' },
  { name: 'Business Anatomy', desc: 'Mapping stakeholders, constraints & success metrics' },
  { name: 'Research Questions', desc: 'Deriving specific, falsifiable questions' },
  { name: 'Perplexity Prompt', desc: 'Crafting a niche-level research brief' },
  { name: 'Research Angles', desc: 'Tagging 10–12 critical blindspot questions' },
  { name: 'Working Hypotheses', desc: 'Forming 3 testable claims before research' },
]

export default function StepTracker({ currentStep }) {
  return (
    <div className="step-tracker">
      {STEPS.map((s, i) => {
        const isDone = i < currentStep
        const isActive = i === currentStep
        return (
          <div
            key={i}
            className={`tracker-item ${isDone ? 'done' : ''} ${isActive ? 'active' : ''}`}
          >
            <div className="tracker-dot">
              {isDone
                ? <span className="tracker-checkmark">✓</span>
                : <div className="tracker-dot-inner" />
              }
            </div>
            <div>
              <div className="tracker-step-name">{s.name}</div>
              <div className="tracker-step-desc">{s.desc}</div>
            </div>
          </div>
        )
      })}
    </div>
  )
}
