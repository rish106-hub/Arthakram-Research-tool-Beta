<div align="center">

# ⚡ Arthakram Research Tool

**First-principles research briefs for case competitions — powered by Gemini 2.5 Flash**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4?style=flat-square&logo=google&logoColor=white)](https://aistudio.google.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa?style=flat-square)](CODE_OF_CONDUCT.md)

[**🚀 Try It**](#setup) · [**🐛 Report a Bug**](../../issues/new?template=bug_report.yml) · [**✨ Request a Feature**](../../issues/new?template=feature_request.yml) · [**📖 Contributing Guide**](CONTRIBUTING.md)

</div>

---

## 📋 What Is This?

Case competition teams waste time on broad, generic research. **Arthakram** forces specificity from the start.

Paste a problem statement → the tool runs it through a **7-step first-principles framework** powered by Gemini 2.5 Flash → returns a structured research brief with:

| Output | Description |
|--------|-------------|
| **Core Problem** | Stripped to one sentence with who/why/impact |
| **First Principles Findings** | Assumption inventory, conventional wisdom audit, riskiest bet |
| **Business Anatomy** | Stakeholder map, constraints, success definition, scope |
| **Derived Research Questions** | Specific, falsifiable questions a competitor team will miss |
| **Perplexity Prompt** | Ready-to-copy research brief for niche-level search |
| **Research Angles** | 10–12 questions tagged [MARKET] [CUSTOMER] [FINANCIAL] [STRATEGIC] [OPERATIONAL] [RISK] |
| **Working Hypotheses** | 3 testable claims: "We believe X because Y. This would be false if Z." |

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| AI | Google Gemini 2.5 Flash (`gemini-2.5-flash`) |
| Frontend | Plain HTML, CSS, Vanilla JavaScript |
| Markdown rendering | marked.js (CDN) |
| Fonts | Syne, DM Sans, Fira Code (Google Fonts CDN) |
| PDF parsing (Phase 2) | pdfplumber |

No database. No auth. No frontend framework. Deliberately minimal.

---

## 📁 Project Structure

```
Arthakram-Research-tool-Beta/
├── app.py                    # Flask backend — routes, Gemini integration, system prompt
├── index.html                # Single-page frontend — UI, markdown rendering, copy logic
├── requirements.txt          # Python dependencies
├── .env                      # API key (not committed — see .gitignore)
├── README.md
├── CONTRIBUTING.md           # Contribution guide
├── CODE_OF_CONDUCT.md        # Community standards
├── CHANGELOG.md              # Version history
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
        ├── bug_report.yml
        ├── feature_request.yml
        └── config.yml
```

---

## 🔨 Setup

### Prerequisites

- Python 3.8+
- A free Gemini API key from [aistudio.google.com](https://aistudio.google.com)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/rish106-hub/Arthakram-Research-tool-Beta.git
cd Arthakram-Research-tool-Beta

# 2. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 5. Start the server
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

> **Security:** Never commit `.env`. It is already in `.gitignore` (add it if not present). The API key stays server-side and is never exposed to the frontend.

---

## 📱 Usage

1. Paste a case competition problem statement into the textarea
2. Click **Analyse** (or press `Ctrl`+`Enter` / `Cmd`+`Enter`)
3. Wait ~15–30 seconds for Gemini to process
4. Read through the structured research brief
5. Click **Copy Prompt** on the Perplexity Prompt section
6. Paste into [Perplexity](https://perplexity.ai) and run

---

## 🌐 API Reference

### `GET /`

Serves `index.html`.

### `POST /analyze`

Accepts a problem statement, returns a structured markdown research brief.

**Request body:**
```json
{ "problem": "string (required)" }
```

**Success response:**
```json
{ "result": "string (markdown)" }
```

**Error response:**
```json
{ "error": "string" }
```

| Status | Condition |
|--------|-----------|
| `200` | Success |
| `400` | Empty or missing `problem` field |
| `500` | `GEMINI_API_KEY` not set, or Gemini API failure |

---

## 🧠 The 7-Step Research Framework

The system prompt embeds an elite case competition methodology. Gemini processes every problem in strict sequence:

| Step | Name | Output |
|------|------|--------|
| 1 | Strip the Problem to Its Core | One-sentence problem + who/why/impact |
| 2 | First Principles Deconstruction | Atomic value question, assumption inventory, conventional wisdom audit, inversion, riskiest bet |
| 3 | Business Anatomy | Company identity, stakeholder map, constraints, success definition, scope |
| 4 | Derived Research Questions | Specific, falsifiable questions traceable to core problem |
| 5 | Perplexity Prompt Generation | Structured search brief across 10 research dimensions |
| 6 | Research Angles | 10–12 critical questions tagged by type |
| 7 | Working Hypotheses | 3 claims: "We believe X because Y. This would be false if Z." |

Gemini configuration: `temperature: 0.3`, `max_output_tokens: 8192`

---

## 🎨 Design System

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
| Syne | Headings |
| DM Sans | Body, UI labels |
| Fira Code | Section labels, Perplexity Prompt content, code blocks |

---

## 🗺️ Roadmap

### Phase 2 — PDF Upload *(in progress)*
- Upload a PDF case brief instead of pasting text
- `POST /analyze-pdf` route extracting text with `pdfplumber`
- Frontend: enable the disabled "Upload PDF" button

### Potential future additions
- Research history (local storage or SQLite)
- Export to PDF / Word
- Saved templates for recurring problem types
- Rate limiting on `/analyze`
- Response caching for identical inputs

Track progress in [CHANGELOG.md](CHANGELOG.md) and [open issues](../../issues).

---

## 🤝 Contributing

We welcome contributions of all sizes — bug fixes, new features, documentation improvements, and UX enhancements.

**Quick start:**

```bash
# Fork the repo, then:
git clone https://github.com/YOUR_USERNAME/Arthakram-Research-tool-Beta.git
git checkout -b feat/your-feature-name
# ... make your changes ...
git push origin feat/your-feature-name
# Open a PR using the PR template
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide covering:
- Branching strategy and naming conventions
- Commit message convention (Conventional Commits)
- PR process and review criteria
- Code style guidelines for Python and HTML/JS
- Conflict resolution workflow

> All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📄 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | Yes | Google Generative AI API key |

---

## ⚠️ Important Notes

- **Fully stateless** — no database, no sessions, no auth
- **API key stays server-side** — never exposed to frontend
- **All logic runs locally** — no external services beyond Gemini API
- **Debug mode is on by default** (`app.run(debug=True)`) — disable for any shared/production use

---

## 📃 License

This project is open source under the [MIT License](LICENSE).

---

<div align="center">

Built with ♥️ by [rish106-hub](https://github.com/rish106-hub) and contributors.

**[Star ⭐ this repo](https://github.com/rish106-hub/Arthakram-Research-tool-Beta) if it helped you win a case comp.**

</div>
