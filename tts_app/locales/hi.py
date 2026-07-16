"""Hindi UI strings (Devanagari)."""

from tts_app.locales.en import MESSAGES as EN

_HI: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>लेखक: <b>{author}</b><br/>
ईमेल: <a href="mailto:{email}">{email}</a><br/>
कंपनी: <b>{company}</b></p>
<p>अनुवाद सूची में Google Translate के <b>सभी भाषाएँ</b> (100+) शामिल हैं। जल्दी खोजने के लिए फ़िल्टर बॉक्स का उपयोग करें।
वॉइस रिकग्निशन Google Web Speech का उपयोग करता है (वह भाषा चुनें जिसमें आप <b>बोलते</b> हैं)। Windows की आवाज़ें कम भाषाओं को कवर करती हैं — सेटिंग्स में मेल खाती आवाज़ चुनें।</p>
<p>वॉइस रिकग्निशन (SpeechRecognition के ज़रिए Google), अनुवाद (deep-translator के ज़रिए Google),
और बोली संश्लेषण (Windows SAPI) को इंटरनेट की आवश्यकता हो सकती है।</p>
<p>दस्तावेज़ प्रारूप: .txt, .doc, .docx, .pdf। सेटिंग्स: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>शॉर्टकट: Ctrl+O खोलें, Ctrl+Shift+S ऑडियो निर्यात, Ctrl+Shift+T प्रतिलेख सहेजें, Ctrl+Return तैयार करें,
Ctrl+T केवल अनुवाद, Ctrl+Space चलाएँ/रोकें, Esc बंद करें।</p>""",
    "menu_file": "&फ़ाइल",
    "menu_open": "खोलें…",
    "menu_export_audio": "ऑडियो निर्यात करें…",
    "menu_save_transcript_txt": "प्रतिलेख सहेजें (TXT)…",
    "menu_save_wav_copy": "अंतिम ऑडियो सहेजें (WAV प्रति)…",
    "menu_open_image_ocr": "छवि खोलें (OCR)…",
    "menu_prepare_refresh": "ऑडियो तैयार / ताज़ा करें",
    "menu_translate_only": "केवल अनुवाद",
    "menu_exit": "&बाहर निकलें",
    "menu_session_history": "सत्र इतिहास",
    "menu_hist_view": "देखें और पुनर्स्थापित करें…",
    "menu_hist_add": "वर्तमान को इतिहास में जोड़ें",
    "menu_hist_clear": "सारा इतिहास साफ़ करें",
    "menu_edit": "&संपादन",
    "menu_copy_original": "मूल पाठ कॉपी करें",
    "menu_copy_translation": "अनुवाद कॉपी करें",
    "menu_paste_original": "मूल में चिपकाएँ",
    "menu_replace_from_clipboard": "क्लिपबोर्ड से मूल बदलें",
    "menu_copy_both": "मूल + अनुवाद कॉपी करें",
    "menu_help": "&सहायता",
    "menu_interface_language": "इंटरफ़ेस भाषा",
    "menu_keyboard_shortcuts": "कीबोर्ड शॉर्टकट…",
    "menu_about": "&परिचय",
    "lang_system": "Windows भाषा जैसा",
    "group_original": "मूल",
    "group_translation_panel": "अनुवाद (जब «बोलने से पहले अनुवाद» चालू हो तो TTS के लिए)",
    "placeholder_original": (
        "फ़ाइल खोलें, टाइप करें या माइक्रोफ़ोन उपयोग करें। "
        "आप बोलने या अनुवाद से पहले पाठ संपादित कर सकते हैं।"
    ),
    "placeholder_translation": "अनुवादित पाठ। संपादन योग्य। क्लाउड अनुवाद के लिए इंटरनेट चाहिए।",
    "group_languages": "भाषाएँ",
    "languages_intro": (
        "अनुवाद Google Translate की हर भाषा को समर्थित करता है। "
        "लंबी सूचियाँ छांटने के लिए नीचे खोजें; माइक्रोफ़ोन सटीकता इस बात पर निर्भर है कि आप किस भाषा में <b>बोलते</b> हैं।"
    ),
    "filter_placeholder": "नाम या कोड से फ़िल्टर (उदा. japanese, ja, hindi, hi)…",
    "btn_clear_filter": "फ़िल्टर साफ़ करें",
    "group_voice_input": "वॉइस इनपुट (माइक्रोफ़ोन)",
    "mic_intro": (
        "Google speech-to-text का उपयोग करता है (इंटरनेट + PyAudio माइक्रोफ़ोन)। "
        "सबसे अच्छी सटीकता के लिए वह भाषा चुनें जिसमें आप <b>बोलते</b> हैं।"
    ),
    "label_i_speak": "मैं बोलता/बोलती हूँ:",
    "btn_listen": "सुनें → पाठ",
    "btn_listen_pipeline": "सुनें → अनुवाद → बोलें",
    "btn_save_transcript": "प्रतिलेख सहेजें…",
    "btn_save_wav": "अंतिम WAV सहेजें…",
    "group_translation_section": "अनुवाद",
    "chk_translate_before": "बोलने से पहले अनुवाद (इंटरनेट लगता है)",
    "label_from": "से:",
    "label_to": "तक:",
    "btn_translate_now": "अब अनुवाद करें",
    "btn_swap_langs": "⇄ से / तक बदलें",
    "tooltip_swap": (
        'निश्चित भाषाएँ अदला-बदली करें। पहले «से» को किसी विशिष्ट भाषा पर सेट करें («भाषा पहचानें» नहीं)।'
    ),
    "group_audio_control": "ऑडियो नियंत्रण",
    "btn_play": "चलाएँ",
    "btn_pause": "विराम",
    "btn_stop": "रोकें",
    "btn_prepare_short": "ऑडियो तैयार / ताज़ा करें",
    "audio_hint": (
        "तैयार करें चयनित इंजन से बोली बनाता है (ऑफ़लाइन SAPI .wav या ऑनलाइन Edge neural .mp3)। "
        "पाठ स्रोत: यदि «बोलने से पहले अनुवाद» चालू है तो अनुवाद फ़ील्ड, अन्यथा मूल।"
    ),
    "group_speech_output": "बोली आउटपुट",
    "engine_sapi": "Windows SAPI (.wav, ऑफ़लाइन)",
    "engine_edge": "Microsoft Edge neural (.mp3, ऑनलाइन)",
    "label_engine": "इंजन:",
    "label_sapi_voice": "SAPI आवाज़:",
    "label_edge_voice": "Edge आवाज़:",
    "tooltip_edge_voice": "«तक» भाषा के अनुसार स्वचालित रूप से न्यूरल आवाज़ चुनने के लिए खाली छोड़ें।",
    "label_speed": "गति (शब्द/मिनट):",
    "label_volume_sapi": "आवाज़ (SAPI):",
    "hint_edge_volume": "(Edge सिस्टम वॉल्यूम उपयोग करता है; स्लाइडर केवल SAPI पर लागू होता है।)",
    "lbl_no_file": "कोई फ़ाइल लोड नहीं",
    "btn_open_file": "फ़ाइल खोलें…",
    "status_ready": "तैयार",
    "status_lang_failed": "भाषा सूची लोड नहीं हो सकी।",
    "status_langs_fmt": "{n} अनुवाद भाषाएँ · {m} माइक्रोफ़ोन/STT विकल्प · तैयार",
    "status_filter_from": "फ़िल्टर से कोई मेल नहीं — पूरी «से» सूची दिख रही है।",
    "status_filter_to": "फ़िल्टर से कोई मेल नहीं — पूरी «तक» सूची दिख रही है।",
    "status_filter_mic": "फ़िल्टर से कोई मेल नहीं — पूरी माइक्रोफ़ोन सूची दिख रही है।",
    "status_history_saved": "वर्तमान पाठ सत्र इतिहास में सहेजा गया।",
    "status_history_cleared": "सत्र इतिहास साफ़ किया गया।",
    "swap_title": "भाषाएँ बदलें",
    "swap_body": "पहले एक विशिष्ट «से» भाषा चुनें («भाषा पहचानें» नहीं), फिर «तक» के साथ अदला-बदली करें।",
    "shortcuts_title": "कीबोर्ड शॉर्टकट",
    "shortcuts_body": (
        "Ctrl+O — फ़ाइल खोलें\n"
        "Ctrl+Shift+S — ऑडियो निर्यात (SAPI के साथ WAV, Edge के साथ MP3)\n"
        "Ctrl+Shift+T — प्रतिलेख सहेजें\n"
        "Ctrl+Return — बोली तैयार / ताज़ा करें\n"
        "Ctrl+T — केवल अनुवाद\n"
        "Ctrl+Alt+V — मूल में चिपकाएँ\n"
        "Ctrl+Space — चलाएँ / विराम\n"
        "Esc — प्लेबैक रोकें"
    ),
    "edge_loading": "न्यूरल आवाज़ें लोड हो रही हैं…",
    "edge_auto_voice": "स्वचालित («तक» भाषा से मेल)",
    "playback_title": "प्लेबैक",
    "ocr_open_title": "OCR के लिए छवि खोलें",
    "ocr_filter": "छवियाँ (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;सभी फ़ाइलें (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "OCR विफल",
    "ocr_no_text": "कोई पाठ पहचाना नहीं गया।",
    "voice_input_title": "वॉइस इनपुट",
    "voice_wait_synth": "बोली संश्लेषण समाप्त होने की प्रतीक्षा करें।",
    "voice_empty": "खाली पहचान — पुनः प्रयास करें।",
    "voice_input_failed_title": "वॉइस इनपुट विफल",
    "translation_empty_title": "अनुवाद",
    "translation_failed_title": "अनुवाद विफल",
    "translate_no_text_title": "अनुवाद",
    "translate_no_text": "अनुवाद के लिए कोई पाठ नहीं।",
    "tts_title": "पाठ से बोली",
    "tts_no_text": "बोलने के लिए कोई पाठ नहीं।",
    "tts_synth_running": "बोली संश्लेषण पहले से चल रहा है।",
    "tts_wait_translate": "कृपया अनुवाद समाप्त होने की प्रतीक्षा करें।",
    "speech_synth_failed_title": "बोली संश्लेषण विफल",
    "save_transcript_title": "प्रतिलेख सहेजें",
    "save_transcript_nothing": "सहेजने के लिए कुछ नहीं।",
    "save_transcript_filter": "पाठ (*.txt)",
    "save_transcript_saved": "सहेजा गया:\n{path}",
    "save_audio_title": "ऑडियो सहेजें",
    "save_audio_no_buffer": "अभी तक कोई ऑडियो बफ़र नहीं — तैयार करें या «सुनें → अनुवाद → बोलें» उपयोग करें।",
    "save_audio_saved": "सहेजा गया:\n{path}",
    "save_audio_error_title": "ऑडियो सहेजें",
    "export_audio_title": "ऑडियो निर्यात",
    "export_no_text": "निर्यात के लिए कोई पाठ नहीं।",
    "export_failed_title": "निर्यात विफल",
    "export_saved": "सहेजा गया:\n{path}",
    "read_file_error_title": "फ़ाइल नहीं पढ़ी जा सकी",
    "open_document_title": "दस्तावेज़ खोलें",
    "open_document_filter": "दस्तावेज़ (*.txt *.doc *.docx *.pdf);;सभी फ़ाइलें (*.*)",
    "about_dialog_title": "परिचय",
    "clear_history_title": "इतिहास साफ़ करें",
    "clear_history_confirm": "सभी सहेजे गए सत्र हटाएँ?",
    "history_dialog_title": "सत्र इतिहास",
    "lang_list_error_fmt": "(त्रुटि: {error})",
    "clip_header_original": "--- मूल ---",
    "clip_header_translation": "--- अनुवाद ---",
    "transcript_empty_marker": "(खाली)",
    "restart_locale_title": "इंटरफ़ेस भाषा",
    "restart_locale_body": "इंटरफ़ेस भाषा ऐप्लिकेशन पुनः प्रारंभ के बाद पूरी तरह लागू होगी।",
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
    "detect_language": "भाषा पहचानें",
    "translation_was_empty": "अनुवाद खाली था।",
    "voice_load_error_fmt": "(आवाज़ें लोड करने में त्रुटि: {error})",
}

MESSAGES = {**EN, **_HI}
