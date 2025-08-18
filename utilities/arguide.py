import streamlit as st
import pandas as pd

# App Title
st.title("📱 AR Development Platforms, Devices, Hardware & Tools")

st.sidebar.header("Navigation")
section = st.sidebar.radio("Go to", [
    "AR Platforms & Tools",
    "AR Devices & Hardware",
    "Software Development in AR",
    "Exercises",
    "Activities",
    "Summary & References"
])

# Section 1: AR Platforms & Tools
if section == "AR Platforms & Tools":
    st.header("🚀 AR Development Platforms")
    st.markdown("""
    Below are the key platforms for building Augmented Reality (AR) applications, with **capabilities** and **recent advancements** so learners can choose the best tool for a use‑case.
    """)

    with st.expander("Unity (AR Foundation)"):
        st.markdown("""
        **What it is:** Unity's cross‑platform layer that targets ARKit (iOS), ARCore (Android) and OpenXR devices from a single codebase.

        **Core capabilities:** Plane/point/face tracking, anchors, hit‑testing, light/ambient intensity estimation, image/object tracking, occlusion with depth, environment probes, AR meshes.

        **Recent advancements / notes:**
        - **OpenXR + XR Hands**: unified input/hand‑tracking across vendors; easier multi‑device support.
        - **AR Background & Occlusion pipeline** improvements for more stable depth‑based occlusion.
        - **Scene reconstruction / meshing** APIs for denser meshes on LiDAR devices.
        - **XR Interaction Toolkit** mature for drag/scale/rotate, ray and direct interaction in AR.
        - **Vision/Spatial platforms** via provider plugins (where supported) and **Runtime Feature Flags** to trim builds.

        **Best for:** Cross‑platform education apps, AR games, product visualization, quick prototyping with Asset Store.
        """)

    with st.expander("Unreal Engine"):
        st.markdown("""
        **What it is:** High‑fidelity real‑time engine with AR support via platform plugins (ARKit/ARCore/OpenXR).

        **Core capabilities:** World/face tracking, image tracking, anchors, hit‑testing; Niagara VFX for particle‑heavy AR; cinematic rendering.

        **Recent advancements / notes:**
        - **UE5 rendering stack (Nanite/Lumen) mobile tuning** enables higher visual quality on supported devices.
        - **OpenXR‑first workflow** for input and anchors; improved AR templates/blueprints.
        - **Efficient mobile materials** and **Virtual Production** crossover for on‑device previz.

        **Best for:** Architectural visualization, film/cinematic AR, enterprise demos where visual fidelity is critical.
        """)

    with st.expander("WebAR (8th Wall, Zappar, WebXR)"):
        st.markdown("""
        **What it is:** AR delivered in the browser. Build once, run without an app install.

        **Core capabilities:** World tracking (SLAM), image/marker tracking, face tracking, hit‑testing, anchors, light estimation; integrates with Three.js/Babylon.

        **Recent advancements / notes:**
        - **WebXR**: stabilized modules for **hit‑test**, **anchors**, **DOM overlay**, and **handed‑input** on more devices.
        - **Depth/segmentation** on select devices for **people occlusion** and improved placement.
        - **8th Wall/Zappar** added visual pipelines for try‑ons, link‑out commerce, and geospatial placement.

        **Best for:** Campaigns, education links, posters/QR activations, e‑commerce try‑ons, rapid distribution.
        """)

    with st.expander("ARKit (Apple)"):
        st.markdown("""
        **What it is:** Apple's native AR framework for iPhone/iPad (with tight hardware integration and LiDAR on Pro devices).

        **Core capabilities:** World/plane tracking, face tracking (TrueDepth), **People Occlusion**, **Scene Geometry** (LiDAR meshes), motion capture/body tracking, image/object tracking, location anchors.

        **Recent advancements / notes:**
        - **RoomPlan & Scene Reconstruction** APIs for quick room scanning and parametric export.
        - **Improved LiDAR depth** stability and mesh classification (floors, walls, seats where available).
        - **App Clips + AR Quick Look** for fast AR preview of USDZ models.

        **Best for:** High‑quality iOS AR, precise indoor scanning, education/health demos on iPad Pro/iPhone Pro.
        """)

    with st.expander("ARCore (Google)"):
        st.markdown("""
        **What it is:** Google's AR SDK for Android devices (and some cross‑platform features).

        **Core capabilities:** Motion tracking, plane detection, light estimation, image/face tracking, **Depth API** (occlusion), **Recording & Playback**.

        **Recent advancements / notes:**
        - **Geospatial API / VPS** for Earth‑scale anchors using Street View/photogrammetry; outdoor navigation and city‑scale AR.
        - **Scene Semantics** (where supported) and improved depth for more reliable occlusion.
        - **Raw Depth** access on capable devices for custom perception.

        **Best for:** Outdoor/location‑based AR, shared anchors, Android‑first experiences and measurement utilities.
        """)

    st.subheader("Feature Matrix (quick compare)")
    df = pd.DataFrame({
        "Platform": ["Unity AR Foundation", "Unreal Engine", "WebAR (WebXR)", "ARKit", "ARCore"],
        "Primary Targets": ["iOS, Android, OpenXR", "iOS, Android, OpenXR", "Modern mobile/desktop browsers", "iOS/iPadOS", "Android"],
        "Tracking": ["World/Face/Image/Object", "World/Face/Image", "World/Face/Image (impl.‑dependent)", "World/Face/Body/Image/Object", "World/Face/Image"],
        "Depth/Occlusion": ["Yes (providers)", "Device‑dependent", "Limited/Device‑dependent", "LiDAR + People Occlusion", "Depth API + Occlusion"],
        "Anchors/Shared": ["Anchors; multi‑user via netcode", "Anchors; OpenXR", "Anchors (WebXR/engine)", "Location Anchors", "Geospatial Anchors"],
        "Notable Recent": ["XR Hands, improved occlusion, meshing", "OpenXR templates, UE5 mobile fidelity", "WebXR anchors/hit‑test, depth seg.", "RoomPlan, better LiDAR meshes", "Geospatial API, Scene Semantics"],
    })
    st.dataframe(df, use_container_width=True)

