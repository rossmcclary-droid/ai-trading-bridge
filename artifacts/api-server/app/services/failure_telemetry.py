"""Strictly allowlisted, non-secret failure metadata for export jobs."""

from __future__ import annotations

from typing import Any
from urllib.error import HTTPError

from app.services.rate_limit import RateLimitError, is_rate_limited


_OPERATIONS = {"auth", "accounts", "instruments", "quotes", "history", "application"}
_STAGES = {"authentication", "account_discovery", "instrument_discovery", "quote_discovery", "deep_analysis", "export", "application"}
_SAFE_TYPES = {
    "AuthenticationError", "ConnectionError", "HTTPError", "JSONDecodeError",
    "KeyError", "RateLimitError", "RuntimeError", "TimeoutError", "TypeError",
    "URLError", "ValueError",
}
_TRACE_OPERATIONS = {
    "authenticate": ("authentication", "auth"),
    "get_accounts": ("account_discovery", "accounts"),
    "get_all_accounts": ("account_discovery", "accounts"),
    "get_available_instruments": ("instrument_discovery", "instruments"),
    "get_quotes": ("quote_discovery", "quotes"),
    "get_quote": ("quote_discovery", "quotes"),
    "get_historical_candles": ("deep_analysis", "history"),
}


def _chain(error: BaseException):
    seen: set[int] = set()
    current: BaseException | None = error
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        yield current
        current = current.__cause__ or current.__context__


def _safe_status(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and 100 <= value <= 599:
        return value
    if isinstance(value, str) and value.strip().isdigit():
        number = int(value.strip())
        return number if 100 <= number <= 599 else None
    return None


def _safe_retry_after(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)) and 0 <= float(value) <= 86400:
        return round(float(value), 3)
    if isinstance(value, str):
        try:
            number = float(value.strip())
        except (TypeError, ValueError):
            return None
        if 0 <= number <= 86400:
            return round(number, 3)
    return None


def sanitize_failure(
    error: BaseException,
    *,
    failure_stage: str = "export",
    provider_operation: str = "application",
) -> dict[str, Any]:
    """Return only fixed taxonomy fields; never serialize an exception or response."""

    stage = failure_stage if failure_stage in _STAGES else "application"
    operation = provider_operation if provider_operation in _OPERATIONS else "application"
    error_type = "UnknownError"
    status: int | None = None
    retry_after: float | None = None
    retry_after_present = False

    for item in _chain(error):
        name = type(item).__name__
        if error_type == "UnknownError" and name in _SAFE_TYPES:
            error_type = name

        try:
            response = getattr(item, "response", None)
        except Exception:
            response = None
        for candidate in (item, response):
            if candidate is None:
                continue
            for attribute in ("status_code", "status", "code"):
                try:
                    candidate_status = _safe_status(getattr(candidate, attribute, None))
                except Exception:
                    candidate_status = None
                if candidate_status is not None:
                    status = candidate_status
                    break

        try:
            operation_hint = getattr(item, "provider_operation", None)
        except Exception:
            operation_hint = None
        if operation_hint in _OPERATIONS:
            operation = operation_hint

        try:
            stage_hint = getattr(item, "failure_stage", None)
        except Exception:
            stage_hint = None
        if stage_hint in _STAGES:
            stage = stage_hint

        try:
            retry_hint = getattr(item, "retry_after", None)
        except Exception:
            retry_hint = None
        # urllib's HTTPError is itself the response object. Inspect exactly
        # one named header and never enumerate or serialize the header set.
        if retry_hint is None and isinstance(item, HTTPError):
            try:
                retry_hint = item.headers.get("Retry-After")
            except Exception:
                retry_hint = None
        if retry_hint is not None:
            retry_after_present = True
            safe_retry = _safe_retry_after(retry_hint)
            if safe_retry is not None:
                retry_after = safe_retry

        traceback = item.__traceback__
        while traceback is not None:
            hint = _TRACE_OPERATIONS.get(traceback.tb_frame.f_code.co_name)
            if hint is not None:
                stage, operation = hint
            traceback = traceback.tb_next

    rate_limited = isinstance(error, RateLimitError) or is_rate_limited(error) or status == 429
    result: dict[str, Any] = {
        "error_type": error_type,
        "failure_stage": stage,
        "provider_http_status": status,
        "provider_operation": operation,
        "rate_limited": rate_limited,
        "retry_after_present": retry_after_present,
        "retry_after_seconds": retry_after,
    }
    return result
