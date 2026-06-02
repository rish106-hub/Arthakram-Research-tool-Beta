# Case comp. Research Tool - BETA 

> Paste your case competition problem statement. Get a first-principles research brief, a ready-to-copy Perplexity prompt, and targeted research angles — in seconds.

---

## What It Does

Case competition teams waste time on broad, generic research. Arthakram forces specificity from the start.

Paste a problem statement → the tool runs it through a 7-step first-principles framework powered by Gemini 2.5 Flash → returns a structured research brief with:

- **Core Problem** — stripped to one sentence with impact analysis
- **First Principles Findings** — assumption inventory, conventional wisdom audit, riskiest bet identification
- **Business Anatomy** — stakeholder map, constraints, success definition, scope
- **Derived Research Questions** — specific, falsifiable questions a competitor team will miss
- **Perplexity Prompt** — a ready-to-copy research brief structured for niche-level insight
- **Research Angles** — 10–12 questions tagged by type (Market / Customer / Financial / Strategic / Operational / Risk)
- **Working Hypotheses** — 3 testable claims with explicit falsifiability conditions

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI | Google Gemini 2.0 Flash (`gemini-2.0-flash`) |
| Frontend | Plain HTML, CSS, Vanilla JavaScript |
| Markdown rendering | marked.js (CDN) |
| Fonts | Syne, DM Sans, Fira Code (Google Fonts CDN) |
| PDF parsing (Phase 2) | pdfplumber |

---

## Project Structure

```
case-comp-tool/
├── app.py              # Flask backend — routes, Gemini integration, system prompt
├── index.html          # Single-page frontend — UI, markdown rendering, copy logic
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed)
└── README.md
```

---

## Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Create `.env` file**
```
GEMINI_API_KEY=your_key_here
```

Get a key at [aistudio.google.com](https://aistudio.google.com).

**3. Run the server**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

---

## Usage

1. Paste a case competition problem statement into the textarea
2. Click **Analyse** (or press `Ctrl+Enter` / `Cmd+Enter`)
3. Wait ~15–30 seconds for Gemini to process
4. Read through the structured research brief
5. Click **Copy Prompt** on the Perplexity Prompt section to copy it directly to clipboard
6. Paste into [Perplexity](https://perplexity.ai) and run

---

## API Reference

### `GET /`
Serves `index.html`.

---

### `POST /analyze`

Accepts a problem statement, returns a structured markdown research brief.

**Request**
```json
{
  "problem": "string (required)"
}
```

**Response — success**
```json
{
  "result": "string (markdown)"
}
```

**Response — error**
```json
{
  "error": "string"
}
```

| Status | Condition |
|--------|-----------|
| `200` | Success |
| `400` | Empty or missing `problem` field |
| `500` | `GEMINI_API_KEY` not set, or Gemini API failure |

---

## The 7-Step Research Framework

The system prompt embeds an elite case competition methodology. Gemini processes every problem in strict sequence:

| Step | Name | Output |
|------|------|--------|
| 1 | Strip the Problem to Its Core | One-sentence problem statement + who/why/impact |
| 2 | First Principles Deconstruction | Atomic value question, assumption inventory, conventional wisdom audit, inversion, riskiest bet, from-scratch reconstruction |
| 3 | Business Anatomy | Company identity, problem classification, stakeholder map, constraints, success definition, scope |
| 4 | Derived Research Questions | Specific, falsifiable questions traceable to core problem — not generic frameworks |
| 5 | Perplexity Prompt Generation | Structured search brief: competitive intelligence, customer intelligence, channel/distribution, financials, failure patterns, assumption-breaking evidence, unconventional wins, riskiest bet validation, trend signals, operational benchmarks |
| 6 | Research Angles | 10–12 critical questions tagged [MARKET] [CUSTOMER] [FINANCIAL] [STRATEGIC] [OPERATIONAL] [RISK] |
| 7 | Working Hypotheses | 3 claims: "We believe X because Y. This would be false if Z." |

**Gemini configuration:** temperature `0.3`, max output tokens `8192`.

---

## Frontend Features

- **Dark UI** — `#080808` background, minimal chrome, max-width 720px
- **Loading state** — animated pulsing dots, button + textarea disabled during request
- **Markdown rendering** — marked.js with custom styles per section
- **Perplexity Prompt section** — visually isolated with `#0a0f1a` background and monospace font
- **Copy button** — one click copies only the Perplexity Prompt content; changes to "Copied" for 2 seconds
- **Keyboard shortcut** — `Ctrl+Enter` / `Cmd+Enter` submits
- **Error display** — inline, styled, no page reload

---

## Design System

### Colours

| Token | Value | Usage |
|-------|-------|-------|
| Background | `#080808` | Page background |
| Card | `#111111` | Input and output card surfaces |
| Border | `#1e1e1e` | All borders |
| Text | `#e8e8e8` | Primary body text |
| Accent | `#f0f0f0` | Button fill, section headers |
| Muted | `#555` | Placeholders, secondary labels |
| Prompt BG | `#0a0f1a` | Perplexity Prompt section background |
| Prompt Border | `#1a2a3a` | Perplexity Prompt section border |

### Typography

| Font | Role |
|------|------|
| [Syne](https://fonts.google.com/specimen/Syne) | Headings |
| [DM Sans](https://fonts.google.com/specimen/DM+Sans) | Body, UI labels |
| [Fira Code](https://fonts.google.com/specimen/Fira+Code) | Section labels, Perplexity Prompt content, code blocks |

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | Yes | Google Generative AI API key |

Never commit `.env`. Add it to `.gitignore` if not already present.

---

## Roadmap

### Phase 2 — PDF Upload
Upload a PDF case brief instead of pasting text.

- Frontend: Enable the **Upload PDF** button (currently disabled, labelled *Coming Soon*)
- Backend: New `POST /analyze-pdf` route — extract text with `pdfplumber`, feed into same system prompt
- Dependency: `pdfplumber` (already in `requirements.txt`)

### Potential future additions
- Research history (local storage or SQLite)
- Export to PDF / Word
- Saved templates for recurring problem types
- Rate limiting on `/analyze`
- Response caching for identical inputs

---

## Notes

- Fully stateless — no database, no sessions, no auth
- API key stays server-side — never exposed to frontend
- All logic runs locally; no external services beyond Gemini API
- Debug mode is on by default (`app.run(debug=True)`) — disable for any shared/production use
