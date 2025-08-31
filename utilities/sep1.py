# streamlit_app.py
# Full-featured Streamlit teaching tool for: Spatial Mapping & Surface Detection in AR
# Topics covered: AR Systems & Surface Detection, Spatial Mapping, Surface Detection Algorithms,
# Designing User Interactions, Basic Interaction Techniques, Implementing Interactions in a Real-World Scenario

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
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

def diagram_pipeline_surface_detection():
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.axis('off')
    steps = ["Features", "Plane\nHypotheses", "RANSAC\nFit", "Track", "Anchors"]
    x = 0.05
    for s in steps:
        ax.add_patch(Rectangle((x, 0.3), 0.16, 0.4, fill=False))
        ax.text(x+0.08, 0.5, s, ha='center', va='center')
        x += 0.2
    # arrows
    for i in range(5-1):
        ax.add_patch(FancyArrow(0.21 + 0.2*i, 0.5, 0.06, 0, width=0.01, head_width=0.05, head_length=0.03))
    return fig


def diagram_slam_flow():
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.axis('off')
    blocks = ["Cam/IMU\nInput", "Feature\nTracking", "Pose\nEstimation", "Map\nUpdate", "Loop\nClosure"]
    x = 0.05
    for b in blocks:
        ax.add_patch(Rectangle((x, 0.3), 0.16, 0.4, fill=False))
        ax.text(x+0.08, 0.5, b, ha='center', va='center')
        x += 0.2
    for i in range(len(blocks)-1):
        ax.add_patch(FancyArrow(0.21 + 0.2*i, 0.5, 0.06, 0, width=0.01, head_width=0.05, head_length=0.03))
    return fig


def diagram_gesture_cheatsheet():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.axis('off')
    # Draw simple phone and gesture icons
    ax.add_patch(Rectangle((0.05, 0.2), 0.2, 0.6, fill=False))
    ax.text(0.15, 0.85, "Tap", ha='center')
    ax.plot([0.15], [0.5], marker='o')

    ax.add_patch(Rectangle((0.4, 0.2), 0.2, 0.6, fill=False))
    ax.text(0.5, 0.85, "Pinch", ha='center')
    ax.plot([0.45, 0.55], [0.5, 0.5], marker='o')
    ax.add_patch(FancyArrow(0.46, 0.5, -0.05, 0, width=0.005, head_width=0.04, head_length=0.02))
    ax.add_patch(FancyArrow(0.54, 0.5, 0.05, 0, width=0.005, head_width=0.04, head_length=0.02))

    ax.add_patch(Rectangle((0.75, 0.2), 0.2, 0.6, fill=False))
    ax.text(0.85, 0.85, "Rotate", ha='center')
    circle = plt.Circle((0.85, 0.5), 0.1, fill=False)
    ax.add_patch(circle)
    ax.add_patch(FancyArrow(0.85, 0.62, 0.0, -0.05, width=0.005, head_width=0.04, head_length=0.02))
    return fig


# -------------------------------
# Activities / Simulations
# -------------------------------

def activity_bbox_simulator():
    st.markdown("**Hands-on:** Simulate surface selection by drawing a bounding box on an image.")
    uploaded = st.file_uploader("Upload a room photo (JPG/PNG)", type=["jpg", "jpeg", "png"], key="bbox_img")
    if uploaded:
        import PIL.Image as Image
        img = Image.open(uploaded).convert("RGB")
        w, h = img.size
        st.image(img, caption=f"Image {w}x{h}", use_column_width=True)
        st.write("Select bounding box (normalized coordinates)")
        x = st.slider("x (left)", 0.0, 0.9, 0.2, 0.01)
        y = st.slider("y (top)", 0.0, 0.9, 0.2, 0.01)
        bw = st.slider("width", 0.05, 1.0 - x, 0.5, 0.01)
        bh = st.slider("height", 0.05, 1.0 - y, 0.3, 0.01)
        # visualize
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')
        ax.add_patch(Rectangle((x*w, y*h), bw*w, bh*h, fill=False, linewidth=2))
        st.pyplot(fig, use_container_width=True)
        st.success("Pretend this is a candidate plane region; discuss stability and cues.")
    else:
        st.info("Upload an image to try the bounding box simulator.")


