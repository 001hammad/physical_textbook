---
sidebar_position: 2
---

# Content Creation Workflow

This document outlines the workflow for creating and maintaining content in the Physical AI & Humanoid Robotics textbook.

## Chapter Structure

Each chapter in Module 1 follows a consistent structure:

1. **Frontmatter**: Contains metadata like sidebar position
2. **Main Title**: Follows the format "Chapter X: [Title]"
3. **Collapsible Sections**: Use details/summary HTML elements for organized content

## Creating New Content

### Adding a New Chapter

To add a new chapter to Module 1:

1. Create a new Markdown file in `docs/module1/`
2. Add frontmatter with the appropriate sidebar_position
3. Use the H1 heading for the chapter title
4. Include collapsible sections using details/summary elements

### Creating Collapsible Sections

Use the following format for collapsible sections:

```html
<details>
<summary>Section Title</summary>

Content goes here...

</details>
```

### Best Practices

- Keep section titles concise and descriptive
- Ensure content is beginner-friendly while maintaining technical accuracy
- Use consistent terminology across all chapters
- Maintain the same structural patterns in all chapters
- Include at least 3 collapsible sections per chapter for better organization