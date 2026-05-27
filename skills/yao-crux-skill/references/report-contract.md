# Report Contract

The report is a diagnostic artifact, not a philosophy essay. It should help the user decide where to focus resources in the current stage.

## Required Sections

1. `先看结论`
   - `最该先解决`
   - `为什么是它`
   - confidence in plain Chinese
   - first action
   - rough expected result after action

2. `先把现状说清楚`
   - target, stage, constraints, resources, and key facts in 3-5 sentences
   - mark important facts as observed, estimated, or assumed

3. `现状够不够清楚`
   - clarity score
   - whether it is responsible to start judging the key bottleneck
   - current-state snapshot
   - missing questions before diagnosis, phrased as ordinary questions

4. `一张图看懂：从表象到主要矛盾`
   - analysis flow chart
   - iceberg model
   - Bayesian update and Ockham razor notes
   - contradiction decision matrix
   - HTML/PDF should use inline SVG; Markdown/DOCX may use compact tables

5. `主要矛盾判断过程`
   - show how the diagnosis moved from visible symptoms to a higher-layer constraint
   - include `第一性原理`, `看得见的问题`, `上升一层`, and `看不见的根部变量`
   - explain why a visible issue is not necessarily the principal contradiction
   - explain the leading candidate with `决定性`, `牵引性`, and `阶段性`
   - separate `内部可改变结构`, `外部硬条件`, and `外因如何通过内因起作用`
   - compare 3-7 possible bottlenecks
   - keep internal `力量A 与 力量B` structure, but label the comparison column as `可能的卡点`
   - priority score and plain evidence

6. `主要矛盾（最关键的卡点）`
   - one current-stage focus
   - name it explicitly as `主要矛盾`
   - explain the `主要方面` in plain language as `现在最影响局面的一侧`
   - why to handle it first
   - what would change the judgment

7. `次要矛盾（先不主攻，但要盯住）`
   - issues not to spend main resources on yet
   - why they can wait
   - trigger for when to handle them

8. `时间、精力、资源应该怎么重新分配`
   - current vs recommended allocation
   - use time, attention, decision rights, people, money, or other scarce resources as appropriate
   - explain what to reduce, what to protect, and what to over-invest in
   - when the diagnosis is stable, the recommendation should be visibly tilted: usually 50%-70% into the principal contradiction, 10%-25% into secondary stop-loss, and 10%-20% into evidence and monitoring

9. `接下来怎么做`
   - 1-3 breakthrough actions
   - owner, deadline, resource, acceptance metric
   - what to stop or defer
   - each action should state which side of the principal contradiction or principal aspect it changes

10. `做完以后可能怎样`
   - baseline probability
   - possible help from actions
   - possible drag from risk
   - plain scenarios: status quo, recommended execution, high-quality execution, blocked execution
   - notes on what could change the estimate

11. `主要矛盾什么时候会转移`
   - current principal contradiction
   - next likely principal contradictions
   - trigger evidence for stage change

12. `什么时候回头看`
   - when to review
   - what signal means the key focus changed
   - what new evidence to collect

13. `注意事项`
   - professional review caveats for medical, legal, financial, safety, or psychological-crisis domains
   - uncertainty and assumption warnings

## Legacy Section Mapping

Older report drafts used these headings. Convert them in new reports:

- `几个可能的卡点排序` -> `主要矛盾判断过程`
- `最关键的卡点` -> `主要矛盾（最关键的卡点）`
- `先不主攻，但要盯住` -> `次要矛盾（先不主攻，但要盯住）`

## Candidate Ranking Content

Inside `主要矛盾判断过程`, still include:

   - 3-7 possible bottlenecks
   - keep internal `力量A 与 力量B` structure, but label the column as `可能的卡点`
   - priority score and plain evidence

## Language Standard

- Use concrete nouns and verbs. Avoid abstract slogans.
- Avoid over-certainty. Use `当前阶段`, `按现有证据`, `临时判断`, and `复盘条件`.
- Put the conclusion before the reasoning.
- Keep `主要矛盾` and `次要矛盾` visible because they are core concepts, but immediately translate them with practical wording such as `最关键的卡点` and `先不主攻，但要盯住`.
- Avoid standalone academic labels like `概率推演` and `监控阈值`; say `做完以后可能怎样` and `什么时候要重新判断`.
- When choosing an upstream principal contradiction, include a plain explanation of why the obvious visible problem is not the real focus.
- Explain the main judgment through `决定性`, `牵引性`, and `阶段性`; use the score table as backup evidence, not the main prose.
- Avoid using `内因` and `外因` as abstract labels only. Translate them into concrete structures such as `平台规则`, `账号存活`, `人才密度`, `决策权`, `内容质量`, `客户预算`, or `负责人注意力`.
- Use charts only when they clarify logic: no decorative charts.
- Use Bayesian/Ockham language sparingly and explain it as `用新证据修正判断` and `用更少假设解释更多现象`.
- Keep tables for comparison and scoring; use short paragraphs for judgment.
- Action advice should be small enough to do in 7-30 days unless the user supplied a longer planning horizon.
- Resource advice should not be timid when the principal contradiction is clear. Say what to stop, cap, or sharply reduce so the main line actually gets capacity.

## Minimum Useful Report

If information is incomplete, still provide:

- current-state snapshot with missing fields
- explicit statement that principal contradiction is not stable yet
- top missing evidence
- 3 follow-up questions
- a low-risk next action that produces evidence
- clear statement that exportable reports should wait until the user answers

## Four-Format Synchronization

The same canonical report JSON must drive all four formats:

- `.md`: easiest to edit and review
- `.html`: styled reading and print surface
- `.docx`: portable Word handoff
- `.pdf`: final presentation artifact

Do not manually rewrite one format after generation unless all formats are regenerated or the divergence is documented.
