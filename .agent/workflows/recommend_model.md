---
description: Recommend the best AI model for the next task based on context.
---

1. Analyze the current situation using the recommender prompt.
    - **Prompt Module**: `prompts/modules/recommender.md`
    - **Context**: Read the last few messages of the conversation (if possible) or the `task.md` status.
    *(Note: Since I cannot natively read the chat history variable directly in this workflow, I will ask you to provide a summary of what you want to do next, or I will infer it from the current open files/tasks.)*

2. Provide the recommendation.
    - Display the JSON output from the recommender prompt in a user-friendly format.

    **Example Output:**
    > 🧠 **Recommended: Architect (Claude 4.5 Opus)**
    > *Reason: You are asking for a system design review.*

    > ⚡ **Recommended: Constructor (Gemini 3 Pro)**
    > *Reason: You requested a UI implementation for the login page.*
