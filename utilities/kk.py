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
        "Introduction", "Session Breakdown & Activities", "Icebreaker & Activity", "IoT in Genetic Data Collection", 
        "IoT Applications in Disease Diagnosis", "Security and Privacy in IoT-based Genetic Data Handling", 
        "Challenges and Future Trends", "Case Studies & Best Practices", "Wrap-Up & Q&A", "Lecture Notes & Case Studies", "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)
    
    with st.container():
        if choice == "Introduction":
            st.header("📌 Introduction")
            st.title("Genomics Fun Facts: Genome Data")
            st.video("https://www.youtube.com/watch?v=ZXY0udW61uI")
            st.write("The Internet of Things (IoT) is transforming healthcare by enabling real-time data collection, remote monitoring, and predictive analytics for disease diagnosis and genetic analysis.")
            st.subheader("🔬 Sensors and Real-time Data Collection")
            st.write("IoT in genetic data analysis relies heavily on advanced **biosensors** and **wearable technology** that collect physiological and genetic markers in real-time. These sensors include:")
            st.markdown("- **Wearable Devices** (e.g., smartwatches, biosensors) that track vital signs like heart rate, blood glucose levels, and oxygen saturation.")
            st.markdown("- **Microfluidic Chips** that analyze DNA and biomarkers at a molecular level, providing immediate genetic insights.")
            st.markdown("- **Implantable Sensors** that continuously monitor genetic mutations or disease progression in high-risk patients.")
            st.markdown("- **Environmental IoT Sensors** that collect external data (air quality, exposure to harmful substances) and correlate it with genetic predispositions.")
            st.subheader("📡 Remote Monitoring and IoT in Healthcare")
            st.write("Remote monitoring allows continuous observation of patients and genetic conditions without requiring hospital visits. IoT enables this through:")
            st.markdown("- **Cloud-based Health Dashboards** that store and analyze genetic data, accessible to doctors and researchers globally.")
            st.markdown("- **Connected Wearables** that transmit real-time health updates to medical professionals, enabling **early detection of anomalies**.")
            st.markdown("- **Telemedicine Integration** where IoT devices communicate patient vitals and genetic risks directly to doctors, facilitating quick decisions.")
            st.markdown("- **AI-powered Alerts** that notify healthcare providers of critical genetic markers or disease progression.")
            st.subheader("📊 Predictive Analytics in Genetic Data")
            st.write("Predictive analytics uses IoT-generated data to **forecast disease risks and progression**, improving preventive care. Key aspects include:")
            st.markdown("- **Machine Learning Models** trained on genetic and health data to predict conditions like cancer, diabetes, or hereditary disorders.")
            st.markdown("- **Pattern Recognition Algorithms** that identify early symptoms of genetic diseases before physical symptoms appear.")
            st.markdown("- **Big Data Analysis** that combines genetic information, lifestyle habits, and environmental factors to personalize treatment plans.")
            st.markdown("- **Automated Risk Scores** where AI assigns a probability to a patient developing a disease based on IoT-collected genetic and biometric data.")
    
            st.write("This session will explore IoT's role in genetic data collection, its applications in disease diagnosis, security challenges, and future advancements in detail.")

        elif choice == "Session Breakdown & Activities":
            st.header("📝 Session Breakdown & Activities")
            session_data = pd.DataFrame({
                "Time": ["0-10 mins", "10-30 mins", "30-50 mins", "50-60 mins", "60-80 mins", "80-100 mins", "100-120 mins"],
                "Topic": ["Introduction", "Icebreaker & Activity", "IoT in Genetic Data Collection", "IoT Applications in Disease Diagnosis", "Security and Privacy in IoT-based Genetic Data Handling", "Challenges and Future Trends", "Case Studies & Best Practices"],
                "Activity": [
                    "What are your thoughts on IoT in healthcare? Participants share opinions.",
                    "Interactive Icebreaker: ‘Decode Your DNA’ & ‘IoT Lab Challenge’.",
                    "Hands-on: Explore IoT devices used in genetic data collection.",
                    "Case Study Discussion: IoT-powered disease diagnosis solutions.",
                    "Identify key security risks and propose mitigation strategies.",
                    "Brainstorm future IoT trends in genetic research.",
                    "Analyze real-world IoT applications in disease prediction."
                ]
            })
            st.table(session_data)

        elif choice == "Icebreaker & Activity":
            st.header("🎉 Icebreaker: Decode Your DNA")
            st.write("Get ready to explore the world of IoT in genetic data with a fun and interactive icebreaker!")
            
            st.write("### Step 1: Your Futuristic Health IoT Device")
            user_input = st.text_area("Describe your futuristic IoT device:")
            
            st.write("### Step 2: Generate Your DNA Code Name")
            fav_food = st.text_input("Your Favorite Food:")
            first_name = st.text_input("Your First Name:")
            
            if st.button("Generate Code Name"):
                fun_name = f"{fav_food} {first_name}"
                st.success(f"Your DNA Code Name is: {fun_name} 🧬")

            st.write("### 🔬 Main Activity: IoT Lab Challenge")
            st.write("**Your Challenge:** Form teams and create a concept for an IoT-powered system that detects genetic diseases.")
            st.markdown("**Your project must include:**")
            st.markdown("- **Device Name**")
            st.markdown("- **What Data it Collects** (e.g., DNA markers, protein levels, vital signs)")
            st.markdown("- **How IoT is Used** (sensors, cloud storage, real-time monitoring)")
            st.markdown("- **Privacy & Security Features** (How will they protect genetic data?)")
            st.markdown("- **Predictive Analysis** (How will the device warn patients about risks?)")
            
            st.write("Teams will present their ideas in **3 minutes**, and the audience will vote for the most innovative idea!")

        elif choice == "IoT in Genetic Data Collection":
            st.header("📡 IoT in Genetic Data Collection")
            st.write("IoT devices such as biosensors, wearable health monitors, and smart laboratory equipment are essential for gathering genetic data in real-time.")

        elif choice == "IoT Applications in Disease Diagnosis":
            st.header("🩺 IoT Applications in Disease Diagnosis")
            st.write("IoT-powered healthcare solutions enable early detection and real-time monitoring of diseases through connected devices and AI-driven analysis.")

        elif choice == "Security and Privacy in IoT-based Genetic Data Handling":
            st.header("🔒 Security and Privacy in IoT-based Genetic Data Handling")
            st.write("With large-scale genetic data collection comes the need for robust security measures, including encryption, blockchain, and regulatory compliance (GDPR, HIPAA).")

        elif choice == "Challenges and Future Trends":
            st.header("🚀 Challenges and Future Trends")
            st.write("Despite IoT advancements, challenges like data standardization, interoperability, and cost constraints remain.")

        elif choice == "Case Studies & Best Practices":
            st.header("📊 Case Studies & Best Practices")
            st.write("**Philips Healthcare** - Remote patient monitoring using IoT for genetic disease prediction.")
            st.write("**IBM Watson Genomics** - AI-driven analysis of genetic mutations for precise cancer diagnosis.")

        elif choice == "Wrap-Up & Q&A":
            st.header("📝 Wrap-Up & Q&A")
            st.write("Key takeaways from the session, open discussion, and reflections on how IoT is shaping genetic research and healthcare.")
        elif choice == "Lecture Notes & Case Studies":
            st.title("Watch This Video on IoT in Genetic Data Analysis!")
            st.video("https://www.youtube.com/watch?v=Q3RMS1OWKwY")

if __name__ == "__main__":
    main()

