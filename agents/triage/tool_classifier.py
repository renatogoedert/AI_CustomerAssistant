import json
import re
from langchain_core.tools import tool
from config.llm_config import get_llm

CATEGORY_KEYWORDS = {
    "technical":  ["not working", "shutting down", "slow", "error", "troubleshoot",
                   "install", "setup", "driver", "connect", "crash", "blue screen",
                   "flickering", "overheating", "fan", "boot"],
    "warranty":   ["warranty", "defect", "fault", "dead on arrival", "broken",
                   "repair", "replace", "manufacturing", "stopped working"],
    "returns":    ["return", "refund", "send back", "exchange", "changed my mind",
                   "cooling off", "money back"],
    "delivery":   ["delivery", "shipping", "dispatch", "not arrived", "tracking",
                   "lost", "damaged in transit", "wrong item"],
    "bulk":       ["bulk", "business", "procurement", "volume", "company", "office",
                   "fleet", "multiple units"],
    "escalation": ["escalate", "manager", "complaint", "legal", "trading standards",
                   "solicitor", "unacceptable"],
}

URGENCY_KEYWORDS = {
    "high":   ["urgent", "asap", "immediately", "emergency", "business trip",
               "deadline", "won't turn on", "lost data", "critical"],
    "medium": ["warranty", "defect", "return", "refund", "not arrived", "damaged"],
}

# Code based on Class 9 Lab
def _keyword_classify(query: str) -> dict | None:
    """
    Fast keyword-based classification.
    Returns a result dict if confident, None if inconclusive.
    """
    query_lower = query.lower()

    # Category
    matched_category = None
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in query_lower for kw in keywords):
            matched_category = category
            break

    if not matched_category:
        return None 

    # Urgency
    if any(kw in query_lower for kw in URGENCY_KEYWORDS["high"]):
        urgency = "high"
    elif any(kw in query_lower for kw in URGENCY_KEYWORDS["medium"]):
        urgency = "medium"
    else:
        urgency = "low"

    return {
        "category": matched_category,
        "urgency": urgency,
        "reason": f"Keyword match — classified as {matched_category} with {urgency} urgency",
        "method": "keyword",
    }

# Code based on Class 9 Lab
def _llm_classify(query: str) -> dict:
    """
    LLM-based classification for ambiguous queries.
    Used as fallback when keyword matching is inconclusive.
    """
    llm = get_llm(temperature=0)

    prompt = f"""
        You are a customer support triage system for Omnia Retail Ltd, an Irish electronics retailer.
        Classify this query into exactly one category and urgency level.

        Categories:
        - technical: troubleshooting, setup, compatibility, product not working
        - warranty: defects, faults, repairs, dead on arrival
        - returns: refunds, exchanges, change of mind, cooling off period
        - delivery: shipping, tracking, not arrived, damaged in transit
        - bulk: business orders, volume pricing, procurement
        - escalation: complaints, manager requests, legal threats
        - general: policies, payments, account, product info

        Urgency:
        - high: blocking work, urgent need, business critical
        - medium: important but not blocking
        - low: general enquiry

        Query: {query}

        Respond only in JSON with no explanation:
        {{"category": "<category>", "urgency": "<urgency>", "reason": "<one sentence>"}}
    """

    try:
        result = llm.invoke(prompt).content
        json_match = re.search(r'\{.*\}', result, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group())
            parsed["method"] = "llm"
            return parsed
    except Exception:
        pass

    return {
        "category": "general",
        "urgency": "low",
        "reason": "Classification failed — defaulting to general",
        "method": "fallback",
    }

# Code based on Class 9-10 Lab
@tool
def classify_query(query: str) -> dict:

    """
    Classify a customer support query into a category and urgency level.
    Uses fast keyword matching first, falls back to LLM for ambiguous queries.
    Returns {"category": str, "urgency": str, "reason": str, "method": str}.
    """

    result = _keyword_classify(query)
    if result:
        return result
    return _llm_classify(query)