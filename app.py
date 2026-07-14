import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -------------------------
# Memory Vault (Task 1)
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Page title
st.title("🤖 AI Multiverse Chatbot")
st.write("Talk to different AI personalities!")

# Sidebar
st.sidebar.title("App Settings")

personality = st.sidebar.selectbox(
    "Choose Personality",
    [
        "Helpful Teacher",
        "Expert Hacker",
        "Funny Friend",
        "Panicked College Student",
        "1920s Mafia Boss",
        "Sarcastic Fitness Coach"
    ]
)

intensity = st.sidebar.slider(
    "Intensity Level",
    1,
    10,
    5
)

# Avatar selection
if personality == "Helpful Teacher":
    bot_avatar = "👨‍🏫"
elif personality == "Expert Hacker":
    bot_avatar = "💻"
elif personality == "Funny Friend":
    bot_avatar = "😂"
elif personality == "Panicked College Student":
    bot_avatar = "😰"
elif personality == "1920s Mafia Boss":
    bot_avatar = "🕴️"
else:
    bot_avatar = "💪"

# -------------------------
# Display Chat History (Task 2)
# -------------------------
for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar=bot_avatar):
            st.write(message["content"])
    else:
        with st.chat_message("user"):
            st.write(message["content"])

# -------------------------
# Chat Input (Task 3)
# -------------------------
if user_message := st.chat_input("Say something..."):

    # Save user message (Task 4)
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    with st.chat_message("user"):
        st.write(user_message)

    ai_instructions = f"""
You are acting as {personality}.
Respond with intensity level {intensity}/10.

User says:
{user_message}
"""

    with st.spinner("Connecting to the Multiverse..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=ai_instructions
        )

    ai_reply = response.text

    with st.chat_message("assistant", avatar=bot_avatar):
        st.write(ai_reply)

    # Save AI response (Task 4)
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )