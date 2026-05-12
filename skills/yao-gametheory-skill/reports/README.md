# Example Reports

This folder contains a curated generated example for `yao-gametheory-skill`.

The reusable logic lives in the skill source. The example is included so readers can inspect the final report layout, table handling, and synchronized artifact set.

## Included Example

### Price War Strategy Case

- `price-war-case.md`
- `price-war-case.html`
- `price-war-case.docx`
- `price-war-case.pdf`
- `price-war-case.canonical.json`

The case models a price-war and channel-conflict decision. It combines Bertrand competition, prisoner's dilemma, repeated game, signaling, credible commitment, and Nash-equilibrium checks.

The current example also demonstrates historical behavior calibration: competitor rationality is adjusted with prior price-war reversals, weak free-tier follow-through, and reference-class SaaS channel-war experience.

## Notes

- The DOCX uses real Word tables instead of pipe-separated paragraphs.
- The PDF is rendered from the HTML with wide-table safeguards.
- The canonical JSON keeps the structured model for future opponent-update runs.
- The report includes prior and history-adjusted rationality probabilities so commitment analysis is not based only on abstract payoff inference.
- Generated working directories from local development are intentionally not included here.
