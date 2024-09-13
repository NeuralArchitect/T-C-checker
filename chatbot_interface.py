import streamlit as st
import requests
import random
from bs4 import BeautifulSoup
import re
from groq import Groq
from main import fetch_and_save_to_file

st.set_page_config(page_title="Chatbot Interface", page_icon="💬", layout="centered")

GROQ_API_KEY = "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"
prompt = (
    "There are terms and conditions of a website, are there any terms and conditions "
    "which violate users privacy? If there are, then summarize it. Don't give an intro to the output; "
    "directly come to the point and give each point a numbering. At last, give your rating whether it's harmful or not, "
    "and if many people will agree with the terms and conditions."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

def clean_text(text):
    text = text.strip()
    text = re.sub(r'\n\s*\n', '\n', text)
    text = '\n'.join(line.strip() for line in text.splitlines())
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('. ', '.\n')
    text = re.sub(r'\*', '', text)
    return text


def get_groq_response(user_input, page_text):
    client = Groq(api_key=GROQ_API_KEY)
    tuned_text = prompt + page_text
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": tuned_text}],
        model="llama3-70b-8192",
    )
    output = chat_completion.choices[0].message.content
    cleaned_text = clean_text(output)
    return cleaned_text

st.title("🤖 Chatbot for T&C")

for message in st.session_state.messages:
    st.markdown(message)

user_input = st.text_input("Type your message / Enter URL:", value="", key="user_input")

if st.button("Send"):
    if user_input:
        user_message = f"**You:** {user_input}"
        st.session_state.messages.append(user_message)

        url = "https://learn.microsoft.com/en-us/office/developer-program/terms-and-conditions"
        with open("proxy_server/valid_proxies.txt", "r") as f:
            proxies = [proxy.strip() for proxy in f.readlines() if proxy.strip()]

        fetch_and_save_to_file(url, "data/test.html")

        scraped_html_path = "data/test.html"

        with open(scraped_html_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")
        page_text = soup.get_text(separator="\n")
        page_text = ' '.join(page_text.split())

        bot_response = get_groq_response(user_input, page_text)
        st.session_state.messages.append(f"**Chatbot:** {bot_response}")

        st.session_state["user_input"] = ""
