import os
from typing import List
from uuid import uuid4

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from src.config import VECTOR_DB_PATH, EMBEDDING_MODEL


def load_vectorstore():
    """
    Loads an existing FAISS vector DB using the new LangChain API.
    """
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    if not os.path.exists(VECTOR_DB_PATH):
        return None

    try:
        db = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True  # safe if you trust your data
        )
        return db

    except Exception as e:
        print(f"❌ Error loading vector store: {e}")
        return None


def create_vectorstore(chunks: List[str], filename: str):
    """
    Creates a brand new FAISS DB from scratch.
    Adds metadata for filename + unique doc_id.
    """
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    doc_id = str(uuid4())  # unique per document
    metadatas = [{"doc_id": doc_id, "filename": filename} for _ in chunks]

    db = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings,
        metadatas=metadatas
    )

    db.save_local(VECTOR_DB_PATH)
    return db


def update_vectorstore(chunks: List[str], filename: str):
    """
    Adds new chunks to the existing FAISS DB.
    If DB doesn't exist yet, create a new one.
    """

    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    db = load_vectorstore()

    doc_id = str(uuid4())
    metadatas = [{"doc_id": doc_id, "filename": filename} for _ in chunks]

    # Update existing DB
    if db:
        db.add_texts(texts=chunks, metadatas=metadatas)
        db.save_local(VECTOR_DB_PATH)
        return db

    # Otherwise create a new DB
    return create_vectorstore(chunks, filename)


def list_documents():
    """
    Returns a dict of doc_id → filename for all docs in the FAISS index.
    """
    db = load_vectorstore()
    if not db:
        return {}

    docs = {}

    # FAISS stores documents inside db.docstore._dict
    for doc in db.docstore._dict.values():
        meta = doc.metadata
        d_id = meta.get("doc_id")
        fname = meta.get("filename")
        docs[d_id] = fname

    return docs
