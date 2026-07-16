"""Spanish UI strings."""

from tts_app.locales.en import MESSAGES as EN

_ES: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>Autor: <b>{author}</b><br/>
Correo: <a href="mailto:{email}">{email}</a><br/>
Empresa: <b>{company}</b></p>
<p>La lista de traducción incluye <b>todos los idiomas</b> de Google Translate (100+). Use el cuadro de búsqueda para encontrar un idioma rápidamente.
El reconocimiento de voz usa Google Web Speech (elija el idioma en el que <b>habla</b>). Las voces de Windows cubren menos idiomas — elija una voz adecuada en Configuración.</p>
<p>Reconocimiento de voz (Google mediante SpeechRecognition), traducción (Google mediante deep-translator)
y síntesis de voz (Windows SAPI) pueden requerir conexión a Internet cuando se indique.</p>
<p>Formatos: .txt, .doc, .docx, .pdf. Ajustes: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>Atajos: Ctrl+O abrir, Ctrl+Mayús+S exportar audio, Ctrl+Mayús+T guardar transcripción, Ctrl+Intro preparar,
Ctrl+T traducir, Ctrl+Espacio reproducir/pausa, Esc detener.</p>""",
    "menu_file": "&Archivo",
    "menu_open": "Abrir…",
    "menu_export_audio": "Exportar audio…",
    "menu_save_transcript_txt": "Guardar transcripción (TXT)…",
    "menu_save_wav_copy": "Guardar último audio (copia WAV)…",
    "menu_open_image_ocr": "Abrir imagen (OCR)…",
    "menu_prepare_refresh": "Preparar / Actualizar audio",
    "menu_translate_only": "Solo traducir",
    "menu_exit": "&Salir",
    "menu_session_history": "Historial de sesión",
    "menu_hist_view": "Ver y restaurar…",
    "menu_hist_add": "Añadir actual al historial",
    "menu_hist_clear": "Borrar todo el historial",
    "menu_edit": "&Editar",
    "menu_copy_original": "Copiar texto original",
    "menu_copy_translation": "Copiar traducción",
    "menu_paste_original": "Pegar en original",
    "menu_replace_from_clipboard": "Reemplazar original desde portapapeles",
    "menu_copy_both": "Copiar original + traducción",
    "menu_help": "A&yuda",
    "menu_interface_language": "Idioma de la interfaz",
    "menu_keyboard_shortcuts": "Atajos de teclado…",
    "menu_about": "Acerca &de",
    "lang_system": "Igual que el idioma de Windows",
    "group_original": "Original",
    "group_translation_panel": "Traducción (para TTS con «Traducir antes de hablar»)",
    "placeholder_original": (
        "Abra un archivo, escriba o use el micrófono. "
        "Puede editar el texto antes de hablar o traducir."
    ),
    "placeholder_translation": "Texto traducido. Editable. La traducción en la nube requiere Internet.",
    "group_languages": "Idiomas",
    "languages_intro": (
        "La traducción admite todos los idiomas de Google Translate. "
        "Busque abajo para acortar listas largas; la precisión del micrófono depende de elegir "
        "el idioma en el que <b>habla</b>."
    ),
    "filter_placeholder": "Filtrar por nombre o código (ej. japanese, ja, hindi, hi)…",
    "btn_clear_filter": "Borrar filtro",
    "group_voice_input": "Entrada de voz (micrófono)",
    "mic_intro": (
        "Usa Google de voz a texto (Internet + micrófono PyAudio). "
        "Elija el idioma en el que <b>habla</b> para mayor precisión."
    ),
    "label_i_speak": "Hablo:",
    "btn_listen": "Escuchar → texto",
    "btn_listen_pipeline": "Escuchar → traducir → hablar",
    "btn_save_transcript": "Guardar transcripción…",
    "btn_save_wav": "Guardar último WAV…",
    "group_translation_section": "Traducción",
    "chk_translate_before": "Traducir antes de hablar (usa Internet)",
    "label_from": "De:",
    "label_to": "A:",
    "btn_translate_now": "Traducir ahora",
    "btn_swap_langs": "⇄ Intercambiar De / A",
    "tooltip_swap": (
        'Intercambia idiomas fijos. Primero fije «De» en un idioma concreto (no «Detectar idioma»).'
    ),
    "group_audio_control": "Control de audio",
    "btn_play": "Reproducir",
    "btn_pause": "Pausa",
    "btn_stop": "Detener",
    "btn_prepare_short": "Preparar / Actualizar audio",
    "audio_hint": (
        "Preparar genera voz con el motor elegido (SAPI .wav sin conexión o Edge neural .mp3 en línea). "
        "Texto: campo traducido si «Traducir antes de hablar» está activo, si no el original."
    ),
    "group_speech_output": "Salida de voz",
    "engine_sapi": "Windows SAPI (.wav, sin conexión)",
    "engine_edge": "Microsoft Edge neural (.mp3, en línea)",
    "label_engine": "Motor:",
    "label_sapi_voice": "Voz SAPI:",
    "label_edge_voice": "Voz Edge:",
    "tooltip_edge_voice": "Deje «Automático según idioma A» para elegir voz neuronal del idioma «A» actual.",
    "label_speed": "Velocidad (palabras/min):",
    "label_volume_sapi": "Volumen (SAPI):",
    "hint_edge_volume": "(Edge usa el volumen del sistema; el control solo afecta a SAPI.)",
    "lbl_no_file": "Ningún archivo cargado",
    "btn_open_file": "Abrir archivo…",
    "status_ready": "Listo",
    "status_lang_failed": "No se pudo cargar la lista de idiomas.",
    "status_langs_fmt": "{n} idiomas de traducción · {m} opciones de micrófono/STT · Listo",
    "status_filter_from": "Sin coincidencias — lista «De» completa.",
    "status_filter_to": "Sin coincidencias — lista «A» completa.",
    "status_filter_mic": "Sin coincidencias — lista de micrófono completa.",
    "status_history_saved": "Textos actuales guardados en el historial de sesión.",
    "status_history_cleared": "Historial de sesión borrado.",
    "swap_title": "Intercambiar idiomas",
    "swap_body": "Elija primero un idioma «De» concreto (no «Detectar idioma»), luego intercambie con «A».",
    "shortcuts_title": "Atajos de teclado",
    "shortcuts_body": (
        "Ctrl+O — Abrir archivo\n"
        "Ctrl+Mayús+S — Exportar audio (WAV con SAPI, MP3 con Edge)\n"
        "Ctrl+Mayús+T — Guardar transcripción\n"
        "Ctrl+Intro — Preparar / actualizar voz\n"
        "Ctrl+T — Solo traducir\n"
        "Ctrl+Alt+V — Pegar en original\n"
        "Ctrl+Espacio — Reproducir / pausa\n"
        "Esc — Detener reproducción"
    ),
    "edge_loading": "Cargando voces neuronales…",
    "edge_auto_voice": "Automático (coincide con idioma «A»)",
    "playback_title": "Reproducción",
    "ocr_open_title": "Abrir imagen para OCR",
    "ocr_filter": "Imágenes (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;Todos los archivos (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "OCR falló",
    "ocr_no_text": "No se reconoció texto.",
    "voice_input_title": "Entrada de voz",
    "voice_wait_synth": "Espere a que termine la síntesis de voz.",
    "voice_empty": "Reconocimiento vacío — inténtelo de nuevo.",
    "voice_input_failed_title": "Entrada de voz falló",
    "translation_empty_title": "Traducción",
    "translation_failed_title": "Traducción falló",
    "translate_no_text_title": "Traducir",
    "translate_no_text": "No hay texto para traducir.",
    "tts_title": "Texto a voz",
    "tts_no_text": "No hay texto para hablar.",
    "tts_synth_running": "La síntesis de voz ya está en ejecución.",
    "tts_wait_translate": "Espere a que termine la traducción.",
    "speech_synth_failed_title": "Síntesis de voz falló",
    "save_transcript_title": "Guardar transcripción",
    "save_transcript_nothing": "Nada que guardar.",
    "save_transcript_filter": "Texto (*.txt)",
    "save_transcript_saved": "Guardado:\n{path}",
    "save_audio_title": "Guardar audio",
    "save_audio_no_buffer": "Aún no hay búfer de audio — use Preparar o «Escuchar → traducir → hablar».",
    "save_audio_saved": "Guardado:\n{path}",
    "save_audio_error_title": "Guardar audio",
    "export_audio_title": "Exportar audio",
    "export_no_text": "No hay texto para exportar.",
    "export_failed_title": "Exportación falló",
    "export_saved": "Guardado:\n{path}",
    "read_file_error_title": "No se pudo leer el archivo",
    "open_document_title": "Abrir documento",
    "open_document_filter": "Documentos (*.txt *.doc *.docx *.pdf);;Todos los archivos (*.*)",
    "about_dialog_title": "Acerca de",
    "clear_history_title": "Borrar historial",
    "clear_history_confirm": "¿Eliminar todas las sesiones guardadas?",
    "history_dialog_title": "Historial de sesión",
    "lang_list_error_fmt": "(error: {error})",
    "clip_header_original": "--- Original ---",
    "clip_header_translation": "--- Traducción ---",
    "transcript_empty_marker": "(vacío)",
    "restart_locale_title": "Idioma de la interfaz",
    "restart_locale_body": (
        "El idioma de la interfaz se aplicará por completo después de reiniciar la aplicación."
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
    "detect_language": "Detectar idioma",
    "translation_was_empty": "La traducción estaba vacía.",
    "voice_load_error_fmt": "(error al cargar voces: {error})",
}

MESSAGES = {**EN, **_ES}
