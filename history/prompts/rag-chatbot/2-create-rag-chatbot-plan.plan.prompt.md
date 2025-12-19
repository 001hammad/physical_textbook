---
id: 2
title: create-rag-chatbot-plan
stage: plan
date: 2025-01-20
surface: agent
model: Claude Sonnet 4.5
feature: rag-chatbot
branch: 001-rag-chatbot
user: Claude-Code
command: /sp.plan
labels: ["plan", "rag", "chatbot", "ai", "architecture"]
links:
  spec: specs/001-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-rag-chatbot/plan.md
 - specs/001-rag-chatbot/research.md
 - specs/001-rag-chatbot/data-model.md
 - specs/001-rag-chatbot/quickstart.md
 - specs/001-rag-chatbot/contracts/chat-api.yaml
tests:
 - "Constitution compliance check passed"
 - "API contract validation completed"
 - "Data model validation completed"
---

## Prompt

Create a technical implementation plan for Phase-2: the RAG chatbot for the book "Physical AI & Humanoid Robotics". Follow these guidelines:

 **Agent Architecture**
- Agent acts as the main controller.
- Uses OpenAI Agents SDK-inspired pattern:
- Instructions → Context → Tool calls → Output
- Tools include:
- **Retriever** → fetches relevant book sections from Qdrant
- **Embedding generator** → Cohere embeddings for vectorization
- **LLM responder** → Gemini model for answer generation
- Agent enforces:
- Selected-text mode
- No hallucinations
- Answer strictly from book content

 **Vector Database**
- Qdrant Free Tier
- Collection: `book-collection`
- Stores embeddings for all book sections

 **Embeddings**
- Use Cohere free-tier embeddings
- Index each book section separately

 **LLM**
- Gemini model (`gemini-1.5-flash`)
- Generates answers from retrieved sections
- Max tokens per response: 512 (configurable)

**Backend**
- FastAPI-based REST API
- Endpoints:
- `/chat` → receives user question + optional selected text
- `/status` → health check
- and as per need create endpoints
- CORS restricted to `https://physical-textbook.vercel.app`
- Local URL for development: `http://localhost:8000`

**Frontend Integration**
- Chat UI embedded in book site
- Sends questions + selected text to FastAPI backend
- Displays responses from agent

**Free-tier compliance**
- Gemini LLM (free)
- Cohere embeddings (free)
- Qdrant Cloud (free)
- No paid services, no billing keys

**Configuration**
- `.env` file for env variables

## Response snapshot

Created a comprehensive technical implementation plan for the RAG chatbot including:

- Detailed technical context with Python 3.11, FastAPI, and free-tier services
- Constitution compliance check confirming alignment with project principles
- Complete project structure with backend and frontend components
- Research summary with technology decisions and best practices
- Data models for all core entities (BookContent, UserQuery, RetrievedContext, etc.)
- API contract (OpenAPI spec) for the chat endpoint
- Quickstart guide with setup and usage instructions
- Agent context updated with new technologies

The plan addresses all requirements including:
- Agent-based architecture with anti-hallucination constraints
- Two interaction modes (normal question and selected-text)
- Free-tier service usage (Gemini, Cohere, Qdrant)
- API service with CORS support
- Complete separation between book content and chatbot functionality

## Outcome

- ✅ Impact: Complete technical implementation plan created for RAG chatbot project
- 🧪 Tests: Constitution compliance, API contract, and data model validations completed
- 📁 Files: plan.md, research.md, data-model.md, quickstart.md, and API contract created
- 🔁 Next prompts: Ready for task generation phase (/sp.tasks)
- 🧠 Reflection: Plan provides clear roadmap for implementation with all technical details

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All validation criteria passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to task generation phase