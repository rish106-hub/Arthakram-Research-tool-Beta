import React, { useState } from 'react'
import { renderMd } from '../../utils/parseMarkdown.js'

const ADVICE_SECTIONS = [
  { key: 'Core Problem', num: '01', title: 'Core Problem' },
  { key: 'First Principles Findings', num: '02', title: 'First Principles Findings' },
  { key: 'Business Anatomy', num: '03', title: 'Business Anatomy' },
  { key: 'Derived Research Questions', num: '04', title: 'Derived Research Questions' },
]

function AccordionItem({ num, title, content }) {
  const [open, setOpen] = useState(num === '01') // first one open by default

  return (
    <div className={`accordion-item ${open ? 'open' : ''}`}>
      <div className="accordion-header" onClick={() => setOpen(o => !o)}>
        <div className="accordion-header-left">
          <div className="accordion-num">{num}</div>
          <div className="accordion-title">{title}</div>
        </div>
        <span className="accordion-chevron">{open ? '▲' : '▼'}</span>
      </div>
      {open && (
        <div className="accordion-body">
          <div
            className="accordion-body-inner"
            dangerouslySetInnerHTML={{ __html: renderMd(content) }}
          />
        </div>
      )}
    </div>
  )
}

export default function AdviceTab({ sections }) {
  return (
    <div className="accordion fade-in">
      {ADVICE_SECTIONS.map(s => (
        <AccordionItem
          key={s.key}
          num={s.num}
          title={s.title}
          content={sections[s.key] || 'No content found for this section.'}
        />
      ))}
    </div>
  )
}
