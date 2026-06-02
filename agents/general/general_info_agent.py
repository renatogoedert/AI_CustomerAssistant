from langchain.agents import create_agent
from langchain_core.tools import tool

from agents.tools.safety import is_safe
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
    - If asked to perform an action (e.g. process a return, raise a warranty claim), explain what 
    the customer needs to do and what information is required, but make clear that actions are 
    handled by our support team
    - Answer based only on the provided documentation
    - If the documentation does not contain enough information, say so clearly and suggest the 
    customer contacts support directly at support@omniaretail.ie
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
    Handles returns, delivery, warranties, orders, and policies.
    Uses the RAG pipeline for retrieval and context compression.
    Does not perform actions — provides information only.
    """

    def __init__(self, documents: list[dict], vectorstore):
        self.llm = get_llm(temperature=0.3)
        self.retriever = HybridRetriever(documents=documents, vectorstore=vectorstore)
        self.compressor = ContextCompressor(embeddings=get_embeddings())
        self.tools = [is_safe]

        self.executor = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=SYSTEM_PROMPT,
        )

    def process(self, query: str, history: str = "") -> dict:
        """
        Process a general support query using the RAG pipeline.
        Returns {"response": str, "retrieved_docs": list, "safe": bool}.
        """
        # Safety check
        safety_result = is_safe.invoke(query)
        if not safety_result["safe"]:
            return {
                "safe": False,
                "response": f"I cannot process this request: {safety_result['reason']}",
                "retrieved_docs": [],
            }

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

        # Build context and generate response
        context = "\n\n".join([doc.page_content for doc in compressed])
        prompt = _build_rag_prompt(query, context, history)

        response = self.llm.invoke(prompt)

        return {
            "safe": True,
            "response": response.content,
            "retrieved_docs": [doc.metadata.get("document_id") for doc in retrieved],
        }