import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents(folder_path):

    docs = []

    print(f"Scanning: {folder_path}")

    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return docs

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            path = os.path.join(folder_path, file)

            print(f"Loading: {path}")

            loader = PyPDFLoader(path)

            docs.extend(loader.load())

    return docs