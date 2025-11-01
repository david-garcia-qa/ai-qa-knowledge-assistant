import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

def build_answer(question: str, retrieved_docs):
    """
    Use LLM to synthesize an answer for QA, with citations.
    """
    llm = ChatOpenAI(
        model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        temperature=0.2,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Build context
    context_blocks = []
    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(
            f"[Source {i}: {doc.metadata.get('source', 'unknown')}]\n{doc.page_content}"
        )
    context_text = "\n\n".join(context_blocks)

    prompt = ChatPromptTemplate.from_template("""
You are a QA assistant. You answer questions about product behavior,
security rules, business rules, and audit/compliance expectations.

You MUST:
- Answer concisely.
- Focus on what must be tested.
- Mention any timeouts, limits, retries, lockouts, etc.
- At the end, list which sources you used.

User question:
{question}

Relevant documentation:
{context}

Now provide:
1. The answer for QA (what needs to be tested / validated).
2. A "Sources:" section listing file names you relied on.
""")

    chain = prompt | llm
    result = chain.invoke({
        "question": question,
        "context": context_text
    })

    return result.content
