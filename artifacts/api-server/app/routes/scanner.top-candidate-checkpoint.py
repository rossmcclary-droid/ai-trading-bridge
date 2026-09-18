"""Read-only market scan routes."""

from fastapi import APIRouter, HTTPException, Query

from app.account_manager import AccountManager
from app.services.analysis import analyze_scan, derive_alert_level
from app.services.ranker import rank_candidates
from app.services.scanner import ScannerService


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

    requested_symbols = symbols or DEFAULT_SYMBOLS

    if len(requested_symbols) > 10:
        raise HTTPException(
            status_code=400,
            detail="A scan may contain no more than 10 symbols.",
        )

    scanner = ScannerService()

    batch = await scanner.scan_symbols(
        symbols=requested_symbols,
        account_id=int(account.external_account_id),
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

    requested_symbols = symbols or DEFAULT_SYMBOLS

    if len(requested_symbols) > 10:
        raise HTTPException(
            status_code=400,
            detail="A scan may contain no more than 10 symbols.",
        )

    scanner = ScannerService()

    batch = await scanner.scan_symbols(
        symbols=requested_symbols,
        account_id=int(account.external_account_id),
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

    requested_symbols = symbols or DEFAULT_SYMBOLS

    if len(requested_symbols) > 10:
        raise HTTPException(
            status_code=400,
            detail="A scan may contain no more than 10 symbols.",
        )

    scanner = ScannerService()

    batch = await scanner.scan_symbols(
        symbols=requested_symbols,
        account_id=int(account.external_account_id),
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
                    "grade": analysis["setup_grade"],
                    "reason": analysis["reason"],
                }
            )
            continue

        alert = derive_alert_level(
            scan,
            bias=analysis["directional_bias"],
            state=analysis["multi_horizon_state"],
        )

        if (
            alert["alert_level"] is not None
            and len(alerts) < 6
            and analysis["decision"] in {"WATCH", "ALERT ONLY"}
        ):
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
        else:
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

        top_candidate = {
            "instrument": top["symbol"],
            "score": top["score"],
            "grade": top["grade"],
            "decision": top["decision"],
            "state": top["state"],
            "bias": top["bias"],
            "reason": top_analysis["reason"],
        }

    return {
        "account": account.nickname,
        "requested": batch["requested"],
        "successful": batch["successful"],
        "failed": batch["failed"],
        "errors": batch["errors"],
        "top_candidate": top_candidate,
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
