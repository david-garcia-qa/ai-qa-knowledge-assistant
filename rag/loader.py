import os
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(data_dir: str = "data"):
    """
    Load all .md files from the data directory and return a list of dicts:
    { "source": filename, "text": content }
    """
    docs = []
    for file in Path(data_dir).glob("*.md"):
        text = file.read_text(encoding="utf-8")
        docs.append({
            "source": file.name,
            "text": text,
        })
    return docs

def split_documents(docs, chunk_size=600, chunk_overlap=100):
    """
    Split documents into semantically meaningful chunks for retrieval.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " "],
    )

    chunks = []
    for doc in docs:
        for chunk in splitter.split_text(doc["text"]):
            chunks.append({
                "source": doc["source"],
                "text": chunk.strip()
            })
    return chunks
