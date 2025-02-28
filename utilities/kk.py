import streamlit as st
import pandas as pd
import random
import time

def iot_healthcare_solutions():
    """Streamlit function to display IoT-powered healthcare solutions."""
    
    st.title("🚑 IoT-Powered Healthcare Solutions")
    st.subheader("🔬 Transforming Early Detection & Real-Time Monitoring")

    st.write("""
    IoT (Internet of Things) devices, combined with AI-driven analysis, are revolutionizing healthcare by enabling 
    **early disease detection** and **real-time patient monitoring**. These solutions enhance **diagnostic accuracy**, 
    **remote healthcare**, and **personalized treatment**, reducing hospital visits and improving patient outcomes.
    """)

    # Section: How IoT Enhances Healthcare
    st.header("📡 How IoT Enhances Healthcare?")
    st.markdown("""
    - **Continuous Monitoring** – Tracks vitals like heart rate, blood pressure, oxygen levels, glucose, and ECG.
    - **AI-Powered Analytics** – Detects abnormalities and predicts potential health risks.
    - **Automated Alerts** – Notifies doctors, caregivers, or emergency services in case of critical changes.
    """)

    # Section: Key Applications
    st.header("🚀 Key Applications of IoT in Healthcare")

    with st.expander("1️⃣ Early Disease Detection"):
        st.write("""
        IoT devices detect diseases at an early stage by analyzing real-time biometric data patterns.
        **Examples:**
        - AI-powered ECG monitors detect irregular heart rhythms.
        - Continuous Glucose Monitors (CGMs) predict early diabetes risks.
        - Wearable Skin Patches detect hydration levels and electrolyte imbalance.
        """)

    with st.expander("2️⃣ Real-Time Patient Monitoring & Telehealth"):
        st.write("""
        Remote patient monitoring allows doctors to track patients' health from anywhere, reducing hospital readmissions.
        **Examples:**
        - Smartwatches & fitness bands track heart rate, SpO2, and sleep patterns.
        - IoT-enabled blood pressure monitors send real-time data to healthcare providers.
        - Smart Insulin Pens track glucose levels and adjust insulin dosage.
        """)

    with st.expander("3️⃣ AI-Driven Diagnostics & Predictive Analytics"):
        st.write("""
        AI enhances IoT-driven healthcare by analyzing large datasets to identify disease trends.
        **Examples:**
        - AI-based MRI & CT scan analysis improves cancer detection rates.
        - Neural networks in biosensors detect early Alzheimer’s & Parkinson’s symptoms.
        - AI-powered voice analysis predicts neurological disorders like ALS and depression.
        """)

    with st.expander("4️⃣ Smart Implants & Bio-Sensors"):
        st.write("""
        Smart implants and bio-sensors improve chronic disease management by delivering real-time feedback to healthcare professionals.
        **Examples:**
        - Cardiac pacemakers track heart activity and send data to cardiologists.
        - Smart contact lenses monitor intraocular pressure for glaucoma patients.
        - Bio-ingestible sensors track gut health and medication adherence.
        """)

    with st.expander("5️⃣ IoT in Hospitals & Emergency Care"):
        st.write("""
        IoT helps hospitals improve efficiency with smart beds, automated medication dispensers, and real-time tracking of medical assets.
        **Examples:**
        - Smart hospital beds adjust patient position to prevent bedsores.
        - IoT-enabled ambulance tracking optimizes emergency response.
        - Connected drug dispensers ensure accurate medication dosage and adherence.
        """)

    # Section: Advantages of IoT in Healthcare
    st.header("✅ Advantages of IoT-Powered Healthcare")
    st.markdown("""
    - **Early Diagnosis** – AI-driven insights detect diseases **before symptoms appear**.
    - **24/7 Monitoring** – Patients are continuously tracked **outside hospitals**.
    - **Reduced Hospital Visits** – Remote monitoring minimizes **unnecessary check-ups**.
    - **Personalized Healthcare** – Tailored treatment plans based on real-time patient data.
    - **Cost-Effective** – Saves **healthcare costs** by preventing severe complications.
    """)

    # Section: Future of IoT in Healthcare
    st.header("🌍 Future of IoT in Healthcare")
    st.markdown("""
    - **5G Integration** – Faster real-time health data transmission.
    - **Blockchain for Medical Data Security** – Ensures **tamper-proof patient records**.
    - **AI-Enabled Virtual Health Assistants** – AI-powered chatbots for **24/7 health guidance**.
    - **Brain-Computer Interfaces (BCI)** – IoT implants for neurological disorder treatment.
    """)

    # Conclusion
    st.success("IoT-powered healthcare solutions are revolutionizing medicine with real-time disease detection, continuous monitoring, and AI-driven analytics. These technologies empower patients, improve treatment accuracy, and pave the way for a smarter, proactive healthcare system.")

  

