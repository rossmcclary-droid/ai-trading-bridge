"""Read-only market scan routes."""

import time

from fastapi import APIRouter, HTTPException, Query

from app.account_manager import AccountManager
from app.services.analysis import analyze_scan, derive_alert_level, derive_alert_levels, derive_alert_levels
from app.services.ranker import rank_candidates
from app.services.scanner import ScannerService
from app.services.tradability_interlock import verify_symbol_tradable_on_account
from app.services.market_session import default_tradable_symbols, weekend_crypto_only


router = APIRouter()

DEFAULT_SYMBOLS = [
    "XAUUSD",
    "BTCUSD",
    "EURUSD",
    "GBPUSD",
    "USDJPY",
]


@router.get("/scan/{nickname}")
async def scan_account(
    nickname: str,
    symbols: list[str] | None = Query(default=None),
):
    manager = AccountManager()
    account = manager.get_account(nickname)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail=f"Account {nickname!r} not found.",
        )

    if not account.external_account_id:
        raise HTTPException(
            status_code=400,
            detail="Account has no external account ID.",
        )

    if not account.external_account_number:
        raise HTTPException(
            status_code=400,
            detail="Account has no external account number.",
        )

    requested_symbols = (
        symbols
        if symbols
        else default_tradable_symbols(DEFAULT_SYMBOLS)
    )

    if len(requested_symbols) > 10:
        raise HTTPException(
            status_code=400,
            detail="A scan may contain no more than 10 symbols.",
        )

    scanner = ScannerService()

    batch = await scanner.scan_symbols(
        symbols=requested_symbols,
        account_id=int(account.external_account_id),
        broker_crypto_only=(
            symbols is None and weekend_crypto_only()
        ),
        acc_num=account.external_account_number,
    )

    analyses = [
        analyze_scan(scan)
        for scan in batch["results"].values()
    ]

    ranked = rank_candidates(
        analyses,
        limit=3,
    )

    return {
        "account": account.nickname,
        "requested": batch["requested"],
        "successful": batch["successful"],
        "failed": batch["failed"],
        "errors": batch["errors"],
        "candidates": ranked,
        "analyses": analyses,
    }


@router.get("/scan/{nickname}/summary")
async def scan_account_summary(
    nickname: str,
    symbols: list[str] | None = Query(default=None),
):
    manager = AccountManager()
    account = manager.get_account(nickname)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail=f"Account {nickname!r} not found.",
        )

    if not account.external_account_id:
        raise HTTPException(
            status_code=400,
            detail="Account has no external account ID.",
        )

    if not account.external_account_number:
        raise HTTPException(
            status_code=400,
            detail="Account has no external account number.",
        )

    requested_symbols = (
        symbols
        if symbols
        else default_tradable_symbols(DEFAULT_SYMBOLS)
    )

    if len(requested_symbols) > 10:
        raise HTTPException(
            status_code=400,
            detail="A scan may contain no more than 10 symbols.",
        )

    scanner = ScannerService()

    batch = await scanner.scan_symbols(
        symbols=requested_symbols,
        account_id=int(account.external_account_id),
        broker_crypto_only=(
            symbols is None and weekend_crypto_only()
        ),
        acc_num=account.external_account_number,
    )

    analyses = [
        analyze_scan(scan)
        for scan in batch["results"].values()
    ]

    ranked = rank_candidates(
        analyses,
        limit=3,
    )

    candidates = []

    for item in ranked:
        analysis = item["analysis"]
        plan = analysis["trade_plan"]
        execution = analysis["execution_5m"]

        candidates.append(
            {
                "symbol": item["symbol"],
                "score": item["score"],
                "grade": item["grade"],
                "decision": item["decision"],
                "bias": item["bias"],
                "state": item["state"],
                "trade_plan_valid": plan["valid"],
                "safe_loss": plan["safe_loss"],
                "tp1": plan["tp1"],
                "tp2": plan["tp2"],
                "rr_tp1": plan["rr_tp1"],
                "rr_tp2": plan["rr_tp2"],
                "5m_confirmed": execution["confirmed"],
                "reason": analysis["reason"],
            }
        )

    return {
        "account": account.nickname,
        "requested": batch["requested"],
        "successful": batch["successful"],
        "failed": batch["failed"],
        "errors": batch["errors"],
        "top_candidates": candidates,
    }


