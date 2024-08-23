from flask import Flask, request, jsonify
from pathlib import Path
from langchain_chroma import Chroma
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from utils.vector_store import generate_vector_store
import utils.globals as globals

# LLM initialization
cached_llm = Ollama(model=globals.LLM_MODEL_NAME, base_url=globals.OLLAMA_BASE_URL)
PROMPT_TEMPLATE = PromptTemplate.from_template("""
    Responda à pergunta com base no contexto: {context}
    --
    Responda à pergunta com base no contexto acima: {input}
""")

# Flask
app = Flask(__name__)

def get_vector_store():
    """Initializes the Chroma Vector Store."""
    return Chroma(persist_directory=globals.PERSIST_DIRECTORY, embedding_function=globals.EMBEDDING)

def create_qa_chain():
    """Creates the question and answer chain using the LLM and Vector Store."""
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": globals.K_RETRIEVER, "score_threshold": globals.SCORE_THRESHOLD}
    )
    document_chain = create_stuff_documents_chain(cached_llm, PROMPT_TEMPLATE)
    return create_retrieval_chain(retriever, document_chain)

@app.route("/ask", methods=["POST"])
def ask_question():
    """API route to answer questions."""
    query = request.json.get("query")
    if not query:
        return jsonify({"error": "A query is required"}), 400
    
    qa_chain = create_qa_chain()
    result = qa_chain.invoke({"input": query})
    
    return jsonify({"answer": result["answer"]})

def start_app():
    """Starts the application."""
    app.run(host=globals.FLASK_HOST, debug=True)

    # Performs RAG if AI does not have it
    my_file = Path(globals.PERSIST_DATABASE)
    if not my_file.is_file():
        generate_vector_store()

if __name__ == "__main__":
    start_app()
