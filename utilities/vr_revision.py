import streamlit as st
import random

st.set_page_config(page_title="VR Basics Interactive Guide", layout="wide")
st.title("🎮 Getting Started with Virtual Reality (VR)")

# --- Step 1: Welcome ---
st.header("👋 Welcome to the World of Virtual Reality")
st.video("https://www.youtube.com/watch?v=Jd3-eiid-Uw")
st.write("Virtual Reality (VR) is a simulated experience that immerses users in a digital world. Let's explore how it works!")

# --- Step 2: Match the Terms ---
st.header("🧩 Match the VR Terms")
with st.expander("Click to Match VR Concepts"):
    terms = {
        "Immersion": "A deep mental involvement in the virtual world",
        "Presence": "The sense that you're really 'there' in the VR space",
        "Interaction": "How you engage with virtual objects and people",
        "Feedback": "System response to user actions (vibration, visuals, sound)"
    }
    for term, definition in terms.items():
        st.markdown(f"**{term}** ➡️ {definition}")

# --- Step 3: Explore Hardware ---
st.header("🛠️ Explore VR Hardware")
hardware_data = {
    "VR Headset": "Immerses the user visually in 3D space",
    "Motion Controllers": "Used to pick up and move objects",
    "Eye Tracker": "Follows user gaze for responsive systems",
    "Haptic Gloves": "Let users feel textures and resistance",
    "Body Trackers": "Capture full-body motion for avatars"
}
cols = st.columns(3)
for i, (hardware, desc) in enumerate(hardware_data.items()):
    with cols[i % 3]:
        st.subheader(hardware)
        st.write(desc)

st.video("https://www.youtube.com/watch?v=tEdgPrK5vE4&t=3724s")

# --- Step 4: Concepts Carousel ---
st.header("🔄 VR Concepts in Action")
examples = [
    ("Sense of Agency", "You move a hand in VR, it responds in real-time"),
    ("Body Ownership", "You see a virtual hand and feel it's yours"),
    ("Spatial Illusion", "You feel you're standing on a cliff edge"),
    ("Temporal Sync", "A thrown ball flies instantly in VR")
]
for concept, example in examples:
    st.markdown(f"**{concept}**: {example}")

# --- Step 5: Quiz Zone ---
st.header("🧠 Quick Quiz")
q1 = st.radio("Q1: An avatar moves before you do, but you still feel in control. What illusion is this?",
             ["Presence", "Tracking Delay", "Agency & Ownership", "Visual Lag"])
if q1 == "Agency & Ownership":
    st.success("Correct! This is a cognitive illusion where timing mismatch still gives a sense of control.")
else:
    st.error("Oops! Think again. It's about agency and body ownership.")

q2 = st.radio("Q2: Which hardware gives a sense of touch in VR?",
             ["Eye Tracker", "Haptic Gloves", "VR Headset", "Base Station"])
if q2 == "Haptic Gloves":
    st.success("Exactly! Haptic gloves simulate touch through feedback.")
else:
    st.error("Try again. Think about 'feeling' in VR.")

# --- Step 6: Explore Your Domain ---
st.header("🌐 VR Across Domains")
domain = st.selectbox("Choose a domain to see how VR is applied:",
                      ["Education", "Healthcare", "Industry", "Entertainment", "Social VR"])
if domain == "Education":
    st.write("- VR labs for physics and chemistry\n- Virtual field trips\n- Historical reenactments")
    st.video("https://www.youtube.com/watch?v=GT2kYCX9wNs")
elif domain == "Healthcare":
    st.write("- VR therapy for PTSD\n- Surgical training simulators")
    st.video("https://www.youtube.com/watch?v=uCQU6g1J4HM")
elif domain == "Industry":
    st.write("- Fire safety training\n- Virtual product design")
    st.video("https://www.youtube.com/watch?v=Rnk_akgSjqg")
elif domain == "Entertainment":
    st.write("- Immersive gaming\n- VR concerts and experiences")
elif domain == "Social VR":
    st.write("- Virtual meetups\n- Remote collaboration in VR offices")

# --- Step 7: Project Prompt ---
st.header("💡 Build Your Own VR Idea")
user_input = st.text_area("Describe your VR idea using at least 3 hardware components")
if st.button("Submit Idea"):
    if user_input.strip():
        st.success("Awesome! Your idea has been recorded. Keep innovating!")
    else:
        st.warning("Please enter your idea before submitting.")
