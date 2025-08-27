import streamlit as st
from src.db import supabase
from utils.ai_helper import ai_generate_riddle  # your AI helper function
import tempfile
import speech_recognition as sr

st.title("Submit Podupu Kathalu")

# --- Input options ---
input_type = st.radio("Input type:", ["Text", "Audio"])

if input_type == "Text":
    title = st.text_input("Title")
    riddle = st.text_area("Riddle")
else:
    title = st.text_input("Title")
    audio_file = st.file_uploader("Upload audio (.wav/.mp3)", type=["wav", "mp3"])
    riddle = ""
    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(audio_file.read())
            recognizer = sr.Recognizer()
            with sr.AudioFile(tmp_file.name) as source:
                audio_data = recognizer.record(source)
                try:
                    riddle = recognizer.recognize_google(audio_data)
                    st.success("Audio converted to text!")
                except:
                    st.error("Could not understand audio.")

answer = st.text_input("Answer")
tags = st.text_input("Tags (comma separated)")

# --- AI assistant suggestion ---
if st.button("Generate suggestion using AI"):
    ai_text = ai_generate_riddle(title or "Riddle")
    st.info(ai_text)
    riddle = riddle or ai_text  # fill riddle if empty

# --- Submit ---
if st.button("Submit Podupu Kathalu"):
    if riddle.strip() and answer.strip():
        supabase.table("riddles").insert({
            "title": title,
            "text": riddle,
            "answer": answer,
            "tags": [t.strip() for t in tags.split(",")]
        }).execute()
        st.success("Podupu Kathalu submitted!")
    else:
        st.error("Riddle or answer cannot be empty.")
