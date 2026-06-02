# Changelog

All notable changes to **Arthakram Research Tool** will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Planned
- PDF upload support (Phase 2) via `pdfplumber`
- Research history via local storage or SQLite
- Export to PDF / Word
- Saved templates for recurring problem types
- Rate limiting on `/analyze` endpoint
- Response caching for identical inputs

---

## [0.2.0] - 2026-06-02

### Added
- `CONTRIBUTING.md` — full contribution guide covering branching strategy, commit convention, PR process, and code style
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
- `CHANGELOG.md` — this file
- `.github/PULL_REQUEST_TEMPLATE.md` — structured PR form with type, label, problem, solution, test steps, breaking changes, and pre-submission checklist
- `.github/ISSUE_TEMPLATE/bug_report.yml` — YAML-based bug report form with structured fields
- `.github/ISSUE_TEMPLATE/feature_request.yml` — YAML-based feature request form
- `.github/ISSUE_TEMPLATE/config.yml` — issue template chooser with contact links
- Professional-grade README overhaul with badges, architecture diagram, full API reference, design system docs, roadmap, and contribution quick-start

### Changed
- README updated to reflect Gemini 2.5 Flash as the AI layer

---

## [0.1.0] - 2026-06-01

### Added
- Initial build: Flask backend + Gemini 2.5 Flash integration
- `app.py` — Flask routes (`GET /`, `POST /analyze`), Gemini API call, 7-step system prompt
- `index.html` — single-page frontend with dark UI, markdown rendering via marked.js, copy-to-clipboard
- `requirements.txt` — Python dependencies
- `README.md` — initial documentation

### System Prompt Framework (v1)
1. Strip the Problem to Its Core
2. First Principles Deconstruction
3. Business Anatomy
4. Derived Research Questions
5. Perplexity Prompt Generation
6. Research Angles (10–12 questions tagged by type)
7. Working Hypotheses (3 testable claims with falsifiability conditions)

---

*Changelog format: `[version] — YYYY-MM-DD`, entries grouped as Added / Changed / Fixed / Removed / Security*
