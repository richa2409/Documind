from pypdf import PdfReader
import os


def load_pdf(
    pdf_path,
    source_name=None
):
    reader = PdfReader(pdf_path)

    if source_name is None:
        source_name = os.path.basename(
            pdf_path
        )

    pages = []

    for page_number, page in enumerate(
        reader.pages
    ):

        text = page.extract_text()

        pages.append(
            {
                "page": page_number + 1,
                "text": text,
                "source": source_name
            }
        )

    return pages
