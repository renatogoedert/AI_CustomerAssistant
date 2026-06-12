import json
import re

from langchain_core.tools import tool
from config.llm_config import get_llm

REWRITE_PROMPT = """
    You are a query rewriting specialist for Omnia Retail Ltd, an Irish electronics retailer.

    Rewrite the given customer query into a clearer, more specific version for document retrieval.

    Rules:
    - Expand abbreviations and slang into full technical terms
    - Add related keywords and synonyms
    - Make implicit intent explicit
    - Keep it concise — one clear sentence
    - Do NOT change the meaning or intent
    - Do NOT answer the query — only rewrite it

    Examples:

    Input: "its not working"
    Output: {"rewritten": "product not working troubleshooting steps repair replacement options"}

    Input: "screen issue"
    Output: {"rewritten": "laptop monitor screen display not working blank flickering troubleshooting"}

    Input: "how long"
    Output: {"rewritten": "delivery shipping timeframe how long does delivery take"}

    Input: "my stuff"
    Output: {"rewritten": "order status delivery tracking customer order information"}

    Return ONLY valid JSON with key "rewritten". No explanation, no extra text.
"""

# Code based on Class 9 Lab
@tool
def rewrite_query(query: str) -> dict:
    
    """
    Rewrite a vague, unclear or short customer query into a clearer retrieval-friendly version.
    Use when the query is too short (under 5 words), ambiguous, or uses slang/abbreviations.
    """

    llm = get_llm(temperature=0)
    prompt = f"{REWRITE_PROMPT}\n\nInput: {query}\nOutput:"
    response = llm.invoke(prompt)

    try:
        json_match = re.search(r'\{.*\}', response.content, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group())
            if parsed.get("rewritten"):
                return parsed
    except Exception:
        pass

    return {"rewritten": query}