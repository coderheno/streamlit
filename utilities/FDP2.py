import streamlit as st
st.set_page_config(page_title="Mini Game", layout="centered")
st.title("🎮 Simple Gamified App")
# Score system
if "score" not in st.session_state:
    st.session_state.score = 0
st.write("### 📝 Question:")
st.write("Streamlit apps are built using which language?")
if st.button("Python 🐍"):
    st.success("Correct! +1 point")
    st.session_state.score += 1
if st.button("JavaScript"):
    st.error("Wrong answer ❌")
st.write("---")
# Show Score
st.write("### ⭐ Your Score:", st.session_state.score)
# Video
st.write("### 🎥 Quick Intro to Streamlit")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
# External Link
st.write("### 🔗 Useful Link")
st.markdown("[Visit Streamlit Website](https://streamlit.io)")
st.write("---")
# Completion message
if st.session_state.score >= 1:
    st.balloons()
    st.success("You completed the simple FDP task! 🎉")
