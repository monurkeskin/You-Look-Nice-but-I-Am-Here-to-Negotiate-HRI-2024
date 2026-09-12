"""Paper-specific study contracts, independently executable without a robot."""

import json
from pathlib import Path
import pytest
from negotiator.application.contracts import StudySpec
from negotiator.application.protocol import (
    ordered_conditions,
    protocol_digest,
    protocol_readiness,
)

ROOT = Path(__file__).resolve().parents[1]
CONFIGS = list((ROOT / "configs").glob("protocol*.json"))


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_published_templates_pin_behavior_and_expose_unrecovered_evidence(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    assert spec.purpose == "published-protocol"
    assert spec.protocol.configuration_sha256 == protocol_digest(spec)
    assert spec.protocol.requirements
    assert protocol_readiness(spec), (
        "Historical evidence is still unrecovered; do not imply a runnable original experiment."
    )
    assert not spec.synthetic


def test_demo_is_explicit_and_device_free():
    spec = StudySpec.model_validate_json(
        (ROOT / "configs/synthetic.json").read_text(encoding="utf-8")
    )
    assert spec.purpose == "demonstration"
    assert spec.synthetic
    assert spec.output == "text"
    assert all(c.output in (None, "text", "avatar") for c in spec.conditions)
    assert not spec.speech_device and not spec.perception_device


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_appearance_cohorts_and_elicitation_are_separate(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    assert spec.preference_mode == "elicited"
    assert len(spec.conditions) == 2
    assert all(c.duration_seconds == 900 for c in spec.conditions)
    expected = {"NAO", "QT"} if spec.cohort == "nao-qt" else {"NAO", "Pepper"}
    assert {c.label for c in spec.conditions} == expected
    assert any("domain" in r.description.lower() for r in spec.protocol.requirements)
