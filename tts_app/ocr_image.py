"""Optional OCR: requires Pillow, pytesseract, and a system Tesseract installation."""

from __future__ import annotations

from pathlib import Path


def image_to_text(path: str, *, lang_hint: str = "eng") -> str:
    """
    Extract text from an image. ``lang_hint`` is a Tesseract language code
    (e.g. ``bul``, ``eng``, ``eng+bul``). Requires Tesseract OCR on PATH or
    ``TESSDATA_PREFIX`` set correctly.
    """
    try:
        from PIL import Image  # noqa: PLC0415
        import pytesseract  # noqa: PLC0415
    except ImportError as e:
        raise RuntimeError(
            "Install optional packages: pip install pillow pytesseract"
        ) from e

    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(path)

    img = Image.open(path)
    try:
        text = pytesseract.image_to_string(img, lang=lang_hint or "eng")
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(
            "Tesseract failed. Install Tesseract OCR for Windows and ensure it is on PATH. "
            f"Details: {e}"
        ) from e
    finally:
        img.close()

    return (text or "").strip()
