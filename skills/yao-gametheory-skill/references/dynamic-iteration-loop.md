# Dynamic Iteration Loop

Use this workflow when the user adds new opponent moves, channel behavior, regulatory feedback, negotiation terms, bids, or public signals after the first report.

## Goal

Maintain a living game report:

1. keep the previous model as the baseline
2. classify the new move
3. update reactions, payoffs, commitments, and equilibrium interpretation
4. update strategy readiness, sensitivity stability, and next-information needs
5. decide whether the recommendation changes
6. record the update in the report

## Round Log

Each round should be serializable:

```json
{
  "round": 2,
  "date": "2026-05-04",
  "stage": "竞品动作更新",
  "new_information": [
    "头部竞品宣布 30 天免费版本"
  ],
  "classified_as": [
    "signaling game",
    "price war escalation"
  ],
  "affected_players": [
    "us",
    "head_competitor",
    "channel"
  ],
  "payoff_changes": [
    {
      "our_action": "bundle_channel",
      "opponent_action": "launch_free_tier",
      "old_our_payoff": 35,
      "new_our_payoff": 20,
      "reason": "渠道短期会被免费版吸引，但高端客户仍重视服务与集成"
    }
  ],
  "commitment_update": {
    "commitment": "渠道绑定与高端服务 SLA",
    "old_score": 0.78,
    "new_score": 0.82,
    "reason": "新增年度返点和联合交付资源后，承诺更可观察且更难撤回"
  },
  "strategy_readiness_after": 0.78,
  "sensitivity_update": {
    "old_stability": "mixed",
    "new_stability": "stable",
    "reason": "渠道绑定承诺更强，主推荐对免费版冲击更稳健"
  },
  "next_information": [
    "继续观察免费版是否有真实渠道推广与续费路径"
  ],
  "recommendation_status": "unchanged",
  "interim_judgment": "继续避免价格战，强化渠道绑定和高端差异化"
}
```

## Update Rules

- New competitor price cut: re-score price-war payoffs and channel incentives.
- Competitor free version: test whether it is funded, distributed, and product-backed.
- Channel attack: update channel payoff and credibility of channel-binding commitments.
- Regulatory signal: add regulator as a player if approval, enforcement, or public risk changes incentives.
- New bid or financing term: switch to bargaining or auction logic if timing and reservation values matter.
- Alliance shift: re-map coalition payoffs and whether a partner can defect cheaply.

## Stop Condition

Produce an updated report when either:

- the recommendation changes
- commitment credibility crosses a threshold
- one player introduces a new feasible strategy
- a payoff changes enough to alter equilibrium interpretation
- strategy readiness crosses a decision threshold
- sensitivity changes from stable to mixed or fragile
- the user asks for a refreshed board, CEO, or investor artifact
