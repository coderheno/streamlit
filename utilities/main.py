import streamlit as st
import pandas as pd
import random

def main():
    st.title("Managing Resources for Business Analytics")
    st.markdown("### An Interactive Learning Session")

    st.sidebar.title("Navigation")
    options = [
        "Introduction", "Managing BA Personnel, Data, and Technology", 
        "Organizational Structures Aligning BA", "Managing Information Policy & Data Quality", 
        "Managing Change in BA", "Action Plan & Best Practices", "Wrap-Up & Q&A", "Lecture Notes & Case Studies", "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)

    if choice == "Introduction":
        st.header("Introduction & Icebreaker")
        st.write("\U0001F4A1 *What’s Your BA Challenge?* - Share a key challenge in managing BA resources.")
        st.text_area("Enter your challenge here:")
        
    elif choice == "Managing BA Personnel, Data, and Technology":
        st.header("Role-Play: The BA Team Challenge")
        st.write("Participants take roles (Data Analyst, IT Manager, Business Leader) and discuss resource conflicts.")
        st.markdown("**Key Discussion Points:**")
        st.write("- Aligning technical and business needs")
        st.write("- Balancing security with accessibility")
        st.write("- Budget constraints and technology investment")

    elif choice == "Organizational Structures Aligning BA":
        st.header("Case Study: Which Structure Works Best?")
        st.write("Compare centralized, decentralized, and hybrid BA models.")
        st.markdown("**Group Activity:** Discuss pros and cons of each model.")
        st.text_area("Enter your insights here:")

    elif choice == "Managing Information Policy & Data Quality":
        st.header("Hands-on Data Quality Check")
        st.write("Analyze a dataset with quality issues and propose fixes.")
        st.markdown("**Best Practices for Data Governance:**")
        st.write("- Ensuring consistency and accuracy")
        st.write("- Defining data ownership and responsibilities")
        st.write("- Implementing validation and security measures")

    elif choice == "Managing Change in BA":
        st.header("Change Resistance Simulation")
        st.write("Brainstorm reasons for resistance to BA tools and strategies to overcome it.")
        st.text_area("Enter your strategies here:")
        
    elif choice == "Action Plan & Best Practices":
        st.header("Group Brainstorm: How to Optimize BA Resources?")
        st.write("Develop a framework for effective resource management.")
        st.text_area("Enter your key takeaways here:")

    elif choice == "Wrap-Up & Q&A":
        st.header("Reflection & Key Takeaways")
        st.write("Participants share one actionable takeaway.")
        st.text_area("Enter your key learning here:")
    
    elif choice == "Lecture Notes & Case Studies":
        st.header("Lecture Notes & Case Studies")
        
        st.subheader("Managing BA Personnel, Data, and Technology")
        st.write("**Understanding Business Analytics Personnel:**")
        st.write("Business Analytics (BA) personnel include Data Analysts, Data Scientists, Business Intelligence Experts, and IT specialists.")
        st.write("Their role is to extract insights from data to drive business decisions.")
        st.write("### Example:")
        st.write("Infosys implemented a structured BA team to optimize IT service management, leading to better performance tracking and risk analysis.")
        
        st.subheader("Organizational Structures Aligning BA")
        st.write("### Understanding BA Structures:")
        st.write("Organizations can have different BA team structures:")
        st.write("- **Centralized BA:** All BA resources are controlled by a single unit.")
        st.write("- **Decentralized BA:** Each department has its own BA resources.")
        st.write("- **Hybrid BA:** A mix of centralized and decentralized structures.")
        st.write("### Case Study:")
        st.write("Flipkart adopted a hybrid BA model to balance centralized decision-making with departmental autonomy, allowing for more agile responses to market changes.")
        
        st.subheader("Managing Information Policy & Data Quality")
        st.write("### Importance of Information Policies:")
        st.write("Good data governance ensures compliance, security, and data quality.")
        st.write("Key principles include data accuracy, completeness, and reliability.")
        st.write("### Example:")
        st.write("HDFC Bank’s data governance policies ensure data integrity and regulatory compliance, preventing financial data breaches.")
        
        st.subheader("Managing Change in BA")
        st.write("### Handling Change Resistance:")
        st.write("Change management in BA requires clear communication, training, and stakeholder engagement.")
        st.write("### Case Study:")
        st.write("Tata Motors successfully transitioned to cloud-based BA despite initial resistance by implementing a phased adoption approach and employee training programs.")
    
    elif choice == "Student Activity Group Generator":
        st.header("Student Activity Group Generator")
        
        uploaded_file = st.file_uploader("Upload student list (CSV/Excel)", type=["csv", "xlsx"])
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

if __name__ == "__main__":
    main()
