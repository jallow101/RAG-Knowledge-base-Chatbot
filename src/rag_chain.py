from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from src.vector_store import load_vectorstore
from src.config import LLM_MODEL


def get_llm():
    """Load the LLM using LangChain's new API."""
    return ChatOpenAI(
        model=LLM_MODEL,
        temperature=0.1
    )


def get_retriever():
    """Return a FAISS retriever using the new API."""
    db = load_vectorstore()
    if not db:
        raise ValueError("Vector store not found. Please upload PDFs first.")
    return db.as_retriever(search_kwargs={"k": 4})


def build_rag_chain():
    """
    Build a modern LangChain RAG pipeline using Runnable components.
    """

    retriever = get_retriever()
    llm = get_llm()

    # Prompt template
    template = """
You are an AI assistant. Answer the user's question using ONLY the context provided.

If the answer is not in the context, say:
"I don't know based on the current documents."

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )

    # Runnable pipeline (modern RAG)
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return rag_chain
