# app.py
import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

st.set_page_config(page_title="Education 5.0 – Case Studies", layout="wide")

st.title("Education 5.0 – Case Studies & Interactive Demos")
st.caption("Microlearning for the Masses: Building Personalized Learning Paths in Education 5.0")

st.markdown("""
Use the tabs below to explore two short, visual case studies.
Each section includes **before/after** context and a **tiny interactive demo** you can run live.
""")

tabs = st.tabs([
    "1) No‑Code Tools Empowering Rural Learners",
    "2) From PowerPoints to Interactive Dashboards"
])

# -----------------------------
# TAB 1: Rural Learners Case
# -----------------------------
with tabs[0]:
    st.header("1) No‑Code Tools Empowering Rural Learners")

    st.subheader("Story")
    st.markdown("""
In a small government school in rural Karnataka, students had never built a website before.  
Using **Streamlit** as a low‑code approach (they wrote **very little** Python), they created a **local weather & crop suggestion dashboard**.  

**Before:** project work stayed on chart papers and could not be updated.  
**After:** a mobile‑friendly dashboard that local farmers use to check daily rainfall and **crop suggestions in Tamil**.
""")

    st.markdown("""
- Students presented work as **printed charts** and verbal explanations  
- No way to **update or reuse** work after submission  
- Skills limited to **Word & PowerPoint**
""")
    st.markdown("""
- Live dashboards accessible on **mobile**  
- **Real‑time weather** inputs (or teacher-entered) for local context  
- Students gained **confidence** to share beyond the classroom
""")

    st.markdown("---")
    st.subheader("Tiny Demo: Weather → Crop Suggestion (Teacher‑friendly, no API)")

    lang = st.toggle("Show outputs in Tamil (தமிழ்)?", value=False)
    with st.form("weather_form"):
        colA, colB, colC, colD = st.columns(4)
        with colA:
            season = st.selectbox("Season", ["Kharif", "Rabi", "Summer"], index=0)
        with colB:
            soil = st.selectbox("Soil Type", ["Red", "Black", "Sandy", "Loam"], index=0)
        with colC:
            rainfall = st.slider("Rainfall (mm)", 0, 300, 80, step=10)
        with colD:
            irrigated = st.selectbox("Irrigation", ["Rainfed", "Irrigated"], index=0)

        submitted = st.form_submit_button("Get Suggestion")
    if submitted:
        # Simple, explainable rule-based suggestion (no external calls)
        # You can replace these with your actual local heuristics
        def suggest_crop(season, soil, rainfall, irrigated):
            candidates = []
            if season == "Kharif":
                if rainfall >= 120:
                    candidates.append("Paddy")
                if 60 <= rainfall <= 150:
                    candidates.append("Maize")
                if soil in ["Red", "Sandy"] and rainfall <= 100:
                    candidates.append("Millets")
            if season == "Rabi":
                if 40 <= rainfall <= 120:
                    candidates.append("Wheat")
                if soil in ["Black", "Loam"]:
                    candidates.append("Chickpea")
            if season == "Summer":
                if irrigated == "Irrigated":
                    candidates.append("Vegetables")
                if rainfall < 60 and soil in ["Red", "Sandy"]:
                    candidates.append("Groundnut")

            # Deduplicate while preserving order
            seen = set()
            ordered = [c for c in candidates if not (c in seen or seen.add(c))]
            return ordered or ["Millets"]  # safe default

        crops = suggest_crop(season, soil, rainfall, irrigated)

        if not lang:
            st.success(f"Suggested crops for {season}, {soil} soil, {rainfall} mm, {irrigated}: " + ", ".join(crops))
            st.caption("Note: This is a simple, explainable classroom demo. Replace rules with local agronomy inputs.")
        else:
            # Tamil labels (simple)
            crop_ta = {
                "Paddy": "நெல்",
                "Maize": "சோளம்",
                "Millets": "தானியங்கள்",
                "Wheat": "கோதுமை",
                "Chickpea": "கொண்டைக் கடலை",
                "Vegetables": "காய்கறிகள்",
                "Groundnut": "வேர்க்கடலை"
            }
            crops_ta = [crop_ta.get(c, c) for c in crops]
            st.success(f"பரிந்துரைக்கப்படும் பயிர்கள்: {', '.join(crops_ta)}")
            st.caption("கவனம்: இது வகுப்பறை விளக்கத்துக்கான எளிய மாதிரி. உள்ளூர் விவசாய ஆலோசனைகளால் மாற்றிக் கொள்ளுங்கள்.")

    # A tiny trends chart to show “real-time” feel (random demo data)
    st.markdown("**Sample Rainfall Trend (Demo Data)**")
    demo = pd.DataFrame({
        "Day": pd.date_range(datetime.now().date(), periods=7),
        "Rainfall_mm": np.random.randint(0, 180, size=7)
    })
    st.line_chart(demo.set_index("Day"))

