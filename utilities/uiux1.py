import streamlit as st
import random
import time
import json
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="UX Beyond Today",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.hero {
    padding: 35px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 25px;
    background: linear-gradient(135deg, #111827, #312e81, #4c1d95);
    color: white;
}

.hero h1 {
    font-size: 3.2rem;
    margin-bottom: 5px;
}

.hero p {
    font-size: 1.25rem;
    opacity: 0.9;
}

.challenge-card {
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #ddd;
    background-color: #fafafa;
    margin: 15px 0;
}

.problem-card {
    padding: 25px;
    border-radius: 18px;
    background-color: #fff7ed;
    border-left: 7px solid #f97316;
}

.forbidden {
    padding: 20px;
    border-radius: 15px;
    background-color: #fef2f2;
    border-left: 7px solid #ef4444;
}

.future {
    padding: 20px;
    border-radius: 15px;
    background-color: #eff6ff;
    border-left: 7px solid #3b82f6;
}

.success-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #f0fdf4;
    border-left: 7px solid #22c55e;
}

.big-number {
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
}

.timer {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
}

.small-muted {
    color: #6b7280;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# CHALLENGES
# ============================================================

CHALLENGES = [

    {
        "domain": "EXAMINATION",
        "emoji": "📝",
        "challenge": "Redesign the concept of examination for the AI era.",
        "context": "Students are still commonly evaluated through written exams, online exams, projects, viva and practical assessments.",
        "forbidden": [
            "Online examination",
            "AI proctoring",
            "MCQ platform",
            "LMS examination",
            "Video proctoring"
        ],
        "future_prompt": "What if the concept of an examination itself disappeared?"
    },

    {
        "domain": "E-COMMERCE",
        "emoji": "🛒",
        "challenge": "Rethink how people shop in the future.",
        "context": "Today users browse products, compare prices, read reviews and click Buy.",
        "forbidden": [
            "Shopping app",
            "Product recommendation engine",
            "Chatbot",
            "AR try-on",
            "Faster delivery"
        ],
        "future_prompt": "What if users never had to browse products?"
    },

    {
        "domain": "CLASSROOM",
        "emoji": "🎓",
        "challenge": "Redesign learning for the future.",
        "context": "Traditional education relies heavily on classrooms, timetables, lectures and assignments.",
        "forbidden": [
            "Online classroom",
            "Video lectures",
            "LMS",
            "Recorded classes",
            "AI tutor"
        ],
        "future_prompt": "What if there were no classrooms, lectures or fixed timetables?"
    },

    {
        "domain": "HOSPITAL",
        "emoji": "🏥",
        "challenge": "Redesign the complete healthcare experience from the patient's perspective.",
        "context": "Patients often deal with appointments, queues, forms, tests and repeated visits.",
        "forbidden": [
            "Appointment booking app",
            "Telemedicine",
            "Hospital website",
            "Digital token system",
            "Chatbot"
        ],
        "future_prompt": "What if healthcare happened continuously instead of only when patients visit a hospital?"
    },

    {
        "domain": "JOB INTERVIEW",
        "emoji": "💼",
        "challenge": "Rethink how companies evaluate candidates.",
        "context": "Recruitment commonly depends on resumes, interviews, coding tests and group discussions.",
        "forbidden": [
            "Online interview",
            "AI interview",
            "Resume screening",
            "Coding test platform",
            "Video interview"
        ],
        "future_prompt": "What if the traditional job interview disappeared?"
    },

    {
        "domain": "AIRPORT",
        "emoji": "✈️",
        "challenge": "Redesign the passenger experience at airports.",
        "context": "Passengers currently deal with check-in, baggage, security, immigration, gates and queues.",
        "forbidden": [
            "Airport app",
            "Self check-in kiosk",
            "Digital boarding pass",
            "Queue management app",
            "Airport chatbot"
        ],
        "future_prompt": "What if passengers never had to think about check-in, documents or queues?"
    },

    {
        "domain": "BANKING",
        "emoji": "🏦",
        "challenge": "Rethink how humans interact with money.",
        "context": "People currently use banking apps, cards, ATMs and online banking.",
        "forbidden": [
            "Banking app",
            "Chatbot",
            "UPI improvement",
            "Digital wallet",
            "Better ATM"
        ],
        "future_prompt": "What if managing money required almost no conscious effort?"
    },

    {
        "domain": "UNIVERSITY",
        "emoji": "🏫",
        "challenge": "Redesign the complete student experience.",
        "context": "Students interact with departments, faculty, timetables, examinations, fees, clubs and administration.",
        "forbidden": [
            "University app",
            "Student portal",
            "Chatbot",
            "Digital ID",
            "Better website"
        ],
        "future_prompt": "What if the university itself became an intelligent environment?"
    },

    {
        "domain": "PUBLIC TRANSPORT",
        "emoji": "🚌",
        "challenge": "Rethink how people experience public transportation.",
        "context": "People currently plan routes, wait for vehicles, purchase tickets and navigate stations.",
        "forbidden": [
            "Transport tracking app",
            "Google Maps-like app",
            "Digital ticket",
            "Bus tracking",
            "Route recommendation"
        ],
        "future_prompt": "What if transportation adapted itself to each person's needs?"
    },

    {
        "domain": "CANTEEN",
        "emoji": "🍱",
        "challenge": "Redesign the experience of getting food on a busy campus.",
        "context": "Students typically view menus, stand in queues, order, pay and wait.",
        "forbidden": [
            "Food ordering app",
            "QR menu",
            "Online payment",
            "Token system",
            "Delivery app"
        ],
        "future_prompt": "What if the student never had to place an order?"
    },

    {
        "domain": "LIBRARY",
        "emoji": "📚",
        "challenge": "Rethink how humans access and experience knowledge.",
        "context": "Libraries traditionally organize physical and digital resources for users.",
        "forbidden": [
            "Library app",
            "Digital library",
            "Book recommendation system",
            "Library chatbot",
            "Book search website"
        ],
        "future_prompt": "What if knowledge came to the learner instead of the learner searching for knowledge?"
    },

    {
        "domain": "GOVERNMENT SERVICES",
        "emoji": "🏛️",
        "challenge": "Redesign how citizens interact with government services.",
        "context": "Citizens often deal with forms, documents, websites, offices and multiple departments.",
        "forbidden": [
            "Government website",
            "Government app",
            "Chatbot",
            "Online form",
            "Single-window portal"
        ],
        "future_prompt": "What if citizens never had to figure out which government service they need?"
    },

    {
        "domain": "SUPERMARKET",
        "emoji": "🛍️",
        "challenge": "Rethink grocery shopping.",
        "context": "Customers walk through aisles, select products, queue and pay.",
        "forbidden": [
            "Self-checkout",
            "Shopping app",
            "Digital trolley",
            "QR scanning",
            "Home delivery"
        ],
        "future_prompt": "What if the supermarket disappeared as we know it?"
    },

    {
        "domain": "TRAVEL",
        "emoji": "🌍",
        "challenge": "Rethink how people experience travel.",
        "context": "Travelers currently research destinations, compare options, book accommodation and plan activities.",
        "forbidden": [
            "Travel website",
            "Travel app",
            "AI itinerary",
            "Chatbot",
            "Recommendation engine"
        ],
        "future_prompt": "What if travelers never had to plan a trip?"
    },

    {
        "domain": "PERSONAL FINANCE",
        "emoji": "💰",
        "challenge": "Rethink how ordinary people manage their finances.",
        "context": "People track expenses, budgets, investments, bills and savings.",
        "forbidden": [
            "Expense tracker",
            "Budgeting app",
            "Investment app",
            "Financial chatbot",
            "Notification system"
        ],
        "future_prompt": "What if financial decisions became almost invisible to the user?"
    },

    {
        "domain": "CAMPUS NAVIGATION",
        "emoji": "🧭",
        "challenge": "Rethink navigation inside a large university campus.",
        "context": "Students and visitors currently rely on signs, maps and mobile navigation.",
        "forbidden": [
            "Campus map app",
            "GPS navigation",
            "QR codes",
            "Digital map",
            "Beacon navigation"
        ],
        "future_prompt": "What if the campus itself guided you?"
    },

    {
        "domain": "FITNESS",
        "emoji": "🏃",
        "challenge": "Rethink how humans maintain physical fitness.",
        "context": "People use gyms, fitness apps, wearables and exercise programs.",
        "forbidden": [
            "Fitness app",
            "Smartwatch",
            "Fitness tracker",
            "Online workout",
            "AI workout recommendation"
        ],
        "future_prompt": "What if people didn't have to consciously 'work out'?"
    },

    {
        "domain": "EMERGENCY SERVICES",
        "emoji": "🚨",
        "challenge": "Rethink how people get help during emergencies.",
        "context": "People currently call emergency numbers, describe their location and wait for responders.",
        "forbidden": [
            "Emergency app",
            "Emergency chatbot",
            "Location sharing",
            "SOS button",
            "Emergency notification"
        ],
        "future_prompt": "What if the emergency system knew help was needed before the user asked?"
    },

    {
        "domain": "WORKPLACE",
        "emoji": "🏢",
        "challenge": "Imagine the workplace of the future.",
        "context": "Employees currently use offices, email, meetings, messaging systems and productivity tools.",
        "forbidden": [
            "Video conferencing",
            "Slack-like platform",
            "Productivity app",
            "AI meeting assistant",
            "Virtual office"
        ],
        "future_prompt": "What if the concept of a workplace changed completely?"
    },

]

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "home",
    "team_name": "",
    "members": [],
    "challenge": None,
    "ideas": [],
    "why_answers": ["", "", "", "", ""],
    "how_might_we": "",
    "selected_idea": "",
    "solution": "",
    "technology": "",
    "experience": "",
    "wow": "",
    "pitch": "",
    "submitted": False,
    "scores": {},
    "timer_end": None,
    "timer_label": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# HELPERS
# ============================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def start_timer(minutes, label):
    st.session_state.timer_end = time.time() + minutes * 60
    st.session_state.timer_label = label


def timer_display():
    if st.session_state.timer_end:
        remaining = int(st.session_state.timer_end - time.time())

        if remaining <= 0:
            return "⏰ TIME'S UP!"

        mins = remaining // 60
        secs = remaining % 60

        return f"{mins:02d}:{secs:02d}"

    return "Not started"


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">
    <h1>🚀 UX BEYOND TODAY</h1>
    <p>Don't improve today's solution. Imagine tomorrow's experience.</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "home":

    st.markdown("## 🎯 Welcome, Future Designers")

    st.markdown("""
    <div class="challenge-card">
        <h3>Your mission</h3>
        <p>
        You will receive a real-world problem domain.
        Your team must imagine a solution that goes beyond
        today's commonly known solutions.
        </p>
        <h3>🚫 You are NOT here to...</h3>
        <ul>
            <li>Copy an existing application</li>
            <li>Simply add AI to an existing system</li>
            <li>Design screens immediately</li>
            <li>Search for an existing solution</li>
        </ul>
        <h3>🧠 You ARE here to...</h3>
        <ul>
            <li>Question assumptions</li>
            <li>Understand the user</li>
            <li>Generate unexpected ideas</li>
            <li>Imagine future experiences</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "💡 Remember: Technology is not the solution. "
        "Technology should enable a better user experience."
    )

    st.markdown("### 👥 Enter your team")

    col1, col2 = st.columns(2)

    with col1:
        st.session_state.team_name = st.text_input(
            "Team name",
            placeholder="Example: UX Avengers"
        )

    with col2:
        member_text = st.text_input(
            "Members",
            placeholder="Asha, Rahul, Priya, John"
        )

    if st.button("🎲 DRAW OUR CHALLENGE", type="primary", use_container_width=True):

        if not st.session_state.team_name:
            st.warning("Please enter your team name.")

        else:
            st.session_state.members = [
                x.strip()
                for x in member_text.split(",")
                if x.strip()
            ]

            st.session_state.challenge = random.choice(CHALLENGES)
            st.session_state.ideas = []
            st.session_state.why_answers = ["", "", "", "", ""]
            st.session_state.submitted = False

            go("challenge")


# ============================================================
# CHALLENGE
# ============================================================

elif st.session_state.page == "challenge":

    c = st.session_state.challenge

    st.markdown(
        f"""
        <div class="problem-card">
            <h1>{c['emoji']} {c['domain']}</h1>
            <h2>{c['challenge']}</h2>
            <p>{c['context']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🚫 Forbidden Solutions")

    st.markdown(
        "<div class='forbidden'><b>You cannot simply propose:</b><br><br>"
        + " • ".join(c["forbidden"])
        + "</div>",
        unsafe_allow_html=True
    )

    st.markdown("## 🔥 Your Future Thinking Trigger")

    st.markdown(
        f"""
        <div class="future">
            <h3>💭 {c['future_prompt']}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Team", st.session_state.team_name)

    with col2:
        st.metric("Members", len(st.session_state.members))

    with col3:
        st.metric("Ideas Required", "10+")

    st.markdown("### 🧠 Phase 1 — Understand Before You Solve")

    if st.button("▶ Start 10-Minute Problem Analysis"):

        start_timer(10, "Problem Analysis")

    st.markdown(
        f"<div class='timer'>{timer_display()}</div>",
        unsafe_allow_html=True
    )

    if st.session_state.timer_end:
        st.caption(f"Current phase: {st.session_state.timer_label}")

    st.markdown("### 🔍 Discuss these questions")

    st.write("1. Who is the primary user?")
    st.write("2. What is the user actually trying to accomplish?")
    st.write("3. What frustrates the user today?")
    st.write("4. Why does this problem exist?")
    st.write("5. What assumptions are we making?")

    if st.button("➡️ Continue to 5 WHYS", use_container_width=True):
        go("five_whys")


# ============================================================
# FIVE WHYS
# ============================================================

elif st.session_state.page == "five_whys":

    st.markdown("# 🧠 5 WHYS")

    st.info(
        "Do not jump to a solution. Keep asking WHY until you reach "
        "the deeper problem behind the obvious problem."
    )

    st.markdown("### Start with your initial problem")

    st.session_state.why_answers[0] = st.text_input(
        "Problem",
        value=st.session_state.why_answers[0],
        placeholder="Example: Students dislike examinations."
    )

    labels = [
        "Why does this happen?",
        "Why does THAT happen?",
        "Why is THAT happening?",
        "Why does the underlying problem exist?"
    ]

    for i, label in enumerate(labels, start=1):

        st.session_state.why_answers[i] = st.text_input(
            label,
            value=st.session_state.why_answers[i]
        )

    st.markdown("---")

    st.markdown("### 🎯 Reframe the problem")

    st.session_state.how_might_we = st.text_area(
        "Write your 'How Might We...' statement",
        value=st.session_state.how_might_we,
        placeholder="How might we..."
    )

    if st.button("➡️ Generate Ideas", type="primary", use_container_width=True):

        go("ideas")


# ============================================================
# IDEA GENERATION
# ============================================================

elif st.session_state.page == "ideas":

    st.markdown("# 💡 IDEATION ARENA")

    st.markdown("""
    <div class="future">
        <h3>RULE:</h3>
        <p>Generate first. Judge later.</p>
        <p>Your first idea is probably ordinary.</p>
        <p>Your tenth idea might be interesting.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("▶ Start 15-Minute Brainstorm"):

        start_timer(15, "Divergent Ideation")

    st.markdown(
        f"<div class='timer'>{timer_display()}</div>",
        unsafe_allow_html=True
    )

    st.markdown("### 🚀 Future Thinking Prompts")

    prompts = [
        "What if AI did it?",
        "What if there was no app?",
        "What if there was no screen?",
        "What if the user didn't have to initiate anything?",
        "What if the system predicted the need?",
        "What if the experience was continuous?",
        "What if humans and AI collaborated?",
        "What if the physical environment became intelligent?",
        "What if the problem disappeared entirely?",
        "What if today's biggest constraint didn't exist?"
    ]

    cols = st.columns(2)

    for i, p in enumerate(prompts):

        with cols[i % 2]:
            st.write(f"💭 {p}")

    st.markdown("---")

    st.markdown("## Add your ideas")

    new_idea = st.text_input(
        "Idea",
        placeholder="Enter one idea at a time..."
    )

    if st.button("➕ Add Idea"):

        if new_idea.strip():

            st.session_state.ideas.append(new_idea.strip())
            st.rerun()

    st.markdown(
        f"### Ideas generated: **{len(st.session_state.ideas)}**"
    )

    for i, idea in enumerate(st.session_state.ideas):

        st.write(f"**{i+1}.** {idea}")

    if len(st.session_state.ideas) >= 10:

        st.success(
            "🔥 Excellent! You reached the minimum 10 ideas. "
            "Now select your strongest concept."
        )

    if st.button(
        "➡️ Continue",
        disabled=len(st.session_state.ideas) == 0,
        use_container_width=True
    ):
        go("selection")


# ============================================================
# IDEA SELECTION
# ============================================================

elif st.session_state.page == "selection":

    st.markdown("# 🎯 CHOOSE YOUR FUTURE")

    st.write(
        "Now stop brainstorming. Evaluate your ideas."
    )

    st.markdown("### Score your ideas")

    best_scores = {}

    for i, idea in enumerate(st.session_state.ideas):

        st.markdown(f"### 💡 Idea {i+1}")
        st.write(idea)

        col1, col2, col3 = st.columns(3)

        with col1:
            user_score = st.slider(
                "User value",
                1,
                5,
                3,
                key=f"user_{i}"
            )

        with col2:
            originality = st.slider(
                "Originality",
                1,
                5,
                3,
                key=f"original_{i}"
            )

        with col3:
            feasibility = st.slider(
                "Feasibility",
                1,
                5,
                3,
                key=f"feasible_{i}"
            )

        best_scores[idea] = (
            user_score + originality + feasibility
        )

    if st.button("🏆 SELECT BEST IDEA", type="primary"):

        selected = max(
            best_scores,
            key=best_scores.get
        )

        st.session_state.selected_idea = selected

        go("future_canvas")


# ============================================================
# FUTURE CANVAS
# ============================================================

elif st.session_state.page == "future_canvas":

    st.markdown("# 🚀 FUTURE EXPERIENCE CANVAS")

    st.success(
        f"Your selected concept:\n\n"
        f"### 💡 {st.session_state.selected_idea}"
    )

    st.markdown("### 1️⃣ What is your solution?")

    st.session_state.solution = st.text_area(
        "Describe your concept",
        value=st.session_state.solution,
        height=120
    )

    st.markdown("### 2️⃣ What technology enables it?")

    st.session_state.technology = st.text_area(
        "Technology",
        value=st.session_state.technology,
        placeholder="AI, AR, robotics, spatial computing..."
    )

    st.markdown("### 3️⃣ How does the user experience it?")

    st.session_state.experience = st.text_area(
        "User experience",
        value=st.session_state.experience,
        placeholder="Step 1 → Step 2 → Step 3..."
    )

    st.markdown("### 4️⃣ Your WOW factor")

    st.session_state.wow = st.text_area(
        "What makes your solution radically different?",
        value=st.session_state.wow,
        height=100
    )

    if st.button(
        "➡️ Prepare 60-Second Pitch",
        type="primary",
        use_container_width=True
    ):
        go("pitch")


# ============================================================
# PITCH
# ============================================================

elif st.session_state.page == "pitch":

    st.markdown("# 🎤 60-SECOND FUTURE PITCH")

    st.warning(
        "You have exactly 60 seconds. "
        "Your goal is not to explain everything. "
        "Your goal is to make the audience understand your idea."
    )

    st.markdown("""
    ### Recommended structure

    **0–10 sec:** The problem  
    **10–20 sec:** The user pain  
    **20–40 sec:** Your future solution  
    **40–50 sec:** Technology  
    **50–60 sec:** WOW factor
    """)

    st.session_state.pitch = st.text_area(
        "Write your pitch",
        value=st.session_state.pitch,
        height=250,
        placeholder="Imagine you are presenting to an investor..."
    )

    if st.button("🎤 START 60-SECOND TIMER"):

        start_timer(1, "60-Second Pitch")

    st.markdown(
        f"<div class='timer'>{timer_display()}</div>",
        unsafe_allow_html=True
    )

    if st.button(
        "🏁 SUBMIT TEAM CHALLENGE",
        type="primary",
        use_container_width=True
    ):

        st.session_state.submitted = True
        go("submission")


# ============================================================
# SUBMISSION
# ============================================================

elif st.session_state.page == "submission":

    st.markdown("# 🏆 TEAM SUBMISSION")

    if st.session_state.submitted:

        st.markdown(
            """
            <div class="success-box">
                <h2>🎉 Challenge Submitted!</h2>
                <p>Your team has completed the UX Beyond Today challenge.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    c = st.session_state.challenge

    st.markdown("## 📋 Your Case")

    st.write("### Team")
    st.write(st.session_state.team_name)

    st.write("### Members")
    st.write(", ".join(st.session_state.members))

    st.write("### Challenge")
    st.write(c["domain"])

    st.write("### How Might We...")
    st.write(st.session_state.how_might_we)

    st.write("### Selected Idea")
    st.write(st.session_state.selected_idea)

    st.write("### Solution")
    st.write(st.session_state.solution)

    st.write("### Technology")
    st.write(st.session_state.technology)

    st.write("### User Experience")
    st.write(st.session_state.experience)

    st.write("### WOW Factor")
    st.write(st.session_state.wow)

    st.write("### 60-Second Pitch")
    st.write(st.session_state.pitch)

    # --------------------------------------------------------
    # DOWNLOAD JSON
    # --------------------------------------------------------

    submission = {
        "team": st.session_state.team_name,
        "members": st.session_state.members,
        "challenge": c["domain"],
        "problem": c["context"],
        "five_whys": st.session_state.why_answers,
        "how_might_we": st.session_state.how_might_we,
        "ideas": st.session_state.ideas,
        "selected_idea": st.session_state.selected_idea,
        "solution": st.session_state.solution,
        "technology": st.session_state.technology,
        "experience": st.session_state.experience,
        "wow_factor": st.session_state.wow,
        "pitch": st.session_state.pitch,
        "submitted_at": datetime.now().isoformat()
    }

    st.download_button(
        "📥 Download Team Submission",
        data=json.dumps(submission, indent=4),
        file_name=f"{st.session_state.team_name}_UX_Challenge.json",
        mime="application/json",
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("""
    # 🧠 What did you actually learn?

    You started with:

    **A PROBLEM**

    Then you moved through:

    **USER → PAIN → WHY → REFRAME → IDEAS → FUTURE EXPERIENCE**

    And that is exactly where **UX begins.**
    """)

    if st.button("🔄 Start Another Challenge"):

        st.session_state.challenge = random.choice(CHALLENGES)
        st.session_state.ideas = []
        st.session_state.why_answers = ["", "", "", "", ""]
        st.session_state.how_might_we = ""
        st.session_state.selected_idea = ""
        st.session_state.solution = ""
        st.session_state.technology = ""
        st.session_state.experience = ""
        st.session_state.wow = ""
        st.session_state.pitch = ""
        st.session_state.submitted = False

        go("challenge")