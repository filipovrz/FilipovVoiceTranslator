import tts_app.history_store as hs


def test_append_and_load(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(hs, "_history_path", lambda: tmp_path / "h.json")
    hs.append_entry(original="hello", translated="здравей", source_lang="en", target_lang="bg")
    entries = hs.load_entries()
    assert len(entries) == 1
    assert entries[0]["o"] == "hello"
    assert entries[0]["tr"] == "здравей"


def test_clear(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(hs, "_history_path", lambda: tmp_path / "h.json")
    hs.append_entry(original="a", translated="b", source_lang="en", target_lang="de")
    hs.clear_all()
    assert hs.load_entries() == []
