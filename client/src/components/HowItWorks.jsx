import React from 'react'

const STEPS = [
  { num: '01', title: 'Strip the Core Problem', desc: 'Removes noise. Rewrites the problem in one sentence. Identifies who, why now, and what changes if solved.' },
  { num: '02', title: 'First Principles Deconstruction', desc: 'Finds atomic value questions. Audits assumptions. Identifies the riskiest bet that could collapse your entire strategy.' },
  { num: '03', title: 'Business Anatomy', desc: 'Maps stakeholders, constraints, and success definitions. Separates what\'s non-negotiable from what\'s a variable.' },
  { num: '04', title: 'Derived Research Questions', desc: 'Specific, falsifiable questions traceable to the core problem — the ones competitor teams will miss.' },
  { num: '05', title: 'Perplexity Prompt', desc: 'A ready-to-copy research brief built for Perplexity AI. Benchmarks, failure patterns, customer psychology — all requested specifically.' },
  { num: '06', title: 'Research Angles', desc: '10–12 critical questions tagged [MARKET] [CUSTOMER] [FINANCIAL] [STRATEGIC] [OPERATIONAL] [RISK].' },
  { num: '07', title: 'Working Hypotheses', desc: '3 testable claims before research begins. "We believe X because Y. This would be false if Z." Start researching with direction.' },
]

export default function HowItWorks() {
  return (
    <section className="hiw-section" id="how-it-works">
      <div className="section-header">
        <div className="section-tag">// The Framework</div>
        <h2 className="section-title">7 steps from chaos<br />to clarity</h2>
        <p className="section-desc">
          Every problem gets the same rigorous treatment. No shortcuts,
          no surface-level analysis — just structured thinking that wins.
        </p>
      </div>

      <div className="steps-grid">
        {STEPS.map(s => (
          <div className="step-card" key={s.num}>
            <div className="step-num">{s.num}</div>
            <div className="step-content">
              <div className="step-title">{s.title}</div>
              <div className="step-desc">{s.desc}</div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}
