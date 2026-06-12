from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.triage.triage_agent import TriageAgent
from agents.general.general_info_agent import GeneralAgent
from agents.technical.technical_agent import TechnicalAgent
from agents.action.action_agent import ActionAgent
from agents.returns.returns_agent import ReturnsAgent
from agents.warranty.warranty_agent import WarrantyAgent
from agents.delivery.delivery_agent import DeliveryAgent


# Based on Code for Class 10 Session 6 lab
###
# State
###

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
    mcp_tools_called: list
    used_web_search: bool
    specialist_action: dict | None

    # Processing log
    processing_log: list

###
# Node functions
###

def triage_node(state: OmniaState, triage_agent: TriageAgent) -> OmniaState:

    """
    Classify and route. Skips if sticky routing applies.
    """

    log = state.get("processing_log", [])
    current_agent = state.get("current_agent", "")
    needs_handoff = state.get("needs_handoff", False)

    # Sticky routing
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

    # Handoff
    handoff_context = f" [Handoff reason: {state.get('handoff_reason')}]" if needs_handoff else ""
    result = triage_agent.process(state["query"] + handoff_context, debug=state.get("debug", False))

    # Extract rewritten
    rewritten_query = result.get("rewritten_query")
    if rewritten_query and state.get("debug"):
        print(f"  [Triage] Query rewritten → {rewritten_query}")

    route  = result.get("route_to", "GeneralAgent")

    # Loop detection
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

    # Logging
    log.append(f"Triage: category={result.get('category')} urgency={result.get('urgency')} "
               f"route={route} method={result.get('method', 'N/A')}"
               + (f" [handoff from {current_agent}]" if needs_handoff else ""))

    # Debugging
    if state.get("debug"):
        print(f"  [Triage] category={result.get('category')} urgency={result.get('urgency')} "
              f"route={route} method={result.get('method', 'N/A')}"
              + (f" [handoff from {current_agent}]" if needs_handoff else ""))

    # State Return
    return {
        "query":         rewritten_query if rewritten_query else state["query"],
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

    """
    Handle general information queries. Signals handoff to triage if needed.
    """

    result = general_agent.process(state["query"], history=state.get("history", ""), debug=state.get("debug", False))
    log = state.get("processing_log", [])

    # Handoff detection
    if result.get("needs_handoff"):
        log.append(f"GeneralAgent: handoff - triage ({result.get('handoff_reason', '')})")
        if state.get("debug"):
            print(f"  [GeneralAgent] Handoff - triage — {result.get('handoff_reason', '')}")
        return {
            "needs_handoff":  True,
            "handoff_reason": result.get("handoff_reason", ""),
            "route_to":       "triage",
            "response":       result["response"],
            "retrieved_docs": [],
            "used_web_search": False,
            "processing_log": log,
        }

    # Logging
    log.append(f"GeneralAgent: docs={result.get('retrieved_docs', [])}")
    if state.get("debug"):
        print(f"  [GeneralAgent] docs={result.get('retrieved_docs', [])}")

    return {
        "needs_handoff":  False,
        "handoff_reason": "",
        "response":       result["response"],
        "retrieved_docs": result.get("retrieved_docs", []),
        "used_web_search": False,
        "processing_log": log,
    }

def technical_node(state: OmniaState, technical_agent: TechnicalAgent) -> OmniaState:

    """
    Handle technical queries. Signals handoff to triage if needed.
    """

    result = technical_agent.process(state["query"], history=state.get("history", ""), debug=state.get("debug", False))
    log = state.get("processing_log", [])

    # Handoff detection
    if result.get("needs_handoff"):
        log.append(f"TechnicalAgent: handoff - triage ({result.get('handoff_reason', '')})")
        if state.get("debug"):
            print(f"  [TechnicalAgent] Handoff - triage — {result.get('handoff_reason', '')}")
        return {
            "needs_handoff":  True,
            "handoff_reason": result.get("handoff_reason", ""),
            "route_to":       "triage",
            "response":       result["response"],
            "retrieved_docs": [],
            "used_web_search": False,
            "processing_log": log,
        }

    # Logging
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
        "used_web_search": result.get("used_web_search", False),
        "processing_log": log,
    }

