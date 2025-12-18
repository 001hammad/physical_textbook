# Data Model: Physical AI & Humanoid Robotics Textbook - Module 1

## Entity: Book Project
- **Description**: The Docusaurus-based textbook structure containing modules and chapters
- **Attributes**:
  - title: "Physical AI & Humanoid Robotics"
  - version: Current version of the textbook
  - modules: Collection of modules in the book
  - configuration: Docusaurus configuration settings
- **Validation**: Must be initialized using official Docusaurus command only
- **Relationships**: Contains multiple modules

## Entity: Module
- **Description**: A major section of the textbook containing related chapters
- **Attributes**:
  - id: Unique identifier for the module
  - title: Title of the module
  - description: Brief description of the module content
  - chapters: Collection of chapters in the module
- **Validation**: Must contain exactly 4 chapters for Module 1
- **Relationships**: Contains multiple chapters; belongs to a book project

## Entity: Chapter
- **Description**: Individual content pages within the book, each containing multiple collapsible sections
- **Attributes**:
  - id: Unique identifier for the chapter
  - title: Title of the chapter
  - content: Main content of the chapter
  - sections: Collection of collapsible sections
  - position: Order within the module
- **Validation**: Must be a single page as per requirements
- **Relationships**: Contains multiple sections; belongs to a module

## Entity: Collapsible Section
- **Description**: Expandable/collapsible content blocks within chapters that organize information hierarchically
- **Attributes**:
  - title: Title of the section (acts as header)
  - content: Content that is shown/hidden
  - isExpanded: Boolean indicating if section is currently expanded
  - position: Order within the chapter
- **Validation**: Must remain on the same page as parent chapter
- **Relationships**: Belongs to a chapter