# Yao Expert Skill

## 中文说明

`yao-expert-skill` 用来把任意行业、领域、技术、市场、角色、产品方向或模糊想法，整理成一套专家学习报告和学习教程。

它不是简单写一篇行业介绍，而是先帮用户建立领域认知结构：边界是什么、怎么分类、价值链怎么流动、谁参与、政策和技术怎么影响、哪些公司/人物/机构/案例最适合作为学习锚点、哪些关键词必须掌握、最后如何用费曼问题检验自己是否真的理解。

### 适合什么时候用

- 你想快速理解一个陌生行业或新兴领域
- 你要给新人、销售、产品、运营或管理层做领域培训
- 你正在做创业、产品、投资、战略或市场预研
- 你需要一份既能阅读、又能作为教程使用的专家学习材料
- 你希望同时输出 `Markdown`、`Word`、`PDF` 和 `HTML`
- 你需要关注 Word/PDF/HTML 的表格、边框、换行、溢出和目录体验

### 核心流程

1. 归一化输入：主题、地域、用途、受众、时间范围、深度和排除项。
2. 定义边界：先说明什么算在这个领域里，什么不算，避免后面资料口径混乱。
3. 建立结构：从分类、价值链、参与者、需求、供给、竞争、生命周期、政策、技术和资本信号展开。
4. 做证据分层：把关键判断标记为 `fact`、`inference`、`hypothesis` 或 `unknown`。
5. 生成关键词教学卡：每个关键词都有一句话通俗理解、概念阐述、底层逻辑、真实示例、应用场景、指标、误区和证据。
6. 加入学习锚点：用代表公司、人物、机构、产品、项目或场景帮助新人理解真实世界里的运作逻辑。
7. 组织学习教程：把报告转成可学习、可练习、可检查的路径。
8. 生成费曼自测：输出 10 个问题、参考答案和 `0-5` 评分标准。
9. 多格式导出：生成 `Markdown`、`Word`、`PDF` 和 `HTML`。
10. 质量验证：检查章节、摘要、表格宽度、导航、PDF 页眉页脚、本地路径和导出完整性。

### 输出物

标准输出通常包括：

```text
exports/
├── <basename>.md
├── <basename>.docx
├── <basename>.pdf
└── <basename>.html
```

报告内容通常包括：

- 导读摘要
- 默认假设与研究边界
- 一页专家速览
- 领域定义、边界与排除项
- 多口径分类地图
- 价值链、参与者与利润池
- 当前状态八维诊断
- 生命周期与变化变量
- 竞争结构、壁垒与替代风险
- 政策、标准、技术与资本信号
- 代表公司、人物、机构、案例或实践场景
- 关键词库与概念关系图
- 专家学习教程
- 费曼问题、参考答案与评分
- 机会、风险与验证清单
- 不确定性日志
- 参考资料

### 设计特点

- **结构优先**：先定边界和分类，再进入市场、竞争、案例和关键词。
- **读者友好**：每个大模块先用自然段过渡，再进入表格或矩阵。
- **关键词教学卡**：避免只给术语表，每个概念都解释“是什么、为什么、怎么用、容易错在哪”。
- **真实学习锚点**：用公司、人物、机构、产品、项目和场景帮助新人建立现实感。
- **证据和不确定性分离**：事实、推断、假设和未知不会混成一种语气。
- **四格式交付**：同一份 Markdown 源稿导出 HTML、Word 和 PDF。
- **HTML 目录体验**：固定左侧编号目录，中文锚文本保持四字短标签。
- **Word/PDF 排版检查**：表格列宽、边框、换行、溢出、PDF 导航残留和本地路径都会被检查。

### 公开案例

仓库里包含两个完整案例：

1. [中国新型储能行业专家学习报告](../../skills/yao-expert-skill/reports/examples/storage-industry-demo/storage-expert-sample.md)
2. [GEO（生成式引擎优化）中国市场专家学习报告](../../skills/yao-expert-skill/reports/examples/geo-china-demo/geo-china-expert-report.md)

每个案例都包含 `Markdown`、`HTML`、`Word` 和 `PDF` 导出文件。

### 参考材料

这个 Skill 的原始设计和理论研究文档也已收录在公开目录：

- [industry_expert_skill_design.docx](../../skills/yao-expert-skill/reference-materials/industry_expert_skill_design.docx)
- [industry_learning_deep_research_report.docx](../../skills/yao-expert-skill/reference-materials/industry_learning_deep_research_report.docx)

它们是补充阅读材料，不是 Skill 运行时必须读取的规则文件。实际执行规则仍以 `SKILL.md`、`references/`、`templates/` 和 `scripts/` 为准。

### 重要边界

不要把这个 Skill 用在：

- 一句话快速解释
- 无来源观点文
- 单纯文件格式转换
- 不需要领域结构的普通教程
- 纯商业模式诊断
- 法律、医疗、金融或安全高风险场景里的最终建议

高风险主题可以作为教育性研究处理，但必须保留来源、证据等级和不确定性说明。

## English Usage

`yao-expert-skill` turns a domain, industry, technology, market, role, product direction, or fuzzy idea into an expert learning report and tutorial.

It is built for structured domain learning rather than quick answers. The workflow defines the boundary, classifies the domain, maps the value chain and actors, separates evidence from inference, creates keyword teaching cards, adds representative real-world anchors, builds a learning path, and exports Markdown, DOCX, PDF, and HTML.

Use it when you need:

- a structured expert-learning packet from a broad topic
- a beginner-friendly but evidence-backed industry or domain report
- keyword teaching cards with examples and practical applications
- Feynman self-test questions
- polished Word, PDF, HTML, and Markdown exports
- layout checks for tables, borders, navigation, and overflow

Primary entry points:

- [Skill file](../../skills/yao-expert-skill/SKILL.md)
- [Skill README](../../skills/yao-expert-skill/README.md)
- [Domain expert method](../../skills/yao-expert-skill/references/domain-expert-method.md)
- [Report and tutorial contract](../../skills/yao-expert-skill/references/report-and-tutorial-contract.md)
- [Export and layout quality](../../skills/yao-expert-skill/references/export-and-layout-quality.md)
- [Exporter](../../skills/yao-expert-skill/scripts/export_expert_report.py)
- [Validator](../../skills/yao-expert-skill/scripts/validate_artifacts.py)
- [Examples](../../skills/yao-expert-skill/reports/examples/)
- [Reference materials](../../skills/yao-expert-skill/reference-materials/)
