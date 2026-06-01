import time

import numpy as np
from typing import List
from langchain_core.documents import Document


class ContextCompressor:
    """
    Dynamic context selection layer for RAG.
    """

    def __init__(
        self,
        embeddings,
        relative_threshold: float = 0.5,
        max_chunks_per_doc: int = 6,
        debug: bool = False
    ):
        self.embeddings = embeddings
        self.relative_threshold = relative_threshold
        self.max_chunks_per_doc = max_chunks_per_doc
        self.debug = debug

    def compress(
        self,
        query: str,
        documents: List[Document],
    ) -> tuple[List[Document]]:
        """
        Filter by relative retrieval score, then compress each document
        to its most semantically relevant sections.
        Returns (compressed_docs, latency_seconds).
        """

        filtered = self._filter_by_relative_score(documents)

        compressed = []
        for doc in filtered:
            compressed_text = self._paragraph_chunking(query, doc.page_content)
            if compressed_text.strip():
                compressed.append(Document(
                    page_content=compressed_text,
                    metadata=doc.metadata,
                ))

        return compressed

    # Based on Code for Class 04, Section 2 
    def _filter_by_relative_score(self, documents: List[Document]) -> List[Document]:

        """Drop documents scoring below relative_threshold * top_score."""

        if not documents:
            self.debug and print("  [Compressor] No documents to filter")
            return []

        scores = [float(doc.metadata.get("retrieval_score", 0)) for doc in documents]
        top_score = max(scores)
        cutoff = top_score * self.relative_threshold

        kept = [doc for doc, score in zip(documents, scores) if score >= cutoff]
        dropped = len(documents) - len(kept)

        if self.debug and dropped:
            print(f"  [Compressor] Dropped {dropped} doc(s) below {cutoff:.3f} "
                  f"(threshold={self.relative_threshold} × top={top_score:.3f})")

        return kept

    # Based on Code for Class 05, Section 2 
    def _paragraph_chunking(self, query: str, text: str) -> str:
        """
        Split document into paragraphs using \n separator,
        score each by cosine similarity to the query embedding,
        and return the top max_chunks_per_doc sections.
        Falls back to full text if only one section found.
        """
        sections = [p.strip() for p in text.split("\n") if p.strip()]

        self.debug and print(f"  [Compressor] sections={len(sections)}")

        if len(sections) <= 1:
            self.debug and print(f"  [Compressor] Single section — returning full text")
            return text 

        query_vec = self.embeddings.embed_query(query)
        section_vecs = self.embeddings.embed_documents(sections)

        scored = [
            (section, self._cosine_similarity(query_vec, vec))
            for section, vec in zip(sections, section_vecs)
        ]
        scored.sort(key=lambda x: x[1], reverse=True)

        top = [sec for sec, _ in scored[:self.max_chunks_per_doc]]
        return "\n\n".join(top)

    # Based on Code for Class 03, Section 1 
    def _cosine_similarity(self, vec1: list, vec2: list) -> float:
        """Calculate cosine similarity between two vectors.
        
        This is the fundamental operation in semantic search. Understanding
        this calculation helps you debug similarity scores later.
        """
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        
        # Dot product
        dot_product = np.dot(vec1, vec2)
        
        # Magnitudes
        magnitude1 = np.linalg.norm(vec1)
        magnitude2 = np.linalg.norm(vec2)
        
        # Cosine similarity
        similarity = dot_product / (magnitude1 * magnitude2)
        
        return similarity