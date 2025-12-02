import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

##########################################
# API KEYS
##########################################

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

##########################################
# ADMIN SETTINGS
##########################################

# Admin password for the Streamlit panel
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "adminAi")

##########################################
# PATH SETTINGS
##########################################

# Base data folders
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
VECTOR_DB_PATH = os.path.join(BASE_DIR, "data", "vectorstore")

##########################################
# RAG SETTINGS
##########################################

# Chunking
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

# Embedding model (OpenAI or others)
EMBEDDING_MODEL = "text-embedding-3-small"

# LLM model used for answering questions
LLM_MODEL = "gpt-4o-mini"

##########################################
# VECTORDB SETTINGS
##########################################

VECTOR_DB_TYPE = "faiss"   # or chroma later
