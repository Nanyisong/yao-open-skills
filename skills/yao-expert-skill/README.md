# Yao Expert Skill

`yao-expert-skill` turns any domain, industry, technology, market, role, product direction, or fuzzy idea into an expert learning packet.

It is designed for situations where a user does not just want a short explanation. The goal is to build enough structure, vocabulary, evidence, examples, and self-check questions for a newcomer to start thinking like an informed practitioner.

## What It Produces

- A source-backed expert learning report
- A reader-facing opening summary
- Boundary, classification, value-chain, lifecycle, competition, policy, risk, and opportunity analysis
- `50-100` keyword teaching cards
- Representative people, companies, institutions, products, cases, and scenarios as learning anchors
- A practical expert learning tutorial
- Ten Feynman self-test questions with reference answers
- Four export formats: `Markdown`, `Word`, `PDF`, and `HTML`

## How It Works

The skill follows a structure-first learning path:

1. Normalize the topic, region, purpose, audience, time horizon, depth, and exclusions.
2. Define the boundary before collecting facts, so adjacent concepts do not get mixed together.
3. Build the domain map through classifications, value chains, actors, demand, supply, competition, lifecycle, policy, technology, and capital signals.
4. Separate `fact`, `inference`, `hypothesis`, and `unknown`.
5. Convert key terms into teaching cards with plain-language explanations, bottom logic, examples, applications, metrics, misconceptions, and evidence.
6. Turn the report into a tutorial path and Feynman self-test.
7. Export and validate Markdown, DOCX, PDF, and HTML.

## Key Design Choices

- Reports begin with `导读摘要`, so readers get the purpose, highlights, reading path, and logic before entering the formal report.
- Each major module starts with natural prose before tables or matrices.
- Keyword cards are rendered as readable two-column teaching cards instead of oversized glossary tables.
- HTML output uses a fixed left-side numbered navigation tree with compact four-character Chinese anchor labels.
- PDF output removes the HTML navigation node before printing.
- Word, PDF, and HTML exports include table width, border, wrapping, overflow, and local-path checks.

## Typical Use Cases

- Newcomer onboarding for a new industry or technology
- Founder or product pre-research before entering a market
- Sales and marketing teams learning an unfamiliar customer domain
- Investment or strategy teams building a first-pass domain map
- Internal training packs for complex concepts
- Source-backed learning material for emerging fields

## Example Reports

Two public examples are included:

- [China new energy storage expert report](reports/examples/storage-industry-demo/storage-expert-sample.md)
- [GEO China market expert report](reports/examples/geo-china-demo/geo-china-expert-report.md)

Each example also includes exported `Markdown`, `DOCX`, `PDF`, and `HTML` files under its `exports/` directory.

## Reference Materials

The original design and research documents are available in [`reference-materials/`](reference-materials/):

- [industry_expert_skill_design.docx](reference-materials/industry_expert_skill_design.docx)
- [industry_learning_deep_research_report.docx](reference-materials/industry_learning_deep_research_report.docx)

## Main Files

- [`SKILL.md`](SKILL.md): Skill entry point and workflow
- [`references/domain-expert-method.md`](references/domain-expert-method.md): domain research and expert-learning method
- [`references/report-and-tutorial-contract.md`](references/report-and-tutorial-contract.md): report structure and tutorial contract
- [`references/export-and-layout-quality.md`](references/export-and-layout-quality.md): export and layout rules
- [`scripts/export_expert_report.py`](scripts/export_expert_report.py): multi-format exporter
- [`scripts/validate_artifacts.py`](scripts/validate_artifacts.py): artifact validator
- [`templates/expert-report-template.md`](templates/expert-report-template.md): canonical report template
- [`reports/examples/`](reports/examples/): public examples and exported artifacts
- [`reference-materials/`](reference-materials/): source design and research documents

## Boundaries

Do not use this skill for:

- One-off factual answers
- Pure opinion writing without sources
- Simple file conversion
- Business model diagnosis with no learning-report requirement
- Legal, medical, financial, or safety advice as final recommendations

For high-stakes topics, use it as educational research with explicit source and uncertainty labels.
