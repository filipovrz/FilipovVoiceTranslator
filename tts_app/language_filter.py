"""Filter long language lists in the UI (name or ISO code)."""


def filter_language_pairs(
    pairs: list[tuple[str, str]],
    query: str,
) -> list[tuple[str, str]]:
    q = (query or "").strip().lower()
    if not q:
        return list(pairs)
    out: list[tuple[str, str]] = []
    for label, code in pairs:
        c = (code or "").lower()
        if q in label.lower() or q in c or (len(q) >= 2 and c.startswith(q)):
            out.append((label, code))
    return out
