import streamlit as st

st.set_page_config(page_title="AR/VR, AI, and Emerging Tech", layout="wide")

st.title("🚀 Augmented Reality (AR) and Virtual Reality (VR)")
st.markdown("#### Presented by: Dr. Vijay Arputharaj, CHRIST (Deemed to be University), India")

# Sidebar navigation
section = st.sidebar.radio("Choose a Section", [
    "Welcome",
    "AR/VR Fundamentals",
    "VR vs AR Examples",
    "Experiential Learning Task",
    "Career Outlook"
])

if section == "Welcome": 
    st.header("👋 Welcome to the Session")
    st.markdown("""
    **Topic:** Revolutionary Technologies in Computer Science Driving the Future  
    **Source:** [CoinTelegraph Article](https://cointelegraph.com/news/10-emerging-technologies-in-computer-science-that-will-shape-the-future)
    """)

    st.markdown("---")
    st.subheader("🎥 Guess the Field of Computer Science")

    # First Guess Video - AR
    st.markdown("##### 🔍 Video 1")
    st.video("https://www.youtube.com/watch?v=miXPEPpHTwA")
    guess1 = st.text_input("Your guess for Video 1:")

    if guess1:
        if guess1.strip().lower() == "ar" or "augmented" in guess1.lower():
            st.success("✅ Correct! This is **Augmented Reality (AR)**.")
        else:
            st.error("❌ Not quite. Try again! Hint: It's AR.")

    st.markdown("---")

    # Second Guess Video - VR
    st.markdown("##### 🔍 Video 2")
    st.video("https://www.youtube.com/watch?v=SXUrzqqHZs8")
    guess2 = st.text_input("Your guess for Video 2:")

    if guess2:
        if guess2.strip().lower() == "vr" or "virtual" in guess2.lower():
            st.success("✅ Correct! This is **Virtual Reality (VR)**.")
        else:
            st.error("❌ Not quite. Try again! Hint: It's VR.")

    st.markdown("---")
    st.markdown("📘 **Creating Immersive VR Environments:**")
    st.markdown(
        "[📄 Link](https://bca304w3.streamlit.app/)", unsafe_allow_html=True )
elif section == "AR/VR Fundamentals":
    st.header("🕶️ AR and VR Fundamentals")

    st.subheader("Virtual Reality (VR)")
    st.write("""
    Virtual Reality (VR) immerses users in a fully simulated digital environment, often using head-mounted displays (HMDs). It replaces the real world with a computer-generated one, allowing users to interact within this virtual space.
    """)
    st.markdown("**🎬 Example:**")
    st.video("https://www.youtube.com/watch?v=XVLXJ8cD83I")  # Replace with a relevant VR video link

    st.subheader("Augmented Reality (AR)")
    st.write("""
    Augmented Reality (AR) overlays digital elements onto the real world, enhancing the user's perception without replacing the actual environment. AR can be experienced through smartphones, tablets, or AR glasses.
    """)
    st.markdown("**🎬 Example:**")
    st.video("https://www.youtube.com/watch?v=iXXLTctFBHE")  # Replace with a relevant AR video link

    st.markdown("---")
    st.subheader("🔍 Real-World Applications")

    st.markdown("**Healthcare:**")
    st.write("""
    - **AR in Surgery:** Surgeons use AR to overlay critical information during procedures, improving accuracy.
    - **VR in Therapy:** VR is employed for pain management and rehabilitation, providing immersive therapeutic environments.
    """)
    st.markdown("**Education:**")
    st.write("""
    - **AR in Classrooms:** Interactive AR models help students visualize complex concepts.
    - **VR Field Trips:** Students can explore historical sites or natural environments virtually.
    """)
    st.markdown("**Retail:**")
    st.write("""
    - **AR Shopping:** Customers can virtually try on clothes or see how furniture fits in their space.
    - **VR Showrooms:** Brands offer virtual showrooms for an immersive shopping experience.
    """)
    st.markdown("**Manufacturing:**")
    st.write("""
    - **AR Maintenance:** Technicians receive real-time information overlaid on machinery for efficient repairs.
    - **VR Training:** Workers are trained in virtual environments, reducing risks and costs.
    """)

    st.markdown("---")
    st.subheader("🚀 Recent Advancements")

    st.markdown("**1. Apple Vision Pro:**")
    st.write("""
    Apple's mixed reality headset combines AR and VR, offering high-resolution displays and advanced tracking for immersive experiences.
    """)
    st.markdown("**2. Meta's XR Initiatives:**")
    st.write("""
    Meta is developing XR products for various applications, including collaborations with defense sectors to enhance training and operational planning.
    """)
    st.markdown("**3. AllFocal's Nanophotonic Lens:**")
    st.write("""
    This innovative lens projects images directly onto the retina, improving clarity and reducing eye strain in AR/VR devices.
    """)
    st.markdown("**4. SenseGlove Haptic Feedback:**")
    st.write("""
    SenseGlove's wearable gloves provide tactile feedback in virtual environments, enhancing realism in VR interactions.
    """)
    st.markdown("**5. VR in Telerehabilitation:**")
    st.write("""
    VR is being used in remote rehabilitation, aiding in recovery for patients with musculoskeletal issues, stroke, and Parkinson’s disease.
    """)

