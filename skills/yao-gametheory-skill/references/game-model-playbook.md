# Game Model Playbook

Use the lightest model that explains strategic reactions. Start with `references/framework-catalog.md` when the case needs a named framework library, then use this playbook to instantiate the selected framework combination.

## Core Elements

- players: who can change the outcome
- strategy set: what each player can actually do
- payoff matrix: how each action pair changes each player's utility
- beliefs: what players expect others to do
- equilibrium candidates: stable action profiles where no player has an obvious unilateral improvement
- timing: simultaneous, sequential, bargaining, auction, repeated, or coalition game
- commitment and signals: actions that alter other players' expectations

## Model Selection

Choose one primary frame after checking the router in `references/framework-catalog.md`:

- normal-form game: price moves, feature parity, channel offers, simultaneous launch choices
- sequential game: entry deterrence, retaliation threats, channel exclusivity, regulator engagement
- repeated game: pricing discipline, partner trust, marketplace governance, ecosystem retaliation
- bargaining game: financing terms, labor negotiation, M&A terms, channel take rate
- auction or bidding game: M&A竞价, procurement, scarce channel slots
- coalition game: alliances, platform ecosystems, multi-party distribution, standard-setting
- signaling game: public roadmap, free-tier announcement, regulatory posture, financing confidence

## Payoff Scoring

Use a compact score when precise numbers are unavailable:

- `+100`: very strong strategic upside
- `+50`: meaningful advantage
- `0`: neutral or unclear
- `-50`: meaningful loss
- `-100`: severe strategic loss

Name the payoff basis:

- margin
- market share
- channel control
- customer retention
- switching cost
- reputation
- option value
- regulatory exposure
- alliance durability

## Equilibrium Reasoning

Use equilibrium language only as far as the evidence supports it:

- dominant strategy: one action beats alternatives regardless of opponent response
- Nash equilibrium: each player's action is a best response to the others
- subgame-perfect logic: ignore threats that would not be rational when the moment arrives
- mixed strategy: players may randomize or keep ambiguity when pure commitment is exploitable
- repeated-game equilibrium: cooperation can hold when future punishment or future surplus is valuable

## CEO Interpretation

Translate the model into operational language:

- "对手最可能怎么回击"
- "什么动作会把我们锁进低质量博弈"
- "哪个承诺对外可信、对内可执行"
- "哪个信号只是口头威胁"
- "哪类后续动作会迫使我们更新报告"

## Default Price-War Heuristic

When our options include lowering price, bundling channels, differentiating upward, or holding price:

- discount low-margin price cuts if the head competitor can match quickly
- favor channel binding when channel incentives can be made visible and durable
- favor high-end differentiation when customers value quality, integration, service, or risk reduction
- treat free-version threats as credible only when the competitor has distribution, funding, and product architecture to support them
