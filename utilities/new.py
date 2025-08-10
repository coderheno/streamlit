import streamlit as st
import base64
from textwrap import dedent

st.set_page_config(page_title="AR & VR Hardware — Interactive Lecture", layout="wide")

# --- SVG diagrams ---
AR_SVG = '''
<svg width="800" height="380" xmlns="http://www.w3.org/2000/svg">
  <style>
    .label { font: 14px sans-serif; fill: #222 }
    .title { font: 18px sans-serif; font-weight: bold; }
    .box { fill: #f4f7fb; stroke: #8aa0d9; stroke-width: 2; rx:10 }
    .arrow { stroke:#555; stroke-width:2; fill:none; marker-end:url(#arrowhead)}
  </style>
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#555" />
    </marker>
  </defs>
  <rect x="10" y="10" width="220" height="80" class="box" />
  <text x="20" y="40" class="title">AR Device (Glass / HMD)</text>
  <text x="20" y="62" class="label">Display (optical/video)</text>

  <rect x="260" y="10" width="220" height="80" class="box" />
  <text x="270" y="40" class="title">Sensors & Cameras</text>
  <text x="270" y="62" class="label">RGB, Depth, IMU, LiDAR</text>

  <rect x="10" y="120" width="220" height="80" class="box" />
  <text x="20" y="150" class="title">Processor</text>
  <text x="20" y="172" class="label">Edge CPU/GPU (XR chip)</text>

  <rect x="260" y="120" width="220" height="80" class="box" />
  <text x="270" y="150" class="title">Connectivity</text>
  <text x="270" y="172" class="label">Wi-Fi / 5G / BLE / Cloud</text>

  <rect x="530" y="40" width="250" height="160" class="box" />
  <text x="545" y="80" class="title">World (Real Environment)</text>
  <text x="545" y="110" class="label">Surfaces, Objects, People</text>

  <path d="M230 50 L260 50" class="arrow" />
  <path d="M230 150 L260 150" class="arrow" />
  <path d="M480 90 L530 90" class="arrow" />
  <path d="M430 90 L480 90" class="arrow" />

  <text x="20" y="230" class="label">Notes:</text>
  <text x="20" y="250" class="label">• Camera feeds + sensors align overlays to world.</text>
  <text x="20" y="270" class="label">• Low-latency pipeline: capture → compute → render → display.</text>
</svg>
'''

VR_SVG = '''
<svg width="800" height="380" xmlns="http://www.w3.org/2000/svg">
  <style>
    .label { font: 14px sans-serif; fill: #222 }
    .title { font: 18px sans-serif; font-weight: bold; }
    .box { fill: #fff7f2; stroke: #e89a7a; stroke-width: 2; rx:10 }
    .arrow { stroke:#555; stroke-width:2; fill:none; marker-end:url(#arrowhead)}
  </style>
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#555" />
    </marker>
  </defs>
  <rect x="10" y="10" width="220" height="80" class="box" />
  <text x="20" y="40" class="title">VR Headset (HMD)</text>
  <text x="20" y="62" class="label">Stereo Screens + Optics</text>

  <rect x="260" y="10" width="220" height="80" class="box" />
  <text x="270" y="40" class="title">Tracking System</text>
  <text x="270" y="62" class="label">Inside-out / Outside-in</text>

  <rect x="10" y="120" width="220" height="80" class="box" />
  <text x="20" y="150" class="title">Input Devices</text>
  <text x="20" y="172" class="label">Controllers, Gloves, Treadmill</text>

  <rect x="260" y="120" width="220" height="80" class="box" />
  <text x="270" y="150" class="title">Audio & Haptics</text>
  <text x="270" y="172" class="label">Spatial audio, haptic feedback</text>

  <rect x="530" y="40" width="250" height="160" class="box" />
  <text x="545" y="80" class="title">Rendering Host</text>
  <text x="545" y="110" class="label">PC / Console / On-board GPU</text>

  <path d="M230 50 L260 50" class="arrow" />
  <path d="M230 150 L260 150" class="arrow" />
  <path d="M480 90 L530 90" class="arrow" />
  <path d="M430 90 L480 90" class="arrow" />

  <text x="20" y="230" class="label">Notes:</text>
  <text x="20" y="250" class="label">• Low motion-to-photon latency is critical (≤20ms target).</text>
  <text x="20" y="270" class="label">• Accurate tracking avoids motion sickness.</text>
</svg>
'''

