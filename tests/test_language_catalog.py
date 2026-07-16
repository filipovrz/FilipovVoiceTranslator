"""Tests for offline language catalog and UI pairs."""

from tts_app.language_catalog import clear_language_catalog_cache, load_language_catalog
from tts_app.translate import language_pairs_for_ui, supported_languages


def test_bundled_catalog_has_bulgarian_and_english() -> None:
    clear_language_catalog_cache()
    d = load_language_catalog()
    assert d.get("bulgarian") == "bg"
    assert d.get("english") == "en"
    assert len(d) >= 50


def test_language_pairs_pin_bg_and_en() -> None:
    clear_language_catalog_cache()
    source, target = language_pairs_for_ui(detect_label="Detect language")
    assert source[0] == ("Detect language", "auto")
    codes = [c for _, c in target]
    assert "bg" in codes
    assert "en" in codes
    # bg then en should appear before other languages in sort order
    assert codes.index("bg") < codes.index("en") or codes[0] == "bg"


def test_supported_languages_offline() -> None:
    clear_language_catalog_cache()
    assert "bg" in supported_languages().values()
