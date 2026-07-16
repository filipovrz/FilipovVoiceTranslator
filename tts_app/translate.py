from __future__ import annotations

from tts_app.language_catalog import load_language_catalog

# Chunk size conservative for free Google Translate endpoints used by deep-translator
_MAX_CHUNK = 4500


def supported_languages(*, refresh: bool = False) -> dict[str, str]:
    """Return mapping display_name -> ISO code (lowercase). Offline-capable."""
    return load_language_catalog(refresh=refresh)


def language_pairs_for_ui(
    *,
    detect_label: str = "Detect language",
) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    """
    Each list item is (display_label, iso_code). Source list starts with
    (detect_label, "auto"). Lists are sorted by display label.
    Bulgarian and English are pinned near the top for convenience.
    """
    d = supported_languages()
    items = [(name.title(), code) for name, code in d.items()]

    def sort_key(item: tuple[str, str]) -> tuple[int, str]:
        code = item[1]
        if code == "bg":
            return (0, item[0])
        if code == "en":
            return (1, item[0])
        return (2, item[0])

    items.sort(key=sort_key)
    source = [(detect_label, "auto")] + items
    target = list(items)
    return source, target


def translate_text(text: str, source: str, target: str) -> str:
    """
    Translate *text* from *source* to *target* (ISO codes, or 'auto' for source).
    Uses Google Translate via deep-translator (requires network).
    """
    text = (text or "").strip()
    if not text:
        return ""

    src = (source or "auto").lower().strip()
    tgt = (target or "en").lower().strip()

    if src != "auto" and src == tgt:
        return text

    from deep_translator import GoogleTranslator

    chunks = _split_chunks(text, _MAX_CHUNK)
    out: list[str] = []
    for chunk in chunks:
        t = GoogleTranslator(source=src, target=tgt).translate(chunk)
        out.append(t)
    return "\n".join(out)


def _split_chunks(text: str, max_len: int) -> list[str]:
    if len(text) <= max_len:
        return [text]
    out: list[str] = []
    i = 0
    while i < len(text):
        end = min(i + max_len, len(text))
        if end < len(text):
            cut = text.rfind("\n", i + max_len // 2, end)
            if cut <= i:
                cut = text.rfind(" ", i + max_len // 2, end)
            if cut > i:
                end = cut + 1
        out.append(text[i:end])
        i = end
    return out
