import random

def ai_generate_riddle(prompt):
    riddles = [
        "I speak without a mouth and hear without ears. What am I?",
        "The more of me you take, the more you leave behind. What am I?",
        "I’m light as a feather, but even the world’s strongest man can’t hold me for long. What am I?"
    ]
    return random.choice(riddles)
