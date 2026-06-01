import json
import os

from config.llm_config import get_embeddings, get_llm
from langchain_community.vectorstores import Chroma
from chunking.chunker import Chunker
from context.context_compressor import ContextCompressor
from evaluation.nlp_evaluator import NLPEvaluator
from retrieval.hybrid_retriever import HybridRetriever
from evaluation.evaluation_runner  import EvaluationRunner
from chat.chat_session import ChatSession


# Based on Code on Exercize for lab 05
def load_dataset(path: str) -> tuple[list[dict], list[dict]]:
    """Load documents and test queries from the Omnia dataset JSON."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["documents"], data["test_queries"]


# Based on Code on Exercize for lab 05
def build_rag_prompt(query: str, retrieved_docs: list, history: str) -> str:
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    return f"""You are a customer support assistant for Omnia Retail Ltd, an Irish electronics retailer.
    Use the documentation below to answer the customer's question accurately.
    If the documentation doesn't contain enough information, say so clearly.
    Do not partake in any conversation that is not related to the store
    
    Documentation:
    {context}
    
    Conversation so far:
    {history}
    
    Customer: {query}
    Assistant:"""


# Based on Code for Class 05, Section 3
def build_vectorstore(documents: list[dict], embeddings, persist_dir="./chroma_db") -> Chroma:
    if os.path.exists(persist_dir):
        print("Loading existing vector database from disk")
        return Chroma(
            collection_name="omnia_retail",
            embedding_function=embeddings,
            persist_directory=persist_dir,
        )

    print("Building vector database...")
    texts = [doc["content"] for doc in documents]
    metadatas = [
        {
            "document_id": doc["document_id"],
            "type": doc["type"],
            "category": doc["category"],
            "product_category": doc.get("product_category", ""),
            "date": doc.get("date", ""),
            "resolution_status": str(doc.get("resolution_status", "")),
            "customer_satisfaction": str(doc.get("customer_satisfaction", "")),
            "priority": str(doc.get("priority", "")),
        }
        for doc in documents
    ]
    return Chroma.from_texts(
        texts=texts,
        metadatas=metadatas,
        embedding=embeddings,
        collection_name="omnia_retail",
    )


# Based on Code on Exercize for lab 05
def main():
    embeddings = get_embeddings()
    llm = get_llm()
    llm_eval = get_llm(temperature=0.1)
    evaluator = NLPEvaluator(llm=llm_eval)

    documents, test_queries = load_dataset("./dataset/omnia_retail_knowledge_base.json")
    print(f"✓ Loaded {len(documents)} documents, {len(test_queries)} test queries")

    vectorstore = build_vectorstore(documents, embeddings)
    print(f"✓ Indexed {len(documents)} documents\n")

    # retriever = HybridRetriever(documents=documents, vectorstore=vectorstore)
    # compressor = ContextCompressor(embeddings=embeddings)

    print("Choose mode:")
    print("  1 - Chat")
    print("  2 - Evaluation")
    mode = input("\nEnter 1 or 2: ").strip()

    if mode == "1":
        ChatSession(llm, documents, vectorstore, embeddings, build_rag_prompt).run()
    elif mode == "2":
        EvaluationRunner(llm, evaluator, documents, vectorstore, embeddings, build_rag_prompt).run(test_queries)
    else:
        print("Invalid choice — starting chat by default.")
        ChatSession(llm, documents, vectorstore, embeddings, build_rag_prompt).run()


if __name__ == "__main__":
    main()