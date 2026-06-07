from rag.loader import load_pdf
from rag.chunker import chunk_documents

pages = load_pdf("uploads/science.1254050.pdf")

chunks = chunk_documents(pages)

print(f"Pages: {len(pages)}")
print(f"Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])

print("\nMetadata:\n")
print(chunks[0].metadata)
