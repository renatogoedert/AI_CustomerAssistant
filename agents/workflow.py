from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.triage.triage_agent import TriageAgent
from agents.general.general_info_agent import GeneralAgent
from agents.technical.technical_agent import TechnicalAgent
from agents.action.action_agent import ActionAgent


# Based on Code for Class 10 Session 6 lab

class OmniaState(TypedDict):
    query: str
    username: str
    history: str
    debug: bool

    # Sticky routing
    current_agent: str

    # Triage output
    category: str
    urgency: str
    route_to: str
    triage_method: str

    # Handoff signal from agents
    needs_handoff: bool
    handoff_reason: str

    # Response
    response: str
    retrieved_docs: list
    actions_taken: list
    used_web_search: bool

    # Processing log
    processing_log: list



# Node functions

def triage_node(state: OmniaState, triage_agent: TriageAgent) -> OmniaState:
    """
    Classify and route. Skips if sticky routing applies.
    Always runs when a handoff is signalled from another agent.
    """
    log = state.get("processing_log", [])
    current_agent = state.get("current_agent", "")
    needs_handoff = state.get("needs_handoff", False)

    # Sticky routing — skip triage if same topic and no handoff
    if current_agent  and not needs_handoff:
        log.append(f"Triage: skipped — staying with {current_agent}")
        if state.get("debug"):
            print(f"  [Triage] Skipped — staying with {current_agent}")
        return {
            "route_to": current_agent,
            "triage_method": "sticky",
            "needs_handoff": False,
            "processing_log": log,
        }

    # Re-triage — either first message, topic change, or handoff
    handoff_context = f" [Handoff reason: {state.get('handoff_reason')}]" if needs_handoff else ""
    result = triage_agent.process(state["query"] + handoff_context)
    route  = result.get("route_to", "GeneralAgent")

    # Loop detection — if triage routes back to same agent after handoff
    if needs_handoff and route == current_agent:
        if state.get("debug"):
            print(f"  [Triage] Loop detected — escalating to human support")
        return {
            "route_to":      "EscalationAgent",
            "current_agent": "EscalationAgent",
            "category":      "escalation",
            "urgency":       "high",
            "needs_handoff": False,
            "handoff_reason": "",
            "response":      "I'm having trouble processing your request. Please contact our support team directly at support@omniaretail.ie or call 01-XXX-XXXX for immediate assistance.",
            "processing_log": log,
        }

    log.append(f"Triage: category={result.get('category')} urgency={result.get('urgency')} "
               f"route={route} method={result.get('method', 'N/A')}"
               + (f" [handoff from {current_agent}]" if needs_handoff else ""))

    if state.get("debug"):
        print(f"  [Triage] category={result.get('category')} urgency={result.get('urgency')} "
              f"route={route} method={result.get('method', 'N/A')}"
              + (f" [handoff from {current_agent}]" if needs_handoff else ""))

    return {
        "category":      result.get("category", "general"),
        "urgency":       result.get("urgency", "low"),
        "route_to":      route,
        "triage_method": result.get("method", "unknown"),
        "current_agent": route,
        "needs_handoff": False,
        "handoff_reason": "",
        "processing_log": log,
    }


def general_node(state: OmniaState, general_agent: GeneralAgent) -> OmniaState:
    """Handle general information queries. Signals handoff to triage if needed."""
    result = general_agent.process(state["query"], history=state.get("history", ""))
    log = state.get("processing_log", [])

    if result.get("needs_handoff"):
        log.append(f"GeneralAgent: handoff → triage ({result.get('handoff_reason', '')})")
        if state.get("debug"):
            print(f"  [GeneralAgent] Handoff → triage — {result.get('handoff_reason', '')}")
        return {
            "needs_handoff":  True,
            "handoff_reason": result.get("handoff_reason", ""),
            "response":       result["response"],
            "retrieved_docs": [],
            "actions_taken":  [],
            "used_web_search": False,
            "processing_log": log,
        }

    log.append(f"GeneralAgent: docs={result.get('retrieved_docs', [])}")
    if state.get("debug"):
        print(f"  [GeneralAgent] docs={result.get('retrieved_docs', [])}")

    return {
        "needs_handoff":  False,
        "handoff_reason": "",
        "response":       result["response"],
        "retrieved_docs": result.get("retrieved_docs", []),
        "actions_taken":  [],
        "used_web_search": False,
        "processing_log": log,
    }


