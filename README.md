# 🧠 Multi-Agent Finance & Web Search System

A powerful AI-driven project that combines financial data analysis and web search capabilities using **Agno Agents**, **Groq models**, and a **Streamlit** interface.

---

## 🚀 Features

- 🔍 **Web Search Agent** — Fetches relevant, sourced web results using DuckDuckGo.
- 💹 **Finance Advisor Agent** — Retrieves real-time stock prices, fundamentals, analyst recommendations, and company news using Yahoo Finance.
- 🤖 **Multi-Agent System** — Combines both agents for intelligent, domain-specific responses.
- 🧑‍💻 **Streamlit UI** — Clean and interactive web interface for user queries.
- 🪶 **LLM-Powered** — Uses `llama-3.1-8b-instant` from Groq for reasoning and summarization.

---

## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/multi-agent-finance.git
   cd multi-agent-finance

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\\Scripts\\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set up environment variables**
   ```bash
   GROQ_API_KEY=your_groq_api_key

---

## ▶️ Running the App

**Start the Streamlit server:**
   ```bash
   streamlit run app.py
```

**Then open your browser and go to:**
   ```bash
   http://localhost:8501
```

---

## 🛠️ Tech Stack

**Agno** — Agent framework

**Groq LLM** — High-speed inference engine

**Streamlit** — UI for user interactions

**YFinanceTools** — Finance data integration

**DuckDuckGoTools** — Web search capabilities

**Multi AI Agent** — Statefull Collaborative system

---

## 📜 License

This project is licensed under the MIT License.