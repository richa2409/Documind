from rag.loader import load_pdf
from rag.chunker import chunk_documents
from rag.embedder import embed_and_store
from rag.retriever import retrieve
from rag.chain import generate_answer

pages = load_pdf("uploads/science.1254050.pdf")

chunks = chunk_documents(pages)

vectorstore = embed_and_store(chunks)

question = "How does chronic pain affect motivation?"

retrieved_chunks = retrieve(vectorstore, question)

answer = generate_answer(
    question,
    retrieved_chunks
)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)
