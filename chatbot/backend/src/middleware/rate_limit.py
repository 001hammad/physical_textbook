import time
from typing import Dict
from collections import defaultdict
from fastapi import Request, HTTPException
from src.utils.logging_config import get_logger
from src.utils.config import config

logger = get_logger(__name__)


class RateLimiter:
    """
    Simple in-memory rate limiter to comply with free-tier usage limits
    """
    def __init__(self, requests_per_minute: int = 30, burst_size: int = 5):
        self.requests_per_minute = requests_per_minute
        self.burst_size = burst_size
        self.requests: Dict[str, list] = defaultdict(list)

    def is_allowed(self, identifier: str) -> bool:
        """
        Check if a request from the given identifier is allowed
        """
        current_time = time.time()

        # Clean old requests (older than 1 minute)
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier]
            if current_time - req_time < 60
        ]

        # Check burst limit (requests within a short time window)
        recent_requests = [
            req_time for req_time in self.requests[identifier]
            if current_time - req_time < 1  # Within last second
        ]

        if len(recent_requests) >= self.burst_size:
            logger.warning(f"Rate limit exceeded for {identifier} (burst limit)")
            return False

        # Check overall rate limit
        if len(self.requests[identifier]) >= self.requests_per_minute:
            logger.warning(f"Rate limit exceeded for {identifier} (minute limit)")
            return False

        # Add current request
        self.requests[identifier].append(current_time)
        return True


from src.utils.config import config

# Create a global rate limiter instance
rate_limiter = RateLimiter(
    requests_per_minute=config.RATE_LIMIT_REQUESTS_PER_MINUTE,
    burst_size=config.RATE_LIMIT_BURST_SIZE
)  # Limits from configuration


async def rate_limit_middleware(request: Request, call_next):
    """
    Middleware function to apply rate limiting
    """
    # Get client IP address
    client_ip = request.client.host if request.client else "unknown"

    # For API endpoints that need rate limiting
    if request.url.path.startswith("/api/v1/chat"):
        if not rate_limiter.is_allowed(client_ip):
            logger.warning(f"Rate limited request from {client_ip} for {request.url.path}")
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please try again later."
            )

    response = await call_next(request)
    return response