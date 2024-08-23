from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFPlumberLoader

import utils.globals as globals

def load_documents():
    """Loads and splits the PDF documents into texts using PDFPlumber."""
    loader = PDFPlumberLoader(globals.PDF_FILE)
    documents = loader.load_and_split()
    return documents

def split_text(documents):
    """Splits the documents into smaller chunks for processing."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False
    )
    chunks = text_splitter.split_documents(documents)
    return chunks

def save_to_chroma(chunks):
    """Saves the text chunks to the Chroma Vector Store."""
    vector_store = Chroma(
        embedding_function=globals.EMBEDDING,
        persist_directory=globals.PERSIST_DIRECTORY,
    )
    vector_store.add_documents(documents=chunks)

def generate_vector_store():
    """Generates the Vector Store from loaded and split documents."""
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)
