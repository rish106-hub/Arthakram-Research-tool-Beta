import os
import json
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from google import genai
from google.genai import types
from deck_templates import (
    FRAMEWORKS_BY_CASE_TYPE, SECTION_BLUEPRINT, SLIDE_ARCHETYPE_DESCRIPTIONS,
    MONEYSHOT_BY_CASE_TYPE, CASE_TYPE_LABELS,
)

load_dotenv()

app = Flask(__name__)

SYSTEM_PROMPT = """You are an elite case competition research strategist. Your job is not to describe an industry. Your job is to find what is actually true about a specific problem, from the ground up, and produce research tools that get a team to insight faster than any other team in the room.

Process every problem statement in strict sequence. Do not skip steps. Each step informs the next.

Return your entire response in clean markdown. Use the exact section headers specified in the output format.

---

**STEP 1: STRIP THE PROBLEM TO ITS CORE**

Read the problem statement and remove all noise. Rewrite it in one sentence that captures only what is actually being asked. No jargon, no filler, no category labels.

Then answer:
- Who has this problem?
- Why do they have it right now and not before?
- What changes if it gets solved?
- What stays broken if it does not?

This single sentence becomes the anchor for everything that follows. If a research question cannot be traced back to it, that research question gets cut.

---

**STEP 2: FIRST PRINCIPLES DECONSTRUCTION**

Before touching any research, break the problem down to its irreducible truths. You are looking for what is actually true, not what the industry assumes to be true.

### Atomic Value Question

What is the single most fundamental job this product or service is hired to do? Go beneath the category. Not *people buy coffee* but "people buy a socially acceptable reason to sit somewhere quiet for an hour." What is the real human need underneath the surface behaviour? Why has this need not been fully solved yet?

### Assumption Inventory

List every assumption embedded in the problem statement, both stated and implied. For each one ask three questions: Is there evidence this is true? What would the strategy look like if this were false? Has anyone ever succeeded by ignoring this assumption?

### Conventional Wisdom Audit

Write down what everyone in this industry believes. Then challenge each belief directly. Where does the standard playbook for this problem type break down? What does the industry assume about customers that customers do not actually demonstrate through their behaviour?

Inversion Describe in detail how you would guarantee this business fails. What is the fastest path to irrelevance? What does the worst version of this GTM or strategy look like and why does it fail? Work backwards from that failure. What does it reveal about what must be protected or avoided?

### The Riskiest Bet

Identify the single most dangerous assumption in this problem. The one that, if false, collapses the entire strategy. State it clearly as a testable claim. Everything in the research phase must either validate or invalidate this bet first.

From-Scratch Reconstruction If you were building this business today with no inherited conventions, no existing category playbook, and full knowledge of the problem — what would it look like? How does that differ from the approach implied in the problem statement? Why does that gap exist — is it because the current approach is optimal, or because it is inherited?

---

**STEP 3: BUSINESS ANATOMY**

Now that assumptions are on the table, map the business precisely.

Identity Company type, industry sub-vertical stated at maximum specificity, business model, revenue model, geography and city-tier, scale signals if present.

### Problem Classification

Identify the primary problem type and any secondary ones: market entry, GTM design, GTM revamp, growth strategy, turnaround, product-market fit, pricing strategy, channel optimization, brand repositioning, competitive response, operational fix, retention or churn, unit economics improvement.

### Stakeholder Map

Who commissioned this problem. Who the business actually serves. Intermediaries and their incentives. Direct and indirect competitors. Regulators if relevant.

Constraints Explicit constraints from the problem. Implicit constraints inferred from context — budget signals, timeline pressure, risk appetite. What is non-negotiable versus what is a variable.

### Success Definition

What does a win look like in 6, 12, and 24 months. What metrics would prove the strategy worked. What are the judges likely evaluating this solution on and what separates a top answer from an average one.

Scope What this problem is asking. What it is not asking. What looks relevant but should be deprioritized to avoid diluting the answer.

---

**STEP 4: DERIVED RESEARCH QUESTIONS**

Based on Steps 1, 2, and 3 only — before any external research — write the questions that actually need to be answered. These are derived from first principles, not from standard research frameworks.

Each question must:
- Trace directly back to the core problem statement from Step 1
- Challenge or validate at least one assumption from Step 2
- Be specific enough to have a findable, falsifiable answer
- Represent something a competitor team is likely to miss

Do not write generic research questions. *What is the market size* is not a question. "What is the average CAC for a specialty cafe acquiring urban professionals through Instagram in tier-2 Indian cities in 2024" is a question.

---

**STEP 5: PERPLEXITY PROMPT GENERATION**

Now construct the Perplexity prompt. This prompt exists to answer the questions from Step 4. Nothing else.

### Opening Line

Start with the exact business context and problem. Never start with the industry or the category. Structure: "I am advising [specific business type] facing [specific problem] in [specific market context] and I need..."

### Competitive Intelligence

Direct competitors at the exact niche level — not industry leaders, not adjacent categories. Their GTM approaches, pricing, positioning, and channel mix. Recent moves, failures, and pivots. Where the competitive map has gaps. Do not request general competitive landscapes.

### Customer Intelligence

Specific customer segments relevant to this problem. Their actual decision-making process — not what they say, what they do. Triggers and barriers at the point of purchase. Where they currently get this need met and why that solution is incomplete. Revealed preference data, not stated preference.

Channel and Distribution Intelligence Which channels work for this exact sub-niche. CAC benchmarks by channel for this business type and geography. Saturation levels and emerging alternatives. Intermediary economics — margins, incentive structures, conflicts of interest.

### Financial Benchmarks

Unit economics for similar businesses at similar stages: CAC, LTV, payback period, gross margin, revenue per customer. If the business model is specific, request benchmarks for that model specifically. Flag when India-specific data differs from global benchmarks.

### Failure Patterns

Why similar businesses or GTM approaches have failed in this niche specifically. Common mistakes at this exact stage and problem type. What the graveyard of failed attempts in this category looks like and what the failure mode was each time.

Assumption-Breaking Evidence Cases where conventional wisdom about this problem type or industry was proven wrong. What actually happened. Why the standard approach failed. What the winning team understood that others did not.

### Unconventional Wins

Businesses that succeeded in a similar niche by doing the opposite of what the industry expected. What the underlying insight was. Whether that insight is transferable to this problem.

### Riskiest Bet Validation

Find data that directly validates or invalidates the single most dangerous assumption identified in Step 2. This is the most important research dimension. Return evidence, not opinion.

Regulatory and Compliance Context Regulations specific to this sub-niche and geography. Licensing, compliance, certifications. Recent regulatory changes affecting strategy. Cut this dimension if not relevant.

### Trend Signals

Trends specific to this sub-niche only. Consumer behaviour shifts affecting this exact customer segment. Technology changes relevant to this problem. Economic context affecting this geography and demographic. No broad industry trends unless they directly connect to the core problem statement.

### Operational Benchmarks

How similar businesses are structured operationally. Key operating metrics and benchmarks. Where operations typically break at this scale or stage.

### Prompt Formatting Rules

Use *in the context of [specific situation]* framing throughout. Request specific numbers, benchmarks, named examples — not summaries or overviews. When geography is India, explicitly request India-specific data and flag when only global data exists. Request data from the last 12 to 18 months. Ask for failure cases alongside every success case. Do not request TAM, SAM, SOM, or broad market size figures unless the problem explicitly requires market sizing work.

---

**STEP 6: RESEARCH ANGLES**

Produce 10 to 12 specific questions this team must answer to build a top-tier case response. These come from the first principles work in Step 2, not from standard frameworks.

Order them from most to least critical. Each must be specific, falsifiable, and represent a blindspot an average team misses.

Tag each one: [MARKET] — competitive and market landscape [CUSTOMER] — behaviour, psychology, segmentation [FINANCIAL] — unit economics and benchmarks [STRATEGIC] — positioning, differentiation, defensibility [OPERATIONAL] — execution and implementation [RISK] — what breaks this strategy and how to mitigate

---

**STEP 7: WORKING HYPOTHESES**

Before the team begins research, write 3 preliminary hypotheses about what the answer might look like. These are built from the first principles work in Step 2 and the business anatomy in Step 3. They are not conclusions. They are the team's best guesses before evidence arrives — the claims they are trying to prove or kill through research.

State each hypothesis as: "We believe [claim] because [first principles reasoning]. This would be false if [condition]."

---

**OUTPUT FORMAT** — return in this exact structure using markdown:

## Core Problem

## First Principles Findings

## Business Anatomy

## Derived Research Questions

## Perplexity Prompt

## Research Angles

## Working Hypotheses"""


