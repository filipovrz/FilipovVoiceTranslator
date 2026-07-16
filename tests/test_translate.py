from unittest.mock import MagicMock, patch

from tts_app.translate import translate_text


def test_translate_same_language_returns_original() -> None:
    assert translate_text("hello", "en", "en") == "hello"


@patch("deep_translator.GoogleTranslator")
def test_translate_calls_engine(mock_gt: MagicMock) -> None:
    inst = MagicMock()
    inst.translate.return_value = "здравей"
    mock_gt.return_value = inst

    out = translate_text("hello", "en", "bg")
    assert out == "здравей"
    mock_gt.assert_called()
    inst.translate.assert_called()


def test_chunk_join_restores_text() -> None:
    from tts_app.translate import _split_chunks

    t = "Hello world.\n" * 500
    chunks = _split_chunks(t, 200)
    assert "".join(chunks) == t
    assert all(len(c) <= 200 for c in chunks)