def activity_pointcloud_plane_demo():
    st.markdown("**Concept demo:** Plane fitting on a noisy point cloud.")
    n_plane = st.slider("Points on plane", 100, 2000, 800, 50)
    n_out = st.slider("Outliers", 0, 1000, 150, 25)
    noise = st.slider("Noise (σ)", 0.0, 0.1, 0.02, 0.005)

    # Generate synthetic plane z = 0.3x + 0.1y + 0.0 + noise
    rng = np.random.default_rng(42)
    X = rng.uniform(-1, 1, size=(n_plane, 2))
    Z = 0.3 * X[:, 0] + 0.1 * X[:, 1] + rng.normal(0, noise, size=n_plane)
    plane_pts = np.c_[X, Z]

    outliers = rng.uniform(-1, 1, size=(n_out, 3))
    pts = np.vstack([plane_pts, outliers])

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], s=4)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Synthetic point cloud with plane + outliers')
    st.pyplot(fig, use_container_width=True)
    st.info("Discuss: how RANSAC would sample, vote, and select best plane; impact of outliers.")


def activity_interaction_simulator():
    st.markdown("**Interaction Simulator:** Conceptual 2D plane with a virtual object.")
    col1, col2 = st.columns([1,1])
    with col1:
        placed = st.session_state.pose["placed"]
        st.checkbox("Placed?", value=placed, key="placed_check")
        st.session_state.pose["placed"] = st.session_state.placed_check
        if st.button("Tap to place at center"):
            st.session_state.pose.update({"placed": True, "x": 0.5, "y": 0.5})
        st.slider("X position", 0.0, 1.0, st.session_state.pose["x"], 0.01, key="xpos")
        st.slider("Y position", 0.0, 1.0, st.session_state.pose["y"], 0.01, key="ypos")
        st.slider("Scale", 0.2, 2.0, st.session_state.pose["scale"], 0.05, key="scale")
        st.slider("Rotation (deg)", -180.0, 180.0, st.session_state.pose["rotation_deg"], 1.0, key="rot")
        st.session_state.pose.update({"x": st.session_state.xpos, "y": st.session_state.ypos, "scale": st.session_state.scale, "rotation_deg": st.session_state.rot})
        if st.button("Reset"):
            st.session_state.pose.update({"placed": False, "x": 0.5, "y": 0.5, "scale": 1.0, "rotation_deg": 0.0})
    with col2:
        # Render a simple plane and a rectangle object
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        # plane grid
        for i in np.linspace(0, 1, 11):
            ax.plot([i, i], [0, 1], linewidth=0.3)
            ax.plot([0, 1], [i, i], linewidth=0.3)
        if st.session_state.pose["placed"]:
            cx, cy = st.session_state.pose["x"], st.session_state.pose["y"]
            s = 0.15 * st.session_state.pose["scale"]
            ax.text(0.03, 0.97, f"pos=({cx:.2f},{cy:.2f}) scale={st.session_state.pose['scale']:.2f} rot={st.session_state.pose['rotation_deg']:.0f}°", va='top')
            # Draw oriented rectangle representing the object
            theta = np.deg2rad(st.session_state.pose["rotation_deg"])
            # Corners of square centered at origin
            corners = np.array([[-s, -s], [s, -s], [s, s], [-s, s]])
            # Rotation
            R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
            rc = corners @ R.T
            rc[:, 0] += cx
            rc[:, 1] += cy
            poly = plt.Polygon(rc, fill=False, linewidth=2)
            ax.add_patch(poly)
            ax.plot(cx, cy, marker='o')
        else:
            ax.text(0.5, 0.5, "Tap to place", ha='center', va='center')
        st.pyplot(fig, use_container_width=True)


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
        st.pyplot(diagram_pipeline_surface_detection())
    with colB:
        st.markdown("### SLAM overview")
        st.pyplot(diagram_slam_flow())
        st.markdown("### Gesture cheatsheet")
        st.pyplot(diagram_gesture_cheatsheet())

elif topic == "AR Systems & Surface Detection":
    st.header("AR Systems & Surface Detection")
    tabs = st.tabs(["Lecture", "Activity", "Quiz", "Code", "Notes"])
    with tabs[0]:
        st.markdown(notes_ar_systems)
        st.pyplot(diagram_pipeline_surface_detection())
    with tabs[1]:
        activity_bbox_simulator()
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
        st.pyplot(diagram_slam_flow())
    with tabs[1]:
        activity_pointcloud_plane_demo()
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
        activity_pointcloud_plane_demo()
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
        st.pyplot(diagram_gesture_cheatsheet())
    with tabs[1]:
        st.markdown("**Group task:** Map gestures to actions for an AR lab guide.")
        st.markdown("- Define tap/drag/rotate/scale; add voice command for accessibility.")
        activity_interaction_simulator()
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
        activity_interaction_simulator()
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
        activity_interaction_simulator()
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
