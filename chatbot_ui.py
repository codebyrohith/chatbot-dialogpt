import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

st.title("AI Chatbot using DialoGPT 🤖")
st.write("An interactive AI chatbot that remembers conversation history.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history in a conversational format
for message in st.session_state.messages:
    if message["role"] == "You":
        st.markdown(f"🧑‍💻 **You:** {message['content']}")
    else:
        st.markdown(f"🤖 **Chatbot:** {message['content']}")

# User input field (store input in a temporary variable)
user_message = st.text_input("Type your message and press Send:")

# Process message only when "Send" button is clicked
if st.button("Send") and user_message:
    # Append user input to chat history
    st.session_state.messages.append({"role": "You", "content": user_message})

    # Send message to backend API
    response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_message})

    # Get response text from API
    if response.status_code == 200:
        bot_reply = response.json().get("response", "Sorry, I couldn't generate a response.")
    else:
        bot_reply = "Error: Unable to connect to the chatbot API."

    # Append chatbot response to chat history
    st.session_state.messages.append({"role": "Chatbot", "content": bot_reply})

    # Refresh UI after processing input
    st.rerun()

# Clear chat history button
if st.button("Clear Chat"):
    try:
        # Call backend API to clear chat
        clear_response = requests.post("http://127.0.0.1:5000/clear_chat")
        if clear_response.status_code == 200:
            # Reset chat history in UI
            st.session_state.messages = []
            st.rerun()
        else:
            st.error("Failed to clear chat history.")
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
