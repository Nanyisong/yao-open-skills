---
name: yao-crux-skill
description: Use when a user is stuck in a complex real-world situation with many conflicts, limited resources, unclear priorities, or asks to identify the principal contradiction, secondary contradictions, dominant aspect, breakthrough actions, monitoring thresholds, probability projection, and Markdown/Word/HTML/PDF reports. Triggers on 矛盾论, 主要矛盾, 次要矛盾, 主次矛盾, 卡住了, 优先级混乱, 找关键问题, 资源有限, 冲突很多. Do not use for philosophy-only summaries, Mao text commentary with no live case, generic brainstorming with no diagnosis, or final licensed medical, legal, investment, or psychological-crisis advice.
metadata:
  author: Yao Team
  maturity: production-scaffold
  public_release: sanitized
---

# Yao Crux Skill

Use this skill to first clarify the user's current situation, then turn it into a principal-contradiction diagnosis, a secondary-contradiction watchlist, a focused action plan, and a four-format report bundle.

## Use This Skill For

- ask concise follow-up questions before judging a user's current situation
- assess whether the user's current situation is clear enough for diagnosis before naming the principal contradiction
- produce a confirmable current-state snapshot with goal, facts, stage, resources, constraints, stakeholders, and repeated patterns
- identify goals, stage, constraints, facts, stakeholders, resources, and repeated conflict patterns
- rewrite messy symptoms as candidate contradictions in the form `力量A 与 力量B 的冲突`
- run a first-principles layer scan so the principal contradiction can be an upstream, not-yet-visible constraint rather than the loudest symptom
- use the three plain principal-contradiction checks: `决定性`, `牵引性`, and `阶段性`
- separate internal changeable structures from external hard conditions, then judge how external conditions act through internal structure
- use Bayesian-style evidence updates and Ockham-razor parsimony as supporting checks when candidate contradictions are close
- score principal and secondary contradictions by goal impact, causal leverage, stage urgency, resource constraint, changeability, spillover risk, and evidence strength
- identify the principal aspect inside the principal contradiction
- recommend 1-3 breakthrough actions that explicitly weaken or reverse the principal aspect, monitoring thresholds, review conditions, and probability projections after action
- make resource and attention allocation decisive when the principal contradiction is clear, typically concentrating 50%-70% of high-leverage resources on the main line
- include visual reasoning modules: analysis flow, iceberg model, contradiction decision matrix, resource allocation, and stage transition map
- write user-facing reports that explicitly use `主要矛盾` and `次要矛盾`, while translating them with practical labels such as `最关键的卡点` and `先不主攻，但要盯住`
- export synchronized `markdown`, `html`, `docx`, and `pdf` reports using the Kami-style layout rules in this package

## Do Not Route Here

- generic explanation of `矛盾论` with no concrete user case
- historical, ideological, or textual commentary where no diagnosis or action report is needed
- broad brainstorming that does not require a principal/secondary contradiction conclusion
- final professional medical, legal, investment, safety-critical, or psychological-crisis advice

## Default Workflow

1. Read `references/intake-and-questioning.md`; extract the user's target, stage, constraints, resources, facts, stakeholders, and previous attempts.
2. Run the current-state gate from `references/intake-and-questioning.md` or `scripts/current_state_clarity.py`; score clarity before diagnosis.
3. If clarity is `insufficient`, do not name a principal contradiction. Ask no more than 3 decisive questions and stop.
4. If clarity is `workable`, produce a provisional current-state snapshot, ask the missing questions, and label any contradiction read as provisional.
5. If clarity is `clear`, restate the current-state snapshot and ask the user to confirm or correct it before deep diagnosis.
6. Run `references/safety-and-boundaries.md`; hard constraints remain guardrails even when they are not the principal contradiction.
7. Read `references/theory-anchors.md`; use `决定性`, `牵引性`, and `阶段性` as the plain-language front gate before detailed scoring.
8. Use the first-principles gate in `references/contradiction-model.md`: separate visible symptoms from the hidden root variable that can explain several symptoms together.
9. Separate `内部可改变结构`, `外部硬条件`, and `外因通过内因起作用`; do not mistake an external condition for the principal contradiction when an internal response path is available.
10. Build 3-7 candidate contradictions, including at least one upstream candidate if the visible symptoms share a common cause.
11. Score candidates with the weighted model; use Bayesian-style updates to ask which explanation fits the evidence best.
12. Apply Ockham razor only as a supporting tie-breaker: prefer the explanation that covers more symptoms with fewer extra assumptions.
13. If the top contradiction is below `3.5/5` or the evidence is too weak, return a provisional read and ask for the missing evidence instead of over-claiming.
14. Identify the principal contradiction, its principal aspect, secondary contradictions, defer reasons, monitor triggers, and review conditions.
15. Tie each breakthrough action to the principal aspect: say whether it weakens the currently dominant side, strengthens the weaker side, or changes their relationship.
16. Reallocate resources aggressively when evidence is sufficient: protect the main line, cap secondary contradictions, and keep only minimal stop-loss capacity for monitored risks.
17. Build a canonical report input JSON using `templates/crux-report.schema.json`, including visual and dynamic-stage fields when available.
18. Run `scripts/generate_report_bundle.py input_file.json output_dir` for synchronized Markdown, HTML, Word, PDF, and `.report.json` artifacts.
19. Check the bundle with `scripts/verify_report_bundle.py output_dir` before claiming completion.
20. For HTML/PDF delivery, perform a visual pass on the conclusion, current-state tables, iceberg, decision matrix, and stage-transition sections. Reject the output if the content container width drifts away from the top navigation width, or if there is horizontal overflow, clipped legends, overlapping labels, empty chart space, or decorative imagery that does not explain the analysis.

