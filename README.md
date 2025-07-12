# 🔍 Ask Me Anything - LLM Chatbot (Powered by OpenRouter)

This is a lightweight web-based chatbot built with [Streamlit](https://streamlit.io) and [LangChain](https://www.langchain.com), designed to answer user questions using an OpenRouter-hosted LLM (`mistralai/mistral-7b-instruct`).

---

## 🚀 Features

- 🌐 Web interface powered by **Streamlit**
- 🧠 LLM integration using **LangChain** and **OpenRouter**
- 🔧 Custom prompt templates
- 🤖 Utilizes the **Mistral 7B Instruct** model via OpenRouter API

---

## 📦 Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

**Dependencies include:**
- `streamlit`
- `langchain>=0.1.13`
- `langchain-community`
- `openai`

---

## 🔑 Setup Instructions

1. **Clone or download** this repository.

2. **Add your OpenRouter API key**:
   - Open `main.py`
   - Replace the placeholder in `openai_api_key="sk-or-..."` with your actual API key.

3. **Run the app**:

```bash
streamlit run main.py
```

---

## 🧪 Usage

1. Open the Streamlit web app in your browser.
2. Type a question in the input field.
3. The app sends your question to the LLM via OpenRouter and displays the answer.

---

## 📁 Project Structure

```
.
├── main.py              # Main application file
├── requirements.txt     # List of dependencies
```

---

## ⚠️ Note

- Ensure you use a valid OpenRouter API key.
- The current version is a minimal prototype; you can extend it with features like:
  - Chat history
  - Model selection
  - File upload and QA over documents

---

## 📝 License

This project is provided as-is for educational/demo purposes. Feel free to modify and extend.
