import streamlit as st
st.title("Student Result Application")
name = st.text_input("Enter your name")
num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")
total = num1 + num2
st.write("Total:", total)

if name:
    st.write("Welcome", name)