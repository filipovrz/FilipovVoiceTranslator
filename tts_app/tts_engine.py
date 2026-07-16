from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VoiceInfo:
    id: str
    name: str
    languages: tuple[str, ...] = ()


def _engine():
    import pyttsx3

    return pyttsx3.init()


def _voice_languages(v) -> tuple[str, ...]:
    langs = getattr(v, "languages", None) or []
    out: list[str] = []
    for item in langs:
        if isinstance(item, bytes):
            try:
                item = item.decode("utf-8", errors="ignore")
            except Exception:  # noqa: BLE001
                continue
        s = str(item).strip()
        if s:
            out.append(s)
    return tuple(out)


def list_voices() -> list[VoiceInfo]:
    eng = _engine()
    out: list[VoiceInfo] = []
    for v in eng.getProperty("voices"):
        vid = getattr(v, "id", None) or v.name
        out.append(
            VoiceInfo(
                id=str(vid),
                name=v.name or str(vid),
                languages=_voice_languages(v),
            )
        )
    return out


def _matches_lang(voice: VoiceInfo, lang_iso: str) -> bool:
    lang = (lang_iso or "").lower().strip().split("-")[0][:2]
    if not lang:
        return False
    blob = f"{voice.id} {voice.name} {' '.join(voice.languages)}".lower()
    aliases = {
        "bg": ("bg", "bulgarian", "българ", "bul"),
        "en": ("en", "english", "eng"),
    }
    needles = aliases.get(lang, (lang,))
    return any(n in blob for n in needles)


def prefer_voice_for_language(lang_iso: str, voices: list[VoiceInfo] | None = None) -> str:
    """Return best matching SAPI voice id for *lang_iso*, or '' if none."""
    voices = voices if voices is not None else list_voices()
    for v in voices:
        if _matches_lang(v, lang_iso):
            return v.id
    return ""


def apply_voice(eng, voice_id: str) -> None:
    if not voice_id:
        return
    for v in eng.getProperty("voices"):
        vid = getattr(v, "id", None) or v.name
        if str(vid) == voice_id or v.name == voice_id:
            eng.setProperty("voice", getattr(v, "id", v.name))
            return


def synthesize_to_file(
    text: str,
    out_path: str,
    *,
    voice_id: str = "",
    rate: int = 200,
    volume: float = 1.0,
    prefer_lang_iso: str = "",
) -> None:
    import pyttsx3

    eng = pyttsx3.init()
    chosen = voice_id
    if not chosen and prefer_lang_iso:
        chosen = prefer_voice_for_language(prefer_lang_iso, list_voices())
    apply_voice(eng, chosen)
    eng.setProperty("rate", int(rate))
    eng.setProperty("volume", float(volume))
    eng.save_to_file(text, out_path)
    eng.runAndWait()
