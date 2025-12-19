from typing import List, Optional
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct
from src.models.data_models import BookContent, RetrievedContext
from src.utils.config import config
import logging

logger = logging.getLogger(__name__)


class RetrievalService:
    """Service for retrieving relevant book content from Qdrant vector database"""

    def __init__(self):
        # Initialize Qdrant client
        if config.QDRANT_API_KEY:
            self.client = QdrantClient(
                url=config.QDRANT_URL,
                api_key=config.QDRANT_API_KEY,
                prefer_grpc=False
            )
        else:
            # For local Qdrant without API key
            self.client = QdrantClient(url=config.QDRANT_URL)

        self.collection_name = config.QDRANT_COLLECTION_NAME
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        """Ensure the collection exists in Qdrant with proper configuration"""
        try:
            # Check if collection exists
            self.client.get_collection(self.collection_name)
            logger.info(f"Collection '{self.collection_name}' already exists")
        except Exception:
            # Create collection if it doesn't exist
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
            )
            logger.info(f"Created collection '{self.collection_name}'")

    def store_book_content(self, book_content: BookContent) -> bool:
        """
        Store book content in Qdrant with its embedding
        """
        try:
            # Prepare the point to store
            point = PointStruct(
                id=book_content.id,
                vector=book_content.embedding if book_content.embedding else [],
                payload={
                    "title": book_content.title,
                    "content": book_content.content,
                    "metadata": book_content.metadata
                }
            )

            # Upsert the point into the collection
            self.client.upsert(
                collection_name=self.collection_name,
                points=[point]
            )
            logger.info(f"Stored book content with ID: {book_content.id}")
            return True
        except Exception as e:
            logger.error(f"Error storing book content: {e}")
            return False

    def retrieve_relevant_content(self, query_embedding: List[float], limit: int = 5) -> List[RetrievedContext]:
        """
        Retrieve the most relevant book content based on the query embedding
        """
        try:
            # Search for similar vectors in Qdrant
            search_results = self.client.query_points(
                collection_name=self.collection_name,
                query=query_embedding,
                limit=limit,
                with_payload=True
            )

            # Convert search results to RetrievedContext objects
            # Note: query_points returns a QueryResponse object with points
            retrieved_contexts = []
            for result in search_results.points:  # Access the points attribute
                if result.payload:
                    retrieved_context = RetrievedContext(
                        context_id=result.id,
                        content=result.payload.get("content", ""),
                        similarity_score=result.score,
                        source_id=result.id,
                        retrieval_metadata={
                            "title": result.payload.get("title", ""),
                            "metadata": result.payload.get("metadata", {})
                        }
                    )
                    retrieved_contexts.append(retrieved_context)

            logger.info(f"Retrieved {len(retrieved_contexts)} relevant content pieces")
            return retrieved_contexts
        except Exception as e:
            logger.error(f"Error retrieving content: {e}")
            return []

    def get_all_content_ids(self) -> List[str]:
        """
        Get all stored content IDs
        """
        try:
            records, _ = self.client.scroll(
                collection_name=self.collection_name,
                limit=10000,  # Adjust as needed
                with_payload=False
            )
            return [record.id for record in records]
        except Exception as e:
            logger.error(f"Error getting content IDs: {e}")
            return []

    def delete_content(self, content_id: str) -> bool:
        """
        Delete specific content from the collection
        """
        try:
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=models.PointIdsList(points=[content_id])
            )
            logger.info(f"Deleted content with ID: {content_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting content: {e}")
            return False