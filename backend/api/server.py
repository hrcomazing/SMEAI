"""FastAPI server exposing chatbot endpoints."""

from fastapi import FastAPI, HTTPException

from ..retrieval.query_bot import answer_query

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/query")
def query_endpoint(token: str, query: str):
    """Return the LLM answer for a user's query."""
    try:
        answer = answer_query(query, token)
    except Exception as exc:  # pragma: no cover - placeholder error handling
        raise HTTPException(status_code=500, detail=str(exc))
    return {"answer": answer}
