from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()

OPENAI_API_KEY: Optional[str] = os.getenv("API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
QDRANT_URL: Optional[str] = os.getenv("QDRANT_URL")
QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION: str = os.getenv("QDRANT_COLLECTION", "research_papers")

if OPENAI_API_KEY is None:
    print("⚠️ WARNING: OPENAI API KEY not set in environment (API calls will fail).")
