import streamlit as st
from rag.retriever import retrieve
from rag.generator import generate_answer

st.title(
    "AML & Fraud Detection Co-Pilot"
)

question = st.text_input(
    "Ask AML Compliance Question"
)

if question:

    docs = retrieve(question)

    answer = generate_answer(
        question,
        docs
    )

    st.write(answer)