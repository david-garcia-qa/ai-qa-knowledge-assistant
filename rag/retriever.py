def retrieve_relevant_context(vectordb, query: str, k: int = 4):
    """
    Return top-k relevant chunks for the given query.
    Each chunk includes text + source metadata.
    """
    results = vectordb.similarity_search(query, k=k)
    return results  # list of Documents with .page_content and .metadata
