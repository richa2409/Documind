from rag.embedder import load_vectorstore
from rag.planner import create_plan
from rag.agent_retriever import retrieve_with_plan
from rag.chain import generate_answer
from rag.critic import critique_answer


def ask_question(
    question,
    history=""
):

    vectorstore = load_vectorstore()

    # Agent 1: Planner
    plan = create_plan(
        question
    )

    # Agent 2: Retriever
    retrieved_chunks = retrieve_with_plan(
        vectorstore=vectorstore,
        question=question,
        plan=plan
    )

    # Agent 3: Answer Generator
    answer = generate_answer(
        question=question,
        retrieved_chunks=retrieved_chunks,
        history=history
    )

    # Agent 4: Critic
    review = critique_answer(
        question,
        answer
    )

    unique_sources = set()

    for chunk in retrieved_chunks:

        unique_sources.add(
            (
                chunk.metadata.get("source"),
                chunk.metadata.get("page")
            )
        )

    sources = []

    for source, page in sorted(unique_sources):

        sources.append(
            {
                "source": source,
                "page": page
            }
        )

    return {
        "plan": plan,
        "answer": answer,
        "review": review,
        "sources": sources
    }


if __name__ == "__main__":

    question = (
        "Compare motivation findings "
        "with fatigue findings."
    )

    result = ask_question(
        question
    )

    print("\n" + "=" * 60)
    print("DOCUMIND AGENTIC RAG")
    print("=" * 60)

    print("\nQUESTION:")
    print(question)

    print("\nPLAN:")
    print(result["plan"])

    print("\nANSWER:")
    print(result["answer"])

    print("\nCRITIC REVIEW:")
    print(result["review"])

    print("\nSOURCES:")

    for source in result["sources"]:

        print(
            f"{source['source']} "
            f"- Page {source['page']}"
        )

    print("\n" + "=" * 60)
