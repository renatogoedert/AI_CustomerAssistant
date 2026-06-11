from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun

from agents.tools.safety import is_safe
from agents.tools.handoff import handoff, check_for_handoff
from config.llm_config import get_llm, get_embeddings
from rag.retrieval.hybrid_retriever import HybridRetriever
from rag.context.context_compressor import ContextCompressor


SYSTEM_PROMPT = """
    You are a technical support specialist at Omnia Retail Ltd, an Irish electronics retailer.

    Your role is to help customers resolve technical issues with their products including:
    - Troubleshooting laptops, monitors, storage devices and accessories
    - Compatibility questions
    - Driver and software issues
    - Setup and installation guidance
    - Performance problems

    How to handle queries:
    1. First check the internal knowledge base for relevant documentation
    2. If the knowledge base doesn't have enough information, use web search for current technical information
    3. Always provide clear step-by-step guidance
    4. If the issue requires a repair or replacement, explain the process but make clear actions are handled by our support team
    
    Important boundaries:
    - You provide technical information and guidance only
    - If the customer asks to process a refund, check order status or perform any non-technical action,
    use the handoff tool with the reason
    - If the customer is very upset or requests escalation, use the handoff tool
    - If the issue cannot be resolved remotely, advise the customer to contact support@omniaretail.ie
    
    Examples:
    
    Customer: "My laptop keeps shutting down"
    Action: Check knowledge base, provide troubleshooting steps. No handoff needed.
    
    Customer: "Can you process a refund for my broken laptop?"
    Action: handoff(reason="Customer wants to process a refund — non-technical action required")
    
    Customer: "My AMD driver is causing BSODs on Windows 11"
    Action: Use web search for current AMD driver issues and fixes.
"""


def _build_technical_prompt(query: str, rag_context: str, search_results: str, history: str = "") -> str:

    return f"""
        You are a technical support specialist at Omnia Retail Ltd.
        Use the information below to help the customer resolve their technical issue.
        Provide clear, step-by-step guidance where appropriate.

        Internal Documentation:
        {rag_context if rag_context else "No relevant internal documentation found."}

        Web Search Results:
        {search_results if search_results else "No web search performed."}

        Conversation so far:
        {history}

        Customer: {query}
        Assistant:
    """


class TechnicalAgent:

    """
    Technical support agent for product troubleshooting and technical queries.
    Uses RAG for internal documentation and DuckDuckGo for current technical information.
    """

    def __init__(self, documents: list[dict], vectorstore):
        self.llm = get_llm(temperature=0.2)
        self.retriever = HybridRetriever(documents=documents, vectorstore=vectorstore)
        self.compressor = ContextCompressor(embeddings=get_embeddings())
        self.search = DuckDuckGoSearchRun()
        self.tools = [is_safe, self.search]

        self.executor = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=SYSTEM_PROMPT,
        )

    def _search_web(self, query: str) -> str:

        """Run a web search and return results."""

        try:
            return self.search.invoke(query)
        except Exception as e:
            return f"Web search unavailable: {str(e)}"

    def process(self, query: str, history: str = "") -> dict:

        """
        Process a technical support query.
        Uses RAG first, falls back to web search if needed.
        Returns {"response": str, "retrieved_docs": list, "used_web_search": bool, "safe": bool}.
        """

        # Safety check
        safety_result = is_safe.invoke(query)
        if not safety_result["safe"]:
            return {
                "safe": False,
                "response": f"I cannot process this request: {safety_result['reason']}",
                "retrieved_docs": [],
                "used_web_search": False,
            }

        # Run agent — checks if handoff is needed
        exec_result = self.executor.invoke({
            "messages": [("human", query)]
        })
 
        # Check for handoff
        handoff_result = check_for_handoff(exec_result)
        if handoff_result:
            return {**handoff_result, "safe": True}
        
        # RAG
        retrieved = self.retriever.retrieve(query)
        compressed = self.compressor.compress(query, retrieved) if retrieved else []
        rag_context = "\n\n".join([doc.page_content for doc in compressed]) if compressed else ""

        # Web Search
        used_web_search = False
        search_results = ""
        top_score = 0.0

        if not retrieved or not rag_context:
            print(f"  [TechnicalAgent] RAG empty — using web search")
            search_results = self._search_web(query)
            used_web_search = True
        else:
            top_score = float(retrieved[0].metadata.get("retrieval_score", 0))
            if top_score < 1.8:
                print(f"  [TechnicalAgent] Low RAG confidence ({top_score}) — supplementing with web search")
                search_results = self._search_web(query)
                used_web_search = True

        # Generate response
        prompt = _build_technical_prompt(query, rag_context, search_results, history)
        response = self.llm.invoke(prompt)

        return {
            "safe": True,
            "response": response.content,
            "top_score": top_score,
            "search_results": search_results,
            "retrieved_docs": [doc.metadata.get("document_id") for doc in retrieved],
            "used_web_search": used_web_search,
        }