import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Parameters:
        pdf_file (UploadedFile): A file-like object representing the uploaded PDF.

    Returns:
        str: The extracted text from the PDF.
    """
    extracted_text = ""

    # Open the PDF file
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        # Iterate over each page
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Get page
            extracted_text += page.get_text("text")  # Extract text

    return extracted_text
