import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Creating a VR Environment", layout="wide")

st.title("🎮 Creating Immersive VR Environments")

st.markdown("""
This app guides you through the essential steps to build a VR environment like the one shown in the [example video](https://www.youtube.com/watch?v=0p8HZVCZSkc).

---

## 📽️ Demo Video
""")

components.iframe("https://www.youtube.com/embed/0p8HZVCZSkc", height=400)

st.markdown("""
---

## 🧰 Step-by-Step Guide

### 1. **Choose Tools & Platforms**
- **Unity** with XR Toolkit
- **Unreal Engine** with Blueprints
- **Web-based VR** with A-Frame (HTML + JavaScript)

### 2. **Plan & Prototype**
- Define purpose: e.g., educational, medical, gaming
- Sketch out the scene, interactions, and user journey

### 3. **Build the Environment**
- Use Blender to model 3D assets
- Import into Unity/Unreal or use ready-made asset packs

### 4. **Lighting & Sound**
- Add ambient lighting and shadows
- Spatial audio for immersive feel

### 5. **Interactivity & Navigation**
- Add teleportation, grab and UI interactions
- Use Unity's XR Interaction Toolkit

### 6. **Optimize for Performance**
- Bake lighting
- Use LODs and texture compression

### 7. **Test & Deploy**
- Test on headset (Meta Quest, HTC Vive, etc.)
- Export and deploy to WebXR or as a desktop/mobile app

---

## 🌐 Domain Examples

### 🧠 Education
- Virtual classrooms
- Biology lab simulations (e.g., DNA visualization)

### 🏥 Healthcare
- Surgery training modules
- PTSD therapy environments

### 🏛️ Cultural Heritage
- VR museums and ancient reconstructions
- Temple/mosque/monument tours

### 🌱 Eco-Education
- Climate change awareness scenes
- Water conservation VR games

### 💼 Corporate Training
- Emergency evacuation drills
- Customer service role-play

---

## 💡 Tools to Explore
| Task | Tool |
|------|------|
| Modeling | Blender, Quixel |
| Game Engines | Unity, Unreal |
| Web VR | A-Frame |
| Sound | Ambisonics, Audacity |
| Interaction | Unity XR Toolkit, Unreal Blueprints |

---

""")
