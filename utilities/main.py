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
            st.write("🤣 *Funny Business Analytics Story:* Once, a data analyst spent weeks cleaning data, only to realize they had been analyzing last year’s sales instead of the current one. Moral of the story? Always check your dataset first! 😆")
            st.write("💡 *What’s Your BA Challenge?* - Share a key challenge in managing BA resources.")
            user_input = st.text_area("Enter your challenge here:")
            
            st.subheader("🌟 Name Generator")
            fav_food = st.text_input("Your Favorite Food:")
            first_name = st.text_input("Your First Name:")
            
            if st.button("Make Public"):
                fun_name = f"{fav_food} {first_name}"
                st.session_state["user_name"] = fun_name
                st.success(f"Your new fun name is: {fun_name} 🎉")
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                formatted_input = f"{timestamp} - {user_input} - ({st.session_state.get('user_name', 'Anonymous')})"
                st.session_state["public_responses"].append(formatted_input)
    
        elif choice == "Managing BA Personnel, Data, and Technology":
            st.header("👥 Role-Play: The BA Team Challenge")
            st.markdown("Participants take roles (Data Analyst, IT Manager, Business Leader) and discuss resource conflicts.")
            st.markdown("**Key Discussion Points:**")
            st.write("- Aligning technical and business needs")
            st.write("- Balancing security with accessibility")
            st.write("- Budget constraints and technology investment")
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
        if st.session_state["public_responses"]:
            sorted_responses = sorted(st.session_state["public_responses"], reverse=True)
            for response in sorted_responses:
                st.write(f"💬 {response}")
        else:
            st.write("No contributions yet. Be the first to share!")

if __name__ == "__main__":
    main()

