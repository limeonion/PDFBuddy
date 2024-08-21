import spacy
from transformers import pipeline

# Load the spaCy model for basic NLP tasks (make sure to download it beforehand)
nlp = spacy.load("en_core_web_sm")

# Load the pre-trained question answering pipeline from Hugging Face
qa_pipeline = pipeline("question-answering")

def preprocess_text(text):
    """
    Preprocesses the extracted text for better NLP results.

    Parameters:
        text (str): The raw text extracted from the PDF.

    Returns:
        str: The cleaned and preprocessed text.
    """
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    cleaned_text = " ".join(sentences)
    return cleaned_text

def answer_question(question, context):
    """
    Answers a question based on the provided context.

    Parameters:
        question (str): The question posed by the user.
        context (str): The text extracted from the PDF.

    Returns:
        str: The answer to the question.
    """
    # Use the Hugging Face QA pipeline to find the answer
    result = qa_pipeline(question=question, context=context)
    return result['answer']
