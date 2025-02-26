import streamlit as st
import pandas as pd
import random

def main():
    st.set_page_config(page_title="Managing Resources for Business Analytics", layout="wide")
    st.title("📊 Managing Resources for Business Analytics")
    st.markdown("### 🚀 An Interactive Learning Session")

    st.sidebar.title("📌 Navigation")
    options = [
        "Introduction", "Managing BA Personnel, Data, and Technology", 
        "Organizational Structures Aligning BA", "Managing Information Policy & Data Quality", 
        "Managing Change in BA", "Action Plan & Best Practices", "Wrap-Up & Q&A", "Lecture Notes & Case Studies", "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)
    
    tab1, tab2 = st.tabs(["Session Content", "Participant Contributions"])

    with tab1:
        if choice == "Introduction":
            st.header("🎯 Introduction & Icebreaker")
            st.write("💡 *What’s Your BA Challenge?* - Share a key challenge in managing BA resources.")
            user_input = st.text_area("Enter your challenge here:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)

        elif choice == "Managing BA Personnel, Data, and Technology":
            st.header("👥 Role-Play: The BA Team Challenge")
            st.subheader("Key Discussion Points:")
            st.markdown("- Aligning technical and business needs")
            st.markdown("- Balancing security with accessibility")
            st.markdown("- Budget constraints and technology investment")
            user_input = st.text_area("Your Thoughts:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)

        elif choice == "Organizational Structures Aligning BA":
            st.header("🏢 Case Study: Which Structure Works Best?")
            st.subheader("Compare centralized, decentralized, and hybrid BA models.")
            user_input = st.text_area("Your Analysis:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)

        elif choice == "Managing Information Policy & Data Quality":
            st.header("🛠️ Hands-on Data Quality Check")
            st.subheader("Best Practices for Data Governance:")
            st.markdown("- Ensuring consistency and accuracy")
            st.markdown("- Defining data ownership and responsibilities")
            st.markdown("- Implementing validation and security measures")
            user_input = st.text_area("Your Observations:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)

        elif choice == "Managing Change in BA":
            st.header("🔄 Change Resistance Simulation")
            user_input = st.text_area("Strategies to Overcome Resistance:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)

        elif choice == "Action Plan & Best Practices":
            st.header("✅ Group Brainstorm: How to Optimize BA Resources?")
            user_input = st.text_area("Your Key Takeaways:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)

        elif choice == "Wrap-Up & Q&A":
            st.header("📌 Reflection & Key Takeaways")
            user_input = st.text_area("Your Learning:")
            if st.button("Make Public"):
                st.session_state.setdefault("public_responses", []).append(user_input)
    
    with tab2:
        st.header("🌍 Public Contributions")
        if "public_responses" in st.session_state:
            for response in st.session_state["public_responses"]:
                st.write(f"💬 {response}")

    if choice == "Student Activity Group Generator":
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

if __name__ == "__main__":
    main()