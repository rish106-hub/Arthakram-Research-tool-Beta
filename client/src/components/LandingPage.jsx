import React from 'react'
import HowItWorks from './HowItWorks.jsx'

export default function LandingPage({ onStart }) {
  return (
    <div className="landing">
      {/* Hero */}
      <section className="hero">
        <div className="hero-eyebrow">
          <span className="hero-eyebrow-dot" />
          First-principles case research · Powered by Gemini 2.5 Flash
        </div>
        <h1 className="hero-headline">
          Win case comps<br />with <span className="accent">smarter research.</span>
        </h1>
        <p className="hero-sub">
          Paste your problem statement. Arthakram breaks it down using a{' '}
          <strong>7-step first-principles framework</strong> and returns a
          structured research brief in under 30 seconds.
        </p>
        <div className="hero-cta-group">
          <button className="btn-primary" onClick={onStart}>
            Analyse a Problem <span>→</span>
          </button>
          <a className="btn-ghost" href="#how-it-works">
            How it works ↓
          </a>
        </div>

        <div className="hero-stats">
          <div className="stat-item">
            <div className="stat-value"><span className="stat-accent">7</span></div>
            <div className="stat-label">Research dimensions</div>
          </div>
          <div className="stat-sep" />
          <div className="stat-item">
            <div className="stat-value"><span className="stat-accent">30s</span></div>
            <div className="stat-label">Average response time</div>
          </div>
          <div className="stat-sep" />
          <div className="stat-item">
            <div className="stat-value"><span className="stat-accent">0→</span></div>
            <div className="stat-label">Prior research needed</div>
          </div>
          <div className="stat-sep" />
          <div className="stat-item">
            <div className="stat-value"><span className="stat-accent">∞</span></div>
            <div className="stat-label">Perplexity prompts generated</div>
          </div>
        </div>
      </section>

      <HowItWorks />

      {/* Bottom CTA Banner */}
      <div className="cta-banner">
        <h2>Ready to compete smarter?</h2>
        <p>Paste your problem statement and get your research brief in under 30 seconds.</p>
        <button className="btn-primary" onClick={onStart}>
          Start Researching <span>→</span>
        </button>
      </div>
    </div>
  )
}
