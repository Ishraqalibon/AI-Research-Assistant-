import streamlit as st
from core.graph import app as langgraph_app
from core.state import ResearchState
import logging

logger = logging.getLogger(__name__)

def qa_section():
    st.subheader("Standard Q&A")
    citation_style = st.selectbox("Citation Format", ["APA", "IEEE", "MLA", "Chicago"])
    query = st.text_input("Enter your question about the uploaded papers:")

    if st.button("Ask"):
        if not st.session_state.uploaded_files:
            st.warning("⚠️ Please upload PDFs first.")
            return
        state: ResearchState = {
            "query": query,
            "research_params": {"mode": "standard_qa", "citation_style": citation_style},
            "current_file": st.session_state.get("current_file"),
            "docs": st.session_state.get("docs", [])
        }
        with st.spinner("Analyzing and answering..."):
            try:
                result = langgraph_app.invoke(state)
            except Exception as e:
                st.error(f"Processing failed: {e}")
                logger.error(e)
                return

        if result.get("answer"):
            st.subheader("📘 Generated Answer")
            st.write(result["answer"])
        elif result.get("error"):
            st.error(result["error"])
        else:
            st.info("No answer produced.")

        with st.expander("📄 Source Documents"):
            for i, doc in enumerate(result.get("docs", st.session_state.docs[:5])):
                preview = getattr(doc, "page_content", str(doc))[:200]
                st.write(f"**Document {i+1}:** {preview}...")
