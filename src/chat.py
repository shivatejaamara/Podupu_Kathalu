
# src/chat.py
import os, requests

API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_ai(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "model": "llama-3.1-8b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    res = requests.post(BASE_URL, json=payload, headers=headers)
    return res.json()["choices"][0]["message"]["content"]
