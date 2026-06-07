from rag.retriever import retrieve
from rag.reranker import rerank_chunks


def retrieve_with_plan(
    vectorstore,
    question,
    plan
):

    search_query = f"""
Question:
{question}

Plan:
{plan}
"""

    chunks = retrieve(
        vectorstore,
        search_query,
        k=20
    )

    chunks = rerank_chunks(
        question,
        chunks,
        top_k=5
    )

    return chunks
