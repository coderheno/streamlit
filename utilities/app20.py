import streamlit as st

# Function to set the background color
def set_bg_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Title
st.title("Color Picker and Bollywood Fun Facts Quiz")

# Color selection
st.header("Select a Color")
color = st.color_picker("Pick a Color", "#000000")

# Change background color to the selected color
set_bg_color(color)

# Fun facts quiz
st.header("Bollywood Fun Facts Quiz")
questions = [
    {
        "question": "Who is known as the King of Bollywood?",
        "options": ["Shah Rukh Khan", "Aamir Khan", "Salman Khan", "Akshay Kumar"],
        "answer": "Shah Rukh Khan"
    },
    {
        "question": "Which Bollywood movie is the highest-grossing of all time?",
        "options": ["Dangal", "Baahubali 2", "PK", "Sanju"],
        "answer": "Baahubali 2"
    },
    {
        "question": "Who is the first Bollywood actor to be immortalized at Madame Tussauds?",
        "options": ["Amitabh Bachchan", "Raj Kapoor", "Shah Rukh Khan", "Dilip Kumar"],
        "answer": "Amitabh Bachchan"
    },
    {
        "question": "Which Bollywood actress is also a former Miss World?",
        "options": ["Priyanka Chopra", "Aishwarya Rai", "Sushmita Sen", "Lara Dutta"],
        "answer": "Aishwarya Rai"
    }
]

user_answers = []

for i, q in enumerate(questions):
    user_answer = st.radio(f"{i+1}. {q['question']}", q['options'])
    user_answers.append(user_answer)

# Result generation
if st.button("Generate Results"):
    correct_answers = sum(1 for i, q in enumerate(questions) if user_answers[i] == q['answer'])
    
    smileys = ["😔", "😐", "🙂", "😀", "😁"]
    message = ""
    
    if correct_answers == 0:
        message = "Better luck next time!"
    elif correct_answers == 1:
        message = "You got one right! Keep learning!"
    elif correct_answers == 2:
        message = "Good job! You're getting there!"
    elif correct_answers == 3:
        message = "Great! You know quite a bit!"
    elif correct_answers == 4:
        message = "Excellent! You're a true Bollywood expert!"

    st.header("Your Results")
    st.write(f"You got {correct_answers} out of {len(questions)} correct.")
    st.write(f"Your score: {smileys[correct_answers]}")
    st.write(message)
