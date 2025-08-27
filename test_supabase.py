from src.db import supabase

# Fetch all riddles
riddles = supabase.table("riddles").select("*").execute()
print("Riddles in Supabase:", riddles.data)
