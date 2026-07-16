"""French UI strings."""

from tts_app.locales.en import MESSAGES as EN

_FR: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>Auteur : <b>{author}</b><br/>
E-mail : <a href="mailto:{email}">{email}</a><br/>
Société : <b>{company}</b></p>
<p>La liste des langues couvre <b>toutes les langues</b> proposées par Google Translate (100+). Utilisez la recherche pour trouver une langue rapidement.
La reconnaissance vocale utilise Google Web Speech (choisissez la langue que vous <b>parlez</b>). Les voix Windows couvrent moins de langues — choisissez une voix adaptée dans les paramètres.</p>
<p>Reconnaissance vocale (Google via SpeechRecognition), traduction (Google via deep-translator)
et synthèse vocale (Windows SAPI) peuvent nécessiter une connexion Internet selon les fonctions.</p>
<p>Formats : .txt, .doc, .docx, .pdf. Paramètres : <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>Raccourcis : Ctrl+O ouvrir, Ctrl+Maj+S exporter l’audio, Ctrl+Maj+T enregistrer la transcription, Ctrl+Entrée préparer,
Ctrl+T traduire, Ctrl+Espace lecture/pause, Échap arrêter.</p>""",
    "menu_file": "&Fichier",
    "menu_open": "Ouvrir…",
    "menu_export_audio": "Exporter l’audio…",
    "menu_save_transcript_txt": "Enregistrer la transcription (TXT)…",
    "menu_save_wav_copy": "Enregistrer le dernier audio (copie WAV)…",
    "menu_open_image_ocr": "Ouvrir une image (OCR)…",
    "menu_prepare_refresh": "Préparer / Actualiser l’audio",
    "menu_translate_only": "Traduire uniquement",
    "menu_exit": "&Quitter",
    "menu_session_history": "Historique de session",
    "menu_hist_view": "Afficher et restaurer…",
    "menu_hist_add": "Ajouter l’actuel à l’historique",
    "menu_hist_clear": "Effacer tout l’historique",
    "menu_edit": "&Édition",
    "menu_copy_original": "Copier le texte original",
    "menu_copy_translation": "Copier la traduction",
    "menu_paste_original": "Coller dans l’original",
    "menu_replace_from_clipboard": "Remplacer l’original depuis le presse-papiers",
    "menu_copy_both": "Copier original + traduction",
    "menu_help": "&Aide",
    "menu_interface_language": "Langue de l’interface",
    "menu_keyboard_shortcuts": "Raccourcis clavier…",
    "menu_about": "À &propos",
    "lang_system": "Comme la langue Windows",
    "group_original": "Original",
    "group_translation_panel": "Traduction (pour la synthèse si « Traduire avant de parler » est activé)",
    "placeholder_original": (
        "Ouvrez un fichier, saisissez du texte ou utilisez le microphone. "
        "Vous pouvez modifier le texte avant de parler ou de traduire."
    ),
    "placeholder_translation": "Texte traduit. Modifiable. La traduction cloud nécessite Internet.",
    "group_languages": "Langues",
    "languages_intro": (
        "La traduction prend en charge toutes les langues Google Translate. "
        "Filtrez ci-dessous pour raccourcir les listes ; la précision du microphone dépend du choix "
        "de la langue que vous <b>parlez</b>."
    ),
    "filter_placeholder": "Filtrer par nom ou code (ex. japanese, ja, hindi, hi)…",
    "btn_clear_filter": "Effacer le filtre",
    "group_voice_input": "Entrée vocale (microphone)",
    "mic_intro": (
        "Utilise Google speech-to-text (Internet + microphone PyAudio). "
        "Choisissez la langue que vous <b>parlez</b> pour une meilleure précision."
    ),
    "label_i_speak": "Je parle :",
    "btn_listen": "Écouter → texte",
    "btn_listen_pipeline": "Écouter → traduire → parler",
    "btn_save_transcript": "Enregistrer la transcription…",
    "btn_save_wav": "Enregistrer le dernier WAV…",
    "group_translation_section": "Traduction",
    "chk_translate_before": "Traduire avant de parler (Internet)",
    "label_from": "De :",
    "label_to": "Vers :",
    "btn_translate_now": "Traduire maintenant",
    "btn_swap_langs": "⇄ Échanger De / Vers",
    "tooltip_swap": (
        'Échange les langues fixes. Réglez d’abord « De » sur une langue précise (pas « Détecter la langue »).'
    ),
    "group_audio_control": "Contrôle audio",
    "btn_play": "Lecture",
    "btn_pause": "Pause",
    "btn_stop": "Arrêt",
    "btn_prepare_short": "Préparer / Actualiser l’audio",
    "audio_hint": (
        "Préparer génère la voix avec le moteur choisi (SAPI .wav hors ligne ou Edge neural .mp3 en ligne). "
        "Source : champ traduit si « Traduire avant de parler » est activé, sinon l’original."
    ),
    "group_speech_output": "Sortie vocale",
    "engine_sapi": "Windows SAPI (.wav, hors ligne)",
    "engine_edge": "Microsoft Edge neural (.mp3, en ligne)",
    "label_engine": "Moteur :",
    "label_sapi_voice": "Voix SAPI :",
    "label_edge_voice": "Voix Edge :",
    "tooltip_edge_voice": "Laissez « Auto selon la langue Vers » pour une voix neurale adaptée à « Vers ».",
    "label_speed": "Vitesse (mots/min) :",
    "label_volume_sapi": "Volume (SAPI) :",
    "hint_edge_volume": "(Edge utilise le volume système ; le curseur n’affecte que SAPI.)",
    "lbl_no_file": "Aucun fichier chargé",
    "btn_open_file": "Ouvrir un fichier…",
    "status_ready": "Prêt",
    "status_lang_failed": "Échec du chargement de la liste des langues.",
    "status_langs_fmt": "{n} langues de traduction · {m} choix micro/STT · Prêt",
    "status_filter_from": "Aucune correspondance — liste « De » complète.",
    "status_filter_to": "Aucune correspondance — liste « Vers » complète.",
    "status_filter_mic": "Aucune correspondance — liste microphone complète.",
    "status_history_saved": "Textes actuels enregistrés dans l’historique de session.",
    "status_history_cleared": "Historique de session effacé.",
    "swap_title": "Échanger les langues",
    "swap_body": "Choisissez d’abord une langue « De » précise (pas « Détecter la langue »), puis échangez avec « Vers ».",
    "shortcuts_title": "Raccourcis clavier",
    "shortcuts_body": (
        "Ctrl+O — Ouvrir un fichier\n"
        "Ctrl+Maj+S — Exporter l’audio (WAV avec SAPI, MP3 avec Edge)\n"
        "Ctrl+Maj+T — Enregistrer la transcription\n"
        "Ctrl+Entrée — Préparer / actualiser la voix\n"
        "Ctrl+T — Traduire uniquement\n"
        "Ctrl+Alt+V — Coller dans l’original\n"
        "Ctrl+Espace — Lecture / pause\n"
        "Échap — Arrêter la lecture"
    ),
    "edge_loading": "Chargement des voix neuronales…",
    "edge_auto_voice": "Auto (correspond à la langue « Vers »)",
    "playback_title": "Lecture",
    "ocr_open_title": "Ouvrir une image pour l’OCR",
    "ocr_filter": "Images (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;Tous les fichiers (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "Échec OCR",
    "ocr_no_text": "Aucun texte reconnu.",
    "voice_input_title": "Entrée vocale",
    "voice_wait_synth": "Attendez la fin de la synthèse vocale.",
    "voice_empty": "Reconnaissance vide — réessayez.",
    "voice_input_failed_title": "Échec de l’entrée vocale",
    "translation_empty_title": "Traduction",
    "translation_failed_title": "Échec de la traduction",
    "translate_no_text_title": "Traduire",
    "translate_no_text": "Aucun texte à traduire.",
    "tts_title": "Synthèse vocale",
    "tts_no_text": "Aucun texte à lire.",
    "tts_synth_running": "La synthèse vocale est déjà en cours.",
    "tts_wait_translate": "Veuillez attendre la fin de la traduction.",
    "speech_synth_failed_title": "Échec de la synthèse vocale",
    "save_transcript_title": "Enregistrer la transcription",
    "save_transcript_nothing": "Rien à enregistrer.",
    "save_transcript_filter": "Texte (*.txt)",
    "save_transcript_saved": "Enregistré :\n{path}",
    "save_audio_title": "Enregistrer l’audio",
    "save_audio_no_buffer": "Pas encore de tampon audio — utilisez Préparer ou « Écouter → traduire → parler ».",
    "save_audio_saved": "Enregistré :\n{path}",
    "save_audio_error_title": "Enregistrer l’audio",
    "export_audio_title": "Exporter l’audio",
    "export_no_text": "Aucun texte à exporter.",
    "export_failed_title": "Échec de l’export",
    "export_saved": "Enregistré :\n{path}",
    "read_file_error_title": "Impossible de lire le fichier",
    "open_document_title": "Ouvrir un document",
    "open_document_filter": "Documents (*.txt *.doc *.docx *.pdf);;Tous les fichiers (*.*)",
    "about_dialog_title": "À propos",
    "clear_history_title": "Effacer l’historique",
    "clear_history_confirm": "Supprimer toutes les sessions enregistrées ?",
    "history_dialog_title": "Historique de session",
    "lang_list_error_fmt": "(erreur : {error})",
    "clip_header_original": "--- Original ---",
    "clip_header_translation": "--- Traduction ---",
    "transcript_empty_marker": "(vide)",
    "restart_locale_title": "Langue de l’interface",
    "restart_locale_body": (
        "La langue de l’interface s’appliquera entièrement après le redémarrage de l’application."
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
    "detect_language": "Détecter la langue",
    "translation_was_empty": "La traduction était vide.",
    "voice_load_error_fmt": "(erreur de chargement des voix : {error})",
}

MESSAGES = {**EN, **_FR}
