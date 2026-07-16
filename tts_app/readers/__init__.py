from pathlib import Path

from tts_app.readers.doc_legacy import read_doc
from tts_app.readers.docx_reader import read_docx
from tts_app.readers.pdf_reader import read_pdf
from tts_app.readers.txt_reader import read_txt


def load_text(path: str) -> str:
    p = Path(path)
    suf = p.suffix.lower()
    if suf == ".txt":
        return read_txt(path)
    if suf == ".docx":
        return read_docx(path)
    if suf == ".pdf":
        return read_pdf(path)
    if suf == ".doc":
        return read_doc(path)
    raise ValueError(f"Unsupported file type: {suf}")
