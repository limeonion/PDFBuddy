import os
import logging
import re

def setup_logging(log_file="app.log"):
    """
    Sets up logging for the application.

    Parameters:
        log_file (str): The file where logs should be written.

    Returns:
        None
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logging.info("Logging setup complete.")

def sanitize_text(text):
    """
    Cleans and sanitizes text by removing unwanted characters and normalizing whitespace.

    Parameters:
        text (str): The raw text to sanitize.

    Returns:
        str: The sanitized text.
    """
    # Remove non-printable characters
    sanitized_text = re.sub(r'[^\x20-\x7E]+', ' ', text)
    # Normalize whitespace
    sanitized_text = ' '.join(sanitized_text.split())
    return sanitized_text

def ensure_directory_exists(dir_path):
    """
    Ensures that a directory exists. If not, it creates the directory.

    Parameters:
        dir_path (str): The path to the directory.

    Returns:
        None
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        logging.info(f"Created directory: {dir_path}")
    else:
        logging.info(f"Directory already exists: {dir_path}")

def split_text_into_chunks(text, chunk_size=500):
    """
    Splits a long text into smaller chunks, each of a specified size.

    Parameters:
        text (str): The text to be split.
        chunk_size (int): The maximum size of each chunk.

    Returns:
        list: A list of text chunks.
    """
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks
