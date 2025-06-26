"""Configuration settings for the chatbot application."""

from pathlib import Path

# Paths for persisted data
DATA_DIR = Path("data")
FAISS_INDEX_PATH = DATA_DIR / "faiss_index.index"
METADATA_PATH = DATA_DIR / "metadata.json"

# Authentication tokens will be loaded from .env or tokens.py
# Add additional configuration values as needed
