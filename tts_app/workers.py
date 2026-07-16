"""Background QThread workers for STT, translation, and TTS."""

from __future__ import annotations

from PyQt6.QtCore import QThread, pyqtSignal

from tts_app.synth_unified import synthesize_to_path


class ListenThread(QThread):
    finished_ok = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(self, google_stt_locale: str) -> None:
        super().__init__()
        self.google_stt_locale = google_stt_locale

    def run(self) -> None:
        try:
            from tts_app.speech_input import listen_once

            text = listen_once(self.google_stt_locale)
            self.finished_ok.emit(text)
        except Exception as e:  # noqa: BLE001
            self.failed.emit(str(e))


class TranslateThread(QThread):
    finished_ok = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(self, text: str, source: str, target: str) -> None:
        super().__init__()
        self.text = text
        self.source = source
        self.target = target

    def run(self) -> None:
        from tts_app.translate import translate_text

        try:
            r = translate_text(self.text, self.source, self.target)
            self.finished_ok.emit(r)
        except Exception as e:  # noqa: BLE001
            self.failed.emit(str(e))


class SynthesizeThread(QThread):
    finished_ok = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(
        self,
        text: str,
        out_path: str,
        engine: str,
        sapi_voice_id: str,
        rate: int,
        volume: float,
        edge_voice_id: str,
        target_lang_iso: str,
    ):
        super().__init__()
        self.text = text
        self.out_path = out_path
        self.engine = engine
        self.sapi_voice_id = sapi_voice_id
        self.rate = rate
        self.volume = volume
        self.edge_voice_id = edge_voice_id
        self.target_lang_iso = target_lang_iso

    def run(self) -> None:
        try:
            synthesize_to_path(
                self.text,
                self.out_path,
                engine=self.engine,
                sapi_voice_id=self.sapi_voice_id,
                rate=self.rate,
                volume=self.volume,
                edge_voice_id=self.edge_voice_id,
                target_lang_iso=self.target_lang_iso,
            )
            self.finished_ok.emit(self.out_path)
        except Exception as e:  # noqa: BLE001
            self.failed.emit(str(e))


class EdgeVoicesLoadThread(QThread):
    finished_ok = pyqtSignal(object)
    failed = pyqtSignal(str)

    def run(self) -> None:
        try:
            from tts_app.edge_tts_engine import list_edge_voices

            self.finished_ok.emit(list_edge_voices())
        except Exception as e:  # noqa: BLE001
            self.failed.emit(str(e))
