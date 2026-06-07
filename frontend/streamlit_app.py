import sys
import os
import tempfile

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import streamlit as st

from app import ask_question
from ingest import ingest_pdf

st.set_page_config(
    page_title="DocuMind",
    page_icon="📄",
    layout="wide"
)

st.title("📄 DocuMind")
st.subheader("Multi-Document Agentic RAG Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents" not in st.session_state:
    st.session_state.documents = []

if "total_pages" not in st.session_state:
    st.session_state.total_pages = 0

if "total_chunks" not in st.session_state:
    st.session_state.total_chunks = 0


# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.header("📚 Knowledge Base")

    st.metric(
        "Documents",
        len(st.session_state.documents)
    )

    st.metric(
        "Pages",
        st.session_state.total_pages
    )

    st.metric(
        "Chunks",
        st.session_state.total_chunks
    )

    st.divider()

    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        if st.button(
            "Process Documents"
        ):

            for uploaded_file in uploaded_files:

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as tmp_file:

                    tmp_file.write(
                        uploaded_file.getbuffer()
                    )

                    pdf_path = tmp_file.name

                with st.spinner(
                    f"Processing {uploaded_file.name}..."
                ):

                    stats = ingest_pdf(
                        pdf_path,
                        uploaded_file.name
                    )

                st.session_state.documents.append(
                    uploaded_file.name
                )

                st.session_state.total_pages += (
                    stats["pages"]
                )

                st.session_state.total_chunks += (
                    stats["chunks"]
                )

            st.success(
                "Knowledge Base Updated Successfully"
            )

    if st.session_state.documents:

        st.divider()

        st.subheader(
            "Indexed Documents"
        )

        for doc in st.session_state.documents:

            st.write(
                f"📄 {doc}"
            )


# ==================================
# CHAT HISTORY
# ==================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )


# ==================================
# CHAT INPUT
# ==================================

question = st.chat_input(
    "Ask a question about your documents"
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message(
        "user"
    ):
        st.markdown(
            question
        )

    history = ""

    for msg in st.session_state.messages[-6:]:

        history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    with st.spinner(
        "Agentic RAG Working..."
    ):

        result = ask_question(
            question=question,
            history=history
        )

    answer = result["answer"]

    # ==================================
    # AGENT PLAN
    # ==================================

    with st.expander(
        "🤖 Agent Plan"
    ):
        st.markdown(
            result["plan"]
        )

    # ==================================
    # CRITIC REVIEW
    # ==================================

    with st.expander(
        "🔍 Critic Review"
    ):
        st.markdown(
            result["review"]
        )

    # ==================================
    # SOURCES
    # ==================================

    sources_text = ""

    for source in result["sources"]:

        sources_text += (
            f"\n• {source['source']} "
            f"(Page {source['page']})"
        )

    final_response = (
        answer
        + "\n\n### Sources"
        + sources_text
    )

    with st.chat_message(
        "assistant"
    ):
        st.markdown(
            final_response
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_response
        }
    )
