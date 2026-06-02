# Contributing to Arthakram Research Tool

> First off — thank you for considering contributing. Every bug fix, feature idea, and documentation improvement makes Arthakram better for everyone building competitive research workflows.

---

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Who Can Contribute](#who-can-contribute)
3. [Project Overview](#project-overview)
4. [How to Contribute](#how-to-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Features](#suggesting-features)
   - [Submitting Code Changes](#submitting-code-changes)
5. [Development Setup](#development-setup)
6. [Branching Strategy](#branching-strategy)
7. [Commit Message Convention](#commit-message-convention)
8. [Pull Request Process](#pull-request-process)
9. [Code Style Guidelines](#code-style-guidelines)
10. [Labels Reference](#labels-reference)
11. [Getting Help](#getting-help)

---

## 🤝 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold it. Unacceptable behaviour can be reported to the maintainers via GitHub Issues or by tagging `@rish106-hub`.

---

## 👥 Who Can Contribute

Anyone is welcome. You don't need to be a professional developer. Here are some ways to contribute regardless of skill level:

- **Beginners** — Fix typos, improve documentation, improve comments in code
- **Intermediate** — Fix labelled `bug` issues, improve frontend UX
- **Advanced** — Implement new features, improve the Gemini prompt, add new research frameworks

---

## 🧠 Project Overview

Arthakram is a Flask + Gemini 2.5 Flash web app that takes a case competition problem statement and returns a structured, first-principles research brief. The stack is deliberately minimal:

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| AI | Google Gemini 2.5 Flash |
| Frontend | Plain HTML/CSS/Vanilla JS |
| Fonts | Syne, DM Sans, Fira Code |

There is no database, no auth, and no framework on the frontend. Keep it that way unless there's a strong reason to change it.

---

## 🔧 How to Contribute

### Reporting Bugs

1. Search [existing issues](../../issues) to avoid duplicates.
2. Open a new issue using the **🐛 Bug Report** template.
3. Fill in every field — vague reports will be closed.

### Suggesting Features

1. Search [existing issues](../../issues) to avoid duplicates.
2. Open a new issue using the **✨ Feature Request** template.
3. Explain the problem your feature solves, not just the solution.
4. Keep scope tight — this is a focused research tool, not a general-purpose app.

### Submitting Code Changes

1. Fork the repository.
2. Create a branch following the [branching strategy](#branching-strategy) below.
3. Make your changes.
4. Test locally (`python app.py`).
5. Open a PR using the [PR template](/.github/PULL_REQUEST_TEMPLATE.md).
6. Wait for review.

---

## 💻 Development Setup

```bash
# 1. Fork and clone the repo
git clone https://github.com/YOUR_USERNAME/Arthakram-Research-tool-Beta.git
cd Arthakram-Research-tool-Beta

# 2. Create a virtual environment (strongly recommended)
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your .env file (never commit this)
echo "GEMINI_API_KEY=your_key_here" > .env

# 5. Run the development server
python app.py

# 6. Open in browser
# http://localhost:5000
```

**Important:** Get a free Gemini API key at [aistudio.google.com](https://aistudio.google.com). The free tier is sufficient for development.

---

## 🌳 Branching Strategy

Always branch off `main`. Use the following naming format:

| Branch type | Format | Example |
|-------------|--------|---------|
| Bug fix | `fix/<short-description>` | `fix/copy-button-crash` |
| New feature | `feat/<short-description>` | `feat/pdf-upload` |
| Enhancement | `enhance/<short-description>` | `enhance/research-prompt` |
| Documentation | `docs/<short-description>` | `docs/setup-instructions` |
| Refactor | `refactor/<short-description>` | `refactor/route-structure` |
| Chore / Meta | `chore/<short-description>` | `chore/update-dependencies` |

**Never commit directly to `main`.** All changes go through a PR.

### Keeping your branch up-to-date

Before opening a PR, always rebase or merge with the latest `main` to avoid conflicts:

```bash
git fetch origin
git rebase origin/main
# or
git merge origin/main
```

If you have a conflict:
1. Resolve each conflicting file manually.
2. Stage resolved files: `git add <file>`
3. Continue: `git rebase --continue` (or `git commit` if merging)
4. Force-push your branch: `git push --force-with-lease origin your-branch`

---

## 📝 Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/) for clean, parseable history.

**Format:** `<type>(<scope>): <short description>`

| Type | When to use |
|------|------------|
| `feat` | New feature added |
| `fix` | Bug fix |
| `enhance` | Improvement to existing behaviour |
| `docs` | Documentation only |
| `style` | Formatting, whitespace (no logic change) |
| `refactor` | Code restructuring (no behaviour change) |
| `perf` | Performance improvement |
| `chore` | Tooling, dependencies, CI |
| `revert` | Reverts a previous commit |

**Examples:**

```
feat(backend): add PDF upload route using pdfplumber
fix(frontend): correct copy button clipboard logic on Safari
docs(readme): update setup instructions for Windows
enhance(prompt): tighten first-principles step 2 output
```

**Rules:**
- Use lowercase
- Keep under 72 characters
- Use the imperative mood ("add" not "added" or "adds")
- Do not end with a period

---

## 🔄 Pull Request Process

1. **Ensure your branch is up-to-date** with `main` before opening the PR.
2. **Fill in the PR template fully.** Incomplete PRs may be closed.
3. **One concern per PR.** Don't bundle unrelated changes.
4. **Mark your PR with the correct label** (see [Labels Reference](#labels-reference)).
5. **Respond to review comments promptly.** PRs with no activity for 14 days may be closed.
6. **Do not force-push after review has started** unless asked to.
7. **Maintainer merges.** Contributors do not merge their own PRs.

### PR Review Criteria

Your PR will be reviewed for:
- Does it solve the stated problem?
- Is the code clear and well-commented?
- Does it follow the code style guidelines?
- No credentials, debug statements, or unrelated changes?
- Is the README updated if needed?

---

## 🖌️ Code Style Guidelines

### Python (`app.py`)

- Follow [PEP 8](https://pep8.org/)
- Use descriptive variable names
- Add a docstring to any new function
- No hardcoded API keys, tokens, or secrets
- No `print()` statements for debugging — use Flask's logger
- Keep routes focused; move logic into helper functions if needed

### HTML/CSS/JS (`index.html`)

- Inline styles are acceptable but prefer the existing `<style>` block
- Keep the design system consistent (colours, fonts — see README)
- Vanilla JS only — no frameworks, no npm
- Handle loading and error states explicitly
- No `console.log()` calls in submitted code

### General

- Delete commented-out code before submitting
- Keep lines under 100 characters where possible
- Prefer explicit over implicit

---

## 🏷️ Labels Reference

| Label | Meaning |
|-------|---------|
| `bug` | Something is broken |
| `enhancement` | Improves existing functionality |
| `feature` | Adds new functionality |
| `documentation` | Docs-only change |
| `ui/ux` | Frontend / design change |
| `refactor` | Code restructuring |
| `performance` | Speed or efficiency improvement |
| `security` | Security-related change |
| `good first issue` | Good for newcomers |
| `help wanted` | Maintainer needs help with this |
| `needs-triage` | Newly opened, not yet reviewed |
| `wontfix` | This will not be worked on |
| `duplicate` | Already reported/tracked elsewhere |

---

## 🙋 Getting Help

- Open a [GitHub Issue](../../issues/new/choose) with your question
- Tag `@rish106-hub` in an issue comment for maintainer attention
- For urgent concerns, use the Discussions tab (if enabled)

---

## 🌟 Recognition

All contributors will be listed in the project's contributor graph and acknowledged in release notes. Significant contributions may be highlighted in the README.

---

*This CONTRIBUTING guide is inspired by open-source best practices from projects like VS Code, Flask, and Google Summer of Code organisations.*
