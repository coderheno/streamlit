import streamlit as st
import pandas as pd
import random
import time
import streamlit as st
import pandas as pd

def business_analytics_app():
    st.set_page_config(page_title="Business Analytics Course", layout="wide")

    # Sidebar Navigation
    st.sidebar.title("📌 Navigation")
    options = [
        "Introduction", "Session Breakdown & Activities", "Managing BA Personnel, Data, and Technology", 
        "Organizational Structures Aligning BA", "Managing Information Policy & Data Quality", 
        "Managing Change in BA", "Action Plan & Best Practices", "Wrap-Up & Q&A", 
        "Lecture Notes & Case Studies", "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)

    # Main Title
    st.title("📊 Business Analytics Course")

    # Define Tabs
    tab1, tab2 = st.tabs(["Session Content", "Participant Contributions"])

    # Tab 1: Session Content
    with tab1:
        st.subheader("Comparison of Business Analytics Tools")
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
                "Python, R, Julia, SQL"
            ]
        }
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

        st.subheader("Why Use Python & Streamlit in Business Analytics?")
        advantages = [
            "✅ **Open-source & Cost-effective** – Unlike commercial tools like SAS and SPSS, Python & Streamlit are free.",
            "✅ **Scalability** – Python can handle large datasets efficiently, making it superior to Excel.",
            "✅ **Real-time Analytics** – Streamlit enables interactive dashboards for decision-making.",
            "✅ **AI/ML Integration** – Python supports ML models, difficult to implement in Excel."
        ]
        for adv in advantages:
            st.markdown(adv)

    # Tab 2: Participant Contributions (Public Responses)
    with tab2:
        st.subheader("📝 Share Your Insights")
        if "public_responses" not in st.session_state:
            st.session_state["public_responses"] = []

        response = st.text_area("Enter your thoughts or questions:", key="user_response")
        if st.button("Submit Response"):
            if response:
                st.session_state["public_responses"].append(response)
                st.success("✅ Response recorded!")
        
        if st.session_state["public_responses"]:
            st.write("### 🔍 Public Responses")
            for i, res in enumerate(st.session_state["public_responses"], 1):
                st.write(f"**{i}.** {res}")


    
