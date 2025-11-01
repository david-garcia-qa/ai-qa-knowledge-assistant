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

## 🔍 Why this matters for QA
- Faster onboarding: new testers can ask questions instead of reading 80 pages of specs.
- Test design quality: QA can confirm rules (timeouts, lockouts, retry limits) before writing scenarios.
- Compliance & audit: makes it easy to prove what is "mandatory" vs "nice to have".
- Release confidence: security blockers are no longer tribal knowledge.

## 🛠 Tech stack
- Python
- LangChain
- ChromaDB (local vector store)
- OpenAI GPT models (you can swap to any other LLM provider)
- dotenv for secret management

## 📜 License
MIT License © 2025 David Garcia
For educational and demonstration purposes only.
