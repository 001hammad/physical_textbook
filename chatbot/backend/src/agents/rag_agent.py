from typing import List, Optional
from src.models.data_models import UserQuery, AgentResponse, RetrievedContext, BookContent
from src.models.chat import ChatMode
from src.services.embedding_service import EmbeddingService
from src.services.retrieval_service import RetrievalService
from src.services.llm_service import LLMService
from src.utils.logging_config import get_logger
from src.utils.cache import cached
import uuid
from datetime import datetime

logger = get_logger(__name__)


class RAGAgent:
    """
    RAG Agent that follows OpenAI Agents SDK-inspired pattern:
    Instructions → Context → Tool calls → Output
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.retrieval_service = RetrievalService()
        self.llm_service = LLMService()

    def process_query(self, question: str, selected_text: Optional[str] = None, mode: ChatMode = ChatMode.NORMAL) -> AgentResponse:
        """
        Process a user query following the RAG pattern
        """
        query_id = f"query_{uuid.uuid4().hex[:8]}"
        logger.info(f"Processing query {query_id} in mode: {mode}")

        try:
            # Create UserQuery object
            user_query = UserQuery(
                query_id=query_id,
                question=question,
                selected_text=selected_text,
                mode=mode.value,
                timestamp=datetime.now()
            )

            # Based on mode, follow different processing paths
            if mode == ChatMode.SELECTED_TEXT:
                # Selected-text mode: bypass global retrieval, use only provided text
                response = self._process_selected_text_mode(user_query)
            else:
                # Normal mode: use semantic search to retrieve relevant content
                response = self._process_normal_mode(user_query)

            logger.info(f"Successfully processed query {query_id}")
            return response

        except Exception as e:
            logger.error(f"Error processing query {query_id}: {e}")
            # Return a response indicating the information is not available
            return AgentResponse(
                response_id=f"resp_{uuid.uuid4().hex[:8]}",
                query_id=query_id,
                answer="An error occurred while processing your request. Please try again.",
                sources=[],
                confidence=0.0,
                timestamp=datetime.now()
            )

    def _process_normal_mode(self, user_query: UserQuery) -> AgentResponse:
        """
        Process query in normal mode: retrieve relevant content then generate response
        """
        logger.info(f"Processing query {user_query.query_id} in normal mode")

        # Step 1: Generate embedding for the question with caching
        from src.utils.cache import cache
        import hashlib

        # Create cache key for the question embedding
        question_hash = hashlib.md5(user_query.question.encode()).hexdigest()
        cache_key = f"embedding:{question_hash}"

        query_embedding = cache.get(cache_key)
        if query_embedding is None:
            query_embedding = self.embedding_service.generate_query_embedding(user_query.question)
            if query_embedding:
                cache.set(cache_key, query_embedding, ttl=300)  # Cache for 5 minutes
        else:
            logger.info(f"Retrieved embedding from cache for question: {user_query.question[:50]}...")

        if not query_embedding:
            logger.error(f"Failed to generate embedding for query {user_query.query_id}")
            return AgentResponse(
                response_id=f"resp_{uuid.uuid4().hex[:8]}",
                query_id=user_query.query_id,
                answer="Could not process your question. Please try again.",
                sources=[],
                confidence=0.0,
                timestamp=datetime.now()
            )

        # Step 2: Retrieve relevant content from Qdrant
        retrieved_contexts = self.retrieval_service.retrieve_relevant_content(query_embedding, limit=5)
        if not retrieved_contexts:
            logger.warning(f"No relevant content found for query {user_query.query_id}")
            return AgentResponse(
                response_id=f"resp_{uuid.uuid4().hex[:8]}",
                query_id=user_query.query_id,
                answer="The information you requested is not available in the book.",
                sources=[],
                confidence=0.0,
                timestamp=datetime.now()
            )

        # Step 3: Combine retrieved contexts for the LLM
        context_text = "\n\n".join([ctx.content for ctx in retrieved_contexts])
        source_ids = [ctx.source_id for ctx in retrieved_contexts]

        # Step 4: Generate response using LLM with the retrieved context
        try:
            response_text = self.llm_service.generate_response(context_text, user_query.question)
        except Exception as e:
            logger.error(f"Error generating response with LLM for query {user_query.query_id}: {e}")
            # Check if it's a service availability issue
            error_msg = str(e).lower()
            if any(keyword in error_msg for keyword in ["api", "connection", "timeout", "quota", "rate limit", "service"]):
                return AgentResponse(
                    response_id=f"resp_{uuid.uuid4().hex[:8]}",
                    query_id=user_query.query_id,
                    answer="The response generation service is temporarily unavailable. Please try again later.",
                    sources=source_ids,  # Still include sources even if LLM is unavailable
                    confidence=0.0,
                    timestamp=datetime.now()
                )
            else:
                return AgentResponse(
                    response_id=f"resp_{uuid.uuid4().hex[:8]}",
                    query_id=user_query.query_id,
                    answer="Could not generate a response for your question.",
                    sources=source_ids,
                    confidence=0.5,  # Medium confidence since we have sources but no response
                    timestamp=datetime.now()
                )

        if not response_text:
            logger.warning(f"LLM returned empty response for query {user_query.query_id}")
            return AgentResponse(
                response_id=f"resp_{uuid.uuid4().hex[:8]}",
                query_id=user_query.query_id,
                answer="Could not generate a response for your question.",
                sources=source_ids,
                confidence=0.5,  # Medium confidence since we have sources but no response
                timestamp=datetime.now()
            )

        # Step 5: Calculate confidence based on anti-hallucination validation
        alignment_confidence = self._validate_anti_hallucination(response_text, retrieved_contexts)

        # Use the minimum of alignment confidence and average similarity as final confidence
        avg_similarity = sum(ctx.similarity_score for ctx in retrieved_contexts) / len(retrieved_contexts)
        confidence = min(alignment_confidence, avg_similarity, 1.0)  # Cap at 1.0

        # Step 6: Create and return the response
        response_id = f"resp_{uuid.uuid4().hex[:8]}"
        response = AgentResponse(
            response_id=response_id,
            query_id=user_query.query_id,
            answer=response_text,
            sources=source_ids,
            confidence=confidence,
            timestamp=datetime.now()
        )

        logger.info(f"Generated response {response_id} with confidence {confidence:.2f}")
        return response

    def _process_selected_text_mode(self, user_query: UserQuery) -> AgentResponse:
        """
        Process query in selected-text mode: use only provided text, no retrieval
        """
        logger.info(f"Processing query {user_query.query_id} in selected-text mode")

        if not user_query.selected_text:
            logger.error(f"Selected text is required for selected-text mode in query {user_query.query_id}")
            return AgentResponse(
                response_id=f"resp_{uuid.uuid4().hex[:8]}",
                query_id=user_query.query_id,
                answer="Selected text is required in selected-text mode.",
                sources=[],
                confidence=0.0,
                timestamp=datetime.now()
            )

        # Step 1: Generate response using only the selected text
        try:
            response_text = self.llm_service.generate_response_from_selected_text(
                user_query.selected_text,
                user_query.question
            )
        except Exception as e:
            logger.error(f"Error generating response with LLM for selected-text query {user_query.query_id}: {e}")
            # Check if it's a service availability issue
            error_msg = str(e).lower()
            if any(keyword in error_msg for keyword in ["api", "connection", "timeout", "quota", "rate limit", "service"]):
                return AgentResponse(
                    response_id=f"resp_{uuid.uuid4().hex[:8]}",
                    query_id=user_query.query_id,
                    answer="The response generation service is temporarily unavailable. Please try again later.",
                    sources=[],  # No sources in selected-text mode
                    confidence=0.0,
                    timestamp=datetime.now()
                )
            else:
                return AgentResponse(
                    response_id=f"resp_{uuid.uuid4().hex[:8]}",
                    query_id=user_query.query_id,
                    answer="Could not generate a response for your question based on the selected text.",
                    sources=[],
                    confidence=0.0,
                    timestamp=datetime.now()
                )

        if not response_text:
            logger.warning(f"LLM returned empty response for selected-text query {user_query.query_id}")
            return AgentResponse(
                response_id=f"resp_{uuid.uuid4().hex[:8]}",
                query_id=user_query.query_id,
                answer="Could not generate a response for your question based on the selected text.",
                sources=[],
                confidence=0.0,
                timestamp=datetime.now()
            )

        # Step 2: Create response with high confidence since we're using specific text
        response_id = f"resp_{uuid.uuid4().hex[:8]}"
        response = AgentResponse(
            response_id=response_id,
            query_id=user_query.query_id,
            answer=response_text,
            sources=[],  # No sources since we're using provided text directly
            confidence=0.9,  # High confidence as we're using the exact provided text
            timestamp=datetime.now()
        )

        logger.info(f"Generated response {response_id} in selected-text mode")
        return response

    def validate_response(self, response: AgentResponse, context: Optional[str] = None) -> bool:
        """
        Validate that the response adheres to anti-hallucination constraints
        """
        # Basic validation: ensure the response is not empty
        if not response.answer or not response.answer.strip():
            return False

        # Check that confidence is within valid range
        if not (0.0 <= response.confidence <= 1.0):
            return False

        # Check for common hallucination indicators
        answer_lower = response.answer.lower()

        # If sources are empty but answer claims to be from book content, that's likely hallucination
        if not response.sources and any(phrase in answer_lower for phrase in [
            "according to the book", "the book states", "as mentioned in the text",
            "the text says", "the content indicates", "the book explains"
        ]):
            return False

        # In a more sophisticated implementation, we could check if the response
        # aligns with the provided context or sources
        return True

    def _validate_anti_hallucination(self, response_text: str, retrieved_contexts: List[RetrievedContext]) -> float:
        """
        Enhanced anti-hallucination validation that calculates confidence based on
        how well the response aligns with retrieved contexts
        """
        if not retrieved_contexts or not response_text:
            return 0.0

        # This is a simplified validation - in production, you might use more
        # sophisticated NLP techniques to check alignment between response and context
        response_lower = response_text.lower()
        context_text = " ".join([ctx.content.lower() for ctx in retrieved_contexts])

        # Count how many words from the response appear in the context
        response_words = set(response_lower.split())
        context_words = set(context_text.split())

        if not response_words:
            return 0.0

        matching_words = response_words.intersection(context_words)
        alignment_score = len(matching_words) / len(response_words)

        # Use the minimum of alignment score and average similarity as confidence
        avg_similarity = sum(ctx.similarity_score for ctx in retrieved_contexts) / len(retrieved_contexts)

        # Return the minimum to ensure both good alignment and good retrieval quality
        return min(alignment_score, avg_similarity)

    def index_book_content(self, book_content: BookContent) -> bool:
        """
        Index book content by generating embeddings and storing in Qdrant
        """
        logger.info(f"Indexing book content: {book_content.id}")

        try:
            # Generate embedding for the content
            embedding = self.embedding_service.embed_book_content(book_content.content)
            if not embedding:
                logger.error(f"Failed to generate embedding for content: {book_content.id}")
                return False

            # Update the book content with the embedding
            book_content.embedding = embedding

            # Store in Qdrant
            success = self.retrieval_service.store_book_content(book_content)
            if success:
                logger.info(f"Successfully indexed book content: {book_content.id}")
            else:
                logger.error(f"Failed to store book content in Qdrant: {book_content.id}")

            return success
        except Exception as e:
            logger.error(f"Error indexing book content {book_content.id}: {e}")
            return False