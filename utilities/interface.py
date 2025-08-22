import streamlit as st
import random

# Name lists for BCA A and B
bca_a_names = [
    "A RAKSHAN", "ADARSH K.S", "ADITYA SUNIL PAREKKEL", "ADRINO ROSARIO JAMES",
    "AKSHAY A KURDEKAR", "ALAN JAMES", "ALEENA SHAJAN", "ALEX JOHN", "ANN MARIYA SABU",
    "ARZOO SINGLA", "ASHLIN JOSE", "BHARGAVI R S", "CHANDRA SHEKAR A", "DARSHAN PRAJAPATH",
    "DENNIS MATHEW ABEE", "EBI BIJU", "EDRIN VINOD MATHEW", "ELWIN OOMMEN VARGHESE",
    "FARHAN MUHAMMED SANOOJ", "FAY STEPHEN", "G VIGNESH", "GAYATHRI R", "HARDIK BAJAJ",
    "HARINI B", "ISHWAAK SARAOGI", "JASMIN JENNIFER", "JOBIN SAM", "JOSEPH ALEX",
    "K PRASANNA", "MAYUR VENKATESHA", "MIR MOHAMMAD FASEEH", "MOHAMMED TAHA",
    "NEEL SAHIL PODDAR", "NISHITA SHAIJU", "PAVITHRA B", "PRASANTH K", "PRAVEENA VYAS",
    "PREETHAM S", "R MITHRA BHARATHI", "RACHEL MARY D SOUZA", "RUCHITHA K", "S KHUSHAL",
    "SARAH KURIALA", "SARAH SHARON HANS", "SHAHZEEN SHAJI", "SHASHWAT DWIVEDI",
    "SHAUN ROY", "SHAURYA GARG", "SIMON CALVIN S", "SREESHMA CHOWDARY YETUKURI",
    "SURIYA M", "THEJUS DYLAN THOMAS", "U PRATHIKSHA KINI", "UNAT KAUR PANNU",
    "YASH RAJ RAJAWAT", "DILNA SHAJI", "MUSENGE WA MUSENGE"
]

bca_b_names = [
    "ABHISHEK M", "ABHISHEK N", "ADHARV P P", "AKASH GANESH", "ALEENA ELSA BENOY",
    "AMAN", "AMAN SONY", "ANDREW JUDAH", "ANDREW SHELTON S", "ANGEL SHIBU", "ANNIKA DUBEY",
    "ANSON NORONHA", "ANTONY OUSEPPACHAN", "ARUSH CHANDRA", "ARYANANDA BIJU", "BABITHA RAVINDRA",
    "CHRIS SAMUEL", "DEVYANSH SINGH", "DHAIRYA BARBHAYA", "DHAYAA V", "ETHAN THOMAS MATHEW",
    "GAURAV SINGH ADHIKARI", "HIMANSHI KANSAL", "ISHAAN KATARIA", "JESHAL MATHIAS",
    "JUSTIN T SHIJOY", "KUSHAL K", "LEO DSOUZA S", "LIDIA ARUL", "MARIA RACHEL MANOJ",
    "MARVIN ROPMUANG", "MEET GARG", "MEHAK DHINGRA", "NEEL VIKRAM JADHAV", "NEIL THOMAS MATHEW",
    "NIHARIKA NAIR", "NIMISHAMBHA A M", "NISANTH V S", "NITHYA SHREE S",
    "O LAKSHMI TANMAY TEJA", "PRANATHI NAGASAI PALLE", "PRATYUSH GUPTA", "PURVI CHAKARVARTI",
    "RAMONA ELISHA MARY", "ROHAIL KURIAKOSE VARGHESE", "ROHIT RATHEESH", "RYAN JOSHY",
    "SAI TANUSHREE SINGHA", "SAMARTHA SHAH", "SASHA ALWIN", "SHALOM P DANIEL", "SHRAVANI H K",
    "SHREYAS J N", "SHREYAS V MELLIGERI", "SIMRAN RAO", "SONIA C", "SRIDHAR N", "SUDHIR SALVA",
    "SUPRITH R B", "TEJAS SUJITH", "ZEHRAH SHAMEER", "LUCKY BOHRA N", "NANDAN H P SETTY",
    "JUBAIR MAHMUD"
]

