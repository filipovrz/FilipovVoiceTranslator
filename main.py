import sys

from PyQt6.QtWidgets import QApplication

from tts_app.about import APP_NAME, APP_VERSION, ORG_NAME
from tts_app.config import load as load_config
from tts_app.i18n import apply_application_locale
from tts_app.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName(ORG_NAME)
    cfg = load_config()
    apply_application_locale(app, cfg.get("ui_locale"))
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