## Output Contract

- Lead with the conclusion: current principal contradiction, principal aspect, confidence, and first action.
- Before the conclusion, make sure the current-state snapshot is explicit enough; if not, lead with follow-up questions instead of a diagnosis.
- Default report headings must integrate the concepts and the practical translation: `主要矛盾（最关键的卡点）`, `次要矛盾（先不主攻，但要盯住）`, `主要矛盾判断过程`.
- The report must show the first-principles reasoning: `看得见的问题`, `上升一层`, `看不见的根部变量`, and why the visible issue is not necessarily the principal contradiction.
- The report must explain the principal contradiction through `决定性`, `牵引性`, and `阶段性` before falling back to scores.
- The report must separate `内部可改变结构` from `外部硬条件`, then explain how external conditions act through internal structure.
- The report must include the visual reasoning sections `一张图看懂：从表象到主要矛盾`, `时间、精力、资源应该怎么重新分配`, and `主要矛盾什么时候会转移`.
- HTML/PDF reports should render four inline SVG charts plus a photo-based iceberg module. The iceberg must use a real above-water/below-water iceberg image, not a flat glacier, abstract triangle, or decorative ice background. When the image is wide enough, place it as a full-width visual anchor, put `水面上` and `水面下` explanation cards below it, and make `当前主要矛盾` a full-width long module. Markdown and DOCX can use readable text/table fallbacks.
- Mark major facts and numbers as `observed`, `estimated`, or `assumed`.
- Keep the analysis dynamic: every principal contradiction conclusion needs a reversal condition and a review point.
- Treat secondary contradictions as monitored risks, not ignored problems.
- Keep action advice narrow: 1-3 actions with owner, deadline, resource, metric, and expected effect.
- Each action should name the principal aspect it changes.
- When diagnosis confidence is sufficient, resource allocation should be deliberately tilted rather than balanced: usually 50%-70% to the principal contradiction, 10%-25% to secondary-risk containment, and 10%-20% to monitoring/evidence.
- Include probability projection as a decision-support estimate, not a promise: baseline probability, expected action uplift, risk drag, scenario probabilities, and sensitivity notes.
- Reports default to Simplified Chinese and must stay synchronized across Markdown, HTML, Word, and PDF.
- The HTML/PDF layout should follow `references/kami-layout-guide.md`: warm paper background, ink-blue accent, restrained hierarchy, compact tables, readable chart labels, no text overlap, and print-safe A4 rules.

## Reference Map

- `references/intake-and-questioning.md`: follow-up strategy and input contract
- `references/theory-anchors.md`: theory-to-rule anchors for principal contradiction, internal/external causes, principal aspect, and aggressive resource allocation
- `references/contradiction-model.md`: scoring model, principal aspect, secondary contradiction, and probability projection rules
- `references/report-contract.md`: report sections and language standard
- `references/report-export-pipeline.md`: four-format generation workflow and verification
- `references/kami-layout-guide.md`: Kami-derived layout rules for the report bundle
- `references/safety-and-boundaries.md`: high-risk and professional-boundary gates
- `reference-materials/README.md`: downloadable background research and design materials for readers
- `templates/crux-report.schema.json`: canonical input/report shape
- `scripts/generate_report_bundle.py`: JSON to Markdown, HTML, DOCX, PDF, and report JSON
- `scripts/current_state_clarity.py`: current-state clarity gate and follow-up question selector
- `scripts/verify_report_bundle.py`: generated artifact checks
