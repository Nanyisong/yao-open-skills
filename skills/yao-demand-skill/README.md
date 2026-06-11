# Yao Demand Skill

`yao-demand-skill` 用来评估一个产品、服务、应用、SaaS、AI 工具或早期项目的真实需求基础，并输出可复核的需求三角报告。

它不是泛泛写市场分析，也不是只看产品体验。核心问题是：

> 用户是否真的缺这个东西，这个目标物是否能缓解缺乏感，用户是否有能力和意愿完成购买、采用或持续使用？

## 适合什么场景

- 产品上线前判断需求是否足够成立
- 投资、孵化、立项或资源投入前做需求评估
- 官网、PRD、产品介绍、应用商店页或销售材料需要被系统诊断
- 转化、留存、付费或采用受阻，需要找出需求三角里的短板
- 需要把竞品、替代方案、用户反馈和证据整理成正式报告

不适合纯 TAM/SAM/SOM 市场规模测算、泛商业模式设计、单纯 UX 走查、广告文案创意，或法律、医疗、金融等高风险场景里的最终建议。

## 底层模型

Skill 使用需求三角模型：

1. **缺乏感**：用户是否存在清晰、高频或高痛感的未满足需求。
2. **目标物**：产品是否被用户理解为能解决这个缺口，并且相对替代方案更可信。
3. **消费者能力**：用户是否具备购买、采用、迁移、学习、信任和持续使用的能力。

三项评分不会简单相加。脚本使用几何短板逻辑和信心系数，避免一个维度高分掩盖另一个维度塌陷。

## 工作流程

1. 接收产品链接、产品描述、PRD、官网文案、应用商店页、白皮书、销售材料或截图。
2. 归一化产品画布：目标用户、场景、功能、价格、承诺、商业模式、市场和关键假设。
3. 规划证据：官方资料、第三方报道、用户反馈、竞品、替代方案、价格和当前市场/监管信息。
4. 区分事实、估计、假设和建议，避免把产品自述当成市场证据。
5. 按需求三角评估缺乏感、目标物和消费者能力。
6. 输出评分、短板、反证、风险、定位建议、产品改进、定价/信任/渠道建议和验证实验。
7. 基于同一份 canonical report JSON 导出 `Markdown`、`HTML`、`Word` 和 `PDF`。

## 输出内容

标准输出包括：

- `.report.json`：结构化报告事实源
- `.md`：适合版本管理和团队协作
- `.html`：纯白背景、顶部固定跟随导航、表格溢出保护和可打印样式
- `.docx`：适合 Word 审阅和批注
- `.pdf`：适合正式归档和分发

HTML/PDF 报告采用“总-分-分-总”结构：

- 顶部先给总分、等级、最大机会、最大风险、最短板和下一步动作。
- 中部提供至少 `10` 个可视化诊断模块，包括雷达图、条形图、热力图、矩阵、漏斗、证据分布、风险矩阵、建议优先级和预测情景。
- 每个图表都有 `1-2` 句解读和 `1` 句建议。
- 后半部分保留产品画布、用户分群、竞品、需求三角深度分析、证据、建议、实验、风险和方法说明。
- 结尾给出最终判断、`30/60/90` 天行动方案、预测和复盘条件。

## 快速运行

在 Skill 目录内运行：

```bash
python3 scripts/validate_report.py reports/sample-ai-meeting-tool.report.json
python3 scripts/render_report.py reports/sample-ai-meeting-tool.report.json --outdir reports/rendered-sample --basename sample-ai-meeting-tool
```

生成结果：

```text
reports/rendered-sample/
├── sample-ai-meeting-tool.md
├── sample-ai-meeting-tool.html
├── sample-ai-meeting-tool.docx
└── sample-ai-meeting-tool.pdf
```

公开仓库默认保留结构化示例 JSON，不把本地生成的导出文件作为源码提交。

## 主要文件

- `SKILL.md`：触发规则、工作流和输出约束
- `references/workflow.md`：需求评估流程
- `references/evidence-policy.md`：证据分层、引用和时效性规则
- `references/triangle-model.md`：需求三角评分模型
- `references/report-contract.md`：报告结构契约
- `references/kami-white-report-layout.md`：纯白报告排版规则
- `templates/report.schema.json`：canonical report JSON schema
- `scripts/score_triangle.py`：三角评分计算
- `scripts/validate_report.py`：报告结构和质量校验
- `scripts/render_report.py`：可视化四格式导出
- `evals/`：触发、边界和资源引用检查

## 公开边界

公开版本只包含可复用的 Skill 本体、脚本、模板、引用规则、评估脚本和虚构示例。真实用户产品资料、本地生成的最终报告、私有设计原始文件、缓存和运行输出默认不进入公开仓库。
