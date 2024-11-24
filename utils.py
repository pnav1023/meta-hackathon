import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os


def chat():
    load_dotenv()
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    if "model" not in st.session_state:
        st.session_state["model"] = "llama-3.2-11b-vision-preview"
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Send prompt to Groq API
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model=st.session_state["model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            # Display response
            st.markdown(response.choices[0].message.content)
        st.session_state.messages.append(
            {"role": "assistant", "content": response.choices[0].message.content}
        )
