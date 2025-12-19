import os
from typing import List, Optional
from dotenv import load_dotenv
from .logging_config import setup_logging

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to manage application settings"""

    # API Keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    COHERE_API_KEY: str = os.getenv("COHERE_API_KEY", "")
    QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")

    # Qdrant Configuration
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "book-collection")

    # Book Content Path
    BOOK_CONTENT_PATH: Optional[str] = os.getenv("BOOK_CONTENT_PATH")

    # CORS Configuration
    CORS_ORIGINS: List[str] = os.getenv("CORS_ORIGINS", "https://physical-textbook.vercel.app").split(",")

    # Gemini Configuration
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "512"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))

    # Application Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: Optional[str] = os.getenv("LOG_FILE")

    # Rate Limiting Configuration
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = int(os.getenv("RATE_LIMIT_REQUESTS_PER_MINUTE", "30"))
    RATE_LIMIT_BURST_SIZE: int = int(os.getenv("RATE_LIMIT_BURST_SIZE", "5"))

    # Performance Configuration
    MAX_QUESTION_LENGTH: int = int(os.getenv("MAX_QUESTION_LENGTH", "1000"))
    MAX_SELECTED_TEXT_LENGTH: int = int(os.getenv("MAX_SELECTED_TEXT_LENGTH", "5000"))
    RESPONSE_TIMEOUT: int = int(os.getenv("RESPONSE_TIMEOUT", "30"))  # seconds

    # Security Configuration
    ENABLE_RATE_LIMITING: bool = os.getenv("ENABLE_RATE_LIMITING", "true").lower() == "true"
    ENABLE_INPUT_SANITIZATION: bool = os.getenv("ENABLE_INPUT_SANITIZATION", "true").lower() == "true"

    @classmethod
    def validate(cls) -> List[str]:
        """Validate configuration and return list of missing required values"""
        errors = []

        if not cls.GEMINI_API_KEY:
            errors.append("GEMINI_API_KEY is required")

        if not cls.COHERE_API_KEY:
            errors.append("COHERE_API_KEY is required")

        if not cls.QDRANT_URL:
            errors.append("QDRANT_URL is required")

        return errors

    @classmethod
    def setup_logging(cls):
        """Set up logging based on configuration"""
        setup_logging(log_level=cls.LOG_LEVEL, log_file=cls.LOG_FILE)


# Initialize configuration
config = Config()
config.setup_logging()