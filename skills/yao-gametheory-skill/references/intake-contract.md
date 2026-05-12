# Intake Contract

Use this contract to turn a messy strategy question into one game brief.

## Minimum Viable Brief

Collect only what changes the model:

- decision question: what move are we choosing now
- time horizon: one-shot, launch window, quarter, annual contract, repeated season
- players: us, direct competitors, channels, customers, platforms, regulators, investors, partners
- strategies: actions each player can realistically take
- payoffs: revenue, margin, share, retention, channel power, reputation, optionality, regulatory risk
- information: what each player knows, observes, hides, or can credibly signal
- historical behavior data: how each player actually behaved in similar past games, including threat follow-through, reversal patterns, price discipline, channel conduct, and signal accuracy
- experience reference analysis: analogous cases or operator experience that should adjust the model's default rationality assumptions
- timing: simultaneous, sequential, auction, negotiation, repeated interaction
- constraints: cash, contracts, capacity, compliance, channel exclusivity, reputation, board limits
- current observed moves: announcements, price changes, channel attacks, free versions, bids, public filings

## Default Player Frame

For CEO strategy work, start with these players unless the user gives a better map:

- `us`: the focal company
- `head_competitor`: strongest competitor or incumbent
- `channel`: distributors, agencies, platforms, resellers, or procurement gatekeepers
- `customer`: buyer segment whose switching behavior determines payoffs
- `regulator_or_investor`: include only when the case involves compliance, public policy, financing, or M&A approval

## Required Distinctions

Mark every payoff, probability, and constraint as one of:

- observed: directly provided or sourceable from the user
- estimated: analyst judgment from current evidence
- assumed: placeholder used to keep the first model moving

## Historical Behavior Calibration

Do not let the model infer rationality only from abstract payoff logic. In repeated games and credible-commitment analysis, AI models often overestimate how rational and time-consistent opponents will be.

Prefer real historical behavior when available:

- past threats: whether the player actually followed through
- past price wars: how long discounts lasted before reversal
- past channel attacks: whether promised incentives were funded and sustained
- past free-version launches: whether product, support, and conversion resources followed the announcement
- past negotiations: whether the player honored deadlines, walk-away threats, or public commitments
- operator experience: credible reference classes from similar markets, channels, or deal types

Recommended input fields:

```json
{
  "rationality_priors": {
    "head_competitor": 0.74
  },
  "historical_behavior_data": [
    {
      "player_id": "head_competitor",
      "event": "Previous price-war threat was reversed after 6 weeks.",
      "observed_action": "cheap_talk_then_reversal",
      "context_similarity": 0.82,
      "rationality_signal": "bounded",
      "commitment_follow_through": 0.25,
      "source": "CRM quotes and channel interviews",
      "implication": "Lower the credibility of long-term low-price threats."
    }
  ],
  "experience_reference_analysis": [
    {
      "player_id": "head_competitor",
      "reference_class": "Similar SaaS channel price wars",
      "pattern": "Free-tier threats often create short-term noise but lack sustained delivery investment.",
      "rationality_adjustment": -0.14,
      "confidence": 0.72,
      "implication": "Reduce the probability of fully rational long-term follow-through."
    }
  ]
}
```

If historical behavior is missing, explicitly mark rationality as a model prior and add a next-information item to collect it.

## Clarification Rule

Do not block on perfect data. If a brief is incomplete:

- create a provisional model with assumptions
- ask at most three questions that would change the recommendation
- record the missing inputs in the update log

## Near-Neighbor Boundary

If the task is only "what is game theory" or "explain Nash equilibrium", answer directly without invoking the full report flow. Use this skill when the user needs a strategic decision artifact.
