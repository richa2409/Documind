from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def critique_answer(
    question,
    answer
):

    prompt = f"""
You are a quality assurance agent.

Question:
{question}

Answer:
{answer}

Evaluate:

1. Relevance (1-10)
2. Completeness (1-10)
3. Clarity (1-10)

Return:

Relevance:
Completeness:
Clarity:

One sentence feedback.
"""

    response = llm.invoke(
        prompt
    )

    return response.content
