"""
Manual test script for the TechnicalAgent.

Usage:
    python -m agents.technical.run_technical
"""
import json
import os
import sys
import time

from config.llm_config import get_embeddings
from agents.technical.technical_agent import TechnicalAgent


def load_dataset(path: str):
    with open(path, encoding="utf-8") as f:
        return json.load(f)["documents"]


def build_vectorstore(documents, embeddings):
    from langchain_community.vectorstores import Chroma
    persist_dir = os.path.join(os.path.dirname(__file__), "..", "..", "rag", "chroma_db")
    if os.path.exists(persist_dir):
        return Chroma(
            collection_name="omnia_retail",
            embedding_function=embeddings,
            persist_directory=persist_dir,
        )
    raise FileNotFoundError("Chroma DB not found — run the RAG pipeline first")


TEST_QUERIES = [
    # Should use RAG — in knowledge base
    "My laptop keeps shutting down unexpectedly",
    # Should use RAG — storage question in knowledge base
    "What is the difference between NVMe and SATA SSD?",
    # Should trigger web search — specific driver issue
    "AMD amdppm.sys BSOD on Windows 11",
    # Should trigger web search — current compatibility question
    "Is the Lenovo ThinkPad X1 Carbon compatible with Thunderbolt 4 docks?",
]


def run():
    print("=" * 60)
    print("TECHNICAL AGENT — MANUAL TEST")
    print("=" * 60)

    print("\nLoading dataset and vectorstore...")
    embeddings = get_embeddings()
    documents = load_dataset("./rag/dataset/omnia_retail_knowledge_base.json")
    vectorstore = build_vectorstore(documents, embeddings)
    print(f"✓ Loaded {len(documents)} documents\n")

    print("Initialising TechnicalAgent...")
    agent = TechnicalAgent(documents=documents, vectorstore=vectorstore)
    print("✓ Ready\n")

    for query in TEST_QUERIES:
        print(f"Query        : {query}")

        t0 = time.time()
        result = agent.process(query)
        latency = round(time.time() - t0, 3)

        print(f"Safe                : {result['safe']}")
        print(f"Top Score           : {result['top_score']}")
        print(f"Docs                : {result['retrieved_docs']}")
        print(f"Web search          : {result['used_web_search']}")
        print(f"Web search Results  : {result['search_results'][:300]}")
        print(f"Latency             : {latency}s")
        print(f"Response            : {result['response'][:300]}...")
        print("-" * 60)


if __name__ == "__main__":
    run()
