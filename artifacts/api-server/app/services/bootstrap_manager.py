"""Versioned Bootstrap file management.

Strategy-file updates only.
Does not modify broker credentials, account configuration,
risk limits, approvals, or execution permissions.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import shutil


BOOTSTRAP_PATH = (
    Path(__file__).resolve().parent.parent
    / "brain"
    / "bootstrap_v2.md"
)

HISTORY_DIR = (
    Path(__file__).resolve().parent.parent
    / "brain"
    / "bootstrap_history"
)

REQUIRED_MARKERS = (
    "PART I — HUMAN-READABLE STRATEGY",
    "PART II — MACHINE-READABLE BOOTSTRAP",
)

MAX_BOOTSTRAP_BYTES = 1_000_000


class BootstrapValidationError(ValueError):
    """Raised when an incoming Bootstrap revision is invalid."""


class BootstrapRollbackError(ValueError):
    """Raised when a previous Bootstrap cannot be restored."""


@dataclass(frozen=True)
class BootstrapStatus:
    path: str
    sha256: str
    size_bytes: int
    modified_at: str
    previous_available: bool
    previous_filename: str | None


def _digest(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def validate_bootstrap(text: str) -> None:
    if not isinstance(text, str):
        raise BootstrapValidationError(
            "Bootstrap content must be text."
        )

    if not text.strip():
        raise BootstrapValidationError(
            "Bootstrap content is empty."
        )

    encoded = text.encode("utf-8")

    if len(encoded) > MAX_BOOTSTRAP_BYTES:
        raise BootstrapValidationError(
            "Bootstrap exceeds the 1 MB safety limit."
        )

    for marker in REQUIRED_MARKERS:
        if marker not in text:
            raise BootstrapValidationError(
                f"Bootstrap is missing required section: {marker}"
            )


def _history_files() -> list[Path]:
    if not HISTORY_DIR.exists():
        return []

    return sorted(
        (
            path
            for path in HISTORY_DIR.glob("bootstrap_*.md")
            if path.is_file()
        ),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )


def get_bootstrap_status() -> BootstrapStatus:
    if not BOOTSTRAP_PATH.exists():
        raise BootstrapValidationError(
            f"Active Bootstrap does not exist: {BOOTSTRAP_PATH}"
        )

    text = BOOTSTRAP_PATH.read_text(encoding="utf-8")
    validate_bootstrap(text)

    stat = BOOTSTRAP_PATH.stat()
    history = _history_files()
    previous = history[0] if history else None

    return BootstrapStatus(
        path=str(BOOTSTRAP_PATH),
        sha256=_digest(text),
        size_bytes=len(text.encode("utf-8")),
        modified_at=datetime.fromtimestamp(
            stat.st_mtime,
            tz=timezone.utc,
        ).isoformat(),
        previous_available=previous is not None,
        previous_filename=previous.name if previous else None,
    )


def install_bootstrap(
    text: str,
    *,
    source_name: str | None = None,
) -> BootstrapStatus:
    validate_bootstrap(text)

    current = BOOTSTRAP_PATH.read_text(encoding="utf-8")
    validate_bootstrap(current)

    incoming_hash = _digest(text)
    current_hash = _digest(current)

    if incoming_hash == current_hash:
        raise BootstrapValidationError(
            "Incoming Bootstrap is identical to the active Bootstrap."
        )

    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%dT%H%M%SZ"
    )

    backup = HISTORY_DIR / (
        f"bootstrap_{timestamp}_{current_hash[:12]}.md"
    )

    shutil.copy2(BOOTSTRAP_PATH, backup)

    temp = BOOTSTRAP_PATH.with_suffix(".md.tmp")

    try:
        temp.write_text(text, encoding="utf-8")
        validate_bootstrap(
            temp.read_text(encoding="utf-8")
        )
        temp.replace(BOOTSTRAP_PATH)
    finally:
        if temp.exists():
            temp.unlink()

    return get_bootstrap_status()


def rollback_bootstrap() -> BootstrapStatus:
    history = _history_files()

    if not history:
        raise BootstrapRollbackError(
            "No previous Bootstrap revision is available."
        )

    previous = history[0]
    previous_text = previous.read_text(encoding="utf-8")
    validate_bootstrap(previous_text)

    current = BOOTSTRAP_PATH.read_text(encoding="utf-8")
    validate_bootstrap(current)

    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%dT%H%M%SZ"
    )

    current_hash = _digest(current)

    rollback_backup = HISTORY_DIR / (
        f"bootstrap_{timestamp}_{current_hash[:12]}_pre_rollback.md"
    )

    shutil.copy2(BOOTSTRAP_PATH, rollback_backup)

    temp = BOOTSTRAP_PATH.with_suffix(".md.tmp")

    try:
        temp.write_text(previous_text, encoding="utf-8")
        validate_bootstrap(
            temp.read_text(encoding="utf-8")
        )
        temp.replace(BOOTSTRAP_PATH)
    finally:
        if temp.exists():
            temp.unlink()

    return get_bootstrap_status()