# --- Sidebar ---
with st.sidebar:
    st.title("AR & VR — Lecture Toolkit")
    st.write("Select sections to explore:")
    show_notes = st.checkbox("Show full lecture notes", value=True)
    show_diagrams = st.checkbox("Show diagrams", value=True)
    show_activities = st.checkbox("Show learner activities", value=True)
    show_examples = st.checkbox("Show extended examples", value=True)
    download_md = st.checkbox("Enable notes download", value=True)

st.title("Understanding AR & VR Hardware — Interactive Lecture")
st.markdown("---")

# --- Lecture notes content ---
lecture_md = dedent('''
# Understanding AR & VR Hardware

## 1. Introduction
AR (Augmented Reality) overlays digital information on the real world; VR (Virtual Reality) fully simulates an environment.

## 2. AR Hardware — Components
- **Display**: Optical see-through (waveguide) or video see-through.
- **Sensors**: RGB camera, depth sensors, IMU (accelerometer, gyroscope), LiDAR.
- **Processor**: Edge XR chips (e.g., Snapdragon XR2), or paired host.
- **Connectivity**: Wi‑Fi, 5G, BLE for cloud/IoT sync.

## 3. AR Devices — Examples
- **Smartphones/Tablets** (ARKit, ARCore)
- **HoloLens 2**: enterprise AR with hand tracking
- **Magic Leap 2**: medical & industrial use
- **Epson Moverio**: drone piloting, guides

## 4. VR Hardware — Components
- **HMD**: dual displays + optics
- **Tracking**: inside-out (cameras on headset) or outside-in (external sensors)
- **Input**: controllers, gloves, treadmills
- **Audio/Haptics**: spatial audio and force feedback
- **Rendering Host**: PC / Console / Onboard GPU

## 5. VR Devices — Examples
- **Meta Quest 3**: standalone VR
- **HTC Vive Pro**: high‑end PC VR
- **PlayStation VR2**: console VR
- **Specialized**: Teslasuit (haptics), Omnidirectional treadmills

## 6. System Pipelines
- AR pipeline: capture → localization & mapping → content placement → rendering → display
- VR pipeline: input → simulation → rendering → display → haptics/audio

## 7. Design Considerations
- Latency (motion-to-photon)
- Field of View (FOV)
- Resolution & pixel density (ppi)
- Ergonomics & weight
- Battery life & heat

## 8. Applications
- AR: maintenance, education (anatomy overlays), retail (virtual try‑on)
- VR: training simulators, therapy, immersive tours

## 9. Learner Activities (brief)
- Device exploration, scenario roleplay, design-a-device, hands-on AR tryout
''')

if show_notes:
    
    st.markdown(lecture_md)

# Diagrams
if show_diagrams:
    st.header("Hardware Setup Diagrams")
    st.write("SVG diagrams below visualise the main components and information flow for AR and VR setups.")
    st.markdown("**AR Hardware Flow**")
    st.components.v1.html(AR_SVG, height=420)
    st.markdown("**VR Hardware Flow**")
    st.components.v1.html(VR_SVG, height=420)

