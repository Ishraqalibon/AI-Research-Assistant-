import streamlit as st

def init_layout():
    st.title("📘 Advanced Research Assistant")
    st.markdown(
        """
        Upload PDFs on the left. Use the Research Interface to ask questions,
        generate citations, compare papers, or summarize documents.
        """
    )
    st.sidebar.title("Research Assistant")
    st.sidebar.markdown("Upload PDFs, choose modes, and configure options here.")
