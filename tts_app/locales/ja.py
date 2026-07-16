"""Japanese UI strings."""

from tts_app.locales.en import MESSAGES as EN

_JA: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>作者: <b>{author}</b><br/>
メール: <a href="mailto:{email}">{email}</a><br/>
会社: <b>{company}</b></p>
<p>翻訳リストは Google 翻訳の<b>すべての言語</b>（100以上）を含みます。フィルターで素早く探せます。
音声認識は Google Web Speech を使用します（話す言語を選択してください）。Windows の音声は対応言語が少ないです — 設定で適した音声を選んでください。</p>
<p>音声認識（SpeechRecognition 経由の Google）、翻訳（deep-translator 経由の Google）、
音声合成（Windows SAPI）は機能によりインターネット接続が必要な場合があります。</p>
<p>文書形式: .txt, .doc, .docx, .pdf。設定: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>ショートカット: Ctrl+O 開く、Ctrl+Shift+S 音声書き出し、Ctrl+Shift+T 書き起こし保存、Ctrl+Enter 準備、
Ctrl+T 翻訳のみ、Ctrl+Space 再生/一時停止、Esc 停止。</p>""",
    "menu_file": "ファイル(&F)",
    "menu_open": "開く…",
    "menu_export_audio": "音声を書き出す…",
    "menu_save_transcript_txt": "書き起こしを保存 (TXT)…",
    "menu_save_wav_copy": "直近の音声を保存 (WAV コピー)…",
    "menu_open_image_ocr": "画像を開く (OCR)…",
    "menu_prepare_refresh": "音声を準備 / 更新",
    "menu_translate_only": "翻訳のみ",
    "menu_exit": "終了(&X)",
    "menu_session_history": "セッション履歴",
    "menu_hist_view": "表示と復元…",
    "menu_hist_add": "現在を履歴に追加",
    "menu_hist_clear": "履歴をすべて削除",
    "menu_edit": "編集(&E)",
    "menu_copy_original": "原文をコピー",
    "menu_copy_translation": "訳文をコピー",
    "menu_paste_original": "原文に貼り付け",
    "menu_replace_from_clipboard": "クリップボードで原文を置換",
    "menu_copy_both": "原文と訳文をコピー",
    "menu_help": "ヘルプ(&H)",
    "menu_interface_language": "表示言語",
    "menu_keyboard_shortcuts": "キーボードショートカット…",
    "menu_about": "バージョン情報(&A)",
    "lang_system": "Windows の言語に合わせる",
    "group_original": "原文",
    "group_translation_panel": "翻訳（「読み上げ前に翻訳」がオンなら TTS に使用）",
    "placeholder_original": (
        "ファイルを開く、入力する、またはマイクを使います。"
        "読み上げや翻訳の前にテキストを編集できます。"
    ),
    "placeholder_translation": "翻訳テキスト。編集可能。クラウド翻訳にはインターネットが必要です。",
    "group_languages": "言語",
    "languages_intro": (
        "Google 翻訳が提供するすべての言語に対応しています。"
        "長いリストは下の検索で絞り込みます。マイクの精度は、話す言語を選ぶことに依存します。"
    ),
    "filter_placeholder": "名前またはコードでフィルター (例: japanese, ja, hindi, hi)…",
    "btn_clear_filter": "フィルターを解除",
    "group_voice_input": "音声入力（マイク）",
    "mic_intro": (
        "Google の音声テキスト変換を使用します（インターネット + PyAudio マイク）。"
        "精度のため、話す言語を選んでください。"
    ),
    "label_i_speak": "話す言語:",
    "btn_listen": "聞く → テキスト",
    "btn_listen_pipeline": "聞く → 翻訳 → 読み上げ",
    "btn_save_transcript": "書き起こしを保存…",
    "btn_save_wav": "直近の WAV を保存…",
    "group_translation_section": "翻訳",
    "chk_translate_before": "読み上げ前に翻訳（インターネット使用）",
    "label_from": "元:",
    "label_to": "先:",
    "btn_translate_now": "今すぐ翻訳",
    "btn_swap_langs": "⇄ 元 / 先を入れ替え",
    "tooltip_swap": "固定言語を入れ替えます。先に「元」を具体的な言語にしてください（「言語を検出」以外）。",
    "group_audio_control": "音声コントロール",
    "btn_play": "再生",
    "btn_pause": "一時停止",
    "btn_stop": "停止",
    "btn_prepare_short": "音声を準備 / 更新",
    "audio_hint": (
        "準備では選択したエンジンで音声を生成します（オフラインの SAPI .wav、またはオンラインの Edge neural .mp3）。"
        "「読み上げ前に翻訳」がオンのときは訳文、オフのときは原文が使われます。"
    ),
    "group_speech_output": "音声出力",
    "engine_sapi": "Windows SAPI (.wav, オフライン)",
    "engine_edge": "Microsoft Edge neural (.mp3, オンライン)",
    "label_engine": "エンジン:",
    "label_sapi_voice": "SAPI 音声:",
    "label_edge_voice": "Edge 音声:",
    "tooltip_edge_voice": "「先の言語に合わせる自動」で、現在の「先」言語用のニューラル音声を選びます。",
    "label_speed": "速度 (語/分):",
    "label_volume_sapi": "音量 (SAPI):",
    "hint_edge_volume": "（Edge はシステム音量を使用。スライダーは SAPI のみに効きます。）",
    "lbl_no_file": "ファイルが読み込まれていません",
    "btn_open_file": "ファイルを開く…",
    "status_ready": "準備完了",
    "status_lang_failed": "言語リストを読み込めませんでした。",
    "status_langs_fmt": "翻訳言語 {n} · マイク/STT {m} · 準備完了",
    "status_filter_from": "一致なし — 「元」の一覧をすべて表示。",
    "status_filter_to": "一致なし — 「先」の一覧をすべて表示。",
    "status_filter_mic": "一致なし — マイク一覧をすべて表示。",
    "status_history_saved": "現在のテキストをセッション履歴に保存しました。",
    "status_history_cleared": "セッション履歴を消去しました。",
    "swap_title": "言語を入れ替え",
    "swap_body": "先に具体的な「元」言語を選んでから（「言語を検出」以外）、「先」と入れ替えてください。",
    "shortcuts_title": "キーボードショートカット",
    "shortcuts_body": (
        "Ctrl+O — ファイルを開く\n"
        "Ctrl+Shift+S — 音声を書き出す（SAPI は WAV、Edge は MP3）\n"
        "Ctrl+Shift+T — 書き起こしを保存\n"
        "Ctrl+Enter — 音声を準備 / 更新\n"
        "Ctrl+T — 翻訳のみ\n"
        "Ctrl+Alt+V — 原文に貼り付け\n"
        "Ctrl+Space — 再生 / 一時停止\n"
        "Esc — 再生を停止"
    ),
    "edge_loading": "ニューラル音声を読み込み中…",
    "edge_auto_voice": "自動（「先」の言語に合わせる）",
    "playback_title": "再生",
    "ocr_open_title": "OCR 用に画像を開く",
    "ocr_filter": "画像 (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;すべてのファイル (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "OCR 失敗",
    "ocr_no_text": "テキストが認識されませんでした。",
    "voice_input_title": "音声入力",
    "voice_wait_synth": "音声合成が終わるまでお待ちください。",
    "voice_empty": "認識結果が空です — もう一度お試しください。",
    "voice_input_failed_title": "音声入力に失敗しました",
    "translation_empty_title": "翻訳",
    "translation_failed_title": "翻訳に失敗しました",
    "translate_no_text_title": "翻訳",
    "translate_no_text": "翻訳するテキストがありません。",
    "tts_title": "テキスト読み上げ",
    "tts_no_text": "読み上げるテキストがありません。",
    "tts_synth_running": "音声合成が既に実行中です。",
    "tts_wait_translate": "翻訳が終わるまでお待ちください。",
    "speech_synth_failed_title": "音声合成に失敗しました",
    "save_transcript_title": "書き起こしを保存",
    "save_transcript_nothing": "保存する内容がありません。",
    "save_transcript_filter": "テキスト (*.txt)",
    "save_transcript_saved": "保存しました:\n{path}",
    "save_audio_title": "音声を保存",
    "save_audio_no_buffer": "まだ音声バッファがありません — 「準備」または「聞く → 翻訳 → 読み上げ」を使ってください。",
    "save_audio_saved": "保存しました:\n{path}",
    "save_audio_error_title": "音声を保存",
    "export_audio_title": "音声を書き出す",
    "export_no_text": "書き出すテキストがありません。",
    "export_failed_title": "書き出しに失敗しました",
    "export_saved": "保存しました:\n{path}",
    "read_file_error_title": "ファイルを読み取れませんでした",
    "open_document_title": "文書を開く",
    "open_document_filter": "文書 (*.txt *.doc *.docx *.pdf);;すべてのファイル (*.*)",
    "about_dialog_title": "バージョン情報",
    "clear_history_title": "履歴を削除",
    "clear_history_confirm": "保存したセッションをすべて削除しますか？",
    "history_dialog_title": "セッション履歴",
    "lang_list_error_fmt": "(エラー: {error})",
    "clip_header_original": "--- 原文 ---",
    "clip_header_translation": "--- 翻訳 ---",
    "transcript_empty_marker": "(空)",
    "restart_locale_title": "表示言語",
    "restart_locale_body": "表示言語はアプリケーションを再起動すると完全に反映されます。",
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
    "detect_language": "言語を検出",
    "translation_was_empty": "翻訳が空でした。",
    "voice_load_error_fmt": "(音声の読み込みエラー: {error})",
}

MESSAGES = {**EN, **_JA}
