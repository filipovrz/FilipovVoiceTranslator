import tempfile

from tts_app.readers import load_text


def test_read_txt_utf8() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write("Hello български")
        path = f.name
    try:
        assert "български" in load_text(path)
    finally:
        import os

        os.unlink(path)
