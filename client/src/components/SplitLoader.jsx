import React from 'react'
import MindMapCanvas from './MindMapCanvas.jsx'
import StepTracker from './StepTracker.jsx'

export default function SplitLoader({ currentStep }) {
  return (
    <div className="split-loader">
      <div className="loader-left">
        <div className="loader-canvas-label">// Building Research Map</div>
        <MindMapCanvas />
      </div>
      <div className="loader-right">
        <div className="loader-right-title">// AI Processing Steps</div>
        <StepTracker currentStep={currentStep} />
      </div>
    </div>
  )
}
