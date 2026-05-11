# Yao Game Theory Skill

`yao-gametheory-skill` is a game-theory strategy-report skill for competitive, negotiation, channel, platform, M&A, financing, competitor-response, alliance, and regulator-facing decisions.

It is not a textbook explainer. It is built for situations where our best move depends on how other players may react.

## Best-Fit Scenarios

Use it for strategic interactions such as:

- price wars and pricing response
- channel conflict and channel bundling
- competitor retaliation and free-version launches
- platform ecosystem rules and incentives
- financing and commercial negotiation
- M&A bidding and auction-like decisions
- market entry and entry deterrence
- alliances, partner trust, and cooperation design
- regulator communication and public commitments

## Design Principle

The core design principle is simple:

1. Identify players.
2. Map each player's available strategies.
3. Estimate payoffs and constraints.
4. Model timing, information, signals, and commitments.
5. Route the case to the right game-theory framework combination.
6. Convert the model into an executive strategy report.

The skill focuses on three questions:

- What will opponents probably do next?
- Are our commitments credible?
- Which strategy remains robust after opponent reactions?

## Processing Logic

The skill first detects the strategic structure of the case, then combines a primary game-theory framework with secondary lenses.

Common routing combinations include:

- price war: Bertrand + prisoner's dilemma + repeated game + credible commitment
- channel conflict: coalition game + repeated game + bargaining + signaling
- platform ecosystem: coordination + network effects + mechanism design
- M&A bidding: auction + bargaining + signaling + winner's curse
- financing negotiation: bargaining + signaling + outside option + sequential concessions
- market entry: entry deterrence + Stackelberg + credible threat + incomplete information
- regulator communication: sequential game + signaling + reputation

The framework catalog covers Nash equilibrium, zero-sum and non-zero-sum games, coordination games, chicken/hawk-dove, stag hunt, entry deterrence, Stackelberg, Bertrand/Cournot, signaling, repeated games, bargaining, auctions, coalition games, and mechanism design.

## Output Highlights

The report puts action before theory:

- recommended move
- opponent reaction map
- payoff matrix
- credible commitment checks
- signal-quality checks
- possible equilibria
- strategy-readiness score
- sensitivity analysis
- next information to collect
- update triggers for future opponent moves

It exports synchronized `Markdown`, `HTML`, `DOCX`, `PDF`, and canonical `JSON` from the same structured input.

## Quick Start

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-case
```

To merge a later opponent move and regenerate the report:

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-refresh --update input/opponent_update.template.json
```

## Key Files

- `SKILL.md`: skill entrypoint
- `references/framework-catalog.md`: framework catalog and AI application router
- `references/game-model-playbook.md`: modeling playbook for players, strategies, payoffs, timing, and equilibrium logic
- `references/commitment-signal-checklist.md`: credibility and signal-quality checks
- `references/dynamic-iteration-loop.md`: opponent-update workflow
- `scripts/generate_report_bundle.py`: report generator
- `reports/price-war-case.*`: example report artifacts

