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
        if choice == "Introduction":
            st.header("📌 Introduction")
            st.write("The Internet of Things (IoT) is transforming healthcare by enabling real-time data collection, remote monitoring, and predictive analytics for disease diagnosis and genetic analysis.")
            st.write("This session will explore IoT's role in genetic data collection, its applications in disease diagnosis, security challenges, and future advancements.")

        elif choice == "Session Breakdown & Activities":
            st.header("📝 Session Breakdown & Activities")
            session_data = pd.DataFrame({
                "Time": ["0-10 mins", "10-30 mins", "30-50 mins", "50-60 mins", "60-80 mins", "80-100 mins", "100-120 mins"],
                "Topic": ["Introduction", "IoT in Genetic Data Collection", "IoT Applications in Disease Diagnosis", "Security and Privacy in IoT-based Genetic Data Handling", "Challenges and Future Trends", "Case Studies & Best Practices", "Wrap-Up & Q&A"],
                "Activity": [
                    "What are your thoughts on IoT in healthcare? Participants share opinions.",
                    "Hands-on: Explore IoT devices used in genetic data collection.",
                    "Case Study Discussion: IoT-powered disease diagnosis solutions.",
                    "Identify key security risks and propose mitigation strategies.",
                    "Brainstorm future IoT trends in genetic research.",
                    "Analyze real-world IoT applications in disease prediction.",
                    "Q&A and participant reflections."
                ]
            })
            st.table(session_data)

        elif choice == "IoT in Genetic Data Collection":
            st.header("📡 IoT in Genetic Data Collection")
            st.write("IoT devices such as biosensors, wearable health monitors, and smart laboratory equipment are essential for gathering genetic data in real-time.")
            st.write("**Example:** Smart wearables measuring biomarkers for early disease detection.")

        elif choice == "IoT Applications in Disease Diagnosis":
            st.header("🩺 IoT Applications in Disease Diagnosis")
            st.write("IoT-powered healthcare solutions enable early detection and real-time monitoring of diseases through connected devices and AI-driven analysis.")
            st.write("**Example:** IoT-enabled imaging diagnostics improving cancer detection accuracy.")

        elif choice == "Security and Privacy in IoT-based Genetic Data Handling":
            st.header("🔒 Security and Privacy in IoT-based Genetic Data Handling")
            st.write("With large-scale genetic data collection comes the need for robust security measures, including encryption, blockchain, and regulatory compliance (GDPR, HIPAA).")
            st.write("**Example:** Blockchain-based storage ensuring secure genetic data transmission.")

        elif choice == "Challenges and Future Trends":
            st.header("🚀 Challenges and Future Trends")
            st.write("Despite IoT advancements, challenges like data standardization, interoperability, and cost constraints remain.")
            st.write("Future trends include AI-integrated IoT for predictive healthcare and cloud-based genetic data analysis.")

        elif choice == "Case Studies & Best Practices":
            st.header("📊 Case Studies & Best Practices")
            st.write("1. **Philips Healthcare** - Remote patient monitoring using IoT for genetic disease prediction.")
            st.write("2. **IBM Watson Genomics** - AI-driven analysis of genetic mutations for precise cancer diagnosis.")
            st.write("3. **23andMe** - IoT-integrated genetic testing kits identifying inherited traits.")

        elif choice == "Wrap-Up & Q&A":
            st.header("📝 Wrap-Up & Q&A")
            st.write("Key takeaways from the session, open discussion, and reflections on how IoT is shaping genetic research and healthcare.")

        elif choice == "Lecture Notes & Case Studies":
            st.header("📚 Lecture Notes & Case Studies")
            st.write("## Role of IoT in Genetic Data Analysis and Disease Diagnosis")
            st.write("### Key Learnings:")
            st.markdown("- IoT devices enhance genetic data collection for precision medicine.")
            st.markdown("- AI and IoT integration improves disease diagnosis and patient monitoring.")
            st.markdown("- Security risks in IoT healthcare solutions require advanced encryption and compliance measures.")
            st.markdown("- Future trends include real-time genome analysis and cloud-based predictive healthcare.")

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

