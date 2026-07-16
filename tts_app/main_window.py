from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path

from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import (
    QAction,
    QActionGroup,
    QCloseEvent,
    QDragEnterEvent,
    QDropEvent,
    QGuiApplication,
    QKeySequence,
    QShortcut,
)
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSlider,
    QSplitter,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

import tts_app.config as app_config
from tts_app.about import about_html, window_title
from tts_app.i18n import locale_ui_labels, tr
from tts_app.language_filter import filter_language_pairs
from tts_app.readers import load_text
from tts_app.speech_locales import iso_to_google_stt_locale
from tts_app.translate import language_pairs_for_ui
from tts_app.tts_engine import list_voices, prefer_voice_for_language
from tts_app.workers import (
    EdgeVoicesLoadThread,
    ListenThread,
    SynthesizeThread,
    TranslateThread,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(window_title())
        self.resize(1040, 760)
        self._settings = app_config.load()
        self._current_file: str | None = None
        self._temp_wav: str | None = None
        self._synth_thread: SynthesizeThread | None = None
        self._translate_thread: TranslateThread | None = None
        self._listen_thread: ListenThread | None = None
        self._pending_synth_path: str | None = None
        self._listen_then_pipeline = False
        self._pending_mic_release = False
        self._full_source_pairs: list[tuple[str, str]] = []
        self._full_target_pairs: list[tuple[str, str]] = []
        self._full_mic_pairs: list[tuple[str, str]] = []
        self._edge_voices_cache: list | None = None
        self._edge_voices_thread: EdgeVoicesLoadThread | None = None
        self._export_path: str | None = None

        self._player = QMediaPlayer()
        self._audio = QAudioOutput()
        self._player.setAudioOutput(self._audio)
        self._player.playbackStateChanged.connect(self._on_playback_state)
        self._player.errorOccurred.connect(self._on_player_error)

        self._build_ui()
        self._apply_translations()
        self._restore_geometry()
        self._populate_languages()
        self._populate_voices()
        self._apply_settings_to_widgets()
        self._on_playback_state()
        self.setAcceptDrops(True)
        sc_play = QShortcut(QKeySequence("Ctrl+Space"), self)
        sc_play.activated.connect(self._toggle_play_pause)

    def _build_ui(self) -> None:
        self._act_open = QAction(self)
        self._act_open.setShortcut(QKeySequence.StandardKey.Open)
        self._act_open.triggered.connect(self._open_file)

        self._act_export = QAction(self)
        self._act_export.setShortcut("Ctrl+Shift+S")
        self._act_export.triggered.connect(self._export_audio)

        self._act_save_txt = QAction(self)
        self._act_save_txt.setShortcut("Ctrl+Shift+T")
        self._act_save_txt.triggered.connect(self._save_transcript)

        self._act_save_wav = QAction(self)
        self._act_save_wav.triggered.connect(self._save_last_audio_copy)

        self._act_ocr = QAction(self)
        self._act_ocr.triggered.connect(self._open_image_ocr)

        self._act_prep = QAction(self)
        self._act_prep.setShortcut("Ctrl+Return")
        self._act_prep.triggered.connect(self._prepare_audio)

        self._act_tr_only = QAction(self)
        self._act_tr_only.setShortcut("Ctrl+T")
        self._act_tr_only.triggered.connect(self._translate_only)

        self._act_quit = QAction(self)
        self._act_quit.setShortcut(QKeySequence.StandardKey.Quit)
        self._act_quit.triggered.connect(self.close)

        self._menu_file = self.menuBar().addMenu("")
        self._menu_file.addAction(self._act_open)
        self._menu_file.addAction(self._act_export)
        self._menu_file.addAction(self._act_save_txt)
        self._menu_file.addAction(self._act_save_wav)
        self._menu_file.addAction(self._act_ocr)
        self._menu_file.addAction(self._act_prep)
        self._menu_file.addAction(self._act_tr_only)
        self._menu_file.addSeparator()
        self._hist_menu = self._menu_file.addMenu("")
        self._act_hist_view = QAction(self)
        self._act_hist_view.triggered.connect(self._open_history_dialog)
        self._act_hist_add = QAction(self)
        self._act_hist_add.triggered.connect(self._add_current_to_history)
        self._act_hist_clear = QAction(self)
        self._act_hist_clear.triggered.connect(self._clear_history)
        self._hist_menu.addAction(self._act_hist_view)
        self._hist_menu.addAction(self._act_hist_add)
        self._hist_menu.addAction(self._act_hist_clear)
        self._menu_file.addSeparator()
        self._menu_file.addAction(self._act_quit)

        self._menu_edit = self.menuBar().addMenu("")
        self._act_copy_o = QAction(self)
        self._act_copy_o.triggered.connect(self._copy_original_text)
        self._act_copy_t = QAction(self)
        self._act_copy_t.triggered.connect(self._copy_translation_text)
        self._act_paste_o = QAction(self)
        self._act_paste_o.setShortcut("Ctrl+Alt+V")
        self._act_paste_o.triggered.connect(self._paste_into_original)
        self._act_clip_in = QAction(self)
        self._act_clip_in.triggered.connect(self._import_clipboard_to_original)
        self._act_copy_both = QAction(self)
        self._act_copy_both.triggered.connect(self._copy_both_sections_to_clipboard)
        self._menu_edit.addAction(self._act_copy_o)
        self._menu_edit.addAction(self._act_copy_t)
        self._menu_edit.addSeparator()
        self._menu_edit.addAction(self._act_paste_o)
        self._menu_edit.addAction(self._act_clip_in)
        self._menu_edit.addSeparator()
        self._menu_edit.addAction(self._act_copy_both)

        self._menu_help = self.menuBar().addMenu("")
        self._act_shortcuts = QAction(self)
        self._act_shortcuts.triggered.connect(self._show_shortcuts_help)
        self._menu_help.addAction(self._act_shortcuts)
        self._menu_help.addSeparator()
        self._locale_group = QActionGroup(self)
        self._locale_group.setExclusive(True)
        self._menu_locale = self._menu_help.addMenu("")
        pref = self._settings.get("ui_locale") or "system"
        for code, label in locale_ui_labels():
            act = QAction(label, self, checkable=True)
            act.setData(code)
            if pref == code:
                act.setChecked(True)
            self._locale_group.addAction(act)
            self._menu_locale.addAction(act)
        self._locale_group.triggered.connect(self._on_locale_chosen)
        self._menu_help.addSeparator()
        self._act_about = QAction(self)
        self._act_about.triggered.connect(self._about)
        self._menu_help.addAction(self._act_about)

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        root.addWidget(splitter, 1)

        text_column = QSplitter(Qt.Orientation.Vertical)
        self._group_orig = QGroupBox()
        ob = QVBoxLayout(self._group_orig)
        self.text_edit = QTextEdit()
        self.text_edit.setFontFamily("Segoe UI")
        self.text_edit.setFontPointSize(11)
        ob.addWidget(self.text_edit)

        self._group_trans = QGroupBox()
        tb = QVBoxLayout(self._group_trans)
        self.translated_edit = QTextEdit()
        self.translated_edit.setFontFamily("Segoe UI")
        self.translated_edit.setFontPointSize(11)
        tb.addWidget(self.translated_edit)

        text_column.addWidget(self._group_orig)
        text_column.addWidget(self._group_trans)
        text_column.setStretchFactor(0, 1)
        text_column.setStretchFactor(1, 1)
        splitter.addWidget(text_column)

        side = QWidget()
        side_lay = QVBoxLayout(side)
        splitter.addWidget(side)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 1)

        self._group_lang = QGroupBox()
        lf = QVBoxLayout(self._group_lang)
        self._lbl_lang_intro = QLabel()
        self._lbl_lang_intro.setTextFormat(Qt.TextFormat.RichText)
        lf.addWidget(self._lbl_lang_intro)
        lfh = QHBoxLayout()
        self.lang_filter = QLineEdit()
        self.btn_lang_filter_clear = QPushButton()
        self.btn_lang_filter_clear.setFixedWidth(110)
        lfh.addWidget(self.lang_filter, 1)
        lfh.addWidget(self.btn_lang_filter_clear)
        lf.addLayout(lfh)
        self.lang_filter.textChanged.connect(self._on_language_filter_changed)
        self.btn_lang_filter_clear.clicked.connect(self._clear_language_filter)
        side_lay.addWidget(self._group_lang)

        self._group_mic = QGroupBox()
        mb = QVBoxLayout(self._group_mic)
        self._lbl_mic_intro = QLabel()
        self._lbl_mic_intro.setTextFormat(Qt.TextFormat.RichText)
        mb.addWidget(self._lbl_mic_intro)
        mic_form = QFormLayout()
        self.combo_mic = QComboBox()
        self._lbl_i_speak = QLabel()
        mic_form.addRow(self._lbl_i_speak, self.combo_mic)
        mb.addLayout(mic_form)
        row_mic = QHBoxLayout()
        self.btn_mic_listen = QPushButton()
        self.btn_mic_pipeline = QPushButton()
        row_mic.addWidget(self.btn_mic_listen)
        row_mic.addWidget(self.btn_mic_pipeline)
        mb.addLayout(row_mic)
        row_save = QHBoxLayout()
        self.btn_save_txt = QPushButton()
        self.btn_save_wav = QPushButton()
        row_save.addWidget(self.btn_save_txt)
        row_save.addWidget(self.btn_save_wav)
        mb.addLayout(row_save)
        self.combo_mic.currentIndexChanged.connect(self._persist_mic_lang)
        self.btn_mic_listen.clicked.connect(self._mic_listen_text_only)
        self.btn_mic_pipeline.clicked.connect(self._mic_listen_translate_speak)
        self.btn_save_txt.clicked.connect(self._save_transcript)
        self.btn_save_wav.clicked.connect(self._save_last_audio_copy)
        side_lay.addWidget(self._group_mic)

        self._group_tr = QGroupBox()
        tgl = QVBoxLayout(self._group_tr)
        self.chk_translate = QCheckBox()
        tgl.addWidget(self.chk_translate)
        form_tr = QFormLayout()
        self.combo_src = QComboBox()
        self.combo_tgt = QComboBox()
        self._lbl_from = QLabel()
        self._lbl_to = QLabel()
        form_tr.addRow(self._lbl_from, self.combo_src)
        form_tr.addRow(self._lbl_to, self.combo_tgt)
        tgl.addLayout(form_tr)
        tr_row = QHBoxLayout()
        self.btn_translate = QPushButton()
        self.btn_swap_langs = QPushButton()
        tr_row.addWidget(self.btn_translate)
        tr_row.addWidget(self.btn_swap_langs)
        tgl.addLayout(tr_row)
        self.btn_swap_langs.clicked.connect(self._swap_translate_languages)
        self.chk_translate.toggled.connect(self._persist_translate)
        self.combo_src.currentIndexChanged.connect(self._persist_translate)
        self.combo_tgt.currentIndexChanged.connect(self._persist_translate)
        self.combo_tgt.currentIndexChanged.connect(self._on_target_lang_changed_for_edge)
        self.btn_translate.clicked.connect(self._translate_only)
        side_lay.addWidget(self._group_tr)

        self._group_audio = QGroupBox()
        ab = QVBoxLayout(self._group_audio)
        row = QHBoxLayout()
        self.btn_play = QPushButton()
        self.btn_pause = QPushButton()
        self.btn_stop = QPushButton()
        self.btn_speak = QPushButton()
        row.addWidget(self.btn_play)
        row.addWidget(self.btn_pause)
        row.addWidget(self.btn_stop)
        ab.addLayout(row)
        self._lbl_audio_hint = QLabel()
        self._lbl_audio_hint.setWordWrap(True)
        self._lbl_audio_hint.setStyleSheet("color: #666;")
        ab.addWidget(self._lbl_audio_hint)
        side_lay.addWidget(self._group_audio)

        self.btn_play.clicked.connect(self._play)
        self.btn_pause.clicked.connect(self._pause)
        self.btn_stop.clicked.connect(self._stop)
        self.btn_speak.clicked.connect(self._prepare_audio)

        self._group_speech = QGroupBox()
        sf = QFormLayout(self._group_speech)
        self.combo_engine = QComboBox()
        self.combo_engine.addItem("", "sapi")
        self.combo_engine.addItem("", "edge")
        self._lbl_engine = QLabel()
        sf.addRow(self._lbl_engine, self.combo_engine)
        self.voice_combo = QComboBox()
        self.combo_edge_voice = QComboBox()
        self._lbl_sapi_voice = QLabel()
        self._lbl_edge_voice = QLabel()
        sf.addRow(self._lbl_sapi_voice, self.voice_combo)
        sf.addRow(self._lbl_edge_voice, self.combo_edge_voice)
        self.rate_slider = QSlider(Qt.Orientation.Horizontal)
        self.rate_slider.setRange(80, 400)
        self.rate_slider.setSingleStep(10)
        self.vol_slider = QSlider(Qt.Orientation.Horizontal)
        self.vol_slider.setRange(0, 100)
        self.vol_slider.setValue(100)
        self.lbl_vol_hint = QLabel()
        self.lbl_vol_hint.setWordWrap(True)
        self.lbl_vol_hint.setStyleSheet("color: #666;font-size:10px;")
        self._lbl_speed = QLabel()
        self._lbl_vol_sapi = QLabel()
        sf.addRow(self._lbl_speed, self.rate_slider)
        sf.addRow(self._lbl_vol_sapi, self.vol_slider)
        sf.addRow("", self.lbl_vol_hint)
        side_lay.addWidget(self._group_speech)

        self.combo_engine.currentIndexChanged.connect(self._on_engine_changed)
        self.combo_edge_voice.currentIndexChanged.connect(self._persist_edge_voice)
        self.voice_combo.currentIndexChanged.connect(self._persist_voice)
        self.rate_slider.valueChanged.connect(self._persist_numeric)
        self.vol_slider.valueChanged.connect(self._persist_numeric)

        bottom = QHBoxLayout()
        self.lbl_file = QLabel()
        self.lbl_file.setWordWrap(True)
        bottom.addWidget(self.lbl_file, 1)
        self.open_btn = QPushButton()
        self.open_btn.clicked.connect(self._open_file)
        bottom.addWidget(self.open_btn)
        root.addLayout(bottom)

        self.statusBar().showMessage(tr("status_ready"))

    def _on_locale_chosen(self, action: QAction) -> None:
        code = action.data()
        if code is None:
            return
        self._settings["ui_locale"] = str(code)
        self._save_settings()
        from tts_app.i18n import apply_application_locale

        apply_application_locale(QApplication.instance(), str(code))
        self._apply_translations()
        self._refresh_language_status_message()
        self.statusBar().showMessage(tr("status_ready"), 2500)

    def _apply_translations(self) -> None:
        self.setWindowTitle(window_title())
        self._menu_file.setTitle(tr("menu_file"))
        self._act_open.setText(tr("menu_open"))
        self._act_export.setText(tr("menu_export_audio"))
        self._act_save_txt.setText(tr("menu_save_transcript_txt"))
        self._act_save_wav.setText(tr("menu_save_wav_copy"))
        self._act_ocr.setText(tr("menu_open_image_ocr"))
        self._act_prep.setText(tr("menu_prepare_refresh"))
        self._act_tr_only.setText(tr("menu_translate_only"))
        self._act_quit.setText(tr("menu_exit"))
        self._hist_menu.setTitle(tr("menu_session_history"))
        self._act_hist_view.setText(tr("menu_hist_view"))
        self._act_hist_add.setText(tr("menu_hist_add"))
        self._act_hist_clear.setText(tr("menu_hist_clear"))
        self._menu_edit.setTitle(tr("menu_edit"))
        self._act_copy_o.setText(tr("menu_copy_original"))
        self._act_copy_t.setText(tr("menu_copy_translation"))
        self._act_paste_o.setText(tr("menu_paste_original"))
        self._act_clip_in.setText(tr("menu_replace_from_clipboard"))
        self._act_copy_both.setText(tr("menu_copy_both"))
        self._menu_help.setTitle(tr("menu_help"))
        self._menu_locale.setTitle(tr("menu_interface_language"))
        self._act_shortcuts.setText(tr("menu_keyboard_shortcuts"))
        self._act_about.setText(tr("menu_about"))
        for act in self._locale_group.actions():
            code = act.data()
            labels = dict(locale_ui_labels())
            if code in labels:
                act.setText(labels[code])
        sel = self._settings.get("ui_locale") or "system"
        for act in self._locale_group.actions():
            act.setChecked(act.data() == sel)
        self._group_orig.setTitle(tr("group_original"))
        self._group_trans.setTitle(tr("group_translation_panel"))
        self.text_edit.setPlaceholderText(tr("placeholder_original"))
        self.translated_edit.setPlaceholderText(tr("placeholder_translation"))
        self._group_lang.setTitle(tr("group_languages"))
        self._lbl_lang_intro.setText(tr("languages_intro"))
        self.lang_filter.setPlaceholderText(tr("filter_placeholder"))
        self.btn_lang_filter_clear.setText(tr("btn_clear_filter"))
        self._group_mic.setTitle(tr("group_voice_input"))
        self._lbl_mic_intro.setText(tr("mic_intro"))
        self._lbl_i_speak.setText(tr("label_i_speak"))
        self.btn_mic_listen.setText(tr("btn_listen"))
        self.btn_mic_pipeline.setText(tr("btn_listen_pipeline"))
        self.btn_save_txt.setText(tr("btn_save_transcript"))
        self.btn_save_wav.setText(tr("btn_save_wav"))
        self._group_tr.setTitle(tr("group_translation_section"))
        self.chk_translate.setText(tr("chk_translate_before"))
        self._lbl_from.setText(tr("label_from"))
        self._lbl_to.setText(tr("label_to"))
        self.btn_translate.setText(tr("btn_translate_now"))
        self.btn_swap_langs.setText(tr("btn_swap_langs"))
        self.btn_swap_langs.setToolTip(tr("tooltip_swap"))
        self._group_audio.setTitle(tr("group_audio_control"))
        self.btn_play.setText(tr("btn_play"))
        self.btn_pause.setText(tr("btn_pause"))
        self.btn_stop.setText(tr("btn_stop"))
        self.btn_speak.setText(tr("btn_prepare_short"))
        self._lbl_audio_hint.setText(tr("audio_hint"))
        self._group_speech.setTitle(tr("group_speech_output"))
        self.combo_engine.setItemText(0, tr("engine_sapi"))
        self.combo_engine.setItemText(1, tr("engine_edge"))
        self._lbl_engine.setText(tr("label_engine"))
        self._lbl_sapi_voice.setText(tr("label_sapi_voice"))
        self._lbl_edge_voice.setText(tr("label_edge_voice"))
        self.combo_edge_voice.setToolTip(tr("tooltip_edge_voice"))
        self._lbl_speed.setText(tr("label_speed"))
        self._lbl_vol_sapi.setText(tr("label_volume_sapi"))
        self.lbl_vol_hint.setText(tr("hint_edge_volume"))
        if self._current_file:
            self.lbl_file.setText(self._current_file)
        else:
            self.lbl_file.setText(tr("lbl_no_file"))
        self.open_btn.setText(tr("btn_open_file"))
        if self._tts_engine() == "edge" and self._edge_voices_cache is not None:
            self._populate_edge_voice_combo()
            self._restore_edge_voice_selection()

    def _save_settings(self) -> None:
        try:
            app_config.save(self._settings)
        except app_config.ConfigError as e:
            self.statusBar().showMessage(str(e), 6000)

    def _populate_languages(self) -> None:
        self.combo_src.clear()
        self.combo_tgt.clear()
        self.combo_mic.clear()
        try:
            source_full, target_full = language_pairs_for_ui(
                detect_label=tr("detect_language")
            )
        except Exception as e:  # noqa: BLE001
            self._full_source_pairs = [("Detect language", "auto")]
            self._full_target_pairs = [("Bulgarian", "bg"), ("English", "en")]
            self._full_mic_pairs = list(self._full_target_pairs)
            self.combo_src.addItem(tr("lang_list_error_fmt", error=e), "auto")
            self.combo_tgt.addItem("Bulgarian", "bg")
            self.combo_tgt.addItem("English", "en")
            self.combo_mic.addItem("Bulgarian", "bg")
            self.combo_mic.addItem("English", "en")
            self.statusBar().showMessage(tr("status_lang_failed"))
            return
        self._full_source_pairs = list(source_full)
        self._full_target_pairs = list(target_full)
        self._full_mic_pairs = list(target_full)
        self.lang_filter.blockSignals(True)
        self.lang_filter.clear()
        self.lang_filter.blockSignals(False)
        self._rebuild_filtered_language_combos()
        self._refresh_language_status_message()

    def _refresh_language_status_message(self) -> None:
        try:
            from tts_app.translate import supported_languages

            n = len(supported_languages())
            extra = tr(
                "status_langs_fmt",
                n=n,
                m=len(self._full_mic_pairs),
            )
            self.statusBar().showMessage(extra)
        except Exception:  # noqa: BLE001
            self.statusBar().showMessage(tr("status_ready"))

    def _on_language_filter_changed(self) -> None:
        self._rebuild_filtered_language_combos()

    def _clear_language_filter(self) -> None:
        self.lang_filter.blockSignals(True)
        self.lang_filter.clear()
        self.lang_filter.blockSignals(False)
        self._rebuild_filtered_language_combos()

    def _rebuild_filtered_language_combos(self) -> None:
        if not self._full_source_pairs:
            return
        q = self.lang_filter.text()
        fs = filter_language_pairs(self._full_source_pairs, q)
        ft = filter_language_pairs(self._full_target_pairs, q)
        fm = filter_language_pairs(self._full_mic_pairs, q)
        narrow = bool(q.strip())
        if not fs and narrow:
            fs = self._full_source_pairs
            self.statusBar().showMessage(tr("status_filter_from"), 4000)
        if not ft and narrow:
            ft = self._full_target_pairs
            self.statusBar().showMessage(tr("status_filter_to"), 4000)
        if not fm and narrow:
            fm = self._full_mic_pairs
            self.statusBar().showMessage(tr("status_filter_mic"), 4000)

        src_sel = self.combo_src.currentData()
        tgt_sel = self.combo_tgt.currentData()
        mic_sel = self.combo_mic.currentData()

        self.combo_src.blockSignals(True)
        self.combo_tgt.blockSignals(True)
        self.combo_mic.blockSignals(True)
        self.combo_src.clear()
        for label, code in fs:
            self.combo_src.addItem(f"{label} ({code})", code)
        self.combo_tgt.clear()
        for label, code in ft:
            self.combo_tgt.addItem(f"{label} ({code})", code)
        self.combo_mic.clear()
        for label, code in fm:
            self.combo_mic.addItem(f"{label} ({code})", code)
        self.combo_src.blockSignals(False)
        self.combo_tgt.blockSignals(False)
        self.combo_mic.blockSignals(False)

        self._restore_combo_by_code(self.combo_src, src_sel)
        self._restore_combo_by_code(self.combo_tgt, tgt_sel)
        self._restore_combo_by_code(self.combo_mic, mic_sel)

    def _restore_combo_by_code(self, combo: QComboBox, code: object | None) -> bool:
        if code is None or code == "":
            return False
        for i in range(combo.count()):
            if combo.itemData(i) == code:
                combo.setCurrentIndex(i)
                return True
        return False

    def _swap_translate_languages(self) -> None:
        src = self.combo_src.currentData()
        tgt = self.combo_tgt.currentData()
        if src == "auto":
            QMessageBox.information(
                self,
                tr("swap_title"),
                tr("swap_body"),
            )
            return
        if not tgt:
            return
        self._restore_combo_by_code(self.combo_src, tgt)
        self._restore_combo_by_code(self.combo_tgt, src)
        self._persist_translate()

    def _copy_original_text(self) -> None:
        QGuiApplication.clipboard().setText(self.text_edit.toPlainText())

    def _copy_translation_text(self) -> None:
        QGuiApplication.clipboard().setText(self.translated_edit.toPlainText())

    def _paste_into_original(self) -> None:
        t = QGuiApplication.clipboard().text()
        self.text_edit.setPlainText(t)

    def _import_clipboard_to_original(self) -> None:
        self._paste_into_original()

    def _copy_both_sections_to_clipboard(self) -> None:
        o = self.text_edit.toPlainText().strip()
        ttext = self.translated_edit.toPlainText().strip()
        blob = (
            f"{tr('clip_header_original')}\n{o}\n\n"
            f"{tr('clip_header_translation')}\n{ttext}\n"
        )
        QGuiApplication.clipboard().setText(blob)

    def _show_shortcuts_help(self) -> None:
        QMessageBox.information(
            self,
            tr("shortcuts_title"),
            tr("shortcuts_body"),
        )

    def _populate_voices(self) -> None:
        self.voice_combo.clear()
        try:
            voices = list_voices()
        except Exception as e:  # noqa: BLE001
            self.voice_combo.addItem(tr("voice_load_error_fmt", error=e), "")
            return
        # Prefer Bulgarian / English SAPI voices near the top when present
        preferred_ids = {
            prefer_voice_for_language("bg", voices),
            prefer_voice_for_language("en", voices),
        }
        preferred_ids.discard("")
        ordered = [v for v in voices if v.id in preferred_ids] + [
            v for v in voices if v.id not in preferred_ids
        ]
        for v in ordered:
            self.voice_combo.addItem(v.name, v.id)

    def _apply_settings_to_widgets(self) -> None:
        self.chk_translate.setChecked(bool(self._settings.get("translate_before_speech")))
        src = self._settings.get("translate_source") or "auto"
        tgt = self._settings.get("translate_target") or "bg"
        mic = self._settings.get("mic_language") or "bg"
        eng = self._settings.get("tts_engine") or "edge"
        for i in range(self.combo_src.count()):
            if self.combo_src.itemData(i) == src:
                self.combo_src.setCurrentIndex(i)
                break
        for i in range(self.combo_tgt.count()):
            if self.combo_tgt.itemData(i) == tgt:
                self.combo_tgt.setCurrentIndex(i)
                break
        for i in range(self.combo_mic.count()):
            if self.combo_mic.itemData(i) == mic:
                self.combo_mic.setCurrentIndex(i)
                break
        self.combo_engine.blockSignals(True)
        for i in range(self.combo_engine.count()):
            if self.combo_engine.itemData(i) == eng:
                self.combo_engine.setCurrentIndex(i)
                break
        self.combo_engine.blockSignals(False)
        vid = self._settings.get("voice_id") or ""
        for i in range(self.voice_combo.count()):
            if self.voice_combo.itemData(i) == vid:
                self.voice_combo.setCurrentIndex(i)
                break
        self.rate_slider.setValue(int(self._settings.get("rate", 200)))
        vol = float(self._settings.get("volume", 1.0))
        self.vol_slider.setValue(int(round(vol * 100)))
        self._update_engine_ui_visibility()
        if eng == "edge":
            self._load_edge_voices_if_needed()

    def _persist_translate(self) -> None:
        self._settings["translate_before_speech"] = self.chk_translate.isChecked()
        self._settings["translate_source"] = self.combo_src.currentData() or "auto"
        self._settings["translate_target"] = self.combo_tgt.currentData() or "bg"
        self._save_settings()

    def _persist_mic_lang(self) -> None:
        self._settings["mic_language"] = self.combo_mic.currentData() or "bg"
        self._save_settings()

    def _persist_voice(self) -> None:
        self._settings["voice_id"] = self.voice_combo.currentData() or ""
        self._save_settings()

    def _persist_numeric(self) -> None:
        self._settings["rate"] = self.rate_slider.value()
        self._settings["volume"] = self.vol_slider.value() / 100.0
        self._save_settings()

    def _tts_engine(self) -> str:
        return str(self.combo_engine.currentData() or "edge")

    def _on_engine_changed(self) -> None:
        self._settings["tts_engine"] = self._tts_engine()
        self._save_settings()
        self._update_engine_ui_visibility()
        if self._tts_engine() == "edge":
            self._load_edge_voices_if_needed()

    def _persist_edge_voice(self) -> None:
        ev = self.combo_edge_voice.currentData()
        if ev == "__loading__":
            return
        self._settings["edge_voice_id"] = ev or ""
        self._save_settings()

    def _update_engine_ui_visibility(self) -> None:
        is_edge = self._tts_engine() == "edge"
        self.voice_combo.setEnabled(not is_edge)
        self.vol_slider.setEnabled(not is_edge)
        self.lbl_vol_hint.setVisible(is_edge)
        self.combo_edge_voice.setEnabled(is_edge)

    def _load_edge_voices_if_needed(self) -> None:
        if self._tts_engine() != "edge":
            return
        if self._edge_voices_cache is not None:
            self._populate_edge_voice_combo()
            self._restore_edge_voice_selection()
            return
        if self._edge_voices_thread and self._edge_voices_thread.isRunning():
            return
        self.combo_edge_voice.blockSignals(True)
        self.combo_edge_voice.clear()
        self.combo_edge_voice.addItem(tr("edge_loading"), "__loading__")
        self.combo_edge_voice.blockSignals(False)
        self._edge_voices_thread = EdgeVoicesLoadThread()
        self._edge_voices_thread.finished_ok.connect(self._on_edge_voices_loaded)
        self._edge_voices_thread.failed.connect(self._on_edge_voices_failed)
        self._edge_voices_thread.start()

    def _on_edge_voices_loaded(self, voices: object) -> None:
        self._edge_voices_cache = voices
        self._populate_edge_voice_combo()
        self._restore_edge_voice_selection()

    def _on_edge_voices_failed(self, msg: str) -> None:
        QMessageBox.warning(self, tr("edge_tts_title"), msg)
        self._edge_voices_cache = []

    def _populate_edge_voice_combo(self) -> None:
        self.combo_edge_voice.blockSignals(True)
        self.combo_edge_voice.clear()
        self.combo_edge_voice.addItem(tr("edge_auto_voice"), "")
        cache = self._edge_voices_cache or []
        tgt = str(self.combo_tgt.currentData() or "bg").lower().split("-")[0][:2]
        filtered = [v for v in cache if v.locale.lower().startswith(tgt)] if cache else []
        use = filtered if filtered else cache
        for v in use:
            self.combo_edge_voice.addItem(f"{v.friendly_name} ({v.locale})", v.short_name)
        self.combo_edge_voice.blockSignals(False)

    def _restore_edge_voice_selection(self) -> None:
        ev = self._settings.get("edge_voice_id")
        if not ev:
            self.combo_edge_voice.setCurrentIndex(0)
            return
        if not self._restore_combo_by_code(self.combo_edge_voice, ev):
            self.combo_edge_voice.setCurrentIndex(0)

    def _on_target_lang_changed_for_edge(self) -> None:
        if self._tts_engine() != "edge" or not self._edge_voices_cache:
            return
        cur = self.combo_edge_voice.currentData()
        self._populate_edge_voice_combo()
        if cur and cur != "__loading__":
            self._restore_combo_by_code(self.combo_edge_voice, cur)

    def _append_history_session(self) -> None:
        from tts_app.history_store import HistoryError, append_entry

        try:
            append_entry(
                original=self.text_edit.toPlainText(),
                translated=self.translated_edit.toPlainText(),
                source_lang=str(self.combo_src.currentData() or ""),
                target_lang=str(self.combo_tgt.currentData() or ""),
            )
        except HistoryError as e:
            self.statusBar().showMessage(str(e), 6000)

    def _add_current_to_history(self) -> None:
        self._append_history_session()
        self.statusBar().showMessage(tr("status_history_saved"), 4000)

    def _clear_history(self) -> None:
        from tts_app.history_store import HistoryError, clear_all

        reply = QMessageBox.question(
            self,
            tr("clear_history_title"),
            tr("clear_history_confirm"),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        try:
            clear_all()
        except HistoryError as e:
            QMessageBox.warning(self, tr("clear_history_title"), str(e))
            return
        self.statusBar().showMessage(tr("status_history_cleared"), 4000)

    def _open_history_dialog(self) -> None:
        from tts_app.history_store import load_entries

        entries = load_entries()
        dlg = QDialog(self)
        dlg.setWindowTitle(tr("history_dialog_title"))
        dlg.resize(560, 420)
        lay = QVBoxLayout(dlg)
        lw = QListWidget()
        lw.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        for e in entries:
            t = e.get("t", "")[:19].replace("T", " ")
            o = (e.get("o") or "").replace("\n", " ")[:80]
            tr = (e.get("tr") or "").replace("\n", " ")[:80]
            item = QListWidgetItem(f"{t}  |  {o} → {tr}")
            item.setData(Qt.ItemDataRole.UserRole, e)
            lw.addItem(item)
        lay.addWidget(lw)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Close
        )
        buttons.accepted.connect(dlg.accept)
        buttons.rejected.connect(dlg.reject)
        lay.addWidget(buttons)

        def on_double_click(item: QListWidgetItem) -> None:
            data = item.data(Qt.ItemDataRole.UserRole)
            if isinstance(data, dict):
                self.text_edit.setPlainText(data.get("o") or "")
                self.translated_edit.setPlainText(data.get("tr") or "")
                src = data.get("src") or ""
                tgt = data.get("tgt") or ""
                if src:
                    self._restore_combo_by_code(self.combo_src, src)
                if tgt:
                    self._restore_combo_by_code(self.combo_tgt, tgt)
                dlg.accept()

        lw.itemDoubleClicked.connect(on_double_click)
        dlg.exec()

    def _open_image_ocr(self) -> None:
        start = self._settings.get("last_open_dir") or ""
        path, _ = QFileDialog.getOpenFileName(
            self,
            tr("ocr_open_title"),
            start,
            tr("ocr_filter"),
        )
        if not path:
            return
        self._settings["last_open_dir"] = str(Path(path).parent)
        self._save_settings()
        lang = self._settings.get("ocr_tesseract_lang") or "eng+bul"
        try:
            from tts_app.ocr_image import image_to_text

            text = image_to_text(path, lang_hint=lang)
        except RuntimeError as e:
            QMessageBox.warning(self, tr("ocr_title"), str(e))
            return
        except Exception as e:  # noqa: BLE001
            QMessageBox.critical(self, tr("ocr_failed_title"), str(e))
            return
        if not text.strip():
            QMessageBox.information(self, tr("ocr_title"), tr("ocr_no_text"))
            return
        self.text_edit.setPlainText(text)
        self.translated_edit.clear()
        self.lbl_file.setText(path)

    def _voice_id(self) -> str:
        return self.voice_combo.currentData() or ""

    def _new_temp_audio_path(self) -> str:
        suf = ".mp3" if self._tts_engine() == "edge" else ".wav"
        fd, path = tempfile.mkstemp(suffix=suf, prefix="tts_")
        os.close(fd)
        return path

    def _edge_voice_id(self) -> str:
        ev = self.combo_edge_voice.currentData()
        if ev in ("", None, "__loading__"):
            return ""
        return str(ev)

    def _mic_locale(self) -> str:
        iso = self.combo_mic.currentData() or "bg"
        return iso_to_google_stt_locale(str(iso))

    def _mic_set_busy(self, busy: bool) -> None:
        self.btn_mic_listen.setEnabled(not busy)
        self.btn_mic_pipeline.setEnabled(not busy)

    def _tts_source_text(self) -> str:
        original = self.text_edit.toPlainText().strip()
        if not self.chk_translate.isChecked():
            return original
        translated = self.translated_edit.toPlainText().strip()
        if translated:
            return translated
        return original

    def _mic_listen_text_only(self) -> None:
        self._start_listen(pipeline_after=False)

    def _mic_listen_translate_speak(self) -> None:
        self._start_listen(pipeline_after=True)

    def _start_listen(self, *, pipeline_after: bool) -> None:
        if self._listen_thread and self._listen_thread.isRunning():
            return
        if self._synth_thread and self._synth_thread.isRunning():
            QMessageBox.information(self, tr("voice_input_title"), tr("voice_wait_synth"))
            return
        self._listen_then_pipeline = pipeline_after
        self._mic_set_busy(True)
        loc = self._mic_locale()
        self._listen_thread = ListenThread(loc)
        self._listen_thread.finished_ok.connect(self._on_listen_ok)
        self._listen_thread.failed.connect(self._on_listen_failed)
        self._listen_thread.start()

    def _on_listen_ok(self, text: str) -> None:
        text = (text or "").strip()
        if not text:
            self._mic_set_busy(False)
            QMessageBox.warning(self, tr("voice_input_title"), tr("voice_empty"))
            return
        self.text_edit.setPlainText(text)
        if self._listen_then_pipeline:
            self._listen_then_pipeline = False
            self._pipeline_translate_and_speak(text)
        else:
            self._mic_set_busy(False)

    def _on_listen_failed(self, msg: str) -> None:
        self._listen_then_pipeline = False
        self._mic_set_busy(False)
        QMessageBox.critical(self, tr("voice_input_failed_title"), msg)

    def _pipeline_translate_and_speak(self, original: str) -> None:
        mic_iso = str(self.combo_mic.currentData() or "bg")
        tgt = str(self.combo_tgt.currentData() or "bg")
        if self._translate_thread and self._translate_thread.isRunning():
            self._mic_set_busy(False)
            return
        self.btn_speak.setEnabled(False)
        self._translate_thread = TranslateThread(original, mic_iso, tgt)
        self._translate_thread.finished_ok.connect(self._on_pipeline_translate_ok)
        self._translate_thread.failed.connect(self._on_pipeline_translate_fail)
        self._translate_thread.start()

    def _on_pipeline_translate_ok(self, translated: str) -> None:
        self.translated_edit.setPlainText(translated)
        body = translated.strip()
        if not body:
            self._mic_set_busy(False)
            self.btn_speak.setEnabled(True)
            QMessageBox.warning(
                self, tr("translation_empty_title"), tr("translation_was_empty")
            )
            return

        path = self._new_temp_audio_path()
        if self._temp_wav and os.path.isfile(self._temp_wav):
            try:
                os.remove(self._temp_wav)
            except OSError:
                pass
        self._temp_wav = path
        self._pending_mic_release = True
        self._append_history_session()
        self._run_synth(body, path)

    def _on_pipeline_translate_fail(self, msg: str) -> None:
        self.btn_speak.setEnabled(True)
        self._mic_set_busy(False)
        QMessageBox.critical(self, tr("translation_failed_title"), msg)

    def _translate_only(self) -> None:
        text = self.text_edit.toPlainText().strip()
        if not text:
            QMessageBox.information(
                self, tr("translate_no_text_title"), tr("translate_no_text")
            )
            return
        if self._translate_thread and self._translate_thread.isRunning():
            return
        self.btn_translate.setEnabled(False)
        src = self.combo_src.currentData() or "auto"
        tgt = self.combo_tgt.currentData() or "bg"
        self._translate_thread = TranslateThread(text, str(src), str(tgt))
        self._translate_thread.finished_ok.connect(self._on_translate_only_ok)
        self._translate_thread.failed.connect(self._on_translate_only_fail)
        self._translate_thread.finished.connect(lambda: self.btn_translate.setEnabled(True))
        self._translate_thread.start()

    def _on_translate_only_ok(self, t: str) -> None:
        self.translated_edit.setPlainText(t)
        self._append_history_session()

    def _on_translate_only_fail(self, msg: str) -> None:
        QMessageBox.critical(self, tr("translation_failed_title"), msg)

    def _prepare_audio(self) -> None:
        original = self.text_edit.toPlainText().strip()
        if not original:
            QMessageBox.information(self, tr("tts_title"), tr("tts_no_text"))
            return
        if self._synth_thread and self._synth_thread.isRunning():
            QMessageBox.information(self, tr("tts_title"), tr("tts_synth_running"))
            return
        if self._translate_thread and self._translate_thread.isRunning():
            QMessageBox.information(self, tr("tts_title"), tr("tts_wait_translate"))
            return

        path = self._new_temp_audio_path()
        if self._temp_wav and os.path.isfile(self._temp_wav):
            try:
                os.remove(self._temp_wav)
            except OSError:
                pass
        self._temp_wav = path

        if self.chk_translate.isChecked():
            self.btn_speak.setEnabled(False)
            self._pending_synth_path = path
            src = self.combo_src.currentData() or "auto"
            tgt = self.combo_tgt.currentData() or "bg"
            self._translate_thread = TranslateThread(original, str(src), str(tgt))
            self._translate_thread.finished_ok.connect(self._on_translate_then_synth_ok)
            self._translate_thread.failed.connect(self._on_translate_then_synth_fail)
            self._translate_thread.start()
        else:
            self._run_synth(original, path)

    def _on_translate_then_synth_ok(self, translated: str) -> None:
        self.translated_edit.setPlainText(translated)
        self._append_history_session()
        path = self._pending_synth_path
        self._pending_synth_path = None
        if path:
            self._run_synth(translated.strip() or self.text_edit.toPlainText().strip(), path)

    def _on_translate_then_synth_fail(self, msg: str) -> None:
        self._pending_synth_path = None
        self.btn_speak.setEnabled(True)
        QMessageBox.critical(self, tr("translation_failed_title"), msg)

    def _run_synth(self, text: str, path: str, *, play_when_done: bool = True) -> None:
        self.btn_speak.setEnabled(False)
        self._act_export.setEnabled(False)
        self._synth_thread = SynthesizeThread(
            text,
            path,
            self._tts_engine(),
            self._voice_id(),
            self.rate_slider.value(),
            self.vol_slider.value() / 100.0,
            self._edge_voice_id(),
            str(self.combo_tgt.currentData() or "bg"),
        )
        if play_when_done:
            self._synth_thread.finished_ok.connect(self._on_synth_ok)
            self._synth_thread.failed.connect(self._on_synth_fail)
        else:
            self._synth_thread.finished_ok.connect(self._on_export_ok)
            self._synth_thread.failed.connect(self._on_export_fail)

        def _unlock() -> None:
            self.btn_speak.setEnabled(True)
            self._act_export.setEnabled(True)
            if self._pending_mic_release:
                self._pending_mic_release = False
                self._mic_set_busy(False)

        self._synth_thread.finished.connect(_unlock)
        self._synth_thread.start()

    def _on_synth_ok(self, path: str) -> None:
        self._player.setSource(QUrl.fromLocalFile(path))
        self._audio.setVolume(self.vol_slider.value() / 100.0)
        self._player.play()
        self._on_playback_state()

    def _on_synth_fail(self, msg: str) -> None:
        if self._pending_mic_release:
            self._pending_mic_release = False
            self._mic_set_busy(False)
        QMessageBox.critical(self, tr("speech_synth_failed_title"), msg)

    def _on_export_ok(self, path: str) -> None:
        self._export_path = None
        QMessageBox.information(self, tr("tts_title"), tr("export_saved", path=path))

    def _on_export_fail(self, msg: str) -> None:
        self._export_path = None
        QMessageBox.critical(self, tr("export_failed_title"), msg)

    def _save_transcript(self) -> None:
        orig = self.text_edit.toPlainText().strip()
        tra = self.translated_edit.toPlainText().strip()
        if not orig and not tra:
            QMessageBox.information(
                self, tr("save_transcript_title"), tr("save_transcript_nothing")
            )
            return
        start = self._settings.get("last_export_dir") or self._settings.get("last_open_dir") or ""
        path, _ = QFileDialog.getSaveFileName(
            self,
            tr("save_transcript_title"),
            str(Path(start) / "transcript.txt"),
            tr("save_transcript_filter"),
        )
        if not path:
            return
        self._settings["last_export_dir"] = str(Path(path).parent)
        self._save_settings()
        lines = [
            tr("clip_header_original"),
            orig or tr("transcript_empty_marker"),
            "",
            tr("clip_header_translation"),
            tra or tr("transcript_empty_marker"),
            "",
        ]
        Path(path).write_text("\n".join(lines), encoding="utf-8")
        QMessageBox.information(
            self, tr("save_transcript_title"), tr("save_transcript_saved", path=path)
        )

    def _save_last_audio_copy(self) -> None:
        src = self._temp_wav
        if not src or not os.path.isfile(src):
            QMessageBox.information(
                self, tr("save_audio_title"), tr("save_audio_no_buffer")
            )
            return
        start = self._settings.get("last_export_dir") or ""
        ext = Path(src).suffix.lower() or ".wav"
        default = "voice_output.mp3" if ext == ".mp3" else "voice_output.wav"
        filt = "MP3 (*.mp3)" if ext == ".mp3" else "WAV (*.wav)"
        path, _ = QFileDialog.getSaveFileName(
            self,
            tr("save_audio_title"),
            str(Path(start) / default),
            filt,
        )
        if not path:
            return
        self._settings["last_export_dir"] = str(Path(path).parent)
        self._save_settings()
        try:
            shutil.copy2(src, path)
        except OSError as e:
            QMessageBox.critical(self, tr("save_audio_error_title"), str(e))
            return
        QMessageBox.information(
            self, tr("save_audio_title"), tr("save_audio_saved", path=path)
        )

    def _play(self) -> None:
        if self._player.source().isEmpty() and self._temp_wav:
            self._player.setSource(QUrl.fromLocalFile(self._temp_wav))
        self._audio.setVolume(self.vol_slider.value() / 100.0)
        self._player.play()

    def _pause(self) -> None:
        self._player.pause()

    def _stop(self) -> None:
        self._player.stop()

    def _toggle_play_pause(self) -> None:
        if self._player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self._pause()
        else:
            self._play()

    def _on_playback_state(self, *_args) -> None:
        state = self._player.playbackState()
        playing = state == QMediaPlayer.PlaybackState.PlayingState
        paused = state == QMediaPlayer.PlaybackState.PausedState
        has_source = not self._player.source().isEmpty() or bool(
            self._temp_wav and os.path.isfile(self._temp_wav)
        )
        self.btn_play.setEnabled(has_source and not playing)
        self.btn_pause.setEnabled(playing)
        self.btn_stop.setEnabled(playing or paused)

    def _on_player_error(self, *_args) -> None:
        QMessageBox.warning(self, tr("playback_title"), self._player.errorString())

    def _open_file(self) -> None:
        start = self._settings.get("last_open_dir") or ""
        path, _ = QFileDialog.getOpenFileName(
            self,
            tr("open_document_title"),
            start,
            tr("open_document_filter"),
        )
        if not path:
            return
        self._settings["last_open_dir"] = str(Path(path).parent)
        self._save_settings()
        self._load_path(path)

    def _load_path(self, path: str) -> None:
        try:
            text = load_text(path)
        except Exception as e:  # noqa: BLE001
            QMessageBox.critical(self, tr("read_file_error_title"), str(e))
            return
        self._current_file = path
        self.text_edit.setPlainText(text)
        self.translated_edit.clear()
        self.lbl_file.setText(path)

    def _export_audio(self) -> None:
        text = self._tts_source_text().strip()
        if not text:
            QMessageBox.information(self, tr("export_audio_title"), tr("export_no_text"))
            return
        if self._synth_thread and self._synth_thread.isRunning():
            QMessageBox.information(self, tr("tts_title"), tr("tts_synth_running"))
            return
        start = self._settings.get("last_export_dir") or self._settings.get("last_open_dir") or ""
        use_edge = self._tts_engine() == "edge"
        default_name = "speech.mp3" if use_edge else "speech.wav"
        filt = "MP3 (*.mp3)" if use_edge else "WAV (*.wav)"
        path, _ = QFileDialog.getSaveFileName(
            self,
            tr("export_audio_title"),
            str(Path(start) / default_name),
            filt,
        )
        if not path:
            return
        self._settings["last_export_dir"] = str(Path(path).parent)
        self._save_settings()
        self._export_path = path
        self._run_synth(text, path, play_when_done=False)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Escape:
            self._stop()
            event.accept()
            return
        super().keyPressEvent(event)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event: QDropEvent) -> None:
        urls = event.mimeData().urls()
        if urls:
            local = urls[0].toLocalFile()
            if local:
                self._load_path(local)
        event.acceptProposedAction()

    def _about(self) -> None:
        box = QMessageBox(self)
        box.setWindowTitle(tr("about_dialog_title"))
        box.setTextFormat(Qt.TextFormat.RichText)
        box.setText(about_html())
        box.exec()

    def _restore_geometry(self) -> None:
        g = self._settings.get("window_geometry")
        if isinstance(g, list) and len(g) == 4:
            self.setGeometry(*g)

    def closeEvent(self, event: QCloseEvent) -> None:
        geo = self.geometry()
        self._settings["window_geometry"] = [geo.x(), geo.y(), geo.width(), geo.height()]
        self._save_settings()
        if self._temp_wav and os.path.isfile(self._temp_wav):
            try:
                os.remove(self._temp_wav)
            except OSError:
                pass
        event.accept()
