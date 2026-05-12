# Yao Game Theory Skill

[English README](README.en.md)

`yao-gametheory-skill` 是一个面向竞争、谈判、渠道、平台、并购、融资、竞品反击、联盟合作和监管沟通的博弈论战略报告 Skill。

它不是博弈论教材，而是用于处理这类问题：我们的最佳动作，取决于其他玩家接下来会怎么反应。

## 适用场景

适合所有“我们的动作会引发对手反应”的战略互动场景：

- 价格战和定价应对
- 渠道冲突和渠道绑定
- 竞品反击和免费版本发布
- 平台生态规则、补贴和激励设计
- 融资谈判和商务谈判
- 并购竞价、招投标和类拍卖决策
- 市场进入和进入威慑
- 联盟合作、伙伴信任和合作机制设计
- 监管沟通和公开承诺

## 设计原理

核心设计原理很简单：

1. 识别玩家。
2. 梳理每个玩家可选的策略。
3. 估计收益、约束和风险。
4. 建模行动时序、信息、信号和承诺。
5. 路由到合适的博弈论框架组合。
6. 把模型转成管理层可直接使用的战略报告。

这个 Skill 重点回答三个问题：

- 对手可能怎么反应？
- 我们的承诺动作是否可信？
- 哪个策略在对手反应之后仍然更稳？

## 关键迭代：历史行为校正

实际跑博弈报告时有一个坑：AI 估算 payoff matrix 时容易过度简化，尤其在多轮博弈和 credible commitment 判断里，模型会倾向于高估对手的理性程度和时间一致性。

所以这个 Skill 现在要求优先输入真实历史行为数据和相关经验参考，用来校正“对手会不会真的兑现威胁/承诺”的概率。

可以输入：

- 竞品过去是否真的持续降价
- 免费版发布后是否有真实产品、预算、渠道和交付投入
- 渠道攻击是否真正兑现过返点或独家政策
- 公开威胁是否经常反转
- 同类市场、同类谈判、同类渠道冲突中的经验模式

报告会输出：

- 玩家理性概率的先验值
- 历史行为校正后的理性概率
- 历史样本和参考经验
- 对承诺可信度的历史校正评分
- 哪些结论可能来自“高估对手理性”的脆弱假设

## 处理逻辑

Skill 会先识别案例的战略结构，再组合一个主框架和若干辅助视角。

常见路由组合包括：

- 价格战：Bertrand + 囚徒困境 + 重复博弈 + 可信承诺
- 渠道冲突：联盟博弈 + 重复博弈 + 讨价还价 + 信号博弈
- 平台生态：协调博弈 + 网络效应 + 机制设计
- 并购竞价：拍卖博弈 + 讨价还价 + 信号博弈 + 赢家诅咒
- 融资谈判：讨价还价 + 信号博弈 + 外部选项 + 顺序让步
- 市场进入：进入威慑 + Stackelberg + 可信威胁 + 不完全信息
- 监管沟通：顺序博弈 + 信号博弈 + 声誉机制

框架目录覆盖：纳什均衡、零和与非零和博弈、协调博弈、鹰鸽博弈、猎鹿博弈、进入威慑、Stackelberg、Bertrand/Cournot、信号博弈、重复博弈、讨价还价、拍卖、联盟博弈和机制设计。

## 输出亮点

报告会把行动建议放在理论之前：

- 推荐动作
- 对手反应地图
- 收益矩阵
- 可信承诺检查
- 历史行为与理性概率校正
- 信号质量检查
- 可能均衡
- 策略准备度评分
- 敏感性分析
- 下一步最值得补的信息
- 后续对手动作的更新触发器

所有输出都来自同一份结构化输入，支持同步导出 `Markdown`、`HTML`、`DOCX`、`PDF` 和 canonical `JSON`。

## 快速开始

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-case
```

如果后续有新的对手动作，可以并入原案例后重新生成报告：

```bash
python3 scripts/generate_report_bundle.py input/price_war_case.json reports/price-war-refresh --update input/opponent_update.template.json
```

## 关键文件

- `SKILL.md`：Skill 入口
- `references/framework-catalog.md`：博弈论框架目录和 AI 应用路由器
- `references/game-model-playbook.md`：玩家、策略、收益、时序和均衡建模手册
- `references/commitment-signal-checklist.md`：承诺可信度和信号质量检查
- `references/dynamic-iteration-loop.md`：对手动作更新流程
- `scripts/generate_report_bundle.py`：报告生成脚本
- `reports/price-war-case.*`：示例报告产物
