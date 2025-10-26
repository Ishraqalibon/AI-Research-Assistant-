# Advanced AI Research Assistant: Hybrid Retrieval and LangGraph Orchestration

A sophisticated Streamlit application for AI-powered PDF document analysis, Q&A, Summarization, and Comparative Review, built on state-of-the-art RAG techniques.

This project showcases expertise in building robust, multi-step Generative AI applications using Streamlit for a responsive user interface and a powerful LangGraph workflow for reliable backend intelligence. It addresses the critical need for grounded, verifiable answers in academic research by employing a dedicated Hybrid Retrieval Augmented Generation (RAG) pipeline.

## Project Motivation & Technical Challenge

### Problem Statement (Academic Context)

Research often involves synthesizing information from multiple, lengthy PDF documents. Traditional search is inefficient, and standard AI assistants frequently hallucinate or provide answers lacking citations. The user needs a tool that can provide highly accurate, grounded, and citable answers specific to their uploaded document set.

### Technical Challenge (Solution & Expertise)

The core challenge was ensuring the model received the most relevant context possible, even across large, semantically diverse documents. This required moving beyond basic vector search to implement an advanced pipeline:

- **Hybrid Search:** Combining the semantic precision of Dense Retrieval (Qdrant) with the keyword exactness of Sparse Retrieval (BM25) to cover all query types.
- **Cross-Encoder Reranking:** Implementing a powerful Cross-Encoder model after the initial retrieval to re-score and eliminate low-relevance document chunks. This crucial step minimizes noise and significantly boosts the quality and reliability of the final answer.
- **Stateful Workflow:** Orchestrating complex, multi-step tasks (like comparative analysis and summarization) reliably using LangGraph to manage application state and sequence decisions seamlessly.

## Key Features

- **PDF Upload & Vectorization:** Easily upload single or multiple PDF research papers. Documents are automatically chunked and indexed using OpenAI Embeddings and stored in a Qdrant vector database.
- **Hybrid Retrieval (RAG):** Combines Dense Retrieval (Qdrant) and Sparse Retrieval (BM25) for highly relevant context extraction, followed by Cross-Encoder Reranking to ensure the most accurate context is passed to the LLM.
- **Intelligent Q&A:** Ask complex questions about the uploaded document(s) and receive answers strictly grounded in the content, complete with inline citations.
- **Research Tools Suite:**
  - **Summarization (Literature Review Mode):** Generate abstracts, critical analyses, or key bullet points of documents.
  - **Comparative Analysis:** Upload two papers and generate a structured report comparing their methodologies, findings, and contributions.
  - **Citation Generator:** Instantly generate bibliographic citations in popular formats (APA, IEEE, MLA, Chicago).
- **Modular Architecture:** Uses LangGraph for a clear, stateful workflow management across different research tasks, ensuring low latency and high reliability.

## Technology Stack

| Component            | Technology                  | Role                                                                 |
|----------------------|-----------------------------|----------------------------------------------------------------------|
| Frontend             | streamlit                   | User interface and document upload management.                       |
| Workflow Orchestration | langgraph                 | State management and orchestration of complex research flows.        |
| LLM Interface        | langchain_openai, ChatOpenAI | Handles interaction with gpt-4o-mini for reasoning and generation.   |
| Vector Database      | Qdrant                      | Highly scalable vector storage for semantic search and payload filtering. |
| Embeddings           | OpenAIEmbeddings            | Converts text chunks into vector representations.                    |
| Retrieval            | BM25Retriever, EnsembleRetriever, CrossEncoder | Hybrid search and reranking for superior context quality.            |

## Key Learnings & Skill Showcase

This project served as a deep dive into advanced GenAI application development, yielding expertise in:

- **Advanced RAG Pipeline Design:** Successfully implementing and validating the performance gain from a hybrid retrieval approach combined with reranking over basic vector search.
- **Stateful Agentic Workflows (LangGraph):** Mastering how to define state, nodes, and conditional edges to handle complex, branching application logic (Q&A vs. Summarization vs. Comparison).
- **Integration of Disparate Services:** Seamlessly connecting LangChain components with a cloud-based Vector DB (Qdrant) and a high-performance web framework (Streamlit).
- **PDF Processing:** Developing robust document loading and chunking strategies that preserve crucial metadata (like source) for accurate citation generation.

## Getting Started

### Prerequisites

- Python 3.8+
- An OpenAI API Key (required for LLM and Embeddings).
- A Qdrant Host URL and API Key (you can use Qdrant Cloud or a self-hosted instance).

### 1. Environment Setup

Create a file named `.env` in the root directory and populate it with your API keys:
