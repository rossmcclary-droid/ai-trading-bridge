"""Versioned Trading Brain configuration metadata.

Bootstrap v2 rules are intentionally not included yet. This module provides
the stable container into which the approved rule set can be loaded later.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict

Grade = Literal["A+", "A", "A-", "B+", "WATCH", "REJECT"]


class GradingOverride(BaseModel):
    """Permanent grading policy for executable trade proposals."""

    model_config = ConfigDict(frozen=True)

    grades: tuple[Grade, ...] = ("A+", "A", "A-", "B+", "WATCH", "REJECT")
    minimum_executable_grade: Literal["B+"] = "B+"


class StrategyMetadata(BaseModel):
    """Bootstrap lineage metadata without strategy rules."""

    model_config = ConfigDict(frozen=True)

    supersedes: str = "AI Trading Bridge Strategy Bootstrap v1"
    inheritance: str = (
        "Inherits v1 operational rules except where v2 explicitly supersedes them."
    )


class TradingBrainConfig(BaseModel):
    """Active versioned Trading Brain configuration."""

    model_config = ConfigDict(frozen=True)

    bootstrap_name: Literal["AI Trading Bridge Strategy Bootstrap v2"] = (
        "AI Trading Bridge Strategy Bootstrap v2"
    )
    version: Literal["research_integrated_2026-08-24"] = (
        "research_integrated_2026-08-24"
    )
    grading_override: GradingOverride = GradingOverride()
    metadata: StrategyMetadata = StrategyMetadata()
    full_strategy_rules_loaded: bool = False
    full_strategy_rules: None = None


active_strategy = TradingBrainConfig()
# Load and validate the permanent grading override.
import json
from pathlib import Path

_GRADING_OVERRIDE_PATH = (
    Path(__file__).resolve().parent.parent
    / "brain"
    / "grading_override.json"
)

with _GRADING_OVERRIDE_PATH.open("r", encoding="utf-8") as _f:
    _grading_override_data = json.load(_f)

_loaded_grading_override = GradingOverride.model_validate(
    {
        "grades": tuple(_grading_override_data["grades"]),
        "minimum_executable_grade": _grading_override_data[
            "minimum_executable_grade"
        ],
    }
)

active_strategy = active_strategy.model_copy(
    update={"grading_override": _loaded_grading_override}
)

_BOOTSTRAP_V2_PATH = (
    Path(__file__).resolve().parent.parent
    / "brain"
    / "bootstrap_v2.md"
)

with _BOOTSTRAP_V2_PATH.open("r", encoding="utf-8") as _f:
    _bootstrap_v2_rules = _f.read()

if not _bootstrap_v2_rules.strip():
    raise ValueError("bootstrap_v2.md is empty")

if "PART I — HUMAN-READABLE STRATEGY" not in _bootstrap_v2_rules:
    raise ValueError("bootstrap_v2.md is missing PART I")

if "PART II — MACHINE-READABLE BOOTSTRAP" not in _bootstrap_v2_rules:
    raise ValueError("bootstrap_v2.md is missing PART II")

active_strategy = active_strategy.model_copy(
    update={
        "full_strategy_rules_loaded": True,
        "full_strategy_rules": _bootstrap_v2_rules,
    }
)
