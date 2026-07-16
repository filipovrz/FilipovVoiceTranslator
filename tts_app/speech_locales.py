"""Map ISO 639-1 codes (as used by translation) to Google Web Speech API BCP-47 locales."""

# Fallback for missing keys: use en-US (user should pick a closer language in the UI if needed).
ISO_TO_GOOGLE_STT: dict[str, str] = {
    "af": "af-ZA",
    "am": "am-ET",
    "ar": "ar-SA",
    "az": "az-AZ",
    "be": "be-BY",
    "bg": "bg-BG",
    "bn": "bn-IN",
    "bs": "bs-BA",
    "ca": "ca-ES",
    "cs": "cs-CZ",
    "cy": "cy-GB",
    "da": "da-DK",
    "de": "de-DE",
    "el": "el-GR",
    "en": "en-US",
    "eo": "eo-001",
    "es": "es-ES",
    "et": "et-EE",
    "eu": "eu-ES",
    "fa": "fa-IR",
    "fi": "fi-FI",
    "fr": "fr-FR",
    "ga": "ga-IE",
    "gd": "gd-GB",
    "gl": "gl-ES",
    "gu": "gu-IN",
    "ha": "ha-NG",
    "he": "he-IL",
    "hi": "hi-IN",
    "hr": "hr-HR",
    "hu": "hu-HU",
    "hy": "hy-AM",
    "id": "id-ID",
    "ig": "ig-NG",
    "is": "is-IS",
    "it": "it-IT",
    "ja": "ja-JP",
    "jw": "jv-ID",
    "ka": "ka-GE",
    "kk": "kk-KZ",
    "km": "km-KH",
    "kn": "kn-IN",
    "ko": "ko-KR",
    "ku": "ku-TR",
    "ky": "ky-KG",
    "la": "la-VA",
    "lb": "lb-LU",
    "lo": "lo-LA",
    "lt": "lt-LT",
    "lv": "lv-LV",
    "mg": "mg-MG",
    "mi": "mi-NZ",
    "mk": "mk-MK",
    "ml": "ml-IN",
    "mn": "mn-MN",
    "mr": "mr-IN",
    "ms": "ms-MY",
    "mt": "mt-MT",
    "my": "my-MM",
    "ne": "ne-NP",
    "nl": "nl-NL",
    "no": "no-NO",
    "ny": "ny-MW",
    "pa": "pa-IN",
    "pl": "pl-PL",
    "ps": "ps-AF",
    "pt": "pt-BR",
    "ro": "ro-RO",
    "ru": "ru-RU",
    "sd": "sd-IN",
    "si": "si-LK",
    "sk": "sk-SK",
    "sl": "sl-SI",
    "so": "so-SO",
    "sq": "sq-AL",
    "sr": "sr-RS",
    "st": "st-ZA",
    "su": "su-ID",
    "sv": "sv-SE",
    "sw": "sw-TZ",
    "ta": "ta-IN",
    "te": "te-IN",
    "tg": "tg-TJ",
    "th": "th-TH",
    "tk": "tk-TM",
    "tr": "tr-TR",
    "uk": "uk-UA",
    "ur": "ur-PK",
    "uz": "uz-UZ",
    "vi": "vi-VN",
    "xh": "xh-ZA",
    "yi": "yi-001",
    "yo": "yo-NG",
    "zh": "zh-CN",
    "zu": "zu-ZA",
}


def iso_to_google_stt_locale(iso_code: str) -> str:
    """Return BCP-47 locale for Google Speech-to-Text (Web API)."""
    raw = (iso_code or "en").strip()
    if "-" in raw and len(raw) >= 4:
        lang, rest = raw.split("-", 1)
        lang = lang.lower().strip()
        rest = rest.strip()
        if len(rest) == 2 and rest.isalpha():
            rest = rest.upper()
        return f"{lang}-{rest}"
    base = raw.lower()
    if len(base) >= 2:
        two = base[:2]
        if two in ISO_TO_GOOGLE_STT:
            return ISO_TO_GOOGLE_STT[two]
        # Many Google STT locales follow ll-LL for Latin-script ISO 639-1 codes
        return f"{two}-{two.upper()}"
    return "en-US"
