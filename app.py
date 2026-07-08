from fastapi import FastAPI
from rag.retriever import retrieve
from rag.generator import generate_answer

app = FastAPI()

@app.get("/ask")

def ask(question: str):

    docs = retrieve(question)

    answer = generate_answer(
        question,
        docs
    )

    return {

        "question": question,
        "answer": answer
    }