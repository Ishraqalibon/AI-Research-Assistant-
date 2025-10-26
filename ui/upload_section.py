import streamlit as st
import os
from core.loader import load_and_split_pdf
from core.vectorstore import build_vectorstore
import logging

logger = logging.getLogger(__name__)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def upload_section():
    col = st.sidebar
    col.header("📤 Upload Research Papers")
    uploaded_files = col.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        if not isinstance(uploaded_files, list):
            uploaded_files = [uploaded_files]

        new_docs = []
        for uploaded_file in uploaded_files:
            if uploaded_file.name in st.session_state.processed_files_names:
                continue
            file_path = os.path.join(DATA_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            try:
                chunks = load_and_split_pdf(file_path)
                new_docs.extend(chunks)
                st.session_state.processed_files_names.append(uploaded_file.name)
                st.session_state.uploaded_files.append({"name": uploaded_file.name, "path": file_path})
                st.session_state.current_file = uploaded_file.name
            except Exception as e:
                st.error(f"Failed to process {uploaded_file.name}: {e}")
                logger.error(e)

        if new_docs:
            try:
                st.session_state.docs.extend(new_docs)
                build_vectorstore(new_docs)
                st.success(f"✅ {len(new_docs)} chunks processed and vector store updated.")
            except Exception as e:
                st.error(f"Vectorstore build failed: {e}")
                logger.error(e)

    if st.session_state.uploaded_files:
        col.markdown("**Uploaded files:**")
        for f in st.session_state.uploaded_files:
            col.write(f"- {f['name']}")
    else:
        col.info("No files uploaded yet.")
