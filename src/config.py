# src/config.py

import os

# Directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "../logs")
OUTPUT_DIR = os.path.join(BASE_DIR, "../output")

# Logging settings
LOG_FILE = os.path.join(LOG_DIR, "app.log")
LOG_LEVEL = "INFO"

# PDF processing settings
PDF_TEXT_CHUNK_SIZE = 500  # Maximum number of words per chunk

# NLP settings
NLP_MODEL_NAME = "distilbert-base-uncased-distilled-squad"  # Hugging Face model for QA

# Streamlit UI settings
UI_TITLE = "PDF Buddy"
UI_FILE_UPLOAD_LABEL = "Upload a PDF file"
UI_QUESTION_INPUT_LABEL = "Ask a question about the text"
UI_ANSWER_BUTTON_LABEL = "Answer"
UI_EXTRACTED_TEXT_AREA_LABEL = "Extracted Text"

# Other settings
DEFAULT_ENCODING = "utf-8"

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
