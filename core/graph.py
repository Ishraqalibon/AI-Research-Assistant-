from langgraph.graph import StateGraph, START, END
from core.state import ResearchState
from functools import partial
from core.retrieval import hybrid_retrieve
from core.processing import generate_answer, summarize_docs, compare_papers, generate_bibliographic_citation
from core.vectorstore import load_vectorstore

db = load_vectorstore()

graph = StateGraph(ResearchState)
graph.add_node("retrieve", partial(hybrid_retrieve))
graph.add_node("generate_answer", generate_answer)
graph.add_node("summarize", summarize_docs)
graph.add_node("compare", compare_papers)
graph.add_node("generate_citations", generate_bibliographic_citation)

def route_task(state: ResearchState) -> str:
    mode = state.get("research_params", {}).get("mode", "standard_qa")
    if mode == "literature_review":
        return "summarize"
    elif mode == "comparative_analysis":
        return "compare"
    elif mode == "Generate Citations":
        return "generate_citations"
    else:
        return "generate_answer"

graph.add_edge(START, "retrieve")
graph.add_conditional_edges("retrieve", route_task, {
    "generate_answer": "generate_answer",
    "summarize": "summarize",
    "compare": "compare",
    "generate_citations": "generate_citations",
})
graph.add_edge("generate_answer", END)
graph.add_edge("summarize", END)
graph.add_edge("compare", END)
graph.add_edge("generate_citations", END)

app = graph.compile()
