# deck_templates.py
# Central registry for deck generation: case types, frameworks, archetypes, 8-section blueprint

CASE_TYPE_LABELS = {
    "strategy": "Strategy / Market Entry",
    "mna_finance": "M&A / Finance",
    "marketing": "Marketing / GTM",
    "social_impact": "Social Impact / NGO",
    "policy_trade_ir": "Policy / Trade / IR",
    "operations": "Operations / Supply Chain",
}

FRAMEWORKS_BY_CASE_TYPE = {
    "strategy": {
        "context": ["PESTLE", "Porter's 5 Forces", "Industry Life Cycle", "Wardley Mapping"],
        "actors": ["Symmetric comparison grid", "Strategic Group Mapping", "Core Competencies (VRIO)"],
        "analysis": ["NPV of strategic options", "Market sizing model", "3-scenario projection", "Sensitivity analysis"],
        "feasibility": ["Capability gap assessment", "RACI matrix", "McKinsey 7-S Framework"],
        "alternative": ["Strategy Diamond", "Ansoff Matrix", "Blue Ocean ERRC", "Implementation roadmap"],
    },
    "mna_finance": {
        "context": ["Industry Life Cycle", "Porter's 5 Forces", "PESTLE"],
        "actors": ["Acquirer vs. Target symmetric comparison", "Stakeholder Power-Interest Grid"],
        "analysis": ["Comparable company analysis", "DCF with synergies", "EPS accretion/dilution", "Football field valuation", "3-scenario projection"],
        "feasibility": ["Financing structure analysis", "Governance assessment", "Integration risk matrix"],
        "alternative": ["Alternative target analysis", "Value creation waterfall", "Post-merger integration plan"],
    },
    "marketing": {
        "context": ["PESTLE", "Consumer trend analysis", "Competitive positioning map"],
        "actors": ["STP (Segmentation-Targeting-Positioning)", "Customer journey map", "Competitor GTM comparison"],
        "analysis": ["Customer LTV model", "CAC by channel", "ROAS benchmarks", "3-scenario AARRR funnel"],
        "feasibility": ["Brand fit assessment", "Execution capability gap", "Channel saturation analysis"],
        "alternative": ["Repositioning strategy", "New segment targeting plan", "GTM redesign roadmap"],
    },
    "social_impact": {
        "context": ["Problem root-cause analysis", "Ecosystem map", "Policy / regulatory landscape"],
        "actors": ["Beneficiary profiles", "Implementer / funder landscape", "Stakeholder influence grid"],
        "analysis": ["Cost-effectiveness analysis", "SROI model", "3-scenario impact projection", "Reach vs. depth tradeoff"],
        "feasibility": ["Implementation risk matrix", "Sustainability / funding analysis", "Capacity assessment"],
        "alternative": ["Theory of change", "Intervention comparison table", "Phased implementation roadmap"],
    },
    "policy_trade_ir": {
        "context": ["Geopolitical context analysis", "CAGE framework (Ghemawat)", "Economic impact baseline"],
        "actors": ["Country / bloc symmetric comparison", "Domestic stakeholder map", "Coalition opportunity mapping"],
        "analysis": ["Welfare economics analysis", "Employment / sector impact model", "3-scenario geopolitical projection"],
        "feasibility": ["Political feasibility assessment", "Diplomatic cost-benefit", "WTO / international law compliance"],
        "alternative": ["Alternative policy instrument", "Coalition-building strategy", "Negotiation roadmap"],
    },
    "operations": {
        "context": ["Value chain analysis", "Industry benchmarking", "Porter's 5 Forces (supply side)"],
        "actors": ["Customer / supplier / ops symmetric comparison", "RACI for current state"],
        "analysis": ["Cost-benefit analysis", "Throughput / bottleneck model", "3-scenario cost projection", "Lean waste analysis"],
        "feasibility": ["Change management assessment", "Capability gap analysis", "CapEx / ROI model"],
        "alternative": ["Future-state value stream map", "Implementation phasing plan", "Risk heat map"],
    },
}

MONEYSHOT_BY_CASE_TYPE = {
    "strategy": "$X bn opportunity / $X bn competitive risk if inaction",
    "mna_finance": "$X bn of value created / destroyed",
    "marketing": "X% LTV improvement / $X CAC reduction vs. current approach",
    "social_impact": "X lives reached at $Y per beneficiary — X× more cost-effective than status quo",
    "policy_trade_ir": "$X bn welfare impact / X jobs affected / X% trade flow change",
    "operations": "$X bn cost savings / X% throughput improvement over 24 months",
}

