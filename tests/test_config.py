import json

import tts_app.config as cfg


def test_defaults_include_translation_keys() -> None:
    assert "translate_before_speech" in cfg.DEFAULTS
    assert "translate_target" in cfg.DEFAULTS


def test_save_roundtrip(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "config_path", lambda: tmp_path / "s.json")
    d = cfg.load()
    d["translate_target"] = "bg"
    cfg.save(d)
    data = json.loads((tmp_path / "s.json").read_text(encoding="utf-8"))
    assert data["translate_target"] == "bg"
