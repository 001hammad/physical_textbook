import pytest
from unittest.mock import Mock, patch
from src.agents.rag_agent import RAGAgent
from src.models.chat import ChatMode


class TestRAGAgent:
    """Unit tests for RAGAgent"""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.agent = RAGAgent()

    @patch('src.services.embedding_service.EmbeddingService.generate_query_embedding')
    @patch('src.services.retrieval_service.RetrievalService.retrieve_relevant_content')
    @patch('src.services.llm_service.LLMService.generate_response')
    def test_process_query_normal_mode_success(self, mock_llm_gen, mock_retrieve, mock_embed_gen):
        """Test processing a query in normal mode successfully"""
        # Arrange
        mock_embed_gen.return_value = [0.1, 0.2, 0.3]
        mock_retrieve.return_value = []
        mock_llm_gen.return_value = "Test response"

        # Act
        result = self.agent.process_query("Test question", mode=ChatMode.NORMAL)

        # Assert
        assert result is not None
        assert result.answer == "Test response"

    @patch('src.services.llm_service.LLMService.generate_response_from_selected_text')
    def test_process_query_selected_text_mode_success(self, mock_llm_gen):
        """Test processing a query in selected-text mode successfully"""
        # Arrange
        mock_llm_gen.return_value = "Test response from selected text"

        # Act
        result = self.agent.process_query(
            "Test question",
            selected_text="Selected text",
            mode=ChatMode.SELECTED_TEXT
        )

        # Assert
        assert result is not None
        assert result.answer == "Test response from selected text"

    def test_validate_response_valid(self):
        """Test that a valid response passes validation"""
        # Arrange
        from src.models.data_models import AgentResponse
        response = AgentResponse(
            response_id="test_id",
            query_id="test_query_id",
            answer="This is a valid answer",
            sources=[],
            confidence=0.8,
        )

        # Act
        result = self.agent.validate_response(response)

        # Assert
        assert result is True

    def test_validate_response_invalid_confidence(self):
        """Test that a response with invalid confidence fails validation"""
        # Arrange
        from src.models.data_models import AgentResponse
        response = AgentResponse(
            response_id="test_id",
            query_id="test_query_id",
            answer="This is a valid answer",
            sources=[],
            confidence=1.5,  # Invalid confidence
        )

        # Act
        result = self.agent.validate_response(response)

        # Assert
        assert result is False