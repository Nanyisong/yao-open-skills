# Yao Open Skills

一个面向研究、决策、商业分析、学习和文档生成的公开 Skill 合集。

`OpenYao` 延续 `YAO = Yielding AI Outcomes` 这条方法线。重点不是继续堆更多 prompt 文本，而是把有效的方法、流程、评估、审美约束和执行边界沉淀成可复用的 AI 资产，并最终产生真实可交付的结果。

这个仓库收录的是已经整理成公开版本的 AI Skill。它们面向真实工作场景，比如把不确定决策整理成报告，把商业问题拆成结构化分析，把主题、资料包或参考材料生产成教程文档。

这个仓库主要承担三件事：

- 对外展示已经整理好的公开 Skill，并提供说明文档和源码入口。
- 记录每个 Skill 的收录路径、公开状态和同步状态。
- 作为后续版本迭代的发布入口，在确认更新后同步推送到 GitHub。

如果只是想找能用的 Skill，先看 [Skill 导航目录](#skill-导航目录)。如果想理解 `OpenYao` 背后的方法论，再看 [推荐入口](#推荐入口) 和 [OpenYao 理念](#openyao-理念)。

## 快速入口

- [OpenYao 理念](#openyao-理念)
- [推荐入口](#推荐入口)
- [Skill 导航目录](#skill-导航目录)
- [重点 Skill 速览](#重点-skill-速览)
- [已发布 Skill 说明](#已发布-skill-说明)
- [规划中的能力线](#规划中的能力线)
- [发布规则](docs/publishing-rules.md)
- [命名规范](docs/naming-conventions.md)
- [仓库设计](docs/repository-design.md)

## OpenYao 理念

`yao-open-skills` 想公开的不是“零散 prompt 收藏”，而是一套更稳定的 AI 资产观：

- Skill 应该服务真实任务结果，而不是只服务对话过程。
- Skill 应该可复用、可维护、可评估，而不是一次性技巧。
- Skill 应该能沉淀为团队资产，而不是停留在个人记忆和聊天记录里。
- 开源合集应该强调方法质量、边界清晰和持续演进，而不是数量堆叠。

换句话说，`OpenYao` 是把 `YAO` 的方法论往公开知识库推进一步：让那些值得分享的 Skill，不只存在于本地，而是成为可以被发现、引用、改进和复用的公开能力集合。

## 规划中的能力线

这部分展示的是 `OpenYao` 计划长期建设的能力线，风格上会尽量保持“功能导向 + 动词感”，避免命名体系散掉。

**Skill Doctor**，自动诊断并修复 Skill 中的问题。

**Skill Optimizer**，优化 Skill 的结构、执行效果和可维护性。

**Skill Ranker**，基于真实效果评估和排序 Skill。

这些名称代表的是产品方向，不等于它们现在都已经作为独立 Skill 收录进仓库。当前仓库会把“已发布能力”和“规划中的能力线”区分开维护。

## 推荐入口

如果你想理解 `OpenYao` 背后的元方法，优先看 [`yao-meta-skill`](https://github.com/yaojingang/yao-meta-skill)。

这是 `YAO` 方法线里的元 Skill 项目，用来把工作流、提示词、笔记和执行经验，进一步沉淀成可创建、可评估、可治理、可打包的 Skill 资产。

在这两个仓库之间，关系可以简单理解为：

- [`yao-meta-skill`](https://github.com/yaojingang/yao-meta-skill): 定义如何系统化地创建、评估、治理和打包 Skill
- [`yao-open-skills`](https://github.com/yaojingang/yao-open-skills): 收录那些已经值得公开分享的 Skill 成果

如果把 `yao-meta-skill` 理解成“元方法引擎”，那么 `yao-open-skills` 更像“公开产品化陈列层”。

## 仓库目标

- 把零散的本地 Skill 整理成一个稳定的公开合集。
- 为每个公开 Skill 保留清晰的来源、收录路径、同步状态和许可证信息。
- 用统一规则筛选 Skill，避免把私有数据、输出产物和实验垃圾一起推到公开仓库。
- 让 `YAO` 方法论下真正有价值的 Skill 形成一个持续演进的公开资产库。

## 公开收录标准

- 主题清晰：别人看到 Skill 名称和说明就知道它解决什么问题。
- 可复用：不依赖你个人电脑上的私有上下文才能运行。
- 可清理：能移除敏感信息、缓存、输出物、账号痕迹和内部文档。
- 可维护：你愿意继续修复、迭代和解释它。

详细规则见：

- [docs/repository-design.md](docs/repository-design.md)
- [docs/naming-conventions.md](docs/naming-conventions.md)
- [docs/publishing-rules.md](docs/publishing-rules.md)

## 目录结构

```text
yao-open-skills/
├── README.md
├── docs/
├── registry/
├── scripts/
└── skills/
```

- `docs/`: 仓库设计、发布规则、同步规范。
- `registry/`: Skill 登记表，是本地和公开状态的事实源。
- `scripts/`: 更新登记表和 README 的辅助脚本。
- `skills/`: 真正收录进公开合集的 Skill 副本。

## 已发布 Skill 说明

- [说明文档索引](docs/skills/README.md)
- [Learning Builder](docs/skills/learning-builder.md)
- [Yao Open Skills Sync](docs/skills/yao-open-skills-sync.md)
- [Yao Bayesian Skill](docs/skills/yao-bayesian-skill.md)
- [Yao Business Skill](docs/skills/yao-business-skill.md)
- [Yao Copyright Skill](docs/skills/yao-copyright-skill.md)
- [Yao Crux Skill](docs/skills/yao-crux-skill.md)
- [Yao Demand Skill](docs/skills/yao-demand-skill.md)
- [Yao Expert Skill](docs/skills/yao-expert-skill.md)
- [Yao Game Theory Skill](docs/skills/yao-gametheory-skill.md)
- [Yao Kelly Skill](docs/skills/yao-kelly-skill.md)
- [Yao Tutorial Skill](docs/skills/yao-tutorial-skill.md)
- [Yao WeRead Skill](docs/skills/yao-weread-skill.md)
- [Yao Websecurity Skill](docs/skills/yao-websecurity-skill.md)

## 重点 Skill 速览

### Yao Crux Skill

[`yao-crux-skill`](docs/skills/yao-crux-skill.md) 是一个面向复杂现实问题的主次矛盾诊断 Skill。

它会先判断用户当前现状是否足够清楚，再把看得见的问题、看不见的根部变量、主要矛盾、次要矛盾、主要方面、行动建议和结果概率组织成一份可复盘的诊断报告。

它的公开版本现在有这些比较突出的特点：

- 先做现状清晰度判断，信息不足时优先追问，不急着输出结论
- 用 `决定性`、`牵引性`、`阶段性` 解释主要矛盾判断，再用主次矛盾、第一性原理、贝叶斯式证据更新和奥卡姆剃刀辅助校验
- 区分内部可改变结构、外部硬条件，以及外因如何通过内因起作用
- 明确区分 `主要矛盾（最关键的卡点）` 和 `次要矛盾（先不主攻，但要盯住）`
- 当主要矛盾足够清楚时，更激进地把 50%-70% 高杠杆资源压到主攻线
- 每个结论都带反转条件、复盘时间和下一阶段主要矛盾可能转移的信号
- 报告包含分析流程图、照片式冰山模型、矛盾候选矩阵、资源倾斜图和动态阶段迁移图
- 默认生成 `Markdown + HTML + DOCX + PDF + report JSON`
- 公开仓库包含三个虚构业务示例和可下载参考资料，真实案例和私有输入不进入仓库

如果你想快速理解这个 Skill，建议按这个顺序看：

1. [公开说明文档](docs/skills/yao-crux-skill.md)
2. [中文目录说明](skills/yao-crux-skill/README.md)
3. [英文 README](skills/yao-crux-skill/README.en.md)
4. [Skill 入口](skills/yao-crux-skill/SKILL.md)
5. [追问与现状清晰度](skills/yao-crux-skill/references/intake-and-questioning.md)
6. [理论锚点与规则](skills/yao-crux-skill/references/theory-anchors.md)
7. [主次矛盾判断模型](skills/yao-crux-skill/references/contradiction-model.md)
8. [报告导出流程](skills/yao-crux-skill/references/report-export-pipeline.md)
9. [虚构示例报告](skills/yao-crux-skill/reports/github-examples/README.md)
10. [参考资料下载](skills/yao-crux-skill/reference-materials/README.md)

### Yao WeRead Skill

[`yao-weread-skill`](docs/skills/yao-weread-skill.md) 是一个面向微信读书数据的个人阅读可视化报告 Skill。

它会把近两年的阅读时长、阅读节律、书架资产、内容偏好和笔记语义组织成一份可直接打开的 HTML 报告。相比简单统计阅读分钟数，它更关注“你如何读书、读什么、在哪些书上留下了想法”。

它的公开版本现在有这些比较突出的特点：

- 默认生成 26 个图表模块，覆盖月度阅读、星期节律、累计阅读、读得最久的书、分类雷达、作者/出版社偏好、书架构成、笔记类型、进度散点、词云和笔记时间线
- 支持真实微信读书账号报告，也支持无需账号的 AI 创业者示例画像
- 使用 `/readdata/detail`、`/shelf/sync`、`/user/notebooks`、`/book/bookmarklist` 和 `/review/list/mine` 组合出完整数据视图
- 词云优先保留高信号领域词，并过滤常见中文分词碎片
- HTML 报告采用温暖纸面、墨蓝强调和紧凑证据卡片，适合本地浏览、截图和归档
- API Key 只从环境变量读取，真实报告默认不进入公开仓库

如果你想快速理解这个 Skill，建议按这个顺序看：

1. [公开说明文档](docs/skills/yao-weread-skill.md)
2. [目录说明](skills/yao-weread-skill/README.md)
3. [Skill 入口](skills/yao-weread-skill/SKILL.md)
4. [图表目录](skills/yao-weread-skill/references/chart-catalog.md)
5. [数据契约](skills/yao-weread-skill/references/data-contract.md)
6. [生成脚本](skills/yao-weread-skill/scripts/generate_weread_report.py)
7. [AI 创业者版示例报告](skills/yao-weread-skill/examples/ai-founder-report/weread-report.html)

### Yao Websecurity Skill

[`yao-websecurity-skill`](docs/skills/yao-websecurity-skill.md) 是一个面向授权网站、SaaS、API、AI 应用、本地代码目录和 GitHub 仓库的安全审查 Skill。

它不是简单调用扫描器，而是先理解系统代码、路由、认证、数据模型、部署配置、依赖和 AI/LLM 集成，再从 `V001-V275` 漏洞本体中筛选真正相关的检查项，最后输出可复核的安全评分表和审查报告。

它的公开版本现在有这些比较突出的特点：

- 内置 275 个网站安全检查项，覆盖访问控制、认证会话、API、XSS、CSRF、SSRF、文件上传、依赖、容器、CI/CD、数据库、缓存、AI/RAG/LLM 等风险域
- 支持 `static`、`dynamic-safe`、`dynamic-active`、`online-authorized` 和 `hybrid` 多种审查模式
- 本地代码和 GitHub 仓库都必须先复制或克隆到全新的临时目录，构建、运行、测试和报告生成都在隔离工作区内完成
- 动态主动测试按授权开关控制，盲 SSRF/OOB、暴力破解、文件变更、数据库写入和资源压力测试默认只允许在隔离临时部署内执行
- 报告默认中文，输出 `Excel + HTML + Markdown + PDF + sanitized JSON`
- HTML 支持中英切换和粘性顶部导航；Excel 使用中文状态、中文解释和工程分派友好的评分表
- 渲染前会清洗本地绝对路径、Cookie、Bearer Token、API Key、密码、私钥和长 token-like 字符串

如果你想快速理解这个 Skill，建议按这个顺序看：

1. [公开说明文档](docs/skills/yao-websecurity-skill.md)
2. [Skill 入口](skills/yao-websecurity-skill/SKILL.md)
3. [目录说明](skills/yao-websecurity-skill/README.md)
4. [审查模式](skills/yao-websecurity-skill/references/review-modes.md)
5. [报告契约](skills/yao-websecurity-skill/references/report-contract.md)
6. [漏洞本体](skills/yao-websecurity-skill/references/vulnerability-ontology.csv)
7. [报告脚本](skills/yao-websecurity-skill/scripts/security_audit_report.py)
8. [虚构示例报告](skills/yao-websecurity-skill/examples/fictional-starbridge-audit/README.md)

### Yao Tutorial Skill

[`yao-tutorial-skill`](docs/skills/yao-tutorial-skill.md) 是一个“从主题或资料包到完整教程成品”的生产型 Skill。

它不是简单帮你写一篇说明文，而是把输入主题、用户给定资料、权威来源、论文、GitHub 实践和案例证据组织成一套可交付教程包：先归一化需求，再做研究取证，再生成面向小白的章节大纲，最后输出带配图的 `Markdown + Word + PDF + HTML`。

它的公开版本现在有这些比较突出的特点：

- 支持只输入一个主题，也支持输入一组资料、链接、论文、仓库或草稿
- 优先以用户给定资料为核心，资料不足时再补充外部权威来源
- 面向新手写作，标题有用户利益，大纲说人话，章节结构通俗、可执行
- 公开成品不显示 `[U1]`、`[X1]` 这类内部证据角标，也不写“基于原文整理”
- 每个章节都必须有一张对应的可视化配图
- 配图先生成 HTML 画板，再截图嵌入教程内容
- HTML 报告支持居中内容容器、左侧目录、日期、章节跳转和清爽阅读排版
- Word/PDF 默认去掉页眉页脚，避免导出路径、页码和浏览器打印信息干扰阅读
- 内置验证脚本，检查章节、配图、引用、导出文件和本地路径泄漏

如果你想快速理解这个 Skill，建议按这个顺序看：

1. [公开说明文档](docs/skills/yao-tutorial-skill.md)
2. [Skill 入口](skills/yao-tutorial-skill/SKILL.md)
3. [输入适配规则](skills/yao-tutorial-skill/references/input-adaptation.md)
4. [教程写作规则](skills/yao-tutorial-skill/references/tutorial-outline-and-writing.md)
5. [可视化画板规则](skills/yao-tutorial-skill/references/visual-html-workflow.md)
6. [导出与验证脚本](skills/yao-tutorial-skill/scripts/validate_package.py)

### Yao Bayesian Skill

[`yao-bayesian-skill`](docs/skills/yao-bayesian-skill.md) 是当前公开合集里最完整的一类“证据到行动”型 Skill。

它的重点不是把贝叶斯定理讲一遍，而是把一个现实里的不确定问题，压缩成一个能执行、能复盘、能继续迭代的决策流程。

它的公开版本现在有这些比较突出的特点：

- 支持从不完整输入开始，先给弱先验和初步判断
- 支持多轮追问，持续更新先验、后验和决策准备度
- 内置贝叶斯先验检查，从 20 条生活判断原则中挑出本次最相关的 3 到 5 条
- 会记录每一轮对话里，哪些信息改变了判断
- 报告先给普通用户可读的结论，再展示技术细节
- 默认生成 `Markdown + 双语 HTML`
- HTML 支持中英切换、粘性导航、打印，以及在浏览器里直接存储为 PDF

如果你想快速理解这个 Skill，建议按这个顺序看：

1. [公开说明文档](docs/skills/yao-bayesian-skill.md)
2. [Skill 入口](skills/yao-bayesian-skill/SKILL.md)
3. [详细案例输入](skills/yao-bayesian-skill/input/detailed_growth_case.json)
4. [导出脚本](skills/yao-bayesian-skill/scripts/generate_report_bundle.py)
5. [示例报告目录](skills/yao-bayesian-skill/reports/README.md)

### Yao Game Theory Skill

[`yao-gametheory-skill`](docs/skills/yao-gametheory-skill.md) 是一个面向竞争、谈判、联盟、渠道、平台和竞品反击的博弈论战略报告 Skill。

它适合所有“我们的动作会引发对手反应”的场景：价格战、渠道冲突、竞品反击、平台生态、融资谈判、并购竞价、市场进入、联盟合作和监管沟通。

它不会把博弈论当成教材概念堆叠，而是把 CEO 问题转成玩家、策略、收益、时序、信号、承诺和均衡检查，重点回答：

- 对手可能怎么反应
- 我们的承诺动作是否可信
- 哪个策略在对手反应之后仍然更稳

它的设计原理是：先识别玩家、策略、收益、约束和行动时序，再路由到合适的博弈框架组合，最后把模型转成管理层能直接使用的战略报告。

它的公开版本现在有这些比较突出的特点：

- 内置框架目录和 AI 应用路由器，覆盖纳什均衡、囚徒困境、零和、协调、鹰鸽、猎鹿、进入威慑、Stackelberg、Bertrand/Cournot、信号、重复博弈、拍卖、联盟和机制设计
- 按场景组合框架，而不是机械套概念；例如价格战会组合 Bertrand、囚徒困境、重复博弈和可信承诺
- 新增真实历史行为校正层，用过往威胁兑现率、免费版投入、渠道攻击历史和经验参考来调整对手理性概率，避免高估对手的时间一致性
- 支持从不完整战略输入开始，先建立可更新的弱模型
- 对价格战、渠道冲突、平台生态、并购竞价、融资谈判、竞品免费版和监管沟通都有明确路由
- 报告前置推荐动作、对手反应地图、收益矩阵、历史行为校正、承诺可信度、策略准备度和敏感性检查
- 支持后续对手新动作并入原案例后重跑报告
- 默认生成 `Markdown + HTML + Word + PDF + canonical JSON`
- Word/PDF 宽表格已做横向页面、真实表格、固定宽度和安全换行处理

如果你想快速理解这个 Skill，建议按这个顺序看：

1. [目录说明](skills/yao-gametheory-skill/README.md)
2. [公开说明文档](docs/skills/yao-gametheory-skill.md)
3. [Skill 入口](skills/yao-gametheory-skill/SKILL.md)
4. [框架目录与 AI 路由器](skills/yao-gametheory-skill/references/framework-catalog.md)
5. [价格战示例输入](skills/yao-gametheory-skill/input/price_war_case.json)
6. [导出脚本](skills/yao-gametheory-skill/scripts/generate_report_bundle.py)
7. [示例报告目录](skills/yao-gametheory-skill/reports/README.md)

## 工作流

1. 你给出一个本地 Skill 路径。
2. 按规则判断这个 Skill 是否适合公开。
3. 清理敏感文件和无关产物后，复制到 `skills/<slug>/`。
4. 在 `registry/skills.json` 写入或更新登记信息。
5. 运行 README 渲染脚本，刷新合集说明页。
6. 如果你要发布，再把仓库推到 GitHub 的 `yao-open-skills`。

## GitHub 发布约定

- GitHub 仓库名固定为 `yao-open-skills`。
- 本地集合完成变更后，先更新 `registry/skills.json` 和 README，再执行 Git 提交与推送。
- 只有实际完成推送后，相关 Skill 才能标记为 `published`，并写入 `last_synced_at`。
- 如果后续本地源 Skill 有变化，但 GitHub 还没更新，对应记录应标记为 `needs-update`。

## 本地管理 Skill

这个仓库内置了一个管理 Skill：

- [skills/yao-open-skills-sync/SKILL.md](skills/yao-open-skills-sync/SKILL.md)

它的职责是：

- 接收你给的本地 Skill 路径。
- 判断是否适合公开。
- 按合集规则导入到 `yao-open-skills`。
- 维护登记表和 README 目录页。
- 记录这个 Skill 是否已经同步到 GitHub，以及线上对应路径。

## Skill 导航目录

<!-- catalog:start -->
这个目录从 `registry/skills.json` 自动生成，优先帮助读者判断每个 Skill 解决什么问题，以及从哪里开始阅读。

| Skill | 简体中文说明 | 主题标签 | 导航 |
| --- | --- | --- | --- |
| [Learning Builder](skills/learning-builder/SKILL.md)<br><sub>`learning-builder`</sub> | 根据学习者画像和权威资料生成个性化教程，支持 Markdown、DOCX、PDF 和可选学习网页扩展。 | `教育`、`教程`、`研究`、`导出` 等 | [说明](docs/skills/learning-builder.md) · [Skill](skills/learning-builder/SKILL.md) · [目录](skills/learning-builder) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/learning-builder) |
| [Yao Bayesian Skill](skills/yao-bayesian-skill/SKILL.md)<br><sub>`yao-bayesian-skill`</sub> | 把不确定选择转成可复盘的贝叶斯决策报告，覆盖先验设定、证据分级、后验更新、行动阈值和 Markdown/HTML 输出。 | `贝叶斯`、`决策分析`、`先验校验`、`报告` 等 | [说明](docs/skills/yao-bayesian-skill.md) · [Skill](skills/yao-bayesian-skill/SKILL.md) · [目录](skills/yao-bayesian-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-bayesian-skill) |
| [Yao Business Skill](skills/yao-business-skill/SKILL.md)<br><sub>`yao-business-skill`</sub> | 围绕商业模式设计、诊断和案例研究，输出市场环境适配、竞品分析、图表报告和 AI 时代升级建议。 | `商业模式`、`战略`、`诊断`、`竞争` 等 | [说明](docs/skills/yao-business-skill.md) · [Skill](skills/yao-business-skill/SKILL.md) · [目录](skills/yao-business-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-business-skill) |
| [Yao Copyright Skill](skills/yao-copyright-skill/SKILL.md)<br><sub>`yao-copyright-skill`</sub> | 为 Skill 包批量添加姚金刚版权注释，并避免破坏 SKILL.md frontmatter、脚本 shebang 和不适合注释的文件。 | `版权`、`Skill`、`发布`、`自动化` 等 | [说明](docs/skills/yao-copyright-skill.md) · [Skill](skills/yao-copyright-skill/SKILL.md) · [目录](skills/yao-copyright-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-copyright-skill) |
| [Yao Crux Skill](skills/yao-crux-skill/SKILL.md)<br><sub>`yao-crux-skill`</sub> | 诊断复杂局面的主次矛盾，澄清现状、识别根部变量、给出主攻行动和结果概率，并导出 Markdown、HTML、DOCX、PDF 报告。 | `决策分析`、`主要矛盾`、`诊断`、`第一性原理` 等 | [说明](docs/skills/yao-crux-skill.md) · [Skill](skills/yao-crux-skill/SKILL.md) · [目录](skills/yao-crux-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-crux-skill) |
| [Yao Demand Skill](skills/yao-demand-skill/SKILL.md)<br><sub>`yao-demand-skill`</sub> | 用需求三角模型评估产品需求，结合证据分级、短板评分、可视化诊断、情景预测和多格式报告输出。 | `需求分析`、`产品`、`验证`、`可视化报告` 等 | [说明](docs/skills/yao-demand-skill.md) · [Skill](skills/yao-demand-skill/SKILL.md) · [目录](skills/yao-demand-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-demand-skill) |
| [Yao Expert Skill](skills/yao-expert-skill/SKILL.md)<br><sub>`yao-expert-skill`</sub> | 把行业、技术、市场、角色或模糊方向整理成专家学习报告和教程，包含关键词教学卡、学习锚点、费曼自测和多格式导出。 | `专家学习`、`研究`、`行业分析`、`教程` 等 | [说明](docs/skills/yao-expert-skill.md) · [Skill](skills/yao-expert-skill/SKILL.md) · [目录](skills/yao-expert-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-expert-skill) |
| [Yao Game Theory Skill](skills/yao-gametheory-skill/SKILL.md)<br><sub>`yao-gametheory-skill`</sub> | 把竞争、谈判、渠道、定价、平台、并购、融资和监管问题转成博弈论战略报告，分析对手反应、可信承诺和策略稳健性。 | `博弈论`、`战略`、`竞争`、`谈判` 等 | [说明](docs/skills/yao-gametheory-skill.md) · [Skill](skills/yao-gametheory-skill/SKILL.md) · [目录](skills/yao-gametheory-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-gametheory-skill) |
| [Yao Kelly Skill](skills/yao-kelly-skill/SKILL.md)<br><sub>`yao-kelly-skill`</sub> | 把投资、下注或资源配置问题转成保守可执行的凯利配置方案，包含适用性判断、行动包、复盘机制和 HTML 输出。 | `凯利公式`、`资源配置`、`决策分析`、`投资` 等 | [说明](docs/skills/yao-kelly-skill.md) · [Skill](skills/yao-kelly-skill/SKILL.md) · [目录](skills/yao-kelly-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-kelly-skill) |
| [Yao Open Skills Sync](skills/yao-open-skills-sync/SKILL.md)<br><sub>`yao-open-skills-sync`</sub> | 管理 yao-open-skills 公开合集的收录、登记、同步状态、说明文档和 README 目录更新。 | `目录`、`治理`、`发布` | [说明](docs/skills/yao-open-skills-sync.md) · [Skill](skills/yao-open-skills-sync/SKILL.md) · [目录](skills/yao-open-skills-sync) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-open-skills-sync) |
| [Yao Tutorial Skill](skills/yao-tutorial-skill/SKILL.md)<br><sub>`yao-tutorial-skill`</sub> | 把主题、资料包、论文、GitHub 仓库、URL 或草稿生产成新手教程包，包含研究取证、章节配图和 Markdown、DOCX、PDF、HTML 导出。 | `教育`、`教程`、`研究`、`配图` 等 | [说明](docs/skills/yao-tutorial-skill.md) · [Skill](skills/yao-tutorial-skill/SKILL.md) · [目录](skills/yao-tutorial-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-tutorial-skill) |
| [Yao Websecurity Skill](skills/yao-websecurity-skill/SKILL.md)<br><sub>`yao-websecurity-skill`</sub> | 审查授权网站、SaaS、API、AI 应用、本地代码或 GitHub 仓库，基于 275 项漏洞本体输出中文优先的 Excel、HTML、Markdown、PDF 报告。 | `安全`、`网站安全`、`审查`、`SAST` 等 | [说明](docs/skills/yao-websecurity-skill.md) · [Skill](skills/yao-websecurity-skill/SKILL.md) · [目录](skills/yao-websecurity-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-websecurity-skill) |
| [Yao WeRead Skill](skills/yao-weread-skill/SKILL.md)<br><sub>`yao-weread-skill`</sub> | 生成微信读书个人阅读可视化报告，覆盖阅读节律、书架资产、分类偏好、笔记语义、词云和独立 HTML 输出。 | `微信读书`、`阅读分析`、`可视化`、`HTML` 等 | [说明](docs/skills/yao-weread-skill.md) · [Skill](skills/yao-weread-skill/SKILL.md) · [目录](skills/yao-weread-skill) · [GitHub](https://github.com/yaojingang/yao-open-skills/tree/main/skills/yao-weread-skill) |
<!-- catalog:end -->

## 后续约定

- `registry/skills.json` 是事实源。
- README 中的目录表由脚本生成，不手工维护。
- 任何新收录 Skill，都必须先过发布规则，再更新登记表和 README。
- 任何准备公开的变更，都应在整理完成后推送到 GitHub 远程仓库。
