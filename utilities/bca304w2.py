# VR Educational Tool Streamlit App

import streamlit as st


st.set_page_config(page_title="VR Educational Tool", layout="wide")
st.title("\U0001F393 Virtual Reality (VR) Educational Tool")

# Navigation
pages = [
    "Lecture Notes",
    "Activities",
    "3D Tools & Examples"
]
selection = st.sidebar.radio("Navigate", pages)

# Lecture Notes Section
if selection == "Lecture Notes":
    st.header("\U0001F4D3 Lecture Notes: Virtual Reality (VR)")

    st.subheader("1. What is VR?")
    st.markdown("""
**Virtual Reality (VR)** is an immersive digital environment created with 3D modeling and game engines. Users wear VR headsets for a first-person experience.

**Example:** Using Blender to model a virtual room, exporting it to Unity, and exploring it with an Oculus headset.
    """)
    st.video("https://www.youtube.com/watch?v=Z_0iFPRYAbI")

    st.subheader("2. VR vs AR")
    st.markdown("""
**VR** replaces the physical world. **AR** adds to it.

| Feature | VR | AR |
|--------|----|----|
| Immersion | Full | Partial |
| Devices | Headsets | Phones, Glasses |
| Toolchains | Unity + XR Toolkit | ARKit, ARCore + Unity |

**Example:** Blender + Unity for VR museum tour; AR for mobile instructions overlay.
    """)
    st.video("https://www.youtube.com/watch?v=wyOqOjSwdVs")




    st.title("🔧 AR/VR Hardware & Software Essentials")

    st.header("🎧 1. Hardware Components in VR/AR Systems")

    with st.expander("a. Headsets"):
        st.markdown("""
        | Headset | Features | Use Case |
        |---------|----------|----------|
        | **Meta Quest (2, 3, Pro)** | Standalone & PC VR, inside-out tracking, hand tracking | Education, Indie devs |
        | **HTC Vive / Vive Pro** | Tethered VR, room-scale tracking | Enterprise training |
        | **Pico / Pimax / Index** | High-end features, ultra FOV | Labs, niche apps |
        | **HoloLens / Magic Leap** | Mixed Reality (AR + VR) | Industrial use |
        """)

    with st.expander("b. Controllers"):
        st.markdown("""
        - Tracked controllers (e.g., Meta Touch, Vive Wands)
            - Positional tracking
            - Grabbing, pointing, teleporting
        - Hand tracking available on Meta Quest
        """)

    with st.expander("c. Haptic Devices"):
        st.markdown("""
        - **Haptic Gloves** (HaptX, SenseGlove): Finger-level touch
        - **Vests** (bHaptics, Teslasuit): Body feedback
        - **Controller vibration**: Simple built-in feedback
        """)

    st.header("💻 2. Software Stack for VR/AR Development")

    with st.expander("a. Game Engines"):
        st.markdown("""
        | Engine | Best For | Strengths |
        |--------|----------|-----------|
        | **Unity** | VR/AR apps, simulations | Fast, AR Foundation, XR Toolkit |
        | **Unreal Engine** | High-fidelity VR | Visual scripting, archviz |
        """)

    with st.expander("b. SDKs and Toolkits"):
        st.markdown("""
        | SDK / Toolkit | Platform | Use |
        |---------------|----------|-----|
        | **Oculus SDK** | Meta devices | Hand tracking, spatial audio |
        | **SteamVR SDK** | Cross-platform | Non-Oculus support |
        | **ARCore / ARKit** | Android / iOS | Mobile AR |
        | **XR Interaction Toolkit** | Unity | Interaction scripts |
        """)

    st.header("🎨 3. 3D Modeling Tools for AR/VR")

    with st.expander("a. Blender (Free)"):
        st.markdown("""
        - Ideal for: **Animation**, **low-poly modeling**
        - Tools: Rigging, UV mapping, Mixamo export
        """)

    with st.expander("b. 3ds Max (Proprietary)"):
        st.markdown("""
        - Ideal for: **Architectural models**, **precise geometry**
        - Tools: CAD-to-VR pipeline, Unreal Engine integration
        """)

    st.header("📚 Summary Table: Tool-Task Mapping")
    st.markdown("""
    | Task | Recommended Tool |
    |------|------------------|
    | Model a building | 3ds Max |
    | Animate a character | Blender |
    | Build VR app | Unity / Unreal |
    | Add hand tracking | Oculus SDK / XR Toolkit |
    | Deploy AR to mobile | Unity + ARCore/ARKit |
    | High-end archviz | Unreal + 3ds Max |
    """)

    st.success("This module gives a complete overview of AR/VR hardware, software, and design tools for beginners.")





    st.title("🕶️ VR Concepts and Cup-Grabbing Demo")

    st.header("🔑 Key Features of VR")

    with st.expander("1. Immersion"):
        st.markdown("""
        - **Full field of view (FOV):** Surrounds user vision.
        - **Spatial audio:** Sounds come from all directions.
        """)

    with st.expander("2. Interactivity"):
        st.markdown("""
        - Users can **grab objects**, teleport, and interact with virtual environments.
        - Unity example: Use XR Toolkit to grab a cup and trigger reactions.
        """)

    with st.expander("3. Presence"):
        st.markdown("""
        - The **feeling of truly 'being there'** in the virtual world.
        - Achieved with realism, physics, and responsive design.
        """)

    st.info("🎯 *Example:* When a user grabs a virtual cup in Unity using the XR Toolkit, the object responds, enhancing immersion and presence.")

    st.header("☕ How to Create 'Grab a Cup' VR Demo")

    st.subheader("🛠️ In Unity (with XR Toolkit)")

    with st.expander("Steps in Unity"):
        st.markdown("""
        1. **Create Project**: Open Unity 3D project with XR Plugin Management.
        2. **Install XR Toolkit**: Via Package Manager; enable Input System.
        3. **Setup XR Rig**: Add XR Rig prefab and left/right controllers.
        4. **Import Cup Model**: Use `.fbx` from Blender or 3ds Max.
        5. **Make Cup Grabbable**:
           - Add `XR Grab Interactable`
           - Add `Rigidbody` (Use Gravity)
           - Add `Collider`
        6. **Test in VR**: Use simulator or build to Quest/Vive.
        """)

    st.subheader("🎨 In Blender")

    with st.expander("Steps in Blender"):
        st.markdown("""
        1. **Create Cup**: Add Cylinder → Shape body & handle using extrude.
        2. **Add Materials**: Ceramic/glass shader via Shader Editor.
        3. **Export**: File → Export as `.fbx` or `.obj` (Apply Transforms).
        4. **Import to Unity**: Drop into Assets folder and drag to scene.
        """)

    st.subheader("🏛️ In 3ds Max")

    with st.expander("Steps in 3ds Max"):
        st.markdown("""
        1. **Model Cup**: Use 2D spline → Apply Lathe modifier.
        2. **Apply Materials**: Use Physical Material Editor.
        3. **Export**: File → Export → `.fbx` (Embed Media ON).
        4. **Import to Unity**: Drag into Unity, position in scene.
        """)

    st.header("📚 Summary Table: Tool vs Purpose")

    st.markdown("""
    | Tool | Purpose | Key Steps |
    |------|---------|-----------|
    | **Unity** | Interactivity (grab, respond) | XR Toolkit, Grab Interactable |
    | **Blender** | 3D modeling & animation | Mesh, material, export `.fbx` |
    | **3ds Max** | High-detail modeling | Lathe, material, export `.fbx` |
    """)

    st.success("You can use this workflow to create a hands-on student demo or a mini-project on 'Interactive VR Objects'.")


    st.header("🏗️ Creating a Virtual Environment")

    st.subheader("🎨 Tools Involved")

    with st.expander("Blender: Modeling, Sculpting, Texturing"):
        st.markdown("""
        - **Modeling:** Use basic mesh tools (cube, plane, cylinder).
        - **Sculpting:** Organic terrain, characters.
        - **Texturing:** UV unwrap + texture painting.
        - **Export Format:** `.fbx` with scale and transform applied.
        """)

    with st.expander("🏛️ 3ds Max: Precision Architecture"):
        st.markdown("""
        - Use **splines + modifiers** (e.g., Extrude, Lathe).
        - Ideal for **interior/exterior** environments.
        - Apply **materials & lighting** before exporting.
        - Export as `.fbx` with textures embedded.
        """)

    with st.expander("🧠 Unity: Scene Assembly and Interactions"):
        st.markdown("""
        - **Import** `.fbx` files into Unity's Assets folder.
        - Add **lights, cameras, skybox**.
        - Use **XR Toolkit** for interaction scripting (grabbing, teleport).
        - Set colliders, rigidbodies, and interaction layers.
        """)

    st.subheader("🔄 Workflow Summary")

    st.markdown("""
    1. **Model in Blender/3ds Max**
    2. **Export as .fbx** (make sure textures/materials are ready)
    3. **Import to Unity** (Assets → Drag & Drop)
    4. **Setup Environment:**
       - Add terrain, lighting, camera
       - Place models
       - Add interaction scripts
    5. **Test in VR or use Simulator**
    """)

    st.success("✅ This pipeline is ideal for student projects on environment creation for AR/VR apps.")

