import streamlit as st

st.title("Text File Reader")

# Read text file
with open("feedback.txt", "r") as file:
    content = file.read()

# Display content
st.write("File Contents:")
st.text(content)