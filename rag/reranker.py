from sentence_transformers import CrossEncoder


reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_chunks(
    question,
    chunks,
    top_k=5
):

    pairs = []

    for chunk in chunks:

        pairs.append(
            [
                question,
                chunk.page_content
            ]
        )

    scores = reranker.predict(
        pairs
    )

    ranked = list(
        zip(
            chunks,
            scores
        )
    )

    ranked.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return [
        chunk
        for chunk, score
        in ranked[:top_k]
    ]
