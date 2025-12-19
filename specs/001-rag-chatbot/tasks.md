---
description: "Task list for RAG Chatbot implementation"
---

# Tasks: RAG Chatbot for Physical AI & Humanoid Robotics Book

**Input**: Design documents from `/specs/001-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `chatbot/backend/src/`, `chatbot/backend/tests/`
- Paths shown below follow the structure from plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure in chatbot/backend/
- [x] T002 Initialize Python project using uv with FastAPI, Google Generative AI (Gemini), Cohere, Qdrant dependencies in chatbot/backend/requirements.txt
- [x] T003 [P] Create .gitignore file for Python project in chatbot/backend/.gitignore
- [x] T004 Create .env.example file with API keys in chatbot/backend/.env.example
- [x] T005 Create README.md for the backend in chatbot/backend/README.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Setup configuration loading in chatbot/backend/src/utils/config.py
- [x] T007 [P] Create base models in chatbot/backend/src/models/data_models.py
- [x] T008 Setup Qdrant client connection in chatbot/backend/src/services/retrieval_service.py
- [x] T009 [P] Setup Cohere client connection in chatbot/backend/src/services/embedding_service.py
- [x] T010 [P] Setup Gemini client connection in chatbot/backend/src/services/llm_service.py
- [x] T011 Create FastAPI app structure in chatbot/backend/src/api/main.py
- [x] T012 Configure CORS middleware for https://physical-textbook.vercel.app in chatbot/backend/src/api/main.py
- [x] T013 Setup logging and error handling infrastructure in chatbot/backend/src/utils/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Ask Questions About Book Content (Priority: P1) 🎯 MVP

**Goal**: Enable users to ask questions about the book and receive accurate answers based on book content without hallucination

**Independent Test**: Can be fully tested by asking various questions about the book content and verifying that responses are accurate, relevant, and based only on the book's information without fabricating details.

### Implementation for User Story 1

- [x] T014 [P] Create chat request/response models in chatbot/backend/src/models/chat.py
- [x] T015 Implement RAG agent controller in chatbot/backend/src/agents/rag_agent.py
- [x] T016 Implement embedding service with Cohere in chatbot/backend/src/services/embedding_service.py
- [x] T017 Implement retrieval service with Qdrant in chatbot/backend/src/services/retrieval_service.py
- [x] T018 Implement LLM service with Gemini in chatbot/backend/src/services/llm_service.py
- [x] T019 [US1] Create chat endpoint in chatbot/backend/src/api/routes/chat.py
- [x] T020 [US1] Integrate RAG agent with chat endpoint for normal question mode
- [x] T021 [US1] Add anti-hallucination validation in response generation
- [x] T022 [US1] Add health check endpoint in chatbot/backend/src/api/routes/chat.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Provide Selected Text for Analysis (Priority: P2)

**Goal**: Enable users to provide selected text from the book and get analysis focused only on that text without global retrieval

**Independent Test**: Can be fully tested by providing selected text to the chatbot and verifying that responses are based only on that specific text without retrieving other book sections.

### Implementation for User Story 2

- [x] T023 [P] [US2] Update chat models to support selected-text mode in chatbot/backend/src/models/chat.py
- [x] T024 [US2] Extend RAG agent to handle selected-text mode in chatbot/backend/src/agents/rag_agent.py
- [x] T025 [US2] Implement bypass logic for Qdrant retrieval in selected-text mode
- [x] T026 [US2] Add validation for selected text input
- [x] T027 [US2] Update chat endpoint to handle selected-text mode in chatbot/backend/src/api/routes/chat.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Access Chatbot Through Book Website (Priority: P3)

**Goal**: Ensure the API service is accessible from the book frontend with proper CORS configuration and security measures

**Independent Test**: Can be fully tested by accessing the book website and verifying that the chatbot API is accessible with proper CORS handling and security measures.

### Implementation for User Story 3

- [x] T028 [P] [US3] Add comprehensive CORS configuration in chatbot/backend/src/api/main.py
- [x] T029 [US3] Implement request validation and sanitization in chatbot/backend/src/api/routes/chat.py
- [x] T030 [US3] Add API rate limiting to comply with free-tier usage in chatbot/backend/src/middleware/
- [x] T031 [US3] Add proper error handling for service unavailability in chatbot/backend/src/api/routes/chat.py
- [x] T032 [US3] Add API documentation with Swagger in chatbot/backend/src/api/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T033 [P] Add unit tests for all services in chatbot/backend/tests/unit/
- [x] T034 [P] Add integration tests for API endpoints in chatbot/backend/tests/integration/
- [x] T035 Add documentation updates in chatbot/backend/README.md
- [x] T036 Code cleanup and refactoring across all modules
- [x] T037 Performance optimization for response times under 5 seconds
- [x] T038 [P] Add environment-specific configurations in chatbot/backend/src/utils/config.py
- [x] T039 Security hardening and input validation
- [x] T040 Run quickstart.md validation to ensure setup works as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- All models within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Create chat request/response models in chatbot/backend/src/models/chat.py"
Task: "Create base models in chatbot/backend/src/models/data_models.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence