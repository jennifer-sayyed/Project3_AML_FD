from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

db = FAISS.load_local(
    "vectordb",
    embedding,
    allow_dangerous_deserialization=True
)

def retrieve(query):

    return db.similarity_search(
        query,
        k=5
    )