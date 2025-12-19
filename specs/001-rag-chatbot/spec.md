# Feature Specification: RAG Chatbot for Physical AI & Humanoid Robotics Book

**Feature Branch**: `001-rag-chatbot`
**Created**: 2025-01-20
**Status**: Draft
**Input**: User description: "Build specification for Phase 2 of the project: a Retrieval-Augmented Generation (RAG) chatbot for the book Physical AI & Humanoid Robotics. The book has already been completed in Phase 1 and must be treated as read-only. This phase is strictly limited to chatbot development. The chatbot must be implemented using an agent-based architecture inspired by the OpenAI Agents SDK. The agent acts as a controller that follows strict instructions, decides when to retrieve information from the book, and generates answers only s → output). The agent must explicitly control when retrieval is allowed and must enforce anti-hallucination constraints at all times. All AI and infrastructure components must use free-tier services only. The chatbot must use a Gemini-based language model for reasoning and response generation, Cohere embeddings for vectorization, and Qdrant Cloud Free Tier for vector storage and retrieval. No paid APIs, billing-required services, or credit-card–dependent services are permitted. The chatbofrom the provided context. The agent must not rely on general world knowledge outside the book. All chatbot-related work must live entirely inside a separate /chatbot directory. The chatbot must never create, modify, or restructure any files inside the /book directory. The book serves solely as the authoritative knowledge source. The chatbot's core responsibility is to answer user questions strictly based on the book's content. If the answer cannot be derived from the book, the agent must respond that the information is not available in the book and must not hallucinate or fabricate responses. The system must support two explicit interaction modes controlled by the agent: 1. Normal question mode, where the agent retrieves the most relevant sections from the book using semantic search and then generates an answer only from those retrieved sections. 2. Selected-text mode, where the user provides selected text from the book; in this mode, the agent must bypass global retrieval and generatet backend must be implemented as an API service that can be embedded into the live book website. It must be accessible from the book frontend, respect strict CORS rules tied to the book's domain, and be designed for clean integration without rebuilding or modifying the book. The overall goal is to deliver a robust, agent-driven RAG chatbot that produces accurate, explainable answers grounded strictly in the book's content, enforces selected-text–only responses when required, and maintains a clean separation between book authoring (Phase 1) and chatbot intelligence (Phase 2)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask Questions About Book Content (Priority: P1)

A user wants to ask questions about Physical AI & Humanoid Robotics and receive accurate answers based on the book's content. The user interacts with the chatbot through a web interface and receives responses that are grounded in the book's content without hallucination.

**Why this priority**: This is the core functionality of the chatbot - users need to be able to ask questions and get accurate, reliable answers from the book content.

**Independent Test**: Can be fully tested by asking various questions about the book content and verifying that responses are accurate, relevant, and based only on the book's information without fabricating details.

**Acceptance Scenarios**:

1. **Given** a user has access to the chatbot interface, **When** the user asks a question about Physical AI concepts from the book, **Then** the chatbot retrieves relevant sections and provides an accurate answer based only on the book's content
2. **Given** a user asks a question that cannot be answered from the book's content, **When** the user submits the question, **Then** the chatbot responds that the information is not available in the book and does not hallucinate an answer

---

### User Story 2 - Provide Selected Text for Analysis (Priority: P2)

A user selects specific text from the book and wants the chatbot to analyze or elaborate on that specific content without performing global retrieval. The user expects the chatbot to focus only on the provided text.

**Why this priority**: This provides an alternative interaction mode that allows users to get focused analysis on specific passages they're interested in.

**Independent Test**: Can be fully tested by providing selected text to the chatbot and verifying that responses are based only on that specific text without retrieving other book sections.

**Acceptance Scenarios**:

1. **Given** a user has selected text from the book, **When** the user submits the selected text with a question, **Then** the chatbot generates a response based only on the provided text without performing global retrieval

---

### User Story 3 - Access Chatbot Through Book Website (Priority: P3)

A user accesses the book website and interacts with the embedded chatbot API service. The user expects seamless integration with the book's frontend while maintaining proper security boundaries.

**Why this priority**: This ensures the chatbot integrates properly with the existing book website without requiring modifications to the book itself.

**Independent Test**: Can be fully tested by accessing the book website and verifying that the chatbot API is accessible with proper CORS handling and security measures.

**Acceptance Scenarios**:

1. **Given** a user is on the book website, **When** the user interacts with the embedded chatbot, **Then** the API responds correctly with appropriate CORS headers and security measures in place

---

### Edge Cases

- What happens when the book content has not been properly indexed in the vector database?
- How does the system handle malformed user queries or extremely long input?
- What occurs when the vector database is temporarily unavailable?
- How does the system respond when users try to ask about topics outside the book's scope?
- What happens when the Gemini API is temporarily unavailable?
- How does the system handle simultaneous requests from multiple users?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST answer user questions strictly based on the book's content without hallucinating or fabricating information
- **FR-002**: System MUST implement two interaction modes: normal question mode with semantic search and selected-text mode that bypasses global retrieval
- **FR-003**: Users MUST be able to ask questions about Physical AI & Humanoid Robotics and receive accurate, contextual responses
- **FR-004**: System MUST use an agent-based architecture that controls when retrieval is allowed and enforces anti-hallucination constraints
- **FR-005**: System MUST integrate with free-tier services only (Gemini for reasoning, Cohere for embeddings, Qdrant Cloud Free Tier for vector storage and use uv package manager ) - Create Python virtual environment and install dependencies for backend using `requirements.txt`.
- Run the FastAPI backend with Uvicorn.
- **FR-006**: System MUST be accessible via an API service that can be embedded into the book website with proper CORS configuration
- **FR-007**: System MUST maintain complete separation between book content (read-only) and chatbot functionality (in /chatbot directory)
- **FR-008**: System MUST provide clear responses when requested information is not available in the book
- **FR-009**: System MUST ensure responses are generated only from retrieved/relevant book sections without using general world knowledge
- **FR-010**: System MUST handle error conditions gracefully and provide informative feedback to users

### Key Entities

- **Book Content**: The authoritative knowledge source for the Physical AI & Humanoid Robotics book, treated as read-only and used exclusively for grounding responses
- **User Query**: Input from users seeking information about the book's content, which triggers the RAG process
- **Retrieved Context**: Relevant sections of the book content retrieved based on semantic similarity to the user's query
- **Agent Response**: The final output generated by the system based on the retrieved context, strictly adhering to anti-hallucination constraints
- **Chatbot Session**: Interaction state between user and the RAG system, maintaining context for the conversation

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can ask questions about Physical AI & Humanoid Robotics and receive accurate answers based solely on book content within 5 seconds response time
- **SC-002**: The system correctly identifies when requested information is not available in the book and responds appropriately 95% of the time
- **SC-003**: 90% of user questions receive relevant, accurate responses that are grounded in the book's content without hallucination
- **SC-004**: The API service maintains 99% uptime and responds to requests with proper CORS headers for seamless integration with the book website
- **SC-005**: The system processes selected-text mode queries by focusing only on provided text without performing global retrieval 100% of the time
