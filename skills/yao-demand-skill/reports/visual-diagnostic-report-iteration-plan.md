# Yao Demand Skill 可视化诊断报告迭代方案

日期：2026-06-11

状态：待确认，不执行代码改造。

## 1. 迭代目标

把 `yao-demand-skill` 的报告从当前的“需求三角文字分析 + 两个核心模型图”，升级为一个更直观、更适合决策阅读的产品需求诊断报告。

新的报告应该做到：

- 用户输入产品资料后，能形成一份完整的需求诊断报告。
- 报告顶部先给整体判断、总分、关键风险和建议动作。
- 报告中部包含 `10` 个以上不同维度的图表模块。
- 每个图表模块都要有 `1-2` 句分析解读和 `1` 句行动建议。
- 图表模块之后保留关键文字分析：方法、底层逻辑、证据质量、建议、预测、风险、实验。
- 报告结尾回到总结性判断，给出总体方案、优先级、预测和复盘条件。
- 仍然输出 `Markdown`、`HTML`、`Word/DOCX`、`PDF` 四种格式。
- 保持纯白背景、稳定排版、表格/图表不溢出、HTML 顶部固定跟随菜单。

## 2. 自查结论

上一版方案方向成立，但还不够完整。需要补强以下几点。

| 自查点 | 原方案不足 | 本次修正 |
|---|---|---|
| 图表数量 | 只列出图表想法，没有定义数据契约 | 新增 `visual_diagnostics` 数据结构，明确图表类型、数据、洞察和建议 |
| Word 输出 | 只强调 HTML/PDF 静态 SVG，Word 可能只剩文字 | 增加 Word 图表策略：优先插入 PNG 图表，失败时降级为表格和图表解读 |
| Markdown 输出 | 只说 Mermaid/table fallback，不够具体 | 为每类图表定义 Markdown 表格/文本 fallback |
| 预测模块 | 容易产生伪精确预测 | 预测只做情景推演，必须说明假设、变量和置信度 |
| 报告结构 | “总-分-分-总”需要落到章节顺序 | 明确新报告章节和每段职责 |
| 图表渲染复杂度 | 一次性写 14 类图表可能难维护 | 用少量通用 SVG helper 支撑多种图表，不引入前端依赖 |
| 兼容旧报告 | 如果 schema 改动过大，旧样例会断 | 保留旧字段，新增字段可选，但新版 validator 可检查增强报告 |
| 验证门槛 | 只验证文件存在不够 | 增加图表数量、洞察、建议、溢出、白底、导航和四格式一致性检查 |
| 报告可读性 | 图表过多可能变成 dashboard | 图表集中放在“可视化诊断”章节，每个图表服务一个判断，不做装饰 |

## 3. 新报告叙事结构

采用 `总-分-分-总`。

### 3.1 顶部总览：先给结论

目标是让读者在前 1 分钟知道结论。

内容包括：

- 一句话判断
- 总分和等级
- 建议动作：扩张、修短板、验证、重定位、暂停
- 三角总览：缺乏感、目标物、消费者能力
- 最大机会
- 最大风险
- 最短板
- 下一步最优先动作

### 3.2 第一层分解：可视化诊断模块

目标是用图表快速呈现不同维度的诊断结果。

每个模块固定包含：

- 图表标题
- 图表
- 关键解读：`1-2` 句话
- 建议动作：`1` 句话
- 关联来源或假设
- 置信度

### 3.3 第二层分解：关键文字分析模块

目标是承接图表，解释为什么得出这些结论。

内容包括：

- 方法说明
- 需求三角底层逻辑
- 产品画布
- 目标用户与 JTBD
- 竞品和替代方案
- 证据质量和反证
- 建议和验证实验
- 风险与伦理
- 预测情景

### 3.4 结尾总括：最终方案

目标是把诊断收束成行动方案。

内容包括：

- 最终判断
- 未来 `30/60/90` 天路线
- 关键假设
- 预测情景
- 复盘条件
- 什么时候应该改变判断

## 4. 建议新增的图表模块

