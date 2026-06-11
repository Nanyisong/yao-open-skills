# Yao Demand Skill

`yao-demand-skill` 是一个面向产品、服务、SaaS、AI 工具、消费品和早期项目的需求评估 Skill。

它会把产品资料、官网、PRD、应用商店页、销售材料、截图或用户给出的描述，整理成一份基于需求三角模型的可视化诊断报告，重点回答：

> 用户是否真的缺这个东西，产品是否是可信的目标物，用户是否有能力完成采用、购买和持续使用？

## 它解决什么问题

很多产品看起来有功能、有市场、有竞品，但真实需求不一定成立。常见问题包括：

- 用户痛点存在，但不够高频或不够紧迫
- 产品承诺很强，但用户不相信它真的能解决问题
- 目标人群有需求，但价格、迁移成本、学习成本、组织阻力或信任门槛太高
- 产品把市场规模当成需求证据，缺少真实用户行为和替代方案比较
- 竞品很多，但没有解释为什么用户会从现有方案切换过来

这个 Skill 会把这些问题压进同一套需求三角框架里，形成可复核的评分、短板、10+ 图表诊断模块、验证实验、预测情景和最终方案。

## 核心模型

需求三角包含三条边：

1. **缺乏感**：用户是否存在清晰、高频、强痛感或高价值的未满足需求。
2. **目标物**：产品是否被用户理解为能缓解这个缺口，并且相对竞品、替代方案和“不购买”更可信。
3. **消费者能力**：用户是否具备预算、权限、迁移能力、学习能力、信任基础和持续使用条件。

评分使用几何短板逻辑和信心系数。也就是说，一个维度很高不能掩盖另一个维度明显塌陷；证据越弱，最终信心越低。

## 适合什么时候用

- 产品立项、孵化、投资或资源投入前做需求评估
- 官网、PRD、产品介绍、应用商店页或白皮书需要被系统诊断
- 转化率、留存、付费、激活或采用率表现不稳，需要定位需求短板
- 需要比较竞品、替代方案、用户评论和市场证据
- 需要输出一份可审阅、可归档、可分发的多格式需求评估报告

不要把它用于：

- 纯市场规模测算
- 泛商业模式设计
- 单纯 UX 可用性检查
- 广告文案创意
- 法律、医疗、金融等高风险场景里的最终建议

## 输出内容

默认输出同一份报告的四种格式：

- `Markdown`
- `HTML`
- `Word / DOCX`
- `PDF`

报告内容通常包括：

- 执行摘要和需求成立判断
- 产品与用户场景画布
- 证据清单、证据等级和反证
- 用户细分、购买角色、触发场景和采用阻力
- 需求三角评分：缺乏感、目标物、消费者能力
- 总分、信心系数、短板和红旗项
- 竞品、替代方案和“不购买”比较
- 定位、产品、定价、渠道、信任和转化建议
- 验证实验与下一步行动
- 方法说明、引用和假设清单

HTML 报告采用纯白背景，顶部置顶导航，表格溢出保护和打印样式。PDF 隐藏网页导航，保持正式报告观感。

## 可视化诊断模块

新版报告采用 `总-分-分-总` 结构：

1. 顶部先给总分、等级、最大机会、最大风险、最短板和下一步动作。
2. 中部展示至少 `10` 个图表模块，每个图表都有解读和建议。
3. 后半部分展开产品画布、用户分群、竞品、需求三角、证据、建议、实验、风险和方法。
4. 结尾给出最终判断、`30/60/90` 天行动方案、预测情景和复盘条件。

当前支持的图表模块包括：

- 总分诊断
- 需求三角雷达
- 三大维度短板
- 子项热力图
- 缺乏感细分
- 目标物细分
- 消费者能力细分
- 用户分群机会矩阵
- JTBD 强度图
- 竞品与替代方案定位
- 采用阻力漏斗
- 证据质量分布
- 风险矩阵
- 建议优先级矩阵
- 预测情景图

## 快速运行

在 Skill 目录内运行：

```bash
python3 scripts/validate_report.py reports/sample-ai-meeting-tool.report.json
python3 scripts/render_report.py reports/sample-ai-meeting-tool.report.json --outdir reports/rendered-sample --basename sample-ai-meeting-tool
```

生成文件：

```text
reports/rendered-sample/
├── sample-ai-meeting-tool.md
├── sample-ai-meeting-tool.html
├── sample-ai-meeting-tool.docx
└── sample-ai-meeting-tool.pdf
```

公开仓库保留结构化虚构示例 JSON。真实用户案例和本地生成的导出文件默认不进入公开仓库。

## 推荐阅读顺序

1. [目录说明](../../skills/yao-demand-skill/README.md)
2. [Skill 入口](../../skills/yao-demand-skill/SKILL.md)
3. [工作流程](../../skills/yao-demand-skill/references/workflow.md)
4. [证据规则](../../skills/yao-demand-skill/references/evidence-policy.md)
5. [需求三角模型](../../skills/yao-demand-skill/references/triangle-model.md)
6. [报告契约](../../skills/yao-demand-skill/references/report-contract.md)
7. [纯白报告排版](../../skills/yao-demand-skill/references/kami-white-report-layout.md)
8. [报告渲染脚本](../../skills/yao-demand-skill/scripts/render_report.py)
9. [示例报告 JSON](../../skills/yao-demand-skill/reports/sample-ai-meeting-tool.report.json)
10. [可视化诊断报告迭代方案](../../skills/yao-demand-skill/reports/visual-diagnostic-report-iteration-plan.md)
