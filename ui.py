import streamlit as st
from assess_image import assess_image
from utils import chat
from groq import Groq
from dotenv import load_dotenv
import os

CITY = "Austin"

st.title("DermAI")

if "assessed_image" not in st.session_state:
    st.session_state.assessed_image = False
if "diagnosis" not in st.session_state:
    st.session_state.diagnosis = ""
if "language" not in st.session_state:
    st.session_state.language = "English"

def chat():
    load_dotenv()
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    if "model" not in st.session_state:
        st.session_state["model"] = "llama-3.2-11b-vision-preview"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "set_context" not in st.session_state:
        st.session_state.set_context = False

    for i, message in enumerate(st.session_state.messages):
        if i is not 0:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Handle user input
    if not st.session_state.set_context:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"""
                        you are a helpful assistant. Respond in {st.session_state.language}
                        Here is the diagnosis of the user's rash as context: {st.session_state.diagnosis}
                        Also, for additional context, the user is located in {CITY}.
                    """,
                }
            ],
            model="llama3-8b-8192",
        )
        st.session_state.messages.append(
            {"role": "system", "content": chat_completion.choices[0].message.content}
        )
        st.session_state.set_context = True

    if st.session_state.set_context:
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

language_options = ["English", "Spanish"]
st.session_state.language = st.selectbox("Choose your language", language_options)
uploaded_file = st.file_uploader("Choose an image...", type=["heic", "jpg", "jpeg", "png"])
if uploaded_file is not None:
    # st.image(uploaded_file, caption='Uploaded Image.')
    with open("/Users/pranavnarahari/Documents/meta-hackathon/uploaded_image.png", "wb") as f:
        f.write(uploaded_file.read())
        
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
location = st.text_input("Enter the location of the image on your body")
if location:
    if st.button('Assess Image'):
        st.session_state.assessed_image = True
        st.session_state.diagnosis = assess_image(location, age, st.session_state.language)

st.write(st.session_state.diagnosis)
if st.session_state.assessed_image:
    chat()


