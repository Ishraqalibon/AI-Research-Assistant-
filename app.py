import streamlit as st
from ui.layout import init_layout
from ui.upload_section import upload_section
from ui.qa_section import qa_section
from ui.citation_section import citation_section
from ui.comparison_section import comparison_section
from ui.summarization_section import summarization_section
import logging
from utils.logging_utils import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

st.set_page_config(page_title="AI Research Assistant", layout="wide")
init_layout()

# Persistent session defaults
if "processed_files_names" not in st.session_state:
    st.session_state.processed_files_names = []
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []
if "docs" not in st.session_state:
    st.session_state.docs = []
if "current_file" not in st.session_state:
    st.session_state.current_file = None
if "use_streaming" not in st.session_state:
    st.session_state.use_streaming = False
if "tools_active" not in st.session_state:
    st.session_state.tools_active = False

# Upload section (left column)
upload_section()

# Main right column: Q&A and tools

st.header("🔍 Research Interface")
# Default to Standard Q&A unless tools activated
qa_section()

# Tools beneath (tabs)
st.header("🛠️ Research Tools")
st.session_state.tools_active = True
tab1, tab2, tab3 = st.tabs(["Citation Generator", "Paper Comparator", "Summarization"])
with tab1:
    citation_section()
with tab2:
    comparison_section()
with tab3:
    summarization_section()
st.session_state.tools_active = False
