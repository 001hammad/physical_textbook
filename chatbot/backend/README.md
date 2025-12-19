# RAG Chatbot Backend for Physical AI & Humanoid Robotics Book

This is the backend service for the RAG (Retrieval-Augmented Generation) chatbot that provides answers based on the content of the Physical AI & Humanoid Robotics book.

## Architecture

The system uses an agent-based architecture with the following components:
- **FastAPI**: Web framework for the API service
- **Gemini**: Language model for response generation
- **Cohere**: Embedding generation for semantic search
- **Qdrant**: Vector database for storing and retrieving book content embeddings

## Features

- Answer user questions based on book content with anti-hallucination constraints
- Support for two interaction modes:
  - Normal question mode: Semantic search through book content
  - Selected-text mode: Focus on provided text without global retrieval
- CORS configuration for secure integration with the book website
- Free-tier service compliance (no billing required)
- Rate limiting to comply with API usage limits
- Input sanitization for security
- Comprehensive error handling for service unavailability

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example` and add your API keys:
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

   For local development, make sure to include localhost in your CORS_ORIGINS:
   ```
   CORS_ORIGINS=https://physical-textbook.vercel.app,http://localhost:3000,http://localhost:3001,http://127.0.0.1:3000,http://127.0.0.1:3001
   ```

4. Run the application:
   ```bash
   uvicorn src.api.main:app --reload --port 8000
   ```

## API Endpoints

- `POST /api/v1/chat`: Process user queries and return responses based on book content
  - Request body: `{"question": "your question", "selected_text": "optional selected text", "mode": "normal|selected-text"}`
  - Response: `{"response_id": "...", "answer": "...", "sources": [...], "confidence": 0.8, "message": "optional additional message"}`
- `GET /api/v1/status`: Health check endpoint
- `GET /health`: Alternative health check endpoint
- `GET /docs`: Interactive API documentation (Swagger UI)
- `GET /redoc`: Alternative API documentation (ReDoc)

## Environment Variables

- `GEMINI_API_KEY`: Your Gemini API key
- `COHERE_API_KEY`: Your Cohere API key
- `QDRANT_URL`: URL of your Qdrant cluster
- `QDRANT_API_KEY`: Qdrant API key (optional for local Qdrant)
- `QDRANT_COLLECTION_NAME`: Name of the collection in Qdrant (default: book-collection)
- `CORS_ORIGINS`: Comma-separated list of allowed origins (default: https://physical-textbook.vercel.app)
- `MAX_TOKENS`: Maximum tokens for Gemini responses (default: 512)
- `TEMPERATURE`: Gemini temperature parameter (default: 0.7)
- `LOG_LEVEL`: Logging level (default: INFO)
- `LOG_FILE`: Optional log file path

## Rate Limiting

The API implements rate limiting to comply with free-tier usage limits:
- Default: 30 requests per minute per IP
- Burst limit: 5 requests per second

## Development

Run tests:
```bash
pytest
```

Run specific test module:
```bash
pytest tests/unit/test_agents.py
pytest tests/integration/test_end_to_end.py
```

Run with coverage:
```bash
pytest --cov=src --cov-report=html
```

Run with auto-reload during development:
```bash
uvicorn src.api.main:app --reload
```

## Testing

The project includes:
- Unit tests for individual components (in `tests/unit/`)
- Integration tests for API endpoints (in `tests/integration/`)

To run all tests:
```bash
pytest
```

To run tests with verbose output:
```bash
pytest -v
```

## Security

- Input sanitization to prevent injection attacks
- Rate limiting to prevent abuse
- CORS configuration to restrict origins
- Environment-based configuration to keep secrets secure

## Deployment

For production deployment:
1. Set appropriate environment variables
2. Use a production WSGI server like Gunicorn:
   ```bash
   pip install "uvicorn[standard]"
   uvicorn src.api.main:app --host 0.0.0.0 --port 8000
   ```
3. Set up a reverse proxy (e.g., nginx) for additional security and performance