第一版建议做 `14` 个模块，超过用户要求的 `10` 个，同时留出筛选空间。真实报告可按资料质量输出其中至少 `10` 个。

| 序号 | 模块 | 图表类型 | 回答的问题 | 主要数据来源 |
|---:|---|---|---|---|
| 1 | 总分诊断 | 分数卡 / 仪表盘 | 这个需求整体强不强？ | `executive_summary` |
| 2 | 需求三角雷达 | 雷达图 | 三条边是否平衡？ | 三大维度分数 |
| 3 | 三大维度短板 | 横向条形图 | 哪一条边最短？ | 三大维度分数 |
| 4 | 子项热力图 | 热力图 | 哪些细项拖后腿？ | 全部 subscore |
| 5 | 缺乏感细分 | 雷达 / 条形图 | 用户缺乏感是强痛点还是弱愿望？ | `lack.subscores` |
| 6 | 目标物细分 | 雷达 / 条形图 | 产品是否被看作合适解法？ | `target_object.subscores` |
| 7 | 消费者能力细分 | 雷达 / 条形图 | 用户能不能买、用、信任、坚持？ | `consumer_ability.subscores` |
| 8 | 用户分群机会矩阵 | 二维矩阵 | 哪些用户群优先验证？ | `segments` + 评分推断 |
| 9 | 竞品与替代方案定位图 | 二维象限 | 为什么用户会从替代方案切换？ | `competitors` |
| 10 | 采用阻力漏斗 | 漏斗图 | 从知道到持续使用卡在哪里？ | adoption blockers |
| 11 | 证据质量分布 | 堆叠条 / 金字塔 | 结论靠事实还是假设？ | `evidence` |
| 12 | 风险矩阵 | 影响 x 概率矩阵 | 哪些风险最可能阻断需求？ | `risks` |
| 13 | 建议优先级矩阵 | Impact x Effort | 先做哪几个动作？ | `recommendations` |
| 14 | 预测情景图 | 三情景折线 / 区间图 | 修短板后结果可能怎样？ | `forecast` |

执行后的 HTML 优化版删除 `JTBD 强度图`，因为它与用户分群、需求三角和竞品定位的解释重复，独立诊断价值低于采用阻力漏斗、证据质量和风险矩阵。

最低要求：

- 每份正式报告至少输出 `10` 个图表模块。
- 如果资料不足，允许某些图表标记为 `low_confidence`，但不能用空图充数。
- 每个图表必须有解读和建议，否则 validator 报错。

## 5. 数据契约设计

保留当前字段：

- `executive_summary`
- `product_canvas`
- `segments`
- `competitors`
- `triangle_analysis`
- `recommendations`
- `experiments`
- `risks`
- `evidence`

新增字段：

```json
{
  "visual_diagnostics": [
    {
      "id": "triangle_radar",
      "title": "需求三角雷达图",
      "chart_type": "radar",
      "priority": 1,
      "data": {},
      "insight": "三条边中消费者能力最弱，说明当前不是没有需求，而是采用阻力偏高。",
      "recommendation": "先降低信任和组织审批成本，再扩大获客。",
      "source_ids": ["S1", "S2"],
      "confidence": 0.78
    }
  ],
  "forecast": {
    "horizon": "90 days",
    "scenarios": [
      {
        "name": "不处理短板",
        "score_after": 5.0,
        "adoption_likelihood": "low",
        "assumptions": []
      },
      {
        "name": "修复信任和合规短板",
        "score_after": 6.6,
        "adoption_likelihood": "medium",
        "assumptions": []
      },
      {
        "name": "完成强证据验证",
        "score_after": 7.4,
        "adoption_likelihood": "medium-high",
        "assumptions": []
      }
    ],
    "confidence": 0.7,
    "recheck_trigger": "如果 10 个目标客户访谈中少于 3 个愿意试用，需要重新判断缺乏感。"
  },
  "final_plan": {
    "final_judgment": "",
    "strategy": "",
    "next_30_days": [],
    "next_60_days": [],
    "next_90_days": [],
    "decision_rules": []
  }
}
```

