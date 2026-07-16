import json
import os
from pathlib import Path

DEFAULTS = {
    "voice_id": "",
    "rate": 200,
    "volume": 1.0,
    "last_open_dir": "",
    "last_export_dir": "",
    "window_geometry": None,
    "translate_before_speech": False,
    "translate_source": "auto",
    "translate_target": "bg",
    "mic_language": "bg",
    "tts_engine": "edge",
    "edge_voice_id": "",
    "ocr_tesseract_lang": "eng+bul",
    "ui_locale": "system",
}


class ConfigError(OSError):
    """Raised when settings cannot be written to disk."""


def config_path() -> Path:
    base = os.environ.get("LOCALAPPDATA") or str(Path.home())
    d = Path(base) / "TextToSpeechApp"
    d.mkdir(parents=True, exist_ok=True)
    return d / "settings.json"


def load() -> dict:
    p = config_path()
    if not p.is_file():
        return dict(DEFAULTS)
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return dict(DEFAULTS)
    out = dict(DEFAULTS)
    out.update({k: data[k] for k in DEFAULTS if k in data})
    return out


def save(data: dict) -> None:
    p = config_path()
    merged = dict(DEFAULTS)
    merged.update({k: data[k] for k in DEFAULTS if k in data})
    # Keep unknown keys that callers may still pass for forward-compat
    for k, v in data.items():
        if k not in merged:
            merged[k] = v
    try:
        p.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
    except OSError as e:
        raise ConfigError(str(e)) from e
