from src.db import supabase

# Insert a new riddle
data = {
    "title": "Test Riddle",
    "text": "చిన్నది పెద్దది చేయడానికి ఏది?",
    "answer": "మనసు",
    "tags": ["telugu", "folk"]
}

res = supabase.table("riddles").insert(data).execute()
print("Insert response:", res)

# Fetch all riddles
riddles = supabase.table("riddles").select("*").execute()
print("All riddles:", riddles.data)

