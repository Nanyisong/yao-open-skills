# Strategy Readiness Loop

Borrowed from the Bayesian skill's decision-readiness discipline, this loop tracks whether a game-theory report is mature enough to act on.

## Goal

Turn an incomplete strategic case into a living model:

1. provisional game frame
2. player and strategy map
3. payoff and reaction assumptions
4. commitment and signal checks
5. sensitivity stress test
6. strategy-readiness score
7. next information to collect
8. round-by-round update log

## Readiness Is Not Confidence

`strategy_readiness` measures whether the model has enough structure to support action. It is not a claim that the recommendation is guaranteed.

Default bands:

- `0.00 - 0.44`: still collecting critical strategic information
- `0.45 - 0.74`: usable for directional planning; one or two gaps still matter
- `0.75 - 1.00`: ready for a formal strategy recommendation, with stated caveats

## Readiness Inputs

Score these dimensions:

- player completeness: are the strategic actors named
- strategy completeness: are feasible moves listed for each critical player
- payoff provenance: are payoffs marked observed, estimated, or assumed
- reaction evidence: are opponent responses tied to incentives
- commitment credibility: are our commitments scored for cost, observability, reversibility, incentives, and capability
- framework fit: does the selected framework match timing, information, and payoff structure
- sensitivity stability: does the recommendation survive plausible changes
- updateability: are triggers and round logs present

## Round Rule

After each new opponent, channel, regulator, investor, or partner move, record:

- what changed
- which player and strategy it affects
- which payoff or reaction probability moved
- whether commitment credibility changed
- whether framework choice changed
- whether recommendation changed
- new strategy-readiness score

## Stop Rule

Produce a formal report when either:

- readiness is high enough and the top recommendation is stable, or
- readiness is not high enough but the best action is to avoid irreversible moves and gather specific information first

