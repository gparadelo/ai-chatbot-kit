import streamlit as st
import httpx
import os

# Page config
st.set_page_config(page_title="AI Chatbot Kit", layout="centered")

# Title
st.title("AI Chatbot Kit")

# API base URL - read from environment variable
API_BASE_URL = os.getenv("API_URL")
if not API_BASE_URL:
    st.error("API_URL environment variable is not set")
    st.stop()

# Remove trailing slash if present
API_BASE_URL = API_BASE_URL.rstrip('/')

# Construct endpoint URLs
CHAT_ENDPOINT = f"{API_BASE_URL}/api/chat/"

# Simple text input
user_message = st.text_input("Enter your message:")

# Send button
if st.button("Send"):
    if user_message.strip():
        try:
            with st.spinner("Sending..."):
                with httpx.Client() as client:
                    response = client.post(
                        CHAT_ENDPOINT,
                        params={"message": user_message}
                    )
                
                if response.status_code == 200:
                    result = response.json()
                    st.text_area("Response:", value=result.get("response", ""), height=100, disabled=True)
                else:
                    st.error(f"Error: {response.status_code}")
                    
        except Exception as e:
            st.error(f"Connection error: {str(e)}")
    else:
        st.warning("Please enter a message")
