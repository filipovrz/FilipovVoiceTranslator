"""Application author and branding."""

from tts_app.version import get_version

AUTHOR_NAME = "Filipov"
AUTHOR_EMAIL = "filipovrz@gmail.com"
COMPANY_NAME = "Evtinko Auktions Ltd"

APP_NAME = "Filipov Voice Translator"
ORG_NAME = COMPANY_NAME

APP_VERSION = get_version()


def window_title() -> str:
    from tts_app.i18n import tr

    return tr("window_title_fmt").format(
        app=APP_NAME,
        author=AUTHOR_NAME,
        company=COMPANY_NAME,
    )


def about_html() -> str:
    from tts_app.i18n import tr

    return tr("about_html").format(
        app=APP_NAME,
        author=AUTHOR_NAME,
        email=AUTHOR_EMAIL,
        company=COMPANY_NAME,
        version=APP_VERSION,
    )


# Legacy constant for tests / imports expecting static HTML (English-only)
ABOUT_HTML = (
    f"<p><b>{APP_NAME}</b> v{APP_VERSION}</p>"
    f"<p>Author: <b>{AUTHOR_NAME}</b><br/>"
    f"Email: <a href=\"mailto:{AUTHOR_EMAIL}\">{AUTHOR_EMAIL}</a><br/>"
    f"Company: <b>{COMPANY_NAME}</b></p>"
)

WINDOW_TITLE = f"{APP_NAME} — {AUTHOR_NAME} · {COMPANY_NAME}"
