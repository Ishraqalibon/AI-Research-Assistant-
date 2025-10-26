import streamlit as st
from core.loader import load_and_split_pdf
from core.processing import compare_papers
from core.state import ResearchState
import os

DATA_DIR = "data"

def comparison_section():
    st.subheader("📊 Compare Two Research Papers")
    if not st.session_state.uploaded_files:
        st.info("Upload at least one main paper first to enable comparison.")
        return

    papers = [f["name"] for f in st.session_state.uploaded_files]
    paper1 = st.selectbox("Select Paper 1 (from main uploads)", papers)

    st.markdown("### Upload Paper 2 (for comparison only)")
    uploaded_file_2 = st.file_uploader("Upload a second PDF (temporary)", type=["pdf"], key="comparison_upload")

    comparison_focus = st.text_input("Optional Focus Area", placeholder="e.g., Transformer efficiency")

    if st.button("🔍 Run Comparative Analysis"):
        if not uploaded_file_2:
            st.warning("⚠️ Please upload a second paper.")
            return
        docs_paper1 = [d for d in st.session_state.docs if d.metadata.get("source") == paper1]
        file_path_2 = os.path.join(DATA_DIR, uploaded_file_2.name)
        with open(file_path_2, "wb") as f:
            f.write(uploaded_file_2.getbuffer())
        docs_paper2 = load_and_split_pdf(file_path_2)

        state: ResearchState = {
            "query": comparison_focus or "General comparison",
            "docs": docs_paper1[:10] + docs_paper2[:10],
            "research_params": {"mode": "comparative_analysis", "focus_area": comparison_focus}
        }
        with st.spinner("Running comparative analysis..."):
            result = compare_papers(state)

        st.success("✅ Comparison Complete!")
        meta = result.get("comparison_metadata", {})
        if meta:
            st.markdown("### 🧾 Papers Compared")
            for i, info in enumerate(meta.get("paper_details", []), start=1):
                st.markdown(f"**{i}. {info.get('title')} ({info.get('year')})**")
            if meta.get("focus_area"):
                st.markdown(f"**Focus Area:** {meta['focus_area']}")
        st.markdown("---")
        st.subheader("📋 Comparison Report")
        st.markdown(result.get("comparison", "⚠️ No comparison output."))
