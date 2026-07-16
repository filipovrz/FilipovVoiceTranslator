from tts_app.speech_locales import iso_to_google_stt_locale


def test_iso_mapping_bg() -> None:
    assert iso_to_google_stt_locale("bg") == "bg-BG"


def test_iso_mapping_en() -> None:
    assert iso_to_google_stt_locale("en") == "en-US"


def test_pass_through_full_locale() -> None:
    assert iso_to_google_stt_locale("en-GB") == "en-GB"


def test_unknown_iso_uses_heuristic_pair() -> None:
    assert iso_to_google_stt_locale("xx") == "xx-XX"
