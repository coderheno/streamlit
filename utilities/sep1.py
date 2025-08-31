# streamlit_app.py
# Full-featured Streamlit teaching tool for: Spatial Mapping & Surface Detection in AR
# Topics covered: AR Systems & Surface Detection, Spatial Mapping, Surface Detection Algorithms,
# Designing User Interactions, Basic Interaction Techniques, Implementing Interactions in a Real-World Scenario

import streamlit as st
import numpy as np
from io import BytesIO
import textwrap

# -------------------------------
# App Setup
# -------------------------------
st.set_page_config(page_title="AR Teaching Tool: Spatial Mapping & Interactions", layout="wide")

# Initialize session state
if "scores" not in st.session_state:
    st.session_state.scores = {}
if "total_questions" not in st.session_state:
    st.session_state.total_questions = {}
if "pose" not in st.session_state:
    # Pose for interaction simulator
    st.session_state.pose = {
        "placed": False,
        "x": 0.5,    # normalized 0..1
        "y": 0.5,    # normalized 0..1
        "scale": 1.0,
        "rotation_deg": 0.0,
    }
if "visited" not in st.session_state:
    st.session_state.visited = set()

# -------------------------------
# Helpers
# -------------------------------

def md_download_button(filename: str, content: str, label: str = "Download notes (MD)"):
    b = content.encode("utf-8")
    st.download_button(label=label, data=b, file_name=filename, mime="text/markdown")


def render_quiz(topic_key: str, questions):
    st.subheader("Activity • Quiz")
    correct = 0
    total = len(questions)
    for i, q in enumerate(questions, 1):
        st.markdown(f"**Q{i}. {q['q']}**")
        ans = st.radio("Select one:", q["options"], key=f"{topic_key}_q{i}")
        if ans:
            if ans == q["answer"]:
                st.success("Correct ✅" + (f" — {q.get('explain','')}" if q.get('explain') else ""))
                correct += 1
            else:
                st.error("Not quite ❌")
                if q.get("explain"):
                    st.info(q["explain"])
        st.divider()
    st.session_state.scores[topic_key] = correct
    st.session_state.total_questions[topic_key] = total
    st.toast(f"{topic_key}: {correct}/{total} correct", icon="✅" if correct==total else "ℹ️")


def progress_bar():
    # Overall progress across topics based on quizzes attempted
    total_q = sum(st.session_state.total_questions.values())
    total_c = sum(st.session_state.scores.values())
    pct = (total_c/total_q) if total_q > 0 else 0
    st.progress(pct)
    st.caption(f"Overall quiz progress: {total_c}/{total_q} correct")


def wrap(text):
    return "\n".join(textwrap.wrap(text, width=90))


# -------------------------------
# Notes content (Markdown strings)
# -------------------------------
notes_home = wrap(
    """
    # AR Spatial Mapping & Surface Detection – Teaching Tool

    **Learning Outcomes**
    - Understand AR surface/plane detection and spatial mapping concepts.
    - Explain and compare core algorithms (RANSAC, SLAM, ICP) used in AR pipelines.
    - Design intuitive, low-friction interactions for virtual objects (tap, drag, rotate, scale).
    - Implement a simple end-to-end AR interaction flow (conceptually) with clear UX cues.

    **Syllabus Topics**
    1. AR Systems and Surface Detection
    2. Spatial Mapping in AR
    3. Surface Detection Algorithms
    4. Designing User Interactions with Virtual Objects
    5. Basic Interaction Techniques
    6. Implementing Interactions in a Real-World Scenario

    **Suggested Platforms/Libraries**
    - Mobile SDKs: ARKit (iOS), ARCore (Android)
    - Cross-platform engine: Unity with AR Foundation
    - Head-mounted: HoloLens (Windows MR)

    **Assessment**: Quizzes + in-class design exercise + mini implementation case study.
    """
)

notes_ar_systems = wrap(
    """
    ## AR Systems & Surface Detection

    **What is surface detection?**
     
        The process of identifying trackable, typically planar regions (e.g., floors, tables, walls) in the physical environment so virtual objects can be placed with correct pose and scale.

    
    **Sensors & Signals**
    - RGB camera (features, textures)
    - IMU (gyroscope, accelerometer)
    - Depth (LiDAR/ToF/structured light) — where available

    **Pipeline (high level)**
    1) Feature points → 2) Plane hypotheses → 3) Verify/fit plane model (e.g., RANSAC) → 4) Track over time → 5) Surface anchors.

    **SDK support**
    - **ARKit**: horizontal/vertical plane detection, scene reconstruction, LiDAR (Pro devices)
    - **ARCore**: plane detection, depth-from-motion, scene geometry API
    - **Unity AR Foundation**: cross-platform abstraction for plane/anchor managers

    **Design concern**: Communicate tracking quality to users (visual dots/mesh, coaching overlays).
    """
)

