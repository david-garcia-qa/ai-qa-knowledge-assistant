import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

def build_or_load_vectorstore(chunks, persist_dir="chroma_store"):
    """
    Build (or reload) a persistent Chroma vector DB from the given chunks.
    If the DB already exists, just load it.
    """
    embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    embeddings = OpenAIEmbeddings(model=embedding_model)

    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        return Chroma(persist_directory=persist_dir, embedding_function=embeddings)

    texts = [c["text"] for c in chunks]
    metadatas = [{"source": c["source"]} for c in chunks]

    vectordb = Chroma.from_texts(
        texts=texts,
        metadatas=metadatas,
        embedding=embeddings,
        persist_directory=persist_dir,
    )

    vectordb.persist()
    return vectordb
