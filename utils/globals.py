import os
from langchain_community.embeddings import FastEmbedEmbeddings

# Environment Variables
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')

# Model and Retriever Params
LLM_MODEL_NAME = "llama3.1"
K_RETRIEVER = 20
SCORE_THRESHOLD = 0.1
EMBEDDING = FastEmbedEmbeddings()

# Directories and Files
PERSIST_DIRECTORY = "db"
PERSIST_DATABASE = f"{PERSIST_DIRECTORY}/chroma.sqlite3"
PDF_FILE = "./pdf/Politica_de_Privacidade.pdf"
