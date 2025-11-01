import streamlit as st
from rag.loader import load_documents, split_documents
from rag.embed_store import build_or_load_vectorstore
from rag.retriever import retrieve_relevant_context
from rag.answerer import build_answer

st.set_page_config(page_title="AI QA Knowledge Assistant", page_icon="🧠")

st.title("🧠 AI QA Knowledge Assistant")
st.markdown(
    "<style>body {font-family: 'Inter', sans-serif;} .stTextArea textarea {font-size:16px;}</style>",
    unsafe_allow_html=True,
)
st.markdown(
    """
Ask QA-related questions about product requirements, specs, or audit rules.
The assistant retrieves relevant context from your documentation and provides a concise, test-oriented answer.
"""
)

# Load & prepare documents once
@st.cache_resource
def init_vectorstore():
    docs = load_documents("data")
    chunks = split_documents(docs)
    vectordb = build_or_load_vectorstore(chunks)
    return vectordb

vectordb = init_vectorstore()

# Input area
question = st.text_area("💬 Enter your QA question:", placeholder="e.g., What are the security requirements for MFA login?")

if st.button("Ask") or question:
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Analyzing documentation..."):
            retrieved = retrieve_relevant_context(vectordb, question, k=4)
            answer = build_answer(question, retrieved)

        st.subheader("🧩 QA Assistant Answer")
        st.markdown(answer)

        # Display retrieved sources
        st.subheader("📚 Retrieved Contexts")
        for doc in retrieved:
            st.markdown(f"**{doc.metadata.get('source')}**")
            st.text(doc.page_content[:400] + ("..." if len(doc.page_content) > 400 else ""))