def iot_genetic_data():
    st.subheader("🔬 IoT Devices for Real-Time Genetic Data Collection")

    st.write("""
    IoT devices play a crucial role in **genetic research and healthcare** by enabling **real-time data collection, analysis, and monitoring**.
    Below are three major categories of IoT devices used in genetic studies:
    """)

    option = st.radio("Select a category:", ["Biosensors", "Wearable Health Monitors", "Smart Laboratory Equipment"])

    if option == "Biosensors":
        st.subheader("🧪 Biosensors")
        st.write("""
        **Biosensors** detect and analyze biological molecules such as DNA, RNA, and proteins.  
        They convert biological responses into measurable signals for real-time genetic analysis.
        """)

        st.markdown("### 🔹 Examples:")
        st.write("- **DNA Sequencing Biosensors** for detecting genetic mutations.")
        st.write("- **Glucose Biosensors** used in genetic predisposition studies.")
        st.write("- **Microfluidic Biosensors** for rapid genetic screening.")

        st.markdown("### ✅ Advantages:")
        st.write("✔ High sensitivity & specificity")
        st.write("✔ Rapid real-time analysis")
        st.write("✔ Portable & suitable for field use")

    elif option == "Wearable Health Monitors":
        st.subheader("⌚ Wearable Health Monitors")
        st.write("""
        **Wearable devices** track real-time physiological and genetic markers,  
        helping in personalized medicine and disease prevention.
        """)

        st.markdown("### 🔹 Examples:")
        st.write("- **Smartwatches** track heart rate & genetic health analysis.")
        st.write("- **Electrodermal Sensors** detect stress-related genetic markers.")
        st.write("- **Smart Contact Lenses** analyze tear fluid for genetic disorders.")

        st.markdown("### ✅ Advantages:")
        st.write("✔ Continuous & real-time health tracking")
        st.write("✔ Non-invasive & user-friendly")
        st.write("✔ AI-powered predictive analytics")

    elif option == "Smart Laboratory Equipment":
        st.subheader("🧬 Smart Laboratory Equipment")
        st.write("""
        **IoT-enabled lab devices** automate genetic sequencing and analysis,  
        improving accuracy and scalability in genetic research.
        """)

        st.markdown("### 🔹 Examples:")
        st.write("- **Automated DNA Sequencers** allow remote genome sequencing.")
        st.write("- **Smart PCR Machines** optimize genetic amplification & analysis.")
        st.write("- **Hyperspectral Imaging Sensors** detect genetic anomalies.")

        st.markdown("### ✅ Advantages:")
        st.write("✔ Reduces human error with automation")
        st.write("✔ Remote monitoring & real-time analysis")
        st.write("✔ High-throughput sequencing capabilities")

    st.info("IoT in genetic research enables **faster detection, personalized medicine, and remote genetic monitoring**. 🌍💡")


    
def main():
    st.set_page_config(page_title="Role of IoT in Genetic Data Analysis and Disease Diagnosis", layout="wide")
    st.title("🔬 Role of IoT in Genetic Data Analysis and Disease Diagnosis")
    

    st.sidebar.title("📌 Navigation")
    options = [
        "Introduction", "Session Breakdown & Activities", "Icebreaker & Activity", "IoT in Genetic Data Collection", 
        "IoT Applications in Disease Diagnosis", "Security and Privacy in Genetic Data Handling", 
        "Challenges and Future Trends", "Case Studies & Best Practices", "Wrap-Up & Q&A", "Lecture Notes & Case Studies", "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)
    
    with st.container():
        if choice == "Introduction":
            st.header("📌 Introduction")
            st.subheader("Genomics Fun Facts: Genome Data")
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
            iot_genetic_data()

        elif choice == "IoT Applications in Disease Diagnosis":
            st.header("🩺 IoT Applications in Disease Diagnosis")
            st.write("IoT-powered healthcare solutions enable early detection and real-time monitoring of diseases through connected devices and AI-driven analysis.")
            iot_healthcare_solutions()
        elif choice == "Security and Privacy in Genetic Data Handling":
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
            st.header("📌 Wrap-Up & Q&A")
            st.write("Students should Summarize the key takeaways and opening the floor for questions and discussions.")
        
        elif choice == "Lecture Notes & Case Studies":
            st.subheader("Watch This Video on IoT in Genetic Data Analysis!")
            st.video("https://www.youtube.com/watch?v=Q3RMS1OWKwY")
            st.subheader("🚀 Why Include Python and Streamlit in Genetic Data Analysis?")
            st.write("""
            Python is one of the most widely used languages in GDA due to its extensive libraries:
            - **Data Cleaning & Preprocessing** (Pandas, NumPy)
            - **Statistical Analysis & Hypothesis Testing** (Statsmodels)
            - **Machine Learning & Predictive Analytics** (Scikit-learn, TensorFlow)
            - **Data Visualization** (Matplotlib, Seaborn)
            - **Automation of Repetitive Tasks** (Scripting & APIs)
            
            Streamlit is an open-source framework that helps create interactive Genomic models quickly:
            - **Rapid Deployment** of dashboards
            - **Interactive Visualizations** for real-time decision-making
            - **Seamless ML Integration** for predictive analytics
            """)

            st.subheader("📊 List of GDA Analytics Tools")
            data = {
                "Category": [
                    "Spreadsheet-Based Tools", "Statistical & Predictive Analytics",
                    "Data Mining & Machine Learning", "Data Visualization",
                    "Big Data & Cloud Analytics", "Programming & Development"
                ],
                "Tools": [
                    "MS Excel, Google Sheets",
                    "SPSS, SAS, R, MATLAB, Stata, Salford Systems",
                    "Python (Pandas, Scikit-learn, TensorFlow), KXEN, RapidMiner",
                    "Tableau, Power BI, Streamlit, Python (Matplotlib, Seaborn)",
                    "Apache Spark, Google BigQuery, AWS SageMaker",
                    "Python, R, SQL, Julia"
                ]
            }
            df = pd.DataFrame(data)
            st.table(df)

        elif choice == "Student Activity Group Generator":
            st.markdown("[Visit CIT 2024 App](https://cit2024.streamlit.app)")
if __name__ == "__main__":
    main()

