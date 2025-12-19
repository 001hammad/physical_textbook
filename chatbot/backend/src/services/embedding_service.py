import cohere
from typing import List
from src.utils.config import config
import logging

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Service for generating embeddings using Cohere"""

    def __init__(self):
        # Initialize Cohere client
        self.client = cohere.Client(config.COHERE_API_KEY)

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts using Cohere
        """
        try:
            response = self.client.embed(
                texts=texts,
                model="embed-english-v3.0",  # Using a reliable English embedding model
                input_type="search_document"  # Optimize for search documents
            )
            logger.info(f"Generated embeddings for {len(texts)} texts")
            return [embedding for embedding in response.embeddings]
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            return []

    def generate_query_embedding(self, query: str) -> List[float]:
        """
        Generate embedding for a query string
        """
        try:
            response = self.client.embed(
                texts=[query],
                model="embed-english-v3.0",
                input_type="search_query"  # Optimize for search queries
            )
            logger.info("Generated embedding for query")
            return response.embeddings[0] if response.embeddings else []
        except Exception as e:
            logger.error(f"Error generating query embedding: {e}")
            return []

    def embed_book_content(self, content: str) -> List[float]:
        """
        Generate embedding for book content
        """
        try:
            response = self.client.embed(
                texts=[content],
                model="embed-english-v3.0",
                input_type="search_document"
            )
            logger.info("Generated embedding for book content")
            return response.embeddings[0] if response.embeddings else []
        except Exception as e:
            logger.error(f"Error generating content embedding: {e}")
            return []

    def calculate_similarity(self, embedding1: List[float], embedding2: List[float]) -> float:
        """
        Calculate cosine similarity between two embeddings
        This is a simple implementation - in production, consider using optimized libraries
        """
        try:
            # Calculate dot product
            dot_product = sum(a * b for a, b in zip(embedding1, embedding2))

            # Calculate magnitudes
            magnitude1 = sum(a * a for a in embedding1) ** 0.5
            magnitude2 = sum(b * b for b in embedding2) ** 0.5

            # Calculate cosine similarity
            if magnitude1 == 0 or magnitude2 == 0:
                return 0.0

            similarity = dot_product / (magnitude1 * magnitude2)

            # Ensure the result is between 0 and 1 (cosine similarity range is [-1, 1])
            # For our use case, we'll normalize to [0, 1] range
            return max(0.0, (similarity + 1) / 2)
        except Exception as e:
            logger.error(f"Error calculating similarity: {e}")
            return 0.0