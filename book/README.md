# Physical AI & Humanoid Robotics Textbook

This textbook provides an introduction to Physical AI and Humanoid Robotics, covering fundamental concepts, design principles, and applications.

## About This Book

This textbook is organized into modules, with each module containing several chapters. Each chapter explores specific aspects of Physical AI and Humanoid Robotics with collapsible sections for detailed exploration of complex topics.

## Module 1: Foundations

Module 1 contains four chapters that introduce the fundamental concepts:

- Chapter 1: Introduction to Physical AI & Humanoid Robotics
- Chapter 2: Fundamentals of Physical AI
- Chapter 3: Humanoid Robot Design Principles
- Chapter 4: Applications and Future of Physical AI

## Module 2: Intermediate Concepts

Module 2 contains four chapters that build upon the foundational concepts with intermediate-level content:

- Chapter 1: Advanced Sensor Fusion and Perception Systems
- Chapter 2: Advanced Control Systems and Motion Planning
- Chapter 3: Machine Learning for Physical AI
- Chapter 4: Human-Robot Interaction and Social Robotics

## Module 3: Advanced Concepts

Module 3 contains four chapters focusing on advanced research-level topics that require knowledge from Modules 1 and 2:

- Chapter 1: Advanced Sensor Fusion and Perception
- Chapter 2: Advanced Control Systems
- Chapter 3: Advanced Machine Learning for Physical AI
- Chapter 4: Advanced Human-Robot Interaction and Social Robotics

## Navigation

Each chapter includes collapsible sections that allow for organized exploration of complex topics. Use the sidebar navigation to access different chapters and modules.

## Installation

```bash
yarn
```

## Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
yarn build
```

This command generates static content into the build directory and can be served using any static contents hosting service.

## Deployment

Using SSH:

```bash
USE_SSH=true yarn deploy
```

Not using SSH:

```bash
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.