elif section == "VR vs AR Examples": 
    st.header("🎮 VR Examples vs AR Examples")
    
    st.subheader("📌 VR Examples")
    st.markdown("""
    - VR places users inside a fully virtual world using a headset.
    - **Examples from Film:**  
        - *The Matrix (1999)* – Plug into a digital world  
        - *Ready Player One (2018)* – Enter the OASIS with a VR headset
    """)

    st.subheader("📌 AR Examples")
    st.markdown("""
    - AR adds digital content to the real-world view (e.g., via camera or smart glasses).
    - **Examples from Real-life & Film:**  
        - Navigation apps overlay directions on real streets  
        - *Iron Man (2008)* – Holographic overlays in Tony Stark’s lab
    """)

    st.markdown("---")
    st.subheader("🛠️ Tools Used in AR vs VR")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔧 AR Tools")
        st.markdown("""
        - ARKit (Apple)  
        - ARCore (Google)  
        - Vuforia  
        - Microsoft HoloLens  
        - Spark AR (Meta)  
        """)

    with col2:
        st.markdown("### 🔧 VR Tools")
        st.markdown("""
        - Unity 3D  
        - Unreal Engine  
        - Oculus SDK  
        - HTC Vive  
        - Google VR SDK  
        """)

    st.markdown("---")
    st.subheader("🎬 Watch: AR vs VR Explained")
    st.video("https://www.youtube.com/watch?v=IFgGzOpjlUM")
    st.markdown("*This video highlights the differences between AR and VR with real-life visuals and comparisons.*")
elif section == "Experiential Learning Task":
    st.subheader("🧪 Experiential Learning Task: Build Your First AR/VR Model")

    st.markdown("""
    ### 🎯 Objective
    Explore and identify an **emerging domain within AR or VR** based on your interest. Conduct thorough research to understand the current trends, challenges, and future scope in that domain.

    ### 🧭 Step-by-Step Instructions

    #### 1️⃣ Identify Your AR/VR Domain
    Choose a domain where AR/VR is making an impact. Some examples:
    - Medical AR/VR (e.g., surgical simulation)
    - VR in Education or Training
    - AR in Retail or Fashion
    - VR-based Fitness/Wellness
    - AR in Industrial Maintenance

    🔍 Do **extensive research**: What problems are being solved? What are the challenges? What tools are being used?

    #### 2️⃣ Select a Tool to Build a 3D Model
    Choose a tool suitable for 3D modeling and AR/VR development:
    - **Blender** (Open source 3D modeling)
    - **Unity** (Game engine, used for both AR and VR)
    - **Unreal Engine**
    - **3DS Max** (Professional 3D modeling)
    - **Tinkercad** (Simple, web-based 3D tool)

    🛠️ Install the tool, follow beginner tutorials, and get comfortable with the interface.

    #### 3️⃣ Design Your First Model
    Create a **simple 3D model** based on your chosen domain. This could be:
    - A donut 🍩
    - A car 🚗
    - A classroom
    - A wearable device
    - Any object relevant to your chosen field

    💡 Tip: Simplicity is key. Focus on **concept clarity** over technical perfection.

    #### 4️⃣ Document Your Work
    Prepare a short write-up or presentation:
    - Domain you chose and why
    - Summary of your research
    - Tool you used and why
    - Screenshots of your model
    - Challenges faced and what you learned

    #### 5️⃣ Submit or Present
    Be ready to **present your model** in class or submit it digitally for review.

    ---

    ### 🎓 Learning Outcomes
    - Research skills in AR/VR domains
    - Hands-on experience with modeling tools
    - Understanding design constraints in immersive environments
    - Communication and presentation of technical work

    ---
    📥 **Need help getting started?**  
    [Download Blender](https://www.blender.org/download/) | [Unity Hub](https://unity.com/download) | [3DS Max Trial](https://www.autodesk.com/products/3ds-max/free-trial)
    """)

