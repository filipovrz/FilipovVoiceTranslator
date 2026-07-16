# Filipov Voice Translator

Desktop app for Windows: open/edit documents, translate (Google), speak (Windows SAPI or Microsoft Edge neural TTS), listen from the microphone, optional OCR.

**Default focus:** Bulgarian + English — microphone language `bg`, translation target `bg`, Edge neural TTS (Bulgarian voices Kalina / Borislav when “To” is Bulgarian).

## Requirements

- Windows 10/11
- Python 3.11+ (for development)
- Internet for translation, Edge TTS, and Google speech recognition
- Optional: [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) with `eng` + `bul` languages

## Quick start (dev)

```powershell
python -m venv .venv
.\.venv\Scripts\pip.exe install -r requirements-dev.txt
.\.venv\Scripts\python.exe main.py
```

## Tests

```powershell
.\run_tests.ps1
# or
.\.venv\Scripts\python.exe -m pytest tests -q
```

## Build installer

```powershell
.\scripts\build_installer.ps1
```

Outputs:

- Portable: `dist\TextToSpeech\TextToSpeech.exe`
- Setup: `installer_output\FilipovVoiceTranslatorSetup_<version>.exe` (needs Inno Setup 6)

Version is read from the root `VERSION` file (also used by the About dialog and the installer script).

### Optional code signing (SmartScreen)

Set environment variables before building, or create `code_signing.local.ps1` (gitignored):

```powershell
$env:TTS_SIGN_CERT = "C:\path\to\cert.pfx"
$env:TTS_SIGN_PASSWORD = "..."   # optional if cert has no password
$env:TTS_SIGN_TIMESTAMP = "http://timestamp.digicert.com"
.\scripts\build_installer.ps1
```

The build script signs `TextToSpeech.exe` and the setup EXE with `signtool` when a certificate is configured.

## Project layout

| Path | Role |
|------|------|
| `main.py` | Entry point |
| `tts_app/` | Application package |
| `tts_app/workers.py` | Background threads (STT / translate / TTS) |
| `tts_app/data/google_languages.json` | Offline language list |
| `tests/` | Pytest suite |
| `installer/TextToSpeech.iss` | Inno Setup |
| `CHECKPOINT.md` | Bulgarian development notes |

## License

MIT — see [LICENSE](LICENSE).
