# Research Summary: RAG Chatbot Implementation

## Decision: Agent Architecture Pattern
**Rationale**: Using an OpenAI Agents SDK-inspired pattern (Instructions → Context → Tool calls → Output) provides a clear, structured approach to implementing the RAG chatbot. This pattern allows the agent to control when retrieval is allowed and enforce anti-hallucination constraints effectively.

**Alternatives considered**:
- Direct API calls without agent abstraction
- Simple function chaining approach
- The agent-based approach was chosen for its explicit control over the RAG process and ability to enforce constraints.

## Decision: Technology Stack
**Rationale**:
- FastAPI for backend: Provides excellent performance, automatic API documentation, and async support
- Gemini (gemini-1.5-flash) for LLM: Meets free-tier requirement and provides good performance for response generation
- Cohere embeddings: Reliable embedding service with free tier that works well with book content
- Qdrant Cloud Free Tier: Efficient vector database with good Python integration

**Alternatives considered**:
- Other LLMs (OpenAI, Anthropic): Don't meet free-tier requirement
- Other vector databases (Pinecone, Weaviate): May not have suitable free tiers
- Other frameworks (Flask, Django): Don't provide the same performance and features as FastAPI

## Decision: Two Interaction Modes Implementation
**Rationale**: Implementing both normal question mode and selected-text mode as separate API endpoints or with mode detection allows clear separation of concerns and proper enforcement of the different behaviors required by the specification.

**Alternatives considered**:
- Single endpoint with mode parameter
- The approach with clear mode separation was chosen for better maintainability and constraint enforcement

## Decision: Project Structure
**Rationale**: Separating backend and frontend into distinct directories maintains clear boundaries and allows independent development, testing, and deployment. The backend handles all RAG logic while the frontend provides the UI for the book website.

**Alternatives considered**:
- Monolithic structure: Would blur the lines between different concerns
- The separated approach was chosen to maintain the required separation between book and chatbot

## Best Practices for Free-Tier Compliance
- Implement proper rate limiting to stay within API limits
- Add retry mechanisms with exponential backoff for API calls
- Cache embeddings where possible to reduce API usage
- Monitor API usage and set up alerts for approaching limits
- Implement graceful degradation when services are unavailable

## Integration Patterns
- Use environment variables for API keys and configuration
- Implement proper error handling and user feedback for API failures
- Design API with CORS in mind from the start
- Use async/await for I/O operations to maximize throughput
- Implement proper request validation and sanitization