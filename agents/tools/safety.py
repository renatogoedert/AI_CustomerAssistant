import re
from langchain_core.tools import tool


# Prompt injection patterns
PROMPT_INJECTION_PATTERNS = [
    r"ignore.{0,10}(previous|instructions|rules|guidelines|above|told)",
    r"you\s+are\s+now",
    r"act\s+as\s+(a|an)",
    r"forget\s+(everything|all|your)",
    r"new\s+instructions",
    r"system\s*:\s*",
    r"disregard\s+(your|all|previous)",
    r"pretend\s+(you|to)",
    r"jailbreak",
    r"override\s+(your|all|previous)",
]

# SQL injection patterns
SQL_INJECTION_PATTERNS = [
    r"(drop|delete|truncate|alter)\s+table",
    r"union\s+select",
    r";\s*--",
    r"'\s*or\s*'1'\s*=\s*'1",
    r"1\s*=\s*1",
    r"exec\s*\(",
    r"xp_cmdshell",
]

# Other malicious patterns
MALICIOUS_PATTERNS = [
    r"<script.*?>",
    r"javascript\s*:",
    r"on\w+\s*=",
    r"eval\s*\(",
    r"base64_decode",
]


def _normalize(text: str) -> str:

    """
    Normalise text to catch character-spacing bypass attempts.
    e.g. "i g n o r e" - "ignore", "i.g.n.o.r.e" - "ignore"
    Only collapses spaces/separators between single characters.
    """
    
    text = re.sub(r'(?<=[a-z]) (?=[a-z])', '', text)
    text = re.sub(r'(?<=[a-z])[._\-*](?=[a-z])', '', text)
    return text


def _check_patterns(text: str, patterns: list[str]) -> bool:

    """Check both original and normalised text against patterns."""

    text_lower = text.lower()
    text_normalized = _normalize(text.lower())
    for pattern in patterns:
        if re.search(pattern, text_lower) or re.search(pattern, text_normalized):
            return True
    return False

# Based on Code for Lab 9
@tool
def is_safe(query: str) -> dict:

    """
    Validates user input for prompt injection, SQL injection, and malicious content.
    Returns {"safe": bool, "query": str, "reason": str}.
    Agents should check "safe" before using "query".
    """

    if not query or not query.strip():
        return {"safe": False, "query": "", "reason": "Empty input"}

    if len(query) > 2000:
        return {"safe": False, "query": "", "reason": "Input exceeds maximum length of 2000 characters"}

    if _check_patterns(query, PROMPT_INJECTION_PATTERNS):
        return {"safe": False, "query": "", "reason": "Prompt injection attempt detected"}

    if _check_patterns(query, SQL_INJECTION_PATTERNS):
        return {"safe": False, "query": "", "reason": "SQL injection attempt detected"}

    if _check_patterns(query, MALICIOUS_PATTERNS):
        return {"safe": False, "query": "", "reason": "Malicious content detected"}

    return {"safe": True, "query": query.strip(), "reason": ""}