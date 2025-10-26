import streamlit as st
from core.processing import generate_bibliographic_citation
from core.state import ResearchState

def citation_section():
    st.subheader("📚 Generate Bibliographic Citation")
    selected_style = st.selectbox("Citation Style", ["APA", "IEEE", "MLA", "Chicago"], index=0)

    if st.button("🧾 Generate Citations"):
        if not st.session_state.docs:
            st.warning("⚠️ Please upload and process a PDF first.")
            return
        state: ResearchState = {
            "docs": st.session_state.docs,
            "research_params": {"citation_style": selected_style}
        }
        with st.spinner("Generating bibliographic citations..."):
            result = generate_bibliographic_citation(state)
        citation_output = result.get("citation_output", "")
        if citation_output:
            st.success("✅ Citations Generated Successfully!")
            st.code(citation_output)
        else:
            st.warning("No citation could be generated. Check PDF metadata.")
