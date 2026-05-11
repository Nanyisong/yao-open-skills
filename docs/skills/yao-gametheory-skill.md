# Yao Game Theory Skill

`yao-gametheory-skill` 用来把竞争、谈判、联盟、渠道、平台、并购竞价、融资谈判、竞品反击和监管沟通问题，转成一份可执行、可复盘、可继续更新的博弈论战略报告。

它的重点不是讲授博弈论概念，而是回答两个 CEO 真正关心的问题：

- 对手可能怎么反应
- 我们的承诺动作是否可信

当前公开版本默认输出：

- `Markdown`：适合版本管理和团队协作
- `HTML`：适合浏览、分享和打印
- `DOCX`：适合 Word 审阅和批注
- `PDF`：适合正式分发
- `JSON`：保留结构化模型，方便后续加入对手新动作后重跑

## 这个 Skill 最适合做什么

适合存在明确战略互动方的问题：

- 价格战：是否降价、是否跟随、是否转向差异化
- 渠道冲突：是否绑定渠道、如何判断竞品渠道攻击
- 平台生态：规则、补贴、标准和多边参与者反应
- 并购竞价：竞价节奏、信号、赢家诅咒和退出条件
- 融资谈判：估值、条款、BATNA 和让步顺序
- 竞品反击：免费版本、价格跟随、渠道攻击、舆论信号
- 监管沟通：公开承诺、合规姿态和长期声誉

它不适合纯教材问答、数学证明、赌博建议、没有战略对手的泛泛头脑风暴，或替代正式法律、投资、反垄断和监管意见。

## 核心亮点

### 1. 内置博弈论框架库和 AI 应用路由器

`references/framework-catalog.md` 把常见框架整理成可路由目录，包括：

- 纳什均衡
- 囚徒困境
- 零和与非零和博弈
- 协调博弈
- 鹰鸽博弈
- 猎鹿博弈
- 进入威慑
- Stackelberg
- Bertrand / Cournot
- 信号博弈
- 重复博弈
- 讨价还价
- 拍卖和竞价
- 联盟博弈
- 机制设计

每个框架都按“何时使用、玩家结构、典型 CEO 场景、输出检查项”组织。Skill 会先识别战略结构，再选择一个主框架和 2 到 4 个辅助视角，而不是看到关键词就套一个名词。

### 2. 把对手反应放在报告前部

报告不是先讲理论，而是先给：

- 推荐动作
- 对手反应概率
- 可能均衡
- 我们承诺动作的可信度
- 结论成立的关键前提

这让报告更适合管理层阅读，也更容易转成会议讨论材料。

### 3. 支持动态更新

如果后续对手有新动作，例如：

- 竞品正式发布免费版
- 渠道拒绝合作包
- 对方公开长期降价承诺
- 监管方释放新信号

可以用 `--update` 把新信息并入原始案例，重跑报告。输出会更新反应概率、payoff、承诺可信度、策略准备度和更新日志。

### 4. 借鉴了 Bayesian Skill 的长任务设计

这个 Skill 借鉴了 `yao-bayesian-skill` 的几个工程亮点：

- 不完整信息也能先建立弱模型
- 用 readiness score 区分“当前建议”和“是否足够成熟”
- 做敏感性分析，检查结论是否依赖脆弱假设
- 明确下一步最值得补的信息
- 记录每一轮更新如何改变判断
- 多格式报告来自同一份结构化输入

### 5. 修复宽表格导出问题

Word 和 PDF 不是从 Markdown 粗暴转换。当前导出脚本会：

- 用真实 Word 表格生成 DOCX
- 对宽表格使用横向页面和紧凑列宽
- HTML/PDF 打印使用 A4 landscape
- 表格单元格自动换行
- 长中文、英文标识符和混合标签可安全断行

## 典型工作流

1. 用 `references/intake-contract.md` 把用户问题整理成战略 brief。
2. 用 `references/framework-catalog.md` 选择主框架和辅助框架。
3. 用 `references/game-model-playbook.md` 建立玩家、策略、收益、时序、信念和均衡逻辑。
4. 用 `references/commitment-signal-checklist.md` 检查承诺和信号是否可信。
5. 用 `references/strategy-readiness-loop.md`、`references/strategic-hygiene-checklist.md` 和 `references/sensitivity-and-safety.md` 做准备度、假设卫生和敏感性检查。
6. 用 `scripts/generate_report_bundle.py` 生成 Markdown、HTML、DOCX、PDF 和 canonical JSON。

## 快速运行

在 Skill 目录内运行：

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-case
```

加入对手后续动作后重新导出：

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-refresh --update input/opponent_update.template.json
```

## 示例报告

公开副本包含一个价格战示例：

- [Markdown 示例](../../skills/yao-gametheory-skill/reports/price-war-case.md)
- [HTML 示例](../../skills/yao-gametheory-skill/reports/price-war-case.html)
- [Word 示例](../../skills/yao-gametheory-skill/reports/price-war-case.docx)
- [PDF 示例](../../skills/yao-gametheory-skill/reports/price-war-case.pdf)
- [Canonical JSON](../../skills/yao-gametheory-skill/reports/price-war-case.canonical.json)

这个示例的推荐结论是：避免进入低质量价格战，优先采用渠道绑定和高端差异化组合，并持续观察竞品免费版本是否有真实产品、预算和渠道分发能力。

## 关键文件

- [Skill 入口](../../skills/yao-gametheory-skill/SKILL.md)
- [框架目录与 AI 路由器](../../skills/yao-gametheory-skill/references/framework-catalog.md)
- [博弈建模手册](../../skills/yao-gametheory-skill/references/game-model-playbook.md)
- [动态更新循环](../../skills/yao-gametheory-skill/references/dynamic-iteration-loop.md)
- [承诺与信号检查](../../skills/yao-gametheory-skill/references/commitment-signal-checklist.md)
- [导出规范](../../skills/yao-gametheory-skill/references/report-export-pipeline.md)
- [导出脚本](../../skills/yao-gametheory-skill/scripts/generate_report_bundle.py)

