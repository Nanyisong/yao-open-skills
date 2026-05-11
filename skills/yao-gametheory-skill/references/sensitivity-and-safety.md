# Sensitivity And Safety

Use this layer to test whether the recommendation depends too heavily on fragile assumptions.

## Sensitivity Questions

Stress test at least these assumptions:

- opponent reaction probability: what if the competitor is more aggressive than expected
- payoff estimates: what if our channel or margin benefit is overestimated
- commitment credibility: what if our commitment is viewed as cheap talk
- signal credibility: what if an opponent announcement is real rather than bluffing
- repeated-game value: what if future relationship value is lower than assumed
- legal and regulatory risk: what if a tactic needs compliance review before execution

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