elif section == "Career Outlook":
    st.header("📈 Career Outlook in India: Animation, VFX, and AR/VR")

    st.markdown("""
    The Indian Animation and AR/VR industries are experiencing significant growth, driven by advancements in technology and increasing demand across various sectors.

    ### 🎨 Animation & VFX Industry

    - **Entry-Level Salaries:** ₹3–5 LPA
    - **Mid-Level Salaries:** ₹10–15 LPA
    - **Senior-Level Salaries:** ₹20 LPA and above
    - **Average 3D Animator Salary:** ₹3.3 LPA
    - **Average Compositor Salary:** ₹3.9 LPA
    - **Average Animation Designer Salary:** ₹4.5 LPA

    *Sources: [Fundaspring](https://fundaspring.com/blogs/careers/how-to-become-an-animation-artist-in-india), [Webdew](https://careers.webdew.com/blogs/average-animator-salary-in-india/)*

    ### 🕶️ AR/VR Industry

    - **Market Size (2023):** USD 4.84 billion
    - **Projected CAGR (2024–2032):** 38.3%
    - **Key Sectors:** Education, Gaming, Healthcare, Retail
    - **Notable Companies:** Tata Elxsi, Simulanis, Merxius, Imaginate

    *Source: [UnivDatos](https://univdatos.com/reports/india-ar-vr-market)*

    ### 🏥 AR/VR in Healthcare

    - **Market Size (2024):** USD 136.2 million
    - **Projected Market Size (2030):** USD 440.2 million
    - **Projected CAGR (2025–2030):** 21.6%

    *Source: [Grand View Research](https://www.grandviewresearch.com/horizon/outlook/augmented-reality-virtual-reality-in-healthcare-market/india)*

    ### 🧠 In-Demand Skills

    - 3D Modeling & Animation (Blender, 3DS Max)
    - Game Engines (Unity, Unreal Engine)
    - AR/VR Development (ARKit, ARCore, Vuforia)
    - UI/UX Design
    - Programming (C#, C++, Python)

    *Source: [arXiv Study](https://arxiv.org/abs/2108.04946)*

    ---
    📌 **Key Takeaway:** The convergence of creative arts and technology in India is opening up diverse career paths in Animation, VFX, and AR/VR. Staying updated with the latest tools and trends is essential for success in these dynamic fields.
    """)
    st.markdown("---")
    st.subheader("📬 Contact Information")
    st.markdown("""
    **Dr. Vijay Arputharaj**  
    📱 09677188654  
    📧 [vijay.arputharaj@christuniversity.in](mailto:vijay.arputharaj@christuniversity.in)  
    🌐 [Christ University Faculty Profile](https://m.christuniversity.in/dept/faculty-details/NzAyNQ==/NjI=)
    """)
    st.markdown("""
    **Mr. Sambhav Jain**  
    📱 07878559290  
    📧 [sambhav.jain@bcah.christuniversity.in](mailto:sambhav.jain@bcah.christuniversity.in)  
    🌐 [Linkedin Profile](https://www.linkedin.com/in/sambhav-jain-8243a526a/)
    """)
    st.markdown("---")
    st.caption("For queries regarding coursework, industry sessions, or project guidance, feel free to reach out.")

