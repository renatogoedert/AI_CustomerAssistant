import json
import os
import getpass
from pathlib import Path
from datetime import datetime

from langchain_community.vectorstores import Chroma
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

# Code based on Class 10 section 4 Lab
def load_memory(name: str) -> dict:
    """Load memory for a user by name."""
    memory_file = MEMORY_DIR / f"{name.lower()}.json"
    if memory_file.exists():
        return json.loads(memory_file.read_text(encoding="utf-8"))
    return {
        "name": name,
        "history": [],
        "current_agent": "",
        "created_at": datetime.now().isoformat(),
    }

# Code based on Class 10 section 4 Lab
def save_memory(name: str, memory: dict):
    """Save memory for a user by name."""
    memory_file = MEMORY_DIR / f"{name.lower()}.json"
    memory_file.write_text(json.dumps(memory, indent=2, ensure_ascii=False), encoding="utf-8")

# Code based on Class 10 section 4 Lab
def update_memory(memory: dict, role: str, content: str):
    """Append a message to the memory history."""
    memory["history"].append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat(),
    })
    memory["last_seen"] = datetime.now().isoformat()


# Login 
def login() -> tuple[str, bool]:

    """Simple login — name + shared password. Admin enables debug mode."""
    
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

    """Load dataset, build vectorstore, initialise agents and workflow."""

    debug and print("\nLoading knowledge base...")

    dataset_path = os.path.join(os.path.dirname(__file__), "rag", "dataset", "omnia_retail_knowledge_base.json")
    with open(dataset_path, encoding="utf-8") as f:
        documents = json.load(f)["documents"]

    embeddings = get_embeddings()
    persist_dir = os.path.join(os.path.dirname(__file__), "rag", "chroma_db")

    if os.path.exists(persist_dir):
        debug and print("Loading existing vector database...")
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

    debug and print(f"✓ Loaded {len(documents)} documents")
    debug and print("Initialising agents...")

    triage      = TriageAgent()
    general     = GeneralAgent(documents=documents, vectorstore=vectorstore)
    technical   = TechnicalAgent(documents=documents, vectorstore=vectorstore)
    action      = ActionAgent(username=username)
    returns     = ReturnsAgent(documents=documents)
    warranty    = WarrantyAgent(documents=documents)
    delivery    = DeliveryAgent(documents=documents)

    workflow = build_workflow(triage, general, technical, action, returns, warranty, delivery)

    debug and print("✓ Agents and workflow ready\n")
    return workflow


# Chat loop

def run_session(name: str, is_admin: bool, workflow):

    """Run the main chat loop for a logged-in user."""

    memory = load_memory(name)
    debug  = is_admin
    memory["current_agent"] = ""

    history_str = "\n".join(
        f"{'Customer' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
        for m in memory["history"][-10:]
    ) if memory["history"] else ""

    returning = len(memory["history"]) > 0
    greeting  = f"Welcome back, {name}!" if returning else f"Hello, {name}! How can I help you today?"
    print(f"\n{greeting}")

    if is_admin:
        print("  [Admin mode — debug enabled]")

    print("Type 'quit' to exit, 'clear' to reset memory, 'debug' to toggle debug mode.\n")

    while True:
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
            history_str = ""
            save_memory(name, memory)
            print("--- Memory cleared ---\n")
            continue
        if query.lower() == "debug":
            debug = not debug
            print(f"--- Debug mode {'enabled' if debug else 'disabled'} ---\n")
            continue

        # LangGraph workflow
        result = workflow.invoke({
            "query":          query,
            "username":       name,
            "history":        history_str,
            "debug":          debug,
            "current_agent":  memory.get("current_agent", ""),
            "category":       "",
            "urgency":        "",
            "route_to":       "",
            "triage_method":  "",
            "needs_handoff":  False,
            "handoff_reason": "",
            "response":       "",
            "retrieved_docs": [],
            "mcp_tools_called": [],
            "specialist_action": None,
            "used_web_search": False,
            "processing_log": [],
        })

        response = result["response"]
        print(f"\nAssistant: {response}\n")

        if debug:
            print(f"  [Log] {result.get('processing_log', [])}\n")

        # Update memory 
        memory["current_agent"] = result.get("current_agent", "")
        update_memory(memory, "user", query)
        update_memory(memory, "assistant", response)
        history_str = "\n".join(
            f"{'Customer' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
            for m in memory["history"][-10:]
        )
        save_memory(name, memory)


# Main

def main():
    name, is_admin = login()
    workflow = setup(username=name, debug=is_admin)
    run_session(name, is_admin, workflow)


if __name__ == "__main__":
    main()