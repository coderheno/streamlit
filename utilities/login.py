import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet (Replace with your Google Sheet name)
sheet = client.open("BA_Responses").sheet1

def save_response_to_sheets(response):
    """Save response to Google Sheets"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sheet.append_row([timestamp, response])

def fetch_responses_from_sheets():
    """Fetch all responses from Google Sheets"""
    records = sheet.get_all_values()
    return records[1:]  # Skip header row

def main():
    st.set_page_config(page_title="Managing Resources for Business Analytics", layout="wide")
    st.title("📊 Managing Resources for Business Analytics")
    st.markdown("### 🚀 An Interactive Learning Session")

    st.sidebar.title("📌 Navigation")
    options = [
        "Introduction", "Session Breakdown & Activities", "Managing BA Personnel, Data, and Technology",
        "Organizational Structures Aligning BA", "Managing Information Policy & Data Quality",
        "Managing Change in BA", "Action Plan & Best Practices", "Wrap-Up & Q&A", "Lecture Notes & Case Studies",
        "Student Activity Group Generator"
    ]
    choice = st.sidebar.radio("Go to Section", options)
    
    tab1, tab2 = st.tabs(["Session Content", "Participant Contributions"])

    with tab1:
        if choice == "Introduction":
            st.header("🎯 Introduction & Icebreaker")
            st.write("🤣 *Funny Business Analytics Story:* Once, a data analyst spent weeks cleaning data, only to realize they had been analyzing last year’s sales instead of the current one. Always check your dataset first! 😆")
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
                fun_name = st.session_state.get("user_name", "Anonymous")
                formatted_input = f"{fun_name}: {user_input}"
                save_response_to_sheets(formatted_input)
    
        elif choice == "Session Breakdown & Activities":
            st.header("📝 Session Breakdown")
            session_data = pd.DataFrame({
                "Time": ["0-10 mins", "10-30 mins", "30-50 mins", "50-60 mins", "60-80 mins", "80-100 mins", "100-120 mins"],
                "Topic": ["Introduction & Icebreaker", "Managing BA Personnel, Data, and Technology",
                          "Organizational Structures Aligning BA", "Managing Information Policy & Data Quality",
                          "Managing Change in BA", "Action Plan & Best Practices", "Wrap-Up & Q&A"],
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
        responses = fetch_responses_from_sheets()
        
        if responses:
            for row in responses:
                st.write(f"💬 {row[0]} - {row[1]}")
        else:
            st.write("No contributions yet. Be the first to share!")

if __name__ == "__main__":
    main()
