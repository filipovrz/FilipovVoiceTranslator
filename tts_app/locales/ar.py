"""Arabic UI strings (RTL layout handled in main)."""

from tts_app.locales.en import MESSAGES as EN

_AR: dict[str, str] = {
    "about_html": """<p><b>{app}</b> v{version}</p>
<p>المؤلف: <b>{author}</b><br/>
البريد: <a href="mailto:{email}">{email}</a><br/>
الشركة: <b>{company}</b></p>
<p>تتضمن قائمة الترجمة <b>جميع اللغات</b> التي يقدمها Google Translate (أكثر من 100). استخدم مربع التصفية للعثور على لغة بسرعة.
 يستخدم التعرف على الصوت Google Web Speech (اختر اللغة التي <b>تتحدث</b> بها). تغطي أصوات Windows لغات أقل — اختر صوتًا مناسبًا في الإعدادات.</p>
<p>قد يتطلب التعرف على الصوت (Google عبر SpeechRecognition) والترجمة (Google عبر deep-translator)
ومزج الصوت (Windows SAPI) اتصالاً بالإنترنت حسب الوظيفة.</p>
<p>صيغ المستندات: .txt، .doc، .docx، .pdf. الإعدادات: <code>%LOCALAPPDATA%\\TextToSpeechApp\\settings.json</code></p>
<p>اختصارات: Ctrl+O لفتح، Ctrl+Shift+S تصدير الصوت، Ctrl+Shift+T حفظ النص، Ctrl+Enter إعداد،
Ctrl+T ترجمة فقط، Ctrl+Space تشغيل/إيقاف مؤقت، Esc إيقاف.</p>""",
    "menu_file": "&ملف",
    "menu_open": "فتح…",
    "menu_export_audio": "تصدير الصوت…",
    "menu_save_transcript_txt": "حفظ النص (TXT)…",
    "menu_save_wav_copy": "حفظ آخر صوت (نسخة WAV)…",
    "menu_open_image_ocr": "فتح صورة (OCR)…",
    "menu_prepare_refresh": "إعداد / تحديث الصوت",
    "menu_translate_only": "ترجمة فقط",
    "menu_exit": "&خروج",
    "menu_session_history": "سجل الجلسة",
    "menu_hist_view": "عرض واستعادة…",
    "menu_hist_add": "إضافة الحالي إلى السجل",
    "menu_hist_clear": "مسح كل السجل",
    "menu_edit": "&تحرير",
    "menu_copy_original": "نسخ النص الأصلي",
    "menu_copy_translation": "نسخ الترجمة",
    "menu_paste_original": "لصق في الأصل",
    "menu_replace_from_clipboard": "استبدال الأصل من الحافظة",
    "menu_copy_both": "نسخ الأصل + الترجمة",
    "menu_help": "&مساعدة",
    "menu_interface_language": "لغة الواجهة",
    "menu_keyboard_shortcuts": "اختصارات لوحة المفاتيح…",
    "menu_about": "&حول",
    "lang_system": "مطابقة لغة Windows",
    "group_original": "الأصل",
    "group_translation_panel": "الترجمة (للتحويل إلى كلام عند تفعيل «ترجمة قبل الكلام»)",
    "placeholder_original": (
        "افتح ملفًا أو اكتب أو استخدم الميكروفون. "
        "يمكنك تحرير النص قبل التحدث أو الترجمة."
    ),
    "placeholder_translation": "النص المترجم. قابل للتحرير. تتطلب الترجمة السحابية إنترنتًا.",
    "group_languages": "اللغات",
    "languages_intro": (
        "الترجمة تدعم كل لغات Google Translate. "
        "ابحث أدناه لتقليل القوائم الطويلة؛ دقة الميكروفون تعتمد على اختيار "
        "اللغة التي <b>تتحدث</b> بها."
    ),
    "filter_placeholder": "تصفية بالاسم أو الرمز (مثل japanese، ja، hindi، hi)…",
    "btn_clear_filter": "مسح التصفية",
    "group_voice_input": "إدخال صوتي (ميكروفون)",
    "mic_intro": (
        "يستخدم Google لتحويل الكلام إلى نص (إنترنت + ميكروفون PyAudio). "
        "اختر اللغة التي <b>تتحدث</b> بها لأفضل دقة."
    ),
    "label_i_speak": "أنا أتحدث:",
    "btn_listen": "استمع ← نص",
    "btn_listen_pipeline": "استمع ← ترجم ← تحدث",
    "btn_save_transcript": "حفظ النص…",
    "btn_save_wav": "حفظ آخر WAV…",
    "group_translation_section": "الترجمة",
    "chk_translate_before": "ترجمة قبل الكلام (يستخدم الإنترنت)",
    "label_from": "من:",
    "label_to": "إلى:",
    "btn_translate_now": "ترجم الآن",
    "btn_swap_langs": "⇄ تبديل من / إلى",
    "tooltip_swap": (
        'تبديل اللغات الثابتة. اضبط «من» على لغة محددة أولاً (ليس «اكتشاف اللغة»).'
    ),
    "group_audio_control": "التحكم بالصوت",
    "btn_play": "تشغيل",
    "btn_pause": "إيقاف مؤقت",
    "btn_stop": "إيقاف",
    "btn_prepare_short": "إعداد / تحديث الصوت",
    "audio_hint": (
        "الإعداد ينشئ الكلام باستخدام المحرك المحدد (SAPI .wav دون اتصال أو Edge neural .mp3 مع اتصال). "
        "مصدر النص: حقل الترجمة إذا كان «ترجمة قبل الكلام» مفعلًا، وإلا الأصل."
    ),
    "group_speech_output": "مخرجات الكلام",
    "engine_sapi": "Windows SAPI (.wav، دون اتصال)",
    "engine_edge": "Microsoft Edge neural (.mp3، مع اتصال)",
    "label_engine": "المحرك:",
    "label_sapi_voice": "صوت SAPI:",
    "label_edge_voice": "صوت Edge:",
    "tooltip_edge_voice": "اتركه «تلقائيًا حسب لغة إلى» لاختيار صوت عصبي للغة «إلى» الحالية.",
    "label_speed": "السرعة (كلمات/دقيقة):",
    "label_volume_sapi": "الصوت (SAPI):",
    "hint_edge_volume": "(Edge يستخدم صوت النظام؛ المنزلق يؤثر على SAPI فقط.)",
    "lbl_no_file": "لا يوجد ملف محمّل",
    "btn_open_file": "فتح ملف…",
    "status_ready": "جاهز",
    "status_lang_failed": "فشل تحميل قائمة اللغات.",
    "status_langs_fmt": "{n} لغات ترجمة · {m} خيارات ميكروفون/STT · جاهز",
    "status_filter_from": "لا توجد مطابقة — عرض قائمة «من» كاملة.",
    "status_filter_to": "لا توجد مطابقة — عرض قائمة «إلى» كاملة.",
    "status_filter_mic": "لا توجد مطابقة — عرض قائمة الميكروفون كاملة.",
    "status_history_saved": "تم حفظ النصوص الحالية في سجل الجلسة.",
    "status_history_cleared": "تم مسح سجل الجلسة.",
    "swap_title": "تبديل اللغات",
    "swap_body": "اختر أولاً لغة «من» محددة (ليس «اكتشاف اللغة»)، ثم بدّل مع «إلى».",
    "shortcuts_title": "اختصارات لوحة المفاتيح",
    "shortcuts_body": (
        "Ctrl+O — فتح ملف\n"
        "Ctrl+Shift+S — تصدير الصوت (WAV مع SAPI، MP3 مع Edge)\n"
        "Ctrl+Shift+T — حفظ النص\n"
        "Ctrl+Return — إعداد / تحديث الكلام\n"
        "Ctrl+T — ترجمة فقط\n"
        "Ctrl+Alt+V — لصق في الأصل\n"
        "Ctrl+Space — تشغيل / إيقاف مؤقت\n"
        "Esc — إيقاف التشغيل"
    ),
    "edge_loading": "جارٍ تحميل الأصوات العصبية…",
    "edge_auto_voice": "تلقائي (يطابق لغة «إلى»)",
    "playback_title": "التشغيل",
    "ocr_open_title": "فتح صورة للـ OCR",
    "ocr_filter": "صور (*.png *.jpg *.jpeg *.tif *.tiff *.bmp);;كل الملفات (*.*)",
    "ocr_title": "OCR",
    "ocr_failed_title": "فشل OCR",
    "ocr_no_text": "لم يُتعرّف على نص.",
    "voice_input_title": "إدخال صوتي",
    "voice_wait_synth": "انتظر انتهاء مزج الصوت.",
    "voice_empty": "تعرّف فارغ — أعد المحاولة.",
    "voice_input_failed_title": "فشل الإدخال الصوتي",
    "translation_empty_title": "الترجمة",
    "translation_failed_title": "فشل الترجمة",
    "translate_no_text_title": "ترجمة",
    "translate_no_text": "لا يوجد نص للترجمة.",
    "tts_title": "نص إلى كلام",
    "tts_no_text": "لا يوجد نص للتحدث.",
    "tts_synth_running": "مزج الصوت يعمل بالفعل.",
    "tts_wait_translate": "يرجى انتظار انتهاء الترجمة.",
    "speech_synth_failed_title": "فشل مزج الصوت",
    "save_transcript_title": "حفظ النص",
    "save_transcript_nothing": "لا يوجد شيء للحفظ.",
    "save_transcript_filter": "نص (*.txt)",
    "save_transcript_saved": "تم الحفظ:\n{path}",
    "save_audio_title": "حفظ الصوت",
    "save_audio_no_buffer": "لا يوجد مخزن صوت بعد — استخدم إعداد أو «استمع ← ترجم ← تحدث».",
    "save_audio_saved": "تم الحفظ:\n{path}",
    "save_audio_error_title": "حفظ الصوت",
    "export_audio_title": "تصدير الصوت",
    "export_no_text": "لا يوجد نص للتصدير.",
    "export_failed_title": "فشل التصدير",
    "export_saved": "تم الحفظ:\n{path}",
    "read_file_error_title": "تعذّر قراءة الملف",
    "open_document_title": "فتح مستند",
    "open_document_filter": "مستندات (*.txt *.doc *.docx *.pdf);;كل الملفات (*.*)",
    "about_dialog_title": "حول",
    "clear_history_title": "مسح السجل",
    "clear_history_confirm": "إزالة كل الجلسات المحفوظة؟",
    "history_dialog_title": "سجل الجلسة",
    "lang_list_error_fmt": "(خطأ: {error})",
    "clip_header_original": "--- الأصل ---",
    "clip_header_translation": "--- الترجمة ---",
    "transcript_empty_marker": "(فارغ)",
    "restart_locale_title": "لغة الواجهة",
    "restart_locale_body": "ستُطبَّق لغة الواجهة بالكامل بعد إعادة تشغيل التطبيق.",
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
    "detect_language": "اكتشاف اللغة",
    "translation_was_empty": "كانت الترجمة فارغة.",
    "voice_load_error_fmt": "(خطأ في تحميل الأصوات: {error})",
}

MESSAGES = {**EN, **_AR}
