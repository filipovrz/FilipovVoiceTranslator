"""Microsoft Edge neural voices via edge-tts (online, MP3 output)."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass

# Preferred neural voices for Bulgarian / English when Auto is selected.
_PREFERRED_VOICES: dict[str, list[str]] = {
    "bg": ["bg-BG-KalinaNeural", "bg-BG-BorislavNeural"],
    "en": ["en-US-AriaNeural", "en-GB-SoniaNeural", "en-US-GuyNeural"],
}


@dataclass
class EdgeVoiceInfo:
    short_name: str
    friendly_name: str
    locale: str


def _rate_to_percent(rate_wpm: int) -> str:
    """Map SAPI-like WPM (80–400) to Edge rate string."""
    delta = int(round((int(rate_wpm) - 200) / 4))
    delta = max(-50, min(50, delta))
    sign = "+" if delta >= 0 else ""
    return f"{sign}{delta}%"


def _volume_to_percent(volume: float) -> str:
    """Map 0.0–1.0 volume to Edge volume string (relative to default)."""
    v = max(0.0, min(1.0, float(volume)))
    # Edge volume: -50% … +50%; map 0→-50, 0.5→0, 1→+50
    delta = int(round((v - 0.5) * 100))
    delta = max(-50, min(50, delta))
    sign = "+" if delta >= 0 else ""
    return f"{sign}{delta}%"


async def _list_voices_async() -> list[EdgeVoiceInfo]:
    import edge_tts

    raw = await edge_tts.list_voices()
    out: list[EdgeVoiceInfo] = []
    for v in raw:
        sn = v.get("ShortName") or ""
        if not sn:
            continue
        fn = v.get("FriendlyName") or sn
        loc = v.get("Locale") or ""
        out.append(EdgeVoiceInfo(short_name=sn, friendly_name=fn, locale=loc))
    out.sort(key=lambda x: (x.locale.lower(), x.friendly_name.lower()))
    return out


def list_edge_voices() -> list[EdgeVoiceInfo]:
    return asyncio.run(_list_voices_async())


def _pick_from_list(voices: list[dict], lang_iso: str) -> str | None:
    lang_iso = (lang_iso or "en").lower().strip().split("-")[0][:2]
    preferred = _PREFERRED_VOICES.get(lang_iso, [])
    names = {v.get("ShortName") for v in voices}
    for name in preferred:
        if name in names:
            return name
    neural = [
        v
        for v in voices
        if "Neural" in (v.get("ShortName") or "")
        and (v.get("Locale") or "").lower().startswith(lang_iso)
    ]
    if neural:
        neural.sort(key=lambda x: x.get("ShortName", ""))
        return neural[0]["ShortName"]
    partial = [v for v in voices if (v.get("Locale") or "").lower().startswith(lang_iso)]
    if partial:
        partial.sort(key=lambda x: x.get("ShortName", ""))
        return partial[0]["ShortName"]
    return None


async def _pick_voice_async(lang_iso: str) -> str:
    import edge_tts

    voices = await edge_tts.list_voices()
    picked = _pick_from_list(voices, lang_iso)
    if picked:
        return picked
    # English neural fallback
    for v in voices:
        if v.get("ShortName") == "en-US-AriaNeural":
            return v["ShortName"]
    if voices:
        return voices[0]["ShortName"]
    raise RuntimeError("No Edge voices returned.")


def pick_voice_for_language(lang_iso: str) -> str:
    return asyncio.run(_pick_voice_async(lang_iso))


async def _synthesize_async(
    text: str,
    out_path: str,
    *,
    voice: str,
    rate_wpm: int,
    volume: float,
) -> None:
    import edge_tts

    rate = _rate_to_percent(rate_wpm)
    vol = _volume_to_percent(volume)
    comm = edge_tts.Communicate(text, voice, rate=rate, volume=vol)
    await comm.save(out_path)


def synthesize_edge_to_file(
    text: str,
    out_path: str,
    *,
    voice_id: str,
    target_lang_iso: str,
    rate: int,
    volume: float,
) -> None:
    voice = (voice_id or "").strip()
    if not voice:
        voice = pick_voice_for_language(target_lang_iso)
    asyncio.run(
        _synthesize_async(
            text,
            out_path,
            voice=voice,
            rate_wpm=int(rate),
            volume=float(volume),
        )
    )
