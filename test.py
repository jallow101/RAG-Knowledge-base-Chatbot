from src.ingest import process_and_save_text
from src.chunker import chunk_text
from src.vector_store import update_vectorstore
from src.rag_chain import build_rag_chain

# 1. Process PDF
processed_path, text = process_and_save_text("Nudge.pdf")

# 2. Chunk text safely
chunks = chunk_text(text)  # or chunk_text(text[:3500]) for testing

# 3. Update / create vector store
update_vectorstore(chunks, "Nudge.pdf")

# 4. Build RAG chain
chain = build_rag_chain()

# 5. Ask something — pass string, not dict
query = "what is a nudge ??"
resp = chain.invoke(query)
print(resp)
