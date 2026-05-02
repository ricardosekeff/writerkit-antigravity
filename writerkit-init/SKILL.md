---
name: writerkit-init
description: Use when the user wants to start, plan, write, or publish technical and scientific books in LaTeX, requiring end-to-end orchestration of the production lifecycle.
metadata:
  triggers: technical books, LaTeX, scientific writing, book production, academic references
---

# Producing Technical Books (WriterKit)

## Overview
This skill orchestrates the full lifecycle of technical book production, from initial setup and planning to final publication. It manages a sequence of specialized sub-skills to ensure academic rigor, technical accuracy, and LaTeX compatibility.

## When to Use This Skill
- Starting a new technical or scientific book project.
- Producing a complete chapter following a structured workflow.
- Ensuring code examples are correctly rendered in LaTeX (accent mapping).
- Validating academic references against real-world databases.

## How to Use It
The workflow is divided into 8 mandatory phases. **Phase 0 is required once per project.**

0. **Initialization** (`writerkit-init`): **MANDATORY FIRST STEP.** 
   - Copy the `/home/sekeff/.gemini/antigravity/skills/writerkit-init/memory/` directory to the local project root as `./memory/`.
   - Create the following project structure:
     - `./chapters`: For chapter `.tex` files.
     - `./codes`: For code snippet `.tex` files, organized by `./codes/chapterxx/`.
     - `./images`: For `png`, `svg`, and `tikz` files, organized by `./images/chapterxx/`.
     - `./fonts`: For custom font files (defaults to LaTeX fonts if empty).
     - `./configs`: For `.cls` and `.sty` configuration files.
     - `./templates`: For user-provided template models.
     - `./output`: To hold the final compilable structure for TexPage.
   - Initialize a `main.tex` in the root with capa, TOC, and basic imports.
1. **Setup** (`/writer-setup`): Initialize project and editorial pillars in `./memory/memory.json`.
2. **Planning** (`/writer-planning`): Outline chapter goals and structure.
3. **Drafting** (`/writer-drafting`): Generate conceptual content in LaTeX.
4. **Code Development** (`/writer-code`): Implement and map accents for algorithms.
5. **Integration** (`/writer-integration`): Consolidate text, code, and TikZ diagrams.
6. **Review** (`/writer-review`): Perform pedagogical and technical peer-review.
7. **Validation** (`/writer-validation`): Run structural checks and reference validation.
8. **Revision** (`/writer-revision`): Refactor based on feedback.
9. **Publication** (`/writer-publication`): Finalize LaTeX for TexPage.

### Mandatory Rules
- **Structural Integrity:** ALWAYS follow the defined folder schema. Never place assets outside their designated directories.
- **Progressive Loading:** Activate the specific sub-skill for each phase.
- **Local Project Memory:** All state and decisions MUST be recorded in the local `./memory/memory.json` file. NEVER write to the global skill path.
- **Decision Logging:** Every transition and decision must be recorded in `./memory/memory.json`.
- **Main File Logic:** `main.tex` must be the orchestrator of the book, importing styles from `./configs` and chapters from `./chapters`.
- **Accent Mapping:** Always ensure `literate` mapping for non-ASCII characters in code blocks.
- **Reference Integrity:** Use the Reference Checker script during the Validation phase.
