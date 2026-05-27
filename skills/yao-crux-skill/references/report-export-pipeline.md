# Report Export Pipeline

## Canonical Flow

1. Convert the user's material into a current-state model.
2. Run the clarity gate:

```bash
python3 scripts/current_state_clarity.py input/example.json
```

3. If the gate says `insufficient`, return the follow-up questions instead of generating a final diagnostic report.
4. Convert the confirmed analysis into a JSON file matching `templates/crux-report.schema.json`, including `analysis_logic` when the principal contradiction depends on a higher-layer or hidden root variable.
5. Run:

```bash
python3 scripts/generate_report_bundle.py input/example.json reports
```

6. The script writes:

```text
<slug>.report.json
<slug>.md
<slug>.html
<slug>.docx
<slug>.pdf
```

7. Verify:

```bash
python3 scripts/verify_report_bundle.py reports
```

## Dependency Notes

- DOCX output prefers `python-docx`; if unavailable, the script falls back to `pandoc` when installed.
- PDF output prefers `weasyprint`.
- If WeasyPrint is unavailable, the script may still generate Markdown, HTML, DOCX, and a warning in the report JSON.
- The final user-facing answer should state whether PDF generation succeeded.

## Bundle Naming

Use the report `slug` when supplied. Otherwise slugify the title. Keep filenames stable across regenerated formats.

## Quality Gates

Before delivery, check:

- all requested formats exist
- extracted text contains Chinese and the conclusion section
- HTML contains required section anchors
- no generated HTML contains `/Users/` or `file://`
- PDF text extraction works when `pdftotext` is available
- probability numbers are clamped between `0%` and `100%`
- high-risk reports contain a review or professional-support warning
- generated report JSON includes `current_state_clarity`, `analysis_logic`, `decision_model`, `visuals`, `resource_allocation`, and `stage_transition`
- generated report JSON includes the theory anchors in `analysis_logic`: `decisiveness`, `leverage`, `stage_fit`, `internal_changeable`, `external_conditions`, and `external_through_internal`
- action rows include `principal_aspect_shift` so recommendations show how they change the principal aspect
- `resource_allocation` includes `aggressiveness`, `main_focus_share`, `secondary_cap_share`, and `monitoring_share`; when the diagnosis is clear, the main focus share should usually be at least `50%`
- HTML includes four SVG chart ids plus the photo-based iceberg module: `chart-analysis-flow`, `chart-iceberg`, `chart-decision-matrix`, `chart-resource-allocation`, and `chart-stage-transition`
- HTML contains the upgraded layout hooks: split conclusion header, compact summary strip, photo-based iceberg, matrix legend box, and vertical stage cards
- browser screenshot checks cover at least the conclusion panel, content-width alignment, iceberg section, decision matrix, and stage transition; fail the handoff if any screenshot shows horizontal overflow, cropped legends, overlapping labels, mismatched gutters, or large unintended blank space
- PDF previews cover the first page, iceberg page, decision matrix page, and stage-transition page. Do not rely only on HTML screenshots because WeasyPrint can treat SVG, flex, and pagination differently from Chromium.

## User Handoff

In the final response, link the generated directory and report files. Mention skipped or failed formats plainly.
