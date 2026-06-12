# Kami White Report Layout

Use Kami's document discipline, but apply the user's explicit override: every report background is pure white.

## Visual Direction

The output is a high-trust demand assessment report, not a SaaS dashboard and not a marketing landing page.

- page background: pure white `#ffffff`
- primary text: near-black `#141413`
- secondary text: warm graphite `#3d3d3a`
- tertiary text: warm stone `#6b6a64`
- border: light warm gray `#e8e6dc`
- soft border: `#efeee8`
- accent: ink-blue `#1B365D`, used sparingly for section bars, links, score marks, and nav active state
- state colors: muted green, amber, red only for risk/severity, never decorative gradients

Do not use parchment, beige page background, purple-blue gradients, glass cards, bokeh, blobs, or heavy drop shadows.

## Typography

Use a serif-led document hierarchy:

```css
--serif: "TsangerJinKai02", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", "STSong", Georgia, serif;
--sans: var(--serif);
--mono: "JetBrains Mono", "SF Mono", Consolas, "TsangerJinKai02", "Source Han Serif SC", monospace;
```

Print scale:

| Role | Size | Line Height |
|---|---:|---:|
| Display title | 30-36pt | 1.12 |
| H1 | 21-24pt | 1.20 |
| H2 | 15-17pt | 1.25 |
| H3 | 12-13pt | 1.30 |
| Body | 10-10.5pt | 1.52-1.58 |
| Dense table | 8.5-9.2pt | 1.38-1.45 |
| Caption | 8.5-9pt | 1.40 |

Screen scale should remain readable on mobile; body text should not fall below `15px`.

## HTML Top Follow Menu

HTML reports must include a top follow menu:

- current renderer uses `position: fixed; top: 0; left: 0; right: 0; z-index: 100`
- white background with subtle bottom border
- subtle shadow so the menu remains visible while scrolling
- product/report title on the left
- anchor links to major sections on the right
- horizontal overflow allowed on narrow screens
- no JS required for navigation
- hide the follow menu in print/PDF

Use anchors for:

- summary
- product
- method
- users
- competitors
- triangle
- scores
- recommendations
- risks
- appendix

## Layout

- `max-width: 1120px` on screen
- main content centered with `24-40px` responsive padding
- top report header followed by score strip
- visual diagnostics section appears before dense analysis
- chart modules use a two-column editorial grid on desktop and one-column stack on mobile
- desktop chart modules must stretch to equal height within the same grid row, so row starts and card bottoms align even when chart explanations differ in length
- chart modules should feel editorial and calm: use more width, clear headers, readable chart captions, and avoid cramped labels even if that means using a larger SVG viewBox or internal horizontal scroll on mobile
- desktop and PDF chart modules must show the full chart inside the card. Do not require horizontal scroll on desktop for essential labels, score bands, legends, axis labels, markers, or recommendations.
- mobile chart modules may use internal horizontal scroll, but the first viewport should still show the chart's main signal and must not cut off critical final labels such as the rightmost score band.
- major sections separated by whitespace and a quiet top border
- use cards only for true repeated objects or score blocks, not nested decorative surfaces
- long tables must sit inside `.table-wrap { overflow-x: auto; }`
- long URLs and source titles must use `overflow-wrap: anywhere`
- code and raw evidence blocks must wrap and not overflow
- prose blocks should use the available reading width. Avoid narrow columns that leave large ragged whitespace on the right; use balanced desktop columns only when each column still gives Chinese paragraphs enough line length.

## Visual Diagnostic Modules

Reports should include 10+ chart modules. Treat them as diagnostic figures, not decoration.

Each chart module needs:

- title
- chart
- one or two sentence insight
- one sentence recommendation
- confidence
- source IDs or an assumption label

Supported chart types:

| Type | Use |
|---|---|
| `score_gauge` | Overall score, decision band, and scale readiness. |
| `radar` | Demand triangle and subscore balance. |
| `bar` | Dimension comparison, subscore ranking, and short-board ranking. |
| `heatmap` | Dense subscore weakness scan. |
| `matrix` | Segment, competitor, risk, and recommendation prioritization. |
| `funnel` | Adoption friction from awareness to renewal. |
| `stacked_bar` | Evidence quality or source mix. |
| `forecast` | Scenario-based future state, never deterministic prediction. |

Chart rules:

