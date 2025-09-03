import streamlit as st
#import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(page_title="Basic 3D Object Rendering & AR Steps", layout="wide")

# Tabs
tab1, tab2 = st.tabs(["🎨 3D Shape Rendering", "📘 Unity AR Exercise Steps"])

# ----------------- TAB 1: 3D Shape Rendering -----------------
with tab1:
    st.title("Basic 3D Object Rendering")
    st.write("""
    This exercise demonstrates rendering of basic 3D shapes (**Cube, Sphere, Pyramid**) using **Streamlit** and **Plotly**.
    Choose a shape and color, then view it in an interactive 3D environment.
    """)

    # Shape selection
    shape = st.selectbox("Choose Shape", ["Cube", "Sphere", "Pyramid"])
    color = st.color_picker("Pick a Color", "#FF0000")

    # Initialize Figure
#    fig = go.Figure()

    # Create Shapes
 #   if shape == "Cube":
  #      x = [0, 0, 1, 1, 0, 0, 1, 1]
   #     y = [0, 1, 1, 0, 0, 1, 1, 0]
    #    z = [0, 0, 0, 0, 1, 1, 1, 1]
     #   fig.add_trace(go.Mesh3d(
      #      x=x, y=y, z=z,
       #     i=[0, 0, 0, 1, 2, 4],
        #    j=[1, 2, 4, 5, 3, 5],
         #   k=[2, 3, 5, 6, 7, 6],
          #  color=color,
           # opacity=0.6
       # ))

    #elif shape == "Sphere":
     #   phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:30j]
      #  x = np.sin(phi)*np.cos(theta)
       # y = np.sin(phi)*np.sin(theta)
        #z = np.cos(phi)
        #fig.add_trace(go.Surface(
          #  x=x, y=y, z=z,
           # colorscale=[[0, color], [1, color]]
        #))

    #else:  # Pyramid
     #   x = [0, 1, 1, 0, 0.5]
      #  y = [0, 0, 1, 1, 0.5]
       # z = [0, 0, 0, 0, 1]
        #fig.add_trace(go.Mesh3d(
         #   x=x, y=y, z=z,
          #  i=[0, 0, 0, 1, 2],
           # j=[1, 2, 3, 4, 4],
            #k=[4, 4, 4, 2, 3],
            #color=color,
          #  opacity=0.6
        #))

    # Adjust Layout
    #fig.update_layout(scene=dict(aspectmode="data"), margin=dict(l=0, r=0, t=0, b=0))

    # Display 3D Shape
    #st.plotly_chart(fig, use_container_width=True)

    # Shape Properties
    st.subheader("Shape Properties")
    if shape == "Cube":
        st.write("**Cube**: All sides equal, 6 faces, 8 vertices.")
    elif shape == "Sphere":
        st.write("**Sphere**: Perfectly round, no edges or vertices.")
    else:
        st.write("**Pyramid**: Square base with triangular sides.")

    st.caption("Built with Streamlit and Plotly")

# ----------------- TAB 2: Unity AR Exercise Steps -----------------
with tab2:
    st.title("Unity AR Exercise: Basic 3D Object Rendering in AR")
    st.write("Follow these steps to create an AR app in Unity for rendering basic shapes (Cube, Sphere, Pyramid).")

    st.markdown("### ✅ **Prerequisites**")
    st.markdown("""
    - Unity Hub installed (**2021 LTS or later recommended**)
    - Unity Editor with **AR Foundation**, **ARCore XR Plugin**, and/or **ARKit XR Plugin**
    - A **mobile device** with AR support (Android or iOS)
    - **AR Foundation Package** (via Unity Package Manager)
    - **ARCore** for Android or **ARKit** for iOS
    """)

    st.markdown("### ✅ **Step-by-Step Implementation**")

    steps = """
    **Step 1: Create a New AR Project**
    - Open Unity Hub → New Project → 3D (URP optional).
    - Name it **BasicARShapes**.
    - Set platform to Android or iOS (**File → Build Settings → Switch Platform**).

    **Step 2: Install AR Foundation & XR Plugins**
    - Go to **Window → Package Manager**.
    - Install:
        - AR Foundation (latest)
        - ARCore XR Plugin (Android)
        - ARKit XR Plugin (iOS)
    - Enable AR support:
        - **Edit → Project Settings → XR Plug-in Management**
        - Select ARCore (Android) and/or ARKit (iOS).

    **Step 3: Setup AR Scene**
    - Delete **Main Camera**.
    - Add:
        - AR Session → **GameObject → XR → AR Session**
        - AR Session Origin → **GameObject → XR → AR Session Origin**
    - AR Camera is inside AR Session Origin.

    **Step 4: Add AR Plane Detection (Optional)**
    - In AR Session Origin, add:
        - **AR Plane Manager** (for plane detection)
        - **AR Raycast Manager** (for touch interaction)
    - Assign a **Plane Prefab** (optional).

    **Step 5: Create 3D Shapes**
    - In Hierarchy, create **empty GameObject → ShapeHolder**.
    - Add:
        - **Cube** → GameObject → 3D Object → Cube
        - **Sphere** → GameObject → 3D Object → Sphere
        - **Pyramid** → Import from Blender or FBX model
    - Scale down (e.g., 0.1, 0.1, 0.1).
    - Apply Materials (red, blue, yellow).

    **Step 6: Create AR Placement Logic**
    - For static shapes: Place them under AR Session Origin.
    - For tap placement: Use this script:

    ```csharp
    using UnityEngine;
    using UnityEngine.XR.ARFoundation;
    using UnityEngine.XR.ARSubsystems;
    using System.Collections.Generic;

    public class ARPlacement : MonoBehaviour
    {
        public GameObject cubePrefab;
        public GameObject spherePrefab;
        public GameObject pyramidPrefab;
        private ARRaycastManager raycastManager;
        private List<ARRaycastHit> hits = new List<ARRaycastHit>();

        void Start()
        {
            raycastManager = GetComponent<ARRaycastManager>();
        }

        void Update()
        {
            if (Input.touchCount > 0)
            {
                Touch touch = Input.GetTouch(0);
                if (touch.phase == TouchPhase.Began)
                {
                    if (raycastManager.Raycast(touch.position, hits, TrackableType.PlaneWithinPolygon))
                    {
                        Pose pose = hits[0].pose;
                        int randomShape = Random.Range(0, 3);
                        GameObject objToSpawn = cubePrefab;
                        if (randomShape == 1) objToSpawn = spherePrefab;
                        else if (randomShape == 2) objToSpawn = pyramidPrefab;

                        Instantiate(objToSpawn, pose.position, pose.rotation);
                    }
                }
            }
        }
    }
    ```

    - Attach script to **AR Session Origin**.
    - Assign **cubePrefab**, **spherePrefab**, **pyramidPrefab**.

    **Step 7: Configure Build Settings**
    - File → Build Settings → Player Settings:
        - Enable ARCore/ARKit support
        - Set Minimum API Level (Android: 24+)
        - Enable Camera Permission

    **Step 8: Test on Device**
    - Deploy and test on real device.

    ✅ **Output:** Shapes (cube, sphere, pyramid) render in AR with tap interaction.
    """

    st.markdown(steps)
