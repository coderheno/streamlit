import pandas as pd 
import streamlit as st 

user_data = pd.read_csv(r'C:\Users\N.NAGESH\Documents\GitHub\streamlit\users.csv')

st.set_page_config(page_title="Login Authentication", page_icon="🔒")
st.sidebar.title("Login")


username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")


st.title("Welcome to the Streamlit App with Login Authentication")
st.write("This is the main content of your app.")



if st.sidebar.button("Login"):
    if username in user_data["Username"].values and password in user_data.loc[
        user_data["Username"] == username, "Password"
    ].values:
        st.sidebar.success("Logged in as {}".format(username))
    else:
        st.sidebar.error("Invalid username or password")
