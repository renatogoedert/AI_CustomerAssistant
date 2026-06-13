import json
import re
import os
import getpass
from pathlib import Path
from datetime import datetime

from langchain_community.vectorstores import Chroma
from rank_bm25 import BM25Okapi
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from config.llm_config import get_embeddings
from agents.triage.triage_agent import TriageAgent
from agents.general.general_info_agent import GeneralAgent
from agents.technical.technical_agent import TechnicalAgent
from agents.action.action_agent import ActionAgent
from agents.returns.returns_agent import ReturnsAgent
from agents.warranty.warranty_agent import WarrantyAgent
from agents.delivery.delivery_agent import DeliveryAgent
from agents.workflow import build_workflow

SHARED_PASSWORD = "123456"
ADMIN_NAME      = "admin"
MEMORY_DIR      = Path("./memory")
MEMORY_DIR.mkdir(exist_ok=True)
LOGS_DIR        = Path("./logs")
LOGS_DIR.mkdir(exist_ok=True)

# Code based on Class 10 section 4 Lab
def load_memory(name: str) -> dict:

    """
    Load memory for a user by name.
    """

    memory_file = MEMORY_DIR / f"{name.lower()}.json"
    if memory_file.exists():
        return json.loads(memory_file.read_text(encoding="utf-8"))
    return {
        "name": name,
        "history": [],
        "current_agent": "",
        "pending_queries": [],
        "awaiting_next_issue": False,
        "created_at": datetime.now().isoformat(),
    }

# Code based on Class 10 section 4 Lab
def save_memory(name: str, memory: dict):

    """
    Save memory for a user by name.
    """

    memory_file = MEMORY_DIR / f"{name.lower()}.json"
    memory_file.write_text(json.dumps(memory, indent=2, ensure_ascii=False), encoding="utf-8")

# Code based on Class 10 section 4 Lab
def update_memory(memory: dict, role: str, content: str):

    """
    Append a message to the memory history.
    """

    memory["history"].append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat(),
    })
    memory["last_seen"] = datetime.now().isoformat()


def _build_state(query: str, name: str, history_str: str, debug: bool, memory: dict) -> dict:

    """
    Build LangGraph state dict.
    """

    return {
        "query":            query,
        "username":         name,
        "history":          history_str,
        "debug":            debug,
        "current_agent":    memory.get("current_agent", ""),
        "category":         "",
        "urgency":          "",
        "route_to":         "",
        "triage_method":    "",
        "needs_handoff":    False,
        "handoff_reason":   "",
        "response":         "",
        "retrieved_docs":   [],
        "mcp_tools_called": [],
        "specialist_action": None,
        "used_web_search":  False,
        "processing_log":   [],
    }


# Login
def login() -> tuple[str, bool]:

    """
    Simple login — name + shared password. Admin enables debug mode.
    """

    print("\n" + "=" * 50)
    print("  Omnia Retail — Customer Support")
    print("=" * 50)

    name = input("\nEnter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return login()

    password = getpass.getpass("Enter password: ").strip()
    if password != SHARED_PASSWORD:
        print("Incorrect password. Please try again.")
        return login()

    is_admin = name.lower() == ADMIN_NAME
    return name, is_admin


# Setup
def setup(username: str, debug: bool = False):

    """
    Load dataset, build vectorstore, initialise agents and workflow.
    """

    debug and print("\n  [System] Loading knowledge base...")

    dataset_path = os.path.join(os.path.dirname(__file__), "rag", "dataset", "omnia_retail_knowledge_base.json")
    with open(dataset_path, encoding="utf-8") as f:
        documents = json.load(f)["documents"]

    embeddings = get_embeddings()
    persist_dir = os.path.join(os.path.dirname(__file__), "rag", "chroma_db")

    if os.path.exists(persist_dir):
        debug and print("  [System] Loading existing vector database...")
        vectorstore = Chroma(
            collection_name="omnia_retail",
            embedding_function=embeddings,
            persist_directory=persist_dir,
        )
    else:
        print("Building vector database...")
        texts = [doc["content"] for doc in documents]
        metadatas = [{
            "document_id": doc["document_id"],
            "type": doc["type"],
            "category": doc["category"],
            "product_category": doc.get("product_category", ""),
            "date": doc.get("date", ""),
            "resolution_status": str(doc.get("resolution_status", "")),
            "customer_satisfaction": str(doc.get("customer_satisfaction", "")),
            "priority": str(doc.get("priority", "")),
        } for doc in documents]
        vectorstore = Chroma.from_texts(
            texts=texts,
            metadatas=metadatas,
            embedding=embeddings,
            collection_name="omnia_retail",
            persist_directory=persist_dir,
        )

    debug and print(f"  [System] Loaded {len(documents)} documents")
    debug and print("  [System] Initialising agents...")

    triage   = TriageAgent()
    general  = GeneralAgent(documents=documents, vectorstore=vectorstore)
    technical = TechnicalAgent(documents=documents, vectorstore=vectorstore)
    action   = ActionAgent(username=username)
    returns  = ReturnsAgent(documents=documents)
    warranty = WarrantyAgent(documents=documents)
    delivery = DeliveryAgent(documents=documents)

    workflow = build_workflow(triage, general, technical, action, returns, warranty, delivery)

    debug and print("  [System] Agents and workflow ready\n")
    return workflow, triage


def _process_query(query: str, name: str, history_str: str, debug: bool,
                   memory: dict, workflow) -> tuple[str, dict]:
    
    """
    Run a single query through the workflow. 
    """

    state = _build_state(query, name, history_str, debug, memory)
    result = workflow.invoke(state)
    return result["response"], result

def log_interaction(name: str, query: str, result: dict, debug: bool = False):

    """
    Append interaction to the session log file.
    """

    log_file = LOGS_DIR / f"{name.lower()}.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}]\n")
        f.write(f"Query:    {query}\n")
        f.write(f"Response: {result.get('response', '')[:200]}\n")
        f.write(f"Agent:    {result.get('current_agent', '')}\n")
        f.write(f"Log:      {result.get('processing_log', [])}\n")
        f.write("\n")

