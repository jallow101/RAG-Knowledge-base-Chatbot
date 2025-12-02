import PyPDF2
import os
from src.config import DATA_RAW, DATA_PROCESSED

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file and returns it as a clean string.
    """

    text = ""

    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)

        for page in reader.pages:
            try:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
            except Exception as e:
                print(f"Error reading page: {e}")

    return text



def process_and_save_text(filename: str):
    """
    Loads a PDF from /data/raw,
    extracts its text,
    and saves a .txt file into /data/processed.
    """

    pdf_path = os.path.join(DATA_RAW, filename)

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    # 1. Extract text
    text = extract_text_from_pdf(pdf_path)

    # 2. Save processed text
    processed_filename = filename.replace(".pdf", ".txt")
    processed_path = os.path.join(DATA_PROCESSED, processed_filename)

    with open(processed_path, "w", encoding="utf-8") as f:
        f.write(text)

    return processed_path, text


