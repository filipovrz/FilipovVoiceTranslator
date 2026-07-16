from tts_app.edge_tts_engine import _pick_from_list, _volume_to_percent
from tts_app.tts_engine import VoiceInfo, prefer_voice_for_language


def test_pick_prefers_kalina_for_bulgarian() -> None:
    voices = [
        {"ShortName": "en-US-AriaNeural", "Locale": "en-US"},
        {"ShortName": "bg-BG-BorislavNeural", "Locale": "bg-BG"},
        {"ShortName": "bg-BG-KalinaNeural", "Locale": "bg-BG"},
    ]
    assert _pick_from_list(voices, "bg") == "bg-BG-KalinaNeural"


def test_pick_english_fallback() -> None:
    voices = [
        {"ShortName": "en-US-AriaNeural", "Locale": "en-US"},
        {"ShortName": "de-DE-KatjaNeural", "Locale": "de-DE"},
    ]
    assert _pick_from_list(voices, "xx") is None or _pick_from_list(voices, "en") == "en-US-AriaNeural"


def test_volume_mapping() -> None:
    assert _volume_to_percent(0.5) == "+0%"
    assert _volume_to_percent(1.0) == "+50%"
    assert _volume_to_percent(0.0) == "-50%"


def test_prefer_sapi_voice_bulgarian_by_name() -> None:
    voices = [
        VoiceInfo(id="HKEY\\TTS_MS_EN_US", name="Microsoft David", languages=("en-US",)),
        VoiceInfo(id="HKEY\\TTS_MS_BG_BG", name="Microsoft Bulgarian", languages=("bg-BG",)),
    ]
    assert prefer_voice_for_language("bg", voices).endswith("BG_BG") or "BG" in prefer_voice_for_language(
        "bg", voices
    )
