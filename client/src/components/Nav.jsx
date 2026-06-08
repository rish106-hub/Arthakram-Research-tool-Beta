import React from 'react'

export default function Nav({ onLogoClick, showCta, onCtaClick }) {
  return (
    <nav className="nav">
      <div className="nav-logo" onClick={onLogoClick} role="button" tabIndex={0}
        onKeyDown={e => e.key === 'Enter' && onLogoClick()}>
        <div className="nav-logo-icon">A</div>
        <span className="nav-logo-text">Arthakram</span>
      </div>

      <div className="nav-badge">by Rishihood University</div>

      {showCta && (
        <button className="btn-primary" onClick={onCtaClick}
          style={{ padding: '8px 20px', fontSize: '0.85rem', boxShadow: 'none' }}>
          Start Researching →
        </button>
      )}
    </nav>
  )
}
