"""Legacy Word .doc reader with OLE scrape + optional Word COM fallback on Windows."""

from __future__ import annotations

import re
from pathlib import Path

import olefile


def _extract_utf16_le_chunks(data: bytes) -> list[str]:
    # Latin printable + Cyrillic (incl. Bulgarian) UTF-16-LE runs
    pat = re.compile(
        b"(?:[\x20-\x7e]\x00|[\x00-\xff][\x04\x05]\x00|[\xc0-\xff][\x04\x05\x06]\x00){8,}",
        re.DOTALL,
    )
    found: list[str] = []
    for m in pat.finditer(data):
        chunk = m.group(0)
        try:
            s = chunk.decode("utf-16-le")
        except UnicodeDecodeError:
            continue
        s = s.strip()
        if len(s) < 8:
            continue
        if not re.search(r"[\w\u0400-\u04FF]", s, re.UNICODE):
            continue
        # Drop obvious binary noise
        if sum(1 for c in s if ord(c) < 32 and c not in "\t\n\r") > len(s) // 10:
            continue
        found.append(s)
    return found


def _read_via_ole_scrape(path: str) -> str:
    if not olefile.isOleFile(path):
        with open(path, "rb") as f:
            raw = f.read()
        lines = _extract_utf16_le_chunks(raw)
        return "\n\n".join(lines) if lines else ""

    ole = olefile.OleFileIO(path)
    try:
        parts_bin: list[bytes] = []
        for name in ("WordDocument", "1Table", "Data"):
            if ole.exists(name):
                parts_bin.append(ole.openstream(name).read())
    finally:
        ole.close()

    data = b"".join(parts_bin)
    lines = _extract_utf16_le_chunks(data)
    text = "\n\n".join(dict.fromkeys(lines))
    return text.strip()


def _read_via_word_com(path: str) -> str | None:
    """Use installed Microsoft Word via COM when available (best fidelity)."""
    try:
        import win32com.client  # type: ignore
    except ImportError:
        return None

    abs_path = str(Path(path).resolve())
    word = None
    doc = None
    try:
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        doc = word.Documents.Open(abs_path, ReadOnly=True, AddToRecentFiles=False)
        text = doc.Content.Text
        return (text or "").replace("\r", "\n").strip()
    except Exception:  # noqa: BLE001
        return None
    finally:
        try:
            if doc is not None:
                doc.Close(False)
        except Exception:  # noqa: BLE001
            pass
        try:
            if word is not None:
                word.Quit()
        except Exception:  # noqa: BLE001
            pass


def read_doc(path: str) -> str:
    com_text = _read_via_word_com(path)
    if com_text:
        return com_text
    return _read_via_ole_scrape(path)