# Dares for Wheel of Fun
dares = [
    "Speak like a news reporter for the next 2 minutes.",
    "Act like a professor giving a lecture on 'How to survive Monday mornings.'",
    "Walk across the class as if you’re a runway model.",
    "Sing any nursery rhyme like it’s an emotional Bollywood song.",
    "Pretend to argue with your bag because it 'forgot to do homework.'",
    "Speak only in song lyrics for the next 3 questions someone asks you.",
    "Give a motivational speech about why snacks are more important than exams.",
    "Pretend you’re in a TV ad and advertise chalk, duster, or a pen dramatically.",
    "Do 10 squats while loudly counting in a funny accent.",
    "Act like you’re teaching the class yoga and make up silly poses.",
    "Pretend you’re an alien visiting Earth and trying to understand what a pencil is.",
    "Do your best slow-motion action movie scene while walking to the door.",
    "Give a weather report about what’s happening inside the classroom.",
    "Pretend the floor is lava and show how you’d survive.",
    "Recite the alphabet backwards as fast as you can within 1 minute.",
    "Make up a new dance move and teach it to the class.",
    "Pretend to be a robot with a low battery and move/talk accordingly.",
    "Pretend you’re auditioning for a movie role as a dramatic crying student who failed a test.",
    "Start humming a dramatic song (like a villain theme) until others notice.",
    "Pretend you’re an annoyed teacher scolding a random person."
    "Sing a song in your language",
    "Dance for 30 seconds",
    "Tell a joke but no one should laugh",
    "Imitate your favorite actor",
    "Do 10 jumping jacks",
    "Say the alphabet backward",
    "Call your dad and say 'I love you'",
    "Make an animal sound",
    "Do your best hero pose",
    "Whisper a secret to someone",
    "Speak like a newsreader for 1 minute",
    "Tell your class crush’s name",
    "Balance a book on your head for 20 seconds",
    "Say something in a funny voice",
    "Tell the last 3 digits of your phone number",
    "Do a quick selfie and show the class",
    "Share your favorite food",
    "Make up a short rap",
    "Say a tongue twister 3 times fast",
    "Do your best Bollywood dance move",
    "Teach 1 to 100 in your own language",
    "Read out loud your 4th whats app message",
    "Read out loud your 2nd text message",
    "Read out loud your recent insta message",
    "Give one Dare to any of your classmate",
    "Request someone to confess",
    "Reveal the first letter of your current crush's name",
    "Call someone in your contacts and say 'I miss you'",
    "Share your most embarrassing moment in college",
    "Whisper something funny in the ear of the person next to you",
    "Say 'I love you' to a random object in the class",
    "Tell who you think is the most attractive person in this class",
    "Show the last picture you clicked on your phone (if appropriate)",
    "Do a slow-motion walk toward the crush’s desk",
    "Send a heart emoji ❤️ to the 5th person in your WhatsApp chat list and show proof",
    "Do an imitation of your favorite movie hero/heroine",
    "Tell one secret you’ve never told anyone in this class",
    "Give a compliment to three people of the opposite gender in the class",
    "Pretend to propose to your benchmate in a filmy style",
    "Change your WhatsApp status to 'In a Relationship' for the next 30 minutes",
    "Close your eyes and guess who taps on your shoulder",
    "Sing a song for someone in the class",
    "Show your phone’s wallpaper to everyone",
    "Act like you are on a date for 30 seconds",
    "Mimic your favorite student in the most dramatic way",
    "Speak in a different tone for the next few seconds",
    "Take a selfie with two people of the opposite gender and post it",
    "Share the name of the last person you texted",
    "Show your browsing history (last 3 searches)",
    "Say 'I like you but i hate you when.. ' to the person on your right",
    "Do 10 seconds of a worst dance move",
    "Show your funniest selfie",
    "Imitate a movie breakup scene with full emotion",
    "Give a flying rocket letter to someone in the class",
    "Send a funny voice note to someone randomly",
    "Tell one thing you love about the person sitting farthest from you",
    "Talk in a filmy dialogue and impress someone in a minute",
    "Share the most recent emoji you used and why",
    "Act like you are heartbroken and emote for 10 seconds",
    "Take a funny group selfie with your friends",
    "Play Slap/ Kill and Marry to choose a random classmate",
    "Post 'Feeling Loved ❤️' as your WhatsApp status",
    "Say something cute about your best friend",
    "Walk like a model across the classroom",
    "Pretend to talk to your crush on the phone loudly",
    "Draw a heart on the board with someone’s name inside",
    "Do a dramatic filmy entry from the door",
    "Give a nickname to three people in class right now",
    "Send a text saying 'I hate you' to your classmate and say reason",
    "Say a Bollywood pickup line dramatically",
    "Dance to a song for 15 seconds",
    "Do a handshake in a funny style with 5 classmates",
    "Speak in a baby voice for the next 2 minutes",
    "Tell who in the class would be a perfect couple",
    "Show the last reel you watched on Instagram",
    "Do 10 pushups while saying 'your favorite students'name each time"
]

