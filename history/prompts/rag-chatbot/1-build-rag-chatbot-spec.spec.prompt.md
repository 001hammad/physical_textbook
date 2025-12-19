---
id: 1
title: build-rag-chatbot-spec
stage: spec
date: 2025-01-20
surface: agent
model: Claude Sonnet 4.5
feature: rag-chatbot
branch: 001-rag-chatbot
user: Claude-Code
command: /sp.specify
labels: ["spec", "rag", "chatbot", "ai"]
links:
  spec: specs/001-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-rag-chatbot/spec.md
 - specs/001-rag-chatbot/checklists/requirements.md
tests:
 - "Specification quality checklist completed"
---

## Prompt

Build specification for **Phase 2** of the project: a **Retrieval-Augmented Generation (RAG) chatbot** for the book **Physical AI & Humanoid Robotics**. The book has already been completed in Phase 1 and must be treated as **read-only**. This phase is strictly limited to chatbot development.

The chatbot must be implemented using an **agent-based architecture inspired by the OpenAI Agents SDK**. The agent acts as a controller that follows strict instructions, decides when to retrieve information from the book, and generates answers only s → output). The agent must explicitly control when retrieval is allowed and must enforce anti-hallucination constraints at all times.

All AI and infrastructure components must use **free-tier services only**. The chatbot must use a Gemini-based language model for reasoning and response generation, Cohere embeddings for vectorization, and Qdrant Cloud Free Tier for vector storage and retrieval. No paid APIs, billing-required services, or credit-card–dependent services are permitted.

The chatbofrom the provided context. The agent must not rely on general world knowledge outside the book.

All chatbot-related work must live entirely inside a separate `/chatbot` directory. The chatbot must never create, modify, or restructure any files inside the `/book` directory. The book serves solely as the authoritative knowledge source.

The chatbot's core responsibility is to answer user questions **strictly based on the book's content**. If the answer cannot be derived from the book, the agent must respond that the information is not available in the book and must not hallucinate or fabricate responses.

The system must support two explicit interaction modes controlled by the agent:
1. **Normal question mode**, where the agent retrieves the most relevant sections from the book using semantic search and then generates an answer only from those retrieved sections.
2. **Selected-text mode**, where the user provides selected text from the book; in this mode, the agent must bypass global retrieval and generatet backend must be implemented as an API service that can be embedded into the live book website. It must be accessible from the book frontend, respect strict CORS rules tied to the book's domain, and be designed for clean integration without rebuilding or modifying the book.

The overall goal is to deliver a robust, agent-driven RAG chatbot that produces accurate, explainable answers grounded strictly in the book's content, enforces selected-text–only responses when required, and maintains a clean separation between book authoring (Phase 1) and chatbot intelligence (Phase 2).

## Response snapshot

Created a comprehensive feature specification for the RAG chatbot for the Physical AI & Humanoid Robotics book. The specification includes:

- User Scenarios & Testing with 3 prioritized user stories (P1-P3)
- Functional Requirements (10 specific requirements)
- Key Entities (5 entities defined)
- Success Criteria with 5 measurable outcomes
- Edge Cases (6 specific scenarios)
- Quality validation checklist

The specification addresses all requirements from the feature description including:
- Agent-based architecture with anti-hallucination constraints
- Two interaction modes (normal question and selected-text)
- Free-tier service usage (Gemini, Cohere, Qdrant)
- API service with CORS support
- Separation between book content and chatbot functionality

## Outcome

- ✅ Impact: Complete feature specification created for RAG chatbot project
- 🧪 Tests: Specification quality checklist completed and validated
- 📁 Files: spec.md and requirements.md created in specs/001-rag-chatbot/
- 🔁 Next prompts: Ready for planning phase (/sp.plan or /sp.clarify)
- 🧠 Reflection: Specification addresses all core requirements with clear user value

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All validation criteria passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to planning phase