def action_node(state: OmniaState, action_agent: ActionAgent) -> OmniaState:

    """
    Handle MCP backend operations
    """

    specialist_action = state.get("specialist_action")
    if specialist_action:
        query = f"{state['query']} [Action details: {specialist_action}]"
    else:
        query = state["query"]
    result = action_agent.process(query, username=state["username"], history=state.get("history", ""), debug=state.get("debug", False))

    # Logging
    log = state.get("processing_log", [])
    log.append(f"ActionAgent: mcp_tools={result.get('actions_taken', [])}")
 
    if state.get("debug"):
        print(f"  [ActionAgent] mcp_tools={result.get('actions_taken', [])}")
 
    return {
        "needs_handoff":   False,
        "handoff_reason":  "",
        "response":        result["response"],
        "retrieved_docs":  [],
        "mcp_tools_called": result.get("actions_taken", []),
        "used_web_search": False,
        "processing_log":  log,
    }

def returns_node(state: OmniaState, returns_agent: ReturnsAgent) -> OmniaState:

    """
    Handle return and refund requests.
    """

    result = returns_agent.process(state["query"], username=state["username"], history=state.get("history", ""), debug=state.get("debug", False))
    log = state.get("processing_log", [])

    # Handoff detection
    if result.get("needs_handoff"):
        route = result.get("route_to", "triage")
        log.append(f"ReturnsAgent: handoff - {route} ({result.get('handoff_reason', '')})")
        if state.get("debug"):
            print(f"  [ReturnsAgent] Handoff - {route} — {result.get('handoff_reason', '')}")
        return {
            "needs_handoff":  True,
            "handoff_reason": result.get("handoff_reason", ""),
            "route_to":       route,
            "response":       result["response"],
            "processing_log": log,
        }

    # Logging
    log.append(f"ReturnsAgent: specialist_action={result.get('specialist_action')}")
    if state.get("debug"):
        print(f"  [ReturnsAgent] specialist_action={result.get('specialist_action')}")
 
    return {
        "needs_handoff":  False,
        "handoff_reason": "",
        "response":       result["response"],
        "specialist_action": result.get("specialist_action"),
        "processing_log": log,
    }

def warranty_node(state: OmniaState, warranty_agent: WarrantyAgent) -> OmniaState:

    """
    Handle warranty claims.
    """

    result = warranty_agent.process(state["query"], username=state["username"], history=state.get("history", ""), debug=state.get("debug", False))
    log = state.get("processing_log", [])

    # Handoff detection
    if result.get("needs_handoff"):
        route = result.get("route_to", "triage")
        log.append(f"WarrantyAgent: handoff - {route} ({result.get('handoff_reason', '')})")
        if state.get("debug"):
            print(f"  [WarrantyAgent] Handoff - {route} — {result.get('handoff_reason', '')}")
        return {
            "needs_handoff":  True,
            "handoff_reason": result.get("handoff_reason", ""),
            "route_to":       route,
            "response":       result["response"],
            "processing_log": log,
        }

    #Logging
    log.append(f"WarrantyAgent: specialist_action={result.get('specialist_action')}")
    if state.get("debug"):
        print(f"  [WarrantyAgent] specialist_action={result.get('specialist_action')}")
 
    return {
        "needs_handoff":  False,
        "handoff_reason": "",
        "response":       result["response"],
        "specialist_action": result.get("specialist_action"),
        "processing_log": log,
    }

