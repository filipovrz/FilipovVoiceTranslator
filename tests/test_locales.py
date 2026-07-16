"""Locale catalog completeness."""

from tts_app.locales import TRANSLATIONS
from tts_app.locales.en import MESSAGES as EN


REQUIRED = (
    "detect_language",
    "voice_load_error_fmt",
    "translation_was_empty",
    "window_title_fmt",
    "edge_tts_title",
    "lang_bg",
    "lang_en",
)


def test_all_locales_have_required_keys() -> None:
    for code, messages in TRANSLATIONS.items():
        for key in REQUIRED:
            assert key in messages, f"{code} missing {key}"
        assert "{version}" in messages.get("about_html", ""), f"{code} about_html missing {{version}}"


def test_english_is_superset() -> None:
    for key in REQUIRED:
        assert key in EN
