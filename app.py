import os

import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_KEY")

st.set_page_config(
    page_title="ChatGpt-4o",
    page_icon="🤖",
    layout="centered"
)

st.title('ChatGpt-4o')

prompt = st.chat_input('Ask anything...')

if "chats" not in st.session_state:
    st.session_state.chats = []

if prompt:
    st.session_state.chats.append({
        "role": "user",
        "content": prompt
    })

    assistant = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the world's best social media marketing person."},
            *st.session_state.chats,
            {"role": "user", "content": prompt}
        ]
    )

    st.session_state.chats.append({
        "role": "assistant",
        "content": assistant.choices[0].message.content
    })


for chat in st.session_state.chats:
    st.chat_message(chat['role']).markdown(chat['content'])
