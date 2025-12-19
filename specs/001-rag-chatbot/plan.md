# Implementation Plan: RAG Chatbot for Physical AI & Humanoid Robotics Book

**Branch**: `001-rag-chatbot` | **Date**: 2025-01-20 | **Spec**: [link](spec.md)
**Input**: Feature specification from `/specs/001-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a Retrieval-Augmented Generation (RAG) chatbot for the Physical AI & Humanoid Robotics book using an agent-based architecture. The system will use Gemini for response generation, Cohere for embeddings, and Qdrant for vector storage, all using free-tier services. The backend will be built with FastAPI and include endpoints for chat interactions with strict anti-hallucination constraints to ensure responses are grounded only in book content.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, Google Generative AI (Gemini), Cohere, Qdrant, python-dotenv
**Storage**: Qdrant Cloud Free Tier (vector database), local book content files (read-only)
**Testing**: pytest for unit and integration tests
**Target Platform**: Windows server environment
**Project Type**: web (backend API with potential frontend integration)
**Performance Goals**: <5 second response time for user queries
**Constraints**: Must use only free-tier services, no billing/credit card required, strict anti-hallucination to use only book content
**Scale/Scope**: Support multiple concurrent users, handle book content of moderate size

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Constitution Alignment Check:**
- ✅ Strict Project Separation: Chatbot will be in separate `/chatbot` directory, not modifying book files
- ✅ Book Technology Constraint: Book remains as Docusaurus/Markdown only, no backend code in book
- ✅ Chatbot Independence: Chatbot operates independently with its own folder structure
- ✅ Forbidden Project Creation Method: Not applicable - we're creating chatbot, not book
- ✅ Book Folder Authority: Respecting book as read-only source of truth
- ✅ Chatbot Isolation: Chatbot will be in separate directory with no shared runtime files

**Compliance Status**: All constitutional principles are satisfied. The implementation plan fully aligns with the project constitution.

**Post-Design Re-check:**
- ✅ Data models respect book content as read-only source
- ✅ API design maintains separation between book and chatbot
- ✅ Architecture enforces anti-hallucination constraints as required
- ✅ Free-tier service usage confirmed in all components
- ✅ CORS restrictions properly specified for book website integration

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
chatbot/
├── backend/
│   ├── src/
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   └── rag_agent.py          # Agent controller with OpenAI Agents SDK-inspired pattern
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # FastAPI app and endpoints
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       └── chat.py           # Chat endpoints
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── chat.py               # Chat request/response models
│   │   │   └── data_models.py        # Core data models
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── embedding_service.py  # Cohere embedding generation
│   │   │   ├── retrieval_service.py  # Qdrant vector retrieval
│   │   │   └── llm_service.py        # Gemini response generation
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── config.py             # Configuration loading
│   │   └── __init__.py
│   ├── tests/
│   │   ├── unit/
│   │   │   ├── test_agents/
│   │   │   ├── test_services/
│   │   │   └── test_api/
│   │   └── integration/
│   │       └── test_end_to_end.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   └── README.md
```

**Structure Decision**: The project will use a web application structure with separate backend directories. The backend will be built with FastAPI to provide the API service for the RAG chatbot, using the agent-based architecture pattern. The structure ensures complete separation between the book and chatbot as required by the constitution.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |
