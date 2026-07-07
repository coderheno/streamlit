import streamlit as st

# ============================================================
# Page Configuration
# ============================================================
st.set_page_config(
    page_title="Exploring AR • VR • MR",
    page_icon="🥽",
    layout="wide"
)

# ============================================================
# Custom CSS
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"]{
    background:#0b1120;
    color:white;
    font-family:Arial;
}

.block-container{
    padding-top:2rem;
}

.slide-box{

    background:linear-gradient(145deg,#101826,#17233d);

    border-radius:25px;

    padding:45px;

    box-shadow:0px 8px 30px rgba(0,0,0,.45);

    min-height:620px;
}

.slide-title{

    text-align:center;

    font-size:42px;

    font-weight:700;

    color:#4FC3F7;

    margin-bottom:20px;
}

.slide-content{

    font-size:23px;

    line-height:1.8;

    color:white;

}

.big-center{

    text-align:center;

    font-size:34px;

    font-weight:bold;

    margin-top:35px;

    margin-bottom:35px;
}

.highlight{

    color:#00E5FF;

    font-weight:bold;

}

.footer{

    text-align:center;

    color:gray;

    font-size:16px;

}

table{
font-size:22px;
}

</style>

""",unsafe_allow_html=True)

# ============================================================
# Slides
# ============================================================

slides=[

{
"title":"🚀 Exploring Augmented Reality, Virtual Reality & Mixed Reality",

"content":"""

<div class='big-center'>

University of Buraimi, Oman

</div>

### **2-Hour Interactive Workshop**

### Presented by

## **Dr. Vijay Arputharaj J**

Associate Professor

Department of Computer Science

CHRIST (Deemed to be University)

Bengaluru, India

---

### Session Goal

Understand the exciting world of

**Augmented Reality**

**Virtual Reality**

**Mixed Reality**

through demonstrations, online exploration and discussion.

"""
},

{
"title":"🧭 Session Roadmap",

"content":"""

### Today's Journey

✅ Ice Breaker

✅ Understanding Reality

✅ What is XR?

✅ Augmented Reality

✅ Virtual Reality

✅ Mixed Reality

✅ Real-world Applications

✅ XR Playground

✅ Online Exploration

✅ Group Activity

✅ Career Opportunities

✅ Questions

"""
},

{
"title":"🤔 Ice Breaker",

"content":"""

# Have You Already Used AR?

Think about the following applications.

- Pokémon GO

- Snapchat Filters

- Instagram Filters

- Google Maps Live View

- IKEA Place

---

### Question

**How many of you have used at least one of these?**

"""
},

{
"title":"🌍 From Reality to Extended Reality",

"content":"""

# Our Digital Journey


Reality

↓

Desktop Computing

↓

Mobile Computing

↓

Internet

↓

Artificial Intelligence

↓

Extended Reality (XR)


---

Technology is no longer limited to screens.

It is becoming part of **our physical world.**

"""
},

{
"title":"🌐 What is XR?",

"content":"""

# XR = Extended Reality

XR is an umbrella term that includes

## 📱 AR

## 🥽 VR

## 🪄 MR

---

Each technology provides a different level of immersion.

"""
},

{
"title":"📱 Understanding Augmented Reality",

"content":"""

### Definition

Augmented Reality overlays digital information onto the real world.

---

### Characteristics

✔ Real world remains visible

✔ Digital objects appear on top

✔ Uses mobile phones or tablets

✔ Interactive

---

### Examples

• Pokémon GO

• Google Lens

• Snapchat

• IKEA Place

"""
},

{
"title":"🥽 Understanding Virtual Reality",

"content":"""

### Definition

Virtual Reality completely replaces the real environment with a virtual one.

---

### Characteristics

✔ Full immersion

✔ Head Mounted Display

✔ Controllers

✔ Interactive environments

---

### Examples

• Beat Saber

• VR Classrooms

• Flight Simulators

• Medical Simulation

"""
},

{
"title":"🪄 Understanding Mixed Reality",

"content":"""

### Definition

Mixed Reality merges the real and virtual worlds where both interact together.

---

### Characteristics

✔ Real + Virtual

✔ Spatial Mapping

✔ Object Interaction

✔ Intelligent Environment

---

### Examples

• Microsoft HoloLens

• Industrial Maintenance

• Remote Collaboration

• Surgical Assistance

"""
},

{
"title":"⚖️ AR vs VR vs MR",

"content":"""

| Feature | AR | VR | MR |
|:---|:---:|:---:|:---:|
| Real World Visible | ✅ | ❌ | ✅ |
| Digital Objects | Overlay | Complete World | Interactive |
| Immersion | Medium | Very High | High |
| Device | Phone | Headset | Smart Glasses |
| Cost | Low | Medium | High |

---

### Which one do you think will dominate the future?

"""
},

{
"title":"🎥 Evolution of Immersive Technology",

"content":"""


Reality

↓

Desktop Computing

↓

Mobile Computing

↓

Augmented Reality

↓

Virtual Reality

↓

Mixed Reality

↓

Spatial Computing

↓

Metaverse


---

The future is **immersive computing.**

"""
},

# Slides 17 - 24
# ============================================================

{
"title":"⭐ Tool 1 - Spline",

"content":"""

# Interactive 3D Design in Your Browser

🌐 https://spline.design

---

### What is Spline?

A browser-based 3D design platform for creating

✔ Interactive 3D Scenes

✔ Website Animations

✔ Product Visualizations

✔ UI Prototypes

---

### Explore

🎲 Rotate Objects

💡 Change Lighting

🎨 Apply Materials

🎥 Move the Camera

---

### Challenge

Create a simple 3D scene using the available templates.

"""
},

{
"title":"⭐ Tool 2 - Sketchfab",

"content":"""

# Explore Thousands of 3D Models

🌐 https://sketchfab.com

---

### Search for

🦖 Dinosaur

❤️ Human Heart

🚗 Sports Car

🤖 Robot

🏛 Museum Artefacts

🌍 Earth

---

### Observe

✔ Lighting

✔ Animation

✔ Materials

✔ Textures

✔ Polygon Count

"""
},

{
"title":"⭐ Tool 3 - Ready Player Me",

"content":"""

# Create Your Own Avatar

🌐 https://readyplayer.me

---

### Features

😀 Face Customization

👕 Clothing

👓 Accessories

🎨 Hairstyles

🌎 Export for VR

---

### Activity

Create your own avatar

and imagine using it

inside a virtual classroom.

"""
},

{
"title":"⭐ Tool 4 - Google Model Viewer",

"content":"""

# View 3D Models in the Browser

🌐 https://modelviewer.dev

---

### Supports

✔ glTF

✔ GLB

---

### Features

🔄 Rotate

🔍 Zoom

📱 View in AR

💡 Lighting

---

Perfect for previewing Blender models.

"""
},

{
"title":"⭐ Tool 5 - PlayCanvas",

"content":"""

# Browser-Based Game Engine

🌐 https://playcanvas.com

---

### Create

🎮 Games

🌍 Virtual Worlds

🏢 Architecture Walkthroughs

🚗 Simulations

---

### Advantages

✔ No Installation

✔ Cloud Based

✔ Collaborative

✔ Easy Publishing

"""
},

{
"title":"⭐ Tool 6 - Moon Rider",

"content":"""

# Browser-Based VR Game

🌐 https://moonrider.xyz

---

### Experience

🎵 Rhythm Game

🕹 VR Interaction

🥽 Browser VR

🎯 Hand Tracking

---

Works with

✔ Phone

✔ VR Headset

✔ Desktop Browser

"""
},

{
"title":"⭐ Tool 7 - A-Frame",

"content":"""

# Build VR Using HTML

🌐 https://aframe.io

---

Example

```html
<a-scene>

<a-box color="red"></a-box>

</a-scene>

HTML becomes a 3D world.

Perfect for beginners.

"""
},

{
"title":"🌐 XR Exploration Challenge",

"content":"""

Group Activity

Each group selects ONE tool.

Discuss

✔ What is the purpose?

✔ What impressed you?

✔ Which industry can use it?

✔ What are its limitations?

Present your findings

⏱ One Minute

per group.

"""
},
# ============================================================
# Slides 25 - 32
# ============================================================

{
"title":"💡 Design Thinking Challenge",

"content":"""

# Imagine You Are an XR Innovator

Your university wants an XR solution.

Design ONE idea.

---

### Possible Ideas

🧭 Smart Campus Navigation

📚 AR Library Assistant

🏛 Virtual Museum

🧪 Virtual Science Laboratory

🏥 Medical Training

🌍 Tourism Guide

🏃 Sports Training

♿ Accessibility Assistant

---

Think beyond today's technology.

Think about tomorrow.

"""
},

{
"title":"👥 Team Activity",

"content":"""

# XR Innovation Canvas

Work in groups of 4–5 students.

---

### Discuss

✔ Problem

✔ Target Users

✔ XR Technology

✔ Required Devices

✔ Expected Benefits

---

### Time

⏰ 10 Minutes

Prepare a 1-minute presentation.

"""
},

{
"title":"🚀 Career Opportunities",

"content":"""

# Careers in Extended Reality

💻 XR Developer

🎮 Unity Developer

🌐 WebXR Engineer

🎨 3D Artist

🏗 Digital Twin Engineer

🤖 Simulation Engineer

🩺 Medical XR Specialist

🎓 Educational Technologist

🏭 Industry 5.0 Engineer

🚀 Spatial Computing Developer

---

XR is one of the fastest-growing technology domains.

"""
},

{
"title":"🌍 Future of XR",

"content":"""

# The Next Computing Revolution

Today's Trends

🤖 AI + XR

🥽 Spatial Computing

🏙 Smart Cities

🏭 Industry 5.0

🚗 Autonomous Vehicles

🏥 Digital Healthcare

🌎 Metaverse

🛰 Digital Twin

---

The future is immersive, intelligent, and interactive.

"""
},

{
"title":"🛠 Learning Roadmap",

"content":"""

# How to Become an XR Developer

Step 1

✔ Learn Blender

↓

Step 2

✔ Learn Unity

↓

Step 3

✔ Learn C#

↓

Step 4

✔ Learn AR Foundation

↓

Step 5

✔ Publish Mobile Apps

↓

Step 6

✔ Build Your Portfolio

"""
},

{
"title":"📚 Useful Resources",

"content":"""

## Learn More

🌐 https://unity.com

🌐 https://learn.unity.com

🌐 https://developer.apple.com/augmented-reality/

🌐 https://developers.google.com/ar

🌐 https://aframe.io

🌐 https://playcanvas.com

🌐 https://spline.design

🌐 https://sketchfab.com

---

Keep exploring.

Never stop learning.

"""
},

{
"title":"🎯 Session Recap",

"content":"""

Today We Learned

✅ AR

✅ VR

✅ MR

✅ XR Applications

✅ Healthcare

✅ Education

✅ Manufacturing

✅ Gaming

✅ Online XR Tools

✅ Future Careers

---

You have taken your first step into the world of XR.

"""
},

{
"title":"🙏 Thank You",

"content":"""

# Questions?

Thank You

---

Dr. Vijay Arputharaj J

Associate Professor

Department of Computer Science

CHRIST (Deemed to be University)

Bengaluru

---

Keep Exploring

Keep Innovating

Keep Creating

🚀

"""
},
]

if "slide" not in st.session_state:
    st.session_state.slide = 0


# ============================================================
# Slide 18
# ============================================================

if st.session_state.slide == 17:

    st.subheader("Open Sketchfab")

    st.link_button(
        "Explore Sketchfab",
        "https://sketchfab.com"
    )

# ============================================================
# Slide 19
# ============================================================

if st.session_state.slide == 18:

    st.subheader("Create Avatar")

    st.link_button(
        "Ready Player Me",
        "https://readyplayer.me"
    )

# ============================================================
# Slide 20
# ============================================================

if st.session_state.slide == 19:

    st.subheader("Model Viewer")

    st.link_button(
        "Google Model Viewer",
        "https://modelviewer.dev"
    )

# ============================================================
# Slide 21
# ============================================================

if st.session_state.slide == 20:

    st.subheader("PlayCanvas")

    st.link_button(
        "Launch PlayCanvas",
        "https://playcanvas.com"
    )

# ============================================================
# Slide 22
# ============================================================

if st.session_state.slide == 21:

    st.subheader("Moon Rider")

    st.link_button(
        "Play Moon Rider",
        "https://moonrider.xyz"
    )

# ============================================================
# Slide 23
# ============================================================

if st.session_state.slide == 22:

    st.subheader("A-Frame")

    st.link_button(
        "Visit A-Frame",
        "https://aframe.io"
    )

# ============================================================
# Slide 24
# ============================================================

if st.session_state.slide == 23:

    tool = st.selectbox(

        "Which tool impressed you the most?",

        [

            "Spline",

            "Sketchfab",

            "Ready Player Me",

            "PlayCanvas",

            "Moon Rider",

            "A-Frame",

            "Google Model Viewer"

        ]

    )

    st.success(f"Excellent choice! {tool} is widely used in the XR ecosystem.")

    if st.button("Celebrate Learning 🎉"):

        st.balloons()

# ============================================================

col1,col2,col3=st.columns([1,6,1])

with col1:

    if st.button("⬅ Previous"):

        if st.session_state.slide>0:

            st.session_state.slide-=1

with col3:

    if st.button("Next ➡"):

        if st.session_state.slide<len(slides)-1:

            st.session_state.slide+=1

slide=slides[st.session_state.slide]

st.markdown(f"""

<div class='slide-box'>

<div class='slide-title'>

{slide["title"]}

</div>

<hr>

<div class='slide-content'>

{slide["content"]}

</div>

</div>

""",unsafe_allow_html=True)

st.markdown(
f"<div class='footer'>Slide {st.session_state.slide+1} of {len(slides)}</div>",
unsafe_allow_html=True
)

# ============================================================
# Interactive Elements
# ============================================================

if st.session_state.slide==2:

    st.divider()

    st.subheader("Live Poll")

    choice=st.radio(

        "Have you used any AR application before?",

        [

            "Yes",

            "No",

            "Not Sure"

        ]

    )

    if choice=="Yes":

        st.success("Excellent! You have already experienced Augmented Reality.")

    elif choice=="No":

        st.info("Great! Today will be your first step into the XR world.")

    else:

        st.warning("By the end of this session you'll definitely know!")

if st.session_state.slide==8:

    st.divider()

    st.subheader("Quick Quiz")

    ans=st.radio(

        "Which technology completely replaces the real world?",

        [

            "AR",

            "VR",

            "MR"

        ]

    )

    if ans=="VR":

        st.success("Correct!")

    elif ans:

        st.error("Not quite. VR provides complete immersion.")
# ============================================================
# Slides 11 - 16
# ============================================================

{
"title":"🌎 Where is XR Used?",

"content":"""

# XR is Transforming Every Industry

XR is no longer limited to gaming.

It is becoming an essential technology across multiple sectors.

---

### Major Application Areas

🏥 Healthcare

🎓 Education

🏭 Manufacturing

🎮 Gaming

🛍 Retail

✈ Tourism

🏗 Architecture

🚗 Automotive

🪖 Defence & Military

🚀 Space Exploration

---

### Discussion

**Which industry do you think benefits the most from XR?**

"""
},

{
"title":"🏥 XR in Healthcare",

"content":"""

# Improving Healthcare with XR

### Applications

🩺 Virtual Surgery Training

🫀 3D Human Anatomy

💊 Patient Rehabilitation

🧠 Mental Health Therapy

🚑 Emergency Response Training

👨‍⚕ Medical Education

---

### Example

Medical students can practice surgeries
without any risk to real patients.

---

### Benefits

✔ Safe

✔ Repeatable

✔ Cost Effective

✔ Interactive

"""
},

{
"title":"🎓 XR in Education",

"content":"""

# Making Learning Immersive

Traditional Learning

📚 Books

📽 PowerPoint

📝 Notes

↓

Immersive Learning

🥽 Virtual Laboratories

🧬 3D Biology Models

🏛 Historical Tours

🌍 Virtual Field Trips

🛰 Space Exploration

---

### Imagine

Learning the Solar System

while standing **inside** it.

"""
},

{
"title":"🏭 XR in Industry & Manufacturing",

"content":"""

# Industry 4.0 Meets Extended Reality

### Applications

⚙ Machine Maintenance

👨‍🏭 Worker Training

🏭 Digital Twin

📦 Warehouse Planning

🤝 Remote Assistance

🦾 Smart Manufacturing

---

### Example

A technician wearing smart glasses
receives live repair instructions
while working on a machine.

---

### Benefits

✔ Faster Training

✔ Fewer Errors

✔ Improved Safety

"""
},

{
"title":"🎮 XR in Entertainment & Gaming",

"content":"""

# Gaming Beyond the Screen

### Popular Examples

🎮 Beat Saber

🚗 VR Racing

🧟 Zombie Survival

🏹 VR Archery

⚽ Sports Simulation

🎭 Interactive Storytelling

---

### Why Gamers Love VR

✔ Immersion

✔ Physical Interaction

✔ Realistic Experience

✔ Social Multiplayer

---

Gaming has been one of the biggest drivers
behind modern VR technology.

"""
},

{
"title":"🌐 XR Playground - Today's Online Exploration",

"content":"""

# Time to Explore!

Today we will experience XR using
browser-based tools.

No installation required.

---

### Today's Tools

⭐ Spline

⭐ Sketchfab

⭐ Google Model Viewer

⭐ Ready Player Me

⭐ PlayCanvas

⭐ Moon Rider

⭐ A-Frame

---

### Activity

Each group will explore one tool
and share their observations.

"""
},
# ============================================================
# Slide 11 Interaction
# ============================================================

if st.session_state.slide == 10:

    st.divider()

    st.subheader("Quick Discussion")

    option = st.selectbox(

        "Which industry do you think XR will impact the most?",

        [

            "Healthcare",

            "Education",

            "Gaming",

            "Manufacturing",

            "Tourism",

            "Architecture"

        ]

    )

    st.success(f"Excellent choice! {option} is already adopting XR rapidly.")

# ============================================================
# Slide 12
# ============================================================

if st.session_state.slide == 11:

    st.info("💡 Imagine practicing a heart surgery 100 times before entering an operating theatre.")

# ============================================================
# Slide 13
# ============================================================

if st.session_state.slide == 12:

    st.success("🌍 Virtual field trips allow students to visit museums, volcanoes, or even Mars without leaving the classroom.")

# ============================================================
# Slide 14
# ============================================================

if st.session_state.slide == 13:

    st.warning("Industry 5.0 combines AI, Robotics, IoT and XR to create smarter workplaces.")

# ============================================================
# Slide 15
# ============================================================

if st.session_state.slide == 14:

    st.video("https://www.youtube.com/watch?v=SMbV3sB7JgM")

# ============================================================
# Slide 16
# ============================================================

if st.session_state.slide == 15:

    st.markdown("## 🚀 Ready for Hands-on Exploration?")

    if st.button("Let's Start Exploring!"):

        st.balloons()

        st.success("Awesome! Let's discover the world of XR tools.")
# ============================================================
# ============================================================
# Slide 25
# ============================================================

if st.session_state.slide == 24:

    st.subheader("Innovation Challenge")

    idea = st.text_area(
        "Describe one XR application you would like to build."
    )

    if st.button("Submit Idea"):

        st.success("Excellent! Every innovation begins with an idea.")

# ============================================================
# Slide 26
# ============================================================

if st.session_state.slide == 25:

    st.info("💡 Discuss your idea with your teammates and prepare a one-minute pitch.")

# ============================================================
# Slide 27
# ============================================================

if st.session_state.slide == 26:

    career = st.selectbox(

        "Which XR career interests you the most?",

        [

            "XR Developer",

            "Unity Developer",

            "3D Artist",

            "Medical XR",

            "WebXR Engineer",

            "Game Developer"

        ]

    )

    st.success(f"Great choice! {career} is an exciting career path.")

# ============================================================
# Slide 28
# ============================================================

if st.session_state.slide == 27:

    st.video("https://www.youtube.com/watch?v=UvkgmyfMPks")

# ============================================================
# Slide 29
# ============================================================

if st.session_state.slide == 28:

    progress = st.slider(

        "How ready are you to begin learning XR?",

        0,

        100,

        75

    )

    st.progress(progress / 100)

# ============================================================
# Slide 30
# ============================================================

if st.session_state.slide == 29:

    st.subheader("Useful Links")

    col1, col2 = st.columns(2)

    with col1:
        st.link_button("Unity Learn", "https://learn.unity.com")
        st.link_button("A-Frame", "https://aframe.io")
        st.link_button("Spline", "https://spline.design")

    with col2:
        st.link_button("Sketchfab", "https://sketchfab.com")
        st.link_button("PlayCanvas", "https://playcanvas.com")
        st.link_button("Google AR", "https://developers.google.com/ar")

# ============================================================
# Slide 31
# ============================================================

if st.session_state.slide == 30:

    st.success("🎉 Congratulations! You have completed today's XR exploration workshop.")

    if st.button("Celebrate 🎊"):

        st.balloons()

# ============================================================
# Slide 32
# ============================================================

if st.session_state.slide == 31:

    rating = st.slider(
        "Rate today's session",
        1,
        5,
        5
    )

    if st.button("Submit Feedback"):

        st.success("Thank you for your valuable feedback!")
