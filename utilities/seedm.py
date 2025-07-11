import streamlit as st

st.set_page_config(page_title="Seed Money Slide Deck", layout="wide")

# Initialize session state
if "slide" not in st.session_state:
    st.session_state.slide = 0

# Slide Titles
slides = [
    "Slide 1: Project Overview",
    "Slide 2: Timeline and Current Phase",
    "Slide 3: Publications & Collaborations",
    "Slide 4: Budget and MoUs",
    "Slide 5: Beneficiaries & Outcomes",
    "Slide 6: Future Plans & Tamil Publication"
]

# Slide Navigation Buttons
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    if st.button("⬅️ Previous", disabled=st.session_state.slide == 0):
        st.session_state.slide -= 1
with col3:
    if st.button("Next ➡️", disabled=st.session_state.slide == len(slides) - 1):
        st.session_state.slide += 1

# Display Current Slide
st.markdown(f"### {slides[st.session_state.slide]}")

# Slide Content
slide = st.session_state.slide

if slide == 0:
    st.header("🎯 Project Overview")
    st.write("""
    **Title:** Enhancing Genomic Analysis and Parental Comparison Through IoT-Enabled DNA Sequencing Sensors

    This feasibility study explores integrating IoT technology into DNA sequencing to support real-time data capture, genetic analysis, and parental comparisons in healthcare and biotechnology.
    """)
    st.markdown("- Duration: 18 months\n- PI: Dr. Vijay Arputharaj J\n- Seed Funding: ₹1,00,000")

elif slide == 1:
    st.header("🗓️ Timeline and Current Phase")
    st.markdown("""
    - ✅ Phase 1: Planning & Proposal
    - ✅ Phase 2: Setup & Data Collection
    - ✅ Phase 3: IoT Integration & Testing
    - ✅ Phase 4: Genomic Interpretation
    
    **Currently working on final interpretation and draft report.**
    """)

elif slide == 2:
    st.header("📚 Publications & Collaborations")
    st.markdown("""
    ### Publications
    - Springer Chapter: *The Rise of Quantum Computing in Industry 6.0*
    - Book: *Internet of Things and Genetic Data*, ISBN 978-81-986413-3-5 (Sole Authored)

    ### Collaborations
    - Dept. of Human Genetics, Bharathiar University
    - Centre for Human Genetics, Bangalore
    """)

elif slide == 3:
    st.header("💸 Budget and MoUs")
    st.markdown("""
    ### Budget Utilization
    - ₹10,000 spent on MoU partnerships
    - ₹50,000 planned for travel, data analysis, and TN subsidy publication

    ### Partners
    - Human Genetics Dept. (BU)
    - Centre for Human Genetics (Bangalore)
    """)

elif slide == 4:
    st.header("👥 Beneficiaries & Outputs")
    st.markdown("""
    ### Stakeholders
    - Researchers, healthcare workers, patients, genomic scientists, biotech firms

    ### Outputs
    - 1 Journal article (Q1–Q4 or Scopus)
    - 1 Reference book
    - Patent in progress
    """)

elif slide == 5:
    st.header("🚀 Future Plans & Tamil Publication")
    st.markdown("""
    - Publishing Tamil-translated version (State Subsidy opportunity)
    - Submission to IEEE/Springer AI conferences
    - Expand to cloud-based DNA research platforms
    """)

# Footer
st.markdown("---")
st.caption("🎓 Seed Money Progress Slides – Dr. Vijay Arputharaj J")
x