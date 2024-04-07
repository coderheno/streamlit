import streamlit as st
import random

# List of names
names = [
    "Dr AMRUTHA", "Dr ANITA H B", "Dr AROKIA PAUL RAJAN R", "Dr ASHOK IMMANUEL V", "Dr BEAULAH SOUNDARABAI P",
    "Dr CECIL DONALD A", "Dr CHANDRA J", "Dr CYNTHIA T", "Dr DEEPA V JOSE", "Dr FABIOLA HAZEL POHRMEN",
    "Dr GOBI R", "Dr HELEN K JOY", "Dr. HUBERT(HU)", "Dr KAVITHA R", "Dr KIRUBANAND V B", "Dr LOKANAYAKI K",
    "Dr MANJUNATHA HIREMATH", "Dr MOHANA PRIYA T", "Dr NISMON RIO R", "Dr NISHA VARGHEESE", "Dr NEHA SINGHAL",
    "Dr NIZAR BANU P K", "Dr PETER AUGUSTIN D", "Dr POORNIMA N V", "Dr PRABU P", "Dr RAJESH KANNA R",
    "Dr RAMAMURTHY B", "Dr RESMI K R", "Dr ROHINI V", "Dr SAGAYA AURELIA P", "Dr SANDEEP J", "Dr SANGEETHA GOVINDA",
    "Dr SARAVANAKUMAR K", "Dr SARAVANAN K N", "Dr SENTHILNATHAN T", "Dr SHONY SEBASTIAN", "Prof SMERA",
    "Dr SMITHA VINOD", "Dr SOMNATH SINHA", "Dr SREEJA C S", "Dr SRIDEVI R", "Dr. SUDHAKAR", "Dr SURESH K",
    "Dr THIRUNAVUKKARASU V", "Dr VAIDHEHI V", "Dr VAISHNAVI B", "Dr VIJAY ARPUTHARAJ", "Dr VINEETHA KR"
]

# List of image URLs for wheel rotation
wheel_images = [
    "https://i.gifer.com/93ZM.gif",
    ]

# List of image URLs for dice faces
dice_images = {
    1: "https://emojicdn.elk.sh/🎲",
    2: "https://emojicdn.elk.sh/🎲",
    3: "https://emojicdn.elk.sh/🎲",
    4: "https://emojicdn.elk.sh/🎲",
    5: "https://emojicdn.elk.sh/🎲",
    6: "https://emojicdn.elk.sh/🎲"
}

# List of sound URLs for rolling dice
dice_sounds = {
    1: "https://www.soundjay.com/button/beep-01a.mp3",
    2: "https://www.soundjay.com/button/beep-02.mp3",
    3: "https://www.soundjay.com/button/beep-03.mp3",
    4: "https://www.soundjay.com/button/beep-04.mp3",
    5: "https://www.soundjay.com/button/beep-05.mp3",
    6: "https://www.soundjay.com/button/beep-06.mp3"
}

# Function to pick a random name
def pick_random_name(names):
    return random.choice(names)

# Function to simulate wheel rotation
def rotate_wheel():
    st.write("### Step 1: Rotate the Wheel")
    st.write("Click the button below to rotate the wheel!")
    if st.button("Rotate Wheel"):
        rotated_name = pick_random_name(names)
        st.image(random.choice(wheel_images), width=150)
        st.write(f"The wheel has stopped at: **{rotated_name}**")
        return rotated_name

# Function to display photo of the selected person
def display_photo(selected_name):
    st.write("### Step 2: Display Photo")
    st.write(f"Photo of {selected_name}:")
    # Add code here to display photo of the selected person

# Function to roll the dice
def roll_dice():
    st.write("### Step 3: Roll the Dice")
    st.write("Click the button below to roll the dice!")
    if st.button("Roll Dice"):
        selected_number = random.randint(1, 6)
        st.image(dice_images[selected_number], width=150)
        st.audio(dice_sounds[selected_number], format='audio/mp3', start_time=0)
        st.write(f"The dice shows: **{selected_number}**")
        return selected_number

# Function to perform tasks based on the dice number
def perform_task(selected_number, selected_name):
    st.write("### Step 4: Perform Task")
    tasks = {
        1: "Guess the photo of the person next to you!",
        2: "Guess the person next to you!",
        3: "Tell 2 truths about the person next to you!",
        4: "Perform a dance move!",
        5: "Tell a joke!",
        6: "Do an impression of someone famous!"
    }
    task = tasks.get(selected_number, "No task assigned!")
    st.write(f"Dear {selected_name}, your task is: {task}")

# Function to generate a funny comment
def generate_funny_comment(selected_name):
    st.write("### Step 5: Generate Funny Comment")
    funny_comments = [
        f"Congratulations {selected_name}! You nailed it!",
        f"Well done {selected_name}! That was hilarious!",
        f"{selected_name}, you're the star of the show!",
        f"Bravo {selected_name}! You made everyone laugh!",
        f"{selected_name}, you're a natural comedian!"
    ]
    funny_comment = random.choice(funny_comments)
    st.write(funny_comment)

def main():
    st.title("Fun Activity Generator")

    # First Tab: Rotate the Wheel
    st.write("## Step-by-Step Fun Activity Generator")
    selected_name = rotate_wheel()

    # Second Tab: Display Photo
    if selected_name:
        display_photo(selected_name)

    # Third Tab: Roll the Dice
    selected_number = roll_dice()

    # Fourth Tab: Perform Task
    if selected_number:
        perform_task(selected_number, selected_name)

    # Fifth Tab: Generate Funny Comment
    if selected_number:
        generate_funny_comment(selected_name)

if __name__ == "__main__":
    main()
