
import streamlit as st

st.set_page_config(
    page_title="UI/UX Quest — Unit 1",
    page_icon="🎮",
    layout="wide"
)

# -----------------------------
# Theme
# -----------------------------
st.markdown("""
<style>
    :root{
        --bg: #0f1724;
        --surface: rgba(255,255,255,0.04);
        --card-bg: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
        --text: #e6eef8;
        --muted: #a8b3c7;
        --accent: #7c5cff;
        --success: #8bc48b;
        --danger: #e37b7b;
    }

    .main-title {
        font-size: 2.6rem;
        font-weight: 900;
        margin-bottom: 0.2rem;
        color: var(--text);
        background: linear-gradient(90deg, var(--accent), #4cc9f0);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    .subtitle {
        color: var(--muted);
        font-size: 1.05rem;
        margin-bottom: 1.2rem;
    }
    .quest-card {
        padding: 1rem 1.2rem;
        border-radius: 14px;
        margin-bottom: 0.8rem;
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.06);
        color: var(--text);
        box-shadow: 0 6px 18px rgba(2,6,23,0.6);
        transition: transform .12s ease, box-shadow .12s ease;
    }
    /* Mission text: force black and bold per request */
    .quest-card h3,
    .quest-card b,
    .quest-card small {
        color: #000 !important;
        font-weight: 800 !important;
    }
    .quest-card:hover{ transform: translateY(-4px); box-shadow: 0 12px 30px rgba(2,6,23,0.8); }
    .xp { font-size: 1.15rem; font-weight: 700; color: var(--text); }
    .badge { display: inline-block; padding: 0.35rem 0.7rem; margin: 0.2rem; border-radius: 999px; background: rgba(255,255,255,0.03); color: var(--text); font-weight: 700; border: 1px solid rgba(255,255,255,0.04); }
    .correct { padding: 0.7rem; border-radius: 10px; border: 1px solid var(--success); background: rgba(139,196,139,0.08); color: var(--text); }
    .wrong { padding: 0.7rem; border-radius: 10px; border: 1px solid var(--danger); background: rgba(227,123,123,0.06); color: var(--text); }

    /* small helpers */
    .muted { color: var(--muted); }
    .accent-btn { background: linear-gradient(90deg,var(--accent), #4cc9f0); color: white; padding: 0.45rem 0.9rem; border-radius: 8px; border: none; }
    .color-swatch { width: 14px; height: 14px; display:inline-block; border-radius:4px; margin-right:6px; vertical-align:middle }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# State
# -----------------------------
defaults = {
    "name": "",
    "xp": 0,
    "completed": set(),
    "answers": {},
    "mission_scores": {},
    "submitted": set(),
    "reflection": "",
    "theme": "Default",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -----------------------------
# Data
# -----------------------------
missions = [
    ("Mission 1", "🧭", "Know Your UX World", "HCI, IxD and UI/UX"),
    ("Mission 2", "🔎", "UX Detective", "Defining UI & good design"),
    ("Mission 3", "🎮", "Interaction Master", "Interaction styles"),
    ("Mission 4", "🖥️", "Interface Architect", "GUI & Web UI"),
    ("Mission 5", "🏆", "Principle Boss Battle", "UI design principles"),
]

questions = {
    "Mission 1": [
        {
            "q": "Which field focuses on the academic and foundational study of how humans interact with technology?",
            "options": ["UI Design", "HCI", "Branding", "Visual Design"],
            "answer": "HCI",
            "why": "The Unit 1 material describes HCI as Human–Computer Interaction and focuses on how humans interact with technology."
        },
        {
            "q": "Which area focuses strongly on the structure and behaviour of interactive systems?",
            "options": ["Interaction Design (IxD)", "Typography", "Graphic Design", "Data Science"],
            "answer": "Interaction Design (IxD)",
            "why": "IxD defines the structure and behaviour of interactive systems and shapes user journeys."
        },
        {
            "q": "Which statement best represents UX?",
            "options": [
                "Only colours and typography",
                "The overall feel, ease, satisfaction and usefulness of a product",
                "Only database performance",
                "Only the computer hardware"
            ],
            "answer": "The overall feel, ease, satisfaction and usefulness of a product",
            "why": "The slides distinguish UI as look/layout and UX as the overall experience."
        },
    ],
    "Mission 2": [
        {
            "q": "A banking interface has clear navigation, reduces user confusion and helps users complete tasks efficiently. Which goal of good design is demonstrated?",
            "options": ["Increasing cognitive load", "Improving usability", "Adding complexity", "Reducing visibility"],
            "answer": "Improving usability",
            "why": "Good design aims to make interactions simple, intuitive and efficient while reducing cognitive load."
        },
        {
            "q": "In HCI, the UI acts primarily as:",
            "options": [
                "A database",
                "A bridge between humans and machines",
                "A programming language",
                "A network protocol"
            ],
            "answer": "A bridge between humans and machines",
            "why": "The material describes the UI as the bridge between human and machine."
        },
        {
            "q": "Which is an OUTPUT component of an interface?",
            "options": ["Keyboard input", "Mouse click", "Visual display", "Voice command"],
            "answer": "Visual display",
            "why": "Output conveys results to users through visual, audio or tactile feedback."
        },
    ],
    "Mission 3": [
        {
            "q": "A user selects an option from a structured list. Which interaction style is this?",
            "options": ["Command Line", "Menu Selection", "Direct Manipulation", "Anthropomorphic"],
            "answer": "Menu Selection",
            "why": "Menu selection uses structured lists of options for decision making."
        },
        {
            "q": "Dragging a file from one folder to another is an example of:",
            "options": ["Direct Manipulation", "Command Line", "Menu Selection", "Form Fill-in"],
            "answer": "Direct Manipulation",
            "why": "Direct manipulation provides interactive, physical-feeling control of screen objects."
        },
        {
            "q": "A conversational AI assistant primarily represents which interaction style in the Unit 1 material?",
            "options": ["Form Fill-in", "Anthropomorphic", "Command Line", "Menu Selection"],
            "answer": "Anthropomorphic",
            "why": "The slides describe anthropomorphic interaction as human-like AI assistants and conversational interfaces."
        },
    ],
    "Mission 4": [
        {
            "q": "Which characteristic of GUI means users work directly with visible interface objects?",
            "options": ["Object Orientation", "Security", "Reliability", "Response Time"],
            "answer": "Object Orientation",
            "why": "GUI object orientation focuses user attention directly on objects and actions."
        },
        {
            "q": "Which GUI characteristic uses visible cues so users do not have to remember commands?",
            "options": ["Concurrent Functions", "Recognition Memory", "System Capability", "Integration"],
            "answer": "Recognition Memory",
            "why": "Recognition memory leverages visible visual cues instead of relying on recall."
        },
        {
            "q": "A web interface is especially concerned with:",
            "options": [
                "Navigation and page hierarchy",
                "Only hardware control",
                "Only command-line syntax",
                "Removing all visual information"
            ],
            "answer": "Navigation and page hierarchy",
            "why": "The material identifies intuitive navigation and an easy-to-use page hierarchy as central to web UI."
        },
    ],
    "Mission 5": [
        {
            "q": "A design uses the same button style and behaviour throughout the product. Which principle is strongest?",
            "options": ["Consistency", "Immersion", "Recovery", "Flexibility"],
            "answer": "Consistency",
            "why": "Consistency means maintaining a uniform look, feel and behaviour."
        },
        {
            "q": "A user can easily undo an accidental action. Which principle is demonstrated?",
            "options": ["Recovery", "Aesthetics", "Familiarity", "Directness"],
            "answer": "Recovery",
            "why": "Recovery allows users to recover simply from errors."
        },
        {
            "q": "A designer removes unnecessary steps so users can complete a task faster. Which principle is demonstrated?",
            "options": ["Efficiency", "Immersion", "Compatibility", "Control"],
            "answer": "Efficiency",
            "why": "Efficiency aims to minimise effort and transition time."
        },
    ],
}

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">🎮 UI/UX QUEST — UNIT 1</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Turn Unit 1 into a game: learn, decide, solve, and defeat the final UI/UX boss.</div>',
    unsafe_allow_html=True
)

if not st.session_state.name:
    name = st.text_input("Enter your name to start your quest")
    if st.button("🚀 Start Quest", type="primary"):
        if name.strip():
            st.session_state.name = name.strip()
            st.rerun()
        else:
            st.warning("Please enter your name.")
    st.stop()

# -----------------------------
# Sidebar progress
# -----------------------------
with st.sidebar:
    st.header("🧑‍🎓 Player")
    st.write(st.session_state.name)

    # Theme selector & accent color
    st.markdown("**Theme**")
    theme_choice = st.selectbox("Choose theme", ["Default", "Ocean", "Sunset", "Forest", "Custom"], index=["Default","Ocean","Sunset","Forest","Custom"].index(st.session_state.theme) if st.session_state.theme in ["Default","Ocean","Sunset","Forest","Custom"] else 0)
    st.session_state.theme = theme_choice

    if theme_choice == "Ocean":
        accent = "#2ec4b6"
        bg = "#021124"
    elif theme_choice == "Sunset":
        accent = "#ff6b6b"
        bg = "#1b0b12"
    elif theme_choice == "Forest":
        accent = "#2f9e44"
        bg = "#071607"
    elif theme_choice == "Custom":
        accent = st.color_picker("Pick an accent color", "#7c5cff")
        bg = "#0f1724"
    else:
        accent = "#7c5cff"
        bg = "#0f1724"

    st.markdown(f"<div style='display:flex;align-items:center'><span class='color-swatch' style='background:{accent}'></span><small class='muted'>Accent</small></div>", unsafe_allow_html=True)
    # inject dynamic CSS variables
    st.markdown(f"""<style>:root{{ --accent: {accent}; --bg: {bg}; }}</style>""", unsafe_allow_html=True)

    level = min(5, st.session_state.xp // 60 + 1)
    st.markdown(f"### Level {level}")
    st.progress(min(1.0, st.session_state.xp / 300))
    st.markdown(f'<div class="xp">⭐ {st.session_state.xp} XP</div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("🏅 Badges")
    badges = []
    if "Mission 1" in st.session_state.completed:
        badges.append("🧠 UX Explorer")
    if "Mission 2" in st.session_state.completed:
        badges.append("🔎 UX Detective")
    if "Mission 3" in st.session_state.completed:
        badges.append("🎮 Interaction Master")
    if "Mission 4" in st.session_state.completed:
        badges.append("🖥️ Interface Architect")
    if "Mission 5" in st.session_state.completed:
        badges.append("🏆 UI/UX Boss Slayer")
    if badges:
        for b in badges:
            st.markdown(f'<span class="badge">{b}</span>', unsafe_allow_html=True)
    else:
        st.caption("Complete missions to unlock badges.")

    if st.button("🔄 Restart Quest"):
        for k in ["xp", "completed", "answers", "mission_scores", "submitted"]:
            if k == "completed" or k == "submitted":
                st.session_state[k] = set()
            elif k == "answers" or k == "mission_scores":
                st.session_state[k] = {}
            else:
                st.session_state[k] = 0
        st.rerun()

# -----------------------------
# Main tabs
# -----------------------------
tabs = st.tabs(["🗺️ Quest Map", "📚 Learn", "🎯 Missions", "⚔️ Boss Battle", "📝 Reflection"])

# Quest Map
with tabs[0]:
    st.subheader("Your Quest Map")
    st.write(f"Welcome, **{st.session_state.name}**. Complete all five missions to master the Unit 1 foundations.")

    cols = st.columns(5)
    for i, (m, icon, title, topic) in enumerate(missions):
        with cols[i]:
            done = m in st.session_state.completed
            st.markdown(
                f"""
                <div class="quest-card">
                <h3>{icon} {m}</h3>
                <b>{title}</b><br>
                <small>{topic}</small><br><br>
                {"✅ Completed" if done else "🔒 In progress"}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.info("🎯 Goal: complete the five missions, earn XP, and unlock the final Boss Battle.")

# Learn
with tabs[1]:
    st.subheader("📚 Quick Learn")
    st.caption("Content is based on the uploaded Unit 1 material.")

    with st.expander("01 — HCI, IxD and UI/UX", expanded=True):
        st.markdown("""
        **HCI — Human–Computer Interaction**
        - Foundational study of how humans interact with technology.
        - Brings together computing, psychology, design and social context.

        **IxD — Interaction Design**
        - Defines the structure and behaviour of interactive systems.
        - Focuses on fluid user journeys and interaction behaviour.

        **UI/UX**
        - **UI:** look and layout — visuals, typography and colours.
        - **UX:** overall feel — ease, satisfaction and usefulness.
        """)

    with st.expander("02 — The User Interface & Good Design"):
        st.markdown("""
        The interface is the bridge between humans and machines.

        **Input:** keyboard, mouse, touchscreen, voice commands.  
        **Output:** visual displays, audio or tactile feedback.

        Good design aims for interactions that are:
        - simple
        - intuitive
        - efficient

        It can reduce cognitive load, improve navigation, build trust, support accessibility and strengthen engagement.
        """)

    with st.expander("03 — Interaction Styles"):
        st.markdown("""
        The Unit 1 material introduces:
        - **Command Line** — text-based instructions.
        - **Menu Selection** — structured options.
        - **Form Fill-in** — structured data entry.
        - **Direct Manipulation** — interactive control of screen objects.
        - **Anthropomorphic** — human-like AI assistants and conversational interfaces.
        """)

    with st.expander("04 — GUI & Web UI"):
        st.markdown("""
        **GUI characteristics**
        - Sophisticated visual presentation
        - Pick-and-click interaction
        - Restricted set of options
        - Visualization
        - Object orientation
        - Recognition memory
        - Concurrent functions

        **Web UI**
        - Intuitive navigation
        - Balanced menus, content and linked graphics
        - Clear page hierarchy
        - User movement between pages
        """)

    with st.expander("05 — Principles of UI Design"):
        st.markdown("""
        **Foundation & Usability:** Accessibility, Clarity, Compatibility, Consistency, Simplicity.

        **User Experience:** Aesthetically Pleasing, Control, Directness, Familiarity, Immersion.

        **Performance & Flow:** Efficiency, Flexibility, Recovery, Responsiveness, Operability & Configuration.
        """)

# Missions
with tabs[2]:
    st.subheader("🎯 Mission Challenges")
    selected = st.selectbox(
        "Choose a mission",
        [m[0] for m in missions],
        format_func=lambda x: next(f"{a} — {c}" for a,b,c,d in missions if a == x)
    )

    qs = questions[selected]
    score = 0

    for idx, item in enumerate(qs, 1):
        st.markdown(f"### Question {idx}")
        answer = st.radio(
            item["q"],
            item["options"],
            key=f"{selected}_{idx}"
        )

        if st.button(f"Check Answer {idx}", key=f"check_{selected}_{idx}"):
            st.session_state.submitted.add((selected, idx))
            st.session_state.answers[(selected, idx)] = answer

        if (selected, idx) in st.session_state.submitted:
            chosen = st.session_state.answers.get((selected, idx))
            if chosen == item["answer"]:
                st.markdown(
                    f'<div class="correct">✅ Correct! +10 XP<br><small>{item["why"]}</small></div>',
                    unsafe_allow_html=True
                )
                score += 1
            else:
                st.markdown(
                    f'<div class="wrong">❌ Not quite. Correct answer: <b>{item["answer"]}</b><br><small>{item["why"]}</small></div>',
                    unsafe_allow_html=True
                )

    if st.button("🏁 Complete Mission", type="primary"):
        completed_answers = sum(
            1 for i in range(1, len(qs)+1)
            if (selected, i) in st.session_state.submitted
        )
        correct_answers = sum(
            1 for i, item in enumerate(qs, 1)
            if (selected, i) in st.session_state.submitted
            and st.session_state.answers.get((selected, i)) == item["answer"]
        )

        if completed_answers < len(qs):
            st.warning("Answer and check all questions before completing the mission.")
        elif selected not in st.session_state.completed:
            gained = correct_answers * 10
            st.session_state.xp += gained
            st.session_state.completed.add(selected)
            st.session_state.mission_scores[selected] = correct_answers
            st.success(f"🎉 Mission completed! You earned {gained} XP.")
            st.rerun()
        else:
            st.info("This mission is already completed.")

# Boss Battle
with tabs[3]:
    st.subheader("⚔️ FINAL BOSS — UX DECISION LAB")
    st.write("Apply Unit 1 concepts to real design situations. No memorisation — make the UX decision.")

    boss = [
        {
            "scenario": "A hospital website has 14 menu items on the homepage. Patients struggle to find appointments.",
            "q": "What should the designer investigate first?",
            "options": ["Add more colours", "Improve navigation and hierarchy", "Add animations everywhere", "Increase the number of menu items"],
            "answer": "Improve navigation and hierarchy",
            "why": "The Unit 1 web UI material emphasises intuitive navigation and an easy-to-use page hierarchy."
        },
        {
            "scenario": "A payment button looks different on every screen.",
            "q": "Which principle is being violated?",
            "options": ["Consistency", "Immersion", "Familiarity", "Flexibility"],
            "answer": "Consistency",
            "why": "Consistency requires a uniform look, feel and behaviour."
        },
        {
            "scenario": "A user accidentally deletes a record and cannot undo the action.",
            "q": "Which principle should be strengthened?",
            "options": ["Recovery", "Aesthetics", "Visualization", "Recognition Memory"],
            "answer": "Recovery",
            "why": "Recovery allows users to recover from errors."
        },
        {
            "scenario": "A system requires users to type complex commands, while the same task could be performed by selecting visible options.",
            "q": "Which interaction style could reduce the input barrier for many users?",
            "options": ["Menu Selection", "Command Line", "More typing", "Hidden controls"],
            "answer": "Menu Selection",
            "why": "Menu selection presents structured options for easier decision making."
        },
        {
            "scenario": "A mobile interface uses tiny text and low-contrast controls.",
            "q": "Which principle should be prioritised?",
            "options": ["Accessibility", "Immersion", "Branding", "Concurrent Functions"],
            "answer": "Accessibility",
            "why": "The Unit 1 principles identify accessibility as a foundation of usable design."
        },
    ]

    boss_score = 0
    for i, item in enumerate(boss, 1):
        st.markdown(f"### Boss Challenge {i}")
        st.info(item["scenario"])
        ans = st.radio(item["q"], item["options"], key=f"boss_{i}")
        if st.button(f"Submit Boss Answer {i}", key=f"boss_btn_{i}"):
            st.session_state.answers[("boss", i)] = ans
            st.session_state.submitted.add(("boss", i))

        if ("boss", i) in st.session_state.submitted:
            if st.session_state.answers.get(("boss", i)) == item["answer"]:
                st.success(f"✅ Correct — {item['why']}")
                boss_score += 1
            else:
                st.error(f"❌ Correct answer: {item['answer']} — {item['why']}")

    if st.button("🏆 Claim Boss XP", type="primary"):
        done = sum(1 for i in range(1, 6) if ("boss", i) in st.session_state.submitted)
        if done < 5:
            st.warning("Complete all five boss challenges first.")
        elif "boss_completed" not in st.session_state.completed:
            st.session_state.xp += boss_score * 15
            st.session_state.completed.add("boss_completed")
            st.success(f"🏆 Boss Battle complete! +{boss_score * 15} XP")
            if boss_score == 5:
                st.balloons()

# Reflection
with tabs[4]:
    st.subheader("📝 Exit Reflection")
    st.write("Use this after completing the learning missions.")
    reflection = st.text_area(
        "In 3–5 sentences, explain one UI/UX principle from Unit 1 that changed how you look at digital products.",
        value=st.session_state.reflection,
        height=150
    )
    if st.button("Save Reflection"):
        st.session_state.reflection = reflection
        st.success("Reflection saved for this session.")

    st.divider()
    st.subheader("📊 Quest Summary")
    st.metric("XP Earned", st.session_state.xp)
    st.metric("Missions Completed", f"{len([x for x in st.session_state.completed if x != 'boss_completed'])}/5")
    st.metric("Boss Battle", "Defeated 🏆" if "boss_completed" in st.session_state.completed else "Not yet")
