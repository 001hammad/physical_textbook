import time
import hashlib
from typing import Any, Optional, Dict
from src.utils.logging_config import get_logger
from functools import wraps

logger = get_logger(__name__)


class SimpleCache:
    """
    Simple in-memory cache with TTL (Time To Live)
    """
    def __init__(self, default_ttl: int = 300):  # 5 minutes default
        self.default_ttl = default_ttl
        self._cache: Dict[str, Dict[str, Any]] = {}

    def _generate_key(self, *args, **kwargs) -> str:
        """Generate a unique key for the cache based on arguments"""
        key_data = str(args) + str(sorted(kwargs.items()))
        return hashlib.md5(key_data.encode()).hexdigest()

    def get(self, key: str) -> Optional[Any]:
        """Get a value from the cache if it exists and hasn't expired"""
        if key in self._cache:
            entry = self._cache[key]
            if time.time() < entry['expires_at']:
                logger.debug(f"Cache hit for key: {key[:8]}...")
                return entry['value']
            else:
                # Entry has expired, remove it
                del self._cache[key]
                logger.debug(f"Cache expired for key: {key[:8]}...")

        logger.debug(f"Cache miss for key: {key[:8]}...")
        return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Set a value in the cache with optional TTL"""
        if ttl is None:
            ttl = self.default_ttl

        self._cache[key] = {
            'value': value,
            'expires_at': time.time() + ttl
        }
        logger.debug(f"Cache set for key: {key[:8]}... with TTL: {ttl}s")

    def delete(self, key: str) -> bool:
        """Delete a value from the cache"""
        if key in self._cache:
            del self._cache[key]
            logger.debug(f"Cache deleted for key: {key[:8]}...")
            return True
        return False

    def clear(self) -> None:
        """Clear all cache entries"""
        self._cache.clear()
        logger.debug("Cache cleared")

    def cleanup_expired(self) -> int:
        """Remove all expired entries and return count of removed entries"""
        current_time = time.time()
        initial_count = len(self._cache)

        expired_keys = [
            key for key, entry in self._cache.items()
            if current_time >= entry['expires_at']
        ]

        for key in expired_keys:
            del self._cache[key]

        removed_count = initial_count - len(self._cache)
        if removed_count > 0:
            logger.debug(f"Cleaned up {removed_count} expired cache entries")

        return removed_count


# Global cache instance
cache = SimpleCache(default_ttl=600)  # 10 minutes for most entries


def cached(ttl: Optional[int] = None):
    """
    Decorator to cache function results
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key from function name and arguments
            cache_key = f"{func.__module__}.{func.__name__}:{cache._generate_key(*args, **kwargs)}"

            # Try to get from cache first
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                return cached_result

            # If not in cache, call the function
            result = func(*args, **kwargs)

            # Store in cache
            cache.set(cache_key, result, ttl)

            return result
        return wrapper
    return decorator