# Section 2: AR Devices & Hardware
elif section == "AR Devices & Hardware":
    st.header("🔧 AR Devices & Hardware")
    st.markdown("""
    **AR Hardware Examples:**
    - **Smartphones/Tablets:** Widely used AR devices (ARKit/ARCore).
    - **AR Glasses:** Microsoft HoloLens, Magic Leap, NReal.
    - **Head-Mounted Displays (HMDs):** See-through AR headsets.
    - **Sensors & Cameras:** Depth sensors, LiDAR, RGB-D cameras.
    - **Wearables:** Smart AR contact lenses (emerging).

    **Use Cases:**
    - **Education:** AR headsets for immersive learning.
    - **Retail:** AR glasses for try-on experiences.
    - **Industry:** Remote assistance & design visualization.
    """)

# Section 3: Software Development in AR
elif section == "Software Development in AR":
    st.header("💻 Software Development for AR")
    st.markdown("""
    **Key Components:**
    - **SDKs:** ARKit (iOS), ARCore (Android), Vuforia, Wikitude.
    - **Engines:** Unity, Unreal Engine.
    - **APIs:** WebXR, OpenXR, AR Foundation.
    - **IDEs:** Xcode, Android Studio, Visual Studio, Unity Hub.

    **Development Workflow:**
    1. Select platform (Unity, WebAR, etc.)
    2. Import SDK/Plugin
    3. Design AR scene with 3D models
    4. Add interaction (tap, gestures, voice)
    5. Test on emulator & real device
    6. Deploy to App Store / Play Store / Web
    """)

# Section 4: Exercises
elif section == "Exercises":
    st.header("📝 Exercises")
    st.markdown("""
    **Exercise 1: Unity (AR Foundation)**  
    - Build a cube placement app with plane detection.

    **Exercise 2: Unreal Engine AR**  
    - Create an AR portal doorway to a 3D world.

    **Exercise 3: WebAR**  
    - Design an AR business card with QR code.

    **Exercise 4: ARKit (iOS)**  
    - Build a Face Mask AR Filter using Xcode + ARKit.

    **Exercise 5: ARCore (Android)**  
    - Create a virtual chair placement app with plane detection.
    """)

# Section 5: Activities
elif section == "Activities":
    st.header("🎯 Activities")
    st.markdown("""
    **Activity 1: Platform Debate**  
    - Groups compare Unity, Unreal, WebAR, ARKit, ARCore.  
    **Guidelines:**
    1. Form 5 groups, each assigned a platform.
    2. Research platform strengths, weaknesses, and real-world use cases.
    3. Prepare a 5-minute presentation per group.
    4. Engage in moderated debate, answering peer questions.
    5. Class votes on the best platform for specific scenarios (education, gaming, retail).

    **Activity 2: AR Hackathon**  
    - Teams build AR apps (e.g., AR Museum Guide, AR Shopping Try-On).  
    **Guidelines:**
    1. Teams of 3–5 students.
    2. Time limit: 2–3 hours.
    3. Choose a theme (Education, Healthcare, Retail, Entertainment).
    4. Use any AR platform (Unity, Unreal, WebAR, ARKit, ARCore).
    5. Present prototype/demo to judges/class.
    6. Evaluation Criteria: Creativity (30%), Technical Implementation (40%), Presentation (30%).

    **Activity 3: AR Scavenger Hunt**  
    - QR codes linked to AR 3D clues hidden around campus.

    **Activity 4: Cross-Platform Challenge**  
    - Implement object placement across multiple platforms and compare.
    """)

# Section 6: Summary & References
elif section == "Summary & References":
    st.header("📚 Summary & References")
    st.markdown("""
    **Summary:**
    - Unity & Unreal dominate AR app development.
    - WebAR enables app-less AR experiences.
    - ARKit & ARCore lead mobile AR on iOS & Android.
    - AR hardware ranges from smartphones to AR glasses & sensors.

    **References:**
    - Unity AR Foundation Docs
    - Unreal Engine AR Docs
    - Google ARCore Developer Guide
    - Apple ARKit Developer Guide
    - WebXR Device API (MDN)
    """)
