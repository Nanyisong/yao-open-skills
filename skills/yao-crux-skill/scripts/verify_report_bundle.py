#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


REQUIRED_HTML_IDS = [
    "summary",
    "situation",
    "current-state",
    "visuals",
    "contradictions",
    "principal",
    "secondary",
    "allocation",
    "actions",
    "projection",
    "transition",
    "review",
    "risks",
]

REQUIRED_CHART_IDS = [
    "chart-analysis-flow",
    "chart-iceberg",
    "chart-decision-matrix",
    "chart-resource-allocation",
    "chart-stage-transition",
]

MOJIBAKE_PATTERNS = ["�", "å", "ä¸", "æ", "çš", "ã€"]


def run_text(command: list[str]) -> tuple[int, str, str]:
    completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return completed.returncode, completed.stdout, completed.stderr


def has_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def text_issues(label: str, text: str) -> list[str]:
    issues = []
    if not text.strip():
        issues.append(f"{label}: extracted text is empty")
    if not has_chinese(text):
        issues.append(f"{label}: no Chinese text detected")
    if "先看结论" not in text and "最该先解决" not in text:
        issues.append(f"{label}: conclusion or key focus text not detected")
    for pattern in MOJIBAKE_PATTERNS:
        if pattern in text:
            issues.append(f"{label}: possible mojibake pattern {pattern!r}")
            break
    return issues


def check_markdown(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues = text_issues(path.name, text)
    for heading in [
        "先把现状说清楚",
        "一张图看懂：从表象到主要矛盾",
        "主要矛盾判断过程",
        "先用三问判断是不是主要矛盾",
        "内因、外因和可改变路径",
        "主要矛盾（最关键的卡点）",
        "次要矛盾（先不主攻，但要盯住）",
        "时间、精力、资源应该怎么重新分配",
        "做完以后可能怎样",
        "主要矛盾什么时候会转移",
        "什么时候回头看",
        "注意事项",
    ]:
        if heading not in text:
            issues.append(f"{path.name}: missing heading {heading}")
    return issues


def check_html(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues = text_issues(path.name, text)
    if "/Users/" in text or "file://" in text:
        issues.append(f"{path.name}: contains local filesystem path")
    for anchor in REQUIRED_HTML_IDS:
        if f'id="{anchor}"' not in text:
            issues.append(f"{path.name}: missing HTML section id #{anchor}")
    for chart_id in REQUIRED_CHART_IDS:
        if f'id="{chart_id}"' not in text:
            issues.append(f"{path.name}: missing chart #{chart_id}")
    if text.count("<svg") < 4:
        issues.append(f"{path.name}: fewer than 4 SVG charts detected")
    if "iceberg-photo-model" not in text or "data:image/" not in text:
        issues.append(f"{path.name}: photo iceberg module not detected")
    if "width: min(1080px" not in text:
        issues.append(f"{path.name}: report content width is not aligned to top navigation width")
    for layout_hook in [
        "hero-grid",
        "hero-action",
        "summary-strip",
        "iceberg-waterline",
        "iceberg-card-principal",
        "chart-legend-box",
        "stage-card",
    ]:
        if layout_hook not in text:
            issues.append(f"{path.name}: missing visual layout hook {layout_hook}")
    if "冰山图片：仓库内置素材" not in text and "NOAA / USGS" not in text and "USGS Water Science School" not in text:
        issues.append(f"{path.name}: iceberg image source credit not detected")
    if "window.print" not in text:
        issues.append(f"{path.name}: print/save PDF control not detected")
    return issues


def docx_text(path: Path) -> str:
    textutil = shutil.which("textutil")
    if textutil:
        code, stdout, _ = run_text([textutil, "-convert", "txt", "-stdout", str(path)])
        if code == 0:
            return stdout
    chunks: list[str] = []
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
    for value in re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml):
        chunks.append(re.sub(r"<[^>]+>", "", value))
    return "\n".join(chunks)


def check_docx(path: Path) -> list[str]:
    if path.stat().st_size < 8_000:
        return [f"{path.name}: DOCX file is unexpectedly small"]
    try:
        text = docx_text(path)
    except Exception as exc:
        return [f"{path.name}: failed to extract DOCX text: {exc}"]
    return text_issues(path.name, text)


def check_pdf(path: Path) -> tuple[list[str], list[str]]:
    issues = []
    warnings = []
    if path.stat().st_size < 15_000:
        issues.append(f"{path.name}: PDF file is unexpectedly small")
    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        code, stdout, stderr = run_text([pdftotext, str(path), "-"])
        if code == 0:
            issues.extend(text_issues(path.name, stdout))
        else:
            issues.append(f"{path.name}: pdftotext failed: {stderr.strip()}")
    else:
        warnings.append(f"{path.name}: pdftotext unavailable; skipped text extraction")
    return issues, warnings


def check_report_json(path: Path) -> list[str]:
    try:
        report = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path.name}: invalid JSON: {exc}"]
    issues = []
    for key in [
        "summary",
        "current_state_clarity",
        "analysis_logic",
        "decision_model",
        "visuals",
        "resource_allocation",
        "stage_transition",
        "principal",
        "secondary",
        "actions",
        "projection",
        "review",
    ]:
        if key not in report:
            issues.append(f"{path.name}: missing report field {key}")
    charts = ((report.get("visuals") or {}).get("charts") or [])
    if len(charts) < 5:
        issues.append(f"{path.name}: fewer than 5 visual chart definitions")
    clarity = report.get("current_state_clarity") or {}
    if "score" not in clarity or "diagnosis_allowed" not in clarity:
        issues.append(f"{path.name}: current_state_clarity lacks score or diagnosis gate")
    logic = report.get("analysis_logic") or {}
    for key in [
        "decisiveness",
        "leverage",
        "stage_fit",
        "internal_changeable",
        "external_conditions",
        "external_through_internal",
    ]:
        if not logic.get(key):
            issues.append(f"{path.name}: analysis_logic lacks {key}")
    allocation = report.get("resource_allocation") or {}
    for key in ["aggressiveness", "main_focus_share", "secondary_cap_share", "monitoring_share"]:
        if key not in allocation:
            issues.append(f"{path.name}: resource_allocation lacks {key}")
    if float(allocation.get("main_focus_share") or 0) < 50 and clarity.get("diagnosis_allowed"):
        issues.append(f"{path.name}: main_focus_share should be aggressive when diagnosis is allowed")
    actions = report.get("actions") or []
    for idx, action in enumerate(actions, start=1):
        if not action.get("principal_aspect_shift"):
            issues.append(f"{path.name}: action {idx} lacks principal_aspect_shift")
    probability = (report.get("summary") or {}).get("recommended_probability")
    if probability is None or not (0 <= float(probability) <= 1):
        issues.append(f"{path.name}: recommended_probability is missing or outside 0..1")
    warnings = " ".join(report.get("warnings") or [])
    if report.get("case_type") in {"medical", "legal", "investment", "crisis"} and "专业" not in warnings:
        issues.append(f"{path.name}: high-risk case lacks professional-boundary warning")
    return issues


