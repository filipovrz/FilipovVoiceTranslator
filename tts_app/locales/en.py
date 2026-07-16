"""English UI strings (source locale)."""

MESSAGES: dict[str, str] = {
    "window_title_fmt": "{app} — {author} · {company}",
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>Author: <b>{author}</b><br/>
Email: <a href="mailto:{email}">{email}</a><br/>
Company: <b>{company}</b></p>
<p>Translation lists <b>all languages</b> offered by Google Translate (100+). Use the filter box to find a language quickly.
Speech recognition uses Google Web Speech (pick the language you speak). Windows voices cover fewer languages — for Bulgarian speech prefer Microsoft Edge neural (Kalina/Borislav).</p>
<p>Speech recognition (Google via SpeechRecognition), translation (Google via deep-translator),
and speech synthesis (Windows SAPI) may require an internet connection where noted.</p>
<p>Document formats: .txt, .doc, .docx, .pdf. Settings: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>Shortcuts: Ctrl+O open, Ctrl+Shift+S export audio, Ctrl+Shift+T save transcript, Ctrl+Return prepare,
Ctrl+T translate, Ctrl+Space play/pause, Esc stop.</p>""",
    "menu_file": "&File",
    "menu_open": "Open…",
    "menu_export_audio": "Export audio…",
    "menu_save_transcript_txt": "Save transcript (TXT)…",
    "menu_save_wav_copy": "Save last audio (copy)…",
    "menu_open_image_ocr": "Open image (OCR)…",
    "menu_prepare_refresh": "Prepare / Refresh audio",
    "menu_translate_only": "Translate only",
    "menu_exit": "E&xit",
    "menu_session_history": "Session history",
    "menu_hist_view": "View & restore…",
    "menu_hist_add": "Add current to history",
    "menu_hist_clear": "Clear all history",
    "menu_edit": "&Edit",
    "menu_copy_original": "Copy original text",
    "menu_copy_translation": "Copy translation text",
    "menu_paste_original": "Paste into original",
    "menu_replace_from_clipboard": "Replace original from clipboard",
    "menu_copy_both": "Copy original + translation",
    "menu_help": "&Help",
    "menu_interface_language": "Interface language",
    "menu_keyboard_shortcuts": "Keyboard shortcuts…",
    "menu_about": "&About",
    "detect_language": "Detect language",
    "lang_system": "Match Windows language",
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
    "group_original": "Original",
    "group_translation_panel": "Translation (for TTS when “Translate before speech” is on)",
    "placeholder_original": (
        "Open a file, type, or use the microphone. "
        "You can edit the text before speaking or translating."
    ),
    "placeholder_translation": "Translated text. Editable. Requires internet for cloud translation.",
    "group_languages": "Languages",
    "languages_intro": (
        "Translation supports every language offered by Google Translate. "
        "Search below to narrow long lists; microphone accuracy depends on picking "
        "the language you <b>speak</b>."
    ),
    "filter_placeholder": "Filter by name or code (e.g. japanese, ja, hindi, hi)…",
    "btn_clear_filter": "Clear filter",
    "group_voice_input": "Voice input (microphone)",
    "mic_intro": (
        "Uses Google speech-to-text (internet + PyAudio microphone). "
        "Pick the language you <b>speak</b> for best accuracy."
    ),
    "label_i_speak": "I speak:",
    "btn_listen": "Listen → text",
    "btn_listen_pipeline": "Listen → translate → speak",
    "btn_save_transcript": "Save transcript…",
    "btn_save_wav": "Save last audio…",
    "group_translation_section": "Translation",
    "chk_translate_before": "Translate before speech (uses internet)",
    "label_from": "From:",
    "label_to": "To:",
    "btn_translate_now": "Translate now",
    "btn_swap_langs": "⇄ Swap From / To",
    "tooltip_swap": (
        'Swap fixed languages. Set "From" to a specific language (not "Detect language") first.'
    ),
    "group_audio_control": "Audio control",
    "btn_play": "Play",
    "btn_pause": "Pause",
    "btn_stop": "Stop",
    "btn_prepare_short": "Prepare / Refresh audio",
    "audio_hint": (
        "Prepare builds speech using the selected engine (SAPI .wav offline, or Edge neural .mp3 online). "
        "Text source: translated field if “Translate before speech” is on, otherwise original."
    ),
    "group_speech_output": "Speech output",
    "engine_sapi": "Windows SAPI (.wav, offline)",
    "engine_edge": "Microsoft Edge neural (.mp3, online)",
    "label_engine": "Engine:",
    "label_sapi_voice": "SAPI voice:",
    "label_edge_voice": "Edge voice:",
    "tooltip_edge_voice": 'Leave “Auto by To-language” to pick a neural voice for the current “To” language.',
    "label_speed": "Speed (words/min):",
    "label_volume_sapi": "Volume:",
    "hint_edge_volume": "(Edge volume uses the slider; system volume also applies.)",
    "lbl_no_file": "No file loaded",
    "btn_open_file": "Open file…",
    "status_ready": "Ready",
    "status_lang_failed": "Language list failed to load.",
    "status_langs_fmt": "{n} translation languages · {m} microphone/STT choices · Ready",
    "status_filter_from": "No match for filter — showing full From list.",
    "status_filter_to": "No match for filter — showing full To list.",
    "status_filter_mic": "No match for filter — showing full microphone list.",
    "status_history_saved": "Saved current texts to session history.",
    "status_history_cleared": "Session history cleared.",
    "swap_title": "Swap languages",
    "swap_body": 'Choose a specific “From” language first (not “Detect language”), then swap with “To”.',
    "shortcuts_title": "Keyboard shortcuts",
    "shortcuts_body": (
        "Ctrl+O — Open file\n"
        "Ctrl+Shift+S — Export audio (WAV with SAPI, MP3 with Edge)\n"
        "Ctrl+Shift+T — Save transcript\n"
        "Ctrl+Return — Prepare / refresh speech\n"
        "Ctrl+T — Translate only\n"
        "Ctrl+Alt+V — Paste into original\n"
        "Ctrl+Space — Play / pause\n"
        "Esc — Stop playback"
    ),
    "edge_tts_title": "Microsoft Edge TTS",
    "edge_loading": "Loading neural voices…",
    "edge_auto_voice": "Auto (matches “To” language)",
    "playback_title": "Playback",
    "ocr_open_title": "Open image for OCR",
    "ocr_filter": "Images (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;All files (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "OCR failed",
    "ocr_no_text": "No text recognized.",
    "voice_input_title": "Voice input",
    "voice_wait_synth": "Wait for speech synthesis to finish.",
    "voice_empty": "Empty recognition — try again.",
    "voice_input_failed_title": "Voice input failed",
    "translation_empty_title": "Translation",
    "translation_failed_title": "Translation failed",
    "translation_was_empty": "Translation was empty.",
    "translate_no_text_title": "Translate",
    "translate_no_text": "No text to translate.",
    "tts_title": "Text to Speech",
    "tts_no_text": "No text to speak.",
    "tts_synth_running": "Speech synthesis is already running.",
    "tts_wait_translate": "Please wait for translation to finish.",
    "speech_synth_failed_title": "Speech synthesis failed",
    "save_transcript_title": "Save transcript",
    "save_transcript_nothing": "Nothing to save.",
    "save_transcript_filter": "Text (*.txt)",
    "save_transcript_saved": "Saved:\n{path}",
    "save_audio_title": "Save audio",
    "save_audio_no_buffer": "No audio buffer yet — use Prepare or “Listen → translate → speak”.",
    "save_audio_saved": "Saved:\n{path}",
    "save_audio_error_title": "Save audio",
    "export_audio_title": "Export audio",
    "export_no_text": "No text to export.",
    "export_failed_title": "Export failed",
    "export_saved": "Saved:\n{path}",
    "read_file_error_title": "Could not read file",
    "open_document_title": "Open document",
    "open_document_filter": "Documents (*.txt *.doc *.docx *.pdf);;All files (*.*)",
    "about_dialog_title": "About",
    "clear_history_title": "Clear history",
    "clear_history_confirm": "Remove all saved sessions?",
    "history_dialog_title": "Session history",
    "lang_list_error_fmt": "(error: {error})",
    "voice_load_error_fmt": "(error loading voices: {error})",
    "clip_header_original": "--- Original ---",
    "clip_header_translation": "--- Translation ---",
    "transcript_empty_marker": "(empty)",
    "restart_locale_title": "Interface language",
    "restart_locale_body": (
        "The interface language will fully apply after you restart the application."
    ),
}