# Activities Section
elif selection == "Activities":
    st.header("\U0001F91D Collaborative & Instructional Activities")

    st.subheader("Collaborative: VR Around Us")
    st.markdown("""
Groups research a VR use case, describe goals, tools, reasons, and success.
    """)

    st.subheader("Instructional: Design Your Virtual Space")
    st.markdown("""
Students plan and present a functional VR space (e.g., gallery, station), using a table:

| Feature | Implementation | Tools |
|---------|----------------|-------|
| Immersion | 360 view, SFX | Unity |
| Interactivity | Click/grab | Colliders |
| Presence | Feedback, lighting | Sensors |
    """)

# Tools & Examples Section
elif selection == "3D Tools & Examples":

    st.title("🧱 3D Modeling Basics for AR/VR Projects")

    st.header("🎨 Blender – Organic, Artistic 3D Tool")

    with st.expander("🌟 Basics"):
        st.markdown("""
        - **Primitives**: Cube, Sphere, Cylinder, Cone, Monkey (Suzanne)
        - **Sculpting Tools**: Dynamic topology, multiresolution sculpt
        - **Modifiers**:
            - Subdivision Surface (for smoothing)
            - Mirror (for symmetry)
            - Boolean (for cutout/merge)
        - **UV Unwrapping**: For precise texture painting
        """)

    with st.expander("💡 Lighting & Camera"):
        st.markdown("""
        - **Lights**: Point, Area, Spot, Sun
        - **Shadows**: Use Cycles or Eevee with soft/hard shadows
        - **Camera Setup**: Lock camera to view, adjust depth of field
        """)

    with st.expander("🎞️ Animation"):
        st.markdown("""
        - **Keyframe Animation**: Move/rotate/scale over timeline
        - **Rigging**: Add bones (Armature) for character animation
        - **Timeline & Dope Sheet**: For smooth control
        """)

    st.info("🛠️ Example: Create a detailed car with modifiers and texture it using UV map. Export as `.fbx` to Unity.")

    st.header("🏛️ 3ds Max – Architectural & Precision Tool")

    with st.expander("🔧 Modeling Essentials"):
        st.markdown("""
        - **Standard Primitives**: Box, Cylinder, Torus, Teapot
        - **Extended Primitives**: Hedra, Chamfer Box
        - **Modifiers**:
            - Bend, Taper, Twist
            - Shell (to give thickness)
            - Lattice (for wireframes)
        """)

    with st.expander("🏙️ Architecture Tools"):
        st.markdown("""
        - **2D Spline Drawing + Modifier**: Extrude, Bevel, Lathe
        - **CAD Import**: Use `.dwg` files for precision designs
        """)

    with st.expander("🔦 Lighting & Rendering"):
        st.markdown("""
        - **Photometric Lights**, **Target Spot**, **Omni**
        - Shadow Parameters: Ray Traced, Area Shadows
        - Use **Arnold Renderer** for high-quality outputs
        """)

    with st.expander("📸 Camera & Animation"):
        st.markdown("""
        - **Camera Types**: Free, Target, Physical Camera
        - **Walkthrough Animation**: Animate camera paths
        - **Auto Key/Set Key** system for object animation
        """)

    st.success("🎯 Example: Model a multi-floor building with materials and daylight system. Export to Unity for interaction.")

    st.header("🛠️ Export Workflow to Unity")

    st.markdown("""
    - ✅ Apply all transforms and materials before export
    - 🧾 Export Format: `.fbx` (Recommended for Unity)
    - 🎯 Drag-and-drop `.fbx` files into Unity Assets
    - 🎮 Add Interactions in Unity (XR Toolkit, physics, etc.)
    """)

    st.markdown("---")
    st.subheader("📌 Summary Table")

    st.markdown("""
    | Tool | Best For | Key Features |
    |------|----------|--------------|
    | **Blender** | Organic modeling | Sculpting, Modifiers, Animation |
    | **3ds Max** | CAD-style precision | Architectural modeling, Walkthroughs |
    | **Unity** | Integration & Interactivity | Scene setup, VR toolkit, scripting |
    """)

    st.warning("👨‍🏫 Tip: Learn Blender for modeling basics and 3ds Max for CAD-style accuracy. Combine both in Unity for immersive VR scenes.")


    st.subheader("Scene Setup in Unity")
    st.markdown("""
- Import FBX from Blender/Max
- Use XR Toolkit for hands/controllers
- Add colliders, audio sources, lighting

**Example:** Set up a room scene where users can walk and pick up items.
    """)




# Export Content Section
elif selection == "Export Notes":
    st.header("\U0001F4BE Export Lecture Notes")

    notes = """
Virtual Reality (VR) Notes

1. What is VR?
- Immersive simulation with headsets and 3D environments

2. VR vs AR
- VR = Replaces world; AR = Enhances it

3. Tools
- Blender: Organic modeling
- 3ds Max: Precise CAD
- Unity: VR scripting, deployment

4. Scene Setup
- Model → Export FBX → Unity → Add Interactions

5. Benefits & Challenges
- + Engaging, immersive
- - Hardware cost, motion sickness

Activities:
- VR Debates
- Group modeling
- Virtual space planning
    """

