import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging(log_level: str = "INFO", log_file: str = None):
    """
    Set up comprehensive logging configuration for the application
    """
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level.upper()))

    # Clear any existing handlers
    logger.handlers = []

    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)

    # File handler (if specified)
    if log_file:
        # Create directory if it doesn't exist
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5
        )
        file_handler.setFormatter(detailed_formatter)
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str):
    """
    Get a logger with the specified name
    """
    return logging.getLogger(name)


# Custom exception classes
class RAGChatbotError(Exception):
    """Base exception class for RAG Chatbot application"""
    pass


class ConfigurationError(RAGChatbotError):
    """Raised when there's an issue with application configuration"""
    pass


class ServiceError(RAGChatbotError):
    """Raised when there's an issue with a service (API, database, etc.)"""
    pass


class ValidationError(RAGChatbotError):
    """Raised when validation fails"""
    pass


class ContentNotFoundError(RAGChatbotError):
    """Raised when requested content is not found"""
    pass