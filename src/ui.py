import streamlit as st
from .pdf_processing import extract_text_from_pdf
from .nlp_processing import answer_question

def launch_ui():
    st.title("PDF Buddy")
    
    # File uploader for PDF
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if pdf_file is not None:
        # Extract text from the PDF
        pdf_text = extract_text_from_pdf(pdf_file)
        st.text_area("Extracted Text", pdf_text, height=300)
        
        # Question input
        question = st.text_input("Ask a question about the text")
        
        if st.button("Answer"):
            # Process the question and get an answer
            answer = answer_question(question, pdf_text)
            st.write("Answer:", answer)