# -----------------------------
# TAB 2: Interactive Dashboards Case
# -----------------------------
with tabs[1]:
    st.header("2) From PowerPoints to Interactive Dashboards in the Classroom")

    st.subheader("Story")
    st.markdown("""
A Computer Science department replaced traditional **PowerPoint** slides with a **Streamlit‑based interactive class portal**.  
Students stopped being passive viewers and started **interacting** with live code outputs, charts, and mini‑activities during lectures.
""")

    st.markdown("""
- **Linear** teaching with fixed slides  
- **Limited** student participation  
- **No hands‑on** coding during class
""")
    st.markdown("""
- **Live** code execution (prebuilt, safe demos)  
- Embedded **videos**, **quizzes**, and **instant polls**  
- Students access the portal **anytime** from home
""")

    st.markdown("---")
    st.subheader("Tiny Demo 1: Interactive Chart Instead of a Static Slide")
    st.write("Move the slider to instantly change the chart—this replaces 4–5 static slides with one interactive visual.")
    n = st.slider("Number of data points", min_value=10, max_value=200, value=50, step=10)
    x = np.linspace(0, 2*np.pi, n)
    y = np.sin(x) + 0.2*np.random.randn(n)
    chart_df = pd.DataFrame({"x": x, "y": y})
    st.line_chart(chart_df.set_index("x"))

    st.markdown("---")
    st.subheader("Tiny Demo 2: One‑Minute Quiz (Microlearning Style)")
    st.write("Answer and see instant feedback—this is a bite‑sized formative check you can sprinkle during lectures.")

    q1 = st.radio("1) Which approach increases classroom interactivity the most?",
                  ["Static PPT", "Live portal with inputs", "Printed notes"], index=1)
    q2 = st.radio("2) Microlearning works best when modules are…",
                  ["60–90 minutes", "15–20 minutes", "2–5 minutes"], index=2)
    if st.button("Check Answers"):
        score = 0
        if q1 == "Live portal with inputs": score += 1
        if q2 == "2–5 minutes": score += 1
        st.success(f"You scored {score}/2")
        if score < 2:
            st.info("Tip: Keep modules short and interactive to maintain attention.")

    st.markdown("---")
    st.subheader("Tiny Demo 3: Mini 'Game' for Engagement")
    st.write("A playful moment can reset attention. Try guessing the secret number (1–9).")
    secret = 7
    guess = st.number_input("Your guess", min_value=1, max_value=9, step=1)
    if st.button("Try"):
        if guess == secret:
            st.success("🎉 Correct! Short, playful wins keep energy high.")
        else:
            st.warning("Not this time—try again! Tiny games = quick cognitive resets.")

    st.markdown("---")
    st.info("These tiny, **interactive** elements turn a lecture into a **learning experience**—perfect for Education 5.0, microlearning, and personalized learning paths.")
    st.markdown("""
**Quick Links:**  
[Session-1](https://13july.streamlit.app) [Session-2](https://13july2.streamlit.app)
""")
