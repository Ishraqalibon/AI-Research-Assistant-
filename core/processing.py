import os
import logging
from typing import Dict
from core.state import ResearchState
from langchain_openai import ChatOpenAI
from core.config import OPENAI_MODEL
from langchain.schema import Document

logger = logging.getLogger(__name__)

def _get_llm():
    return ChatOpenAI(model=os.getenv("OPENAI_MODEL", OPENAI_MODEL), temperature=0)

def generate_answer(state: ResearchState) -> ResearchState:
    llm = _get_llm()
    docs = state.get("docs", [])
    if not docs:
        state["error"] = "No documents provided for answering"
        return state

    context = "\n\n".join([d.page_content for d in docs])
    citations = [f"[{i+1}] Source: {d.metadata.get('source','unknown')}" for i, d in enumerate(docs)]

    prompt = f"""
    You are a research assistant. Answer the question using only the provided context.
    If the context doesn't contain relevant information, say so.
    Include inline citations like [1] and list all sources at the end.

    Question: {state.get('query')}
    Context:
    {context}
    """

    try:
        res = llm.invoke(prompt)
        state["answer"] = res.content + "\n\nSources:\n" + "\n".join(citations)
    except Exception as e:
        state["error"] = f"LLM call failed: {e}"
        logger.error(state["error"])
    return state

def summarize_docs(state: ResearchState) -> ResearchState:
    llm = _get_llm()
    docs = state.get("docs", [])
    if not docs:
        state["summary"] = "⚠️ No documents found to summarize."
        return state

    mode = state.get("research_params", {}).get("summarization_mode", "abstract")
    research_focus = state.get("research_params", {}).get("focus_area", "")

    templates = {
        "abstract": "Create a concise abstract (2-3 sentences) focusing on main question, method, findings, significance.\n\nText: {text}",
        "bullet_points": "Extract key points as bullet points: objective, methodology, key results, limitations, future work.\n\nText: {text}",
        "critical_analysis": "Provide critical analysis (strengths, weaknesses, methodological concerns, contribution significance).\n\nText: {text}"
    }
    template = templates.get(mode, templates["abstract"])

    text = "\n\n".join([d.page_content for d in docs])
    if len(text) > 8000:
        text = text[:4000] + "\n\n...[middle content omitted]...\n\n" + text[-4000:]
        state["truncation_note"] = "Document truncated for summarization."

    if research_focus:
        template += f"\n\nPay attention to: {research_focus}"

    try:
        res = llm.invoke(template.replace("{text}", text))
        state["summary"] = res.content
    except Exception as e:
        state["error"] = f"Summarization failed: {e}"
        logger.error(state["error"])
        state["summary"] = state["error"]
    return state

def compare_papers(state: ResearchState) -> ResearchState:
    docs = state.get("docs", [])
    if not docs:
        state["comparison"] = "⚠️ No documents provided for comparison."
        return state

    sources = list({d.metadata.get("source", "unknown") for d in docs})
    if len(sources) < 2:
        state["comparison"] = "⚠️ Need at least two distinct PDFs to compare."
        return state

    grouped = {src: [d for d in docs if d.metadata.get("source") == src] for src in sources[:2]}
    p1, p2 = sources[:2]
    def join(chunks, limit=6000):
        text = "\n".join(d.page_content for d in chunks)
        return text[:limit] + ("\n...[truncated]..." if len(text) > limit else "")

    text1, text2 = join(grouped[p1]), join(grouped[p2])
    title1 = grouped[p1][0].metadata.get("title", p1)
    title2 = grouped[p2][0].metadata.get("title", p2)
    year1 = grouped[p1][0].metadata.get("year", "Unknown")
    year2 = grouped[p2][0].metadata.get("year", "Unknown")
    focus = state.get("research_params", {}).get("focus_area", "")

    llm = _get_llm()
    prompt = f"""
    You are an expert research analyst. Compare two papers.

    FOCUS AREA: {focus or 'General comparison'}

    PAPER 1: {title1} ({year1})
    {text1}

    PAPER 2: {title2} ({year2})
    {text2}

    Provide structured markdown: Executive Summary, Methodology Comparison, Key Findings, Strengths/Limitations, Contributions, Conclusion.
    """
    try:
        res = llm.invoke(prompt)
        state["comparison"] = res.content
        state["comparison_metadata"] = {
            "papers_compared": 2,
            "focus_area": focus,
            "paper_details": [
                {"title": title1, "year": year1, "source": p1},
                {"title": title2, "year": year2, "source": p2},
            ]
        }
    except Exception as e:
        state["comparison"] = f"❌ Comparison failed: {e}"
        state["error"] = str(e)
    return state

def generate_bibliographic_citation(state: ResearchState) -> ResearchState:
    docs = state.get("docs", [])
    style = state.get("research_params", {}).get("citation_style", "APA")
    if not docs:
        state["citation_output"] = "⚠️ No documents found for citation generation."
        return state

    doc = docs[0]
    metadata = getattr(doc, "metadata", {}) or {}
    author = metadata.get("author", "Unknown Author")
    title = metadata.get("title", "Untitled")
    journal = metadata.get("journal") or metadata.get("journaltitle", "Unknown Journal")
    year = metadata.get("year") or metadata.get("creationdate", "n.d.")
    volume = metadata.get("volume", "")
    issue = metadata.get("issue", "")
    pages = metadata.get("pages", "")
    doi = metadata.get("doi", "")
    url = metadata.get("url", "")

    vol_issue = f"{volume}({issue})" if volume and issue else volume or issue
    pages_str = f", pp. {pages}" if pages else ""
    doi_str = f" https://doi.org/{doi}" if doi and not doi.startswith("http") else f" {doi}" if doi else ""
    url_str = f" {url}" if url and not doi else ""

    if style == "APA":
        citation = f"{author} ({year}). *{title}*. *{journal}*, {vol_issue}{pages_str}.{doi_str}{url_str}"
    elif style == "IEEE":
        citation = f"{author}, \"{title},\" *{journal}*, vol. {volume}, no. {issue}, pp. {pages}, {year}.{doi_str}{url_str}"
    elif style == "MLA":
        citation = f"{author}. \"{title}.\" *{journal}*, vol. {volume}, no. {issue}, {year}, pp. {pages}.{doi_str}{url_str}"
    elif style == "Chicago":
        citation = f"{author}. \"{title}.\" *{journal}* {volume}, no. {issue} ({year}): {pages}.{doi_str}{url_str}"
    else:
        citation = f"{author} ({year}). {title}. {journal}.{doi_str}{url_str}"

    state["citation_output"] = " ".join(citation.split()).strip()
    return state
