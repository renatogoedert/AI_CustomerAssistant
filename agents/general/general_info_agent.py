from langchain.agents import create_agent
from langchain_core.tools import tool

from agents.tools.safety import is_safe
from agents.tools.handoff import handoff, check_for_handoff
from config.llm_config import get_llm, get_embeddings
from rag.retrieval.hybrid_retriever import HybridRetriever
from rag.context.context_compressor import ContextCompressor


SYSTEM_PROMPT = """
    You are a customer support information specialist at Omnia Retail Ltd, an Irish electronics retailer.
    
    Your role is to provide accurate information to help customers understand their options regarding:
    - Returns and refunds
    - Delivery and shipping
    - Warranties and statutory rights
    - Order queries
    - Business and bulk orders
    - General policies and procedures
    
    Important boundaries:
    - You provide information only — you do not process returns, warranties, or orders directly
    - If the customer asks to process a refund, check order status, cancel an order or any backend action → use the handoff tool
    - If the customer has a technical issue (laptop not turning on, screen flickering, driver issues) → use the handoff tool
    - If the customer is very upset or requests to speak to a manager → use the handoff tool
    - Answer based only on the provided documentation
    - If the documentation does not contain enough information, say so clearly and suggest contacting support@omniaretail.ie
    
    Examples:
    
    Customer: "What is your return policy?"
    Response: Explain the return policy from documentation. No handoff needed.
    
    Customer: "Can you process my refund for order ORD-2024-3012?"
    Action: handoff(reason="Customer wants to process a refund — action required")
    
    Customer: "My laptop is not turning on"
    Action: handoff(reason="Customer has a technical issue — laptop not turning on")
    
    Customer: "I want to check my order status"
    Action: handoff(reason="Customer wants to check order status — action required")
"""


def _build_rag_prompt(query: str, context: str, history: str = "") -> str:
    return f"""
        You are a customer support information specialist at Omnia Retail Ltd.
        Use the documentation below to answer the customer's question accurately.
        If the documentation doesn't contain enough information, say so clearly.

        Documentation:
        {context}

        Conversation so far:
        {history}

        Customer: {query}
        Assistant:
    """


class GeneralAgent:

    """
    Information agent for general customer support queries.
    """

    def __init__(self, documents: list[dict], vectorstore):
        self.llm = get_llm(provider='openai', model_name='gpt-4.1-mini', temperature=0.3)
        self.retriever = HybridRetriever(documents=documents, vectorstore=vectorstore)
        self.compressor = ContextCompressor(embeddings=get_embeddings())
        self.tools = [is_safe, handoff]

        self.executor = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=SYSTEM_PROMPT,
        )

    def process(self, query: str, history: str = "") -> dict:

        """
        Process a general support query using the RAG pipeline.
        Returns {"response", "retrieved_docs", "safe", "needs_handoff", "handoff_reason"}.
        """

        # Safety check
        safety_result = is_safe.invoke(query)
        if not safety_result["safe"]:
            return {
                "safe": False,
                "response": f"I cannot process this request: {safety_result['reason']}",
                "retrieved_docs": [],
                "needs_handoff": False,
                "handoff_reason": "",
            }

        # Run agent — checks if handoff is needed
        exec_result = self.executor.invoke({
            "messages": [("human", query)]
        })
 
        # Check for handoff
        handoff_result = check_for_handoff(exec_result)
        if handoff_result:
            return {**handoff_result, "safe": True}
        
        # Retrieve relevant documents
        retrieved = self.retriever.retrieve(query)

        if not retrieved:
            return {
                "safe": True,
                "response": (
                    "I couldn't find relevant information for your query in our documentation. "
                    "Please contact our support team directly at support@omniaretail.ie "
                    "or call 01-XXX-XXXX."
                ),
                "retrieved_docs": [],
            }

        # Compress context
        compressed = self.compressor.compress(query, retrieved)

        # Generate response
        context = "\n\n".join([doc.page_content for doc in compressed])
        prompt = _build_rag_prompt(query, context, history)

        response = self.llm.invoke(prompt)

        return {
            "safe": True,
            "response": response.content,
            "retrieved_docs": [doc.metadata.get("document_id") for doc in retrieved],
        }