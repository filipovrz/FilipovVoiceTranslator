# -*- mode: python ; coding: utf-8 -*-
import os

from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all("PyQt6")
hiddenimports = (
    list(hiddenimports)
    + [
        "PyQt6.QtMultimedia",
        "deep_translator",
        "deep_translator.google",
        "speech_recognition",
        "pyaudio",
        "edge_tts",
        "PIL",
        "pytesseract",
        "tts_app.workers",
        "tts_app.language_catalog",
        "tts_app.version",
    ]
)

spec_root = os.path.dirname(os.path.abspath(SPEC))
extra_datas = [
    (os.path.join(spec_root, "VERSION"), "."),
    (
        os.path.join(spec_root, "tts_app", "data", "google_languages.json"),
        os.path.join("tts_app", "data"),
    ),
]
datas = list(datas) + extra_datas

a = Analysis(
    ["main.py"],
    pathex=[spec_root],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="TextToSpeech",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name="TextToSpeech",
)
