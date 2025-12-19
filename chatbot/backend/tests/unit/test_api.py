import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from src.api.main import app
from src.models.chat import ChatMode


@pytest.fixture
def client():
    """Create a test client for the API"""
    return TestClient(app)


class TestChatAPI:
    """Unit tests for the chat API endpoints"""

    def test_health_check(self, client):
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"

    def test_status_endpoint(self, client):
        """Test the status endpoint"""
        response = client.get("/api/v1/status")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data

    @patch('src.agents.rag_agent.RAGAgent.process_query')
    def test_chat_endpoint_normal_mode(self, mock_process_query, client):
        """Test the chat endpoint with normal mode"""
        # Arrange
        mock_response = Mock()
        mock_response.response_id = "test_resp_id"
        mock_response.answer = "Test answer"
        mock_response.sources = ["source1"]
        mock_response.confidence = 0.8
        mock_process_query.return_value = mock_response

        # Act
        response = client.post(
            "/api/v1/chat",
            json={
                "question": "Test question",
                "mode": "normal"
            }
        )

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == "Test answer"
        assert data["confidence"] == 0.8

    @patch('src.agents.rag_agent.RAGAgent.process_query')
    def test_chat_endpoint_selected_text_mode(self, mock_process_query, client):
        """Test the chat endpoint with selected-text mode"""
        # Arrange
        mock_response = Mock()
        mock_response.response_id = "test_resp_id"
        mock_response.answer = "Test answer from selected text"
        mock_response.sources = []
        mock_response.confidence = 0.9
        mock_process_query.return_value = mock_response

        # Act
        response = client.post(
            "/api/v1/chat",
            json={
                "question": "Test question",
                "selected_text": "Selected text for analysis",
                "mode": "selected-text"
            }
        )

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["answer"] == "Test answer from selected text"
        assert data["confidence"] == 0.9

    def test_chat_endpoint_invalid_request(self, client):
        """Test the chat endpoint with invalid request"""
        # Act
        response = client.post(
            "/api/v1/chat",
            json={
                "question": "",  # Empty question should fail validation
                "mode": "normal"
            }
        )

        # Assert
        assert response.status_code == 422  # Validation error


class TestRateLimiting:
    """Tests for rate limiting functionality"""

    @patch('src.middleware.rate_limit.rate_limiter.is_allowed')
    def test_rate_limiting(self, mock_is_allowed, client):
        """Test that rate limiting works"""
        # Arrange
        mock_is_allowed.return_value = False  # Rate limit exceeded

        # For this test, we'd need to test the middleware more directly
        # This is a basic check to ensure the endpoint exists
        response = client.get("/health")
        assert response.status_code == 200