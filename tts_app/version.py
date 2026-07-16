"""Single source of truth for application version."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def get_version() -> str:
    """Read VERSION from project root (dev) or package-adjacent file (frozen)."""
    candidates = [
        Path(__file__).resolve().parent.parent / "VERSION",
        Path(__file__).resolve().parent / "VERSION",
    ]
    try:
        import sys

        if getattr(sys, "frozen", False):
            meipass = getattr(sys, "_MEIPASS", None)
            if meipass:
                candidates.insert(0, Path(meipass) / "VERSION")
            candidates.insert(0, Path(sys.executable).resolve().parent / "VERSION")
    except Exception:  # noqa: BLE001
        pass
    for path in candidates:
        try:
            if path.is_file():
                v = path.read_text(encoding="utf-8").strip()
                if v:
                    return v
        except OSError:
            continue
    return "1.4.0"
