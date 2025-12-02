import streamlit as st
import os

from src.config import ADMIN_PASSWORD
from src.ingest import process_and_save_text
from src.chunker import chunk_text
from src.vector_store import update_vectorstore, list_documents
from src.rag_chain import build_rag_chain


# -------------------------------
# App Settings
# -------------------------------
st.set_page_config(
    page_title="Knowledge Base Chatbot",
    layout="wide"
)

st.title("📚 Knowledge Base Chatbot")
st.write("Ask questions based only on the ingested documents.")


# -------------------------------
# Admin Authentication
# -------------------------------
def is_admin():
    pwd = st.sidebar.text_input("Admin Password", type="password")
    return pwd == ADMIN_PASSWORD


admin_mode = is_admin()

if admin_mode:
    st.sidebar.success("Admin Verified ✔️")
else:
    st.sidebar.info("Enter admin password to unlock PDF upload.")


# -------------------------------
# Admin Panel — Upload PDFs
# -------------------------------
if admin_mode:

    st.subheader("🔐 Admin Panel — Upload and Ingest PDFs")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        for pdf in uploaded_files:

            # Save PDF to /data/raw
            pdf_path = os.path.join("data", "raw", pdf.name)
            with open(pdf_path, "wb") as f:
                f.write(pdf.getbuffer())

            st.write(f"📄 Processing: {pdf.name}")

            # Extract & save text
            processed_path, text = process_and_save_text(pdf.name)

            # Chunk text
            chunks = chunk_text(text)

            # Update vector DB
            update_vectorstore(chunks, pdf.name)

            st.success(f"Added {pdf.name} to vector database!")

    st.divider()

    # Show stored documents
    st.subheader("📁 Documents Stored")
    docs = list_documents()

    if docs:
        for doc_id, fname in docs.items():
            st.write(f"**{fname}** (doc_id: {doc_id})")
    else:
        st.write("No documents stored yet.")


# -------------------------------
# User Chat Interface
# -------------------------------
st.subheader("💬 Ask a Question")

query = st.text_input("Type your question here:")

if st.button("Ask"):

    try:
        chain = build_rag_chain()
        response = chain.invoke(query)
        st.write("### 🧠 Answer")
        st.write(response.content)

    except Exception as e:
        st.error(f"Error: {e}")
