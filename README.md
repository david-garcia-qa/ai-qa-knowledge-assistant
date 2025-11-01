# 🧠 AI QA Knowledge Assistant
RAG-powered assistant for QA teams. Ask questions about product rules, security requirements, and compliance obligations — get concise answers with source citations.

## 🌍 What this project does
Modern QA engineers spend a lot of time digging through:
- Product specs
- Security / compliance rules
- Historical QA notes
- "Tribal knowledge" not written anywhere cleanly

This project is a lightweight Retrieval-Augmented Generation (RAG) assistant designed for QA teams:
1. It ingests internal documentation (Markdown, text).
2. It builds a local vector index for semantic search.
3. You ask a question in natural language.
4. It retrieves the most relevant passages and asks an LLM to generate a QA-focused answer.
5. It cites where the answer came from.

## 🧩 Typical QA use cases
- "What are the lockout rules after failed login attempts?"
- "Does audit logging need timestamps or user IDs?"
- "Which edge cases do we need to test for MFA code expiry?"
- "What is considered a security blocker for release?"

This turns scattered doc into a QA-ready knowledge base.

## 🏗 Architecture

```text
             ┌──────────────────┐
docs (.md) → │  Loader           │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │  Embedding store  │  ← vector DB (Chroma)
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │  Retriever        │  ← find top-k relevant chunks
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │  Answerer (LLM)   │  ← builds final answer + cites sources
             └──────────────────┘
```

## 📂 Project layout

```text
ai-qa-knowledge-assistant/
├── data/                   # Source documents (specs, audit rules, etc.)
├── rag/
│   ├── loader.py           # Load and split documents
│   ├── embed_store.py      # Create/reuse vector DB
│   ├── retriever.py        # Perform semantic search
│   └── answerer.py         # Generate final answer
├── app.py                  # CLI entry point
├── streamlit_app.py        # Streamlit web UI
├── .env.example            # API key / model config template
├── requirements.txt
└── LICENSE
```

## 🚀 How to run locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create .env
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
MODEL_NAME=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
```

### 3. Ask a question
```bash
python app.py "What are the security requirements for MFA login?"
```

### 4. Example output
```text
Answer:
Users must receive a one-time SMS code when MFA is enabled. The code expires after 2 minutes and cannot be reused. After 3 failed login attempts, the account is locked for 15 minutes.

Sources:
- specs_mfa.md (MFA flow, lockout rules)
- audit_requirements.md (traceability / auditability)
```

## ⚡ Live demo (Streamlit UI)

This project includes a lightweight Streamlit app that exposes the QA Assistant as an interactive UI.

You can:
- Ask questions in plain English (e.g. "What happens after 3 failed login attempts?")
- Get an action-focused QA answer
- See which documentation sources were used (traceability / audit)
- Run it locally **or** deploy it publicly

---

### 🖥 Run the UI locally

1. Install dependencies (if not already done):
```bash
pip install -r requirements.txt
```

2. Create a `.env` file at the project root:
```text
OPENAI_API_KEY=sk-your-real-openai-api-key
MODEL_NAME=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
```

3. Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

4. Open the browser at:
```
http://localhost:8501
```

You’ll get:
- A text box to ask QA questions
- The generated answer
- The list of source documents used (e.g. specs_mfa.md, audit_requirements.md)

---

### ☁ Deploy on Streamlit Cloud (free)

You can deploy this app publicly using Streamlit Cloud, directly from this repository.

1. Push this repository to GitHub (public or private).
2. Go to Streamlit Cloud and create a new app:
   - Repo: `your-username/ai-qa-knowledge-assistant`
   - Entry point: `streamlit_app.py`
3. In Streamlit Cloud, go to:
   **Manage app → Secrets**

4. Add the following secrets (no quotes around the keys, quotes around the values):
```toml
OPENAI_API_KEY = "sk-your-openai-key"
MODEL_NAME = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
```

These values are injected as environment variables.  
They are **not committed** to GitHub.

5. Save. Streamlit will rebuild and launch your app.

Now anyone with the link can ask:
> "What are the security requirements for MFA login?"

…and get:
- Lockout rules
- OTP expiry rules
- Audit obligations
- Plus a “Sources:” section to prove where the answer came from

---

### 🔒 Security note

- `OPENAI_API_KEY` is never stored in the repo.
- `.env` is in `.gitignore`.
- On Streamlit Cloud, secrets are stored in the app settings, not in code.
- The vector store (`chroma_store/`) is ignored as well, because it’s a local cache of embeddings and can be rebuilt at startup.

---

### ✅ What this demonstrates

This UI shows how QA can:
- Query product requirements, security rules, and audit constraints without reading all the docs
- Get actionable, testable statements (“lockout is 15 minutes”, “log every attempt with timestamp”)
- Trace back every answer to specific source files

In other words:
**This is an AI-assisted QA knowledge base powered by Retrieval-Augmented Generation (RAG), delivered as a self-serve tool for testers, auditors, and release managers.**

## 🛠 Tech stack
- Python
- LangChain
- LangChain-OpenAI
- ChromaDB (local vector store)
- Streamlit (interactive UI)
- dotenv for secret management

## 📜 License
MIT License © 2025 David Garcia
For educational and demonstration purposes only.
