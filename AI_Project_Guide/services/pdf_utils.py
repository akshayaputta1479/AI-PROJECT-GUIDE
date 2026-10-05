def extract_pdf_text(file_obj):
    try:
        from pypdf import PdfReader
        reader = PdfReader(file_obj)
        return "\n".join((page.extract_text() or "") for page in reader.pages).strip()
    except Exception as exc:
        return f"Unable to read PDF: {exc}"

def chunk_text(text, chunk_size=1200, overlap=150):
    text=text.strip()
    if not text: return []
    chunks=[]
    start=0
    while start < len(text):
        end=min(len(text), start+chunk_size)
        chunks.append(text[start:end])
        if end == len(text): break
        start=end-overlap
    return chunks
