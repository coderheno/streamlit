import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Step 1: Google Sheet URL input
sheet_url = st.text_input("Paste your Google Sheet URL")

if sheet_url:
    # Step 2: Google OAuth (Mocked Here)
    user_email = st.text_input("Continue as (Google email)")

    if user_email:
        regno = st.text_input("Enter your Register Number")

        if regno:
            # Step 3: Connect to Sheet
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
            client = gspread.authorize(creds)

            # Extract sheet ID
            sheet_id = sheet_url.split("/d/")[1].split("/")[0]
            sheet = client.open_by_key(sheet_id).sheet1

            # Step 4: Load and filter data
            data = pd.DataFrame(sheet.get_all_records())
            filtered = data[data['RegNo'] == regno]

            if not filtered.empty:
                st.write("Program-wise Marks:")
                st.dataframe(filtered)
            else:
                st.error("Register number not found.")
