# Strategic Report Contract

Every report should be executive-readable before it becomes technical.

## Required Sections

1. One-sentence conclusion
2. Recommended move and moves to avoid
3. Framework selection: primary framework, secondary lenses, and excluded famous frameworks
4. Opponent reaction map
5. Credible commitment and signal verdict
6. Player map
7. Strategy sets
8. Payoff matrix
9. Expected payoff or scenario ranking
10. Equilibrium interpretation
11. Historical behavior and rationality-probability calibration
12. Strategy readiness and remaining gaps
13. Strategic hygiene checks
14. Sensitivity and stability analysis
15. Next information to collect
16. Repeated-game and relationship dynamics
17. Dynamic update log when available
18. Triggers that should reopen the report
19. Risks, caveats, and illegal or unethical tactic boundaries
20. Appendix with assumptions and data provenance

## Mandatory Distinctions

Never mix:

- observed facts
- estimated payoffs or probabilities
- assumed placeholders
- analyst interpretation

## Recommendation Rule

The report must answer:

- what we should do now
- how the opponent is likely to react
- whether our commitment is credible
- whether opponent rationality and credible commitments were adjusted with real historical behavior
- which move would trap us in a worse game
- what evidence would change the recommendation
- whether the strategy is ready enough to act on
- when to update the game model

## Report Tone

Use concise executive language:

- no theorem-first explanation
- no inflated certainty
- no decorative theory names unless they guide the decision
- no "win-win" claims without payoff evidence

## Schema Alignment

Target the JSON layout in `templates/report.schema.json`.

At minimum, fill:

- `summary`
- `framework_selection`
- `players`
- `our_actions`
- `opponent_actions`
- `reaction_estimates`
- `payoff_matrix`
- `commitment_tests`
- `historical_behavior_analysis`
- `strategy_readiness`
- `strategic_hygiene`
- `sensitivity`
- `next_information`
- `signals`
- `equilibrium`
- `repeated_game`
- `rounds`
- `scenario_triggers`
- `warnings`
