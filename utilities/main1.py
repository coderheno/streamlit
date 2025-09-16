import streamlit as st

st.set_page_config(page_title="Intro to AR/VR Scripting", layout="wide")

st.title("🎮 Introduction to Scripting in AR/VR")

st.markdown("""
This mini app introduces scripting in AR/VR development with **hands-on activities** and **Unity code demos**.
""")

# --- Section 1: Introduction ---
st.header("1. Introduction to Scripting in AR/VR")
st.markdown("""
**Activity: Script Swap Debugging**  
- We'll start with a simple script that makes an object spin.  
- Try spotting errors or modifying values to see what changes.
""")

with st.expander("💻 Unity Code: Spinning Cube"):
    st.code(
        '''using UnityEngine;

public class SpinObject : MonoBehaviour
{
    public float rotationSpeed = 50f;

    void Update()
    {
        transform.Rotate(0, rotationSpeed * Time.deltaTime, 0);
    }
}''', language="csharp"
    )

# --- Section 2: Scripting and AR/VR Development ---
st.header("2. Scripting and AR/VR Development")
st.markdown("""
**Activity: From Pseudocode to Reality**  
Imagine: *“When I look at an object for 3 seconds, it should grow bigger.”*  
- First write pseudocode.  
- Then fill missing parts of the real Unity script.
""")

with st.expander("💻 Unity Code: Grow on Gaze (partial)"):
    st.code(
        '''using UnityEngine;

public class GrowOnGaze : MonoBehaviour
{
    public float growSpeed = 1.5f;
    private float gazeTimer = 0f;

    void Update()
    {
        // TODO: Detect gaze here (raycast or VR headset tracking)
        // If gazed at:
        // gazeTimer += Time.deltaTime;
        // if (gazeTimer >= 3f) {
        //     transform.localScale *= growSpeed;
        // }
    }
}''', language="csharp"
    )

# --- Section 3: Overview of Common Scripting Languages ---
st.header("3. Overview of Common Scripting Languages")
st.markdown("""
Different AR/VR platforms use different scripting languages:
- **C#** → Unity (most common for VR)
- **JavaScript** → WebXR / Three.js (browser-based AR/VR)
- **Python** → Blender scripting
- **Lua** → Roblox VR

**Activity: Language Match & Mini Demo**
Match the snippet to the platform!
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("C# (Unity)")
    st.code("""// Rotate object in Unity
transform.Rotate(0, 1, 0);""", language="csharp")

    st.subheader("JavaScript (WebXR)")
    st.code("""// Move object in Three.js
object.position.x += 0.1;""", language="javascript")

with col2:
    st.subheader("Python (Blender)")
    st.code("""# Print all objects in scene
import bpy
for obj in bpy.data.objects:
    print(obj.name)""", language="python")

    st.subheader("Lua (Roblox)")
    st.code("""-- Change color in Roblox
script.Parent.BrickColor = BrickColor.new("Bright red")""", language="lua")

# --- Wrap Up ---
st.header("✨ Bonus Challenge")
st.markdown("""
**Code vs No Code Challenge**:  
- Try building a bouncing ball using **Unity Visual Scripting** and again using **C# script**.  
- Compare the workflows!
""")
