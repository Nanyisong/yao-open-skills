# Design Summary

## Chosen Fit

- archetype: `library`
- package goal: reusable game theory strategy reporting for CEO-facing competitive interactions
- core boundary: problems where our best action depends on expected reactions from competitors, channels, partners, investors, regulators, or other strategic players

## Reference Scan

- Stanford Encyclopedia of Philosophy: game theory frames outcomes as products of interacting choices and highlights cases where one agent's best action depends on expectations about others.
- Nobel Prize 1994 material: Nash equilibrium and refinements are useful, but credible-threat filtering matters in cases such as price-war deterrence.
- Nobel Prize 2005 material: strategic interaction is a practical cooperation, conflict, and institution-design toolbox, not just a math exercise.
- Local reference: `yao-bayesian-skill` contributed the multi-turn update loop, round log discipline, and one-input-to-many-artifacts export contract.

## Borrowed Patterns

- Keep `SKILL.md` lean and move report rules into `references/`.
- Start from incomplete inputs and produce a provisional model instead of waiting for perfect data.
- Treat every update as a new round with explicit changes to assumptions, payoffs, commitments, and recommendation status.
- Generate Markdown, HTML, DOCX, PDF, and canonical JSON from the same structured input.

## Not Borrowed

- Do not turn the skill into a general economics textbook.
- Do not overfit to two-player zero-sum games; CEO cases often include channels, partners, regulators, and repeated relationships.
- Do not use equilibrium labels when a simpler reaction map is enough.

## MVP Implemented Here

- structured intake contract
- game model playbook
- framework catalog and AI application router
- credible commitment and signal checklist
- dynamic opponent-update loop
- report contract and export pipeline
- sample price-war case
- report generator for Markdown, HTML, DOCX, canonical JSON, and PDF when local rendering is available

## Next Iteration Directions

1. Add a small library of industry-specific payoff templates for SaaS, consumer, marketplace, education, and channel businesses.
2. Add route-confusion tests against Bayesian, generic strategy, and legal/regulatory skills.
3. Add richer visual equilibrium maps and scenario trees in the HTML report.
