"""Bulgarian UI strings."""

from tts_app.locales.en import MESSAGES as EN

_BG: dict[str, str] = {
    "window_title_fmt": "{app} — {author} · {company}",
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>Автор: <b>{author}</b><br/>
Имейл: <a href="mailto:{email}">{email}</a><br/>
Фирма: <b>{company}</b></p>
<p>Списъкът с превод обхваща <b>всички езици</b>, които предлага Google Translate (100+). Ползвайте полето за търсене, за да намерите език бързо.
Разпознаването на реч използва Google Web Speech (изберете езика, на който говорите). Гласовете на Windows покриват по-малко езици — за български предпочитайте Microsoft Edge neural (Калина/Борислав).</p>
<p>Разпознаване на реч (Google чрез SpeechRecognition), превод (Google чрез deep-translator)
и синтез на реч (Windows SAPI) може да изискват интернет връзка където е отбелязано.</p>
<p>Формати на документи: .txt, .doc, .docx, .pdf. Настройки: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>Преки пътища: Ctrl+O отваряне, Ctrl+Shift+S експорт на аудио, Ctrl+Shift+T запис на препис, Ctrl+Return подготовка,
Ctrl+T превод, Ctrl+Space пускане/пауза, Esc спиране.</p>""",
    "menu_file": "&Файл",
    "menu_open": "Отваряне…",
    "menu_export_audio": "Експорт на аудио…",
    "menu_save_transcript_txt": "Запис на препис (TXT)…",
    "menu_save_wav_copy": "Запис на последното аудио (копие)…",
    "menu_open_image_ocr": "Отваряне на изображение (OCR)…",
    "menu_prepare_refresh": "Подготви / Обнови аудио",
    "menu_translate_only": "Само превод",
    "menu_exit": "&Изход",
    "menu_session_history": "История на сесията",
    "menu_hist_view": "Преглед и възстановяване…",
    "menu_hist_add": "Добави текущото към историята",
    "menu_hist_clear": "Изчисти цялата история",
    "menu_edit": "&Редактиране",
    "menu_copy_original": "Копирай оригиналния текст",
    "menu_copy_translation": "Копирай превода",
    "menu_paste_original": "Постави в оригинала",
    "menu_replace_from_clipboard": "Замени оригинала от клипборда",
    "menu_copy_both": "Копирай оригинал + превод",
    "menu_help": "&Помощ",
    "menu_interface_language": "Език на интерфейса",
    "menu_keyboard_shortcuts": "Клавишни комбинации…",
    "menu_about": "&Относно",
    "detect_language": "Открий език",
    "lang_system": "Като езика на Windows",
    "lang_en": "English",
    "lang_bg": "Български",
    "lang_de": "Deutsch",
    "lang_es": "Español",
    "lang_fr": "Français",
    "lang_ru": "Русский",
    "lang_zh_CN": "简体中文",
    "lang_hi": "हिन्दी",
    "lang_ar": "العربية",
    "lang_pt_BR": "Português (Brasil)",
    "lang_ja": "日本語",
    "group_original": "Оригинал",
    "group_translation_panel": "Превод (за TTS когато е включено „Превод преди говор“)",
    "placeholder_original": (
        "Отворете файл, пишете или ползвайте микрофона. "
        "Можете да редактирате текста преди говор или превод."
    ),
    "placeholder_translation": "Преведен текст. Редактируем. Облачен превод изисква интернет.",
    "group_languages": "Езици",
    "languages_intro": (
        "Преводът поддържа всеки език от Google Translate. "
        "Търсете по-долу, за да стесните дългите списъци; точността на микрофона зависи от избора на "
        "езика, на който <b>говорите</b>."
    ),
    "filter_placeholder": "Филтър по име или код (напр. japanese, ja, hindi, hi)…",
    "btn_clear_filter": "Изчисти филтъра",
    "group_voice_input": "Гласов вход (микрофон)",
    "mic_intro": (
        "Използва Google speech-to-text (интернет + микрофон PyAudio). "
        "Изберете езика, на който <b>говорите</b>, за най-добра точност."
    ),
    "label_i_speak": "Говоря на:",
    "btn_listen": "Слушай → текст",
    "btn_listen_pipeline": "Слушай → превод → говори",
    "btn_save_transcript": "Запис на препис…",
    "btn_save_wav": "Запис на последното аудио…",
    "group_translation_section": "Превод",
    "chk_translate_before": "Превод преди говор (изисква интернет)",
    "label_from": "От:",
    "label_to": "Към:",
    "btn_translate_now": "Преведи сега",
    "btn_swap_langs": "⇄ Размени От / Към",
    "tooltip_swap": (
        'Разменя фиксирани езици. Първо задайте „От“ на конкретен език (не „Открий език“).'
    ),
    "group_audio_control": "Управление на аудио",
    "btn_play": "Пусни",
    "btn_pause": "Пауза",
    "btn_stop": "Спри",
    "btn_prepare_short": "Подготви / Обнови аудио",
    "audio_hint": (
        "Подготовката генерира реч с избрания двигател (SAPI .wav офлайн или Edge neural .mp3 онлайн). "
        "Източник на текст: полето за превод, ако е включено „Превод преди говор“, иначе оригиналът."
    ),
    "group_speech_output": "Гласов изход",
    "engine_sapi": "Windows SAPI (.wav, офлайн)",
    "engine_edge": "Microsoft Edge neural (.mp3, онлайн)",
    "label_engine": "Двигател:",
    "label_sapi_voice": "SAPI глас:",
    "label_edge_voice": "Edge глас:",
    "tooltip_edge_voice": "Оставете „Автоматично по език Към“, за да се избере neural глас за текущия „Към“ език.",
    "label_speed": "Скорост (думи/мин):",
    "label_volume_sapi": "Сила:",
    "hint_edge_volume": "(Edge ползва плъзгача; важи и системната сила.)",
    "lbl_no_file": "Няма отворен файл",
    "btn_open_file": "Отвори файл…",
    "status_ready": "Готово",
    "status_lang_failed": "Списъкът с езици не се зареди.",
    "status_langs_fmt": "{n} езика за превод · {m} избора за микрофон/STT · Готово",
    "status_filter_from": "Няма съвпадение с филтъра — показан е пълният списък „От“.",
    "status_filter_to": "Няма съвпадение с филтъра — показан е пълният списък „Към“.",
    "status_filter_mic": "Няма съвпадение с филтъра — показан е пълният списък за микрофона.",
    "status_history_saved": "Текущите текстове са записани в историята на сесията.",
    "status_history_cleared": "Историята на сесията е изчистена.",
    "swap_title": "Размяна на езици",
    "swap_body": "Първо изберете конкретен език „От“ (не „Открий език“), после разменете с „Към“.",
    "shortcuts_title": "Клавишни комбинации",
    "shortcuts_body": (
        "Ctrl+O — Отваряне на файл\n"
        "Ctrl+Shift+S — Експорт на аудио (WAV със SAPI, MP3 с Edge)\n"
        "Ctrl+Shift+T — Запис на препис\n"
        "Ctrl+Return — Подготовка / обновяване на реч\n"
        "Ctrl+T — Само превод\n"
        "Ctrl+Alt+V — Постави в оригинала\n"
        "Ctrl+Space — Пусни / пауза\n"
        "Esc — Спри възпроизвеждане"
    ),
    "edge_tts_title": "Microsoft Edge TTS",
    "edge_loading": "Зареждане на neural гласове…",
    "edge_auto_voice": "Автоматично (съответства на език „Към“)",
    "playback_title": "Възпроизвеждане",
    "ocr_open_title": "Отваряне на изображение за OCR",
    "ocr_filter": "Изображения (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;Всички файлове (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "OCR неуспех",
    "ocr_no_text": "Не е разпознат текст.",
    "voice_input_title": "Гласов вход",
    "voice_wait_synth": "Изчакайте синтеза на реч да приключи.",
    "voice_empty": "Празно разпознаване — опитайте отново.",
    "voice_input_failed_title": "Гласовият вход се провали",
    "translation_empty_title": "Превод",
    "translation_failed_title": "Преводът се провали",
    "translation_was_empty": "Преводът беше празен.",
    "translate_no_text_title": "Превод",
    "translate_no_text": "Няма текст за превод.",
    "tts_title": "Текст към реч",
    "tts_no_text": "Няма текст за говорене.",
    "tts_synth_running": "Синтезът на реч вече работи.",
    "tts_wait_translate": "Моля, изчакайте преводът да приключи.",
    "speech_synth_failed_title": "Синтезът на реч се провали",
    "save_transcript_title": "Запис на препис",
    "save_transcript_nothing": "Няма какво да се запише.",
    "save_transcript_filter": "Текст (*.txt)",
    "save_transcript_saved": "Записано:\n{path}",
    "save_audio_title": "Запис на аудио",
    "save_audio_no_buffer": "Още няма аудио буфер — ползвайте Подготви или „Слушай → превод → говори“.",
    "save_audio_saved": "Записано:\n{path}",
    "save_audio_error_title": "Запис на аудио",
    "export_audio_title": "Експорт на аудио",
    "export_no_text": "Няма текст за експорт.",
    "export_failed_title": "Експортът се провали",
    "export_saved": "Записано:\n{path}",
    "read_file_error_title": "Файлът не може да се прочете",
    "open_document_title": "Отваряне на документ",
    "open_document_filter": "Документи (*.txt *.doc *.docx *.pdf);;Всички файлове (*.*)",
    "about_dialog_title": "Относно",
    "clear_history_title": "Изчистване на историята",
    "clear_history_confirm": "Премахване на всички записани сесии?",
    "history_dialog_title": "История на сесията",
    "lang_list_error_fmt": "(грешка: {error})",
    "voice_load_error_fmt": "(грешка при зареждане на гласове: {error})",
    "clip_header_original": "--- Оригинал ---",
    "clip_header_translation": "--- Превод ---",
    "transcript_empty_marker": "(празно)",
    "restart_locale_title": "Език на интерфейса",
    "restart_locale_body": (
        "Езикът на интерфейса ще се приложи напълно след рестарт на приложението."
    ),
}

MESSAGES = {**EN, **_BG}
