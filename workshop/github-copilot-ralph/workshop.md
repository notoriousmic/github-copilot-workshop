# 🚀 GitHub Copilot Workshop - Ralph Wiggum Edition
*Master autonomous development loops with the GitHub Copilot CLI*
![Ralph Banner](../../images/ralph.jpeg)
---

## 🎯 Workshop Overview

Welcome to the **Ralph Wiggum** module! This advanced workshop introduces a method for running GitHub Copilot CLI in a continuous, autonomous loop. By treating each iteration as a fresh context window, "Ralph" works through a series of tasks until completion without context bloat, perfect for greenfield projects and Proofs of Concept (POCs).

> **Credit:** This guide is inspired by [JeredBlu's Ralph Wiggum Guide](https://github.com/JeredBlu/guides/blob/main/Ralph_Wiggum_Guide.md) and [Arik Bidny's ralph-copilot-cli](https://github.com/arikbidny/ralph-copilot-cli).

### What You'll Master
- 🔄 **Autonomous Loops**: Run continuous development cycles with minimal human intervention
- 📝 **AI-Driven Planning**: Transform vague ideas into structured Product Requirement Documents (PRDs)
- 🧪 **Self-Correction**: Leverage agent-based testing and verification
- ⚡ **Context Management**: Learn how fresh context windows prevent AI hallucination

---

## 🛠️ Workshop Instructions

### 🌟 What is Ralph Wiggum?

Ralph Wiggum is a workflow that enables Copilot to build software iteratively. It relies on a "Plan-Act-Verify" cycle:

1.  **Plan**: A clear `prd.md` defines the roadmap.
2.  **Act**: The `ralph.sh` script executes one task at a time.
3.  **Verify**: The agent checks its work (and optionally uses `agent-browser` for visual confirmation) before moving to the next task.

**Ideal for:**
- Starting NEW projects from scratch
- Building defined Proofs of Concept (POCs)
- Projects where "Done" is clearly defined

---

## 📋 Task 1: The Architect - Design Your PRD

> **🎭 Scenario:** *You have a brilliant idea for a new app, but you don't want to spend days writing boilerplate. You need a solid plan that an AI agent can follow step-by-step.*

### 🎯 Objective
Use the Copilot CLI to interview you about your project and generate a comprehensive `prd.md` (Product Requirements Document) and a tailored `PROMPT.md`.

### 📝 Step-by-Step Instructions
#### Prerequisites
    -  ```npm install -g agent-browser && agent-browser install  # Downloads Chromium```
#### 🚀 Phase 1: The Interview

1. **📄 Create the prd, agent browser skill and copy the prompt file for copilot**
    - Open the terminal in the root of the project.
    - Copy the ```create-prd.md``` from the ```prompts``` directory into ```.github/agents``` directory.
    - Copy the ```PROMPT.md``` file from the ```prompts``` directory to the root it will be used by ralph for iterations.
    - Copy the ```SKILL.md``` file from the ```prompts/ralph``` directory to the ```.github/skills/agent-browser-skill/``` it will be used by GitHub Copilot for agent browser.

2.  **💬 Initialize the Planning Agent**
    Run the following command in your terminal to start the interactive planning session:

    ```bash
    copilot --agent=create-prd --interactive "Run this agent"
    ```

2.  **🗣️ Answer the Discovery Questions**
    The agent will ask you specific questions to define your project. Be detailed!
    *   *Tell me about the application or project you want to build. What problem are you trying to solve?*
        - Answer: I want to improve the user interface of my application to be more engaging to customers also I want to add a new page to the website that explaining about ralph wiggum capabilities with coding agents
    *   *Who is the primary user or audience for this project? What are their key needs or pain points?*
        -  The audience is developers their key need is to have a website that could help them understand better about coding agents    
    *   *What are the 3-5 core features or capabilities you want this project to have? List them in order of priority.*
        - Light and Dark mode for the website, Make the website accessible to users with disability


3.  **📄 Review the Artifacts**
    Once the interview is complete, the agent will generate:
    *   **`prd.md`**: A JSON-structured list of atomic tasks.
    *   **`PROMPT.md`**: The system instructions for the autonomous loop.
    *   **`activity.md`**: A log file for tracking progress.

#### 🔎 Phase 2: Verification (Critical!)

Before unleashing the agent, you **must** verify the generated plan:

*   **Check `prd.md`**: Are the tasks small and atomic? Do they make sense sequentially?
*   **Check `PROMPT.md`**: Are the start/build commands correct for your OS and stack?

---

## 🚀 Task 2: The Builder - Unleash the Autonomous Loop

> **🎭 Scenario:** *The plan is set. The blueprint is ready. Now, you act as the manager while "Ralph" acts as the developer, building your application one task at a time.*

### 🎯 Objective
Execute the `ralph.sh` script to let GitHub Copilot autonomously implement the tasks defined in your PRD.

### 📝 Step-by-Step Instructions

1.  **⌨️ Start the Loop**
    Run the script with a limit on iterations (commands). Start small (5-20) to ensure stability.

    ```bash
    ./ralph.sh 5
    ```

2.  **👀 Observe the Process**
    The script will:
    *   Read the current state from `activity.md` and `prd.md`.
    *   Select the next incomplete task.
    *   Generate code, run commands, and fix errors.
    *   Mark the task as "Passed" in `prd.md` when complete.
    *   Watch the screenshots directory for screenshots of the UI
    *   **Restart** with a fresh context for the next task.

---

## 📊 Task 3: The Manager - Monitor & Verify

> **🎭 Scenario:** *Trust, but verify. While Ralph is working hard, your job is to ensure the quality of the output and unblock any major issues.*

### 🎯 Objective
Monitor the agent's progress through logs and visual artifacts to ensure the project is on track.

### 📝 Step-by-Step Instructions

1.  **📝 Check the Activity Log**
    Open `activity.md` to see a running diary of what Ralph is doing.
    *   *Did it encounter an error? How did it fix it?*
    *   *What files were modified?*

2.  **📸 Review Screenshots (If Enabled)**
    If you have `agent-browser` installed, check the `screenshots/` directory. Ralph takes snapshots to verify UI changes visually.

3.  **🛑 Intervene if Needed**
    If Ralph gets stuck (e.g., repeating a task or failing to fix a bug):
    *   **Stop** the script (`Ctrl+C`).
    *   **Edit** the `prd.md` to break the stuck task into smaller steps.
    *   **Restart** `./ralph.sh`.

---

## 🧠 Best Practices for Ralph

1.  **Iterate on the PRD**: The quality of the code is directly proportional to the quality of your plan.
2.  **Keep it Simple**: Ralph shines on logical, step-by-step builds. Complex, ambiguous architectural decisions should be made by *you* in the PRD phase.
3.  **Fresh Context is King**: The magic of Ralph is that it forgets the noise of previous attempts. If it spirals, restart the loop.

---

## 📚 Resources

- [Original Ralph Wiggum Guide](https://github.com/JeredBlu/guides/blob/main/Ralph_Wiggum_Guide.md)
- [GitHub Copilot CLI Docs](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser)