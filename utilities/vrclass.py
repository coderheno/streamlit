import streamlit as st

st.set_page_config(page_title="VR Environment Setup Guide", layout="wide")

st.title("🎮 VR Environment Setup: Blender & Unity")
st.markdown("An interactive guide covering lighting, shadows, materials, camera, animation, particles and more.")

# Sidebar
st.sidebar.header("Navigation")
unit = st.sidebar.selectbox("Choose Topic", [
    "Overview",
    "Materials & Textures",
    "Lighting & Shadows",
    "Camera Setup",
    "Animation & Timeline",
    "Rigging & Characters",
    "Particles & Dynamics",
    "Exporting to Game Engines"
])

# Content
if unit == "Overview":
    st.header("🧭 Overview of VR Environment Design")
    st.markdown("""
    In both **Blender** and **Unity**, VR environments are crafted through a combination of:

    - **Scene composition**: Geometry, lights, cameras
    - **Lighting and materials**: Realism through shaders
    - **Animation and rigging**: Character motion, cutscenes
    - **Physics & particle systems**: Environmental effects
    - **Export and optimization**: Game engine readiness
    """)

elif unit == "Materials & Textures":
    st.header("🎨 Materials & Textures")
    st.markdown("**In Blender**:")
    st.markdown("""
    - Use Shader Editor to add **Principled BSDF**
    - Combine **diffuse**, **normal**, **roughness**, and **emission maps**
    - Use **UV unwrapping** to map textures accurately
    """)
    st.markdown("**In Unity**:")
    st.markdown("""
    - Use **URP or HDRP** materials
    - Add **Standard Shader** with albedo, metallic, smoothness
    - For VR, optimize using **mobile shaders**
    """)
    st.video("https://www.youtube.com/watch?v=i7gp1TuMIgI") 

elif unit == "Lighting & Shadows":
    st.header("💡 Lighting & Shadows")
    st.markdown("**Types of lights in Blender & Unity:**")
    st.markdown("""
    - **Point Light** (omni-directional)
    - **Spot Light** (cone)
    - **Sun/Directional Light** (global)
    - **Area Light** (soft edges)
    - **Emission Shader / HDRI** for global lighting
    """)
    st.markdown("**Shadows:**")
    st.markdown("""
    - Use **soft shadows** for realism
    - Use **shadow maps** or **ray-traced shadows**
    - Blender: Cycles (accurate), Eevee (real-time)
    - Unity: Baked shadows (static) + Realtime shadows (dynamic)
    """)
    st.video("https://www.youtube.com/watch?v=NOv31HSqs6U") 
elif unit == "Camera Setup":
    st.header("📷 Camera Setup")
    st.markdown("**Blender:**")
    st.markdown("""
    - Add camera (Shift + A > Camera)
    - Set focal length, depth of field in Object Data Properties
    - Use **Track To** constraint for camera targeting
    - For VR: use **Panoramic camera (Equirectangular)** render
    """)
    st.markdown("**Unity:**")
    st.markdown("""
    - MainCamera object = player viewpoint
    - For VR: replace with **XR Rig** (using XR Toolkit or OpenXR)
    - Animate camera using Timeline or Cinemachine
    """)
    st.video("https://www.youtube.com/watch?v=jPU2ri4ZwxM") 
elif unit == "Animation & Timeline":
    st.header("🎞️ Animation & Timeline")
    st.markdown("**Blender Workflow:**")
    st.markdown("""
    - Use **Keyframes** for location, rotation, scale
    - Animate camera and light with **Graph Editor**
    - Use **NLA Editor** to blend animations
    """)
    st.markdown("**3ds Max / Unity:**")
    st.markdown("""
    - Keyframe animation + **AutoKey**
    - Use **Path Constraints** for movement along spline
    - Unity: **Animator Controller + Timeline + State Machine**
    """)
    st.video("https://www.youtube.com/watch?v=DrWOXSlEN94") 
elif unit == "Rigging & Characters":
    st.header("🦴 Rigging & Characters")
    st.markdown("**Blender:**")
    st.markdown("""
    - Use **Armature > Parent with Automatic Weights**
    - IK/FK bones for limbs
    - Use **Rigify Add-on** for auto rigs
    """)
    st.markdown("**3ds Max:**")
    st.markdown("""
    - Use **Biped system** or CAT Toolkit
    - Apply **Skin Modifier**
    - Use **Weight Painting** for bone influence
    """)

elif unit == "Particles & Dynamics":
    st.header("🌬️ Particles & Dynamics")
    st.markdown("**Blender:**")
    st.markdown("""
    - Use **Particle System** for smoke, fire, hair
    - Use **Mantaflow** for fluid/smoke simulations
    """)
    st.markdown("**Unity:**")
    st.markdown("""
    - Use **Particle System** component
    - Add turbulence, wind, noise over time
    - Optimize with **LOD** and performance settings
    """)

elif unit == "Exporting to Game Engines":
    st.header("📦 Exporting to Unity/VR")
    st.markdown("**From Blender to Unity:**")
    st.markdown("""
    - Export as `.FBX` or `.glTF`
    - Apply **Transform > Apply All** before export
    - Bake animations and textures
    - In Unity, drag FBX into Assets and assign materials
    """)
    st.markdown("**VR Integration:**")
    st.markdown("""
    - Use **Unity XR Toolkit**
    - Set up **XR Interaction Manager**, **Locomotion**, and **Teleportation Areas**
    - Connect exported assets as environments
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ using Streamlit")

