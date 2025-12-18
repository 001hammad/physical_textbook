---
id: 1
title: Create Project Constitution
stage: constitution
date: 2025-12-18
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: USER
command: /sp.constitution
labels: [constitution,spec,project-setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
 made project constitution Project: Physical AI & Humanoid Robotics — Spec-Driven Book + RAG Chatbot

Core Principles:
- This project is strictly divided into two independent parts: the BOOK and the CHATBOT. The book is content-only; the chatbot is logic-only.
- The BOOK must be created and managed exclusively using Docusaurus and Markdown. No backend, no chatbot code, and no API logic is allowed inside the book.
- The CHATBOT must be developed separately in its own folder and must never modify, generate, or restructure book files directly.

Non-Negotiable Structural Rules:
- The book project MUST be created by running the Docusaurus initializer command inside the `/book` directory only:
  `npx create-docusaurus@latest . classic`
- Docusaurus project files MUST NOT be manually created, copied, or restructured. All required files must come only from the official Docusaurus initializer.
- The project must NEVER be created using `npx create-docusaurus@latest book classic`.
- The `/book` folder is the Docusaurus project root and contains all configuration, docs, and content.
- The chatbot MUST live in a completely separate `/chatbot` folder and must not share runtime, config, or source files with the book.

Content & Authoring Rules:
- The book is written in Markdown  only and organized as modules and chapters.
- Each chapter is a single page and may contain multiple collapsible (accordion-style) sections using Markdown-native mechanisms.
- No chapter content may be split into multiple pages to simulate accordion behavior.
- Consistent tone, terminology, and structure must be maintained across all chapters.

Process & Phase Enforcement:
- Phase 1 is BOOK ONLY. No chatbot planning, references, files, or code are allowed during Phase 1.
- Phase 2 is CHATBOT ONLY and may begin only after Phase 1 is fully completed and approved.
- The Spec-Kit Plus workflow must be followed strictly in order: constitution → specify → plan → tasks → implement.
- Skipping steps, merging phases, or assuming implementation details before the plan stage is not allowed.

Success Criteria:
- The book builds and runs successfully using Docusaurus without manual fixes.
- The folder separation between `/book` and `/chatbot` is strictly enforced.
- Zero reinitialization errors; the project initializes correctly on the first run.
- The workflow remains spec-driven and predictable without repeated project resets.
```

## Response snapshot

Created the project constitution file (.specify/memory/constitution.md) with all specified principles, structural rules, content & authoring rules, process enforcement rules, and success criteria. The constitution enforces strict separation between the book and chatbot components, mandates Docusaurus for the book, and defines clear development phases and workflows.

## Outcome

- ✅ Impact: Created project constitution with all specified principles and governance rules
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with project-specific rules
- 🔁 Next prompts: Proceed with /sp.specify to define feature specifications
- 🧠 Reflection: Constitution successfully captures all project constraints and principles

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS - all constitutional requirements implemented
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification phase