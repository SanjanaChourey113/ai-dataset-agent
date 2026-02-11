import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




import streamlit as st
from backend.app import ask_gemma

st.set_page_config(page_title="AI Dataset Agent", layout="centered")

st.title(" AI Dataset Question Answering")
st.write("Ask questions based on the dataset using Gemma model")

question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            answer = ask_gemma(question)
        st.subheader("AI Answer:")
        st.write(answer)