# 8-section blueprint with slide allocation proportions
SECTION_BLUEPRINT = [
    {
        "id": "exec_summary",
        "roman": "Front",
        "title": "Executive Summary",
        "proportion": 0.03,
        "min_slides": 3,
        "description": "Cover, TOC, and recommendation headline. Lock in the contrarian recommendation with 3 reasons for and against.",
        "slide_archetypes": ["cover", "table_of_contents", "two_column_for_against"],
    },
    {
        "id": "context",
        "roman": "II",
        "title": "Context / Environment",
        "proportion": 0.15,
        "min_slides": 8,
        "description": "Build the disruption thesis. Foreshadow the contrarian alternative in early slides. Industry analysis using PESTLE + Porter's.",
        "slide_archetypes": [
            "section_divider", "two_chart_action_title", "pestle_grid",
            "porters_five_forces", "sub_section_progress", "three_scenario_projection",
            "two_chart_action_title", "two_chart_action_title",
        ],
    },
    {
        "id": "actors",
        "roman": "III",
        "title": "Actors / Stakeholders",
        "proportion": 0.12,
        "min_slides": 6,
        "description": "Symmetric coverage of all key players. Same axes applied to each. Never favour one actor's slide over another.",
        "slide_archetypes": [
            "section_divider", "symmetric_comparison_grid", "two_chart_action_title",
            "stakeholder_power_interest_grid", "two_chart_action_title", "two_chart_action_title",
        ],
    },
    {
        "id": "analysis",
        "roman": "IV",
        "title": "Quantitative Analysis",
        "proportion": 0.20,
        "min_slides": 8,
        "description": "Quantify the case. The moneyshot lives here. Models, scenarios, sensitivity. Build toward the climax number/visual.",
        "slide_archetypes": [
            "section_divider", "two_chart_action_title", "three_scenario_projection",
            "sensitivity_analysis_matrix", "moneyshot", "mece_option_filter",
            "two_chart_action_title", "two_chart_action_title",
        ],
    },
    {
        "id": "feasibility",
        "roman": "V",
        "title": "Feasibility",
        "proportion": 0.12,
        "min_slides": 6,
        "description": "Show the obvious answer cannot work even if quantitatively attractive. Kill the default option with evidence.",
        "slide_archetypes": [
            "section_divider", "mece_option_filter", "two_chart_action_title",
            "risk_heat_map", "two_chart_action_title", "section_closer_recap",
        ],
    },
    {
        "id": "alternative",
        "roman": "VI",
        "title": "Recommended Alternative",
        "proportion": 0.20,
        "min_slides": 8,
        "description": "Name and analyse the contrarian recommendation. Include 2–4 expert validations. Quantify it. Plan implementation.",
        "slide_archetypes": [
            "section_divider", "option_shortlist_comparison", "two_chart_action_title",
            "deep_dive_with_expert_validation", "build_buy_partner",
            "three_scenario_projection", "implementation_roadmap", "section_closer_recap",
        ],
    },
    {
        "id": "conclusion",
        "roman": "VII",
        "title": "Conclusion",
        "proportion": 0.05,
        "min_slides": 3,
        "description": "Single synthesis. No new content. Recap + call to action.",
        "slide_archetypes": ["section_divider", "conclusion_synthesis", "qa_grid"],
    },
    {
        "id": "appendix",
        "roman": "App.",
        "title": "Appendix",
        "proportion": 0.13,
        "min_slides": 5,
        "description": "Deep dives backing every main-deck quantitative claim. Defensive depth. Harvard-style bibliography.",
        "slide_archetypes": ["appendix_toc", "deep_dive", "deep_dive", "deep_dive", "bibliography"],
    },
]

SLIDE_ARCHETYPE_DESCRIPTIONS = {
    "cover": "Title + subtitle + team / date",
    "table_of_contents": "Section list with page references",
    "abbreviations_table": "Key acronyms and terms defined",
    "two_column_for_against": "Recommendation headline — left: reasons FOR, right: reasons AGAINST",
    "section_divider": "Full-page section title with one-sentence framing",
    "sub_section_progress": "Navigation bar showing progress within current section",
    "two_chart_action_title": "Declarative action-title headline + 2 supporting charts/visuals",
    "multi_chart_dense": "3 charts — dense analytical evidence when 3 visuals are justified",
    "pestle_grid": "6-cell PESTLE visual (Political, Economic, Social, Tech, Legal, Environmental)",
    "porters_five_forces": "5-force diagram with intensity scores",
    "symmetric_comparison_grid": "Same axes applied to comparable subjects (actors, options, scenarios)",
    "mece_option_filter": "Option elimination table — MECE criteria as columns, options as rows",
    "three_scenario_projection": "Pessimistic / Realistic / Optimistic — any uncertain quantity",
    "sensitivity_analysis_matrix": "Two-parameter sensitivity table",
    "moneyshot": "Single dramatic number/visual — the deck's analytical climax",
    "risk_heat_map": "Impact vs. likelihood matrix for key risks",
    "stakeholder_power_interest_grid": "Power vs. interest quadrant for stakeholders",
    "option_shortlist_comparison": "Final shortlisted options with scoring across criteria",
    "build_buy_partner": "Three-path framework with recommended path highlighted",
    "deep_dive_with_expert_validation": "Detailed analysis of chosen alternative + 2–4 named expert quotes",
    "implementation_roadmap": "Phased timeline with workstreams, owners, milestones",
    "section_closer_recap": '"Conclusively…" — bullet recap of section\'s key findings',
    "conclusion_synthesis": '"Therefore…" — three-card or Q&A grid final synthesis',
    "qa_grid": "Anticipated Q&A with pre-emptive answers",
    "appendix_toc": "Appendix table of contents with jump links",
    "deep_dive": "Full-page deep-dive backing a specific main-deck claim",
    "bibliography": "Harvard-style reference list",
}

AUDIENCE_OPTIONS = [
    "Competition Judges",
    "Board / C-Suite",
    "CMO",
    "Government / Policy Maker",
    "Foundation / NGO",
    "Investment Committee",
    "Operations Team",
]
