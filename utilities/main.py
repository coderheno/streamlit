import streamlit as st
import pandas as pd
import random
import time

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
        elif choice == "Lecture Notes & Case Studies":
            st.header("📚 Lecture Notes & Case Studies")
            st.write("### Managing BA Personnel, Data, and Technology")
            st.write("Business Analytics personnel include Data Analysts, Data Scientists, Business Intelligence Experts, and IT specialists who extract insights from data to drive business decisions.")
            st.write("**Case Study:** Infosys implemented a structured BA team to optimize IT service management.")
        
            st.write("### Organizational Structures Aligning BA")
            st.write("Organizations can have different BA team structures: Centralized, Decentralized, and Hybrid.")
            st.write("**Case Study:** Flipkart adopted a hybrid BA model to balance centralized decision-making with departmental autonomy.")
        
            st.write("### Managing Information Policy & Data Quality")
            st.write("Good data governance ensures compliance, security, and data quality.")
            st.write("**Case Study:** HDFC Bank’s data governance policies ensure data integrity and regulatory compliance.")
        
            st.write("### Managing Change in BA")
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
        st.header("🌍 Public Contributions")
        if st.session_state["public_responses"]:
            sorted_responses = sorted(st.session_state["public_responses"], reverse=True)
            for response in sorted_responses:
                st.write(f"💬 {response}")
        else:
            st.write("No contributions yet. Be the first to share!")
            

if __name__ == "__main__":
    main()

