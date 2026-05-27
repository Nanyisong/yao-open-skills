#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generate_report_bundle import build_report, render_markdown


def sample_report() -> dict:
    request = json.loads((ROOT / "input" / "github_examples" / "b2b_saas_sales_conversion_case.json").read_text(encoding="utf-8"))
    return build_report(request)


def test_report_contains_three_principal_contradiction_checks() -> None:
    markdown = render_markdown(sample_report())

    assert "先用三问判断是不是主要矛盾" in markdown
    assert "决定性" in markdown
    assert "牵引性" in markdown
    assert "阶段性" in markdown


def test_report_separates_internal_external_cause_path() -> None:
    markdown = render_markdown(sample_report())

    assert "内因、外因和可改变路径" in markdown
    assert "内部可改变结构" in markdown
    assert "外部硬条件" in markdown
    assert "外因如何通过内因起作用" in markdown


def test_actions_target_principal_aspect() -> None:
    report = sample_report()

    assert report["actions"]
    for action in report["actions"]:
        assert action["principal_aspect_shift"]


def test_resource_allocation_is_aggressive_when_diagnosis_allowed() -> None:
    report = sample_report()
    allocation = report["resource_allocation"]

    assert report["current_state_clarity"]["diagnosis_allowed"] is True
    assert allocation["aggressiveness"] == "aggressive"
    assert allocation["main_focus_share"] >= 50
    assert allocation["secondary_cap_share"] <= 25


if __name__ == "__main__":
    test_report_contains_three_principal_contradiction_checks()
    test_report_separates_internal_external_cause_path()
    test_actions_target_principal_aspect()
    test_resource_allocation_is_aggressive_when_diagnosis_allowed()
    print("PASS: theory anchors and aggressive allocation tests")
