# Premium VIP Neon Theme Specification

## Overview
Update only the UI styling of the existing Docusaurus book site to VIP premium neon theme while preserving all content, pages, and structure. The goal is to create an engaging, modern, high-tech feel that matches the Physical AI & Humanoid Robotics theme.

## Scope
- Update global styling to futuristic neon cyberpunk aesthetic
- Apply consistent color scheme and glow effects
- Enhance interactive elements with animations and transitions
- Maintain all existing content and site structure
- Preserve dark/light mode toggle functionality

## Requirements

### 1. Color Scheme
- **Dark mode background**: #09091f across all pages and components
- **Accent color**: #33fcff cyan for all links, buttons, borders, headings, and highlights
- **Light mode**: White/light backgrounds with cyan accents (preserve existing toggle)

### 2. Glow Effects
- Apply strong glow effects using box-shadow and text-shadow with #33fcff
- Glow effects activate on hover/focus states for interactive elements
- Add subtle constant glow to key elements like titles and buttons

### 3. Transitions
- Apply 0.3s ease transitions to all interactive elements
- Smooth animations for hover, focus, and active states

### 4. Sidebar Styling
- Items should lift slightly and glow on hover
- Active/current item highlighted with cyan border
- Preserve existing functionality and structure

### 5. Navigation Bar
- Logo/title with subtle glow effect
- Links with hover glow effects
- Maintain existing layout and functionality

### 6. Content Area
- Headings with large size and neon shadow effects
- Paragraphs maintain readability with appropriate contrast
- Code blocks with cyan glow border
- Preserve all existing content formatting

### 7. Footer
- Centered text with cyan glow effects
- Links with hover effects
- Maintain existing layout

### 8. Responsive Design
- Ensure all effects work properly on mobile devices
- Maintain readability and usability on all screen sizes
- Optimize glow effects for performance on mobile

### 9. Animation Effects
- Add subtle pulse/glow animations to key elements (titles, buttons)
- Ensure animations are smooth and don't impact performance
- Use CSS animations for effects

## Constraints
- Do not change any book content, pages, or structure
- Do not modify the dark/light mode toggle functionality
- Maintain all existing navigation and site functionality
- Preserve accessibility features
- Keep performance optimal

## Success Criteria
- Entire site has consistent futuristic neon cyberpunk aesthetic
- All interactive elements have glow and transition effects
- Dark/light mode toggle continues to work as before
- Site remains responsive and accessible
- All existing content and structure preserved
- Visual effects work smoothly across all devices

## Non-functional Requirements
- Performance: All animations and effects should maintain 60fps
- Accessibility: Maintain WCAG compliance for color contrast and interaction
- Compatibility: Work consistently across modern browsers
- Maintainability: Use modular CSS that's easy to update