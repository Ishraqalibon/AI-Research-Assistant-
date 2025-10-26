import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document

def load_and_split_pdf(file_path: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[Document]:
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    file_name = os.path.basename(file_path)

    for doc in documents:
        doc.metadata = doc.metadata or {}
        doc.metadata["source"] = file_name

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(documents)

    for c in chunks:
        c.metadata = c.metadata or {}
        c.metadata["source"] = file_name

    return chunks
