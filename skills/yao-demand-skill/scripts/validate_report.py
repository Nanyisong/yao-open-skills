#!/usr/bin/env python3
"""Validate a Yao Demand Skill report JSON before rendering."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set


REQUIRED_TOP_LEVEL = [
    "meta",
    "executive_summary",
    "product_canvas",
    "segments",
    "triangle_analysis",
    "recommendations",
    "risks",
    "evidence",
]

REQUIRED_DIMENSIONS = ["lack", "target_object", "consumer_ability"]
ALLOWED_CHART_TYPES = {
    "score_gauge",
    "radar",
    "bar",
    "heatmap",
    "matrix",
    "funnel",
    "stacked_bar",
    "forecast",
}
SOURCE_ID_RE = re.compile(r"\bS\d+\b")


def walk_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from walk_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk_strings(item)


def score_in_range(value: Any) -> bool:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return False
    return 0 <= number <= 10


def validate_report(report: Dict[str, Any]) -> Dict[str, Any]:
    errors: List[str] = []
    warnings: List[str] = []

    for key in REQUIRED_TOP_LEVEL:
        if key not in report:
            errors.append(f"missing top-level key: {key}")

    meta = report.get("meta", {})
    for key in ["title", "product_name", "generated_at", "language"]:
        if not meta.get(key):
            errors.append(f"meta.{key} is required")

    summary = report.get("executive_summary", {})
    for key in ["total_score", "lack_score", "target_object_score", "consumer_ability_score"]:
        if key in summary and not score_in_range(summary.get(key)):
            errors.append(f"executive_summary.{key} must be 0-10")
    confidence = summary.get("evidence_confidence", 0.0)
    try:
        confidence_value = float(confidence)
        if not 0.7 <= confidence_value <= 1.0:
            errors.append("executive_summary.evidence_confidence must be 0.70-1.00")
    except (TypeError, ValueError):
        errors.append("executive_summary.evidence_confidence must be numeric")

    triangle = report.get("triangle_analysis", {})
    counter_count = 0
    for dimension in REQUIRED_DIMENSIONS:
        payload = triangle.get(dimension)
        if not isinstance(payload, dict):
            errors.append(f"triangle_analysis.{dimension} is required")
            continue
        if not score_in_range(payload.get("score")):
            errors.append(f"triangle_analysis.{dimension}.score must be 0-10")
        if not payload.get("subscores"):
            warnings.append(f"triangle_analysis.{dimension}.subscores is empty")
        if not payload.get("reasoning"):
            errors.append(f"triangle_analysis.{dimension}.reasoning is required")
        if not payload.get("improvement_path"):
            errors.append(f"triangle_analysis.{dimension}.improvement_path is required")
        counter_count += len(payload.get("counter_evidence", []) or [])

    if counter_count < 3:
        warnings.append("fewer than 3 counter-evidence items across the triangle analysis")

    evidence = report.get("evidence", [])
    evidence_ids: Set[str] = set()
    if not evidence:
        warnings.append("evidence list is empty")
    for item in evidence:
        if not isinstance(item, dict):
            errors.append("evidence entries must be objects")
            continue
        source_id = item.get("id")
        if not source_id:
            errors.append("evidence entry missing id")
        else:
            evidence_ids.add(str(source_id))
        if not item.get("title"):
            errors.append(f"evidence {source_id or '<unknown>'} missing title")
        if item.get("quality") not in {"A", "B", "C"}:
            errors.append(f"evidence {source_id or '<unknown>'} quality must be A, B, or C")

    mentioned_ids: Set[str] = set()
    for text in walk_strings(report):
        mentioned_ids.update(SOURCE_ID_RE.findall(text))
    missing_ids = sorted(mentioned_ids - evidence_ids)
    if missing_ids:
        warnings.append(f"mentioned source IDs not found in evidence list: {', '.join(missing_ids)}")

    visual_modules = report.get("visual_diagnostics")
    if visual_modules is None:
        warnings.append("visual_diagnostics is missing; formal reports should include at least 10 chart modules")
    elif not isinstance(visual_modules, list):
        errors.append("visual_diagnostics must be an array")
    else:
        if len(visual_modules) < 10:
            errors.append("visual_diagnostics must include at least 10 chart modules")
        seen_chart_ids: Set[str] = set()
        for index, module in enumerate(visual_modules, start=1):
            if not isinstance(module, dict):
                errors.append(f"visual_diagnostics[{index}] must be an object")
                continue
            chart_id = str(module.get("id") or f"index-{index}")
            if chart_id in seen_chart_ids:
                errors.append(f"duplicate visual_diagnostics id: {chart_id}")
            seen_chart_ids.add(chart_id)
            for key in ["id", "title", "chart_type", "priority", "data", "insight", "recommendation", "confidence"]:
                if key not in module or module.get(key) in ("", None, []):
                    errors.append(f"visual_diagnostics[{chart_id}].{key} is required")
            if module.get("chart_type") not in ALLOWED_CHART_TYPES:
                errors.append(f"visual_diagnostics[{chart_id}].chart_type is invalid")
            if not isinstance(module.get("data"), dict) or not module.get("data"):
                errors.append(f"visual_diagnostics[{chart_id}].data must be a non-empty object")
            try:
                confidence = float(module.get("confidence"))
                if not 0 <= confidence <= 1:
                    errors.append(f"visual_diagnostics[{chart_id}].confidence must be 0-1")
            except (TypeError, ValueError):
                errors.append(f"visual_diagnostics[{chart_id}].confidence must be numeric")
            source_ids = [str(item) for item in module.get("source_ids", []) or [] if str(item).strip()]
            if not source_ids and not module.get("assumption_based"):
                errors.append(f"visual_diagnostics[{chart_id}] must include source_ids or assumption_based=true")
            for source_id in source_ids:
                if evidence_ids and source_id not in evidence_ids:
                    warnings.append(f"visual_diagnostics[{chart_id}] references unknown evidence id: {source_id}")

    forecast = report.get("forecast")
    if forecast is None:
        warnings.append("forecast is missing; formal reports should include scenario-based forecast")
    elif not isinstance(forecast, dict):
        errors.append("forecast must be an object")
    else:
        scenarios = forecast.get("scenarios", [])
        if not isinstance(scenarios, list) or len(scenarios) < 3:
            errors.append("forecast.scenarios must include at least 3 scenarios")
        for index, scenario in enumerate(scenarios if isinstance(scenarios, list) else [], start=1):
            if not isinstance(scenario, dict):
                errors.append(f"forecast.scenarios[{index}] must be an object")
                continue
            for key in ["name", "score_after", "adoption_likelihood", "assumptions"]:
                if key not in scenario or scenario.get(key) in ("", None, []):
                    errors.append(f"forecast.scenarios[{index}].{key} is required")
            if "score_after" in scenario and not score_in_range(scenario.get("score_after")):
                errors.append(f"forecast.scenarios[{index}].score_after must be 0-10")
        try:
            forecast_confidence = float(forecast.get("confidence"))
            if not 0 <= forecast_confidence <= 1:
                errors.append("forecast.confidence must be 0-1")
        except (TypeError, ValueError):
            errors.append("forecast.confidence must be numeric")
        if not forecast.get("recheck_trigger"):
            errors.append("forecast.recheck_trigger is required")

    final_plan = report.get("final_plan")
    if final_plan is None:
        warnings.append("final_plan is missing; formal reports should include final judgment and 30/60/90 plan")
    elif not isinstance(final_plan, dict):
        errors.append("final_plan must be an object")
    else:
        for key in ["final_judgment", "strategy", "next_30_days", "next_60_days", "next_90_days", "decision_rules"]:
            if key not in final_plan or final_plan.get(key) in ("", None, []):
                errors.append(f"final_plan.{key} is required")

    if len(report.get("recommendations", []) or []) == 0:
        errors.append("at least one recommendation is required")
    if len(report.get("risks", []) or []) == 0:
        warnings.append("risk register is empty")
    if len(report.get("segments", []) or []) == 0:
        errors.append("at least one user segment is required")

    return {"ok": not errors, "errors": errors, "warnings": warnings}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a Yao Demand Skill report JSON.")
    parser.add_argument("report_json", help="Path to report JSON")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    path = Path(args.report_json).resolve()
    report = json.loads(path.read_text(encoding="utf-8"))
    result = validate_report(report)
    if args.strict and result["warnings"]:
        result["ok"] = False
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["ok"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
