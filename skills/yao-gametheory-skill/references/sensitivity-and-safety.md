# Sensitivity And Safety

Use this layer to test whether the recommendation depends too heavily on fragile assumptions.

## Sensitivity Questions

Stress test at least these assumptions:

- opponent reaction probability: what if the competitor is more aggressive than expected
- payoff estimates: what if our channel or margin benefit is overestimated
- commitment credibility: what if our commitment is viewed as cheap talk
- signal credibility: what if an opponent announcement is real rather than bluffing
- repeated-game value: what if future relationship value is lower than assumed
- opponent rationality: what if the model overestimates the opponent's rationality, time consistency, or commitment follow-through
- historical behavior: what if real past behavior is more predictive than payoff-matrix inference
- legal and regulatory risk: what if a tactic needs compliance review before execution

## Rationality Overestimation Check

Add this check whenever the case involves repeated games, credible commitments, threats, free-version launches, channel attacks, or negotiation deadlines.

Question the model's default rationality assumption:

- Has this player actually followed through on similar threats?
- Did past announcements receive real budget, product, channel, or legal resources?
- Did the player reverse when costs became visible?
- Is the action rational for the modeled company but irrational for the actual organization because of cash, incentives, politics, capability, or attention limits?
- Does operator experience from similar cases suggest systematic bluffing or under-delivery?

If real behavior contradicts the clean model, historical behavior wins. Lower the relevant rationality probability, commitment score, and signal credibility. Preserve short-term disruption risk even when long-term follow-through is weak.

## Stability Bands

- `stable`: the recommended action remains best under plausible stress tests
- `mixed`: the recommendation remains directionally useful but depends on one or two assumptions
- `fragile`: the recommendation changes under modest assumption shifts

## Minimum Output

Every report should include:

- base recommendation
- runner-up action
- payoff gap or qualitative margin of safety
- most dangerous assumption
- historical behavior or reference-class evidence that could change the rationality probability
- disconfirming evidence
- action that should be delayed if the case is fragile

## Safety Boundaries

Flag and avoid:

- price coordination with competitors
- market allocation
- exclusionary conduct without legal review
- deceptive signaling
- coercive channel tactics
- illegal information exchange
- final legal, investment, financial, or regulatory advice

The skill may identify risk and recommend review; it must not provide final regulated advice.
