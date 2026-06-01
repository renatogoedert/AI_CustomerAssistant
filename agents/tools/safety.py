import re
from langchain_core.tools import tool


# Prompt injection patterns
PROMPT_INJECTION_PATTERNS = [
    r"ignore\s+(previous|all|prior)\s+instructions",
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


def _check_patterns(text: str, patterns: list[str]) -> list[str]:
    """Return list of matched pattern descriptions."""
    text_lower = text.lower()
    matched = []
    for pattern in patterns:
        if re.search(pattern, text_lower):
            matched.append(pattern)
    return matched


@tool
def safety_check(query: str) -> str:
    """
    Validates user input for prompt injection, SQL injection, and other
    malicious content before processing by any agent.

    Returns "SAFE: <query>" if input is clean,
    or "UNSAFE: <reason>" if a threat is detected.
    """
    if not query or not query.strip():
        return "UNSAFE: Empty input"

    if len(query) > 2000:
        return "UNSAFE: Input exceeds maximum length of 2000 characters"

    injection_matches = _check_patterns(query, PROMPT_INJECTION_PATTERNS)
    if injection_matches:
        return "UNSAFE: Prompt injection attempt detected"

    sql_matches = _check_patterns(query, SQL_INJECTION_PATTERNS)
    if sql_matches:
        return "UNSAFE: SQL injection attempt detected"

    malicious_matches = _check_patterns(query, MALICIOUS_PATTERNS)
    if malicious_matches:
        return "UNSAFE: Malicious content detected"

    return f"SAFE: {query.strip()}"


def is_safe(query: str) -> tuple[bool, str]:
    """
    Helper function for agents to check input safety directly.
    Returns (is_safe: bool, message: str).
    """
    result = safety_check.invoke(query)
    if result.startswith("SAFE:"):
        return True, result[6:].strip()
    return False, result[8:].strip()