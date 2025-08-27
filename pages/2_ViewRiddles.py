import streamlit as st
from src.db import supabase

st.title("All Submitted Podupu Kathalu")

# Fetch riddles
response = supabase.table("riddles").select("*").execute()
riddles = response.data

if riddles:
    for r in riddles:
        st.write(f"**{r.get('title', 'Untitled')}**: {r.get('text', '')} (Answer: {r.get('answer', 'N/A')})")
        
        tags = r.get("tags", [])
        if isinstance(tags, list):
            st.write(f"Tags: {', '.join(tags)}")
        else:
            st.write(f"Tags: {tags}")  # fallback if it's stored as text

        st.write("---")
else:
    st.info("No Podupu Kathalu submitted yet.")

