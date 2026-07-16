# Чекпойнт — Filipov Voice Translator (Text to Speech + Translate)

**Дата на чекпойнта:** 2026-07-17  
**Версия на приложението:** **1.4.0** (единствен източник: корневият файл `VERSION`)  
**Корен на проекта:** `D:\Filipov Ne Pipai\Pgojects\text_to_speech`

---

## Какво представлява проектът

Desktop приложение за Windows (**PyQt6**): отваряне/редактиране на текст, превод (Google през `deep-translator`), синтез на реч (Windows **SAPI** офлайн или **Microsoft Edge neural TTS** онлайн), микрофон → текст (Google STT), опционално **OCR** (Tesseract `eng+bul`). История на сесии, настройки в JSON, инсталатор с **Inno Setup 6**.

**По подразбиране (v1.4.0):** целеви език за превод `bg`, микрофон `bg`, двигател **Edge** (български гласове Kalina/Borislav при „Към“ = български).

---

## Структура и ключови файлове

| Файл / папка | Роля |
|----------------|------|
| `VERSION` | Единствен източник на версията |
| `main.py` | Точка на вход |
| `tts_app/main_window.py` | UI и orchestration |
| `tts_app/workers.py` | QThread workers (STT / превод / TTS / Edge voices) |
| `tts_app/version.py` | Чете `VERSION` |
| `tts_app/language_catalog.py` | Офлайн-first списък езици |
| `tts_app/data/google_languages.json` | Bundled каталог (~133 езика) |
| `tts_app/about.py` | Брандинг + версия |
| `tts_app/config.py` | `%LOCALAPPDATA%\TextToSpeechApp\settings.json` |
| `tts_app/locales/` | UI преводи (en, bg, …) |
| `README.md` | Документация (EN) |
| `LICENSE` | MIT |
| `.github/workflows/ci.yml` | Pytest на Windows |
| `scripts/build_installer.ps1` | PyInstaller + Inno + опционален SignTool |

---

## Направено в 1.4.0

- `.gitignore`, `README.md`, `LICENSE`, CI
- Експортът на аудио вече е във фонов thread (не блокира UI)
- Офлайн списък с езици (bundled JSON + user cache)
- Една версия: `VERSION` → about + Inno чрез build скрипта
- Допълнени локали (вкл. BG `voice_load_error_fmt`, `detect_language`)
- По-добър `.doc` reader (Word COM при наличен Word, иначе OLE scrape)
- Повече тестове + обработка на грешки при запис на настройки/история
- Почистен корен; workers изнесени от `main_window`
- Хукове за Authenticode подписване; Edge volume; предпочитани BG/EN гласове

---

## Как да продължиш

1. `.\.venv\Scripts\python.exe -m pytest tests -q`
2. `.\.venv\Scripts\python.exe main.py`
3. `.\scripts\build_installer.ps1`

Подписване (по желание): виж `README.md` → `TTS_SIGN_CERT`.
