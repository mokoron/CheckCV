from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
import docx2txt
import fitz
import streamlit as st


@st.cache
def load_model():
    # model = SentenceTransformer('sentence-transformers/all-roberta-large-v1')
    # model = 'model\pytorch_model.bin'
    model = SentenceTransformer('all-MiniLM-L12-v2')
    return model

@st.cache
def embedding(text, model):
    emb = model.encode(text)
    return emb


def similar(emb1, emb2):
    similarity = list(cosine_similarity(emb1.reshape(1, -1), emb2.reshape(1, -1)))
    return similarity[0] * 100


def pdfread(uploaded_doc):
    with fitz.open(uploaded_doc) as doc:
        cv = ""
        for page in doc:
            cv = ''.join([cv, page.get_text()])
    return cv


def docxread(uploaded_doc):
    cv = docx2txt.process(uploaded_doc)
    return cv
