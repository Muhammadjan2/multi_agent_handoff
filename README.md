# 🤖 Multi-Agent Handoff System with Gemini API (OpenAI Agentic SDK)

This project demonstrates a **multi-agent handoff system** built using the [OpenAI Agentic SDK](https://github.com/openai/openai-agents-python) and integrated with the **Gemini API** (via OpenAI-compatible interface).

The system includes a **triage agent** that routes user input to domain-specific agents based on the question’s topic: **football**, **cricket**, or **hockey**.

---

## ✨ Features

- 🔁 Intelligent handoff system using the Agentic SDK
- 🧠 Specialized agents for:
  - 🏈 Football
  - 🏏 Cricket
  - 🏒 Hockey
- 🔍 Triage agent that analyzes the input and routes it accordingly
- 🧰 Powered by Gemini via OpenAI-compatible `AsyncOpenAI` client
- ⚡ Asynchronous execution using `asyncio`
- ✅ Beginner-friendly and easy to customize

---

## 🛠️ Technologies Used

- Python 3.10+
- [OpenAI Agentic SDK](https://github.com/openai/openai-agents-python)
- Gemini API (via OpenAI-compatible endpoints)
- `dotenv` for environment management
- `asyncio` for async run loop

---

## 📁 Project Structure

```bash
multi_agent_handoff.py   # Main script with triage and agents
.env                     # Contains your GEMINI_API_KEY (not tracked in Git)
README.md                # This file
