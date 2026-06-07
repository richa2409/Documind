from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = []

    for page in pages:

        page_chunks = splitter.create_documents(
            [page["text"]],
            metadatas=[
                {
                    "page": page["page"],
                    "source": page["source"]
                }
            ]
        )

        chunks.extend(page_chunks)

    return chunks
