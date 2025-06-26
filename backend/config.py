"""Configuration settings for the chatbot application."""

from pathlib import Path

# Paths for persisted data
DATA_DIR = Path("data")
FAISS_INDEX_PATH = DATA_DIR / "faiss_index.index"
METADATA_PATH = DATA_DIR / "metadata.json"

# Jira REST API settings
JIRA_BASE_URL = "https://your-domain.atlassian.net"
JIRA_EMAIL = "user@example.com"
JIRA_API_TOKEN = "your_token_here"

# Authentication tokens will be loaded from .env or tokens.py
# Add additional configuration values as needed