@router.get("/scan/{nickname}/trading-summary")
async def scan_trading_summary(
    nickname: str,
    symbols: list[str] | None = Query(default=None),
):
    """Return a compact trading-workflow view of the live scan."""

    manager = AccountManager()
    account = manager.get_account(nickname)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail=f"Account {nickname!r} not found.",
        )

    if not account.external_account_id:
        raise HTTPException(
            status_code=400,
            detail="Account has no external account ID.",
        )

    if not account.external_account_number:
        raise HTTPException(
            status_code=400,
            detail="Account has no external account number.",
        )

    requested_symbols = (
        symbols
        if symbols
        else default_tradable_symbols(DEFAULT_SYMBOLS)
    )

    if len(requested_symbols) > 10:
        raise HTTPException(
            status_code=400,
            detail="A scan may contain no more than 10 symbols.",
        )

    scanner = ScannerService()

    batch = await scanner.scan_symbols(
        symbols=requested_symbols,
        account_id=int(account.external_account_id),
        broker_crypto_only=(
            symbols is None and weekend_crypto_only()
        ),
        acc_num=account.external_account_number,
    )

    scan_by_symbol = batch["results"]

    analyses = {
        symbol: analyze_scan(scan)
        for symbol, scan in scan_by_symbol.items()
    }

    ranked = rank_candidates(
        list(analyses.values()),
        limit=10,
    )

    executable_orders = []
    alerts = []
    watchlist = []

    for ranked_item in ranked:
        symbol = ranked_item["symbol"]
        analysis = analyses[symbol]
        scan = scan_by_symbol[symbol]

        plan = analysis["trade_plan"]

        if (
            analysis["setup_grade"] == "B+"
            and analysis["decision"] == "APPROVED ACTIVE TRADE"
            and plan["valid"]
        ):
            executable_orders.append(
                {
                    "order_type": "Active",
                    "instrument": symbol,
                    "entry": plan["entry_reference"],
                    "safe_loss": plan["safe_loss"],
                    "take_profit_1": plan["tp1"],
                    "take_profit_2": plan["tp2"],
                    "take_profit_3": plan["tp3"],
                    "grade": analysis["setup_grade"],
                    "reason": analysis["reason"],
                }
            )
            continue

        candidate_alerts = derive_alert_levels(
            scan,
            bias=analysis["directional_bias"],
            state=analysis["multi_horizon_state"],
        )

        appended_alert = False

        if analysis["decision"] in {"WATCH", "ALERT ONLY"}:
            for alert in candidate_alerts:
                if len(alerts) >= 6:
                    break

                if alert["alert_level"] is None:
                    continue

                alerts.append(
                    {
                        "instrument": symbol,
                        "alert_level": alert["alert_level"],
                        "meaning": alert["meaning"],
                        "alert_type": alert["alert_type"],
                        "grade": analysis["setup_grade"],
                        "state": analysis["multi_horizon_state"],
                        "bias": analysis["directional_bias"],
                    }
                )
                appended_alert = True

        if not appended_alert:
            watchlist.append(
                {
                    "instrument": symbol,
                    "grade": analysis["setup_grade"],
                    "decision": analysis["decision"],
                    "state": analysis["multi_horizon_state"],
                    "bias": analysis["directional_bias"],
                    "reason": analysis["reason"],
                }
            )

    top_candidate = None

    if ranked:
        top = ranked[0]
        top_analysis = top["analysis"]

        geometry = top_analysis["geometry"]
        context = top_analysis["execution_context"]
        execution = top_analysis["execution_5m"]
        timeframes = top_analysis["timeframes"]

        current_price = (
            timeframes.get("5M", {}).get("last_price")
            or timeframes.get("15M", {}).get("last_price")
        )

        next_conditions = []
        satisfied_conditions = []

        if geometry["entry_quality"] == "late":
            next_conditions.append("Wait for a better entry or controlled pullback.")
        else:
            satisfied_conditions.append("Entry location is acceptable.")

        if (
            geometry["reward_to_risk"] is not None
            and geometry["reward_to_risk"] < 1
        ):
            next_conditions.append(
                "Reward-to-risk must improve before approval."
            )
        else:
            satisfied_conditions.append(
                "Reward-to-risk is not currently a blocker."
            )

        if not execution["confirmed"]:
            next_conditions.append(
                "Wait for 5M execution confirmation."
            )
        else:
            satisfied_conditions.append(
                "5M execution confirmation is satisfied."
            )

        if context["extension"] in {"extended", "highly_extended"}:
            next_conditions.append(
                "Wait for price extension to normalize."
            )
        else:
            satisfied_conditions.append(
                "Price is not excessively extended."
            )

        if top["state"] == "transitioning":
            next_conditions.append(
                "Wait for stronger multi-horizon alignment or reconvergence."
            )
        else:
            satisfied_conditions.append(
                "Multi-horizon state is not transitioning."
            )

        top_candidate = {
            "instrument": top["symbol"],
            "score": top["score"],
            "grade": top["grade"],
            "decision": top["decision"],
            "state": top["state"],
            "bias": top["bias"],
            "current_price": current_price,
            "entry_quality": geometry["entry_quality"],
            "invalidation": geometry["invalidation"],
            "target_reference": geometry["target_reference"],
            "reward_to_risk": geometry["reward_to_risk"],
            "rr_tp1": top_analysis["trade_plan"]["rr_tp1"],
            "rr_tp2": top_analysis["trade_plan"]["rr_tp2"],
            "rr_tp3": top_analysis["trade_plan"]["rr_tp3"],
            "plan_valid": top_analysis["trade_plan"]["valid"],
            "extension": context["extension"],
            "5m_confirmed": execution["confirmed"],
            "next_conditions": next_conditions,
            "satisfied_conditions": satisfied_conditions,
            "reason": top_analysis["reason"],
        }

    pending_setup = None
    pending_rejection = None
    tradability_scan_id = str(int(time.time() * 1000))

    for candidate in ranked:
        candidate_analysis = candidate["analysis"]
        plan = candidate_analysis["trade_plan"]

        if not (
            candidate["bias"] in {"bullish", "bearish"}
            and candidate_analysis["decision"] in {"WATCH", "ALERT ONLY"}
            and plan["valid"]
        ):
            continue

        geometry = candidate_analysis["geometry"]
        context = candidate_analysis["execution_context"]
        execution = candidate_analysis["execution_5m"]

        remaining = []
        satisfied = []

        if geometry["entry_quality"] == "late":
            remaining.append(
                "Wait for a better entry or controlled pullback."
            )
        else:
            satisfied.append("Entry location is acceptable.")

        if not execution["confirmed"]:
            remaining.append("Wait for 5M execution confirmation.")
        else:
            satisfied.append("5M execution confirmation is satisfied.")

        if context["extension"] in {"extended", "highly_extended"}:
            remaining.append("Wait for price extension to normalize.")
        else:
            satisfied.append("Price is not excessively extended.")

        if candidate["state"] == "transitioning":
            remaining.append(
                "Wait for stronger multi-horizon alignment or reconvergence."
            )
        else:
            satisfied.append(
                "Multi-horizon state is not transitioning."
            )

        tradability_ok, tradability_reason, tradability_details = await verify_symbol_tradable_on_account(
            client=scanner.connector, account=account, symbol=candidate["symbol"]
        )
        if not tradability_ok:
            pending_rejection = {"instrument": candidate["symbol"], "reason": tradability_reason, "details": tradability_details}
            continue

        pending_setup = {
            "instrument": candidate["symbol"],
            "direction": (
                "LONG"
                if candidate["bias"] == "bullish"
                else "SHORT"
            ),
            "status": (
                "WAITING FOR CONFIRMATION"
                if remaining
                else "READY FOR REASSESSMENT"
            ),
            "score": candidate["score"],
            "grade": candidate["grade"],
            "entry_reference": plan["entry_reference"],
            "safe_loss": plan["safe_loss"],
            "tp1": plan["tp1"],
            "tp2": plan["tp2"],
            "tp3": plan["tp3"],
            "rr_tp1": plan["rr_tp1"],
            "rr_tp2": plan["rr_tp2"],
            "rr_tp3": plan["rr_tp3"],
            "requirements_remaining": remaining,
            "requirements_satisfied": satisfied,
            "tradability": {"status": tradability_reason, "scan_id": tradability_scan_id, "details": tradability_details},
        }

        # ranked is already ordered best-first, so the first
        # structurally valid candidate becomes the armed setup.
        break

    return {
        "account": account.nickname,
        "requested": batch["requested"],
        "successful": batch["successful"],
        "failed": batch["failed"],
        "errors": batch["errors"],
        "top_candidate": top_candidate,
        "pending_setup": pending_setup,
        "pending_rejection": pending_rejection,
        "tradability_scan_id": tradability_scan_id,
        "executable_orders": executable_orders,
        "alerts": alerts,
        "watchlist": watchlist,
    }


