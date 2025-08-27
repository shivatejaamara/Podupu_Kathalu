# src/db.py
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()  

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
if not url or not key:
    raise ValueError("Supabase URL and KEY are missing. Check your .env file!")
supabase = create_client(url, key)

def insert_riddle(title, text, answer, tags):
    return supabase.table("riddles").insert({
        "title": title, "text": text, "answer": answer, "tags": tags
    }).execute()
def get_riddles():
    return supabase.table("riddles").select("*").execute()