设计原则：

- `visual_diagnostics` 是显式图表清单，避免渲染器靠猜。
- 如果 agent 没有写 `visual_diagnostics`，渲染器可以从现有字段自动生成基础图表，但 validator 会提示增强报告不完整。
- `forecast` 必须是情景推演，不允许伪装成确定性预测。
- `final_plan` 用来承接最后的“总”。

## 6. 图表渲染策略

### 6.1 HTML / PDF

采用无外部依赖的 inline SVG。

优点：

- 纯白背景可控。
- PDF 能通过 WeasyPrint 直接打印。
- 不需要 ECharts、D3 或浏览器 JS。
- 图表可以被嵌入报告，不会有外链失效。

需要新增的 SVG helper：

- `render_score_gauge_svg`
- `render_radar_svg`
- `render_bar_svg`
- `render_heatmap_svg`
- `render_matrix_svg`
- `render_funnel_svg`
- `render_stacked_bar_svg`
- `render_forecast_svg`

### 6.2 Markdown

Markdown 不能稳定承载复杂 SVG，因此使用：

- 分数卡：表格
- 雷达图：分数表 + Mermaid 简图
- 条形图：文本条形图
- 热力图：表格
- 矩阵：表格 + 象限说明
- 漏斗：Mermaid flowchart 或表格
- 预测：情景表

### 6.3 Word / DOCX

Word 是本次方案需要重点补强的地方。

推荐策略：

1. 优先将 SVG 转成 PNG，再用 `python-docx` 插入图片。
2. 如果 `cairosvg` 或图片依赖不可用，则降级为图表表格 + 解读 + 建议。
3. fallback OOXML 版本继续保持可用，但只提供表格图表等价物。

执行时需要确认环境依赖：

- `python-docx`
- `cairosvg` 或可替代的 SVG -> PNG 转换能力
- `WeasyPrint`

验收标准：

- HTML/PDF 必须有真实图表。
- Word 至少有图表等价模块；如果依赖可用，应插入 PNG 图表。
- Markdown 至少有图表等价表格和解读。

## 7. 报告章节改造

新 HTML / PDF 报告建议章节：

1. 顶部导航
2. 报告封面与总览
3. 顶部结论：总分、等级、机会、风险、最短板、下一步
4. 可视化诊断总览
5. 图表模块 1-14
6. 产品画布
7. 用户分群与 JTBD
8. 竞品与替代方案
9. 需求三角深度分析
10. 证据质量与反证
11. 建议优先级
12. 验证实验
13. 风险与伦理
14. 预测情景
15. 最终方案与复盘条件
16. 方法与附录

HTML 顶部菜单需要同步扩展为：

- 总览
- 图表
- 用户
- 竞品
- 三角
- 证据
- 建议
- 预测
- 风险
- 方案
- 附录

## 8. 验证规则

更新 `scripts/validate_report.py`。

新增检查：

- `visual_diagnostics` 至少 `10` 个模块。
- 每个图表模块必须有 `id/title/chart_type/data/insight/recommendation/confidence`。
- `chart_type` 必须属于允许列表。
- 每个图表的 `confidence` 必须是 `0-1`。
- 每个图表至少绑定 `source_ids` 或明确标记为 `assumption_based`。
- `forecast.scenarios` 至少 `3` 个：保守、修短板、强验证。
- `final_plan` 必须包含最终判断和 `30/60/90` 天动作。
- HTML/PDF 生成后至少包含 `10` 个 `.chart-module`。
- HTML 背景必须是 `#ffffff`。
- PDF 不显示 `.top-nav`。
- 不允许横向页面级 overflow。

## 9. 文档与 Skill 说明更新

需要更新：

- `SKILL.md`
  - 输出契约增加“10+ 图表诊断模块”。
- `README.md`
  - 说明新版图表化报告。
- `references/report-contract.md`
  - 写入新报告结构、图表模块契约、总-分-分-总结构。
- `references/kami-white-report-layout.md`
  - 增加图表排版、图表标题、图表说明、移动端和打印规则。
