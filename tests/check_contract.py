#!/usr/bin/env python3
"""Static contract checks for the SaaS Growth Diagnosis skill."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


text = SKILL.read_text(encoding="utf-8")
require(text.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
require("name: saas-growth-diagnosis" in text, "skill name is missing")
require("description:" in text, "skill description is missing")
require("Never guarantee a 2–3× lift" in text, "outcome-guarantee guardrail is missing")
require("Never withhold a useful conclusion" in text, "handoff trust boundary is missing")
require("Discover before asking" in text, "agent-first discovery rule is missing")
require("Never send a form" in text, "questionnaire guardrail is missing")
require("Analytics code is not analytics data" in text, "code-versus-behavior boundary is missing")
require("Pre-launch readiness" in text, "pre-launch route is missing")

for target in re.findall(r"\]\((references/[^)]+\.md)\)", text):
    require((ROOT / target).is_file(), f"referenced file does not exist: {target}")

ui = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
require("$saas-growth-diagnosis" in ui, "default prompt must mention the skill")

all_text = "\n".join(
    path.read_text(encoding="utf-8")
    for path in ROOT.rglob("*")
    if path.is_file() and path.suffix in {".md", ".yaml"}
)
require(not re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", all_text), "unfinished placeholder found")

cases = (ROOT / "tests" / "cases.md").read_text(encoding="utf-8")
require(cases.count("## Case ") >= 8, "expected at least eight behavioral cases")
require("near-neighbor request outside scope" in cases, "missing scope-boundary case")
require("high-consideration enterprise boundary" in cases, "missing benchmark-boundary case")
require("repository-first discovery" in cases, "missing repository-discovery case")
require("pre-launch product" in cases, "missing pre-launch case")

smoke = (ROOT / "tests" / "smoke-output-case-1.md").read_text(encoding="utf-8")
require("800 / 20,000 = 4%" in smoke, "smoke output misses signup calculation")
require("120 / 800 = 15%" in smoke, "smoke output misses activation calculation")
require("18 / 300 = 6%" in smoke, "smoke output misses trial-to-paid calculation")
require("最早、最明确的卡点是激活" in smoke, "smoke output picks the wrong primary bottleneck")
require("暂时不要用折扣" in smoke, "smoke output misses the downstream-action guardrail")
require("付费深度诊断" not in smoke, "smoke output adds an unnecessary commercial handoff")

print("PASS: static contract checks")
