name: writerkit-setup
description: Use when the user wants to initialize a new technical book project, establish editorial standards, or configure LaTeX environment pillars.
metadata:
  triggers: project setup, editorial pillars, LaTeX configuration, template analysis, project initialization
---

# Setting Up Kit

## When to Use This Skill
- Initializing a new project using the WriterKit framework.
- Configuring tone, language, and coding standards for a book.
- Setting up the LaTeX environment for TexPage compatibility.

## How to Use It
1. **Analyze Templates (Strict Mapping):**
   - Inspect provided `.tex`, `.cls`, and `.sty` files.
   - **Crucial:** Map ALL available commands, environments, and functions defined in these files.
   - **Crucial:** Map ALL defined colors from the color scheme files or preamble.
   - Extract preamble requirements.
2. **Conduct Configuration Interview:** Ask the Professor (User) to confirm:
   - **Tone:** (e.g., Formal, Professoral).
   - **Language:** (e.g., pt-BR).
   - **Primary Programming Language:** For syntax highlighting and accent mapping.
   - **Reference Style:** (e.g., ABNT, IEEE).
3. **Map Characters:** Configure the `literate` dictionary for the `listings` package to handle accented characters in code.
4. **Persist State:** Save all configurations, including the **mapped commands/environments and colors**, to `./memory/memory.json` and log the completion in the `decision_log`.
