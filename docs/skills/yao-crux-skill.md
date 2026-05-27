# Yao Crux Skill

`yao-crux-skill` 是一个面向复杂现实问题的主次矛盾诊断 Skill。它的重点不是直接给结论，而是先把“当前现状”追问清楚，再判断当前阶段最该抓住的主要矛盾、需要盯住的次要矛盾，以及下一步行动的结果概率。

GitHub 目录页默认使用简体中文说明：

- [中文目录说明](../../skills/yao-crux-skill/README.md)
- [English README](../../skills/yao-crux-skill/README.en.md)

它适合这类问题：

- 事情很多，但不知道先解决哪一个
- 表面问题很多，背后的根因不明显
- 资源有限，不能所有问题同时开打
- 团队、业务、运营、增长、产品、交付或个人决策进入卡点
- 需要把分析过程整理成 Markdown、Word、HTML 和 PDF 报告

## 它解决什么问题

很多复杂局面里，用户能看到的是加班、返工、转化低、账号死亡、客户催促、流程混乱、资源不足等表面现象。但真正决定局面走向的主要矛盾，往往不在最吵的问题上，而在更上游的根部变量上。

这个 Skill 的核心工作是：

1. 先判断现状是否足够清楚。
2. 如果不清楚，先问少量关键问题，不急着下结论。
3. 把看得见的问题和看不见的根部变量分开。
4. 用 `决定性`、`牵引性`、`阶段性` 解释为什么当前先抓这个矛盾。
5. 区分内部可改变结构、外部硬条件，以及外因如何通过内因起作用。
6. 用主次矛盾、第一性原理、贝叶斯式证据更新和奥卡姆剃刀做辅助判断。
7. 输出当前阶段的主要矛盾、次要矛盾、主要方面、行动建议和结果估计。
8. 生成多格式报告，并用图表把分析过程讲清楚。

## 输出内容

完整报告通常包括：

- 先看结论
- 当前现状是否足够清楚
- 哪些是事实，哪些只是判断
- 一张图看懂：从表象到主要矛盾
- 冰山模型：看得见的问题与看不见的根部变量
- 主要矛盾判断过程：决定性、牵引性、阶段性、内因外因和候选矛盾排序
- 主要矛盾（最关键的卡点）
- 次要矛盾（先不主攻，但要盯住）
- 时间、精力、资源应该怎么重新分配：主要矛盾清楚时，默认更激进地把 50%-70% 高杠杆资源投向主攻线
- 接下来怎么做
- 做完以后可能怎样
- 主要矛盾什么时候会转移
- 什么时候回头看
- 注意事项

默认导出：

- `Markdown`
- `HTML`
- `DOCX`
- `PDF`
- `.report.json`

## 核心特点

### 1. 先追问现状，不急着诊断

Skill 内置 `current_state_clarity` 判断。它会先看目标、事实、阶段、资源、约束、利益相关方、重复模式和已尝试动作是否足够清楚。

如果信息不够，它会先问不超过 3 个关键问题，而不是直接编一个看起来完整的结论。

### 2. 把主要矛盾往上游找

报告不会简单把用户描述的问题按严重程度排序。它会问：

> 如果只能改变一个根部变量，改变什么能让多个看得见的问题一起变轻？

这使它可以识别那些“不在表面、但真正决定结果”的主导冲突。

### 3. 图表化表达分析过程

HTML/PDF 报告包含：

- 分析流程图
- 照片式冰山模型
- 矛盾候选决策矩阵
- 时间/精力/资源倾斜图
- 主要矛盾动态转移图

这些图不是装饰，而是为了帮助读者看懂为什么这个矛盾是主要矛盾，以及为什么其他矛盾暂时不主攻。

### 4. 更果断地倾斜资源

当现状足够清楚、主要矛盾判断稳定时，报告不会把资源平均分给所有问题。它会明确哪些事情要主攻、哪些事情要压缩、哪些只做止血和监控。

默认建议是把 50%-70% 的高杠杆时间、注意力、决策权和稀缺预算投向主要矛盾，同时保留少量资源盯住次要矛盾的触发条件。

### 5. 动态判断，不把结论写死

每个主要矛盾结论都要配：

- 反转条件
- 复盘时间
- 重新判断触发信号
- 下一阶段可能上升的新主要矛盾

这保证报告不是一次性断言，而是一个可以复盘和更新的判断框架。

## 快速运行

在 Skill 目录内运行：

```bash
python3 scripts/generate_report_bundle.py input/github_examples/b2b_saas_sales_conversion_case.json reports/github-examples
python3 scripts/verify_report_bundle.py reports/github-examples
```

## 公开示例

本仓库公开版本包含三个虚构业务场景：

- B2B SaaS 销售转化与线索质量
- 电商库存、现金流与 SKU 配置
- 客服交付压力与根因闭环

示例目录：

- [reports/github-examples](../../skills/yao-crux-skill/reports/github-examples)

真实用户案例、私有输入和本地过程材料不进入公开仓库。

## 推荐阅读顺序

1. [Skill 入口](../../skills/yao-crux-skill/SKILL.md)
2. [中文目录说明](../../skills/yao-crux-skill/README.md)
3. [English README](../../skills/yao-crux-skill/README.en.md)
4. [追问与现状清晰度](../../skills/yao-crux-skill/references/intake-and-questioning.md)
5. [理论锚点与规则](../../skills/yao-crux-skill/references/theory-anchors.md)
6. [主次矛盾判断模型](../../skills/yao-crux-skill/references/contradiction-model.md)
7. [报告结构契约](../../skills/yao-crux-skill/references/report-contract.md)
8. [报告导出流程](../../skills/yao-crux-skill/references/report-export-pipeline.md)
9. [虚构示例报告](../../skills/yao-crux-skill/reports/github-examples/README.md)
