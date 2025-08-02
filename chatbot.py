from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_gemini_response(query):
    response = model.generate_content(query)
    return response.text


# Sidebar
with st.sidebar:
    st.write("*Conversations Start with a Question. Powered by Google Gemini.*")
    st.caption(
        """**Harness the power of AI through a Gemini-powered chatbot. 
               Whether it's idea exploration, response testing, or building something innovative — everything begins with a single prompt. 
               Type a message and let Gemini respond with intelligence, clarity, and creativity. 
               Ready to experience the future of dialogue?**
               """
    )
    st.divider()
    st.caption(
        "<p style = 'text-align:center'>Made with ❤️ by Ankit</p>",
        unsafe_allow_html=True,
    )

st.set_page_config(initial_sidebar_state="expanded", layout="wide")

st.title("Gemini powered Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# def response_generator(prompt):
#     response = generate_gemini_response(prompt)
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = generate_gemini_response(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
