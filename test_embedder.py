from rag.loader import load_pdf
from rag.chunker import chunk_documents
from rag.embedder import embed_and_store

pages = load_pdf("uploads/science.1254050.pdf")

chunks = chunk_documents(pages)

vectorstore = embed_and_store(chunks)

print("Vector DB Created Successfully")

print(f"Stored Chunks: {vectorstore._collection.count()}")
