"""German UI strings."""

from tts_app.locales.en import MESSAGES as EN

_DE: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>Autor: <b>{author}</b><br/>
E-Mail: <a href="mailto:{email}">{email}</a><br/>
Firma: <b>{company}</b></p>
<p>Die Übersetzungsliste umfasst <b>alle Sprachen</b> von Google Translate (100+). Nutzen Sie die Suche, um schnell eine Sprache zu finden.
Die Spracherkennung nutzt Google Web Speech (wählen Sie Ihre <b>gesprochene</b> Sprache). Windows-Stimmen decken weniger Sprachen ab — wählen Sie in den Einstellungen eine passende Stimme.</p>
<p>Spracherkennung (Google über SpeechRecognition), Übersetzung (Google über deep-translator)
und Sprachsynthese (Windows SAPI) können je nach Funktion eine Internetverbindung benötigen.</p>
<p>Dokumentformate: .txt, .doc, .docx, .pdf. Einstellungen: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>Tastenkürzel: Strg+O öffnen, Strg+Umsch+S Audio exportieren, Strg+Umsch+T Transkript speichern, Strg+Enter vorbereiten,
Strg+T übersetzen, Strg+Leertaste wiedergeben/pause, Esc stopp.</p>""",
    "menu_file": "&Datei",
    "menu_open": "Öffnen…",
    "menu_export_audio": "Audio exportieren…",
    "menu_save_transcript_txt": "Transkript speichern (TXT)…",
    "menu_save_wav_copy": "Letztes Audio speichern (WAV-Kopie)…",
    "menu_open_image_ocr": "Bild öffnen (OCR)…",
    "menu_prepare_refresh": "Audio vorbereiten / aktualisieren",
    "menu_translate_only": "Nur übersetzen",
    "menu_exit": "B&eenden",
    "menu_session_history": "Sitzungsverlauf",
    "menu_hist_view": "Anzeigen & wiederherstellen…",
    "menu_hist_add": "Aktuelles zum Verlauf hinzufügen",
    "menu_hist_clear": "Gesamten Verlauf löschen",
    "menu_edit": "&Bearbeiten",
    "menu_copy_original": "Originaltext kopieren",
    "menu_copy_translation": "Übersetzung kopieren",
    "menu_paste_original": "In Original einfügen",
    "menu_replace_from_clipboard": "Original aus Zwischenablage ersetzen",
    "menu_copy_both": "Original + Übersetzung kopieren",
    "menu_help": "&Hilfe",
    "menu_interface_language": "Oberflächensprache",
    "menu_keyboard_shortcuts": "Tastenkürzel…",
    "menu_about": "&Info",
    "lang_system": "Wie Windows-Sprache",
    "group_original": "Original",
    "group_translation_panel": "Übersetzung (für TTS wenn „Vor dem Sprechen übersetzen“ aktiv)",
    "placeholder_original": (
        "Datei öffnen, tippen oder Mikrofon nutzen. "
        "Sie können den Text vor dem Sprechen oder Übersetzen bearbeiten."
    ),
    "placeholder_translation": "Übersetzter Text. Bearbeitbar. Cloud-Übersetzung erfordert Internet.",
    "group_languages": "Sprachen",
    "languages_intro": (
        "Übersetzung unterstützt alle Sprachen von Google Translate. "
        "Filtern Sie unten lange Listen; die Mikrofon-Genauigkeit hängt davon ab, "
        "dass Sie die Sprache wählen, in der Sie <b>sprechen</b>."
    ),
    "filter_placeholder": "Nach Name oder Code filtern (z. B. japanese, ja, hindi, hi)…",
    "btn_clear_filter": "Filter löschen",
    "group_voice_input": "Spracheingabe (Mikrofon)",
    "mic_intro": (
        "Nutzt Google Sprache-zu-Text (Internet + PyAudio-Mikrofon). "
        "Wählen Sie die Sprache, in der Sie <b>sprechen</b>, für beste Ergebnisse."
    ),
    "label_i_speak": "Ich spreche:",
    "btn_listen": "Hören → Text",
    "btn_listen_pipeline": "Hören → übersetzen → sprechen",
    "btn_save_transcript": "Transkript speichern…",
    "btn_save_wav": "Letzte WAV speichern…",
    "group_translation_section": "Übersetzung",
    "chk_translate_before": "Vor dem Sprechen übersetzen (Internet)",
    "label_from": "Von:",
    "label_to": "Nach:",
    "btn_translate_now": "Jetzt übersetzen",
    "btn_swap_langs": "⇄ Von / Nach tauschen",
    "tooltip_swap": (
        'Feste Sprachen tauschen. Legen Sie zuerst „Von“ auf eine konkrete Sprache (nicht „Sprache erkennen“).'
    ),
    "group_audio_control": "Audiosteuerung",
    "btn_play": "Wiedergabe",
    "btn_pause": "Pause",
    "btn_stop": "Stopp",
    "btn_prepare_short": "Audio vorbereiten / aktualisieren",
    "audio_hint": (
        "Vorbereiten erzeugt Sprache mit dem gewählten Modul (SAPI .wav offline oder Edge neural .mp3 online). "
        "Textquelle: Übersetzungsfeld, wenn „Vor dem Sprechen übersetzen“ an ist, sonst Original."
    ),
    "group_speech_output": "Sprachausgabe",
    "engine_sapi": "Windows SAPI (.wav, offline)",
    "engine_edge": "Microsoft Edge neural (.mp3, online)",
    "label_engine": "Modul:",
    "label_sapi_voice": "SAPI-Stimme:",
    "label_edge_voice": "Edge-Stimme:",
    "tooltip_edge_voice": "„Automatisch nach Nach-Sprache“ für eine neurale Stimme zur aktuellen „Nach“-Sprache.",
    "label_speed": "Geschwindigkeit (Wörter/min):",
    "label_volume_sapi": "Lautstärke (SAPI):",
    "hint_edge_volume": "(Edge nutzt die Systemlautstärke; der Schieberegler gilt nur für SAPI.)",
    "lbl_no_file": "Keine Datei geladen",
    "btn_open_file": "Datei öffnen…",
    "status_ready": "Bereit",
    "status_lang_failed": "Sprachenliste konnte nicht geladen werden.",
    "status_langs_fmt": "{n} Übersetzungssprachen · {m} Mikrofon/STT-Optionen · Bereit",
    "status_filter_from": "Kein Treffer für Filter — vollständige „Von“-Liste.",
    "status_filter_to": "Kein Treffer für Filter — vollständige „Nach“-Liste.",
    "status_filter_mic": "Kein Treffer für Filter — vollständige Mikrofonliste.",
    "status_history_saved": "Aktuelle Texte im Sitzungsverlauf gespeichert.",
    "status_history_cleared": "Sitzungsverlauf gelöscht.",
    "swap_title": "Sprachen tauschen",
    "swap_body": 'Wählen Sie zuerst eine konkrete „Von“-Sprache (nicht „Sprache erkennen“), dann mit „Nach“ tauschen.',
    "shortcuts_title": "Tastenkürzel",
    "shortcuts_body": (
        "Strg+O — Datei öffnen\n"
        "Strg+Umsch+S — Audio exportieren (WAV mit SAPI, MP3 mit Edge)\n"
        "Strg+Umsch+T — Transkript speichern\n"
        "Strg+Enter — Sprache vorbereiten / aktualisieren\n"
        "Strg+T — Nur übersetzen\n"
        "Strg+Alt+V — In Original einfügen\n"
        "Strg+Leertaste — Wiedergabe / Pause\n"
        "Esc — Wiedergabe stoppen"
    ),
    "edge_loading": "Neurale Stimmen werden geladen…",
    "edge_auto_voice": "Automatisch (entspricht „Nach“-Sprache)",
    "playback_title": "Wiedergabe",
    "ocr_open_title": "Bild für OCR öffnen",
    "ocr_filter": "Bilder (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;Alle Dateien (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "OCR fehlgeschlagen",
    "ocr_no_text": "Kein Text erkannt.",
    "voice_input_title": "Spracheingabe",
    "voice_wait_synth": "Warten Sie, bis die Sprachsynthese beendet ist.",
    "voice_empty": "Leere Erkennung — erneut versuchen.",
    "voice_input_failed_title": "Spracheingabe fehlgeschlagen",
    "translation_empty_title": "Übersetzung",
    "translation_failed_title": "Übersetzung fehlgeschlagen",
    "translate_no_text_title": "Übersetzen",
    "translate_no_text": "Kein Text zum Übersetzen.",
    "tts_title": "Text zu Sprache",
    "tts_no_text": "Kein Text zum Sprechen.",
    "tts_synth_running": "Sprachsynthese läuft bereits.",
    "tts_wait_translate": "Bitte warten Sie, bis die Übersetzung fertig ist.",
    "speech_synth_failed_title": "Sprachsynthese fehlgeschlagen",
    "save_transcript_title": "Transkript speichern",
    "save_transcript_nothing": "Nichts zu speichern.",
    "save_transcript_filter": "Text (*.txt)",
    "save_transcript_saved": "Gespeichert:\n{path}",
    "save_audio_title": "Audio speichern",
    "save_audio_no_buffer": "Noch kein Audiopuffer — „Vorbereiten“ oder „Hören → übersetzen → sprechen“ nutzen.",
    "save_audio_saved": "Gespeichert:\n{path}",
    "save_audio_error_title": "Audio speichern",
    "export_audio_title": "Audio exportieren",
    "export_no_text": "Kein Text zum Exportieren.",
    "export_failed_title": "Export fehlgeschlagen",
    "export_saved": "Gespeichert:\n{path}",
    "read_file_error_title": "Datei konnte nicht gelesen werden",
    "open_document_title": "Dokument öffnen",
    "open_document_filter": "Dokumente (*.txt *.doc *.docx *.pdf);;Alle Dateien (*.*)",
    "about_dialog_title": "Info",
    "clear_history_title": "Verlauf löschen",
    "clear_history_confirm": "Alle gespeicherten Sitzungen entfernen?",
    "history_dialog_title": "Sitzungsverlauf",
    "lang_list_error_fmt": "(Fehler: {error})",
    "clip_header_original": "--- Original ---",
    "clip_header_translation": "--- Übersetzung ---",
    "transcript_empty_marker": "(leer)",
    "restart_locale_title": "Oberflächensprache",
    "restart_locale_body": (
        "Die Oberflächensprache wird nach einem Neustart der Anwendung vollständig angewendet."
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
    "detect_language": "Sprache erkennen",
    "translation_was_empty": "Übersetzung war leer.",
    "voice_load_error_fmt": "(Fehler beim Laden der Stimmen: {error})",
}

MESSAGES = {**EN, **_DE}
