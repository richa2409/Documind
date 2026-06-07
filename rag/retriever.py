def retrieve(
    vectorstore,
    search_query,
    k=4
):
    results = vectorstore.similarity_search(
        search_query,
        k=k
    )

    return results
