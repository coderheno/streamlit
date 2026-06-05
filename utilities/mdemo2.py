import streamlit as st
import pandas as pd

st.title("Student Marks Viewer")

# Read CSV file
df = pd.read_csv("students.csv")

# Display data
st.write("Student Marks Data")
st.dataframe(df)