def delivery_node(state: OmniaState, delivery_agent: DeliveryAgent) -> OmniaState:

    """
    Handle delivery and shipping queries.
    """

    result = delivery_agent.process(state["query"], username=state["username"], history=state.get("history", ""), debug=state.get("debug", False))
    log = state.get("processing_log", [])

    # Handoff detection
    if result.get("needs_handoff"):
        route = result.get("route_to", "triage")
        log.append(f"DeliveryAgent: handoff - {route} ({result.get('handoff_reason', '')})")
        if state.get("debug"):
            print(f"  [DeliveryAgent] Handoff - {route} — {result.get('handoff_reason', '')}")
        return {
            "needs_handoff":  True,
            "handoff_reason": result.get("handoff_reason", ""),
            "route_to":       route,
            "response":       result["response"],
            "processing_log": log,
        }

    # Logging
    log.append(f"DeliveryAgent: specialist_action={result.get('specialist_action')}")
    if state.get("debug"):
        print(f"  [DeliveryAgent] specialist_action={result.get('specialist_action')}")
 
    return {
        "needs_handoff":  False,
        "handoff_reason": "",
        "response":       result["response"],
        "specialist_action": result.get("specialist_action"),
        "processing_log": log,
    }

###
# Routing 
###

ROUTING_MAP = {
    "TechnicalAgent":  "technical",
    "ReturnsAgent":    "returns",
    "WarrantyAgent":   "warranty",
    "DeliveryAgent":   "delivery",
    "EscalationAgent": "escalation",
    "GeneralAgent":    "general",
    "ActionAgent":     "action",
}

def route_after_triage(state: OmniaState) -> str:
    return ROUTING_MAP.get(state.get("route_to", "GeneralAgent"), "general")

def route_after_agent(state: OmniaState) -> str:
    """Route to action, triage or end based on handoff signal."""
    if state.get("needs_handoff"):
        route = state.get("route_to", "")
        if route == "ActionAgent":
            return "action"
        return "triage"
    return "__end__"

###
# Graph 
###

def build_workflow(
    triage_agent: TriageAgent,
    general_agent: GeneralAgent,
    technical_agent: TechnicalAgent,
    action_agent: ActionAgent,
    returns_agent: ReturnsAgent,
    warranty_agent: WarrantyAgent,
    delivery_agent: DeliveryAgent,
):
    
    """
    Build and compile the LangGraph workflow.
    """

    workflow = StateGraph(OmniaState)

    workflow.add_node("triage",    lambda s: triage_node(s, triage_agent))
    workflow.add_node("general",   lambda s: general_node(s, general_agent))
    workflow.add_node("technical", lambda s: technical_node(s, technical_agent))
    workflow.add_node("action",    lambda s: action_node(s, action_agent))
    workflow.add_node("returns",   lambda s: returns_node(s, returns_agent))
    workflow.add_node("warranty",  lambda s: warranty_node(s, warranty_agent))
    workflow.add_node("delivery",  lambda s: delivery_node(s, delivery_agent))
    workflow.add_node("escalation", lambda s: s)

    workflow.set_entry_point("triage")

    # Triage Agent Edges
    workflow.add_conditional_edges(
        "triage",
        route_after_triage,
        {
            "general":    "general",
            "technical":  "technical",
            "returns":    "returns",
            "warranty":   "warranty",
            "delivery":   "delivery",
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

    # Returns Agent Edges
    workflow.add_conditional_edges(
        "returns",
        route_after_agent,
        {
            "triage":  "triage",
            "action":  "action",
            "__end__": END,
        }
    )

    # Warranty Agent Edges
    workflow.add_conditional_edges(
        "warranty",
        route_after_agent,
        {
            "triage":  "triage",
            "action":  "action",
            "__end__": END,
        }
    )

    # Delivery Agent Edges
    workflow.add_conditional_edges(
        "delivery",
        route_after_agent,
        {
            "triage":  "triage",
            "action":  "action",
            "__end__": END,
        }
    )

    # Action Agent Edges
    workflow.add_edge("action", END)

    # Escalation Agent Edges
    workflow.add_edge("escalation", END)
    
    return workflow.compile()