def main():
    st.set_page_config(page_title="Managing Resources for Business Analytics", layout="wide")
    st.title("📊 Managing Resources for Business Analytics")
    st.markdown("### 🚀 An Interactive Learning Session")

    st.sidebar.title("📌 Navigation")
    options = [
        "Introduction", "Session Breakdown & Activities", "Managing BA Personnel, Data, and Technology", 
        "Organizational Structures Aligning BA", "Managing Information Policy & Data Quality", 
        "Managing Change in BA", "Action Plan & Best Practices", "Wrap-Up & Q&A", "Lecture Notes & Case Studies", "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)
    
    tab1, tab2 = st.tabs(["Session Content", "Participant Contributions"])

    if "public_responses" not in st.session_state:
        st.session_state["public_responses"] = []
    
    with tab1:
        if choice == "Introduction":
            st.header("🎯 Introduction & Icebreaker")
            st.write("💡 *What’s Your BA Challenge?* - Share a key challenge in managing BA resources.")
            user_input = st.text_area("Enter your challenge here:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
    
        elif choice == "Session Breakdown & Activities":
            st.header("📝 Session Breakdown")
            session_data = pd.DataFrame({
                "Time": ["0-10 mins", "10-30 mins", "30-50 mins", "50-60 mins", "60-80 mins", "80-100 mins", "100-120 mins"],
                "Topic": ["Introduction & Icebreaker", "Managing BA Personnel, Data, and Technology", "Organizational Structures Aligning BA", "Managing Information Policy & Data Quality", "Managing Change in BA", "Action Plan & Best Practices", "Wrap-Up & Q&A"],
                "Activity": [ 
                    "'What’s Your BA Challenge?' - Participants share a key challenge in managing BA resources.",
                    "Role-Play: 'The BA Team Challenge' – Assign roles (Analyst, IT, Data Engineer) and discuss resource conflicts.",
                    "Case Study: Compare centralized vs decentralized BA teams & their impact.",
                    "Hands-on: Participants analyze a dataset with quality issues & propose fixes.",
                    "'Change Resistance Simulation' – Small groups strategize on overcoming resistance to a new BA tool.",
                    "Group Brainstorm: 'How to Optimize BA Resources?' - Teams present solutions.",
                    "Reflection: What’s one key takeaway? Share & discuss."
                ]
            })
            st.table(session_data)
    
        elif choice == "Managing BA Personnel, Data, and Technology":
            st.header("👥 Role-Play: The BA Team Challenge")
            st.write("Participants take roles (Data Analyst, IT Manager, Business Leader) and discuss resource conflicts.")
            user_input = st.text_area("Your Thoughts:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
    
        elif choice == "Organizational Structures Aligning BA":
            st.header("🏢 Case Study: Which Structure Works Best?")
            st.write("Compare centralized, decentralized, and hybrid BA models.")
            user_input = st.text_area("Your Analysis:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
    
        elif choice == "Managing Information Policy & Data Quality":
            st.header("🛠️ Hands-on Data Quality Check")
            st.write("Analyze a dataset with quality issues and propose fixes.")
            user_input = st.text_area("Your Observations:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
    
        elif choice == "Managing Change in BA":
            st.header("🔄 Change Resistance Simulation")
            st.write("Brainstorm reasons for resistance to BA tools and strategies to overcome it.")
            user_input = st.text_area("Your Strategies:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
    
        elif choice == "Action Plan & Best Practices":
            st.header("✅ Group Brainstorm: How to Optimize BA Resources?")
            st.write("Teams develop a framework for effective resource management and share best practices.")
            user_input = st.text_area("Enter your key takeaways:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
    
        elif choice == "Wrap-Up & Q&A":
            st.header("📌 Reflection & Key Takeaways")
            st.write("Participants summarize what they learned and ask final questions.")
            user_input = st.text_area("Share your key learning:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
            with tab2:
                st.header("🌍 Public Contributions")
                if st.session_state["public_responses"]:
                    sorted_responses = sorted(st.session_state["public_responses"], reverse=True)
                    for response in sorted_responses:
                        st.write(f"💬 {response}")
                else:
                    st.write("No contributions yet. Be the first to share!")
        elif choice == "Lecture Notes & Case Studies":
            st.header("📚 Lecture Notes & Case Studies")
            
            st.write("## What Are Business Analytics and Managing Resources?")
            st.write("### Learning Objectives:")
            st.markdown("- Define business analytics.")
            st.markdown("- Explain the relationship of analytics and business intelligence to business analytics.")
            st.markdown("- Describe the three steps of the business analytics process.")
            st.markdown("- Describe four data classification measurement scales.")
            st.markdown("- Explain the relationship of the business analytics process with the organization decision-making process.")
            st.markdown("- Manage the resources of the business analytics process with managing information policy, data quality and change in BA.")
            st.write("### 1.1 Terminologies")
            st.write("Business analytics begins with data sets or databases that store information. As these grow, technologies like cloud computing and data warehousing store and manage this information efficiently.")
            st.write("**Big Data vs. Little Data:** Big data refers to vast and complex data sets, while little data focuses on smaller, business-specific insights.")
        
            st.write("### 1.2 Types of Analytics")
            st.table(pd.DataFrame({
            "Type of Analytics": ["Desc", "Pred", "Pres"],
            "Definition": [
                "Describes what is contained in a data set using basic statistical methods.",
                "Uses advanced statistical, software, or operations research methods to identify patterns and make forecasts.",
                "Uses decision science techniques to determine optimal actions and resource allocation."
            ],
            "Example": [
                "A bar chart of customer ages to target advertisements.",
                "A regression model predicting how age, weight, and exercise impact diet food sales.",
                "An optimization model allocating a department store’s advertising budget optimally."
            ]
            }))
        
            st.write("### 1.3 Business Analytics Process")
            st.write("Business analytics follows a sequential process:")
            st.markdown("1. **Descriptive Analytics** - Identifies past trends and summarizes data.")
            st.markdown("2. **Predictive Analytics** - Uses historical data to predict future trends.")
            st.markdown("3. **Prescriptive Analytics** - Uses models to determine the best possible decisions.")
        
            st.write("### 1.4 Relationship Between BA & Decision-Making")
            st.write("Business analytics supports organizational decision-making by providing data-driven insights, helping businesses identify opportunities and allocate resources efficiently.")
        
            st.write("### Case Studies")
            st.markdown("**Infosys** - Implemented structured BA to optimize IT service management.")
            st.markdown("**Flipkart** - Used hybrid BA models for decision-making efficiency.")
            st.markdown("**HDFC Bank** - Leveraged BA for data governance and regulatory compliance.")
            st.markdown("**Tata Motors** - Successfully transitioned to cloud-based BA with minimal disruption.")

            st.write("### 2.1. Managing BA Personnel, Data, and Technology")
            st.write("Business Analytics personnel include Data Analysts, Data Scientists, Business Intelligence Experts, and IT specialists who extract insights from data to drive business decisions.")
            st.write("**Case Study:** Infosys implemented a structured BA team to optimize IT service management.")
        
            st.write("### 2.2. Organizational Structures Aligning BA")
            st.write("Organizations can have different BA team structures: Centralized, Decentralized, and Hybrid.")
            st.write("**Case Study:** Flipkart adopted a hybrid BA model to balance centralized decision-making with departmental autonomy.")
        
            st.write("### 2.3. Managing Information Policy & Data Quality")
            st.write("Good data governance ensures compliance, security, and data quality.")
            st.write("**Case Study:** HDFC Bank’s data governance policies ensure data integrity and regulatory compliance.")
        
            st.write("### 2.4. Managing Change in BA")
            st.write("Change management in BA requires clear communication, training, and stakeholder engagement.")
            st.write("**Case Study:** Tata Motors successfully transitioned to cloud-based BA despite initial resistance.")

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
               

        st.title("🚀 Why Include Python and Streamlit in Business Analytics?")
    
        # Introduction
        st.subheader("Why Include Python and Streamlit?")
        st.write("""
    Python is one of the most widely used languages in business analytics due to its extensive libraries:
    - **Data Cleaning & Preprocessing** (Pandas, NumPy)
    - **Statistical Analysis & Hypothesis Testing** (Statsmodels)
    - **Machine Learning & Predictive Analytics** (Scikit-learn, TensorFlow)
    - **Data Visualization** (Matplotlib, Seaborn)
    - **Automation of Repetitive Tasks** (Scripting & APIs)
    
    Streamlit is an open-source framework that helps create interactive business applications quickly:
    - **Rapid Deployment** of business dashboards
    - **Interactive Visualizations** for real-time decision-making
    - **Seamless ML Integration** for predictive analytics
    """)

     # Business Analytics Tools Table
        st.subheader("📊 List of Business Analytics Tools")
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
            "Python, R, Julia, SQL"
        ]
    }
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    # Advantages of Python & Streamlit
        st.subheader("🚀 Advantages of Python and Streamlit in Business Analytics")
    advantages = [
        "✅ **Open-source & Cost-effective** – Unlike SAS & SPSS, Python & Streamlit are free.",
        "✅ **Scalability** – Python efficiently handles large datasets, unlike Excel.",
        "✅ **Real-time Analytics** – Streamlit enables interactive dashboards for business insights.",
        "✅ **AI/ML Integration** – Python supports ML models, unlike traditional tools."
    ]
    for adv in advantages:
        st.markdown(adv)

    # Optional Comparison Table Prompt
    st.write("Would you like a **comparison table** showing how Python and Streamlit compare to traditional tools? 🚀")
    if st.button("Generate Comparison"):
        comparison_data = {
            "Feature": ["Cost", "Scalability", "AI/ML Support", "Real-Time Dashboards", "Ease of Use"],
            "Python & Streamlit": ["Free & Open Source", "High", "Yes", "Yes", "User-friendly"],
            "Traditional Tools (Excel, SPSS, SAS)": ["Paid", "Limited", "Limited", "No", "Requires Training"]
        }
        comparison_df = pd.DataFrame(comparison_data)
        st.table(comparison_df)



if __name__ == "__main__":
    main()
   
