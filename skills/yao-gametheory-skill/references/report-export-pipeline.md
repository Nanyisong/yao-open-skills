# Report Export Pipeline

## Default Artifact Set

Generate these artifacts from the same structured input:

- Markdown: readable source draft and versionable report
- HTML: visual review report with print controls
- DOCX: Word document for leadership review and tracked edits
- PDF: automatically rendered when a local PDF renderer is available; otherwise use the HTML print flow
- JSON: canonical model output for future updates

## Command

Use:

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-case
```

To include a later opponent update:

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-refresh --update input/opponent_update.template.json
```

## HTML Rules

The HTML report should include:

- sticky navigation
- executive summary first
- payoff and reaction tables
- strategy-readiness and sensitivity sections near the top
- collapsible appendix
- top-right `Print / Save as PDF` action
- automatic expansion of folded sections before print

## Word Rules

The DOCX should be readable without the HTML:

- title
- recommendation
- framework selection
- strategy readiness
- strategic hygiene checks
- sensitivity and stability analysis
- next information to collect
- player map
- payoff table
- reaction map
- commitment checks
- update log
- caveats
- use real Word tables for player maps, reactions, payoffs, commitments, and update logs
- do not simulate tables with pipe-separated paragraphs
- use landscape page setup or compact table widths when wide strategic tables are present

## PDF Rules

Prefer automated PDF rendering from HTML. If no renderer exists, do not fake a low-quality PDF; keep the HTML print-ready and tell the user to save it as PDF from the browser.

Wide tables must remain inside the printable page:

- print layout should use A4 landscape for dense strategy reports
- table width must be fixed to the printable page
- cell text must wrap instead of overflowing rightward
- long identifiers and mixed Chinese/English labels must break safely inside cells

## Automation Rule

Do not hand-write separate artifacts. All formats should be generated from the same input so future opponent moves can be merged and re-exported consistently.
