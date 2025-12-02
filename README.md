# 📚 RAG Knowledge Base Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **LangChain**, and **OpenAI**. This application allows users to upload PDF documents to a secure knowledge base and ask questions, receiving answers based solely on the content of those documents.

## 🚀 Features

- **📄 PDF Ingestion**: Upload and process PDF documents automatically.
- **🔐 Admin Panel**: Secure area for managing the knowledge base (uploading files).
- **🧠 RAG Architecture**: Uses OpenAI's `gpt-4o-mini` and `text-embedding-3-small` for high-quality retrieval and generation.
- **⚡ FAISS Vector Store**: Fast similarity search for retrieving relevant document chunks.
- **💬 Interactive Chat**: Simple and responsive chat interface using Streamlit.

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** (UI)
- **LangChain** (RAG Framework)
- **OpenAI API** (LLM & Embeddings)
- **FAISS** (Vector Database)
- **PyPDF2** (PDF Processing)

## 📂 Project Structure

```
.
├── app/
│   └── streamlit_app.py    # Main application entry point
├── data/                   # Data storage
│   ├── raw/                # Uploaded PDF files
│   ├── processed/          # Extracted text files
│   └── vectorstore/        # FAISS vector index
├── src/
│   ├── config.py           # Configuration settings
│   ├── ingest.py           # PDF processing logic
│   ├── chunker.py          # Text chunking logic
│   ├── vector_store.py     # FAISS vector store operations
│   └── rag_chain.py        # RAG pipeline definition
├── .env.example            # Example environment variables
└── README.md               # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd RAG-Knowledge-base-Chatbot
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit langchain-openai langchain-community faiss-cpu python-dotenv PyPDF2
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```bash
   # Copy the example file (or create new)
   cp .env.example .env
   ```
   
   Open `.env` and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=sk-proj-...
   ADMIN_PASSWORD=adminAi  # Change this to secure your admin panel
   ```

## ▶️ Usage

1. **Run the Application**
   ```bash
   streamlit run app/streamlit_app.py
   ```

2. **Admin Mode (Upload Data)**
   - Open the app in your browser (usually `http://localhost:8501`).
   - Go to the **Sidebar**.
   - Enter the Admin Password (default: `adminAi`).
   - Upload PDF files. They will be automatically chunked and indexed.

3. **User Mode (Chat)**
   - Type your question in the main chat input.
   - The bot will answer based *only* on the uploaded PDFs.

## 🧩 Configuration

You can tweak settings in `src/config.py`:
- `CHUNK_SIZE`: Size of text chunks (default: 1200).
- `CHUNK_OVERLAP`: Overlap between chunks (default: 200).
- `LLM_MODEL`: OpenAI model to use (default: `gpt-4o-mini`).
