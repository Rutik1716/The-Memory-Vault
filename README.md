# 🧠 The Memory Vault

An interactive AI chatbot with conversation memory, built as part of the **MirAI School of Technology – AI Builder Virtual Summer Internship 2026**.

The application uses **Streamlit** and the **Google Gemini API** to create an AI chatbot that remembers the conversation during the current session.

## 🚀 Features

- 🤖 AI chatbot powered by Google Gemini
- 🧠 Conversation memory using Streamlit Session State
- 💬 Maintains previous user and AI messages
- 🎭 Multiple AI personalities
- 🎚️ Adjustable personality intensity from 1–10
- 👤 User and AI messages displayed separately
- ⚡ Real-time AI-generated responses
- 🔐 Secure API key handling using environment variables
- 🖥️ Interactive Streamlit interface

## 🎭 Available AI Personalities

The chatbot supports different personalities:

- 👨‍🏫 Helpful Teacher
- 👨‍💻 Expert Hacker
- 😂 Funny Friend
- 😰 Panicked College Student
- 🕴️ 1920s Mafia Boss
- 💪 Sarcastic Fitness Coach

The selected personality controls the style and tone of the AI responses.

## 🧠 Memory System

The application uses Streamlit's `session_state` to store the conversation:

```python
st.session_state.messages = []
