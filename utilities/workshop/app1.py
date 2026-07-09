import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="AR/VR Research Workshop",
    page_icon="🥽",
    layout="wide"
)

# ---------------------------------------------------
# Simple Styling
# ---------------------------------------------------
st.markdown("""
<style>
.slide{
    background-color:#f8f9fa;
    padding:35px;
    border-radius:15px;
}
h1,h2,h3{
    color:#0b5394;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Slides
# ---------------------------------------------------

slides = [

{
"title":"🚀 From AR/VR to Digital Twins",

"content":"""

## Research Opportunities in

- Augmented Reality (AR)
- Virtual Reality (VR)
- Mixed Reality (MR)
- Digital Twins
- Artificial Intelligence
- Industry 5.0

---

### Interactive Faculty Workshop

**Dr. Vijay Arputharaj J**

Associate Professor

CHRIST (Deemed to be University)

"""
},

{
"title":"🤔 Faculty Poll",

"content":"""

## Tell me about your research

Which domain best represents your current research?

- Architecture
- Computer Science
- Engineering
- Healthcare
- Education
- Smart Cities

"""
},

{
"title":"📈 Evolution of Computing",

"content":"""

```

Reality

↓

Desktop Computing

↓

Internet

↓

Artificial Intelligence

↓

Extended Reality

↓

Digital Twin

↓

Spatial Computing

```

### Discussion

Where do you think the next revolution will happen?

"""
},

{
"title":"🏢 What is a Digital Twin?",

"content":"""

```

Physical Object

↓

IoT Sensors

↓

Cloud

↓

Artificial Intelligence

↓

Digital Twin

↓

Prediction

↓

Decision Support

```

### Definition

A Digital Twin is a dynamic digital representation of a real-world object,
continuously updated using real-time data.

"""
},

{
"title":"🏛 Architecture Research",

"content":"""

### Digital Twins in Architecture

Building

↓

Building Information Modelling (BIM)

↓

IoT Sensors

↓

Digital Twin

↓

Virtual Walkthrough

↓

Predictive Maintenance

---

### Research Questions

• Can Digital Twins reduce energy consumption?

• Can XR improve building maintenance?

• Can AI predict structural failures?

"""
},

{
"title":"🏥 Healthcare Research",

"content":"""

### Human Digital Twin

Patient

↓

Wearable Devices

↓

Medical Records

↓

Artificial Intelligence

↓

Digital Twin

↓

Treatment Prediction

---

Applications

• Surgery Planning

• Rehabilitation

• Remote Healthcare

• Medical Education

"""
},

{
"title":"🏫 Smart Campus",

"content":"""

Imagine creating a Digital Twin of your university.

Data Sources

• Buildings

• Electricity

• Water

• Parking

• Weather

• Student Movement

↓

Digital Twin Dashboard

↓

Smart Decision Making

"""
},

{
"title":"🌍 Research Opportunities",

"content":"""

### XR + Digital Twins can transform

🏙 Smart Cities

🏛 Heritage Conservation

🏭 Manufacturing

🏥 Healthcare

🚗 Transportation

🌱 Sustainability

🎓 Education

---

### Think

How can these technologies support YOUR research?

"""
},

{
"title":"🛠 Research Platforms",

"content":"""

## Platforms Used in XR & Digital Twin Research

### NVIDIA Omniverse
AI + Robotics + Digital Twins

### Bentley iTwin
Infrastructure & Smart Buildings

### Autodesk Tandem
Facility Management

### Matterport
3D Indoor Scanning

### Cesium
3D GIS & Smart Cities

### Twinmotion
Architectural Visualization

---

These platforms are widely used in academia and industry.

"""
},

{
"title":"📚 AI Tools for Research",

"content":"""

## Accelerating Research with AI

🔹 ResearchRabbit
Literature Mapping

🔹 SciSpace
Understand Research Papers

🔹 Consensus
Evidence-based Search

🔹 Elicit
Literature Review

🔹 NotebookLM
Research Assistant

---

Question

Which AI tool would you like to explore?

"""
},

{
"title":"📈 Emerging Research Trends",

"content":"""

## Hot Research Topics

✔ AI + XR

✔ Human Digital Twins

✔ Smart Cities

✔ Spatial Computing

✔ Digital Heritage

✔ Industry 5.0

✔ Digital Healthcare

✔ Immersive Learning

---

Many of these areas have excellent publication and funding opportunities.

"""
},

{
"title":"💰 Research Funding Opportunities",

"content":"""

## Possible Funding Sources

• ANRF

• Horizon Europe

• Industry Collaboration

• Smart City Projects

• Healthcare Innovation

• Digital Heritage

---

Think interdisciplinary.

The best projects combine

XR + AI + IoT + Data Analytics

"""
},

{
"title":"💡 Group Discussion",

"content":"""

## Activity

Form small groups.

Discuss

1. What is one research problem in your domain?

2. Can AR, VR or Digital Twins solve it?

3. What technologies would you need?

---

Time

10 Minutes

"""
},

{
"title":"🚀 Future Research Vision",

"content":"""

Imagine the future.

Every Building

↓

Digital Twin

Every Hospital

↓

Digital Twin

Every University

↓

Digital Twin

Every City

↓

Digital Twin

---

Question

What would you build?

"""
},

{
"title":"🙏 Thank You",

"content":"""

# Thank You

### Questions?

---

Think Beyond Visualization

Think Simulation

Think Prediction

Think Intelligent Decision Support

---

Dr. Vijay Arputharaj J

CHRIST (Deemed to be University)

"""
}

]

# ---------------------------------------------------
# Navigation
# ---------------------------------------------------

if "slide" not in st.session_state:
    st.session_state.slide = 0

col1,col2,col3 = st.columns([1,6,1])

with col1:
    if st.button("⬅ Previous"):
        if st.session_state.slide>0:
            st.session_state.slide-=1

with col3:
    if st.button("Next ➡"):
        if st.session_state.slide < len(slides)-1:
            st.session_state.slide+=1

progress=(st.session_state.slide+1)/len(slides)
st.progress(progress)

slide=slides[st.session_state.slide]

st.markdown(f"""
<div class="slide">
<h1>{slide['title']}</h1>
<hr>
{slide['content']}
</div>
""", unsafe_allow_html=True)

st.caption(f"Slide {st.session_state.slide+1} of {len(slides)}")

# ---------------------------------------------------
# Interactive Components
# ---------------------------------------------------

# Slide 2
if st.session_state.slide==1:

    domain=st.selectbox(

        "Select your research area",

        [

            "Architecture",

            "Computer Science",

            "Engineering",

            "Healthcare",

            "Education",

            "Smart Cities"

        ]

    )

    st.success(f"Excellent! Today's discussion will relate XR to {domain}.")

# Slide 4
if st.session_state.slide==3:

    st.info("💡 A Digital Twin is much more than a 3D model. It continuously receives real-time data from the physical world.")

# Slide 5
if st.session_state.slide==4:

    st.text_area(

        "Can you identify one architecture research problem that could benefit from a Digital Twin?"

    )

# Slide 6
if st.session_state.slide==5:

    st.write("### Discussion")

    option=st.radio(

        "Which healthcare application interests you most?",

        [

            "Virtual Surgery",

            "Rehabilitation",

            "Medical Education",

            "Remote Healthcare"

        ]

    )

    st.success(f"You selected: {option}")

# Slide 7
if st.session_state.slide==6:

    st.write("### Smart Campus Brainstorm")

    st.text_input("Suggest one sensor that should be installed on campus.")

# Slide 8
if st.session_state.slide==7:

    st.write("### Reflection")

    st.text_area("How can XR contribute to your current research?")


# ======================================================
# ADD THESE INTERACTIONS BELOW YOUR EXISTING ONES
# ======================================================

# Research Platforms
if st.session_state.slide == 8:

    st.subheader("Explore Research Platforms")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "NVIDIA Omniverse",
            "https://www.nvidia.com/en-us/omniverse/"
        )

        st.link_button(
            "Bentley iTwin",
            "https://www.bentley.com/software/itwin/"
        )

        st.link_button(
            "Matterport",
            "https://matterport.com"
        )

    with col2:

        st.link_button(
            "Cesium",
            "https://cesium.com"
        )

        st.link_button(
            "Twinmotion",
            "https://www.twinmotion.com"
        )

        st.link_button(
            "Autodesk Tandem",
            "https://intandem.autodesk.com/"
        )


# AI Research Tools
if st.session_state.slide == 9:

    tool = st.selectbox(

        "Which AI research tool would you like to explore?",

        [

            "ResearchRabbit",

            "SciSpace",

            "Consensus",

            "Elicit",

            "NotebookLM"

        ]

    )

    st.success(f"{tool} is an excellent tool for researchers.")


# Research Trends
if st.session_state.slide == 10:

    trend = st.multiselect(

        "Which trends interest you?",

        [

            "Digital Twin",

            "Spatial Computing",

            "Human Digital Twin",

            "Smart Cities",

            "AI + XR",

            "Industry 5.0"

        ]

    )

    if trend:

        st.info(f"You selected {len(trend)} emerging research area(s).")


# Funding
if st.session_state.slide == 11:

    st.text_area(

        "If funding was available, what project would you propose?"

    )


# Group Discussion
if st.session_state.slide == 12:

    st.warning("⏱ Activity Time: 10 Minutes")

    st.text_area(

        "Write one interdisciplinary research idea."

    )


# Future Vision
if st.session_state.slide == 13:

    vision = st.text_input(

        "Complete this sentence: 'In the next 10 years, I believe Digital Twins will...'"

    )

    if vision:

        st.success("Excellent vision! This could become a future research proposal.")


# Final Slide
if st.session_state.slide == 14:

    rating = st.slider(

        "How useful was today's workshop?",

        1,

        5,

        5

    )

    if st.button("Submit Feedback"):

        st.balloons()

        st.success("Thank you for your valuable feedback!")