<!-- Sync Impact Report:
Version change: 1.0.0 → 1.1.0
Modified principles: Added UI/Design principles section
Added sections: UI/Design Principles section
Removed sections: None
Templates requiring updates: ⚠ pending (templates may need UI guidelines)
Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics — Spec-Driven Book + RAG Chatbot Constitution

## Core Principles

### Strict Project Separation
The project is strictly divided into two independent parts: the BOOK and the CHATBOT. The book is content-only; the chatbot is logic-only. This separation ensures clear responsibilities, maintainable code, and independent development cycles.

### Book Technology Constraint
The BOOK must be created and managed exclusively using Docusaurus and Markdown. No backend, no chatbot code, and no API logic is allowed inside the book. This ensures the book remains accessible, lightweight, and focused solely on content delivery.

### Chatbot Independence
The CHATBOT must be developed separately in its own folder and must never modify, generate, or restructure book files directly. This maintains clean separation of concerns and prevents coupling between content and logic layers.

### Docusaurus Initialization Requirement
The book project MUST be created by running the Docusaurus initializer command inside the `/book` directory only:
`npx create-docusaurus@latest . classic`
This ensures consistent project structure and avoids manual configuration errors.

### Official Template Compliance
Docusaurus project files MUST NOT be manually created, copied, or restructured. All required files must come only from the official Docusaurus initializer. This maintains compatibility with Docusaurus ecosystem and reduces maintenance overhead.

### Forbidden Project Creation Method
The project must NEVER be created using `npx create-docusaurus@latest book classic`. This prevents incorrect directory nesting and maintains proper project organization.

### Book Folder Authority
The `/book` folder is the Docusaurus project root and contains all configuration, docs, and content. All book-related assets must reside within this boundary.

### Chatbot Isolation
The chatbot MUST live in a completely separate `/chatbot` folder and must not share runtime, config, or source files with the book. This enables independent deployment and scaling strategies.

## Content & Authoring Rules

### Markdown-Only Content
The book is written in Markdown only and organized as modules and chapters. This ensures content portability and simplicity of authoring process.

### Chapter Structure Constraint
Each chapter is a single page and may contain multiple collapsible (accordion-style) sections using Markdown-native mechanisms. No chapter content may be split into multiple pages to simulate accordion behavior. This maintains clear content organization and navigation.

### Consistency Requirement
Consistent tone, terminology, and structure must be maintained across all chapters. This ensures professional quality and coherent user experience throughout the book.

## Process & Phase Enforcement

### Sequential Phase Execution
Phase 1 is BOOK ONLY. No chatbot planning, references, files, or code are allowed during Phase 1. This ensures focused development and prevents scope creep.

### Dependency-Based Start
Phase 2 is CHATBOT ONLY and may begin only after Phase 1 is fully completed and approved. This maintains proper sequencing and validates the book foundation before building the chatbot.

### Workflow Adherence
The Spec-Kit Plus workflow must be followed strictly in order: constitution → specify → plan → tasks → implement. This ensures systematic development and proper documentation.

### No Step Skipping
Skipping steps, merging phases, or assuming implementation details before the plan stage is not allowed. This preserves the integrity of the spec-driven development process.

## UI/Design Principles

### Premium VIP UI Aesthetic
The project must implement a futuristic neon cyberpunk look with heavy glow effects and smooth transitions. This creates a distinctive, premium visual identity that engages users and sets the project apart from conventional interfaces.

### Color Scheme Standard
Dark mode must use #09091f as the background color with #33fcff neon cyan for text, accents, borders, and glow effects. Light mode must maintain the existing toggle functionality with white/light backgrounds and cyan accents. This ensures consistent visual branding across both themes.

### Interactive Element Behavior
All interactive elements (links, buttons, sidebar items) must have hover glow and lift transitions. This creates a responsive, engaging user experience that reinforces the premium aesthetic.

### Visual Effects Standards
Headings must feature neon text-shadow with pulse animation, code blocks must have cyan border glow with line numbers, and sidebar items must have hover shift with glow. The navbar and footer must include subtle glow borders, and hero banners must feature big glowing titles. This ensures consistent application of the cyberpunk aesthetic across all components.

### Transition Specifications
All interactive elements must use 0.3s-0.4s ease transitions on hover/focus states. This creates smooth, polished animations that enhance the premium feel of the interface.

## Success Criteria

### Book Functionality
The book builds and runs successfully using Docusaurus without manual fixes. This validates the proper initialization and configuration.

### Structural Integrity
The folder separation between `/book` and `/chatbot` is strictly enforced. This confirms adherence to architectural constraints.

### Initialization Quality
Zero reinitialization errors; the project initializes correctly on the first run. This ensures reproducible setup for team members.

### Process Compliance
The workflow remains spec-driven and predictable without repeated project resets. This validates the effectiveness of the development methodology.

## Governance

### Amendment Procedure
Changes to this constitution require unanimous agreement from all core contributors. Amendments must be documented with clear rationale and impact assessment.

### Versioning Policy
- MAJOR: Backward incompatible governance/principle removals or redefinitions
- MINOR: New principle/section added or materially expanded guidance
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements

### Compliance Review
Regular compliance reviews should be conducted at the end of each phase to ensure continued adherence to constitutional principles.

**Version**: 1.1.0 | **Ratified**: 2025-12-18 | **Last Amended**: 2025-12-22
