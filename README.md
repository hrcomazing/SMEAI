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

## Environment Setup

1. Create the conda environment:
   ```bash
   conda env create -f environment.yml
   ```
2. Activate it:
   ```bash
   conda activate SMEAI-env
   ```
3. (Optional) Install or update Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

1. Build the document index (placeholder command):
   ```bash
   python backend/ingest/build_index.py
   ```
2. Start the API server:
   ```bash
   uvicorn backend.api.server:app --reload
   ```
3. Send a request:
   ```bash
   curl -X POST "http://localhost:8000/query" -d 'token=abc123token&query=hello'
   ```

## Status

This project provides only pseudocode placeholders for the ingestion pipeline,
vector search, and LLM interaction. It is intended as a starting point for a
full-scale application.
