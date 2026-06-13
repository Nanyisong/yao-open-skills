#!/usr/bin/env python3

import json
from pathlib import Path


START_MARKER = "<!-- catalog:start -->"
END_MARKER = "<!-- catalog:end -->"
MAX_VISIBLE_TAGS = 4


TAG_LABELS = {
    "ai": "AI",
    "ai-security": "AI 安全",
    "allocation": "资源配置",
    "audit": "审查",
    "automation": "自动化",
    "bayesian": "贝叶斯",
    "business-model": "商业模式",
    "catalog": "目录",
    "charts": "图表",
    "competition": "竞争",
    "copyright": "版权",
    "dast": "DAST",
    "decision-analysis": "决策分析",
    "demand-analysis": "需求分析",
    "diagnosis": "诊断",
    "docx": "DOCX",
    "education": "教育",
    "evidence": "证据",
    "excel": "Excel",
    "expert-learning": "专家学习",
    "export": "导出",
    "first-principles": "第一性原理",
    "forecast": "预测",
    "game-theory": "博弈论",
    "governance": "治理",
    "headers": "文件头",
    "historical-behavior": "历史行为",
    "html": "HTML",
    "industry-analysis": "行业分析",
    "investment": "投资",
    "kelly": "凯利公式",
    "keywords": "关键词",
    "negotiation": "谈判",
    "notes": "笔记",
    "pdf": "PDF",
    "personalization": "个性化",
    "principal-contradiction": "主要矛盾",
    "product": "产品",
    "prior-hygiene": "先验校验",
    "publishing": "发布",
    "reading-analytics": "阅读分析",
    "reporting": "报告",
    "research": "研究",
    "sast": "SAST",
    "security": "安全",
    "skills": "Skill",
    "strategy": "战略",
    "tutorials": "教程",
    "validation": "验证",
    "visual-reporting": "可视化报告",
    "visualization": "可视化",
    "visuals": "配图",
    "web-security": "网站安全",
    "weread": "微信读书",
    "word-cloud": "词云",
    "workflow": "工作流",
}


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def format_tags(tags):
    labels = [TAG_LABELS.get(tag, tag) for tag in tags]
    visible = labels[:MAX_VISIBLE_TAGS]
    if not visible:
        return "未标注"
    rendered = "、".join(f"`{label}`" for label in visible)
    return f"{rendered} 等" if len(labels) > MAX_VISIBLE_TAGS else rendered


def format_nav(skill):
    links = []
    if skill.get("guide_path"):
        links.append("[说明]({path})".format(path=skill["guide_path"]))
    links.append("[Skill]({path}/SKILL.md)".format(path=skill["collection_path"]))
    links.append("[目录]({path})".format(path=skill["collection_path"]))
    if skill.get("github_url"):
        links.append("[GitHub]({url})".format(url=skill["github_url"]))
    return " · ".join(links)


def render_table(skills):
    lines = [
        START_MARKER,
        "这个目录从 `registry/skills.json` 自动生成，优先帮助读者判断每个 Skill 解决什么问题，以及从哪里开始阅读。",
        "",
        "| Skill | 简体中文说明 | 主题标签 | 导航 |",
        "| --- | --- | --- | --- |",
    ]

    for skill in skills:
        summary = escape_table_cell(skill["summary"])
        lines.append(
            "| [{title}]({collection_path}/SKILL.md)<br><sub>`{slug}`</sub> | {summary} | {tags} | {nav} |".format(
                title=skill["title"],
                slug=skill["slug"],
                collection_path=skill["collection_path"],
                summary=summary,
                tags=format_tags(skill.get("tags", [])),
                nav=format_nav(skill),
            )
        )

    lines.append(END_MARKER)
    return "\n".join(lines)


def main():
    repo_root = Path(__file__).resolve().parents[1]
    registry_path = repo_root / "registry" / "skills.json"
    readme_path = repo_root / "README.md"

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    skills = sorted(registry.get("skills", []), key=lambda item: item["slug"])
    table = render_table(skills)

    readme = readme_path.read_text(encoding="utf-8")
    if START_MARKER not in readme or END_MARKER not in readme:
        raise SystemExit("README catalog markers not found.")

    start = readme.index(START_MARKER)
    end = readme.index(END_MARKER) + len(END_MARKER)
    updated = readme[:start] + table + readme[end:]
    readme_path.write_text(updated, encoding="utf-8")
    print(f"Rendered catalog for {len(skills)} skill(s).")


if __name__ == "__main__":
    main()
