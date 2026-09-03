import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

# Your Gemini API key
API_KEY = "AQ.Ab8RN6I0dKODfh5J304TPa3GhHOTlCos08kPAmPSexK7FC6CNQ"

client = genai.Client(api_key="AQ.Ab8RN6I0dKODfh5J304TPa3GhHOTlCos08kPAmPSexK7FC6CNQ")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask Gemini anything...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=question
            )

            answer = response.text
            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            st.error(f"Error: {e}")