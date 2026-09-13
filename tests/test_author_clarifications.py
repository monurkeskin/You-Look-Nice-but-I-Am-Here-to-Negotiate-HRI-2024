"""Author-confirmed session changes and participant-level utility exclusions."""

import json
from pathlib import Path

import pytest

from negotiator.domain.importers import from_dict
from negotiator.examples import builtin_domain
from negotiator.reproduction.operations import paired_summary

ROOT = Path(__file__).resolve().parents[1]
CONFIGS = sorted((ROOT / "configs").glob("*.json"))


def domain(value):
    return builtin_domain(value) if isinstance(value, str) else from_dict(value)


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_only_destinations_change_between_the_two_sessions(path):
    spec = json.loads(path.read_text())
    first, second = [domain(c["domain"]) for c in spec["conditions"]]
    left = {i.name: set(i.values) for i in first.issues}
    right = {i.name: set(i.values) for i in second.issues}
    assert left.pop("Destination") == {"Barcelona", "Rome", "London", "Boston"}
    assert right.pop("Destination") == {"Venice", "Lisbon", "Sydney", "Miami"}
    assert left == right
    assert left == {
        "Accommodation": {"Hotel", "Caravan", "House", "Boat"},
        "Events": {"Shopping", "Museum", "Sports", "Show"},
        "Season": {"Summer", "Winter", "Spring", "Fall"},
    }
    assert first.size == second.size == 256


@pytest.mark.parametrize("short_condition", ["NAO", "Partner"])
@pytest.mark.parametrize("offers,included", [(1, False), (2, True), (3, True)])
@pytest.mark.parametrize("cohort", ["nao-pepper", "nao-qt"])
def test_two_individual_offers_required_in_each_session(
    short_condition, offers, included, cohort
):
    schedule = json.loads((ROOT / "protocol-schedule.json").read_text())
    rule = schedule["utility_inclusion"][cohort]
    assert rule["count_unit"] == "individual-offers"
    assert rule["exclusion_unit"] == "participant-pair"
    recipe = json.loads((ROOT / "reproduction/paired-example.json").read_text())
    assert (
        recipe["parameters"]["minimum_rounds"] == rule["minimum_in_each_session"] == 2
    )
    records = [
        {
            "study_id": "synthetic-appearance",
            "participant_id": "pair-1",
            "session_id": condition,
            "condition": condition,
            "cohort": cohort,
            "domain": "same-scale",
            "rounds": offers if condition == short_condition else 3,
            "utility": 0.6,
        }
        for condition in ("NAO", "Partner")
    ]
    result = paired_summary({"records": records}, recipe["parameters"]).results
    assert result["complete_pairs"] == int(included)
    assert len(result["excluded_pairs"]) == int(not included)


def test_both_cohorts_record_the_author_confirmed_exclusion_rule():
    schedule = json.loads((ROOT / "protocol-schedule.json").read_text())
    for cohort in ("nao-pepper", "nao-qt"):
        assert schedule["utility_inclusion"][cohort]["minimum_in_each_session"] == 2
        assert "author" in schedule["utility_inclusion"][cohort]["evidence"].lower()
