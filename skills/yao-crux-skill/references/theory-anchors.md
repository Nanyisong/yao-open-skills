# Theory Anchors

This file translates contradiction theory into operating rules for the skill. Use it as a judgment aid, not as report filler.

## Three Questions For Principal Contradiction

Before selecting the principal contradiction, check the top candidate with three plain questions:

| Question | Meaning | High-Confidence Signal |
| --- | --- | --- |
| 决定性 | Does this contradiction directly decide whether the current goal can be reached? | If it is not relieved, other work creates only marginal improvement. |
| 牵引性 | If this contradiction improves, will several other visible problems improve together? | It is upstream of repeated symptoms and releases scarce resources. |
| 阶段性 | Is this contradiction the most important one in the current time window? | It matches the user's current stage, deadline, and hard constraints. |

Report language should explain these three checks in plain Chinese before showing detailed scores.

## Internal And External Cause Gate

Separate constraints into three groups:

| Group | What It Means | How To Use It |
| --- | --- | --- |
| 内部可改变结构 | Capabilities, process, talent density, decision rights, incentives, attention, content quality, data routines, or resource allocation that the user can change. | Prefer actions that change this layer first, because it produces feedback. |
| 外部硬条件 | Platform rules, law, market timing, competition, customer budget cycles, health or safety boundaries. | Treat as guardrails or risk variables, not as excuses. |
| 外因通过内因起作用 | External pressure affects the result through the user's internal structure. | Ask what internal structure can absorb, avoid, amplify, or convert the external condition. |

Do not claim an external condition is the principal contradiction unless the user cannot meaningfully change the internal response path.

## Principal Aspect To Action

After naming the principal aspect, every breakthrough action should say which side it changes:

```text
主要方面：B 当前占支配地位。
动作：通过 X 削弱 B / 增强 A / 改变 A 与 B 的关系。
```

If an action cannot be tied to the principal aspect, it is probably a secondary or support action.

## Aggressive Resource Reallocation

When the principal contradiction is clear enough, resource allocation should be more decisive than the user's current pattern.

Default rule:

- Put `50%-70%` of high-leverage time, attention, decision rights, and scarce budget into actions that change the principal contradiction.
- Cut or cap secondary contradictions to `10%-25%` total unless they are hard-boundary risks.
- Keep `10%-20%` for monitoring, evidence collection, and stop-loss patches.

Use softer allocation only when:

- safety, legal, health, cash, or reputation constraints require caution
- the current-state clarity is below the diagnosis threshold
- the selected principal contradiction has a score below `3.5/5`
- actions have high irreversibility or require external approval

In reports, write the allocation as a deliberate tilt: `主攻`, `压缩`, `保底`, and `观察`, not as an even task list.

## Dynamic Transfer Rule

The principal contradiction is a current-stage hypothesis. Every diagnosis needs:

- what evidence shows the current principal contradiction has been relieved
- which secondary contradiction is most likely to rise next
- when to re-score the candidates
- what new evidence would overturn the current judgment
