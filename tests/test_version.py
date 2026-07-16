from tts_app.version import get_version
from tts_app.about import APP_VERSION


def test_version_file_readable() -> None:
    v = get_version()
    assert v
    assert v[0].isdigit()
    assert APP_VERSION == v
