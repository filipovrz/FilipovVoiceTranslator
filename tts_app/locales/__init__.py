"""Locale catalogs for UI strings."""

from . import (
    ar,
    bg,
    de,
    en,
    es,
    fr,
    hi,
    ja,
    pt_BR,
    ru,
    zh_CN,
)

SUPPORTED_LOCALES: tuple[str, ...] = (
    "en",
    "bg",
    "de",
    "es",
    "fr",
    "ru",
    "zh_CN",
    "hi",
    "ar",
    "pt_BR",
    "ja",
)

NATIVE_LOCALE_LABEL: dict[str, str] = {
    "en": "English",
    "bg": "Български",
    "de": "Deutsch",
    "es": "Español",
    "fr": "Français",
    "ru": "Русский",
    "zh_CN": "简体中文",
    "hi": "हिन्दी",
    "ar": "العربية",
    "pt_BR": "Português (Brasil)",
    "ja": "日本語",
}

TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": en.MESSAGES,
    "bg": bg.MESSAGES,
    "de": de.MESSAGES,
    "es": es.MESSAGES,
    "fr": fr.MESSAGES,
    "ru": ru.MESSAGES,
    "zh_CN": zh_CN.MESSAGES,
    "hi": hi.MESSAGES,
    "ar": ar.MESSAGES,
    "pt_BR": pt_BR.MESSAGES,
    "ja": ja.MESSAGES,
}
