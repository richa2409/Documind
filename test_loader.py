from rag.loader import load_pdf

pages = load_pdf("uploads/science.1254050.pdf")

print(f"Total Pages: {len(pages)}")

print("\nFirst Page Preview:\n")

print(pages[0]["text"][:1000])
