"""Offline-first Google Translate language catalog."""

from __future__ import annotations

import json
import os
from pathlib import Path

_CACHE: dict[str, str] | None = None


def _bundled_catalog_path() -> Path:
    return Path(__file__).resolve().parent / "data" / "google_languages.json"


def _user_cache_path() -> Path:
    base = os.environ.get("LOCALAPPDATA") or str(Path.home())
    d = Path(base) / "TextToSpeechApp"
    d.mkdir(parents=True, exist_ok=True)
    return d / "google_languages_cache.json"


def _read_json(path: Path) -> dict[str, str] | None:
    try:
        if not path.is_file():
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict) or not data:
        return None
    out: dict[str, str] = {}
    for name, code in data.items():
        if isinstance(name, str) and isinstance(code, str) and name and code:
            out[name.lower()] = code.lower()
    return out or None


def _write_json(path: Path, data: dict[str, str]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True),
            encoding="utf-8",
        )
    except OSError:
        pass


def _fetch_online() -> dict[str, str] | None:
    try:
        from deep_translator import GoogleTranslator

        raw = GoogleTranslator().get_supported_languages(as_dict=True)
    except Exception:  # noqa: BLE001
        return None
    if not isinstance(raw, dict) or not raw:
        return None
    return {str(k).lower(): str(v).lower() for k, v in raw.items() if k and v}


def _minimal_fallback() -> dict[str, str]:
    return {
        "english": "en",
        "bulgarian": "bg",
        "german": "de",
        "french": "fr",
        "spanish": "es",
        "russian": "ru",
    }


def load_language_catalog(*, refresh: bool = False) -> dict[str, str]:
    """
    Return display_name (lowercase) -> ISO code.

    Default path is offline-first (user cache → bundled JSON) so startup works
    without network. Pass refresh=True to try Google and update the user cache.
    """
    global _CACHE
    if _CACHE is not None and not refresh:
        return _CACHE

    if refresh:
        online = _fetch_online()
        if online:
            _write_json(_user_cache_path(), online)
            _CACHE = online
            return online

    for path in (_user_cache_path(), _bundled_catalog_path()):
        data = _read_json(path)
        if data:
            _CACHE = data
            return data

    online = _fetch_online()
    if online:
        _write_json(_user_cache_path(), online)
        _CACHE = online
        return online

    _CACHE = _minimal_fallback()
    return _CACHE


def clear_language_catalog_cache() -> None:
    global _CACHE
    _CACHE = None
