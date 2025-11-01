import sys
from rag.loader import load_documents, split_documents
from rag.embed_store import build_or_load_vectorstore
from rag.retriever import retrieve_relevant_context
from rag.answerer import build_answer

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py \"your question here\"")
        sys.exit(1)

    question = sys.argv[1]

    # 1. Load and chunk docs
    docs = load_documents("data")
    chunks = split_documents(docs)

    # 2. Build or load vector store
    vectordb = build_or_load_vectorstore(chunks)

    # 3. Retrieve top-k relevant chunks
    retrieved = retrieve_relevant_context(vectordb, question, k=4)

    # 4. Build final answer
    answer = build_answer(question, retrieved)

    print("\n================= QA ASSISTANT ANSWER =================\n")
    print(answer)
    print("\n=======================================================\n")

if __name__ == "__main__":
    main()