notes_spatial_mapping = wrap(
    """
    ## Spatial Mapping in AR

    **Definition**: Building a 3D representation of the nearby environment (point cloud → mesh) enabling physically plausible placement, occlusion, and interaction.

    **Why it matters**
    - Correct occlusion (real objects hide virtual ones) → realism
    - Physics-aware placement and navigation
    - Persistent anchors and world understanding

    **Typical steps**
    - Scan motion → triangulate points (SfM/SLAM)
    - Estimate planes and non-planar geometry
    - Produce mesh + per-vertex confidence

    **Applications**: indoor navigation, furniture preview, educational overlays, maintenance guidance.
    """
)

notes_algorithms = wrap(
    """
    ## Surface Detection Algorithms

    **RANSAC (Random Sample Consensus)**
    - Robust model fitting amidst outliers; commonly used for plane fitting on sparse features.

    **SLAM (Simultaneous Localization and Mapping)**
    - Estimates camera trajectory while building a map; variants include visual-inertial SLAM.

    **ICP (Iterative Closest Point)**
    - Registers/alignment of point clouds; useful for refining surfaces and mesh consistency.

    **Challenges**
    - Low-texture/reflective surfaces, motion blur, low light
    - Dynamic scenes (moving objects)
    - Scale drift without absolute depth
    """
)

notes_design_interactions = wrap(
    """
    ## Designing User Interactions with Virtual Objects

    **Principles**
    - *Affordance*: make actions discoverable
    - *Feedback*: visual haptics/animations indicate success/error
    - *Constraints*: snap/limits prevent unwanted states

    **Common patterns**
    - Tap to place/select; drag to move along plane; pinch to scale; two-finger rotate.
    - Targeting aids (reticle), plane visualizers, anchor gizmos.

    **Accessibility**
    - Voice cues, haptic pulses, guided coach marks.
    """
)

notes_basic_techniques = wrap(
    """
    ## Basic Interaction Techniques

    - **Tap**: raycast to plane → place/select object at hit point
    - **Drag**: continuous raycast updates pose constrained to surface normal
    - **Pinch**: scale object proportionally with clamped limits
    - **Rotate**: delta angle from gesture → yaw about surface normal

    **Error handling**: show placeholder/ghost object until stable plane found.
    """
)

notes_implementing = wrap(
    """
    ## Implementing Interactions in a Real-World Scenario (Furniture Preview)

    **Flow**
    1) Start session → find plane (coach overlay)
    2) Tap to place furniture anchor
    3) Drag/rotate/scale with constraints and grid snapping
    4) Save/restore anchor for persistence between sessions

    **KPIs**: placement time, adjustment counts, tracking losses, user satisfaction.
    """
)

# -------------------------------
# Diagrams (Matplotlib)
# -------------------------------





# -------------------------------
# Activities / Simulations
# -------------------------------




# -------------------------------
# Quizzes per topic
# -------------------------------
quiz_ar_systems = [
    {
        "q": "Which signals are typically fused for robust plane detection?",
        "options": ["RGB only", "RGB + IMU (and depth if available)", "GPS only"],
        "answer": "RGB + IMU (and depth if available)",
        "explain": "Visual-inertial fusion stabilizes pose; depth sensors improve surface confidence."
    },
    {
        "q": "What is the purpose of a 'coaching overlay' during plane detection?",
        "options": ["Decorative UI", "Guide users to move device for better tracking", "Increase brightness"],
        "answer": "Guide users to move device for better tracking",
        "explain": "Movement parallax reveals features and improves plane estimation."
    },
]

quiz_spatial_mapping = [
    {
        "q": "Spatial mapping primarily enables which rendering effect?",
        "options": ["Bloom", "Occlusion (real hides virtual)", "Chromatic aberration"],
        "answer": "Occlusion (real hides virtual)",
        "explain": "A mesh of the environment allows correct depth testing for occlusion."
    },
    {
        "q": "A typical pipeline from motion to mesh includes:",
        "options": ["Audio → waveform → mesh", "Triangulation → plane estimation → meshing", "GPS → map tiles → mesh"],
        "answer": "Triangulation → plane estimation → meshing",
        "explain": "Structure-from-motion/SLAM yields points; planes and mesh follow."
    },
]

quiz_algorithms = [
    {
        "q": "RANSAC is best described as:",
        "options": ["A rendering shader", "A robust model fitting method", "A compression codec"],
        "answer": "A robust model fitting method",
        "explain": "RANSAC samples minimal sets, votes, and selects the best-fitting model."
    },
    {
        "q": "SLAM simultaneously estimates:",
        "options": ["Object textures and shadows", "Camera pose and environment map", "Battery and temperature"],
        "answer": "Camera pose and environment map",
        "explain": "Core SLAM output is trajectory + map."
    },
]

