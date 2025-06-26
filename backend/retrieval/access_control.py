"""Simple token-based access control for retrieved chunks."""

from ..auth.tokens import TOKEN_TO_USER


def filter_chunks(chunks, token: str):
    """Return only chunks a user is allowed to see."""
    user = TOKEN_TO_USER.get(token)
    if user is None:
        return []
    # Each chunk should contain metadata with allowed users
    return [c for c in chunks if user in c.get("user_ids", [])]
