import streamlit as st
import httpx
import os
import time

# Page config
st.set_page_config(page_title="AI Chatbot Kit", layout="centered")

# API base URL - read from environment variable
API_BASE_URL = os.getenv("API_URL")
if not API_BASE_URL:
    st.error("API_URL environment variable is not set")
    st.stop()

# Remove trailing slash if present
API_BASE_URL = API_BASE_URL.rstrip('/')

# Construct endpoint URLs
CHAT_ENDPOINT = f"{API_BASE_URL}/api/chat/"

# Streamed response function for API calls
def get_api_response(message):
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
    
    # Stream the response word by word
    for word in bot_response.split():
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
        response = st.write_stream(get_api_response(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
