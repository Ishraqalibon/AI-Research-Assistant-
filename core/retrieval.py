from core.state import ResearchState
from core.vectorstore import load_vectorstore
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from sentence_transformers import CrossEncoder
from typing import List
from langchain.schema import Document
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
import streamlit as st
import logging

logger = logging.getLogger(__name__)

db = load_vectorstore()

def dense_retrieve(state: ResearchState, k: int = 5):
    current_file = state.get("current_file") or st.session_state.get("current_file")
    if not current_file:
        raise ValueError("No active file specified for dense retrieval")
    if db is None:
        raise ValueError("Embedding DB not available")

    return db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": k,
            "filter": Filter(
                must=[
                    FieldCondition(key="source", match=MatchValue(value=current_file))
                ]
            )
        }
    )

def hybrid_retrieve(state: ResearchState, k: int = 38) -> ResearchState:
    current_file = state.get("current_file") or st.session_state.get("current_file")
    if not current_file:
        raise ValueError("No active file specified for retrieval")

    dense = dense_retrieve(state, k=5)
    file_docs: List[Document] = [d for d in st.session_state.docs if d.metadata.get("source") == current_file]
    sparse = BM25Retriever.from_documents(file_docs)

    ensemble = EnsembleRetriever(retrievers=[dense, sparse], weights=[0.7, 0.3])

    initial_docs = ensemble.get_relevant_documents(state["query"], k=k)

    reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    pairs = [(state["query"], doc.page_content) for doc in initial_docs]
    try:
        scores = reranker.predict(pairs)
    except Exception as e:
        logger.warning(f"Reranker failed: {e}")
        state["docs"] = initial_docs[:5]
        return state

    scored = list(zip(scores, initial_docs))
    scored.sort(key=lambda x: x[0], reverse=True)
    final_docs = [doc for score, doc in scored[:5]]
    state["docs"] = final_docs
    return state
