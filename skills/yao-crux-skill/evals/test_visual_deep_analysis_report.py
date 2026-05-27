#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generate_report_bundle import build_report, render_html, render_markdown


def sample_report() -> dict:
    request = json.loads((ROOT / "input" / "github_examples" / "customer_support_delivery_case.json").read_text(encoding="utf-8"))
    return build_report(request)


def test_report_json_contains_visual_decision_layers() -> None:
    report = sample_report()

    assert "visuals" in report
    assert "decision_model" in report
    assert "resource_allocation" in report
    assert "stage_transition" in report
    assert len(report["visuals"].get("charts", [])) >= 5


def test_markdown_contains_deep_visual_sections_and_reasoning_gates() -> None:
    markdown = render_markdown(sample_report())

    for text in [
        "## 一张图看懂：从表象到主要矛盾",
        "冰山模型",
        "贝叶斯更新",
        "奥卡姆剃刀",
        "## 时间、精力、资源应该怎么重新分配",
        "## 主要矛盾什么时候会转移",
    ]:
        assert text in markdown


def test_html_embeds_visual_charts_and_photo_iceberg() -> None:
    html = render_html(sample_report())

    assert html.count("<svg") >= 4
    for chart_id in [
        "chart-analysis-flow",
        "chart-decision-matrix",
        "chart-resource-allocation",
        "chart-stage-transition",
    ]:
        assert f'id="{chart_id}"' in html
    assert 'id="chart-iceberg"' in html
    assert "iceberg-photo-model" in html
    assert "iceberg-waterline" in html
    assert "iceberg-card-principal" in html
    assert "<img" in html
    assert "data:image/png;base64," in html
    assert "冰山图片：仓库内置素材" in html
    assert "width: min(1080px" in html
    assert "hero-grid" in html
    assert "hero-action" in html
    assert "summary-strip" in html
    assert "chart-legend-box" in html
    assert "matrix-legend-panel" in html
    assert "matrix-legend-list" in html
    assert "stage-card" in html
    assert "水面上" in html
    assert "水面下" in html
    assert "当前主要矛盾" in html


if __name__ == "__main__":
    test_report_json_contains_visual_decision_layers()
    test_markdown_contains_deep_visual_sections_and_reasoning_gates()
    test_html_embeds_visual_charts_and_photo_iceberg()
    print("PASS: visual deep analysis report tests")
