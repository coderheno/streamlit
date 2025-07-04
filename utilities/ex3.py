import streamlit as st

st.set_page_config(page_title="Exercise 3: Exploring a 3D VR Scene", layout="wide")

st.title("🎮 Exercise 3: Exploring a 3D VR Scene in Unity")
st.markdown("### Objective")
st.info("Design and explore a basic VR scene in Unity by integrating custom 3D objects, realistic elements, player movement, and domain-specific interactivity.")

st.markdown("### 🛠️ General Instructions (Applicable to All Domains)")

with st.expander("🔧 Step 1: Unity Project Setup"):
    st.markdown("""
    - Open Unity Hub and **create a new 3D project**.
    - Name your project (e.g., `VR_Gaming_Prototype`, `ImmersiveTrainingVR`, `VR_HealthSim`).
    - Install **XR Plugin Management** and enable **OpenXR**.
    - Add **XR Interaction Toolkit** via Package Manager.
    """)

with st.expander("🎮 Step 2: Setup VR Environment"):
    st.markdown("""
    - Add **XR Rig (Action-Based)** to the scene.
    - Align the camera with eye level.
    - Enable **teleportation or joystick movement** for player control.
    """)

with st.expander("🧱 Step 3: Create & Import Custom 3D Objects"):
    st.markdown("""
    - Design or import 3D models using Blender or Unity Asset Store.
    - Include at least **3 custom or modified** 3D objects:
        - 🎮 Gaming: Enemies, weapons, collectibles
        - 🛠️ Training: Tools, machinery, props
        - 🏥 Healthcare: Body parts, therapy devices
    """)

with st.expander("🎨 Step 4: Add Realistic Elements"):
    st.markdown("""
    - **Materials & Textures**: Use PBR textures for realism.
    - **Lighting**: Add directional/spot/point lights.
    - **Shadows**: Enable soft/hard shadows.
    - **Skybox & Reflections**: Set an immersive skybox and reflection probes.
    """)

with st.expander("🎞️ Step 5: Add Basic Animations (Optional)"):
    st.markdown("""
    - Use the **Animator** or **Animation** window.
    - Animate doors, object movements, characters.
    - Trigger via proximity or clicks.
    """)

with st.expander("🕹️ Step 6: Enable Player Interaction"):
    st.markdown("""
    - Add **XR Grab Interactable** components.
    - Enable object pickup, movement, sound feedback.
    """)

st.markdown("### 🧩 Domain-Specific Ideas")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎮 Gaming Innovation")
    st.markdown("""
    - Create a **mini VR gameplay level**.
    - Add enemies, scoring, health bar.
    - Trigger win/lose animations.
    """)

with col2:
    st.subheader("🛠️ Immersive Training")
    st.markdown("""
    - Build a task-based training room.
    - Use VR props like tools or machines.
    - Include feedback for correct/wrong steps.
    """)

with col3:
    st.subheader("🏥 Healthcare & Therapy")
    st.markdown("""
    - Create a healing space or therapy simulation.
    - Add clickable human anatomy or gesture-based exercises.
    - Use sound and animation to guide therapy.
    """)

st.markdown("### 🚀 Step 7: Test & Navigate the Scene")
st.markdown("""
- Press **Play** and navigate using your headset or simulator.
- Interact with objects and test lighting, shadows, animations.
""")

st.markdown("### 📝 Step 8: Submission & Reflection")
st.markdown("""
**Submit the following:**
- ✅ 1-minute walkthrough video of your scene
- ✅ Document (.pdf or .docx):
    - Title & Domain
    - Summary of features used (objects, lighting, animation)
    - Challenges faced
    - Improvements planned
""")

st.markdown("---")
st.success("💡 Tip: Be creative and domain-specific! Think about user experience in a real-world scenario.")