# Class selection
st.sidebar.title("🎓 Class Activity Setup")
class_choice = st.sidebar.selectbox("Select Class", ["BCA A", "BCA B"])
if class_choice == "BCA A":
    names = bca_a_names
else:
    names = bca_b_names

# Main Menu
st.title("🎉 Class Activity Interface")
activity = st.radio("Choose Activity", ["Guidelines", "Tuple Matching Game", "Spin Wheel Game", "Wheel of Fun Dares"])

# Guidelines
if activity == "Guidelines":
    st.header("📋 Class Activity Guidelines")
    st.subheader("1. Human Bingo (Icebreaker)")
    st.write("""
    Objective: Guess whose hobby/interest is on the slip.
    Steps:
    1. Distribute slips of paper to everyone.
    2. Each student writes down one interest, hobby, or unique fact about themselves.
    3. Collect all slips and place them in a bag.
    4. Mix them well.
    5. Call one random person to pick a slip from the bag.
    6. That person must guess which classmate the slip belongs to.

    Rules:
    • If the guess is correct → both the picker and the owner of the slip get a point.
    • If the guess is wrong → spin the wheel for a mini-game.
    """)
    st.subheader("2. Wheel of Fun (Penalty/Bonus Round)")
    st.write("If a guess is wrong in Human Bingo, spin the wheel for mini-games like 2 Truths & 1 Lie, Funny Dare.")
    st.subheader("3. Headphones Game (Group Challenge)")
    st.write("""
    Divide class into groups. One acts with mute gestures; other guesses the word. Fun for teamwork!
    """)

# Tuple Matching Game
elif activity == "Tuple Matching Game":
    st.header("🎯 Tuple Matching Game")
    st.write("Each student gets a random task. Perform and have fun!")
    tasks = random.sample(dares, len(names))
    for i, name in enumerate(names):
        st.subheader(name)
        st.write(f"👉 Task: {tasks[i % len(tasks)]}")

# Spin Wheel Game
elif activity == "Spin Wheel Game":
    st.header("🎡 Spin the Wheel Game")
    if "spin_name" not in st.session_state:
        st.session_state.spin_name = None
        st.session_state.spin_task = None

    if st.button("🎯 Spin Now"):
        st.session_state.spin_name = random.choice(names)
        st.session_state.spin_task = random.choice(dares)

    if st.session_state.spin_name:
        st.success(f"🎯 {st.session_state.spin_name} → Task: {st.session_state.spin_task}")

# Wheel of Fun (Penalty / Bonus Round)
elif activity == "Wheel of Fun Dares":
    st.header("🔥 Wheel of Fun Dares")
    st.write("Click to get a fun dare!")
    if st.button("Spin Dare"):
        st.success(f"Your Dare: {random.choice(dares)}")
