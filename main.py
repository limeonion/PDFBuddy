# main.py

from src.pdf_processing import extract_text_from_pdf
from src.nlp_processing import answer_question
from src.utils import setup_logging, ensure_directory_exists
from src.config import LOG_FILE, LOG_LEVEL, NLP_MODEL_NAME, PDF_TEXT_CHUNK_SIZE, UI_TITLE
from src.ui import launch_ui

def main():
    # Setup logging using settings from config.py
    setup_logging(log_file=LOG_FILE, level=LOG_LEVEL)
    
    # Ensure necessary directories exist (logs, output)
    ensure_directory_exists("logs/")
    ensure_directory_exists("output/")

    # Display a welcome message with the app title
    print(f"Welcome to {UI_TITLE} - Your PDF Interpretation Assistant!")

    # Launch the user interface (UI)
    launch_ui()

if __name__ == "__main__":
    main()
