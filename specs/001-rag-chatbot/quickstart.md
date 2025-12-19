# Quickstart Guide: RAG Chatbot Backend

## Prerequisites

- Python 3.11+
- Access to Gemini API (free tier)
- Access to Cohere API (free tier)
- Qdrant Cloud account (free tier)

## Setup

### 1. Clone and Navigate
```bash
cd chatbot/backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

Edit `.env` with your API keys:
```env
GEMINI_API_KEY=your_gemini_api_key
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
BOOK_CONTENT_PATH=path/to/book/content
```

### 5. Initialize the Vector Database
```bash
# Run the embedding script to index book content
python -m src.services.embedding_service --index-book
```

## Running the Application

### Development
```bash
# Start the FastAPI server
uvicorn src.api.main:app --reload --port 8000
```

### Production
```bash
# Using uvicorn with production settings
uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

## API Usage

### Chat Endpoint
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the key principles of humanoid robotics?",
    "mode": "normal"
  }'
```

### Health Check
```bash
curl http://localhost:8000/api/v1/status
```

## Environment Variables

- `GEMINI_API_KEY`: Your Gemini API key (required)
- `COHERE_API_KEY`: Your Cohere API key (required)
- `QDRANT_URL`: URL of your Qdrant cluster (required)
- `QDRANT_API_KEY`: Qdrant API key (required)
- `BOOK_CONTENT_PATH`: Path to book content files (optional, for indexing)
- `CORS_ORIGINS`: Comma-separated list of allowed origins (default: https://physical-textbook.vercel.app)
- `MAX_TOKENS`: Maximum tokens for Gemini responses (default: 512)

## Testing

Run unit tests:
```bash
pytest tests/unit/
```

Run integration tests:
```bash
pytest tests/integration/
```

## Project Structure

```
chatbot/backend/
├── src/
│   ├── agents/           # Agent controller logic
│   ├── api/             # FastAPI application and routes
│   ├── models/          # Data models and schemas
│   ├── services/        # Business logic services
│   └── utils/           # Utility functions
├── tests/               # Test files
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # Project documentation
```