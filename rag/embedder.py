from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

PERSIST_DIRECTORY = "./vectorstore"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vectorstore(
    chunks,
    collection_name="documind"
):

    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    vectorstore.add_documents(
        chunks
    )

    return vectorstore


def load_vectorstore(
    collection_name="documind"
):

    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    return vectorstore