quiz_design = [
    {
        "q": "Which is a good feedback mechanism for a successful placement?",
        "options": ["Silent UI", "Subtle scale pop + haptic tick", "Full-screen alert"],
        "answer": "Subtle scale pop + haptic tick",
        "explain": "Immediate, lightweight feedback confirms action without distraction."
    },
    {
        "q": "Affordance in AR UI means:",
        "options": ["Random animations", "Action hints that reveal possible interactions", "Battery saving"],
        "answer": "Action hints that reveal possible interactions",
        "explain": "Affordances help users discover gestures and constraints."
    },
]

quiz_basic = [
    {
        "q": "Pinch gesture in AR typically maps to:",
        "options": ["Scale", "Rotate", "Duplicate"],
        "answer": "Scale",
        "explain": "Pinch distance controls uniform scaling with limits."
    },
    {
        "q": "Dragging an object usually constrains motion:",
        "options": ["Along detected plane", "In 3D freely without constraints", "Only vertically"],
        "answer": "Along detected plane",
        "explain": "Constraining to the plane avoids depth jumps and preserves realism."
    },
]

quiz_implementing = [
    {
        "q": "First-time user flow should begin with:",
        "options": ["Demanding sign-in", "Coach to find a plane", "Immediate object purchase"],
        "answer": "Coach to find a plane",
        "explain": "Placement depends on a stable plane; teach users quickly."
    },
    {
        "q": "A persistence strategy for saved objects is:",
        "options": ["Randomize every launch", "Save anchor IDs/poses and restore on relocalization", "Ask user to measure room each time"],
        "answer": "Save anchor IDs/poses and restore on relocalization",
        "explain": "Anchors allow consistent world locations across sessions."
    },
]

# -------------------------------
# UI Layout
# -------------------------------
with st.sidebar:
    st.title("AR Teaching Tool")
    st.caption("Spatial Mapping & Surface Detection • Interactions")
    topic = st.radio(
        "Select Topic",
        [
            "Home",
            "AR Systems & Surface Detection",
            "Spatial Mapping in AR",
            "Surface Detection Algorithms",
            "Designing User Interactions",
            "Basic Interaction Techniques",
            "Implementing Interactions",
        ],
        index=0,
    )
    st.markdown("---")
    progress_bar()
    st.markdown("---")
    st.info("Tip: Use the Activities and Simulators to spark discussion.")

# -------------------------------
# Pages
# -------------------------------
if topic == "Home":
    st.title("AR Spatial Mapping & Surface Detection – Teaching Tool")
    colA, colB = st.columns([2,1])
    with colA:
        st.markdown(notes_home)
        md_download_button("01_home_notes.md", notes_home)
        
    with colB:
        st.markdown("### SLAM overview")
        

elif topic == "AR Systems & Surface Detection":
    st.header("AR Systems & Surface Detection")
    tabs = st.tabs(["Lecture", "Activity", "Quiz", "Code", "Notes"])
    with tabs[0]:
        st.markdown(notes_ar_systems)
        
    with tabs[1]:
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[2]:
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[3]:
        st.subheader("Sample snippets")
        st.markdown("**Unity (AR Foundation) – plane manager**")
        st.code(
            """
            using UnityEngine.XR.ARFoundation;
            using UnityEngine; 
            public class PlaneLogger : MonoBehaviour {
                public ARPlaneManager planeManager;
                void Update(){
                    foreach (var plane in planeManager.trackables){
                        Debug.Log($"Plane {plane.trackableId} center: {plane.center}");
                    }
                }
            }
            """,
            language="csharp",
        )
        st.markdown("**ARKit (Swift) – enable plane detection**")
        st.code(
            """
            import ARKit
            let config = ARWorldTrackingConfiguration()
            config.planeDetection = [.horizontal, .vertical]
            sceneView.session.run(config)
            """,
            language="swift",
        )
    with tabs[4]:
        md_download_button("02_ar_systems_notes.md", notes_ar_systems)

elif topic == "Spatial Mapping in AR":
    st.header("Spatial Mapping in AR")
    tabs = st.tabs(["Lecture", "Activity", "Quiz", "Code", "Notes"])
    with tabs[0]:
        st.markdown(notes_spatial_mapping)
        
    with tabs[1]:
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[2]:
        render_quiz("Spatial Mapping", quiz_spatial_mapping)
    with tabs[3]:
        st.subheader("ARKit Scene Reconstruction (concept)")
        st.code(
            """
            // Pseudocode: enable scene reconstruction (LiDAR-enabled devices)
            import ARKit
            let config = ARWorldTrackingConfiguration()
            if ARWorldTrackingConfiguration.supportsSceneReconstruction(.mesh) {
                config.sceneReconstruction = .mesh
            }
            sceneView.session.run(config)
            """,
            language="swift",
        )
        st.subheader("Unity – Mesh occlusion material setup (concept)")
        st.code(
            """
            // Assign occlusion material to environment mesh for correct depth testing
            Renderer r = envMesh.GetComponent<Renderer>();
            r.sharedMaterial = occlusionMat; // writes depth only
            """,
            language="csharp",
        )
    with tabs[4]:
        md_download_button("03_spatial_mapping_notes.md", notes_spatial_mapping)

