# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

## Prerequisites

- Node.js (LTS version recommended)
- npm or yarn package manager
- Git (for version control)

## Setup Instructions

### 1. Initialize the Book Project

First, create the book directory and navigate into it:

```bash
mkdir book
cd book
```

Then initialize the Docusaurus project using the official command:

```bash
npx create-docusaurus@latest . classic
```

### 2. Verify Installation

Start the development server to ensure everything is working:

```bash
npm start
```

You should see the default Docusaurus site running on `http://localhost:3000`.

### 3. Create Module 1 Structure

Create the directory structure for Module 1:

```bash
mkdir -p docs/module1
```

### 4. Create the Four Chapters

Create the four required chapters for Module 1:

```bash
touch docs/module1/chapter1.md
touch docs/module1/chapter2.md
touch docs/module1/chapter3.md
touch docs/module1/chapter4.md
```

### 5. Add Content with Collapsible Sections

Edit each chapter file to include content with collapsible sections. Example for chapter1.md:

```markdown
---
sidebar_position: 1
---

# Chapter 1: Introduction to Physical AI & Humanoid Robotics

This chapter introduces the fundamental concepts of Physical AI and Humanoid Robotics.

<details>
<summary>What is Physical AI?</summary>

Physical AI refers to artificial intelligence systems that interact with the physical world through sensors and actuators...

</details>

<details>
<summary>History of Humanoid Robotics</summary>

The development of humanoid robots has evolved significantly since the early 20th century...

</details>

<details>
<summary>Key Technologies</summary>

Several key technologies enable modern Physical AI and Humanoid Robotics...

</details>
```

### 6. Update Navigation

Add the module and chapters to your sidebar by editing `sidebars.js`:

```javascript
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Module 1',
      items: ['module1/chapter1', 'module1/chapter2', 'module1/chapter3', 'module1/chapter4'],
    },
  ],
};
```

### 7. Build and Deploy

To build the static site:

```bash
npm run build
```

The built site will be available in the `build/` directory.

## Development Workflow

1. Run `npm start` to start the development server
2. Edit Markdown files in the `docs/` directory
3. Changes will automatically reload in the browser
4. Use collapsible sections (details/summary HTML elements) for organized content
5. Test functionality regularly to ensure all sections work correctly