# Extended examples
if show_examples:
    st.header("Extended Examples & Case Studies")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("AR — Remote Assistance (HoloLens 2)")
        st.write("Use case: A field technician gets step-by-step 3D overlays while repairing a machine. HoloLens 2 provides hand tracking and spatial anchors so instructions stay pinned.")
        st.write("Key hardware: depth sensor, world tracking, on‑board processor, see‑through display.")
    with col2:
        st.subheader("VR — Flight Simulator (PC + HMD)")
        st.write("Use case: Pilot training with high-fidelity simulation, motion platform, and haptic feedback in controls.")
        st.write("Key hardware: high refresh-rate HMD, accurate head tracking, dual-stick controllers, rendering PC with GPU.")

# Learner-centered activities
if show_activities:
    st.header("Learner-Centered Activities — Interactive")

    st.subheader("Activity 1 — Device Exploration Challenge")
    st.write("Group activity: Each group selects 2 AR and 2 VR devices and prepares a micro-presentation (3 slides). Use the text areas below to draft your group's notes.")
    col1, col2 = st.columns(2)
    with col1:
        group_name = st.text_input("Group name", value="Group A")
        device1 = st.text_input("AR device 1 (name)")
        device2 = st.text_input("AR device 2 (name)")
    with col2:
        device3 = st.text_input("VR device 1 (name)")
        device4 = st.text_input("VR device 2 (name)")
    if st.button("Save draft for Device Exploration"):
        st.success(f"Draft saved for {group_name}. Devices: {device1}, {device2}, {device3}, {device4}")

    st.markdown("---")
    st.subheader("Activity 2 — Immersive Scenario Roleplay")
    scenario = st.selectbox("Choose a scenario:", ["Firefighter training", "Remote surgery", "Interior design", "Warehouse logistics"]) 
    st.write("Explain why AR or VR suits this scenario and propose 2 key hardware requirements.")
    ans = st.text_area("Your reasoning (2–4 lines)")
    if st.button("Submit scenario reasoning"):
        st.info("Responses collected — discuss in class or export as CSV in a larger version of this app.")

    st.markdown("---")
    st.subheader("Activity 3 — Design Your Dream Device (Sketch & Specs)")
    st.write("Describe your next-gen AR/VR device. Include: target users, 3 key hardware features, and a one-line elevator pitch.")
    target = st.text_input("Target users (e.g., surgeons, architects)")
    features = st.text_area("Three hardware features (comma separated)")
    pitch = st.text_input("Elevator pitch")
    if st.button("Save device idea"):
        st.success("Idea saved to session (demo) — you can later export the class ideas.")

    st.markdown("---")
    st.subheader("Activity 4 — Hands-On AR Tryout (Instructions)")
    st.write("Ask learners to use their smartphones to try:")
    st.write("• Google/Apple AR measurement tool, • IKEA Place, • Snap AR filters, or • a free AR anatomy app.")
    st.write("Share one screenshot and one line about latency and alignment quality.")

# Downloadable notes
if download_md:
    st.header("Download: Lecture Notes & Activity Pack")
    md_bytes = lecture_md.encode('utf-8')
    st.download_button("Download notes (Markdown)", data=md_bytes, file_name="AR_VR_Lecture_Notes.md", mime="text/markdown")

# Quick Quiz (small interactive check)
st.markdown("---")
st.header("Quick 5-minute Quiz — Check & Reflect")
q1 = st.radio("1) Which device typically uses optical see-through displays?", ("VR headset", "AR glasses", "Smart TV"))
q2 = st.radio("2) Motion-to-photon latency ideally should be:", (">100 ms", "~50 ms", "<20 ms"))
q3 = st.radio("3) Which tracking method uses external base stations?", ("Inside-out", "Outside-in", "IMU-only"))
if st.button("Submit Quiz"):
    score = 0
    if q1 == "AR glasses": score += 1
    if q2 == "<20 ms": score += 1
    if q3 == "Outside-in": score += 1
    st.success(f"You scored {score}/3. Discuss any wrong answers with peers.")

# Footer / Next steps
st.markdown("---")
st.write("**Next steps:** Want this app packaged so students can run it locally (requirements.txt) or deployed on share.streamlit.io? I can generate the files.")
