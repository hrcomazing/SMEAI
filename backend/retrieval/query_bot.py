"""High-level query handling for the chatbot."""

# The query_bot orchestrates embedding the query, retrieving documents, filtering
# by user permissions, and calling the language model.

from .vector_search import embed_and_search
from .access_control import filter_chunks
from ..llm.mixtral_client import ask_mixtral


def answer_query(query: str, token: str) -> str:
    """Return an answer to ``query`` for the user associated with ``token``."""
    # 1. Embed query and retrieve candidate chunks
    chunks = embed_and_search(query)
    # 2. Filter chunks based on access control
    allowed_chunks = filter_chunks(chunks, token)
    # 3. Assemble context and send to LLM
    return ask_mixtral(query, allowed_chunks)
