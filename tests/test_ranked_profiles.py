"""Four-rank utility oracle, independently specified from the elicitation code."""

import json
from pathlib import Path

import pytest

from negotiator.application.contracts import CommandRequest, PreferencesRequest, StudySpec
from negotiator.application.studies import PhaseError, StudyStore
from negotiator.domain.preferences import ranked_preferences
from negotiator.examples import builtin_domain

ROOT = Path(__file__).resolve().parents[1]


def test_protocol_identifies_fresh_rank_elicitation_in_each_session():
    schedule = json.loads((ROOT / "protocol-schedule.json").read_text())
    assert schedule["elicitation"] == {
        "timing": "before-each-session",
        "input": "descending-issue-and-value-ranks",
        "conversion": "rank-linear-paired-v1",
        "evidence": "maintainer-clarification-and-historical-source",
    }


def test_second_session_requires_new_preferences_and_rebuilds_both_profiles(tmp_path):
    domain = builtin_domain("holiday")
    store = StudyStore(tmp_path)
    spec = StudySpec(domain="holiday", preference_mode="elicited", conditions=[{}, {}])
    pid = store.create(spec)["plan_id"]
    previous = None
    try:
        for position in (1, 2):
            state = store.snapshot(pid)
            assert state["phase"] == "preferences"
            with pytest.raises(PhaseError):
                store.start(pid)
            names = [issue.name for issue in domain.issues]
            values = {issue.name: list(issue.values) for issue in domain.issues}
            if position == 2:
                names.reverse()
                values = {name: list(reversed(ranked)) for name, ranked in values.items()}
            store.preferences(
                pid,
                PreferencesRequest(
                    request_id=f"rank-{position}",
                    phase_id=state["phase_id"],
                    issues=names,
                    values=values,
                ),
            )
            confirmed = store.snapshot(pid)
            assert confirmed["human_profile"]["weights"][names[0]] == 0.4
            assert confirmed["agent_profile"]["weights"][names[0]] == 0.3
            if previous is not None:
                assert confirmed["human_profile"] != previous["human_profile"]
                assert confirmed["agent_profile"] != previous["agent_profile"]
            previous = confirmed
            store.start(pid)
            sid = store.snapshot(pid)["current"]["config"]["session_id"]
            store.command(
                pid, CommandRequest(request_id=f"end-{position}", session_id=sid, kind="withdraw")
            )
            if position == 1:
                store.next(pid, "finish-result", store.snapshot(pid)["phase_id"])
                assert store.snapshot(pid)["break_remaining_seconds"] == 0
                store.next(pid, "next-session", store.snapshot(pid)["phase_id"])
    finally:
        store.shutdown()


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("rotation", range(4))
def test_every_holiday_outcome_uses_the_ranked_opposition_rule(reverse, rotation):
    domain = builtin_domain("holiday")
    issue_order = [issue.name for issue in domain.issues][:: -1 if reverse else 1]
    value_order = {
        issue.name: list(issue.values)[rotation:] + list(issue.values)[:rotation]
        for issue in domain.issues
    }
    human, agent = ranked_preferences(domain, issue_order, value_order)
    # Human rank weights; adjacent issue pairs swapped for the agent. Value
    # ranks are shifted by half the four-value list, not completely reversed.
    human_weights, agent_weights = (0.4, 0.3, 0.2, 0.1), (0.3, 0.4, 0.1, 0.2)
    human_scores, agent_scores = (1, 0.75, 0.5, 0.25), (0.5, 0.25, 1, 0.75)
    for bid in domain.bids():
        ranks = [value_order[name].index(bid[name]) for name in issue_order]
        expected_human = sum(w * human_scores[r] for w, r in zip(human_weights, ranks, strict=True))
        expected_agent = sum(w * agent_scores[r] for w, r in zip(agent_weights, ranks, strict=True))
        assert human.utility(bid) == pytest.approx(expected_human, abs=1e-12)
        assert agent.utility(bid, "agent") == pytest.approx(expected_agent, abs=1e-12)
