
from rag.loader import load_pdf
from rag.chunker import chunk_documents
from rag.embedder import create_vectorstore


def ingest_pdf(
    pdf_path,
    source_name=None
):

    pages = load_pdf(
        pdf_path,
        source_name
    )

    chunks = chunk_documents(
        pages
    )

    create_vectorstore(
        chunks
    )

    return {
        "document": source_name,
        "pages": len(pages),
        "chunks": len(chunks)
    }


if __name__ == "__main__":

    result = ingest_pdf(
        "uploads/science.1254050.pdf",
        "science.1254050.pdf"
    )

    print(result)