def find_bundles(output_dir: Path) -> dict[str, dict[str, Path]]:
    bundles: dict[str, dict[str, Path]] = {}
    for path in output_dir.iterdir():
        if not path.is_file():
            continue
        name = path.name
        if name.endswith(".report.json"):
            stem = name[:-12]
            kind = "json"
        elif path.suffix in {".md", ".html", ".docx", ".pdf"}:
            stem = path.stem
            kind = path.suffix[1:]
        else:
            continue
        bundles.setdefault(stem, {})[kind] = path
    return {stem: files for stem, files in bundles.items() if "json" in files}


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify generated Yao Crux report bundles.")
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    bundles = find_bundles(args.output_dir)
    issues: list[str] = []
    warnings: list[str] = []
    if not bundles:
        issues.append(f"{args.output_dir}: no report bundles found")
    for stem, files in bundles.items():
        for kind in ["json", "md", "html", "docx", "pdf"]:
            if kind not in files:
                issues.append(f"{stem}: missing {kind} artifact")
        if "json" in files:
            issues.extend(check_report_json(files["json"]))
        if "md" in files:
            issues.extend(check_markdown(files["md"]))
        if "html" in files:
            issues.extend(check_html(files["html"]))
        if "docx" in files:
            issues.extend(check_docx(files["docx"]))
        if "pdf" in files:
            pdf_issues, pdf_warnings = check_pdf(files["pdf"])
            issues.extend(pdf_issues)
            warnings.extend(pdf_warnings)
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}", file=sys.stderr)
        return 1
    print(f"PASS: verified {len(bundles)} report bundle(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