def technical_node(state: OmniaState, technical_agent: TechnicalAgent) -> OmniaState:
    """Handle technical queries. Signals handoff to triage if needed."""
    result = technical_agent.process(state["query"], history=state.get("history", ""))
    log = state.get("processing_log", [])

    if result.get("needs_handoff"):
        log.append(f"TechnicalAgent: handoff → triage ({result.get('handoff_reason', '')})")
        if state.get("debug"):
            print(f"  [TechnicalAgent] Handoff → triage — {result.get('handoff_reason', '')}")
        return {
            "needs_handoff":  True,
            "handoff_reason": result.get("handoff_reason", ""),
            "response":       result["response"],
            "retrieved_docs": [],
            "actions_taken":  [],
            "used_web_search": False,
            "processing_log": log,
        }

    log.append(f"TechnicalAgent: docs={result.get('retrieved_docs', [])} "
               f"web_search={result.get('used_web_search', False)}")
    if state.get("debug"):
        print(f"  [TechnicalAgent] docs={result.get('retrieved_docs', [])} "
              f"web_search={result.get('used_web_search', False)}")

    return {
        "needs_handoff":  False,
        "handoff_reason": "",
        "response":       result["response"],
        "retrieved_docs": result.get("retrieved_docs", []),
        "actions_taken":  [],
        "used_web_search": result.get("used_web_search", False),
        "processing_log": log,
    }


def action_node(state: OmniaState, action_agent: ActionAgent) -> OmniaState:
    """Handle action requests — orders, refunds, inventory."""
    result = action_agent.process(state["query"], history=state.get("history", ""))
    log = state.get("processing_log", [])
    log.append(f"ActionAgent: actions={result.get('actions_taken', [])}")

    if state.get("debug"):
        print(f"  [ActionAgent] actions={result.get('actions_taken', [])}")

    return {
        "needs_handoff":  False,
        "handoff_reason": "",
        "response":       result["response"],
        "retrieved_docs": [],
        "actions_taken":  result.get("actions_taken", []),
        "used_web_search": False,
        "processing_log": log,
    }


# ── Routing functions ─────────────────────────────────────────

ROUTING_MAP = {
    "TechnicalAgent":  "technical",
    "ActionAgent":     "action",
    "EscalationAgent": "escalation",
    "GeneralAgent":    "general",
}


def route_after_triage(state: OmniaState) -> str:
    return ROUTING_MAP.get(state.get("route_to", "GeneralAgent"), "general")


def route_after_agent(state: OmniaState) -> str:
    """After general or technical — go back to triage if handoff needed, else end."""
    return "triage" if state.get("needs_handoff") else "__end__"


# ── Graph builder ─────────────────────────────────────────────

def build_workflow(
    triage_agent: TriageAgent,
    general_agent: GeneralAgent,
    technical_agent: TechnicalAgent,
    action_agent: ActionAgent,
):
    """Build and compile the LangGraph workflow."""

    workflow = StateGraph(OmniaState)

    workflow.add_node("triage",    lambda s: triage_node(s, triage_agent))
    workflow.add_node("general",   lambda s: general_node(s, general_agent))
    workflow.add_node("technical", lambda s: technical_node(s, technical_agent))
    workflow.add_node("action",    lambda s: action_node(s, action_agent))
    workflow.add_node("escalation", lambda s: s)

    workflow.set_entry_point("triage")

    # Triage Agent Edges
    workflow.add_conditional_edges(
        "triage",
        route_after_triage,
        {
            "general":   "general",
            "technical": "technical",
            "action":    "action",
            "escalation": "escalation",
        }
    )

    # General Agent Edges
    workflow.add_conditional_edges(
        "general",
        route_after_agent,
        {
            "triage":  "triage",
            "__end__": END,
        }
    )

    # Technical Agent Edges
    workflow.add_conditional_edges(
        "technical",
        route_after_agent,
        {
            "triage":  "triage",
            "__end__": END,
        }
    )

    # Action Agent Edges
    workflow.add_conditional_edges(
        "action",
        route_after_agent,
        {
            "triage":  "triage",
            "__end__": END,
        }
    )

    # Escalation Agent Edges
    workflow.add_edge("escalation", END)
    
    return workflow.compile()