DECK_GENERATION_PROMPT = """You are a case competition deck architect trained on winning decks from top international case competitions.

Given the research brief and case parameters below, output the deck's strategic content as JSON.

You must identify:
1. RECOMMENDATION — what this deck recommends (specific, not generic)
2. CONTRARIAN ALTERNATIVE — the less-obvious answer (not the default implied by the case prompt)
3. FORESHADOWING SEED — one sentence to plant in Context section (30+ slides before naming the alternative)
4. MONEYSHOT — the single dramatic number/visual that is the deck's analytical climax
5. ACTION TITLES for key slides in each section (declarative sentences with numbers)
6. FRAMEWORKS EXPLANATION — which frameworks to use and why, layered for this specific case

RULES:
- All action titles must be declarative findings, not topic labels
  BAD: "Customer Demographics" | GOOD: "Urban Gen Z spends 4.3x more per visit than suburban customers"
- The contrarian alternative must differ meaningfully from the default answer implied by the case prompt
- frameworks_explanation must name specific frameworks and explain the layering logic for this specific case
- Include numbers wherever possible in titles and findings"""


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set in environment")
    return genai.Client(api_key=api_key)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or not data.get("problem", "").strip():
        return jsonify({"error": "Problem statement is required."}), 400

    problem = data["problem"].strip()
    full_prompt = f"{SYSTEM_PROMPT}\n\n---\n\nPROBLEM STATEMENT: {problem}"

    try:
        client = get_gemini_client()
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=8192,
            ),
        )
        return jsonify({"result": response.text})
    except Exception as e:
        return jsonify({"error": f"Gemini API error: {str(e)}"}), 500


