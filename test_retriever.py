from rag.loader import load_pdf
from rag.chunker import chunk_documents
from rag.embedder import embed_and_store
from rag.retriever import retrieve

pages = load_pdf("uploads/science.1254050.pdf")

chunks = chunk_documents(pages)

vectorstore = embed_and_store(chunks)

question = "How does chronic pain affect motivation?"

results = retrieve(vectorstore, question)

print(f"Retrieved {len(results)} chunks\n")

for i, chunk in enumerate(results, start=1):
    print("=" * 50)
    print(f"Result {i}")
    print(f"Page: {chunk.metadata.get('page')}")
    print(chunk.page_content[:500])
    print()
