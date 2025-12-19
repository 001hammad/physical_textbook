import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch, MagicMock
from src.api.main import app
from src.models.chat import ChatMode


@pytest.fixture
def client():
    """Create a test client for the API"""
    return TestClient(app)


class TestEndToEnd:
    """Integration tests for end-to-end functionality"""

    @patch('src.agents.rag_agent.RAGAgent.process_query')
    def test_end_to_end_normal_mode(self, mock_process_query, client):
        """Test end-to-end flow for normal mode"""
        # Arrange
        mock_response = Mock()
        mock_response.response_id = "test_resp_id"
        mock_response.answer = "Based on the book content, humanoid robots require careful design considerations."
        mock_response.sources = ["ch1_introduction", "sec2_3_design_principles"]
        mock_response.confidence = 0.85
        mock_process_query.return_value = mock_response

        # Act
        response = client.post(
            "/api/v1/chat",
            json={
                "question": "What are the key design principles for humanoid robots?",
                "mode": "normal"
            }
        )

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "based on the book content" in data["answer"].lower()
        assert len(data["sources"]) > 0
        assert 0.0 <= data["confidence"] <= 1.0

    @patch('src.agents.rag_agent.RAGAgent.process_query')
    def test_end_to_end_selected_text_mode(self, mock_process_query, client):
        """Test end-to-end flow for selected-text mode"""
        # Arrange
        mock_response = Mock()
        mock_response.response_id = "test_resp_id"
        mock_response.answer = "The selected text explains the core concepts of physical AI."
        mock_response.sources = []  # No sources in selected-text mode
        mock_response.confidence = 0.9
        mock_process_query.return_value = mock_response

        selected_text = "Physical AI combines principles of physics and artificial intelligence..."

        # Act
        response = client.post(
            "/api/v1/chat",
            json={
                "question": "Can you explain the concepts in this text?",
                "selected_text": selected_text,
                "mode": "selected-text"
            }
        )

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "selected text" in data["answer"].lower()
        assert data["confidence"] == 0.9

    @patch('src.agents.rag_agent.RAGAgent.process_query')
    def test_end_to_end_no_content_found(self, mock_process_query, client):
        """Test end-to-end flow when no relevant content is found"""
        # Arrange
        mock_response = Mock()
        mock_response.response_id = "test_resp_id"
        mock_response.answer = "The information you requested is not available in the book."
        mock_response.sources = []
        mock_response.confidence = 0.0
        mock_process_query.return_value = mock_response

        # Act
        response = client.post(
            "/api/v1/chat",
            json={
                "question": "What is the meaning of life according to this book?",
                "mode": "normal"
            }
        )

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "not available in the book" in data["answer"].lower()
        assert data["confidence"] == 0.0

    def test_api_documentation_available(self, client):
        """Test that API documentation is available"""
        # Test Swagger UI
        response = client.get("/docs")
        assert response.status_code == 200

        # Test ReDoc
        response = client.get("/redoc")
        assert response.status_code == 200

        # Test OpenAPI schema
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert data["info"]["title"] == "RAG Chatbot API for Physical AI & Humanoid Robotics Book"

    def test_health_endpoints(self, client):
        """Test that health check endpoints work"""
        # Test root endpoint
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "RAG Chatbot API" in data["message"]

        # Test health endpoint
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"

        # Test status endpoint
        response = client.get("/api/v1/status")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data