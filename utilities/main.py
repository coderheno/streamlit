import streamlit as st
import pandas as pd
import random

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

    with tab1:
        if choice == "Introduction":
            st.header("🎯 Introduction & Icebreaker")
            st.write("🤣 *Funny Business Analytics Story:* Once, a data analyst spent weeks cleaning data, only to realize they had been analyzing last year’s sales instead of the current one. Moral of the story? Always check your dataset first! 😆")
            st.write("💡 *What’s Your BA Challenge?* - Share a key challenge in managing BA resources.")
            user_input = st.text_area("Enter your challenge here:")
            st.subheader("🌟 Fun Name Generator")
            fav_food = st.text_input("Your Favorite Food:")
            first_name = st.text_input("Your First Name:")
            if st.button("Generate Fun Name"):
                fun_name = f"{fav_food} {first_name}"
                st.session_state["user_name"] = fun_name
                st.success(f"Your new fun name is: {fun_name} 🎉")
            if st.button("Make Public"):
                formatted_input = f"{user_input} - ({st.session_state.get('user_name', 'Anonymous')})"
                st.session_state.setdefault("public_responses", []).append(formatted_input)
            
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
    
    with tab2:
        st.header("🌍 Public Contributions")
        if "public_responses" in st.session_state:
            for response in st.session_state["public_responses"]:
                st.write(f"💬 {response}")

if __name__ == "__main__":
    main()
