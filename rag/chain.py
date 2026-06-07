from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful research assistant.

Use the conversation history and retrieved context
to answer the user's question.

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer:
""")


def generate_answer(
    question,
    retrieved_chunks,
    history=""
):
    context = "\n\n".join(
        chunk.page_content
        for chunk in retrieved_chunks
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "history": history,
            "context": context,
            "question": question
        }
    )

    return response.content
