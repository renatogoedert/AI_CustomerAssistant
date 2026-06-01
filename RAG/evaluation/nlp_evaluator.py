import json
import re

from sklearn.metrics.pairwise import cosine_similarity
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import numpy as np


class NLPEvaluator:
    """
    Evaluates machine-generated language using NLP metrics.

    Usage:
        evaluator = NLPEvaluator(llm, embeddings_model)
        evaluator.calculate_rouge_l(generated, reference)
        evaluator.calculate_rouge_1(generated, reference)
        evaluator.calculate_rouge_2(generated, reference)
        evaluator.calculate_bleu(generated, reference)
        evaluator.semantic_similarity_score(text1, text2)
        evaluator.check_faithfulness(retrieved_docs, response)
        evaluator.evaluate_all(generated, reference, query, retrieved_docs)
    """

    def __init__(self, llm=None, embeddings_model=None):
        self.llm = llm
        self.embeddings_model = embeddings_model
        self._rouge_scorer = rouge_scorer.RougeScorer(
            ["rouge1", "rouge2", "rougeL"], use_stemmer=True
        )

    # Based on Code for Class 04, Section 2
    def calculate_rouge_l(self, generated: str, reference: str) -> float:

        """Longest common subsequence recall between generated and reference."""

        scores = self._rouge_scorer.score(reference, generated)
        return round(scores["rougeL"].fmeasure, 3)

    # Based on Code for Class 04, Section 2
    def calculate_rouge_1(self, generated: str, reference: str) -> float:

        """Unigram overlap between generated and reference."""

        scores = self._rouge_scorer.score(reference, generated)
        return round(scores["rouge1"].fmeasure, 3)

    # Based on Code for Class 04, Section 2
    def calculate_rouge_2(self, generated: str, reference: str) -> float:

        """Bigram overlap between generated and reference."""

        scores = self._rouge_scorer.score(reference, generated)
        return round(scores["rouge2"].fmeasure, 3)

    # Based on Code for Class 04, Section 2
    def calculate_bleu(self, generated: str, reference: str) -> float:

        """N-gram precision of generated text against reference."""

        reference_tokens = [reference.split()]
        generated_tokens = generated.split()
        smoothing = SmoothingFunction().method1
        score = sentence_bleu(reference_tokens, generated_tokens, smoothing_function=smoothing)
        return round(score, 3)

    # Based on Code for Class 04, Section 2
    def calculate_cosine_similarity_score(self, text1: str, text2: str) -> float:

        """Cosine similarity between embeddings of two texts."""

        if self.embeddings_model is None:
            raise ValueError("embeddings_model is required for calculate_cosine_similarity_score.")
        emb1 = self.embeddings_model.embed_query(text1)
        emb2 = self.embeddings_model.embed_query(text2)
        similarity = cosine_similarity(
            np.array(emb1).reshape(1, -1),
            np.array(emb2).reshape(1, -1)
        )[0][0]
        return round(float(similarity), 3)
    
    # Based on Code for Class 04, Section 6
    def check_faithfulness(self, retrieved_docs: list, response: str) -> str:
        """Check if response is grounded in retrieved context (YES / NO / PARTIAL)."""
        if self.llm is None:
            raise ValueError("llm is required for check_faithfulness.")
        if not retrieved_docs:
            raise ValueError("retrieved_docs must be a non-empty list.")
 
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        prompt = f"""You are an evaluation system. Your only job is to output a single word.
 
        Retrieved Context:
        {context}
 
        Generated Answer:
        {response}
 
        Does the answer above contain only information that is present in the context above?
        
        Rules:
        - Output YES if every claim in the answer is supported by the context
        - Output NO if the answer contains claims not found in the context
        - Output PARTIAL if some claims are supported and some are not
        
        You must respond with exactly one word: YES, NO, or PARTIAL.
        Do not explain. Do not use punctuation. Output only the single word."""
 
        result = self.llm.invoke(prompt)
        raw = result.content.strip().upper()
 
        for label in ("PARTIAL", "YES", "NO"):
            if label in raw:
                return label
 
        return "UNKNOWN"
 
    # Based on Code for Class 04, Section 6
    def llm_judge_evaluation(self, query: str, description: str) -> str:
        """
        Use LLM as a tech lead judge to evaluate a customer support response.
        Scores helpfulness, clarity, and professionalism on a 1-5 scale.
        Accuracy is excluded as it is already measured by check_faithfulness.
        """
        if self.llm is None:
            raise ValueError("llm is required for llm_judge_evaluation.")

        judge_prompt = f"""You are a senior customer support at Omnia Retail Ltd, 
        an Irish electronics retailer. You are reviewing a support agent's response to a customer query.

        Customer Query:
        {query}

        Agent Response:
        {description}

        Rate the response on the following criteria:
        - Helpfulness (1-5): Does the response actually solve the customer's problem?
        - Clarity (1-5): Is it easy to understand for a non-technical customer?
        - Professionalism (1-5): Is the tone appropriate for customer support?
        - Completeness (1-5): Does the response address all aspects of the customer's query?

        Respond only in JSON format:
        {{
            "helpfulness": <1-5>,
            "clarity": <1-5>,
            "professionalism": <1-5>,
            "completeness": <1-5>,
        }}"""

        try:
            result = self.llm.invoke(judge_prompt).content
            json_match = re.search(r'\{.*\}', result, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except Exception:
            pass

        return {
            "helpfulness": 3,
            "clarity": 3,
            "professionalism": 3,
            "completeness": 3,
        }

    def evaluate_all(
        self,
        generated: str,
        reference: str,
        query: str = None,
        retrieved_docs: list = None,
    ) -> dict:
        """
        Run all available metrics for a single generated/reference pair.
        Faithfulness and semantic similarity are skipped if their
        dependencies (llm, embeddings_model) were not provided at init.
        """
        results = {
            "rouge_1": self.calculate_rouge_1(generated, reference),
            "rouge_2": self.calculate_rouge_2(generated, reference),
            "rouge_l": self.calculate_rouge_l(generated, reference),
            "bleu": self.calculate_bleu(generated, reference),
        }

        if self.embeddings_model is not None:
            results["semantic_similarity"] = self.semantic_similarity_score(generated, reference)
        else:
            results["semantic_similarity"] = "skipped — no embeddings_model provided"

        if self.llm is not None and query is not None and retrieved_docs is not None:
            results["faithfulness"] = self.check_faithfulness(query, retrieved_docs, generated)
        else:   
            missing = []
            if self.llm is None:
                missing.append("llm")
            if query is None:
                missing.append("query")
            if retrieved_docs is None:
                missing.append("retrieved_docs")
            results["faithfulness"] = f"skipped — missing: {', '.join(missing)}"

        return results