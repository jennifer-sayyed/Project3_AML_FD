from ingestion.loader import load_documents
from ingestion.chunker import split_documents

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

documents = []

documents += load_documents("data/FATF")
documents += load_documents("data/RBI")
documents += load_documents("data/FIU")
documents += load_documents("data/SARS")

print("Documents loaded:", len(documents))

chunks = split_documents(documents)

print("Chunks created:", len(chunks))

if len(chunks) == 0:
    raise ValueError(
        "No document chunks found. Check PDFs."
    )

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

db = FAISS.from_documents(
    chunks,
    embedding
)

db.save_local("vectordb")

print("Vector DB Created Successfully")