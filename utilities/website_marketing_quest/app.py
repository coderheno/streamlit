import os
import json
import sqlite3
import random
import csv
import io
from datetime import datetime
from pathlib import Path

import streamlit as st

# ============================================================
# WEBSITE MARKETING QUEST
# Streamlit gamified workshop app for BBA Marketing students
# ============================================================

APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "quest_data.db"

st.set_page_config(
    page_title="Website Marketing Quest",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0b1020 0%, #15152d 55%, #21143b 100%);
        color: #ffffff !important;
    }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .block-container { padding-top: 1.5rem; max-width: 1250px; }
    .stSidebar {
        background: #f2f2f2;
    }
    .stSidebar * {
        color: #000000 !important;
    }
    .stSidebar [data-testid="stBaseButton-secondary"],
    .stSidebar [data-testid="stBaseButton-primary"],
    .stSidebar .stSelectbox div,
    .stSidebar .stRadio div,
    .stSidebar .stTextInput input,
    .stSidebar .stTextArea textarea,
    .stSidebar .stNumberInput input,
    .stSidebar .stDateInput input,
    .stSidebar .stSelectbox input,
    .stSidebar .stMarkdown,
    .stSidebar label {
        color: #000000 !important;
    }
    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input,
    .stDateInput input,
    .stSelectbox div[data-baseweb="select"] {
        color: #000000 !important;
        background: #ffffff !important;
    }
    .hero {
        padding: 1.6rem 1.8rem; border-radius: 22px;
        background: linear-gradient(115deg, #38206c, #183b65 60%, #11645f);
        border: 1px solid rgba(255,255,255,.15); margin-bottom: 1rem;
    }
    .hero h1 { color: white; margin: 0; font-size: 2.25rem; }
    .hero p { color: #ffffff; margin: .4rem 0 0 0; }
    .metric-card {
        background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.12);
        border-radius: 16px; padding: 1rem; min-height: 105px;
    }
    .metric-number { font-size: 1.8rem; font-weight: 800; color: #fff; }
    .metric-label { color: #ffffff; font-size: .85rem; }
    .mission-card {
        background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.13);
        border-radius: 16px; padding: 1rem; min-height: 150px;
    }
    .tag {
        display:inline-block; padding: .18rem .55rem; border-radius: 20px;
        background: #263b58; color: #dbeafe; font-size: .75rem; margin-bottom: .4rem;
    }
    .small-muted { color: #ffffff; font-size: .88rem; }
    div.stButton > button { border-radius: 10px; font-weight: 650; }
    .leader-row { padding:.55rem .8rem; border-radius:10px; background:rgba(255,255,255,.06); margin:.25rem 0; }
</style>
""", unsafe_allow_html=True)

# ---------- Database ----------
def db_connect():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=20)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db_connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS teams (
                team_name TEXT PRIMARY KEY,
                business_name TEXT DEFAULT '',
                audience TEXT DEFAULT '',
                usp TEXT DEFAULT '',
                points INTEGER DEFAULT 0,
                badges TEXT DEFAULT '',
                updated_at TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                team_name TEXT,
                mission TEXT,
                answer TEXT,
                points INTEGER,
                submitted_at TEXT
            )
        """)
        conn.commit()

def get_teams():
    with db_connect() as conn:
        return conn.execute(
            "SELECT * FROM teams ORDER BY points DESC, team_name ASC"
        ).fetchall()

def ensure_team(team):
    with db_connect() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO teams(team_name, updated_at) VALUES (?, ?)",
            (team, datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()

def update_business(team, business, audience, usp):
    with db_connect() as conn:
        conn.execute("""
            UPDATE teams SET business_name=?, audience=?, usp=?, updated_at=?
            WHERE team_name=?
        """, (business, audience, usp, datetime.now().isoformat(timespec="seconds"), team))
        conn.commit()

def award_points(team, mission, answer, points, badge=None):
    with db_connect() as conn:
        row = conn.execute("SELECT badges FROM teams WHERE team_name=?", (team,)).fetchone()
        existing = set(filter(None, (row["badges"] or "").split("|"))) if row else set()
        if badge:
            existing.add(badge)
        conn.execute("""
            UPDATE teams SET points=points+?, badges=?, updated_at=? WHERE team_name=?
        """, (points, "|".join(sorted(existing)), datetime.now().isoformat(timespec="seconds"), team))
        conn.execute("""
            INSERT INTO submissions(team_name, mission, answer, points, submitted_at)
            VALUES (?, ?, ?, ?, ?)
        """, (team, mission, answer[:4000], points, datetime.now().isoformat(timespec="seconds")))
        conn.commit()

def get_submissions():
    with db_connect() as conn:
        return conn.execute(
            "SELECT * FROM submissions ORDER BY id DESC LIMIT 200"
        ).fetchall()

def reset_database():
    with db_connect() as conn:
        conn.execute("DELETE FROM submissions")
        conn.execute("DELETE FROM teams")
        conn.commit()

init_db()

# ---------- Content ----------
MISSIONS = [
    ("🚀", "Startup Challenge", "Define a business idea, audience and unique selling proposition.", 100),
    ("🎨", "Landing Page Lab", "Plan a persuasive landing page and its call-to-action.", 150),
    ("🕵️", "Database Detective", "Understand how customer enquiries become structured data.", 100),
    ("🧩", "Technology Explorer", "Match web technologies to their roles.", 100),
    ("🧠", "AI Marketing Consultant", "Use AI to strengthen your marketing message and SEO.", 150),
    ("🏆", "Next.js Boss Level", "Pitch a modern, search-friendly website experience.", 200),
]

TECH_QUESTIONS = [
    ("Which technology defines the structure and content of a webpage?", ["CSS", "HTML", "MongoDB", "Express"], "HTML",
     "HTML provides the page structure: headings, paragraphs, images, links and forms."),
    ("Which technology controls colours, spacing, layout and typography?", ["JavaScript", "Node.js", "CSS", "MongoDB"], "CSS",
     "CSS controls visual presentation and responsive layout."),
    ("Which technology adds behaviour such as menu toggles and form validation?", ["JavaScript", "HTML", "MongoDB", "Next.js"], "JavaScript",
     "JavaScript adds client-side interactivity and can communicate with APIs."),
    ("Which component is commonly used to build APIs in the MERN stack?", ["React", "Express.js", "MongoDB", "CSS"], "Express.js",
     "Express.js is a Node.js web framework often used to create backend routes and APIs."),
    ("Which MERN component stores documents such as products and customer records?", ["React", "Node.js", "MongoDB", "HTML"], "MongoDB",
     "MongoDB is a document-oriented database that can store product and customer records."),
    ("Which library is used to build component-based user interfaces?", ["React", "Express", "MongoDB", "SQL"], "React",
     "React helps developers build interfaces from reusable components."),
    ("Which React-based framework offers features useful for SEO and server rendering?", ["Bootstrap", "Next.js", "jQuery", "SQLite"], "Next.js",
     "Next.js adds routing and rendering capabilities that can support discoverability and performance."),
]

DB_QUESTIONS = [
    ("A visitor submits their name and email through an enquiry form. What should happen next?",
     ["The details disappear", "The browser stores it forever automatically",
      "The website sends the data securely to a backend/API for validation and storage", "The CSS file stores it"],
     "The website sends the data securely to a backend/API for validation and storage",
     "A frontend form usually sends data to a backend endpoint. The backend validates it and stores it in a database."),
    ("Which field is most useful as a unique identifier for each customer record?",
     ["Favourite colour", "Customer ID", "Page background", "Banner text"],
     "Customer ID", "A unique ID helps distinguish records even when two customers share the same name."),
    ("Which practice is important when collecting customer data?",
     ["Collect everything possible", "Share all data publicly", "Collect only necessary data and explain its use", "Store passwords as plain text"],
     "Collect only necessary data and explain its use",
     "Data minimisation, transparency and secure handling are important principles of responsible data collection."),
]

def call_gemini(prompt, system_instruction="You are a helpful digital marketing and web technology mentor for final-year BBA students. Use clear, practical language."):
    """Optional Gemini integration. Add GEMINI_API_KEY to Streamlit secrets."""
    api_key = None
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", None)
    except Exception:
        api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None, "Gemini API key not configured. Add GEMINI_API_KEY to .streamlit/secrets.toml."

    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{system_instruction}\n\n{prompt}"
        )
        return response.text, None
    except Exception as exc:
        return None, f"AI request failed: {exc}"

def render_header():
    st.markdown("""
    <div class="hero">
      <div class="tag">BBA MARKETING • INTERACTIVE EXPERT SESSION</div>
      <h1>🚀 WEBSITE MARKETING QUEST</h1>
      <p>Build • Market • Innovate • Win — turn a business idea into a digital experience.</p>
    </div>
    """, unsafe_allow_html=True)

def metric_card(label, value):
    st.markdown(
        f'<div class="metric-card"><div class="metric-number">{value}</div>'
        f'<div class="metric-label">{label}</div></div>',
        unsafe_allow_html=True
    )

# ---------- Sidebar ----------
render_header()
with st.sidebar:
    st.title("🧭 Quest Navigation")
    page = st.radio(
        "Choose a zone",
        ["🏠 Quest Home", "🚀 Mission 1: Startup", "🎨 Mission 2: Landing Page",
         "🕵️ Mission 3: Database", "🧩 Mission 4: Tech Explorer",
         "🧠 Mission 5: AI Mentor", "🏆 Mission 6: Next.js",
         "🥇 Live Leaderboard", "👨‍🏫 Faculty Control"]
    )
    st.divider()
    st.caption("Facilitator: Dr. Vijay Arputharaj J")
    st.caption("School of Business & Management | BBA Marketing")

# ---------- Team identity ----------
team_names = [f"Team {name}" for name in [
    "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
    "Golf", "Hotel", "India", "Juliet", "Kilo"
]]
with st.sidebar:
    selected_team = st.selectbox("Your team", team_names)
    ensure_team(selected_team)
    st.caption("Use the same team name on every device.")

# ---------- Home ----------
if page == "🏠 Quest Home":
    teams = get_teams()
    my_team = next((t for t in teams if t["team_name"] == selected_team), None)
    cols = st.columns(3)
    with cols[0]: metric_card("YOUR TEAM XP", my_team["points"] if my_team else 0)
    with cols[1]: metric_card("TEAMS REGISTERED", len(teams))
    with cols[2]: metric_card("QUEST MISSIONS", 6)

    st.subheader("🎯 Your mission map")
    c1, c2, c3 = st.columns(3)
    for i, (icon, title, desc, xp) in enumerate(MISSIONS):
        with [c1, c2, c3][i % 3]:
            st.markdown(f"""
            <div class="mission-card">
              <div style="font-size:1.8rem">{icon}</div>
              <b>{title}</b><br/>
              <span class="small-muted">{desc}</span><br/><br/>
              <span class="tag">UP TO {xp} XP</span>
            </div>
            """, unsafe_allow_html=True)
    st.info("Start with Mission 1. Complete the challenges in sequence and watch your team climb the leaderboard.")
    st.subheader("💡 The big idea")
    st.write("A website is more than an online brochure. It can attract visitors, explain value, collect enquiries, support customer relationships and help a business grow.")
    st.markdown("**Today's journey:** Business idea → Landing page → Customer data → Interactive experience → MERN architecture → Next.js and SEO.")

# ---------- Mission 1 ----------
elif page == "🚀 Mission 1: Startup":
    st.title("🚀 Mission 1 — Startup Challenge")
    st.write("You have ₹10,000 to launch a small business. Define the business before building its website.")
    with st.form("startup_form"):
        business = st.text_input("Business / brand name", placeholder="e.g., GreenBite")
        category = st.selectbox("Business category", ["Food & beverages", "Fashion & lifestyle", "Travel & tourism",
            "Education", "Fitness & wellness", "Local products", "Other"])
        audience = st.text_input("Who is your target customer?", placeholder="e.g., College students looking for healthy snacks")
        product = st.text_area("What product or service will you offer?")
        usp = st.text_area("What makes your business different? (USP)")
        submitted = st.form_submit_button("Submit startup profile and earn 100 XP", type="primary")

    st.markdown("""
    <style>
        div[data-testid="stForm"] label,
        div[data-testid="stForm"] .stTextInput label,
        div[data-testid="stForm"] .stTextArea label,
        div[data-testid="stForm"] .stSelectbox label {
            color: #ffffff !important;
        }
        div[data-testid="stForm"] .stTextInput input,
        div[data-testid="stForm"] .stTextArea textarea,
        div[data-testid="stForm"] .stSelectbox div[data-baseweb="select"] {
            color: #000000 !important;
            background: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    if submitted:
        if not business.strip() or not audience.strip() or not usp.strip():
            st.error("Please complete the brand name, target audience and USP.")
        else:
            update_business(selected_team, business, audience, usp)
            answer = f"Brand: {business}; Category: {category}; Audience: {audience}; Product: {product}; USP: {usp}"
            award_points(selected_team, "Startup Challenge", answer, 100, "Startup Sprinter")
            st.success("Startup profile submitted! +100 XP. Badge unlocked: Startup Sprinter.")
            st.balloons()

    st.markdown("""
    <style>
        div[data-testid="stButton"] > button {
            background: #6b7280 !important;
            border: 1px solid #9ca3af !important;
            color: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    if st.button("✨ Ask AI to improve our USP"):
        record = next((t for t in get_teams() if t["team_name"] == selected_team), None)
        if record and record["business_name"]:
            result, err = call_gemini(
                f"Improve this business USP in 3 alternative concise versions. Brand: {record['business_name']}. "
                f"Target audience: {record['audience']}. Current USP: {record['usp']}"
            )
            if result: st.write(result)
            else: st.warning(err)
        else:
            st.warning("Submit your startup profile first.")

# ---------- Mission 2 ----------
elif page == "🎨 Mission 2: Landing Page":
    st.title("🎨 Mission 2 — Landing Page Lab")
    st.write("A landing page has one primary job: persuade the visitor to take a useful next step.")
    team = next((t for t in get_teams() if t["team_name"] == selected_team), None)
    if team and team["business_name"]:
        st.caption(f"Your brand: **{team['business_name']}** | Audience: {team['audience']}")
    with st.form("landing_form"):
        headline = st.text_input("Hero headline", placeholder="Fresh choices. Better living.")
        subheadline = st.text_area("Supporting message", placeholder="Explain the value in one or two sentences.")
        cta = st.selectbox("Primary call-to-action", ["Shop Now", "Book a Demo", "Register Now", "Get a Quote", "Contact Us"])
        sections = st.multiselect("Choose sections for your page", ["About", "Products / Services", "Benefits", "Testimonials", "Pricing", "FAQ", "Contact"], default=["About", "Products / Services", "Contact"])
        submitted = st.form_submit_button("Submit landing page plan and earn 150 XP", type="primary")

    st.markdown("""
    <style>
        div[data-testid="stForm"] label,
        div[data-testid="stForm"] .stTextInput label,
        div[data-testid="stForm"] .stTextArea label,
        div[data-testid="stForm"] .stSelectbox label,
        div[data-testid="stForm"] .stMultiSelect label {
            color: #ffffff !important;
        }
        div[data-testid="stForm"] .stTextInput input,
        div[data-testid="stForm"] .stTextArea textarea,
        div[data-testid="stForm"] .stSelectbox div[data-baseweb="select"],
        div[data-testid="stForm"] .stMultiSelect div {
            color: #000000 !important;
            background: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    if submitted:
        if not headline.strip() or not subheadline.strip():
            st.error("Add a headline and supporting message.")
        else:
            answer = f"Headline: {headline}; Message: {subheadline}; CTA: {cta}; Sections: {', '.join(sections)}"
            award_points(selected_team, "Landing Page Lab", answer, 150, "Landing Page Designer")
            st.success("Landing page plan submitted! +150 XP. Badge unlocked: Landing Page Designer.")
            st.balloons()

    st.subheader("👀 Live landing-page preview")
    preview_headline = st.session_state.get("preview_headline", "")
    # Preview uses the latest values entered only after a submission.
    latest = next((s for s in get_submissions() if s["team_name"] == selected_team and s["mission"] == "Landing Page Lab"), None)
    if latest:
        try:
            import re
            h = re.search(r"Headline: (.*?); Message:", latest["answer"]).group(1)
            m = re.search(r"Message: (.*?); CTA:", latest["answer"]).group(1)
            b = re.search(r"CTA: (.*?); Sections:", latest["answer"]).group(1)
            st.markdown(f"""
            <div style="background:linear-gradient(120deg,#173b5d,#286b68);padding:2rem;border-radius:18px;color:white;text-align:center">
              <div style="font-size:2rem;font-weight:800">{h}</div>
              <p style="font-size:1.05rem">{m}</p>
              <span style="display:inline-block;background:#fbbf24;color:#111827;padding:.6rem 1.2rem;border-radius:9px;font-weight:800">{b}</span>
            </div>
            """, unsafe_allow_html=True)
        except Exception:
            st.caption("Submit your plan to display the preview.")

    st.subheader("🤖 AI copywriting assistant")
    ai_topic = st.text_input("What should AI help write?", placeholder="e.g., 3 catchy headlines for our organic snack brand")
    st.markdown("""
    <style>
        div[data-testid="stTextInput"] label,
        div[data-testid="stTextInput"] .stTextInput label {
            color: #ffffff !important;
        }
        div[data-testid="stTextInput"] input {
            color: #000000 !important;
            background: #ffffff !important;
        }
        div[data-testid="stBaseButton-secondary"] > button,
        div[data-testid="stBaseButton-primary"] > button,
        div.stButton > button {
            background: #6b7280 !important;
            border: 1px solid #9ca3af !important;
            color: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    if st.button("Generate marketing copy"):
        if ai_topic.strip():
            result, err = call_gemini(ai_topic + ". Give concise options suitable for a student business landing page.")
            if result: st.write(result)
            else: st.warning(err)
        else:
            st.warning("Enter a request for the AI assistant.")

# ---------- Mission 3 ----------
elif page == "🕵️ Mission 3: Database":
    st.title("🕵️ Mission 3 — Database Detective")
    st.write("A visitor submits an enquiry. How does that information travel from a webpage to a database?")
    st.code("Customer form → JavaScript fetch() → Express API → Validation → Database", language="text")
    st.caption("In a real application, the backend should validate inputs, protect personal data and securely store only necessary information.")
    if f"db_q_{selected_team}" not in st.session_state:
        st.session_state[f"db_q_{selected_team}"] = 0
    q_index = st.session_state[f"db_q_{selected_team}"]
    if q_index < len(DB_QUESTIONS):
        question, options, correct, explanation = DB_QUESTIONS[q_index]
        st.markdown(f"**Question {q_index + 1} of {len(DB_QUESTIONS)}**")
        st.markdown("""
        <style>
            div[data-testid="stRadio"] label,
            div[data-testid="stRadio"] .stRadio label,
            div[data-testid="stRadio"] div[role="radiogroup"],
            div[data-testid="stRadio"] .stMarkdownContainer {
                color: #ffffff !important;
            }
            div[data-testid="stRadio"] input {
                accent-color: #ffffff !important;
            }
        </style>
        """, unsafe_allow_html=True)
        answer = st.radio(question, options, key=f"db_answer_{selected_team}_{q_index}")
        st.markdown("""
        <style>
            div[data-testid="stButton"] > button {
                background: #6b7280 !important;
                border: 1px solid #9ca3af !important;
                color: #ffffff !important;
            }
        </style>
        """, unsafe_allow_html=True)
        if st.button("Check answer", key=f"db_check_{selected_team}_{q_index}"):
            if answer == correct:
                award_points(selected_team, "Database Detective", answer, 35, "Data Detective")
                st.success("Correct! +35 XP")
            else:
                st.error("Not quite. Review the explanation and try the next question.")
            st.info(explanation)
            st.session_state[f"db_q_{selected_team}"] += 1
            st.rerun()
    else:
        st.success("Database Detective challenge completed!")
        st.markdown("""
        <style>
            div[data-testid="stButton"] > button {
                background: #6b7280 !important;
                border: 1px solid #9ca3af !important;
                color: #ffffff !important;
            }
        </style>
        """, unsafe_allow_html=True)
        if st.button("Restart database quiz"):
            st.session_state[f"db_q_{selected_team}"] = 0
            st.rerun()
    st.markdown("**Remember:** Never store passwords in plain text. Use secure authentication, access controls and responsible data practices.")

# ---------- Mission 4 ----------
elif page == "🧩 Mission 4: Tech Explorer":
    st.title("🧩 Mission 4 — Technology Explorer")
    st.write("Match each web technology with its role. Each correct answer earns 20 XP.")
    if f"tech_q_{selected_team}" not in st.session_state:
        st.session_state[f"tech_q_{selected_team}"] = 0
    q_index = st.session_state[f"tech_q_{selected_team}"]
    if q_index < len(TECH_QUESTIONS):
        question, options, correct, explanation = TECH_QUESTIONS[q_index]
        st.markdown(f"**Challenge {q_index + 1} of {len(TECH_QUESTIONS)}**")
        st.markdown("""
        <style>
            div[data-testid="stRadio"] label,
            div[data-testid="stRadio"] .stRadio label,
            div[data-testid="stRadio"] div[role="radiogroup"],
            div[data-testid="stRadio"] .stMarkdownContainer,
            div[data-testid="stRadio"] span,
            div[data-testid="stRadio"] p {
                color: #ffffff !important;
            }
            div[data-testid="stRadio"] input {
                accent-color: #ffffff !important;
            }
        </style>
        """, unsafe_allow_html=True)
        answer = st.radio(question, options, key=f"tech_answer_{selected_team}_{q_index}")
        st.markdown("""
        <style>
            div[data-testid="stButton"] > button {
                background: #6b7280 !important;
                border: 1px solid #9ca3af !important;
                color: #ffffff !important;
            }
        </style>
        """, unsafe_allow_html=True)
        if st.button("Lock answer", key=f"tech_check_{selected_team}_{q_index}"):
            if answer == correct:
                award_points(selected_team, "Technology Explorer", answer, 20, "Tech Explorer")
                st.success("Correct! +20 XP")
            else:
                st.error(f"Incorrect. Correct answer: {correct}")
            st.info(explanation)
            st.session_state[f"tech_q_{selected_team}"] += 1
            st.rerun()
    else:
        st.success("Technology Explorer completed!")
        if st.button("Restart technology challenge"):
            st.session_state[f"tech_q_{selected_team}"] = 0
            st.rerun()
    with st.expander("Explore the MERN stack"):
        st.markdown("""
        - **MongoDB:** stores application data.
        - **Express.js:** creates backend routes and APIs.
        - **React.js:** builds the interactive user interface.
        - **Node.js:** runs JavaScript on the server.
        """)
        st.info("Next.js is a React-based framework. It adds routing and rendering options that can help build performant, search-friendly websites.")

# ---------- Mission 5 ----------
elif page == "🧠 Mission 5: AI Mentor":
    st.title("🧠 Mission 5 — AI Marketing Consultant")
    st.write("Ask the AI mentor to act as a marketing strategist, copywriter or SEO coach.")
    team = next((t for t in get_teams() if t["team_name"] == selected_team), None)
    if team and team["business_name"]:
        st.info(f"Current business: {team['business_name']} | Target audience: {team['audience']}")
    st.markdown("""
    <style>
        div[data-testid="stSelectbox"] label,
        div[data-testid="stTextArea"] label,
        div[data-testid="stSelectbox"] .stSelectbox label,
        div[data-testid="stTextArea"] .stTextArea label {
            color: #ffffff !important;
        }
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stSelectbox"] div[data-baseweb="select"] {
            color: #000000 !important;
            background: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    role = st.selectbox("Choose your AI mentor", ["Marketing Strategist", "Landing Page Copywriter", "SEO Coach", "Customer Experience Consultant"])
    prompt = st.text_area("Your question", placeholder="Suggest five SEO keywords and a meta description for our business...")
    if st.button("Ask AI Mentor", type="primary"):
        if not prompt.strip():
            st.warning("Enter a question first.")
        else:
            business_context = ""
            if team:
                business_context = f" Business: {team['business_name']}. Audience: {team['audience']}. USP: {team['usp']}."
            full_prompt = f"Act as a {role} for a student-run business.{business_context}\nUser request: {prompt}\nGive practical, concise, ethical advice."
            with st.spinner("AI mentor is thinking..."):
                result, err = call_gemini(full_prompt)
            if result:
                st.markdown("### 💬 Mentor response")
                st.write(result)
                st.caption("AI-generated suggestions should be reviewed for accuracy and suitability.")
                if st.button("Claim 50 XP for completing AI consultation"):
                    award_points(selected_team, "AI Marketing Consultant", prompt, 50, "AI Innovator")
                    st.success("50 XP awarded!")
            else:
                st.warning(err)
                st.markdown("**Offline prompt challenge:** Discuss your question with your team and write three recommendations. Your facilitator can award points manually.")

# ---------- Mission 6 ----------
elif page == "🏆 Mission 6: Next.js":
    st.title("🏆 Mission 6 — Next.js Boss Level")
    st.write("Your challenge: transform your business idea into a professional website that can be discovered through search engines.")
    st.markdown("""
    **Your team pitch must cover:**
    1. What is the main goal of the website?
    2. Who is the intended customer?
    3. What are the three most important pages?
    4. What search phrase should help customers find the business?
    5. What action should visitors take?
    6. How will you make the experience mobile-friendly and accessible?
    """)
    st.info("Next.js is built on React. Features such as server rendering, static generation and metadata support can help teams create performant, search-friendly experiences. SEO still depends on useful content, technical quality and relevance.")
    st.markdown("""
    <style>
        div[data-testid="stTextArea"] label,
        div[data-testid="stTextInput"] label,
        div[data-testid="stTextArea"] .stTextArea label,
        div[data-testid="stTextInput"] .stTextInput label {
            color: #ffffff !important;
        }
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stTextInput"] input {
            color: #000000 !important;
            background: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    with st.form("nextjs_pitch"):
        pitch = st.text_area("Submit your team's Next.js website pitch", height=180,
            placeholder="Our website will help... Our target customers are... The main pages are...")
        keywords = st.text_input("One primary SEO keyword or search phrase")
        meta = st.text_area("Draft a meta description (around 150–160 characters)")
        submit = st.form_submit_button("Submit Boss Level pitch and earn 200 XP", type="primary")
    if submit:
        if len(pitch.strip()) < 40 or not keywords.strip():
            st.error("Please provide a more detailed pitch and one SEO keyword.")
        else:
            answer = f"Pitch: {pitch}; Keyword: {keywords}; Meta: {meta}"
            award_points(selected_team, "Next.js Boss Level", answer, 200, "Next.js Champion")
            st.success("Boss Level pitch submitted! +200 XP. Badge unlocked: Next.js Champion.")
            st.balloons()
    st.markdown("""
    <style>
        div[data-testid="stButton"] > button {
            background: #6b7280 !important;
            border: 1px solid #9ca3af !important;
            color: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
    if st.button("🤖 Get AI feedback on our pitch"):
        latest = next((s for s in get_submissions() if s["team_name"] == selected_team and s["mission"] == "Next.js Boss Level"), None)
        if latest:
            result, err = call_gemini("Review this student website pitch. Score it out of 10 for clarity, audience fit, SEO thinking, CTA and mobile experience. Give 3 improvements.\n" + latest["answer"])
            if result: st.write(result)
            else: st.warning(err)
        else:
            st.warning("Submit your pitch first.")

# ---------- Leaderboard ----------
elif page == "🥇 Live Leaderboard":
    st.title("🥇 Live Team Leaderboard")
    st.caption("Scores update when teams submit mission activities. Refresh the page to see the latest rankings.")
    teams = get_teams()
    if teams:
        top = teams[0]["points"]
        for rank, team in enumerate(teams, start=1):
            medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"#{rank}"
            st.markdown(
                f'<div class="leader-row"><b>{medal} {team["team_name"]}</b>'
                f'<span style="float:right;font-weight:800">{team["points"]} XP</span><br/>'
                f'<span class="small-muted">{team["business_name"] or "Startup idea not submitted"}</span></div>',
                unsafe_allow_html=True
            )
            if top:
                st.progress(min(team["points"] / top, 1.0))
    else:
        st.info("No teams have joined yet.")
    st.subheader("🏅 Badges earned")
    for team in teams:
        badges = [b for b in (team["badges"] or "").split("|") if b]
        if badges:
            st.write(f"**{team['team_name']}:** " + " · ".join("🏅 " + b for b in badges))

# ---------- Faculty ----------
elif page == "👨‍🏫 Faculty Control":
    st.title("👨‍🏫 Faculty Control Panel")
    st.warning("Faculty-only area. Set a password using FACULTY_PASSWORD in Streamlit secrets or an environment variable.")
    password_expected = None
    try:
        password_expected = st.secrets.get("FACULTY_PASSWORD", None)
    except Exception:
        password_expected = os.getenv("FACULTY_PASSWORD")
    if not password_expected:
        st.error("Faculty password is not configured. Add FACULTY_PASSWORD to secrets before deployment.")
    entered = st.text_input("Faculty password", type="password")
    if password_expected and entered == password_expected:
        st.success("Faculty access granted.")
        teams = get_teams()
        st.subheader("Session summary")
        a, b, c = st.columns(3)
        with a: metric_card("REGISTERED TEAMS", len(teams))
        with b: metric_card("TOTAL XP AWARDED", sum(t["points"] for t in teams))
        with c: metric_card("SUBMISSIONS", len(get_submissions()))
        st.subheader("Award bonus points")
        with st.form("bonus_form"):
            target = st.selectbox("Team", [t["team_name"] for t in teams] or team_names)
            bonus = st.number_input("Bonus XP", min_value=0, max_value=500, value=25, step=5)
            reason = st.text_input("Reason")
            give = st.form_submit_button("Award bonus")
        if give and bonus > 0:
            award_points(target, "Faculty Bonus", reason or "Faculty-awarded bonus", int(bonus), "Bonus Achiever")
            st.success(f"Awarded {bonus} XP to {target}.")
            st.rerun()

        st.subheader("Recent submissions")
        rows = get_submissions()
        if rows:
            st.dataframe([dict(r) for r in rows], use_container_width=True, hide_index=True)
            csv_buffer = io.StringIO()
            writer = csv.DictWriter(csv_buffer, fieldnames=list(dict(rows[0]).keys()))
            writer.writeheader()
            writer.writerows([dict(r) for r in rows])
            st.download_button("⬇️ Download submissions CSV", csv_buffer.getvalue(),
                               file_name="website_marketing_quest_submissions.csv", mime="text/csv")
        else:
            st.info("No submissions yet.")

        st.subheader("Reset session")
        st.caption("This permanently clears all team scores and submissions from this app's local SQLite database.")
        confirm = st.checkbox("I understand that resetting deletes all quest data.")
        if st.button("🗑️ Reset all scores and submissions", disabled=not confirm):
            reset_database()
            st.success("Quest data reset.")
            st.rerun()

st.divider()
st.markdown(
    '<p class="small-muted" style="text-align:center">Website Marketing Quest • Built with Streamlit • '
    'Learning by building, experimenting and marketing.</p>',
    unsafe_allow_html=True
)
