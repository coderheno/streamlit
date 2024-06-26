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
st.title("Quiz App")

# Color selection
st.header("Select a Color")
color = st.color_picker("Pick a Color", "#ffffff")  # Default color is white

# Change background color to the selected color
set_bg_color(color)

# Category selection
st.header("Select a Category")
category = st.selectbox("Choose a category:", ["General Knowledge", "Cinema", "Food and Culture"])

# Questions and answers based on selected category
if category == "General Knowledge":
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "John Steinbeck", "F. Scott Fitzgerald", "Mark Twain"],
            "answer": "Harper Lee"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
            "answer": "Leonardo da Vinci"
        }
    ]
elif category == "Cinema":
    questions = [
        {
            "question": "Who directed 'The Godfather'?",
            "options": ["Francis Ford Coppola", "Martin Scorsese", "Steven Spielberg", "Alfred Hitchcock"],
            "answer": "Francis Ford Coppola"
        },
        {
            "question": "Which actor played the role of Neo in 'The Matrix'?",
            "options": ["Keanu Reeves", "Tom Cruise", "Brad Pitt", "Matt Damon"],
            "answer": "Keanu Reeves"
        },
        {
            "question": "Which movie won the Academy Award for Best Picture in 2021?",
            "options": ["Nomadland", "The Trial of the Chicago 7", "Minari", "Promising Young Woman"],
            "answer": "Nomadland"
        },
        {
            "question": "Who won the Best Actor Oscar for his role in 'The Revenant'?",
            "options": ["Leonardo DiCaprio", "Joaquin Phoenix", "Brad Pitt", "Christian Bale"],
            "answer": "Leonardo DiCaprio"
        }
    ]
elif category == "Food and Culture":
    questions = [
        {
            "question": "What is the traditional Japanese rice wine?",
            "options": ["Sake", "Tequila", "Whiskey", "Vodka"],
            "answer": "Sake"
        },
        {
            "question": "Which country is famous for its chocolate?",
            "options": ["Switzerland", "Italy", "Belgium", "France"],
            "answer": "Switzerland"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["Avocado", "Tomato", "Onion", "Cilantro"],
            "answer": "Avocado"
        },
        {
            "question": "Which country is known for inventing pizza?",
            "options": ["Italy", "Greece", "Spain", "France"],
            "answer": "Italy"
        }
    ]
else:
    st.write("Please select a category.")

# Display questions and collect answers
if category in ["General Knowledge", "Cinema", "Food and Culture"]:
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
            message = "Excellent! You're an expert!"

        st.header("Your Results")
        st.write(f"You got {correct_answers} out of {len(questions)} correct.")
        st.write(f"Your score: {smileys[correct_answers]}")
        st.write(message)
