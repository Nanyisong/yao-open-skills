# Source Synthesis

## Source Materials Read

- Demand assessment skill design packet supplied by the skill author.
- Demand triangle model research packet supplied by the skill author.
- PDF and HTML reference exports of the same two packets, used to recover missing diagram context from Markdown.
- Local Kami report-layout skill instructions, including its cheatsheet, production guidance, and design guidance.

## Extracted Design Decisions

1. The skill should own product demand assessment, not broad market sizing or business-model strategy.
2. The core model is the demand triangle: lack, target object, consumer ability.
3. The practical workflow is input -> parse -> research -> analyze -> score -> output.
4. Evidence is central: official sources first, third-party/user feedback second, social signals only as weak evidence.
5. Scoring must use geometric mean so a strong dimension cannot hide a collapsed short board.
6. Final outputs must be four formats: Markdown, HTML, Word, and PDF.
7. HTML needs fixed top follow navigation, while print/PDF hides that navigation.
8. User explicitly requires pure white report backgrounds. Kami's parchment invariant is overridden, but its editorial hierarchy, spacing, table discipline, and production checks are retained.
9. The original HTML/PDF visual references include two important diagrams: the workflow strip and the triangle model. The new skill renders these as portable inline SVG or text equivalents, not base64 images.

## What Not To Borrow

- Do not paste the source reports' large base64 images into the skill.
- Do not inherit the source HTML's generic blue-gray web styling as the final output system.
- Do not use a dashboard-heavy card grid; keep the artifact as a report.
- Do not route general monetization, legal advice, or pure UX review into this skill.

## Open Assumptions

- The first release is Production-light because the output is reusable and multi-format, but the skill is not yet a shared infrastructure Library.
- The agent still performs research and reasoning; scripts handle scoring, validation, and rendering.
- Word output uses document-native headings and tables. HTML/PDF carry the richer diagrams.
