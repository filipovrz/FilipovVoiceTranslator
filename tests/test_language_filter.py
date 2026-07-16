from tts_app.language_filter import filter_language_pairs


def test_filter_empty_query_returns_all() -> None:
    pairs = [("English", "en"), ("French", "fr"), ("日本語", "ja")]
    assert len(filter_language_pairs(pairs, "")) == 3


def test_filter_by_substring() -> None:
    pairs = [("English", "en"), ("French", "fr")]
    r = filter_language_pairs(pairs, "fre")
    assert len(r) == 1 and r[0][1] == "fr"


def test_filter_by_code_prefix() -> None:
    pairs = [("English", "en"), ("Estonian", "et")]
    r = filter_language_pairs(pairs, "et")
    assert any(c == "et" for _, c in r)
