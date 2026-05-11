# Bayesian-Inspired Upgrade Plan

## Objective

Upgrade `yao-gametheory-skill` from a framework-and-report generator into a dynamic strategic model that borrows the best engineering patterns from `yao-bayesian-skill`.

## Borrowed Design Patterns

- weak-start loop: start with a provisional model instead of waiting for perfect input
- readiness score: separate "recommendation strength" from "decision maturity"
- sensitivity analysis: stress test whether the recommendation survives assumption changes
- next-information discipline: name the exact information that would change the recommendation
- round log: record how each new move changes players, payoffs, commitments, and recommendation status
- one-source export: generate Markdown, HTML, DOCX, PDF, and canonical JSON from the same structured case
- output quality gates: keep report sections readable and mark observed, estimated, and assumed inputs

## Implementation Plan

1. Add `strategy-readiness-loop.md` to define game-readiness scoring and update rules.
2. Add `sensitivity-and-safety.md` for payoff, reaction, commitment, signal, and compliance stress tests.
3. Add `strategic-hygiene-checklist.md` for the strategic equivalent of prior hygiene.
4. Update `SKILL.md` so the default workflow includes hygiene, readiness, sensitivity, and next information.
5. Update report schema with `strategy_readiness`, `strategic_hygiene`, `sensitivity`, and `next_information`.
6. Extend `generate_report_bundle.py` to compute and render those fields.
7. Refresh the price-war sample to demonstrate the upgraded sections.
8. Run validation, resource-boundary, trigger, and export checks.

## Success Checks

- Incomplete cases still produce a useful provisional model.
- Reports show strategy readiness and remaining gaps.
- Reports explain which assumptions could change the recommendation.
- The generated Markdown, HTML, Word, PDF, and JSON stay synchronized.
- Existing framework routing and layout fixes do not regress.

