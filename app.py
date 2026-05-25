import tempfile
import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store
from utils.rag_pipeline import build_rag_chain


st.set_page_config(
    page_title="PDF Chat Intelligence",
    page_icon="📄",
    layout="wide"
)

st.title("RAG-Powered PDF Chatbot with Groq")

st.write("Upload PDF and ask questions using AI")


if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None


# SIDEBAR
with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    process_button = st.button("Process PDF")


# PROCESS PDF
if uploaded_file and process_button:

    with st.spinner("Processing PDF..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:

            tmp_file.write(uploaded_file.read())

            pdf_path = tmp_file.name

        documents = load_pdf(pdf_path)

        chunks = split_documents(documents)

        embeddings = get_embedding_model()

        vectorstore = create_vector_store(
            chunks,
            embeddings
        )

        qa_chain = build_rag_chain(vectorstore)

        st.session_state.qa_chain = qa_chain

        st.success("PDF Processed Successfully")


# ASK QUESTION
question = st.text_input("Ask Question From PDF")


if question:

    if st.session_state.qa_chain is None:

        st.warning("Please upload and process PDF first")

    else:

        with st.spinner("Generating Answer..."):

            response = st.session_state.qa_chain(
                {"query": question}
            )

            st.subheader("Answer")

            st.write(response["result"])

         