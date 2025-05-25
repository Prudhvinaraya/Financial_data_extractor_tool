# 📊 Financial Data Extractor using NVIDIA LLM API 🔥

This is a real-time **Streamlit web tool** that extracts **key financial metrics** like `Revenue` and `EPS` from any paragraph using **NVIDIA’s cutting-edge LLM Meta's llama-4-maverick-17b-128e-instruct** via the `langchain-nvidia-ai-endpoints` API.

> Built for demoing fast, practical GenAI applications.  
> Ideal for extracting insights from earnings reports, news articles, and analyst briefs.

---

## 🚀 Live App

🔗 [Try the live demo on Streamlit →](https://your-deployed-app.streamlit.app)

---

## 🧠 How It Works

- 🔌 Connects to NVIDIA's hosted LLMs (e.g., `meta/llama-4-maverick-17b-128e-instruct`) using secure API
- 🧾 Accepts natural-language financial text (e.g. news or earnings reports)
- 📤 Returns structured JSON with:
  - `revenue_actual`
  - `revenue_expected`
  - `eps_actual`
  - `eps_expected`
- 📊 Displays the data in a clean table using Streamlit

---

## 🖼 Example Input

> **Apple Inc.** reported a quarterly revenue of **$90 billion**, beating expectations of **$87 billion**.  
> EPS came in at **$2.17**, compared to the expected **$2.03**.

🧾 **Output JSON:**
```json
{
  "revenue_actual": "$90 billion",
  "revenue_expected": "$87 billion",
  "eps_actual": "$2.17",
  "eps_expected": "$2.03"
}



**📂 Project Structure**

Financial_data_extractor_tool/
│
├── main.py                  # Streamlit frontend
├── data_extractor.py        # NVIDIA LLM API logic
├── requirements.txt         # Project dependencies
├── .streamlit/
│   └── secrets.toml         # Your NVIDIA API key (not uploaded to GitHub)
└── README.md                # You're here!