elif topic == "Surface Detection Algorithms":
    st.header("Surface Detection Algorithms")
    tabs = st.tabs(["Lecture", "Activity", "Quiz", "Code", "Notes"])
    with tabs[0]:
        st.markdown(notes_algorithms)
    with tabs[1]:
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[2]:
        render_quiz("Algorithms", quiz_algorithms)
    with tabs[3]:
        st.subheader("Python (concept) – minimal RANSAC plane fit outline")
        st.code(
            """
            import numpy as np
            def plane_from_points(p1,p2,p3):
                v1, v2 = p2-p1, p3-p1
                n = np.cross(v1, v2)
                d = -np.dot(n, p1)
                return n, d
            def ransac_plane(points, iters=200, thresh=0.02):
                rng = np.random.default_rng(0)
                best_inliers, best_model = 0, None
                N = len(points)
                for _ in range(iters):
                    idx = rng.choice(N, 3, replace=False)
                    n, d = plane_from_points(points[idx[0]], points[idx[1]], points[idx[2]])
                    n = n / (np.linalg.norm(n) + 1e-8)
                    dist = np.abs(points @ n + d)
                    inliers = (dist < thresh).sum()
                    if inliers > best_inliers:
                        best_inliers, best_model = inliers, (n, d)
                return best_model
            """,
            language="python",
        )
    with tabs[4]:
        md_download_button("04_algorithms_notes.md", notes_algorithms)

elif topic == "Designing User Interactions":
    st.header("Designing User Interactions with Virtual Objects")
    tabs = st.tabs(["Lecture", "Activity", "Quiz", "Code", "Notes"])
    with tabs[0]:
        st.markdown(notes_design_interactions)
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[1]:
        st.markdown("**Group task:** Map gestures to actions for an AR lab guide.")
        st.markdown("- Define tap/drag/rotate/scale; add voice command for accessibility.")
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[2]:
        render_quiz("Design", quiz_design)
    with tabs[3]:
        st.subheader("Unity – gesture mapping (concept)")
        st.code(
            """
            void Update(){
                if (Input.touchCount == 1) { /* tap/drag */ }
                if (Input.touchCount == 2) { /* pinch/rotate */ }
            }
            """,
            language="csharp",
        )
    with tabs[4]:
        md_download_button("05_design_interactions_notes.md", notes_design_interactions)

elif topic == "Basic Interaction Techniques":
    st.header("Basic Interaction Techniques")
    tabs = st.tabs(["Lecture", "Activity", "Quiz", "Code", "Notes"])
    with tabs[0]:
        st.markdown(notes_basic_techniques)
    with tabs[1]:
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[2]:
        render_quiz("Basic Techniques", quiz_basic)
    with tabs[3]:
        st.subheader("Unity – tap detection")
        st.code(
            """
            if (Input.touchCount > 0){
                var t = Input.GetTouch(0);
                if (t.phase == TouchPhase.Began){ Debug.Log("Tap"); }
            }
            """,
            language="csharp",
        )
    with tabs[4]:
        md_download_button("06_basic_techniques_notes.md", notes_basic_techniques)

elif topic == "Implementing Interactions":
    st.header("Implementing Interactions in a Real-World Scenario")
    tabs = st.tabs(["Lecture", "Activity", "Quiz", "Code", "Notes"])
    with tabs[0]:
        st.markdown(notes_implementing)
    with tabs[1]:
        st.markdown("**Case study:** Furniture preview (place/scale/rotate on floor plane).")
        render_quiz("AR Systems", quiz_ar_systems)
    with tabs[2]:
        render_quiz("Implementation", quiz_implementing)
    with tabs[3]:
        st.subheader("Unity – end-to-end flow (pseudo)")
        st.code(
            """
            // 1) Wait for plane; 2) Raycast on tap; 3) Spawn prefab at hit; 4) Manipulate with gestures
            """,
            language="csharp",
        )
    with tabs[4]:
        md_download_button("07_implementing_notes.md", notes_implementing)

# Footer
st.markdown("---")
st.caption("© AR Teaching Tool • Built with Streamlit. Use Activities + Quizzes to reinforce learning.")
