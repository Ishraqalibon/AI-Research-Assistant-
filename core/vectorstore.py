import logging
from typing import List, Optional
from core.config import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.http.models import PayloadSchemaType
from langchain.schema import Document

logger = logging.getLogger(__name__)

def ensure_source_index(collection_name: str = QDRANT_COLLECTION) -> None:
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    try:
        collection_info = client.get_collection(collection_name=collection_name)
        indexed_fields = [index.field_name for index in (collection_info.payload_schema or {}).get("indexes", [])]
        if "source" not in indexed_fields:
            logger.info("Creating 'source' payload index on Qdrant collection.")
            client.create_payload_index(
                collection_name=collection_name,
                field_name="source",
                field_schema=PayloadSchemaType.KEYWORD,
                wait=True
            )
            logger.info("'source' index created.")
        else:
            logger.info("'source' index already exists.")
    except Exception as e:
        logger.warning(f"Could not ensure source index: {e}")

def build_vectorstore(docs: List[Document], collection_name: str = QDRANT_COLLECTION) -> Qdrant:
    embeddings = OpenAIEmbeddings()
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    try:
        existing = [c.name for c in client.get_collections().collections]
        if collection_name not in existing:
            client.create_collection(
                collection_name=collection_name,
                vectors_config={"size": 1536, "distance": "Cosine"}
            )
            logger.info(f"Created Qdrant collection: {collection_name}")
    except Exception as e:
        logger.warning(f"Collection creation check failed: {e}")

    ensure_source_index(collection_name)

    try:
        db = Qdrant.from_documents(
            documents=docs,
            embedding=embeddings,
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            collection_name=collection_name
        )
        logger.info("Built/updated Qdrant vector store from documents.")
        return db
    except Exception as e:
        logger.error(f"Failed to build vectorstore: {e}")
        raise

def load_vectorstore(collection_name: str = QDRANT_COLLECTION) -> Optional[Qdrant]:
    embeddings = OpenAIEmbeddings()
    try:
        ensure_source_index(collection_name)
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        return Qdrant(client=client, collection_name=collection_name, embeddings=embeddings)
    except Exception as e:
        logger.warning(f"Could not load vectorstore: {e}")
        return None
