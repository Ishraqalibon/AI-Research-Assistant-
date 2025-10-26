from typing import TypedDict, List, Optional, Dict, Any
from langchain.schema import Document

class ResearchState(TypedDict, total=False):
    query: str
    docs: List[Document]
    summary: Optional[str]
    answer: Optional[str]
    comparison: Optional[str]
    comparison_metadata: Optional[Dict[str, Any]]
    truncation_note: Optional[str]
    error: Optional[str]
    research_params: Optional[Dict[str, Any]]
    citation_output: Optional[str]
    current_file: Optional[str]
