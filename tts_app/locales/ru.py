"""Russian UI strings."""

from tts_app.locales.en import MESSAGES as EN

_RU: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>Автор: <b>{author}</b><br/>
Электронная почта: <a href="mailto:{email}">{email}</a><br/>
Компания: <b>{company}</b></p>
<p>Список переводов включает <b>все языки</b> Google Translate (100+). Используйте поиск, чтобы быстро найти язык.
Распознавание речи использует Google Web Speech (выберите язык, на котором вы <b>говорите</b>). Голоса Windows поддерживают меньше языков — выберите подходящий голос в настройках.</p>
<p>Распознавание речи (Google через SpeechRecognition), перевод (Google через deep-translator)
и синтез речи (Windows SAPI) могут требовать подключения к Интернету.</p>
<p>Форматы документов: .txt, .doc, .docx, .pdf. Настройки: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>Сочетания: Ctrl+O открыть, Ctrl+Shift+S экспорт аудио, Ctrl+Shift+T сохранить расшифровку, Ctrl+Enter подготовка,
Ctrl+T перевод, Ctrl+Пробел воспроизведение/пауза, Esc стоп.</p>""",
    "menu_file": "&Файл",
    "menu_open": "Открыть…",
    "menu_export_audio": "Экспорт аудио…",
    "menu_save_transcript_txt": "Сохранить расшифровку (TXT)…",
    "menu_save_wav_copy": "Сохранить последнее аудио (копия WAV)…",
    "menu_open_image_ocr": "Открыть изображение (OCR)…",
    "menu_prepare_refresh": "Подготовить / Обновить аудио",
    "menu_translate_only": "Только перевод",
    "menu_exit": "В&ыход",
    "menu_session_history": "История сеанса",
    "menu_hist_view": "Просмотр и восстановление…",
    "menu_hist_add": "Добавить текущее в историю",
    "menu_hist_clear": "Очистить всю историю",
    "menu_edit": "&Правка",
    "menu_copy_original": "Копировать исходный текст",
    "menu_copy_translation": "Копировать перевод",
    "menu_paste_original": "Вставить в оригинал",
    "menu_replace_from_clipboard": "Заменить оригинал из буфера",
    "menu_copy_both": "Копировать оригинал + перевод",
    "menu_help": "&Справка",
    "menu_interface_language": "Язык интерфейса",
    "menu_keyboard_shortcuts": "Сочетания клавиш…",
    "menu_about": "&О программе",
    "lang_system": "Как язык Windows",
    "group_original": "Оригинал",
    "group_translation_panel": "Перевод (для синтеза при включённом «Переводить перед речью»)",
    "placeholder_original": (
        "Откройте файл, введите текст или используйте микрофон. "
        "Текст можно править до озвучивания или перевода."
    ),
    "placeholder_translation": "Переведённый текст. Редактируется. Облачный перевод требует Интернет.",
    "group_languages": "Языки",
    "languages_intro": (
        "Перевод поддерживает все языки Google Translate. "
        "Ищите ниже, чтобы сузить длинные списки; точность микрофона зависит от выбора "
        "языка, на котором вы <b>говорите</b>."
    ),
    "filter_placeholder": "Фильтр по имени или коду (напр. japanese, ja, hindi, hi)…",
    "btn_clear_filter": "Сбросить фильтр",
    "group_voice_input": "Голосовой ввод (микрофон)",
    "mic_intro": (
        "Использует Google speech-to-text (Интернет + микрофон PyAudio). "
        "Выберите язык, на котором вы <b>говорите</b>, для лучшей точности."
    ),
    "label_i_speak": "Я говорю на:",
    "btn_listen": "Слушать → текст",
    "btn_listen_pipeline": "Слушать → перевести → произнести",
    "btn_save_transcript": "Сохранить расшифровку…",
    "btn_save_wav": "Сохранить последний WAV…",
    "group_translation_section": "Перевод",
    "chk_translate_before": "Переводить перед речью (нужен Интернет)",
    "label_from": "С:",
    "label_to": "На:",
    "btn_translate_now": "Перевести сейчас",
    "btn_swap_langs": "⇄ Поменять С / На",
    "tooltip_swap": (
        'Меняет фиксированные языки. Сначала задайте «С» на конкретный язык (не «Определить язык»).'
    ),
    "group_audio_control": "Управление аудио",
    "btn_play": "Воспр.",
    "btn_pause": "Пауза",
    "btn_stop": "Стоп",
    "btn_prepare_short": "Подготовить / Обновить аудио",
    "audio_hint": (
        "Подготовка создаёт речь выбранным движком (SAPI .wav офлайн или Edge neural .mp3 онлайн). "
        "Источник текста: поле перевода, если включено «Переводить перед речью», иначе оригинал."
    ),
    "group_speech_output": "Речевой выход",
    "engine_sapi": "Windows SAPI (.wav, офлайн)",
    "engine_edge": "Microsoft Edge neural (.mp3, онлайн)",
    "label_engine": "Движок:",
    "label_sapi_voice": "Голос SAPI:",
    "label_edge_voice": "Голос Edge:",
    "tooltip_edge_voice": "Оставьте «Авто по языку На», чтобы выбрать нейроголос для текущего языка «На».",
    "label_speed": "Скорость (слов/мин):",
    "label_volume_sapi": "Громкость (SAPI):",
    "hint_edge_volume": "(Edge использует системную громкость; ползунок влияет только на SAPI.)",
    "lbl_no_file": "Файл не загружен",
    "btn_open_file": "Открыть файл…",
    "status_ready": "Готово",
    "status_lang_failed": "Не удалось загрузить список языков.",
    "status_langs_fmt": "{n} языков перевода · {m} вариантов микрофона/STT · Готово",
    "status_filter_from": "Нет совпадений — полный список «С».",
    "status_filter_to": "Нет совпадений — полный список «На».",
    "status_filter_mic": "Нет совпадений — полный список микрофона.",
    "status_history_saved": "Текущие тексты сохранены в истории сеанса.",
    "status_history_cleared": "История сеанса очищена.",
    "swap_title": "Поменять языки",
    "swap_body": "Сначала выберите конкретный язык «С» (не «Определить язык»), затем поменяйте с «На».",
    "shortcuts_title": "Сочетания клавиш",
    "shortcuts_body": (
        "Ctrl+O — Открыть файл\n"
        "Ctrl+Shift+S — Экспорт аудио (WAV через SAPI, MP3 через Edge)\n"
        "Ctrl+Shift+T — Сохранить расшифровку\n"
        "Ctrl+Enter — Подготовить / обновить речь\n"
        "Ctrl+T — Только перевод\n"
        "Ctrl+Alt+V — Вставить в оригинал\n"
        "Ctrl+Пробел — Воспроизведение / пауза\n"
        "Esc — Остановить воспроизведение"
    ),
    "edge_loading": "Загрузка нейроголосов…",
    "edge_auto_voice": "Авто (по языку «На»)",
    "playback_title": "Воспроизведение",
    "ocr_open_title": "Открыть изображение для OCR",
    "ocr_filter": "Изображения (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;Все файлы (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "Ошибка OCR",
    "ocr_no_text": "Текст не распознан.",
    "voice_input_title": "Голосовой ввод",
    "voice_wait_synth": "Дождитесь окончания синтеза речи.",
    "voice_empty": "Пустое распознавание — повторите попытку.",
    "voice_input_failed_title": "Ошибка голосового ввода",
    "translation_empty_title": "Перевод",
    "translation_failed_title": "Ошибка перевода",
    "translate_no_text_title": "Перевод",
    "translate_no_text": "Нет текста для перевода.",
    "tts_title": "Синтез речи",
    "tts_no_text": "Нет текста для озвучивания.",
    "tts_synth_running": "Синтез речи уже выполняется.",
    "tts_wait_translate": "Дождитесь окончания перевода.",
    "speech_synth_failed_title": "Ошибка синтеза речи",
    "save_transcript_title": "Сохранить расшифровку",
    "save_transcript_nothing": "Нечего сохранять.",
    "save_transcript_filter": "Текст (*.txt)",
    "save_transcript_saved": "Сохранено:\n{path}",
    "save_audio_title": "Сохранить аудио",
    "save_audio_no_buffer": "Буфера аудио ещё нет — используйте Подготовить или «Слушать → перевести → произнести».",
    "save_audio_saved": "Сохранено:\n{path}",
    "save_audio_error_title": "Сохранение аудио",
    "export_audio_title": "Экспорт аудио",
    "export_no_text": "Нет текста для экспорта.",
    "export_failed_title": "Ошибка экспорта",
    "export_saved": "Сохранено:\n{path}",
    "read_file_error_title": "Не удалось прочитать файл",
    "open_document_title": "Открыть документ",
    "open_document_filter": "Документы (*.txt *.doc *.docx *.pdf);;Все файлы (*.*)",
    "about_dialog_title": "О программе",
    "clear_history_title": "Очистить историю",
    "clear_history_confirm": "Удалить все сохранённые сеансы?",
    "history_dialog_title": "История сеанса",
    "lang_list_error_fmt": "(ошибка: {error})",
    "clip_header_original": "--- Оригинал ---",
    "clip_header_translation": "--- Перевод ---",
    "transcript_empty_marker": "(пусто)",
    "restart_locale_title": "Язык интерфейса",
    "restart_locale_body": (
        "Язык интерфейса полностью применится после перезапуска приложения."
    ),
    "window_title_fmt": "{app} — {author} · {company}",
    "edge_tts_title": "Microsoft Edge TTS",
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
    "detect_language": "Определить язык",
    "translation_was_empty": "Перевод был пустым.",
    "voice_load_error_fmt": "(ошибка загрузки голосов: {error})",
}

MESSAGES = {**EN, **_RU}
