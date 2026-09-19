"""Shared fail-fast signal for upstream provider rate limits."""

import asyncio
from collections.abc import Awaitable, Callable, Iterable
import re
from typing import TypeVar


T = TypeVar("T")
R = TypeVar("R")


class RateLimitError(RuntimeError):
    """The provider rejected a request because its rate limit was reached."""


_HTTP_429 = re.compile(r"(?i)(?<![A-Za-z0-9])HTTP[\s:/_-]+429(?!\d)")
_RATE_LIMIT_TOKEN = re.compile(
    r"(?i)^(?:rate[_ -]?limit(?:ed|ing)?|too[_ -]?many[_ -]?requests)$"
)


def _is_429_status(value: object) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return value == 429
    if isinstance(value, str):
        return value.strip() == "429"
    return False


def _is_rate_limit_token(value: object) -> bool:
    return isinstance(value, str) and bool(_RATE_LIMIT_TOKEN.fullmatch(value.strip()))


def is_rate_limited(error: BaseException) -> bool:
    """Recognize provider 429s without treating incidental prose as a signal."""

    if isinstance(error, RateLimitError):
        return True

    seen: set[int] = set()
    current: BaseException | None = error
    while current is not None and id(current) not in seen:
        seen.add(id(current))

        exception_name = type(current).__name__
        if (
            _RATE_LIMIT_TOKEN.fullmatch(exception_name)
            or exception_name.lower() in {"ratelimiterror", "toomanyrequestserror"}
        ):
            return True

        for attribute in ("status_code", "status"):
            try:
                if _is_429_status(getattr(current, attribute, None)):
                    return True
            except Exception:
                pass

        try:
            response = getattr(current, "response", None)
        except Exception:
            response = None
        if response is not None:
            for attribute in ("status_code", "status"):
                try:
                    if _is_429_status(getattr(response, attribute, None)):
                        return True
                except Exception:
                    pass

        # Provider SDKs commonly expose a compact machine-readable code,
        # category, or error name. Inspect only those known metadata fields;
        # never walk arbitrary payloads that may contain credentials.
        for attribute in ("code", "error_code", "category", "error_category", "name"):
            try:
                if _is_rate_limit_token(getattr(current, attribute, None)):
                    return True
            except Exception:
                pass

        message = str(current).strip()
        if _is_rate_limit_token(message) or _HTTP_429.search(message):
            return True

        current = current.__cause__ or current.__context__

    return False


async def gather_rate_limit_aware(
    items: Iterable[T],
    worker: Callable[[T], Awaitable[R]],
    *,
    concurrency: int,
) -> list[R | None]:
    """Run a bounded batch, stopping queued and peer work on the first 429."""

    semaphore = asyncio.Semaphore(concurrency)
    rate_limited = asyncio.Event()

    async def run(item: T) -> R | None:
        if rate_limited.is_set():
            return None
        async with semaphore:
            if rate_limited.is_set():
                return None
            try:
                return await worker(item)
            except BaseException as error:
                if is_rate_limited(error):
                    rate_limited.set()
                    if isinstance(error, RateLimitError):
                        raise
                    raise RateLimitError(str(error)) from error
                raise

    tasks = [asyncio.create_task(run(item)) for item in items]
    try:
        return await asyncio.gather(*tasks)
    except RateLimitError:
        for task in tasks:
            if not task.done():
                task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        raise
