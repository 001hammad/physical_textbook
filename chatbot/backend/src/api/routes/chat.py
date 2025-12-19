import html
import re
from fastapi import APIRouter, HTTPException
from typing import Union
from src.models.chat import ChatRequest, ChatResponse, ErrorResponse, StatusResponse
from src.agents.rag_agent import RAGAgent
from src.models.chat import ChatMode
from src.utils.logging_config import get_logger
import uuid
from datetime import datetime

logger = get_logger(__name__)


def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent injection attacks and remove potentially harmful content
    """
    if not text:
        return text

    # Remove potentially dangerous characters/sequences
    # HTML decode to prevent HTML injection
    text = html.unescape(text)

    # Remove any script tags (case insensitive)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)

    # Remove other potentially dangerous tags
    dangerous_tags = ['<iframe', '<object', '<embed', '<form', '<input']
    for tag in dangerous_tags:
        text = re.sub(rf'{tag}[^>]*>.*?</{tag.split("<")[1]}>', '', text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(rf'{tag}[^>]*/>', '', text, flags=re.IGNORECASE)

    # Limit length to prevent extremely long inputs
    max_length = 5000  # Adjust as needed
    if len(text) > max_length:
        text = text[:max_length]

    return text.strip()


# Create router
router = APIRouter()

# Initialize the RAG agent
rag_agent = RAGAgent()


@router.post("/chat",
             response_model=ChatResponse,
             responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def chat_endpoint(chat_request: ChatRequest):
    """
    Process user queries and return responses based on book content with anti-hallucination constraints
    """
    try:
        logger.info(f"Received chat request with mode: {chat_request.mode}")

        # Sanitize inputs
        sanitized_question = sanitize_input(chat_request.question)
        sanitized_selected_text = sanitize_input(chat_request.selected_text) if chat_request.selected_text else None

        # Validate sanitized inputs
        if not sanitized_question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty after sanitization")

        if chat_request.mode == ChatMode.SELECTED_TEXT and (not sanitized_selected_text or not sanitized_selected_text.strip()):
            raise HTTPException(status_code=400, detail="Selected text cannot be empty after sanitization")

        # Process the query using the RAG agent with sanitized inputs
        try:
            agent_response = rag_agent.process_query(
                question=sanitized_question,
                selected_text=sanitized_selected_text,
                mode=ChatMode(chat_request.mode)
            )
        except Exception as e:
            logger.error(f"Error in RAG agent processing: {e}")
            # Return a user-friendly error when services are unavailable
            if "API" in str(e).upper() or "CONNECTION" in str(e).upper() or "TIMEOUT" in str(e).upper():
                raise HTTPException(
                    status_code=503,
                    detail="One or more external services are temporarily unavailable. Please try again later."
                )
            else:
                raise HTTPException(
                    status_code=500,
                    detail="An error occurred while processing your request. Please try again."
                )

        # Create the base chat response
        response = ChatResponse(
            response_id=agent_response.response_id,
            answer=agent_response.answer,
            sources=agent_response.sources,
            confidence=agent_response.confidence
        )

        # Add additional message if information is not available in book
        if "not available in the book" in agent_response.answer.lower() or \
           "cannot be derived from the book" in agent_response.answer.lower():
            response.message = "Information not found in book content"

        logger.info(f"Returning response with ID: {agent_response.response_id}")
        return response

    except ValueError as e:
        logger.error(f"Validation error in chat endpoint: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        logger.error(f"Unexpected error in chat endpoint: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while processing your request"
        )


@router.get("/status", response_model=StatusResponse)
async def status_endpoint():
    """
    Health check endpoint that returns the health status of the API
    """
    try:
        # In a real implementation, you might want to check the status of external services
        # like the Qdrant database, Cohere API, or Gemini API
        status = "healthy"

        response = StatusResponse(
            status=status,
            timestamp=datetime.now()
        )

        logger.info("Status endpoint accessed")
        return response

    except Exception as e:
        logger.error(f"Error in status endpoint: {e}")
        return StatusResponse(
            status="unavailable",
            timestamp=datetime.now()
        )


@router.get("/health", response_model=StatusResponse)
async def health_check():
    """
    Alternative health check endpoint
    """
    try:
        # Perform any additional health checks here if needed
        status = "healthy"

        response = StatusResponse(
            status=status,
            timestamp=datetime.now()
        )

        logger.info("Health check endpoint accessed")
        return response

    except Exception as e:
        logger.error(f"Error in health check endpoint: {e}")
        return StatusResponse(
            status="unavailable",
            timestamp=datetime.now()
        )