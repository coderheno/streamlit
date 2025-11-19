import streamlit as st

# -----------------------------
# Slide Content Dictionary
# -----------------------------
slides = [
    {
        "title": "Rapid Web Application Development using Streamlit",
        "emoji": "🚀",
        "content": """
### **Capacity-Building Programme for Computer Science Faculty, Christ College, Jagdalpur (Online)**

20th Nov 2025, Thursday, 1.30 to 3.30 PM
 
**Presented by: Dr. Vijay Arputharaj J.**     """    },
    {
        "title": "Session Overview",
        "emoji": "🧭",
        "content": """
- Introduction to Streamlit  
- Fast UI/UX development  
- Gamification features with Python  
- Deploying Streamlit apps on the cloud  
- Best practices for teaching & project-based learning  
- Hands-on demo  
"""
    },
    {
        "title": "Why Streamlit?",
        "emoji": "⚡",
        "content": """
✔ Converts Python scripts directly into web apps  
✔ Zero HTML/CSS/JS required  
✔ Rapid prototyping for teaching & research  
✔ Clean UI components  
✔ Ideal for interactive classroom applications  """},
    {
        "title": "What Makes Streamlit Fast?",
        "emoji": "⏱️",
        "content": """
- Real-time updates  
- One-command deployment  
- Widgets for instant UI  
- Auto reload during development  
- Integrates with Python data libraries  
"""
    },
    {
        "title": "Fast UI/UX Development",
        "emoji": "🎨",
        "content": """
**UI building blocks:**
- `st.button()`, `st.slider()`, `st.selectbox()`
- `st.columns()`, `st.tabs()`
- `st.video(URL)` for embedding YouTube or MP4 videos
- `st.progress()`, `st.metric()`
- File uploader (`st.file_uploader()`)

**Outcome:** Build complete interfaces—including media & forms—within minutes. """
    },
    {
        "title": "Gamification in Apps",
        "emoji": "🎮",
        "content": """
**Add elements like:**  
- Points & scoring  
- Levels & progress bars  
- Timers / countdowns  
- Leaderboards  
- Randomized quiz logic  

**Goal:** Make learning interactive & fun.

**Demo App:** https://interface25.streamlit.app/ """
    },
    {
        "title": "Integrating Python Logic",
        "emoji": "🐍",
        "content": """
**Python powers the logic behind every interaction:**
- Rule enforcement & scoring formulas
- Real-time feedback using conditions
- Student performance tracking with CSV/Sheets
- Random question generation using `random` module
- Generating analytics using `matplotlib` & `pandas`

**Example:**
```python
if answer == correct:
score += 1
st.success("Correct!")
else:
st.error("Try again!")
``` """
    },
    {
        "title": "Classroom Gamified Apps",
        "emoji": "🏫",
        "content": """
**Examples include:**  
- MCQ quiz game  
- Coding challenge scoreboard  
- Memory / tuple‐matching game  
- Flashcards  
- Quick in-class competitions   """
    },
    {
        "title": "Cloud Deployment",
        "emoji": "☁️",
        "content": """
**Deployment options:**
- Streamlit Cloud (fastest, simplest)
- HuggingFace Spaces (GPU-ready)
- Render (flexible hosting)
- AWS / GCP (enterprise level)

### Steps:
1. Push to GitHub  
2. Connect to Streamlit Cloud  
3. Auto deployment 
**Process:** Push to GitHub → Deploy → Auto-reload → Share link. """
    },
    {
        "title": "Hands-On Demo Flow",
        "emoji": "🛠️",
        "content": """
1. Create basic app
2. Add UI widgets
3. Insert gamification logic
4. Run locally
5. Deploy
6. Share live app """
    },
    {
        "title": "Best Practices for Teaching",
        "emoji": "👩‍🏫",
        "content": """
- Start with simple widget examples  
- Weekly mini apps  
- Use Streamlit Cloud for evaluation  
- Encourage creativity  
- Integrate gamification   """
    },
    {
        "title": "Streamlit Projects",
        "emoji": "📚",
        "content": """
**Project Ideas:**
- Streamlit Machine Learning dashboards
- Gamified applications for education
- Attendance & evaluation systems
- Quiz, flashcard, memory-match apps
- Small data analytics portals


**Implementation Strategy:**
- Break into modules
- GitHub for version control
- Weekly demos
- Add scoring to increase engagement """
    },
    {
        "title": "Outcomes",
        "emoji": "🏆",
        "content": """
✔ Build interactive apps  
✔ Use gamification  
✔ Deploy to cloud  
✔ Guide student projects effectively   """
    },
    {
        "title": "Tools Required",
        "emoji": "🧰",
        "content": """
- Python 3.10+  
- Streamlit  
- GitHub  
- VS Code / PyCharm  
- Browser  
"""
    },
    {
        "title": "Thank You!",
        "emoji": "🙏",
        "content": """
### **Questions / Discussion**  
Let’s build interactive learning experiences! """
    }
]

# -----------------------------
# Streamlit Page Settings
# -----------------------------
st.set_page_config(page_title="FDP Presentation", layout="wide")

# Custom CSS for slide style
st.markdown("""
<style>
.slide-box {
    background-color: #ffffff;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.15);
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}

h1, h2, h3 {
    text-align: center;
}

.nav-btn {
    display: flex;
    justify-content: space-between;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Slide Navigation System
# -----------------------------
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅ Previous"):
        if st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1

with col3:
    if st.button("Next ➡"):
        if st.session_state.slide_index < len(slides) - 1:
            st.session_state.slide_index += 1

# Current slide
i = st.session_state.slide_index
slide = slides[i]

# -----------------------------
# Slide Layout  
# -----------------------------
st.markdown(f"""
<div class="slide-box">
    <h1>{slide['emoji']} {slide['title']}</h1>
    <hr style="margin-top: 10px; margin-bottom: 30px;">
    <div style="font-size: 20px; text-align: center;">
        {slide['content']}
    </div>
</div>
""", unsafe_allow_html=True)