@router.get("/scan/{nickname}/brief")
async def scan_account_brief(
    nickname: str,
    symbols: list[str] | None = Query(default=None),
):
    """Return a concise human-readable trading brief."""

    data = await scan_trading_summary(
        nickname=nickname,
        symbols=symbols,
    )

    lines = [
        f"Account: {data['account']}",
        f"Scan: {data['successful']}/{data['requested']} successful",
        "",
    ]

    orders = data["executable_orders"]

    if orders:
        lines.append("EXECUTABLE ORDERS")
        lines.append("")

        for order in orders:
            lines.extend(
                [
                    order["order_type"],
                    order["instrument"],
                    f"Entry: {order['entry']}",
                    f"Safe Loss: {order['safe_loss']}",
                    f"Take Profit 1: {order['take_profit_1']}",
                    f"Take Profit 3: {order['take_profit_3']}",
                    f"Take Profit 2: {order['take_profit_2']}",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "EXECUTABLE ORDERS",
                "No trade yet.",
                "",
            ]
        )

    alerts = data["alerts"]

    lines.append("ALERTS")

    if alerts:
        for alert in alerts:
            lines.append(
                f"{alert['instrument']} — "
                f"{alert['alert_level']} — "
                f"{alert['meaning']}"
            )
    else:
        lines.append("None.")

    lines.append("")
    lines.append("WATCHLIST")

    watchlist = data["watchlist"]

    if watchlist:
        for item in watchlist:
            lines.append(
                f"{item['instrument']} — "
                f"{item['state']} — "
                f"{item['reason']}"
            )
    else:
        lines.append("None.")

    if data["errors"]:
        lines.append("")
        lines.append("SCAN ERRORS")

        for symbol, error in data["errors"].items():
            lines.append(f"{symbol} — {error}")

    return {
        "brief": "\n".join(lines),
    }
