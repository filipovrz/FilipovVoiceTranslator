"""Append-only session history (recent translations) stored as JSON under Local AppData."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MAX_ENTRIES = 50


class HistoryError(OSError):
    """Raised when history cannot be written to disk."""


def _history_path() -> Path:
    base = os.environ.get("LOCALAPPDATA") or str(Path.home())
    d = Path(base) / "TextToSpeechApp"
    d.mkdir(parents=True, exist_ok=True)
    return d / "session_history.json"


def _trim(s: str, max_len: int = 12000) -> str:
    s = (s or "").strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 3] + "..."


def load_entries() -> list[dict[str, Any]]:
    p = _history_path()
    if not p.is_file():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    entries = data.get("entries")
    if not isinstance(entries, list):
        return []
    return [e for e in entries if isinstance(e, dict)]


def save_entries(entries: list[dict[str, Any]]) -> None:
    p = _history_path()
    try:
        p.write_text(
            json.dumps({"entries": entries[:MAX_ENTRIES]}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError as e:
        raise HistoryError(str(e)) from e


def append_entry(
    *,
    original: str,
    translated: str,
    source_lang: str,
    target_lang: str,
) -> None:
    original = _trim(original)
    translated = _trim(translated)
    if not original and not translated:
        return
    entries = load_entries()
    entry = {
        "t": datetime.now(timezone.utc).isoformat(),
        "o": original,
        "tr": translated,
        "src": source_lang or "",
        "tgt": target_lang or "",
    }
    entries.insert(0, entry)
    save_entries(entries[:MAX_ENTRIES])


def clear_all() -> None:
    save_entries([])
