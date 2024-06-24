import spacy
from spacy import displacy
import streamlit as st

# Load the trained spaCy model
nlp = spacy.load("trained_model")

# Streamlit app
st.title("Legal Named Entity Recognition with spaCy")
st.write("Enter text below or upload a text file to see named entity recognition for legal documents.")

# Text input
text_input = st.text_area("Copy-paste text to analyze", "")

# File upload
uploaded_file = st.file_uploader("Or upload a text file", type="txt")

# Button to proceed with NER analysis
if st.button("Proceed"):
    text = ""
    if text_input:
        text = text_input
    elif uploaded_file:
        text = uploaded_file.read().decode("utf-8")

    if text:
        doc = nlp(text)
        html = displacy.render(doc, style="ent", jupyter=False)
        st.write(html, unsafe_allow_html=True)

        