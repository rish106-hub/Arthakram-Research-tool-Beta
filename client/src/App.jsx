import React, { useState, useCallback } from 'react'
import Nav from './components/Nav.jsx'
import LandingPage from './components/LandingPage.jsx'
import InputCard from './components/InputCard.jsx'
import SplitLoader from './components/SplitLoader.jsx'
import ResultsView from './components/ResultsView.jsx'
import { parseSections } from './utils/parseMarkdown.js'

// Map section headers that appear in the streamed markdown → step index
// Step 0 = Quick Brief, Step 1 = Core Problem, ... Step 7 = Working Hypotheses
const SECTION_STEP_MAP = [
  { header: '## Quick Brief', step: 0 },
  { header: '## Core Problem', step: 1 },
  { header: '## First Principles Findings', step: 2 },
  { header: '## Business Anatomy', step: 3 },
  { header: '## Derived Research Questions', step: 4 },
  { header: '## Perplexity Prompt', step: 5 },
  { header: '## Research Angles', step: 6 },
  { header: '## Working Hypotheses', step: 7 },
]

// view: 'landing' | 'tool'
// status: 'idle' | 'loading' | 'done' | 'error'
export default function App() {
  const [view, setView] = useState('landing')
  const [status, setStatus] = useState('idle')
  const [currentStep, setCurrentStep] = useState(-1)
  const [sections, setSections] = useState({})
  const [error, setError] = useState(null)

  const showTool = () => {
    setView('tool')
    setStatus('idle')
    setCurrentStep(-1)
    setSections({})
    setError(null)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  const showLanding = () => {
    setView('landing')
    setStatus('idle')
    setCurrentStep(-1)
    setSections({})
    setError(null)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  const resetTool = () => {
    setStatus('idle')
    setCurrentStep(-1)
    setSections({})
    setError(null)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  const analyse = useCallback(async (problem) => {
    if (!problem?.trim()) return

    setStatus('loading')
    setCurrentStep(0)
    setError(null)
    setSections({})

    let accumulated = ''

    try {
      const res = await fetch('/analyze-stream', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ problem: problem.trim() }),
      })

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}))
        throw new Error(errData.error || `Server error ${res.status}`)
      }

      const reader = res.body.getReader()
      const decoder = new TextDecoder()
      let buffer = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })

        // Process all complete SSE events in the buffer
        const lines = buffer.split('\n')
        buffer = lines.pop() // keep incomplete line

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue
          const jsonStr = line.slice(6).trim()
          if (!jsonStr) continue

          let event
          try { event = JSON.parse(jsonStr) } catch { continue }

          if (event.type === 'error') {
            throw new Error(event.message || 'Unknown streaming error')
          }

          if (event.type === 'chunk' || event.type === 'done') {
            accumulated = event.accumulated || event.full || accumulated

            // Detect which section header just appeared → advance step
            let detectedStep = -1
            for (const { header, step } of SECTION_STEP_MAP) {
              if (accumulated.includes(header)) {
                detectedStep = Math.max(detectedStep, step)
              }
            }
            if (detectedStep >= 0) {
              setCurrentStep(detectedStep)
            }
          }

          if (event.type === 'done') {
            const parsed = parseSections(accumulated)
            setSections(parsed)
            setCurrentStep(8) // All done
            setStatus('done')
          }
        }
      }
    } catch (err) {
      setError(err.message || 'Something went wrong. Please try again.')
      setStatus('error')
    }
  }, [])

  return (
    <>
      {/* Fixed animated background orbs */}
      <div className="bg-orbs">
        <div className="orb orb-1" />
        <div className="orb orb-2" />
        <div className="orb orb-3" />
      </div>

      <Nav
        onLogoClick={showLanding}
        showCta={view === 'landing'}
        onCtaClick={showTool}
      />

      {view === 'landing' && (
        <LandingPage onStart={showTool} />
      )}

      {view === 'tool' && (
        <div className="tool-view">
          <div className="tool-container">
            <button className="back-link" onClick={showLanding}>
              ← Back to home
            </button>

            {(status === 'idle' || status === 'loading') && (
              <div className="tool-header fade-up">
                <h1>Research Brief Generator</h1>
                <p>Paste your case competition problem statement below and hit Analyse.</p>
              </div>
            )}

            {(status === 'idle' || status === 'loading') && (
              <InputCard onAnalyse={analyse} loading={status === 'loading'} />
            )}

            {status === 'loading' && (
              <SplitLoader currentStep={currentStep} />
            )}

            {status === 'error' && (
              <div className="error-box fade-in" style={{ marginBottom: '24px' }}>
                ⚠ {error}
                <button
                  onClick={resetTool}
                  style={{
                    display: 'block', marginTop: '12px',
                    background: 'none', border: '1px solid #3a1212',
                    color: '#e88080', padding: '6px 14px', borderRadius: '6px',
                    cursor: 'pointer', fontFamily: 'DM Sans, sans-serif'
                  }}
                >
                  Try Again
                </button>
              </div>
            )}

            {status === 'done' && (
              <ResultsView sections={sections} onReset={resetTool} />
            )}
          </div>

          <div className="tool-footer">
            Built by{' '}
            <a href="https://github.com/rish106-hub" target="_blank" rel="noreferrer">Rishav Dewan</a>
            {' '}&amp;{' '}
            <a href="https://github.com/RedRangerWentWild" target="_blank" rel="noreferrer">Aadi Kalra</a>
            {' '}· Arthakram Consulting Club · Rishihood University
          </div>
        </div>
      )}
    </>
  )
}
