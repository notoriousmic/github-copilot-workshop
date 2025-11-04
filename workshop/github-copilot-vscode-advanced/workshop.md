# 🚀 GitHub Copilot Workshop - Advanced Edition
*Master AI-powered development with advanced concepts and GitHub Copilot features*

---

## 🎯 Workshop Overview

Welcome to the **Advanced Edition** of the GitHub Copilot workshop! This hands-on session dives deeper into AI-powered development, equipping you with advanced techniques to optimize your workflow, enhance code quality, and tackle complex development challenges with ease. By the end of this workshop, you'll master the art of leveraging GitHub Copilot to streamline your coding process.

---

## ⚡ Concepts

### 🔑 General Concepts

- **Context Engineering**: The practice of designing and managing the information an AI assistant uses to give accurate, relevant responses. It involves structuring prompts, metadata, code comments, documentation, and environment context so the AI clearly understands your project’s goals, style, and constraints. This leads to smarter, safer, and more consistent output.
  > *In short: Context engineering is how you teach AI to think like your team.*

- **Prompt Engineering**: The art of crafting clear and effective instructions for AI models to get the desired output. It involves choosing the right words, structure, and context so the AI understands what you want, how you want it, and why it matters.
  > *In short: Prompt engineering is how you communicate with AI to turn intent into results.*

- **MCP (Model Context Protocol)**: An open standard by Anthropic that lets AI models securely connect to external tools, data, and APIs through a common protocol. It acts like a universal adapter—allowing AI assistants (like Claude or Copilot) to access real-time context from your systems without custom integrations.
  > *In short: MCP makes AI truly useful by giving it safe, standardized access to your tools and data.*

### 🤖 GitHub Copilot-Specific Features

- **Copilot Instructions**: GitHub Copilot can provide chat responses tailored to your team’s workflow, tools, or project specifics if you provide it with enough context. Instead of repeatedly adding this contextual detail to your chat questions, you can create a file that automatically adds this information for you. The additional information is not displayed in the chat but is available to Copilot to generate higher-quality responses.
  > *In short: Copilot instructions allow you to create a context for GitHub Copilot and define general rules related to the repository.*

- **Custom Chat Modes**: These consist of a set of instructions and tools applied when you switch to that mode. For example, a "Plan" chat mode could include instructions for generating an implementation plan and only use read-only tools. By creating a custom chat mode, you can quickly switch to that specific configuration without manually selecting relevant tools and instructions each time.
  > *In short: Custom chat modes are predefined instruction sets and tool configurations for Copilot.*

- **Prompt Files**: Markdown files that define reusable prompts for common development tasks like generating code, performing code reviews, or scaffolding project components. They enable the creation of a library of standardized development workflows.
  > *In short: Prompt files store reusable prompts for tasks like coding, reviews, or scaffolding, letting you run them directly in chat.*

---

## 📋 Task 1: Using Copilot Instructions - Making Copilot Self-Tailored

> **🎭 Scenario:** *You are tasked with creating Copilot instructions for your project to help Copilot better understand your goals and make it more personalized to your project.*

### 🎯 Objective
Transform from a newcomer to a productive team member in under 10 minutes using AI-powered code exploration.

### 🛠️ Steps
1. **Understand Your Project Goals**:
   - Identify the key objectives and workflows of your project.
   - Highlight any unique tools, libraries, or coding standards used.

2. **Create a Copilot Instruction File**:
   - Create a directory called (`.github`) that have an `copilot-instructions.md` in it.
   - Write in Markdown file (`copilot-instructions.md`) that you create and include:
     - Project goals and context.
     - Coding standards and best practices.
     - Commonly used libraries or frameworks.

3. **Test and Iterate**:
   - Now use copilot and see how it takes into account the custom instructions in all the interactions.

### 💡 Pro Tip
 - Use clear and concise language in your instruction file. The more specific you are, the better Copilot can tailor its responses to your needs.
 - We recommend organizing prompts into distinct sections (like <background_information>, <instructions>, ## Tool guidance, ## Output description, etc) and using techniques like XML tagging or Markdown headers to delineate these sections, although the exact formatting of prompts is likely becoming less important as models become more capable.  
 example:   
 ```
<role_definition>
Your name is **Mico**.  
You are GitHub Copilot, acting as a **senior software engineer** supporting organizational repositories.  
Your mission is to help developers write **clear, secure, and maintainable** code while following company conventions and compliance rules.
</role_definition>

---
<rules_core>
1. **Clarity & Maintainability** — Write code that is easy to read, explain, and extend.  
2. **Privacy & Security First** — Never generate or expose secrets, credentials, or personal data.  
3. **Context Awareness** — Adapt to each project’s language, framework, and style.  
4. **Transparency** — Be able to justify every generated suggestion.  
</rules_core>

---
<rules_behavior>
When generating code, documentation, or text:
- Summarize intent briefly before or after producing code.
- Prefer clarity over cleverness: short, well-named functions and clear logic.
- Reuse existing utilities and avoid duplication.
- Add docstrings, type hints, or examples where helpful.
- Encourage testing and validation of new code.
- Respect explicit developer instructions.
- Never invent facts, sources, or data.
</rules_behavior>
 ```


---

### 🔑 Key Takeaways
- Context and prompt engineering are essential for effective AI collaboration.
- GitHub Copilot’s advanced features, like custom chat modes and prompt files, can significantly enhance your development workflow.
- Tailoring Copilot to your project ensures higher-quality suggestions and a more seamless coding experience.
