import time

from context.context_compressor import ContextCompressor
from retrieval.hybrid_retriever import HybridRetriever

# Based on Code for Class 05
class EvaluationRunner:
    """
    Runs automated evaluation against the dataset test queries.
    Measures retrieval recall, faithfulness, LLM judge scores, and latency.
    """

    def __init__(self, llm, evaluator, documents, vectorstore, embeddings, build_rag_prompt):
        self.llm = llm
        self.evaluator = evaluator
        self.build_rag_prompt = build_rag_prompt
        self.retriever = HybridRetriever(documents=documents, vectorstore=vectorstore, debug=True)
        self.compressor = ContextCompressor(embeddings=embeddings, debug=True)

    def run(self, test_queries: list) -> list:
        """Run evaluation and return results list."""
        results = []

        print("\n=== Running Evaluation ===\n")
        for test in test_queries:
            query = test["query"]
            expected_doc_ids = test["expected_document_ids"]

            # Retrieval
            t0 = time.time()
            retrieved = self.retriever.retrieve(query)
            retrieval_latency = round(time.time() - t0, 3)

            # Compression
            t0 = time.time()
            retrieved = self.compressor.compress(query, retrieved)
            compression_latency = round(time.time() - t0, 3)

            retrieved_doc_ids = [doc.metadata.get("document_id", "") for doc in retrieved]
            matches = sum(1 for doc_id in retrieved_doc_ids if doc_id in expected_doc_ids)
            retrieval_score = round(matches / len(expected_doc_ids), 2)

            # Generation
            prompt = self.build_rag_prompt(query, retrieved, history="")
            t1 = time.time()
            response = self.llm.invoke(prompt)
            generation_latency = round(time.time() - t1, 3)
            total_latency = round(retrieval_latency + compression_latency + generation_latency, 3)

            response_word_count = len(response.content.split())

            # Faithfulness
            faithfulness = self.evaluator.check_faithfulness(
                retrieved_docs=retrieved,
                response=response.content,
            )

            # LLM Judge
            judge_scores = self.evaluator.llm_judge_evaluation(
                query=query,
                description=response.content,
            )

            result = {
                "query_id": test["query_id"],
                "query": query,
                "category": test["category"],
                "expected_doc_ids": expected_doc_ids,
                "retrieved_doc_ids": retrieved_doc_ids,
                "retrieval_score": retrieval_score,
                "response": response.content,
                "response_word_count": response_word_count,
                "faithfulness": faithfulness,
                "judge_scores": judge_scores,
                "retrieval_latency_s": retrieval_latency,
                "compression_latency_s": compression_latency,
                "generation_latency_s": generation_latency,
                "total_latency_s": total_latency,
            }
            results.append(result)

            print(f"[{test['query_id']}] {query}")
            print(f"  Expected    : {expected_doc_ids}")
            print(f"  Retrieved   : {retrieved_doc_ids}")
            print(f"  Retrieval   : {matches}/{len(expected_doc_ids)} ({retrieval_score*100:.0f}%)")
            print(f"  Faithful    : {faithfulness}")
            print(f"  Judge       : {judge_scores}")
            print(f"  Latency     : retrieval={retrieval_latency}s  compression={compression_latency}s  generation={generation_latency}s  total={total_latency}s")
            print(f"  Words       : {response_word_count}")
            print("-" * 70)

        self._print_summary(results)
        return results

    def _print_summary(self, results: list):
        """Print evaluation summary statistics."""
        total = len(results)
        avg_score = round(sum(r["retrieval_score"] for r in results) / total, 2)
        faithfulness_counts = {"YES": 0, "NO": 0, "PARTIAL": 0, "UNKNOWN": 0}
        for r in results:
            key = r["faithfulness"].strip().upper()
            if key in faithfulness_counts:
                faithfulness_counts[key] += 1

        # Average judge scores
        import json
        helpfulness_scores = []
        clarity_scores = []
        professionalism_scores = []
        completeness_scores = []
        for r in results:
            try:
                raw = r["judge_scores"]
                if isinstance(raw, str):
                    raw = raw.strip().strip("```json").strip("```").strip()
                    scores = json.loads(raw)
                else:
                    scores = raw
                helpfulness_scores.append(scores.get("helpfulness", 0))
                clarity_scores.append(scores.get("clarity", 0))
                professionalism_scores.append(scores.get("professionalism", 0))
                completeness_scores.append(scores.get("completeness", 0))
            except Exception:
                pass

        print("\n=== Evaluation Summary ===")
        print(f"Total queries       : {total}")
        print(f"Avg retrieval score : {avg_score * 100:.0f}%")
        print(f"Faithfulness        : {faithfulness_counts}")
        if helpfulness_scores:
            print(f"Avg helpfulness     : {round(sum(helpfulness_scores) / len(helpfulness_scores), 2)}/5")
            print(f"Avg clarity         : {round(sum(clarity_scores) / len(clarity_scores), 2)}/5")
            print(f"Avg professionalism : {round(sum(professionalism_scores) / len(professionalism_scores), 2)}/5")
            print(f"Avg completeness    : {round(sum(completeness_scores) / len(completeness_scores), 2)}/5")
        print(f"Avg retrieval time  : {round(sum(r['retrieval_latency_s'] for r in results) / total, 3)}s")
        print(f"Avg compression time: {round(sum(r['compression_latency_s'] for r in results) / total, 3)}s")
        print(f"Avg generation time : {round(sum(r['generation_latency_s'] for r in results) / total, 3)}s")
        print(f"Avg total latency   : {round(sum(r['total_latency_s'] for r in results) / total, 3)}s")
        print(f"Avg response words  : {round(sum(r['response_word_count'] for r in results) / total)}")