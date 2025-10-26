import streamlit as st
from core.processing import summarize_docs
from core.state import ResearchState

def summarization_section():
    st.subheader("Summarization")
    if not st.session_state.uploaded_files:
        st.info("Upload PDFs to enable summarization.")
        return

    selected_sum_mode = st.selectbox("Summary Style", ["abstract", "bullet_points", "critical_analysis"])
    st.session_state.use_streaming = st.checkbox("Enable Streaming Mode", value=st.session_state.get("use_streaming", False))

    if st.button("Generate Summary"):
        research_params = {"mode": "literature_review", "summarization_mode": selected_sum_mode}
        state: ResearchState = {
            "query": "Provide a summary of the uploaded documents.",
            "research_params": research_params,
            "current_file": st.session_state.get("current_file"),
            "docs": st.session_state.get("docs", [])
        }
        with st.spinner("Generating summary..."):
            result = summarize_docs(state)
            if result.get("summary"):
                st.subheader("Generated Summary")
                st.write(result["summary"])
            else:
                st.warning("No summary generated.")
        if result.get("truncation_note"):
            st.info(result["truncation_note"])

    with st.expander("📄 Source Documents for Summary"):
        if st.session_state.docs:
            for i, doc in enumerate(st.session_state.docs[:5]):
                preview = getattr(doc, "page_content", str(doc))[:200]
                st.write(f"**Document {i+1}:** {preview}...")
