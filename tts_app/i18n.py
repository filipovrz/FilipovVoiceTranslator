"""UI translations: load locale from settings, expose tr()."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from PyQt6.QtCore import QLocale

from tts_app.locales import NATIVE_LOCALE_LABEL, SUPPORTED_LOCALES, TRANSLATIONS

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QApplication

log = logging.getLogger(__name__)

_current_locale: str = "en"


def resolve_system_locale() -> str:
    """Map QLocale.system() to one of SUPPORTED_LOCALES."""
    from PyQt6.QtCore import QLocale as QL

    loc = QLocale.system()
    name = loc.name().replace("-", "_")
    if name in SUPPORTED_LOCALES:
        return name
    m = {
        QL.Language.English: "en",
        QL.Language.Bulgarian: "bg",
        QL.Language.German: "de",
        QL.Language.Spanish: "es",
        QL.Language.French: "fr",
        QL.Language.Russian: "ru",
        QL.Language.Chinese: "zh_CN",
        QL.Language.Hindi: "hi",
        QL.Language.Arabic: "ar",
        QL.Language.Portuguese: "pt_BR",
        QL.Language.Japanese: "ja",
    }
    l = loc.language()
    if l in m:
        return m[l]
    return "en"


def get_locale() -> str:
    return _current_locale


def set_locale(code: str | None) -> None:
    global _current_locale
    if not code or code == "system":
        _current_locale = resolve_system_locale()
    elif code in SUPPORTED_LOCALES:
        _current_locale = code
    else:
        _current_locale = "en"


def tr(key: str, **kwargs: object) -> str:
    """Translate message key; missing keys fall back to English, then the key id."""
    table = TRANSLATIONS.get(_current_locale, {})
    s = table.get(key)
    if s is None:
        s = TRANSLATIONS["en"].get(key, key)
    if kwargs:
        try:
            return str(s).format(**kwargs)
        except (KeyError, ValueError) as e:
            log.debug("tr format failed for %s: %s", key, e)
            return str(s)
    return str(s)


def apply_application_locale(app: QApplication | None, ui_locale_pref: str | None) -> None:
    """Set global locale from preference and optional RTL for Arabic."""
    from PyQt6.QtCore import Qt

    set_locale(ui_locale_pref)
    loc = get_locale()
    if app is not None:
        if loc == "ar":
            app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        else:
            app.setLayoutDirection(Qt.LayoutDirection.LeftToRight)


def locale_ui_labels() -> list[tuple[str, str]]:
    """Pairs (locale_code, label) for the language menu (native language names)."""
    out: list[tuple[str, str]] = [("system", tr("lang_system"))]
    for code in SUPPORTED_LOCALES:
        out.append((code, NATIVE_LOCALE_LABEL[code]))
    return out
