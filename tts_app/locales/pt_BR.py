"""Brazilian Portuguese UI strings."""

from tts_app.locales.en import MESSAGES as EN

_PT: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>Autor: <b>{author}</b><br/>
E-mail: <a href="mailto:{email}">{email}</a><br/>
Empresa: <b>{company}</b></p>
<p>A lista de tradução inclui <b>todos os idiomas</b> do Google Translate (100+). Use a busca para achar um idioma rapidamente.
O reconhecimento de voz usa o Google Web Speech (escolha o idioma em que você <b>fala</b>). As vozes do Windows cobrem menos idiomas — escolha uma voz adequada nas configurações.</p>
<p>Reconhecimento de voz (Google via SpeechRecognition), tradução (Google via deep-translator)
e síntese de voz (Windows SAPI) podem exigir Internet quando indicado.</p>
<p>Formatos: .txt, .doc, .docx, .pdf. Configurações: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>Atalhos: Ctrl+O abrir, Ctrl+Shift+S exportar áudio, Ctrl+Shift+T salvar transcrição, Ctrl+Enter preparar,
Ctrl+T traduzir, Ctrl+Espaço reproduzir/pausar, Esc parar.</p>""",
    "menu_file": "&Arquivo",
    "menu_open": "Abrir…",
    "menu_export_audio": "Exportar áudio…",
    "menu_save_transcript_txt": "Salvar transcrição (TXT)…",
    "menu_save_wav_copy": "Salvar último áudio (cópia WAV)…",
    "menu_open_image_ocr": "Abrir imagem (OCR)…",
    "menu_prepare_refresh": "Preparar / Atualizar áudio",
    "menu_translate_only": "Apenas traduzir",
    "menu_exit": "Sai&r",
    "menu_session_history": "Histórico da sessão",
    "menu_hist_view": "Ver e restaurar…",
    "menu_hist_add": "Adicionar atual ao histórico",
    "menu_hist_clear": "Limpar todo o histórico",
    "menu_edit": "&Editar",
    "menu_copy_original": "Copiar texto original",
    "menu_copy_translation": "Copiar tradução",
    "menu_paste_original": "Colar no original",
    "menu_replace_from_clipboard": "Substituir original da área de transferência",
    "menu_copy_both": "Copiar original + tradução",
    "menu_help": "Aj&uda",
    "menu_interface_language": "Idioma da interface",
    "menu_keyboard_shortcuts": "Atalhos do teclado…",
    "menu_about": "&Sobre",
    "lang_system": "Igual ao idioma do Windows",
    "group_original": "Original",
    "group_translation_panel": "Tradução (para TTS com «Traduzir antes de falar»)",
    "placeholder_original": (
        "Abra um arquivo, digite ou use o microfone. "
        "Você pode editar o texto antes de falar ou traduzir."
    ),
    "placeholder_translation": "Texto traduzido. Editável. Tradução na nuvem requer Internet.",
    "group_languages": "Idiomas",
    "languages_intro": (
        "A tradução suporta todos os idiomas do Google Translate. "
        "Filtre abaixo para encurtar listas longas; a precisão do microfone depende de escolher "
        "o idioma em que você <b>fala</b>."
    ),
    "filter_placeholder": "Filtrar por nome ou código (ex.: japanese, ja, hindi, hi)…",
    "btn_clear_filter": "Limpar filtro",
    "group_voice_input": "Entrada de voz (microfone)",
    "mic_intro": (
        "Usa Google speech-to-text (Internet + microfone PyAudio). "
        "Escolha o idioma em que você <b>fala</b> para melhor precisão."
    ),
    "label_i_speak": "Eu falo:",
    "btn_listen": "Ouvir → texto",
    "btn_listen_pipeline": "Ouvir → traduzir → falar",
    "btn_save_transcript": "Salvar transcrição…",
    "btn_save_wav": "Salvar último WAV…",
    "group_translation_section": "Tradução",
    "chk_translate_before": "Traduzir antes de falar (usa Internet)",
    "label_from": "De:",
    "label_to": "Para:",
    "btn_translate_now": "Traduzir agora",
    "btn_swap_langs": "⇄ Trocar De / Para",
    "tooltip_swap": (
        'Troca idiomas fixos. Primeiro defina «De» como um idioma específico (não «Detectar idioma»).'
    ),
    "group_audio_control": "Controle de áudio",
    "btn_play": "Reproduzir",
    "btn_pause": "Pausa",
    "btn_stop": "Parar",
    "btn_prepare_short": "Preparar / Atualizar áudio",
    "audio_hint": (
        "Preparar gera fala com o mecanismo escolhido (SAPI .wav offline ou Edge neural .mp3 online). "
        "Fonte do texto: campo traduzido se «Traduzir antes de falar» estiver ativo, senão o original."
    ),
    "group_speech_output": "Saída de voz",
    "engine_sapi": "Windows SAPI (.wav, offline)",
    "engine_edge": "Microsoft Edge neural (.mp3, online)",
    "label_engine": "Mecanismo:",
    "label_sapi_voice": "Voz SAPI:",
    "label_edge_voice": "Voz Edge:",
    "tooltip_edge_voice": "Deixe «Automático pelo idioma Para» para escolher voz neural do idioma «Para» atual.",
    "label_speed": "Velocidade (palavras/min):",
    "label_volume_sapi": "Volume (SAPI):",
    "hint_edge_volume": "(Edge usa o volume do sistema; o controle deslizante afeta apenas SAPI.)",
    "lbl_no_file": "Nenhum arquivo carregado",
    "btn_open_file": "Abrir arquivo…",
    "status_ready": "Pronto",
    "status_lang_failed": "Falha ao carregar a lista de idiomas.",
    "status_langs_fmt": "{n} idiomas de tradução · {m} opções de microfone/STT · Pronto",
    "status_filter_from": "Sem correspondência — lista «De» completa.",
    "status_filter_to": "Sem correspondência — lista «Para» completa.",
    "status_filter_mic": "Sem correspondência — lista de microfone completa.",
    "status_history_saved": "Textos atuais salvos no histórico da sessão.",
    "status_history_cleared": "Histórico da sessão limpo.",
    "swap_title": "Trocar idiomas",
    "swap_body": "Escolha primeiro um idioma «De» específico (não «Detectar idioma»), depois troque com «Para».",
    "shortcuts_title": "Atalhos do teclado",
    "shortcuts_body": (
        "Ctrl+O — Abrir arquivo\n"
        "Ctrl+Shift+S — Exportar áudio (WAV com SAPI, MP3 com Edge)\n"
        "Ctrl+Shift+T — Salvar transcrição\n"
        "Ctrl+Enter — Preparar / atualizar fala\n"
        "Ctrl+T — Apenas traduzir\n"
        "Ctrl+Alt+V — Colar no original\n"
        "Ctrl+Espaço — Reproduzir / pausar\n"
        "Esc — Parar reprodução"
    ),
    "edge_loading": "Carregando vozes neurais…",
    "edge_auto_voice": "Automático (corresponde ao idioma «Para»)",
    "playback_title": "Reprodução",
    "ocr_open_title": "Abrir imagem para OCR",
    "ocr_filter": "Imagens (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;Todos os arquivos (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "Falha no OCR",
    "ocr_no_text": "Nenhum texto reconhecido.",
    "voice_input_title": "Entrada de voz",
    "voice_wait_synth": "Aguarde o término da síntese de voz.",
    "voice_empty": "Reconhecimento vazio — tente novamente.",
    "voice_input_failed_title": "Falha na entrada de voz",
    "translation_empty_title": "Tradução",
    "translation_failed_title": "Falha na tradução",
    "translate_no_text_title": "Traduzir",
    "translate_no_text": "Nenhum texto para traduzir.",
    "tts_title": "Texto para fala",
    "tts_no_text": "Nenhum texto para falar.",
    "tts_synth_running": "A síntese de voz já está em execução.",
    "tts_wait_translate": "Aguarde o término da tradução.",
    "speech_synth_failed_title": "Falha na síntese de voz",
    "save_transcript_title": "Salvar transcrição",
    "save_transcript_nothing": "Nada a salvar.",
    "save_transcript_filter": "Texto (*.txt)",
    "save_transcript_saved": "Salvo:\n{path}",
    "save_audio_title": "Salvar áudio",
    "save_audio_no_buffer": "Ainda sem buffer de áudio — use Preparar ou «Ouvir → traduzir → falar».",
    "save_audio_saved": "Salvo:\n{path}",
    "save_audio_error_title": "Salvar áudio",
    "export_audio_title": "Exportar áudio",
    "export_no_text": "Nenhum texto para exportar.",
    "export_failed_title": "Falha na exportação",
    "export_saved": "Salvo:\n{path}",
    "read_file_error_title": "Não foi possível ler o arquivo",
    "open_document_title": "Abrir documento",
    "open_document_filter": "Documentos (*.txt *.doc *.docx *.pdf);;Todos os arquivos (*.*)",
    "about_dialog_title": "Sobre",
    "clear_history_title": "Limpar histórico",
    "clear_history_confirm": "Remover todas as sessões salvas?",
    "history_dialog_title": "Histórico da sessão",
    "lang_list_error_fmt": "(erro: {error})",
    "clip_header_original": "--- Original ---",
    "clip_header_translation": "--- Tradução ---",
    "transcript_empty_marker": "(vazio)",
    "restart_locale_title": "Idioma da interface",
    "restart_locale_body": (
        "O idioma da interface será aplicado por completo após reiniciar o aplicativo."
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
    "translation_was_empty": "A tradução estava vazia.",
    "voice_load_error_fmt": "(erro ao carregar vozes: {error})",
}

MESSAGES = {**EN, **_PT}
