"""Simplified Chinese UI strings."""

from tts_app.locales.en import MESSAGES as EN

_ZH: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>作者：<b>{author}</b><br/>
电子邮件：<a href="mailto:{email}">{email}</a><br/>
公司：<b>{company}</b></p>
<p>翻译列表涵盖 Google 翻译提供的<b>全部语言</b>（100+）。使用筛选框快速查找语言。
语音识别使用 Google Web Speech（请选择您<b>所说</b>的语言）。Windows 语音覆盖语言较少 — 请在设置中选择匹配的声音。</p>
<p>语音识别（通过 SpeechRecognition 的 Google）、翻译（通过 deep-translator 的 Google）、
语音合成（Windows SAPI）在相应功能上可能需要互联网连接。</p>
<p>文档格式：.txt、.doc、.docx、.pdf。设置：<code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>快捷键：Ctrl+O 打开，Ctrl+Shift+S 导出音频，Ctrl+Shift+T 保存文稿，Ctrl+Enter 准备，
Ctrl+T 仅翻译，Ctrl+Space 播放/暂停，Esc 停止。</p>""",
    "menu_file": "文件(&F)",
    "menu_open": "打开…",
    "menu_export_audio": "导出音频…",
    "menu_save_transcript_txt": "保存文稿 (TXT)…",
    "menu_save_wav_copy": "保存上次音频 (WAV 副本)…",
    "menu_open_image_ocr": "打开图像 (OCR)…",
    "menu_prepare_refresh": "准备 / 刷新音频",
    "menu_translate_only": "仅翻译",
    "menu_exit": "退出(&X)",
    "menu_session_history": "会话历史",
    "menu_hist_view": "查看并恢复…",
    "menu_hist_add": "将当前内容添加到历史",
    "menu_hist_clear": "清除全部历史",
    "menu_edit": "编辑(&E)",
    "menu_copy_original": "复制原文",
    "menu_copy_translation": "复制译文",
    "menu_paste_original": "粘贴到原文",
    "menu_replace_from_clipboard": "从剪贴板替换原文",
    "menu_copy_both": "复制原文 + 译文",
    "menu_help": "帮助(&H)",
    "menu_interface_language": "界面语言",
    "menu_keyboard_shortcuts": "键盘快捷键…",
    "menu_about": "关于(&A)",
    "lang_system": "跟随 Windows 语言",
    "group_original": "原文",
    "group_translation_panel": "译文（开启「朗读前翻译」时用于语音合成）",
    "placeholder_original": (
        "打开文件、键入或使用麦克风。"
        "您可以在朗读或翻译之前编辑文本。"
    ),
    "placeholder_translation": "译文。可编辑。云端翻译需要互联网。",
    "group_languages": "语言",
    "languages_intro": (
        "翻译支持 Google 翻译提供的所有语言。"
        "在下方搜索以缩短长列表；麦克风准确度取决于您选择的<b>所说</b>语言。"
    ),
    "filter_placeholder": "按名称或代码筛选（例如 japanese、ja、hindi、hi）…",
    "btn_clear_filter": "清除筛选",
    "group_voice_input": "语音输入（麦克风）",
    "mic_intro": (
        "使用 Google 语音转文字（互联网 + PyAudio 麦克风）。"
        "请选择您<b>所说</b>的语言以获得最佳准确度。"
    ),
    "label_i_speak": "我说：",
    "btn_listen": "收听 → 文本",
    "btn_listen_pipeline": "收听 → 翻译 → 朗读",
    "btn_save_transcript": "保存文稿…",
    "btn_save_wav": "保存上次 WAV…",
    "group_translation_section": "翻译",
    "chk_translate_before": "朗读前翻译（使用互联网）",
    "label_from": "从：",
    "label_to": "到：",
    "btn_translate_now": "立即翻译",
    "btn_swap_langs": "⇄ 交换 从 / 到",
    "tooltip_swap": "交换固定语言。请先将「从」设为具体语言（而非「检测语言」）。",
    "group_audio_control": "音频控制",
    "btn_play": "播放",
    "btn_pause": "暂停",
    "btn_stop": "停止",
    "btn_prepare_short": "准备 / 刷新音频",
    "audio_hint": (
        "准备使用所选引擎生成语音（离线 SAPI .wav 或在线 Edge 神经网络 .mp3）。"
        "文本来源：若开启「朗读前翻译」则使用译文，否则使用原文。"
    ),
    "group_speech_output": "语音输出",
    "engine_sapi": "Windows SAPI (.wav，离线)",
    "engine_edge": "Microsoft Edge 神经网络 (.mp3，在线)",
    "label_engine": "引擎：",
    "label_sapi_voice": "SAPI 声音：",
    "label_edge_voice": "Edge 声音：",
    "tooltip_edge_voice": "保留「按目标语言自动」以为当前「到」语言选择神经网络声音。",
    "label_speed": "语速（词/分钟）：",
    "label_volume_sapi": "音量 (SAPI)：",
    "hint_edge_volume": "（Edge 使用系统音量；滑块仅影响 SAPI。）",
    "lbl_no_file": "未加载文件",
    "btn_open_file": "打开文件…",
    "status_ready": "就绪",
    "status_lang_failed": "语言列表加载失败。",
    "status_langs_fmt": "{n} 种翻译语言 · {m} 种麦克风/STT 选项 · 就绪",
    "status_filter_from": "无匹配 — 显示完整「从」列表。",
    "status_filter_to": "无匹配 — 显示完整「到」列表。",
    "status_filter_mic": "无匹配 — 显示完整麦克风列表。",
    "status_history_saved": "已将当前文本保存到会话历史。",
    "status_history_cleared": "已清除会话历史。",
    "swap_title": "交换语言",
    "swap_body": "请先将「从」设为具体语言（不是「检测语言」），再与「到」交换。",
    "shortcuts_title": "键盘快捷键",
    "shortcuts_body": (
        "Ctrl+O — 打开文件\n"
        "Ctrl+Shift+S — 导出音频（SAPI 为 WAV，Edge 为 MP3）\n"
        "Ctrl+Shift+T — 保存文稿\n"
        "Ctrl+Enter — 准备 / 刷新语音\n"
        "Ctrl+T — 仅翻译\n"
        "Ctrl+Alt+V — 粘贴到原文\n"
        "Ctrl+Space — 播放 / 暂停\n"
        "Esc — 停止播放"
    ),
    "edge_loading": "正在加载神经网络声音…",
    "edge_auto_voice": "自动（匹配「到」语言）",
    "playback_title": "播放",
    "ocr_open_title": "打开图像进行 OCR",
    "ocr_filter": "图像 (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;所有文件 (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "OCR 失败",
    "ocr_no_text": "未识别到文本。",
    "voice_input_title": "语音输入",
    "voice_wait_synth": "请等待语音合成完成。",
    "voice_empty": "识别为空 — 请重试。",
    "voice_input_failed_title": "语音输入失败",
    "translation_empty_title": "翻译",
    "translation_failed_title": "翻译失败",
    "translate_no_text_title": "翻译",
    "translate_no_text": "没有可翻译的文本。",
    "tts_title": "文本转语音",
    "tts_no_text": "没有可朗读的文本。",
    "tts_synth_running": "语音合成已在运行。",
    "tts_wait_translate": "请等待翻译完成。",
    "speech_synth_failed_title": "语音合成失败",
    "save_transcript_title": "保存文稿",
    "save_transcript_nothing": "没有可保存的内容。",
    "save_transcript_filter": "文本 (*.txt)",
    "save_transcript_saved": "已保存：\n{path}",
    "save_audio_title": "保存音频",
    "save_audio_no_buffer": "尚无音频缓冲区 — 请使用「准备」或「收听 → 翻译 → 朗读」。",
    "save_audio_saved": "已保存：\n{path}",
    "save_audio_error_title": "保存音频",
    "export_audio_title": "导出音频",
    "export_no_text": "没有可导出的文本。",
    "export_failed_title": "导出失败",
    "export_saved": "已保存：\n{path}",
    "read_file_error_title": "无法读取文件",
    "open_document_title": "打开文档",
    "open_document_filter": "文档 (*.txt *.doc *.docx *.pdf);;所有文件 (*.*)",
    "about_dialog_title": "关于",
    "clear_history_title": "清除历史",
    "clear_history_confirm": "删除所有已保存的会话？",
    "history_dialog_title": "会话历史",
    "lang_list_error_fmt": "（错误：{error}）",
    "clip_header_original": "--- 原文 ---",
    "clip_header_translation": "--- 译文 ---",
    "transcript_empty_marker": "（空）",
    "restart_locale_title": "界面语言",
    "restart_locale_body": "界面语言将在重启应用程序后完全生效。",
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
    "detect_language": "检测语言",
    "translation_was_empty": "翻译结果为空。",
    "voice_load_error_fmt": "(加载语音失败: {error})",
}

MESSAGES = {**EN, **_ZH}
