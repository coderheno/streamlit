import streamlit as st

st.set_page_config(page_title="Exercise 4: Unity AR Setup", layout="wide")

st.title("🎮 Exercise 4: Getting Started with AR Development")
st.subheader("Unity3D Setup, Interface, and Basic AR Scene")
st.markdown("---")

# Step 1: Install Unity Hub
st.header("🔧 Step 1: Install Unity Hub")
st.markdown("""
To begin AR development in Unity, you need to install Unity Hub and Unity Editor (LTS version recommended):

1. Go to [Unity Download Page](https://unity.com/download)
2. Download and install **Unity Hub**
3. Inside Unity Hub, install the latest **LTS version** (e.g., Unity 2021.3.x)
4. While installing, include the following modules:
   - Android Build Support / iOS Build Support
   - OpenJDK, SDK & NDK Tools (for Android)
""")
#st.image("images/unity_hub_install.png", caption="Unity Hub Installer", use_column_width=True)

# Step 2: Create a New AR Project
st.header("📁 Step 2: Create a New AR Project")
st.markdown("""
1. Open **Unity Hub**
2. Click on **New Project**
3. Choose the **3D (URP)** template
4. Name the project: `MyFirstARProject`
5. Select a location to save it
6. Click **Create**
""")
#st.image("images/create_ar_project.png", caption="Creating a New AR Project", use_column_width=True)

# Step 3: Import AR Foundation Packages
st.header("🧩 Step 3: Import AR Foundation Packages")
st.markdown("""
To enable AR capabilities:

1. Go to **Window > Package Manager**  
2. In the top-left corner, click **+ > Add package from Git URL**  
3. Paste this:  
   ```plaintext
   https://github.com/Unity-Technologies/arfoundation-samples.git
""")

# Step 4: Unity Interface
st.header("🖥️ Step 4: Explore Unity Interface")
st.markdown("""
Familiarize yourself with the key sections of the Unity Editor:

- **Hierarchy**: Contains all game objects in the current scene  
- **Scene View**: Workspace to design your 3D/AR environment  
- **Game View**: Simulates what the camera sees  
- **Inspector**: Adjust properties of selected objects  
- **Project Panel**: Your asset folder and files
""")
#st.image("images/unity_interface.png", caption="Unity Interface Overview", use_column_width=True)

# Step 5: AR Session and Camera Setup
st.header("🧱 Step 5: Set Up AR Session and Camera")
st.markdown("""
In the **Hierarchy**, create an empty GameObject → Rename to `AR Session Origin`.

Add the following components:

- `AR Session`  
- `AR Session Origin`  
- Inside that, add an `AR Camera` and attach `AR Camera Manager` component.

Also, configure any required **layers and lighting**.
""")
#st.image("images/ar_scene_setup.png", caption="AR Camera and Session Setup", use_column_width=True)

# Step 6: Build Settings
st.header("📲 Step 6: Configure Build Settings")
st.markdown("""
To run your AR app on mobile, configure your build settings:

1. Go to **File > Build Settings**  
2. Select your platform: **Android** or **iOS**  
3. Click **Switch Platform**  
4. Open **Player Settings**:
    - Set Company Name and Product Name  
    - Under **XR Plugin Management**, enable **ARCore (Android)** or **ARKit (iOS)**
""")
#st.image("images/build_settings.png", caption="Build Settings in Unity", use_column_width=True)

# Practice Task
st.header("🧪 Practice Task")
st.markdown("""
✅ **Task**:  
- Add a **cube**, a **plane**, and your **AR camera** setup.  
- Save the scene as `scene1.unity`  
- Run it in Unity using **Play** mode.  

📸 **Upload your output screenshot below**:
""")
uploaded_file = st.file_uploader("📤 Upload Unity Scene Screenshot", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Your Uploaded Unity Output", use_column_width=True)

# Video Tutorial
st.header("🎥 Tutorial Video")
st.video("https://www.youtube.com/watch?v=GfS72wqKQ_g")  # Replace with your own tutorial if needed

# Quiz Section
st.header("📝 Self Check Quiz")
st.markdown("Test your understanding with this short quiz:")

q1 = st.radio("1️⃣ Which panel shows all game objects in your scene?",
              ["Inspector", "Game View", "Hierarchy", "Console"])
q2 = st.radio("2️⃣ Which Unity package is required for Android-based AR?",
              ["ARKit XR Plugin", "ARCore XR Plugin", "Vuforia", "URP Plugin"])
q3 = st.radio("3️⃣ What does the Inspector panel do?",
              ["Displays 3D views", "Adds audio", "Edits object properties", "Runs the game"])

if st.button("✅ Check My Answers"):
    correct = 0
    if q1 == "Hierarchy":
        correct += 1
    if q2 == "ARCore XR Plugin":
        correct += 1
    if q3 == "Edits object properties":
        correct += 1
    st.success(f"🎉 You got {correct}/3 correct!")

