# SMEAI Chatbot Skeleton

This repository contains a starter layout for an authenticated retrieval augmented
chatbot powered by a local Mixtral LLM. The code is organised in modular
components under the `backend/` directory.
User-interface code is placed under the new `frontend/` directory.

## Directory Structure

```
backend/
    ingest/            # Build FAISS index from raw documents
    retrieval/         # Query handling and vector search
    llm/               # Mixtral client wrapper
    api/               # FastAPI application
    auth/              # Token to user mapping
    config.py          # Shared configuration values

frontend/             # Web user interface

data/                 # Persisted FAISS index and metadata
Dockerfile            # Container setup
requirements.txt      # Python dependencies
.env                  # Environment variables
```

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Build the document index (placeholder command):
   ```bash
   python backend/ingest/build_index.py
   ```
3. Start the API server:
   ```bash
   uvicorn backend.api.server:app --reload
   ```
4. Send a request:
   ```bash
   curl -X POST "http://localhost:8000/query" -d 'token=abc123token&query=hello'
   ```

## Status

This project provides only pseudocode placeholders for the ingestion pipeline,
vector search, and LLM interaction. It is intended as a starting point for a
full-scale application.
