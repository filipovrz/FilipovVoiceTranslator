"""Microphone capture + Google Web Speech API (via SpeechRecognition)."""

from __future__ import annotations


def listen_once(
    google_stt_locale: str,
    *,
    timeout: float = 15.0,
    phrase_time_limit: float = 30.0,
    ambient_duration: float = 0.45,
) -> str:
    """
    Record one utterance from the default microphone and return recognized text.
    Requires ``speech_recognition`` and ``PyAudio``. Network required for Google STT.
    """
    import speech_recognition as sr

    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=ambient_duration)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    except sr.WaitTimeoutError as e:
        raise RuntimeError("No speech detected before timeout — try again or speak louder.") from e

    try:
        text = r.recognize_google(audio, language=google_stt_locale)
    except sr.UnknownValueError as e:
        raise RuntimeError("Could not understand audio — check microphone language setting.") from e
    except sr.RequestError as e:
        raise RuntimeError(f"Speech recognition service error: {e}") from e

    return (text or "").strip()
