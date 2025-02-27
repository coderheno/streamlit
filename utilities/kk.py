import streamlit as st
import pandas as pd
import random
import time

def main():
    st.set_page_config(page_title="Role of IoT in Genetic Data Analysis and Disease Diagnosis", layout="wide")
    st.title("🔬 Role of IoT in Genetic Data Analysis and Disease Diagnosis")
    st.markdown("### 🚀 An Interactive Learning Session")

    st.sidebar.title("📌 Navigation")
    options = [
        "Introduction", "Session Breakdown & Activities", "IoT in Genetic Data Collection", 
        "IoT Applications in Disease Diagnosis", "Security and Privacy in IoT-based Genetic Data Handling", 
        "Challenges and Future Trends", "Case Studies & Best Practices", "Wrap-Up & Q&A", "Lecture Notes & Case Studies", "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)
    
    tab1, tab2 = st.tabs(["Session Content", "Participant Contributions"])

    if "public_responses" not in st.session_state:
        st.session_state["public_responses"] = []
    
    with tab1:
        if choice == "Lecture Notes & Case Studies":
            st.header("📚 Lecture Notes & Case Studies")
            st.write("## Role of IoT in Genetic Data Analysis and Disease Diagnosis")
            st.write("### Chapter Objectives:")
            st.markdown("- Define IoT and its significance in genetic data analysis.")
            st.markdown("- Explain how IoT facilitates disease diagnosis through real-time monitoring.")
            st.markdown("- Describe IoT-based data collection methods in healthcare.")
            st.markdown("- Discuss security and privacy concerns in IoT genetic data handling.")
            st.markdown("- Explore future trends in IoT applications for genetic research and healthcare.")
            
            st.write("### 1.1 Introduction to IoT in Healthcare")
            st.write("The Internet of Things (IoT) is revolutionizing healthcare by enabling connected devices to collect, analyze, and transmit medical data in real-time.")
            st.write("**Applications in Genetic Data Analysis:** Wearable devices and smart sensors help in monitoring genetic markers, enabling early disease detection and personalized treatment.")
            
            st.write("### 1.2 IoT in Disease Diagnosis")
            st.table(pd.DataFrame({
                "IoT Application": ["Wearable Health Monitors", "Smart Diagnostic Devices", "Cloud-based Genetic Data Processing"],
                "Function": [
                    "Continuous tracking of vital signs and genetic markers.",
                    "Automated real-time detection of diseases through IoT-enabled lab tests.",
                    "Secure and fast analysis of genetic data using cloud computing."
                ],
                "Example": [
                    "Smartwatches monitoring heart rate variability to detect genetic predispositions.",
                    "IoT-enabled blood tests identifying genetic disorders instantly.",
                    "AI-driven cloud analysis of genome sequences for early cancer detection."
                ]
            }))
            
            st.write("### 1.3 Security and Privacy Challenges")
            st.write("With increasing use of IoT in healthcare, protecting sensitive genetic data is crucial. Data encryption, secure access control, and compliance with GDPR and HIPAA are essential.")
            
            st.write("### Case Studies")
            st.markdown("**Philips Healthcare** - Implemented IoT-driven remote patient monitoring for genetic disease prediction.")
            st.markdown("**IBM Watson Genomics** - Uses AI and IoT to analyze genetic mutations for precise cancer diagnosis.")
            st.markdown("**23andMe** - IoT-integrated genetic testing kits enable users to identify inherited traits and risks.")
    
        elif choice == "Student Activity Group Generator":
            st.header("🎲 Student Activity Group Generator")
            
            uploaded_file = st.file_uploader("📂 Upload student list (CSV/Excel)", type=["csv", "xlsx"])
            num_groups = st.number_input("How many groups do you want?", min_value=2, step=1)
            
            if uploaded_file:
                df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith("xlsx") else pd.read_csv(uploaded_file)
                df = df.sample(frac=1).reset_index(drop=True)  # Shuffle students
                groups = [df.iloc[i::num_groups] for i in range(num_groups)]
                
                st.write("### Generated Groups:")
                for i, group in enumerate(groups):
                    st.write(f"#### Group {i+1}: ")
                    st.dataframe(group)
            
            if st.button("Download Group Format"):
                format_df = pd.DataFrame({"S.No": [], "Student Name": []})
                format_df.to_csv("group_format.csv", index=False)
                st.download_button(label="Download Template", data=format_df.to_csv(index=False), file_name="group_format.csv", mime="text/csv")
    
    with tab2:
        st.header("🌍 Public Contributions")
        if st.session_state["public_responses"]:
            sorted_responses = sorted(st.session_state["public_responses"], reverse=True)
            for response in sorted_responses:
                st.write(f"💬 {response}")
        else:
            st.write("No contributions yet. Be the first to share!")

if __name__ == "__main__":
    main()

