import fitz


def read_pdf(path: str) -> str:
    doc = fitz.open(path)
    try:
        parts = []
        for page in doc:
            parts.append(page.get_text())
        return "\n".join(parts)
    finally:
        doc.close()
