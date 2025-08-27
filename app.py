import streamlit as st
import random
st.set_page_config(page_title="Podupu Kathalu Platform", layout="wide")


# Custom CSS
st.markdown(
    """
    <style>
    /* Title at the top and center */
    .top-center-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: white;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.7);
    }

    /* Floating animation */
    @keyframes floatText {
        0%   {top: 10%; left: 10%;}
        25%  {top: 20%; left: 80%;}
        50%  {top: 70%; left: 60%;}
        75%  {top: 60%; left: 20%;}
        100% {top: 10%; left: 10%;}
    }
    .floating-text {
        position: fixed;
        font-size: 1.8rem;
        font-weight: bold;
        color: #ffdd57;
        animation: floatText 15s infinite linear;
        z-index: 999;
        pointer-events: none;
    }

    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }
    </style>

    <!-- Top center title -->
    <div class="top-center-title">🧩 Podupu Kathalu Platform 🧩</div>

    <!-- Floating word -->
    <div class="floating-text">✨ Podupu Kathalu ✨</div>
    """,
    unsafe_allow_html=True
)


# Main content below the title
st.markdown("## 📖 About This Platform")
st.markdown("""
Welcome to the **Podupu Kathalu Platform** 🎉!  
This is a place where you can **share, explore, and celebrate Podupu Kathalu** – the traditional Telugu riddles that test wit and creativity.  
""")

st.markdown("## 🔑 What You Can Do Here")
st.markdown("""
- ✍️ **Submit** your own Podupu Kathalu and contribute to our growing collection.  
- 📖 **View Riddles** submitted by others and challenge yourself to solve them.  
- 🌟 Connect with tradition while having fun with brain-teasing riddles.  
""")

st.markdown("## 🌍 Why Podupu Kathalu Are Important")
st.markdown("""
- They are an **integral part of Telugu culture** and oral literature.  
- Help in **sharpening thinking skills** and problem-solving ability.  
- A fun way to **pass knowledge between generations**.  
- Keeps the **language, wit, and creativity alive** in modern times.  
""")

def ai_generate_riddle(prompt):
    riddles = [
        "I speak without a mouth and hear without ears. What am I?",
        "The more of me you take, the more you leave behind. What am I?",
        "I’m light as a feather, but even the world’s strongest man can’t hold me for long. What am I?"
    ]
    return f"✨ Suggested riddle based on '{prompt}':\n\n{random.choice(riddles)}"

# ---- UI Section for AI Riddle Generator ----
st.markdown("## 🤖 AI Riddle Generator")
prompt = st.text_input("Enter a topic/idea for your riddle:")

if st.button("Generate Riddle"):
    riddle = ai_generate_riddle(prompt)
    st.success(riddle)
st.markdown("---")

