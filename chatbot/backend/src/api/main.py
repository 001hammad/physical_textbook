from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from src.api.routes import chat
from src.utils.config import config
from src.middleware import rate_limit_middleware, security_headers_middleware
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app instance
app = FastAPI(
    title="RAG Chatbot API for Physical AI & Humanoid Robotics Book",
    description="API for the RAG chatbot that answers questions based on book content with anti-hallucination constraints",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI endpoint
    redoc_url="/redoc",  # ReDoc endpoint
    openapi_url="/openapi.json",  # OpenAPI schema endpoint
    # Additional security settings
    swagger_ui_parameters={"docExpansion": "none"}  # Hide API documentation by default
)

# Add security-related headers and configurations

# Add security headers middleware first (applied to all responses)
app.add_middleware(security_headers_middleware)

# Add rate limiting middleware
app.middleware("http")(rate_limit_middleware)

# Add trusted host middleware to prevent HTTP Host Header attacks
# Only allow the configured CORS origins as valid hosts
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=config.CORS_ORIGINS + ["localhost", "127.0.0.1", "[::1]"]
)

# Configure comprehensive CORS middleware for the book website
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # More specific than ["*"]
    allow_headers=["*"],  # Allow all headers including custom ones
    # Expose headers to client-side JavaScript
    expose_headers=["Access-Control-Allow-Origin", "Access-Control-Allow-Credentials",
                    "X-Response-Time", "X-Response-ID"]
)

# Include chat routes
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])

# Add a root endpoint for basic health check
@app.get("/")
def read_root():
    return {"message": "RAG Chatbot API for Physical AI & Humanoid Robotics Book"}

# Add a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}

# Additional configuration can be added here if needed
logger.info("FastAPI app initialized with CORS configuration")