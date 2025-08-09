import streamlit as st
import httpx
import os
import time

# Optional shared core import
USE_DIRECT_CORE = False
try:
    from shared.chat_core import generate_chat_response  # type: ignore
    USE_DIRECT_CORE = True
except Exception:
    USE_DIRECT_CORE = False

# Page config
st.set_page_config(page_title="AI Chatbot Kit", layout="centered")

# API base URL - read from environment variable (optional if using direct core)
API_BASE_URL = os.getenv("API_URL")

# Remove trailing slash if present
if API_BASE_URL:
    API_BASE_URL = API_BASE_URL.rstrip('/')

# Construct endpoint URLs
CHAT_ENDPOINT = f"{API_BASE_URL}/api/chat/" if API_BASE_URL else None

# Streamed response function for API calls or direct core

def stream_response(message: str):
    if API_BASE_URL and CHAT_ENDPOINT:
        try:
            with httpx.Client() as client:
                response = client.post(
                    CHAT_ENDPOINT,
                    params={"message": message}
                )
            if response.status_code == 200:
                result = response.json()
                bot_response = result.get("response", "Sorry, I couldn't process that.")
            else:
                bot_response = f"Error: {response.status_code}"
        except Exception as e:
            bot_response = f"Connection error: {str(e)}"
    elif USE_DIRECT_CORE:
        try:
            bot_response = generate_chat_response(message)
        except Exception as e:
            bot_response = f"Core error: {str(e)}"
    else:
        bot_response = "API_URL is not set and shared core is unavailable."

    for word in str(bot_response).split():
        yield word + " "
        time.sleep(0.05)

st.title("AI Chatbot Kit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What can I help you with?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(stream_response(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