- `templates/report.schema.json`
  - 增加 `visual_diagnostics`、`forecast`、`final_plan`。
- `reports/sample-ai-meeting-tool.report.json`
  - 补完整图表模块。
- `reports/iteration-directions.md`
  - 更新迭代方向。
- `docs/skills/yao-demand-skill.md`
  - 如果同步公开仓库，需要更新公开说明。

## 10. 实施步骤

确认后建议按以下顺序执行：

1. 更新报告契约和排版参考文件。
2. 扩展 JSON schema。
3. 扩展示例报告 JSON，手工补齐 `14` 个图表模块。
4. 改造 `validate_report.py`，先让新示例通过严格校验。
5. 在 `render_report.py` 中新增通用 SVG helper。
6. 改造 HTML 渲染：新增可视化诊断章节和图表模块。
7. 改造 Markdown 渲染：新增图表等价表格和文本图。
8. 改造 Word 渲染：优先插入 PNG 图表，保留表格 fallback。
9. 改造 PDF 渲染：继续用 HTML -> PDF。
10. 渲染样例报告，检查四格式文件存在。
11. 用 Playwright 或等价方式检查 HTML 桌面/移动端。
12. 用 `pdfinfo`、截图或像素检查确认 PDF 无裁切、白底和导航残留。
13. 用 `unzip -t` 检查 DOCX 可读。
14. 更新公开仓库副本，运行校验，提交并推送。

## 11. 验收标准

功能验收：

- 同一份 report JSON 生成 `.md/.html/.docx/.pdf`。
- 至少 `10` 个图表模块出现在 HTML/PDF。
- 每个图表都有分析解读和建议。
- Markdown 有图表等价表达。
- Word 有图表或图表等价模块。
- 顶部是总览结论，底部是最终方案。
- 包含预测情景和复盘条件。

排版验收：

- HTML 和 PDF 背景为纯白。
- HTML 顶部菜单固定跟随。
- PDF 隐藏顶部菜单。
- 图表文字不裁切。
- 表格和长链接不产生页面级横向溢出。
- 移动端图表可横向滚动或稳定缩放。
- Word 表格不过窄，不出现单字纵向堆叠。

质量验收：

- `validate_skill.py` 通过。
- `validate_report.py --strict` 通过。
- evals 通过。
- PDF 可读，DOCX 可解压。
- 不提交本地生成的最终报告产物到公开仓库，除非明确需要示例输出。

## 12. 风险与控制

| 风险 | 影响 | 控制 |
|---|---|---|
| 图表太多导致报告像 dashboard | 降低正式报告质感 | 图表集中在诊断章节，之后用文字分析承接 |
| SVG helper 过多导致脚本难维护 | 后续扩展成本高 | 抽象通用坐标、颜色、标签、图例和 wrap 逻辑 |
| Word 图表插入失败 | 四格式体验不一致 | PNG 插入优先，表格 fallback 保底并显式验证 |
| 预测显得过度精确 | 误导决策 | 只输出情景、假设、置信度和复盘触发条件 |
| 旧 JSON 不兼容 | 破坏已有示例 | 新字段可选，严格模式再要求 10+ 图表 |
| PDF 图表裁切 | 影响交付质量 | 固定 viewBox、打印截图检查、移动端 overflow 检查 |

## 13. 不做的事

本轮不建议做：

- 不引入 ECharts、D3 或前端构建链。
- 不把报告做成 SaaS dashboard。
- 不把预测写成确定性增长承诺。
- 不把图表做成纯装饰。
- 不为了图表数量牺牲证据质量。
- 不把真实用户资料或本地生成报告提交到公开仓库。

## 14. 推荐决策

建议执行本方案，并采用以下边界：

- 第一版目标：`14` 个候选图表模块，正式报告至少输出 `10` 个。
- HTML/PDF：必须渲染真实静态 SVG 图表。
- Markdown：渲染图表等价表格和文本图。
- Word：优先 PNG 图表，失败时输出表格等价模块。
- 预测：只做情景推演，不做确定承诺。
- 完成后同步到 `yao-open-skills` 并推送。
