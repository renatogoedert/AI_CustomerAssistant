import re

from rank_bm25 import BM25Okapi
from langchain_core.documents import Document
 
 
class HybridRetriever:
    """
    Hybrid retriever using semantic search + BM25 candidates with multi-signal re-ranking.
 
    Usage:
        retriever = HybridRetriever(documents, vectorstore)
        retriever = HybridRetriever(documents, vectorstore, use_filtering=True)
        docs = retriever.retrieve("my laptop keeps shutting down")
    """
 
    CATEGORY_RULES = {
        "returns": {
            "keywords": ["return", "refund", "send back", "exchange", "changed my mind"],
            "categories": ["returns", "return_request", "shipping_info"],
        },
        "warranty": {
            "keywords": ["warranty", "defect", "fault", "dead on arrival"],
            "categories": ["warranty", "warranty_questions", "warranty_claim", "warranty_claims", "defects"],
        },
        "delivery": {
            "keywords": ["delivery", "shipping", "dispatch", "not arrived", "tracking"],
            "categories": ["shipping", "shipping_info", "delivery_issue", "delivery_issues", "damaged_delivery"],
        },
        "technical": {
            "keywords": ["not working", "troubleshoot", "fix", "shutting down", "error", "slow"],
            "categories": ["technical_troubleshooting", "technical_support"],
        },
        "bulk": {
            "keywords": ["bulk", "business pricing", "procurement", "volume"],
            "categories": ["business_customers", "bulk_orders", "bulk_order_inquiry"],
        },
        "environmental": {
            "keywords": ["weee", "recycle", "recycling", "environmental"],
            "categories": ["environmental_sustainability"],
        },
        "products": {
            "keywords": ["recommend", "which should i", "do i need for", "best for", "difference between", "compare"],
            "categories": ["product_questions", "products", "pre_sales", "product_comparison", "installation_help"],
        },
    }
 
    PRODUCT_RULES = {
        "laptops":     ["laptop", "macbook", "thinkpad", "xps", "notebook", "mac", "m1", "m2", "m3"],
        "monitors":    ["monitor", "screen", "display", "ultrawide", "4k", "oled", "ips"],
        "storage":     ["ssd", "hdd", "hard drive", "nvme", "sata", "storage", "m.2"],
        "accessories": ["mouse", "keyboard", "headset", "webcam", "dock", "hub", "router"],
    }
 
    def __init__(self, documents: list[dict], vectorstore, debug: bool = False, use_filtering: bool = True):
        self.vectorstore = vectorstore
        self.documents = documents
        self.debug = debug
        self.use_filtering = use_filtering
        self.doc_lookup = {doc["document_id"]: doc for doc in documents}
 
        tokenized = [self._tokenize(doc["content"]) for doc in documents]
        self.bm25 = BM25Okapi(tokenized)
        self.doc_ids = [doc["document_id"] for doc in documents]
    
    # Based on Code for Class 07, Section 2 
    def _tokenize(self, text: str) -> list[str]:
        return re.findall(r"[a-z0-9]+", text.lower())
 
    def _detect_category(self, query: str) -> list[str] | None:
        """Detect matching category values from query keywords."""
        query_lower = query.lower()
        for topic, rule in self.CATEGORY_RULES.items():
            if any(kw in query_lower for kw in rule["keywords"]):
                return rule["categories"]
        return None
 
    def _detect_product(self, query: str) -> str | None:
        query_lower = query.lower()
        for product, keywords in self.PRODUCT_RULES.items():
            if any(kw in query_lower for kw in keywords):
                return product
        return None
    
    # Based on Code for Class 04, Section 2 
    def _get_bm25_candidates(self, query: str, k: int, categories: list[str] | None = None) -> list[Document]:
        """Return top-k documents by BM25 score, optionally filtered by category."""
        tokens = self._tokenize(query)
        scores = self.bm25.get_scores(tokens)
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
 
        results = []
        for idx in top_indices:
            if scores[idx] == 0:
                continue
            doc = self.documents[idx]
            if categories and doc.get("category") not in categories:
                continue
            results.append(Document(
                page_content=doc["content"],
                metadata={key: str(v) for key, v in doc.items() if key != "content"},
            ))
        return results
    
    # Based on Code for Class 04, Section 2 
    def _bm25_boost(self, query: str, doc_id: str) -> float:
        """Normalised BM25 score."""
        tokens = self._tokenize(query)
        scores = self.bm25.get_scores(tokens)
        idx = next((i for i, d in enumerate(self.doc_ids) if d == doc_id), None)
        if idx is None:
            return 0.0
        max_score = max(scores) if max(scores) > 0 else 1
        return round(scores[idx] / max_score, 3)
 
    def _recency_boost(self, doc: dict) -> float:

        return 0.1 if doc.get("date", "") >= "2024-01" else 0.0

    # Based on Code for Class 07, Section 3 
    def _satisfaction_boost(self, doc: dict) -> float:

        try:
            score = float(doc.get("customer_satisfaction") or 0)
            if score >= 4.0:
                return 0.1
            if score >= 3.0:
                return 0.05
        except (ValueError, TypeError):
            pass
        return 0.0
    
    # Based on Code for Class 07, Section 3 
    def _product_boost(self, doc: dict, product: str | None) -> float:

        if product and doc.get("product_category") == product:
            return 0.15
        return 0.0
    
    # Based on Code for Class 07
    def retrieve(self, query: str, k: int = 5) -> list[Document]:

        """
        Retrieve top-k documents using semantic + BM25 candidates,
        re-ranked by multi-signal scoring.
        """

        categories = self._detect_category(query) if self.use_filtering else None
        product    = self._detect_product(query)
        chroma_filter = {"category": {"$in": categories}} if categories else None
 
        if self.use_filtering and categories:
            self.debug and print(f"  [Retriever] Filter: {categories}")
            semantic_with_scores = self.vectorstore.similarity_search_with_score(query, k=10, filter=chroma_filter)
            bm25_docs = self._get_bm25_candidates(query, k=10, categories=categories)
        else:
            if self.debug and self.use_filtering:
                print(f"  [Retriever] Filter: none detected")
            semantic_with_scores = self.vectorstore.similarity_search_with_score(query, k=10)
            bm25_docs = self._get_bm25_candidates(query, k=10)

        semantic_scores = {
            doc.metadata.get("document_id", ""): round(1 / (1 + distance), 3)
            for doc, distance in semantic_with_scores
        }
        semantic = [doc for doc, _ in semantic_with_scores]

        # Merge
        seen = {}
        for doc in semantic + bm25_docs:
            doc_id = doc.metadata.get("document_id", "")
            if doc_id not in seen:
                seen[doc_id] = doc
        candidates = list(seen.values())
 
        # Score all candidates
        scored = []
        for rank, doc in enumerate(candidates):
            doc_id = doc.metadata.get("document_id", "")
            raw_doc = self.doc_lookup.get(doc_id, {})
 
            sem_score  = semantic_scores.get(doc_id, 0.3)
            kw_boost   = self._bm25_boost(query, doc_id)
            rec_boost  = self._recency_boost(raw_doc)
            sat_boost  = self._satisfaction_boost(raw_doc)
            prod_boost = self._product_boost(raw_doc, product)
 
            final = round(sem_score + kw_boost + rec_boost + sat_boost + prod_boost, 3)
            scored.append((doc, final, {
                "sem":  round(sem_score, 3),
                "kw":   round(kw_boost, 3),
                "rec":  round(rec_boost, 3),
                "sat":  round(sat_boost, 3),
                "prod": round(prod_boost, 3),
            }))
 
        scored.sort(key=lambda x: x[1], reverse=True)
        results = scored[:k]

        # Fallback detection — return empty list if best score is too low
        top_score = results[0][1] if results else 0
        if top_score < 1.3:
            self.debug and print(f"  [Retriever] Low confidence — top score={top_score} below threshold")
            return []
 
        for doc, score, b in results:
            doc.metadata["retrieval_score"] = score
            self.debug and print(f"  [Retriever] {doc.metadata.get('document_id'):12s} score={score} "
                  f"(sem={b['sem']} kw={b['kw']} rec={b['rec']} sat={b['sat']} prod={b['prod']})")
 
        return [doc for doc, _, _ in results]