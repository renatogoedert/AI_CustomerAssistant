from context.context_compressor import ContextCompressor
from retrieval.hybrid_retriever import HybridRetriever


class ChatSession:
    """
    Interactive chat session with conversation memory.
    Handles retrieval, compression, fallback and response generation.
    """

    def __init__(self, llm, documents, vectorstore, embeddings, build_rag_prompt):
        self.llm = llm
        self.build_rag_prompt = build_rag_prompt
        self.history: list[dict] = []
        self.retriever = HybridRetriever(documents=documents, vectorstore=vectorstore)
        self.compressor = ContextCompressor(embeddings=embeddings)

    def run(self):
        """Start the interactive chat loop."""
        print("\n=== Omnia Retail Support Chat ===")
        print("Type your question, 'clear' to reset conversation, or 'quit' to exit.\n")

        while True:
            query = input("You: ").strip()

            if not query:
                continue
            if query.lower() == "quit":
                print("Goodbye!")
                break
            if query.lower() == "clear":
                self.history.clear()
                print("--- Conversation cleared ---\n")
                continue

            # Retrieve
            retrieved = self.retriever.retrieve(query)

            if not retrieved:
                print("\nAssistant: I couldn't find any relevant information for your query. "
                      "Please try rephrasing your question or contact our support team directly at support@omniaretail.ie.")
                continue

            # Compress
            retrieved = self.compressor.compress(query, retrieved)

            history_str = "\n".join(
                f"{'Customer' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
                for m in self.history[-10:]
            )
            prompt = self.build_rag_prompt(query, retrieved, history=history_str)
            response = self.llm.invoke(prompt)

            self.history.append({"role": "user", "content": query})
            self.history.append({"role": "assistant", "content": response.content})

            print(f"\nAssistant: {response.content}")
