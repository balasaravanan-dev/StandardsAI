"""
Hybrid Search Service
Combines BM25 (keyword) + Semantic (vector) search with RRF fusion
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import math
import re


@dataclass
class SearchResult:
    """A single search result."""
    is_number: str
    title: str
    scope: str
    score: float
    bm25_rank: Optional[int] = None
    semantic_rank: Optional[int] = None
    match_reasons: List[str] = None


class HybridSearch:
    """
    Hybrid search combining BM25 and semantic similarity.

    For demo: Uses simple keyword matching + TF-IDF-like scoring.
    For production: Replace with sentence-transformers embeddings.
    """

    def __init__(self, standards: List[Dict]):
        self.standards = standards
        self._build_index()

    def _build_index(self):
        """Build inverted index for BM25-like search."""
        self.index = {}  # term -> list of (doc_idx, term_freq)
        self.doc_lengths = []
        self.avg_doc_length = 0

        for idx, std in enumerate(self.standards):
            # Combine searchable fields
            text = self._get_searchable_text(std)
            tokens = self._tokenize(text)

            self.doc_lengths.append(len(tokens))

            term_freq = {}
            for token in tokens:
                term_freq[token] = term_freq.get(token, 0) + 1

            for term, freq in term_freq.items():
                if term not in self.index:
                    self.index[term] = []
                self.index[term].append((idx, freq))

        if self.doc_lengths:
            self.avg_doc_length = sum(self.doc_lengths) / len(self.doc_lengths)

    def _get_searchable_text(self, std: Dict) -> str:
        """Get all searchable text from a standard."""
        parts = [
            std.get("is_number", ""),
            std.get("title", ""),
            std.get("scope", ""),
            " ".join(std.get("keywords", [])),
            std.get("category", ""),
            std.get("department", "")
        ]
        return " ".join(parts)

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        tokens = text.split()
        # Remove common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'for', 'of', 'to', 'in', 'on', 'with', 'is', 'are', 'as'}
        return [t for t in tokens if t not in stop_words and len(t) > 1]

    def bm25_search(self, query: str, top_k: int = 20) -> List[Tuple[int, float]]:
        """
        BM25 ranking algorithm.

        BM25 parameters:
        - k1: term frequency saturation parameter (1.2-2.0)
        - b: length normalization parameter (0.75)
        """
        k1 = 1.5
        b = 0.75
        N = len(self.standards)

        query_tokens = self._tokenize(query)
        scores = [0.0] * N

        for token in query_tokens:
            if token not in self.index:
                continue

            posting_list = self.index[token]
            df = len(posting_list)  # document frequency
            idf = math.log((N - df + 0.5) / (df + 0.5) + 1)

            for doc_idx, tf in posting_list:
                doc_len = self.doc_lengths[doc_idx]
                tf_component = (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * doc_len / self.avg_doc_length))
                scores[doc_idx] += idf * tf_component

        # Return top K with scores
        ranked = [(i, scores[i]) for i in range(N) if scores[i] > 0]
        ranked.sort(key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    def semantic_search(self, query: str, top_k: int = 20) -> List[Tuple[int, float]]:
        """
        Semantic search using keyword overlap (simplified).

        For production: Use sentence-transformers embeddings.
        """
        query_tokens = set(self._tokenize(query))
        scores = []

        for idx, std in enumerate(self.standards):
            text = self._get_searchable_text(std)
            doc_tokens = set(self._tokenize(text))

            # Jaccard similarity + keyword boost
            intersection = len(query_tokens & doc_tokens)
            union = len(query_tokens | doc_tokens)

            if union > 0:
                jaccard = intersection / union

                # Boost for keyword matches
                keyword_matches = len(query_tokens & set(std.get("keywords", [])))
                boost = keyword_matches * 0.2

                score = jaccard + boost
                if score > 0:
                    scores.append((idx, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

    def hybrid_search(
        self,
        query: str,
        top_k: int = 10,
        bm25_weight: float = 0.5,
        semantic_weight: float = 0.5
    ) -> List[SearchResult]:
        """
        Hybrid search with Reciprocal Rank Fusion (RRF).

        RRF formula: score(d) = sum(1 / (k + rank(d)))
        where k is typically 60
        """
        k = 60  # RRF constant

        # Get results from both methods
        bm25_results = self.bm25_search(query, top_k * 2)
        semantic_results = self.semantic_search(query, top_k * 2)

        # Build rank maps
        bm25_ranks = {doc_idx: rank + 1 for rank, (doc_idx, _) in enumerate(bm25_results)}
        semantic_ranks = {doc_idx: rank + 1 for rank, (doc_idx, _) in enumerate(semantic_results)}

        # Combine with RRF
        all_docs = set(bm25_ranks.keys()) | set(semantic_ranks.keys())
        rrf_scores = {}

        for doc_idx in all_docs:
            bm25_rank = bm25_ranks.get(doc_idx, 1000)  # High rank if not found
            semantic_rank = semantic_ranks.get(doc_idx, 1000)

            rrf_score = (
                bm25_weight * (1 / (k + bm25_rank)) +
                semantic_weight * (1 / (k + semantic_rank))
            )
            rrf_scores[doc_idx] = rrf_score

        # Sort by RRF score
        ranked = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

        # Build results
        results = []
        for doc_idx, score in ranked[:top_k]:
            std = self.standards[doc_idx]

            # Determine match reasons
            reasons = []
            if doc_idx in bm25_ranks:
                reasons.append(f"Keyword match (rank {bm25_ranks[doc_idx]})")
            if doc_idx in semantic_ranks:
                reasons.append(f"Semantic match (rank {semantic_ranks[doc_idx]})")

            results.append(SearchResult(
                is_number=std["is_number"],
                title=std["title"],
                scope=std["scope"],
                score=round(score * 100, 2),  # Normalize to 0-100
                bm25_rank=bm25_ranks.get(doc_idx),
                semantic_rank=semantic_ranks.get(doc_idx),
                match_reasons=reasons
            ))

        return results

    def search_with_context(
        self,
        query: str,
        top_k: int = 10
    ) -> Tuple[List[SearchResult], Dict]:
        """
        Search with context extraction.

        Extracts context factors from query and boosts matching standards.
        """
        context = self._extract_context(query)
        results = self.hybrid_search(query, top_k * 2)

        # Apply context boost
        boosted = []
        for result in results:
            std = next((s for s in self.standards if s["is_number"] == result.is_number), None)
            if not std:
                boosted.append(result)
                continue

            boost = 0
            boost_reasons = []

            # Environment boost
            if context.get("coastal") and "marine" in std.get("scope", "").lower():
                boost += 0.1
                boost_reasons.append("coastal/marine match")
            if context.get("coastal") and "corrosion" in std.get("scope", "").lower():
                boost += 0.1
                boost_reasons.append("corrosion protection")

            # Application boost
            if context.get("drinking_water") and "potable" in std.get("scope", "").lower():
                boost += 0.1
                boost_reasons.append("potable water match")

            result.score = round(result.score + boost * 100, 2)
            if boost_reasons:
                result.match_reasons = (result.match_reasons or []) + boost_reasons

            boosted.append(result)

        # Re-sort after boost
        boosted.sort(key=lambda x: x.score, reverse=True)
        return boosted[:top_k], context

    def _extract_context(self, query: str) -> Dict:
        """Extract context factors from query."""
        query_lower = query.lower()

        context = {
            "coastal": any(w in query_lower for w in ["coastal", "marine", "sea", "beach"]),
            "drinking_water": any(w in query_lower for w in ["drinking", "potable", "water supply"]),
            "industrial": any(w in query_lower for w in ["industrial", "factory", "plant"]),
            "construction": any(w in query_lower for w in ["construction", "building", "road"]),
            "food": any(w in query_lower for w in ["food", "kitchen", "canteen", "eating"])
        }

        return context


# Convenience function
def search(query: str, standards: List[Dict], top_k: int = 10) -> List[SearchResult]:
    """Quick search function."""
    searcher = HybridSearch(standards)
    return searcher.hybrid_search(query, top_k)
