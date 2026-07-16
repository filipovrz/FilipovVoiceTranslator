from __future__ import annotations

from tts_app.edge_tts_engine import synthesize_edge_to_file
from tts_app.tts_engine import synthesize_to_file


def synthesize_to_path(
    text: str,
    out_path: str,
    *,
    engine: str,
    sapi_voice_id: str,
    rate: int,
    volume: float,
    edge_voice_id: str,
    target_lang_iso: str,
) -> None:
    if engine == "edge":
        synthesize_edge_to_file(
            text,
            out_path,
            voice_id=edge_voice_id,
            target_lang_iso=target_lang_iso,
            rate=rate,
            volume=volume,
        )
    else:
        synthesize_to_file(
            text,
            out_path,
            voice_id=sapi_voice_id,
            rate=rate,
            volume=volume,
            prefer_lang_iso=target_lang_iso,
        )