# Based on Code for Class 07, Section 2
def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())
 
 
# Based on temporal/metadata boosting pattern from HybridRetriever (Assignment 1).
def build_history(memory: dict, query: str, max_messages: int = 10) -> str:
    
    """
    Build conversation history string using BM25 relevance + recency boosting.
    """
 
    history = memory.get("history", [])
    if not history:
        return ""
 
    recent = history[-20:]
    if not recent:
        return ""
 
    # BM25 scoring 
    tokenized = [_tokenize(msg["content"]) for msg in recent]
    bm25 = BM25Okapi(tokenized)
    bm25_scores = bm25.get_scores(_tokenize(query))
 
    # Temporal boost
    n = len(recent)
    scored = []
    for i, (msg, bm25_score) in enumerate(zip(recent, bm25_scores)):
        recency = (i + 1) / n
        combined = float(bm25_score) + recency
        scored.append((combined, i, msg))
 
    # Select top messages
    scored.sort(key=lambda x: x[0], reverse=True)
    selected = sorted(scored[:max_messages], key=lambda x: x[1])
 
    return "\n".join(
        f"{'Customer' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
        for _, _, m in selected
    )

# Chat loop
def run_session(name: str, is_admin: bool, workflow, triage: TriageAgent):

    """
    Run the main chat loop for a logged-in user.
    """

    memory = load_memory(name)
    memory["current_agent"] = ""
    memory.setdefault("pending_queries", [])
    memory.setdefault("awaiting_next_issue", False)
    debug = is_admin

    history_str = build_history(memory, "", max_messages=10)

    returning = len(memory["history"]) > 0
    greeting  = f"Welcome back, {name}!" if returning else f"Hello, {name}! How can I help you today?"
    print(f"\n{greeting}")

    is_admin and print("  [Admin mode — debug enabled]")

    print("Type 'quit' to exit, 'clear' to reset memory, 'debug' to toggle debug mode.\n")

    while True:
        # Check for pending sub-queries
        if memory.get("awaiting_next_issue"):
            query = input("You: ").strip()
            if query.lower() in ("yes", "y", "sure", "ok", "okay", "yeah"):
                next_sq = memory["pending_queries"].pop(0)
                memory["awaiting_next_issue"] = False
                memory["current_agent"] = ""
                query = next_sq["query"]
                debug and print(f"  [Decomposer] Starting next issue: {query}")
            else:
                memory["awaiting_next_issue"] = False
                memory["pending_queries"] = []
        else:
            query = input("You: ").strip()

            if not query:
                continue
            if query.lower() == "quit":
                save_memory(name, memory)
                print(f"\nGoodbye, {name}! Your session has been saved.")
                break
            if query.lower() == "clear":
                memory["history"] = []
                memory["current_agent"] = ""
                memory["pending_queries"] = []
                memory["awaiting_next_issue"] = False
                history_str = ""
                save_memory(name, memory)
                print("--- Memory cleared ---\n")
                continue
            if query.lower() == "debug":
                debug = not debug
                print(f"--- Debug mode {'enabled' if debug else 'disabled'} ---\n")
                continue

            # Decompose 
            if not memory.get("current_agent"):
                decomp = triage.decompose(query)
                if decomp.get("complex") and len(decomp.get("sub_queries", [])) > 1:
                    sub_queries = decomp["sub_queries"]
                    if debug:
                        print(f"  [Decomposer] Complex query — {len(sub_queries)} issues detected:")
                        for sq in sub_queries:
                            print(f"    - {sq['query']} (category: {sq['category']})")

                    memory["pending_queries"] = sub_queries[1:]
                    query = sub_queries[0]["query"]
                    memory["current_agent"] = ""

        # Run workflow 
        response, result = _process_query(query, name, history_str, debug, memory, workflow)
        memory["current_agent"] = result.get("current_agent", "")

        if memory["pending_queries"]:
            next_issue = memory["pending_queries"][0]["query"]
            response += f"\n\nI also noticed you mentioned another issue: \"{next_issue}\". Would you like me to help with that now?"
            memory["awaiting_next_issue"] = True

        print(f"\nAssistant: {response}\n")

        debug and print(f"  [Log] {result.get('processing_log', [])}\n")

        log_interaction(name, query, result, debug)

        # Update memory 
        update_memory(memory, "user", query)
        update_memory(memory, "assistant", response)
        history_str = build_history(memory, query, max_messages=10)
        save_memory(name, memory)


# Main
def main():
    name, is_admin = login()
    workflow, triage = setup(username=name, debug=is_admin)
    run_session(name, is_admin, workflow, triage)


if __name__ == "__main__":
    main()
