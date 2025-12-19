import pytest
from unittest.mock import Mock, patch, MagicMock
from src.services.embedding_service import EmbeddingService
from src.services.retrieval_service import RetrievalService
from src.services.llm_service import LLMService


class TestEmbeddingService:
    """Unit tests for EmbeddingService"""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Mock the Cohere client
        with patch('cohere.Client') as mock_client:
            self.service = EmbeddingService()
            self.service.client = mock_client

    @patch('cohere.Client')
    def test_generate_embeddings_success(self, mock_cohere_client):
        """Test generating embeddings successfully"""
        # Arrange
        mock_client_instance = Mock()
        mock_client_instance.embed.return_value = Mock(embeddings=[[0.1, 0.2, 0.3]])
        mock_cohere_client.return_value = mock_client_instance

        service = EmbeddingService()
        texts = ["test text"]

        # Act
        result = service.generate_embeddings(texts)

        # Assert
        assert result == [[0.1, 0.2, 0.3]]
        mock_client_instance.embed.assert_called_once()

    @patch('cohere.Client')
    def test_generate_query_embedding_success(self, mock_cohere_client):
        """Test generating query embedding successfully"""
        # Arrange
        mock_client_instance = Mock()
        mock_client_instance.embed.return_value = Mock(embeddings=[[0.4, 0.5, 0.6]])
        mock_cohere_client.return_value = mock_client_instance

        service = EmbeddingService()
        query = "test query"

        # Act
        result = service.generate_query_embedding(query)

        # Assert
        assert result == [0.4, 0.5, 0.6]


class TestRetrievalService:
    """Unit tests for RetrievalService"""

    @patch('qdrant_client.QdrantClient')
    def test_retrieve_relevant_content_success(self, mock_qdrant_client):
        """Test retrieving relevant content successfully"""
        # Arrange
        mock_client_instance = Mock()
        mock_qdrant_client.return_value = mock_client_instance

        # Mock search results
        mock_search_result = [
            Mock(id="doc1", score=0.9, payload={"content": "test content", "title": "test title"})
        ]
        mock_client_instance.search.return_value = mock_search_result

        service = RetrievalService()
        service.client = mock_client_instance

        # Act
        result = service.retrieve_relevant_content([0.1, 0.2, 0.3], limit=1)

        # Assert
        assert len(result) == 1
        assert result[0].content == "test content"
        assert result[0].similarity_score == 0.9


class TestLLMService:
    """Unit tests for LLMService"""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Mock the Google Generative AI
        with patch('google.generativeai.GenerativeModel') as mock_model:
            with patch('google.generativeai.configure') as mock_configure:
                self.service = LLMService()
                self.service.model = mock_model

    @patch('google.generativeai.configure')
    @patch('google.generativeai.GenerativeModel')
    def test_generate_response_success(self, mock_gen_model_class, mock_configure):
        """Test generating response successfully"""
        # Arrange
        mock_model_instance = Mock()
        mock_response = Mock()
        mock_response.text = "Test response from Gemini"
        mock_model_instance.generate_content.return_value = mock_response
        mock_gen_model_class.return_value = mock_model_instance

        service = LLMService()

        # Act
        result = service.generate_response("test context", "test question")

        # Assert
        assert result == "Test response from Gemini"
        mock_model_instance.generate_content.assert_called_once()