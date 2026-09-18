"""Conservative candidate ranking for AI Trading Bridge."""

from typing import Any


STATE_SCORE = {
    "reconverging": 5,
    "aligned": 4,
    "pulling_back": 3,
    "transitioning": 2,
    "conflicted": 0,
}

DECISION_SCORE = {
    "APPROVED ACTIVE TRADE": 6,
    "PENDING TRADE": 5,
    "ALERT ONLY": 4,
    "WATCH": 2,
    "REJECT": 0,
}


def score_analysis(result: dict[str, Any]) -> dict[str, Any]:
    """Score a classified setup without overriding its decision."""

    score = 0
    reasons: list[str] = []

    state = result.get("multi_horizon_state")
    decision = result.get("decision")

    score += STATE_SCORE.get(state, 0) * 10
    score += DECISION_SCORE.get(decision, 0) * 10

    if result.get("directional_bias") in {"bullish", "bearish"}:
        score += 8
        reasons.append("directional_bias")

    trade_plan = result.get("trade_plan", {})

    if trade_plan.get("valid"):
        score += 15
        reasons.append("valid_trade_geometry")

    execution = result.get("execution_5m", {})

    if execution.get("confirmed"):
        score += 20
        reasons.append("5m_execution_confirmed")

    geometry = result.get("geometry", {})

    if geometry.get("entry_quality") == "efficient":
        score += 10
        reasons.append("efficient_entry")
    elif geometry.get("entry_quality") == "acceptable":
        score += 5
        reasons.append("acceptable_entry")

    context = result.get("execution_context", {})

    if context.get("extension") == "normal":
        score += 5
        reasons.append("not_extended")
    elif context.get("extension") in {"extended", "highly_extended"}:
        score -= 10
        reasons.append("extension_penalty")

    if result.get("setup_grade") == "REJECT":
        score = 0

    return {
        "symbol": result["symbol"],
        "score": score,
        "grade": result["setup_grade"],
        "decision": result["decision"],
        "state": state,
        "bias": result["directional_bias"],
        "score_reasons": reasons,
        "analysis": result,
    }


def rank_candidates(
    analyses: list[dict[str, Any]],
    *,
    limit: int = 3,
) -> list[dict[str, Any]]:
    """Return up to the strongest qualifying candidates."""

    ranked = [
        score_analysis(result)
        for result in analyses
        if result.get("setup_grade") != "REJECT"
    ]

    ranked.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return ranked[:limit]
