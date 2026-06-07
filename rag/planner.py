from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def create_plan(question):

    prompt = f"""
You are a document retrieval planner.

Create a retrieval plan for answering
the user's question using uploaded documents.

Question:
{question}

Requirements:

- Identify key concepts.
- Identify comparison targets if any.
- Keep the plan short.
- Maximum 5 steps.
- Do NOT mention internet searches.
- Do NOT mention external databases.

Return only the plan.

Example:

1. Find motivation-related findings.
2. Find fatigue-related findings.
3. Compare relationships.
"""

    response = llm.invoke(
        prompt
    )

    return response.content
