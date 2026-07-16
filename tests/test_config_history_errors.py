import pytest

import tts_app.config as cfg
from tts_app.history_store import HistoryError, append_entry, clear_all, load_entries


def test_defaults_prefer_bulgarian_and_edge() -> None:
    assert cfg.DEFAULTS["translate_target"] == "bg"
    assert cfg.DEFAULTS["mic_language"] == "bg"
    assert cfg.DEFAULTS["tts_engine"] == "edge"
    assert "bul" in cfg.DEFAULTS["ocr_tesseract_lang"]


def test_config_save_error(tmp_path, monkeypatch) -> None:
    target = tmp_path / "missing" / "s.json"
    monkeypatch.setattr(cfg, "config_path", lambda: target)
    with pytest.raises(cfg.ConfigError):
        cfg.save({"translate_target": "bg"})


def test_history_roundtrip(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))
    clear_all()
    append_entry(original="здравей", translated="hello", source_lang="bg", target_lang="en")
    entries = load_entries()
    assert entries
    assert entries[0]["o"] == "здравей"
    clear_all()
    assert load_entries() == []


def test_history_save_error(tmp_path, monkeypatch) -> None:
    from tts_app import history_store as hs

    bad = tmp_path / "nope"
    bad.write_text("x", encoding="utf-8")  # path is a file, mkdir will fail on parent ops differently

    def boom_path():
        # Return a path under a file-as-directory to force write failure
        p = tmp_path / "blocked"
        p.mkdir(exist_ok=True)
        # Make directory read-only write fail by pointing to invalid nested file
        return p / "a" / "b" / "history.json"

    monkeypatch.setattr(hs, "_history_path", boom_path)
    with pytest.raises(HistoryError):
        hs.save_entries([{"t": "x"}])
