# Artifact Design Profile

## Artifact Family

High-trust executive strategy report.

## Visual Direction

- restrained editorial layout
- clear executive summary at the top
- compact tables for players, reactions, payoffs, and commitments
- subdued palette with action, risk, and evidence accents
- no decorative hero, generic gradients, or repeated card grids

## HTML Quality Gates

- top navigation stays usable on narrow screens
- print controls are visible but hidden in print output
- payoff and reaction tables remain readable on mobile through horizontal scrolling
- appendix sections can collapse on screen but expand before print
- no absolute local filesystem paths in the HTML

## DOCX Quality Gates

- headings remain specific to the case
- recommendation appears on the first page
- tables have short labels and do not depend on color alone
- assumptions and warnings are visible without reading the appendix

## PDF Quality Gates

- generated from the same HTML when possible
- report remains readable in black-and-white print
- folded HTML sections expand before print
- if automated rendering is unavailable, do not create a fake PDF
- wide tables must not overflow the right page edge
- print CSS should use fixed-width tables, automatic text wrapping, and A4 landscape for dense matrix reports

## Word Quality Gates

- DOCX export must use real Word tables for matrix-style content
- fallback OOXML export must not degrade tables into pipe-separated paragraphs
- wide tables should use landscape page setup and compact cell text