- inline SVG in HTML/PDF
- pure white chart background
- no gradients, decorative shadows, blobs, glass effects, or purple-blue palettes
- ink-blue for main signal, muted green/amber/red only for status
- text labels must not be clipped in A4 print
- long labels should wrap or truncate with accompanying table text
- score gauge charts must reserve internal right padding for the last band label and marker. The full scale from weakest to strongest must be visible at desktop report width without scrolling.
- score gauge charts must also fit mobile card width without internal horizontal scrolling; use a compact dedicated viewBox rather than hiding the right side of the scale.
- matrix/scatter charts must include label collision handling: use numbered markers plus a compact two-column legend when points cluster; point-side labels may be used only when they do not overlap or disappear at report scale
- clustered points should remain visible as a cluster instead of becoming unreadable text. Reduce marker size, increase plot area, and separate labels from markers before removing data.
- every chart must remain readable at `375px` mobile width through responsive scaling or horizontal scroll
- dense chart data should also be represented in nearby text or tables for accessibility

## Tables

Table rules:

- `border-collapse: collapse`
- header bottom border `1px solid #e8e6dc`
- row borders `1px solid #efeee8`
- compact padding for dense evidence tables
- no zebra stripes unless a table exceeds six rows and scanning is difficult
- no columns so narrow that Chinese text stacks one character per line

## Diagrams

Required diagrams:

- process flow: `输入 -> 解析 -> 检索 -> 分析 -> 评分 -> 输出`
- demand triangle: `缺乏感 + 目标物 + 消费者能力`, with the center statement that demand depends on motivation clarity, acceptable cost, and scene trigger
- visual diagnostics: score gauge, radar, bar, heatmap, matrix, funnel, stacked bar, and forecast SVGs

Diagram rules:

- use inline SVG for HTML/PDF; avoid large base64 images
- keep diagrams black, warm gray, and ink-blue only
- labels must remain readable on A4 print and mobile
- every diagram needs a `figure` title and an insight caption
- SVG must have a stable `viewBox`, no fixed pixel overflow, and no clipped text
- demand triangle diagrams must not use a large center circle or decorative arrows that compete with the triangle itself. Put the center judgment in lightweight text, with only subtle helper lines when needed.
- Markdown should include Mermaid or a text fallback; Word should include a structured table or figure note when image insertion is unavailable

## PDF Print Rules

Use the same HTML as PDF source when possible:

```css
@page {
  size: A4;
  margin: 18mm 20mm 20mm 20mm;
  background: #ffffff;
}
@media print {
  .top-nav { display: none; }
  section, .score-card, .fact-box, .risk-item { break-inside: avoid; }
}
```

PDF must not show browser UI, fixed nav, broken anchor menu, clipped tables, or low-contrast text.

## Word Rules

Word output is the editable review copy:

- preserve the same section order as Markdown and HTML
- include visual diagnostic modules before dense analysis
- insert chart PNGs when `python-docx` and SVG-to-PNG conversion are available
- fall back to chart-equivalent tables and insight text when image conversion is unavailable
- fallback Word output must still look like a report: A4 margins, serif Chinese typography, clear heading hierarchy, light table borders, subtle header shading, compact cell padding, and readable paragraph spacing
- use heading levels, not manually bolded paragraphs
- use simple tables for scores, competitors, sources, risks, and experiments
- keep borders light and avoid dense nested tables
- include report date, source boundary, and evidence appendix

## QA Checklist

- white background visible in HTML and PDF
- fixed top follow menu works in HTML and is hidden in PDF
- long competitor/source/evidence tables scroll on mobile and do not overflow print pages
- citations remain readable and do not interrupt the core narrative
- no placeholder text remains
- all four outputs have the same title, date, scores, recommendations, and evidence list
- HTML/PDF contain at least 10 `.chart-module` blocks for formal reports
- desktop chart modules align by row height; mobile chart modules stack without forcing page-level horizontal overflow
- desktop `.chart-svg-wrap` elements do not horizontally overflow for essential chart modules, especially score gauges
- mobile score gauge modules show the full scale and rightmost band label in the first viewport
- matrix/scatter chart labels do not overlap in the rendered HTML screenshot
- demand triangle uses a lightweight center label and does not visually fight with a large circle
- Word output is checked for non-empty document XML, styled headings, and readable tables whether it uses `python-docx` or fallback OOXML
- every chart module has a visible insight and recommendation
- forecast module states assumptions and confidence