@app.route("/prepare-deck", methods=["POST"])
def prepare_deck():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body required."}), 400

    research_brief = data.get("research_brief", "").strip()
    case_type = data.get("case_type", "strategy")
    audience = data.get("audience", "Competition Judges")
    deck_length = max(20, min(200, int(data.get("deck_length", 100))))

    if not research_brief:
        return jsonify({"error": "Research brief is required."}), 400
    if case_type not in FRAMEWORKS_BY_CASE_TYPE:
        return jsonify({"error": f"Invalid case type. Must be one of: {', '.join(FRAMEWORKS_BY_CASE_TYPE.keys())}"}), 400

    frameworks = FRAMEWORKS_BY_CASE_TYPE[case_type]
    moneyshot_template = MONEYSHOT_BY_CASE_TYPE[case_type]
    case_label = CASE_TYPE_LABELS[case_type]

    full_prompt = f"""{DECK_GENERATION_PROMPT}

---
CASE TYPE: {case_label}
AUDIENCE: {audience}
DECK LENGTH: {deck_length} slides
MONEYSHOT FORMAT FOR THIS CASE TYPE: {moneyshot_template}

RESEARCH BRIEF:
{research_brief}

Return ONLY this JSON structure (no markdown, no explanation, no code fences):
{{
  "recommendation": "concise recommendation statement for this specific case",
  "contrarian_alternative": "the less-obvious alternative this deck recommends over the default answer",
  "foreshadowing_seed": "one-sentence insight to plant in Context section as a subtle seed for the alternative",
  "moneyshot": "the specific dramatic number/claim adapted from the research for this case",
  "exec_summary_headline": "recommendation action title — declarative sentence with numbers",
  "exec_summary_for_reasons": ["specific reason 1", "specific reason 2", "specific reason 3"],
  "exec_summary_against_reasons": ["counter-argument 1", "counter-argument 2", "counter-argument 3"],
  "context_key_finding": "action title for main context slide — include a number",
  "actors_key_finding": "action title for main actors slide — include a number",
  "analysis_key_finding": "action title for main analysis/moneyshot slide — include a number",
  "feasibility_key_finding": "action title for feasibility slide showing why obvious answer fails",
  "alternative_key_finding": "action title for recommended alternative slide — include a number",
  "conclusion_synthesis": "final synthesis statement for conclusion slide",
  "frameworks_explanation": "350-word explanation of which frameworks to use, how to layer them, and why for this specific case"
}}"""

    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                temperature=0.4,
                max_output_tokens=4096,
                response_mime_type="application/json",
            ),
        )
        text = response.text.strip()
        # Strip markdown fences if present
        if text.startswith("```json"):
            text = text[7:]  # Remove ```json
        if text.startswith("```"):
            text = text[3:]  # Remove ```
        if text.endswith("```"):
            text = text[:-3]  # Remove closing ```
        text = text.strip()
        gemini_data = json.loads(text)
    except ValueError as e:
        return jsonify({"error": str(e)}), 500
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Failed to parse AI response as JSON. Please try again. ({str(e)})"}), 500
    except Exception as e:
        return jsonify({"error": f"Gemini API error: {str(e)}"}), 500

    # --- Build deterministic deck structure ---
    slide_counts = []
    for section in SECTION_BLUEPRINT:
        count = max(section["min_slides"], round(deck_length * section["proportion"]))
        slide_counts.append(count)

    # Adjust total to match requested deck_length
    total = sum(slide_counts)
    diff = deck_length - total
    if diff != 0:
        slide_counts[3] = max(SECTION_BLUEPRINT[3]["min_slides"], slide_counts[3] + diff)

    fw_key_map = {
        "exec_summary": None, "context": "context", "actors": "actors",
        "analysis": "analysis", "feasibility": "feasibility",
        "alternative": "alternative", "conclusion": None, "appendix": None,
    }

    key_finding_map = {
        "exec_summary": gemini_data.get("exec_summary_headline", "Strategic recommendation"),
        "context": gemini_data.get("context_key_finding", "Industry context demands strategic urgency"),
        "actors": gemini_data.get("actors_key_finding", "Key actors face divergent incentives"),
        "analysis": gemini_data.get("analysis_key_finding", "Quantitative gap reveals strategic imperative"),
        "feasibility": gemini_data.get("feasibility_key_finding", "Conventional approach fails feasibility test"),
        "alternative": gemini_data.get("alternative_key_finding", "Contrarian alternative delivers superior outcomes"),
        "conclusion": gemini_data.get("conclusion_synthesis", "Recommended alternative uniquely solves the core problem"),
        "appendix": "Supporting analysis and references",
    }

    slide_number = 1
    sections = []

    for i, section_def in enumerate(SECTION_BLUEPRINT):
        section_id = section_def["id"]
        section_slide_count = slide_counts[i]
        fw_key = fw_key_map.get(section_id)
        section_frameworks = frameworks.get(fw_key, []) if fw_key else []
        archetypes = section_def["slide_archetypes"]
        slides = []

        for archetype in archetypes:
            if len(slides) >= section_slide_count:
                break

            slide = {
                "slide_number": slide_number,
                "archetype": archetype,
                "archetype_description": SLIDE_ARCHETYPE_DESCRIPTIONS.get(archetype, ""),
            }

            if archetype == "cover":
                slide["title"] = "Case Competition Deck"
                slide["subtitle"] = gemini_data.get("recommendation", "Strategic Recommendation")
            elif archetype == "table_of_contents":
                slide["title"] = "Table of Contents"
            elif archetype == "two_column_for_against":
                slide["title"] = gemini_data.get("exec_summary_headline", "Recommendation")
                slide["for_reasons"] = gemini_data.get("exec_summary_for_reasons", ["Reason 1", "Reason 2", "Reason 3"])
                slide["against_reasons"] = gemini_data.get("exec_summary_against_reasons", ["Counter 1", "Counter 2", "Counter 3"])
            elif archetype == "section_divider":
                slide["title"] = section_def["title"]
                slide["framing"] = section_def["description"]
            elif archetype == "moneyshot":
                slide["title"] = gemini_data.get("moneyshot", moneyshot_template)
                slide["note"] = "Deck climax — single dramatic number/visual"
            elif archetype == "conclusion_synthesis":
                slide["title"] = gemini_data.get("conclusion_synthesis", "Therefore…")
            elif archetype in ("two_chart_action_title", "multi_chart_dense"):
                kf = key_finding_map.get(section_id, section_def["title"])
                slide["title"] = kf
                slide["chart_1"] = section_frameworks[0] if section_frameworks else "Primary analysis"
                slide["chart_2"] = section_frameworks[1] if len(section_frameworks) > 1 else "Secondary analysis"
            elif archetype == "three_scenario_projection":
                slide["title"] = f"Three scenarios: {key_finding_map.get(section_id, section_def['title'])}"
                slide["pessimistic"] = "Worst case — [populate with specific figures]"
                slide["realistic"] = "Base case — [populate with specific figures]"
                slide["optimistic"] = "Best case — [populate with specific figures]"
            elif archetype == "implementation_roadmap":
                slide["title"] = "Implementation roadmap — phases, owners, milestones"
            elif archetype == "deep_dive_with_expert_validation":
                alt = gemini_data.get("contrarian_alternative", "recommended approach")
                slide["title"] = f"Expert validation: {alt[:80]}"
            else:
                slide["title"] = SLIDE_ARCHETYPE_DESCRIPTIONS.get(archetype, archetype.replace("_", " ").title())

            slides.append(slide)
            slide_number += 1

        # Fill remaining with two_chart_action_title
        while len(slides) < section_slide_count:
            kf = key_finding_map.get(section_id, section_def["title"])
            slides.append({
                "slide_number": slide_number,
                "archetype": "two_chart_action_title",
                "archetype_description": SLIDE_ARCHETYPE_DESCRIPTIONS.get("two_chart_action_title", ""),
                "title": f"{kf} — supporting analysis",
                "chart_1": section_frameworks[0] if section_frameworks else "Supporting data",
                "chart_2": section_frameworks[1] if len(section_frameworks) > 1 else "Supporting data",
            })
            slide_number += 1

        sections.append({
            "id": section_id,
            "roman": section_def["roman"],
            "title": section_def["title"],
            "slide_count": len(slides),
            "description": section_def["description"],
            "frameworks": section_frameworks,
            "slides": slides,
        })

    deck_structure = {
        "case_type": case_type,
        "case_type_label": case_label,
        "audience": audience,
        "total_slides": slide_number - 1,
        "recommendation": gemini_data.get("recommendation", ""),
        "contrarian_alternative": gemini_data.get("contrarian_alternative", ""),
        "foreshadowing_seed": gemini_data.get("foreshadowing_seed", ""),
        "moneyshot": gemini_data.get("moneyshot", ""),
        "sections": sections,
        "recommended_frameworks": frameworks,
        "frameworks_explanation": gemini_data.get("frameworks_explanation", ""),
    }

    return jsonify({"deck_structure": deck_structure})


@app.route("/get-frameworks", methods=["POST"])
def get_frameworks():
    data = request.get_json()
    case_type = (data.get("case_type", "strategy") if data else "strategy")

    if case_type not in FRAMEWORKS_BY_CASE_TYPE:
        return jsonify({"error": f"Invalid case type. Valid options: {', '.join(FRAMEWORKS_BY_CASE_TYPE.keys())}"}), 400

    return jsonify({
        "case_type": case_type,
        "case_type_label": CASE_TYPE_LABELS[case_type],
        "frameworks": FRAMEWORKS_BY_CASE_TYPE[case_type],
        "moneyshot_template": MONEYSHOT_BY_CASE_TYPE[case_type],
    })


if __name__ == "__main__":
    # macOS Monterey+ uses port 5000 for AirPlay Receiver — default to 5001 if not set
    port = int(os.getenv("FLASK_RUN_PORT", 5001))
    app.run(debug=True, port=port)
