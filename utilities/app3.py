import streamlit as st
import pandas as pd
import random

# Function to display the input form for teachers to enter their details
def display_teacher_form():
    st.write("## Welcome Teachers! Please Enter Your Details Below:")
    name = st.text_input("Name:")
    favorite_food = st.text_input("Favorite Food:")
    favorite_pet = st.text_input("Favorite Pet:")
    favorite_color = st.text_input("Favorite Color:")
    date_of_birth = st.date_input("Date of Birth:")
    teacher_image = st.file_uploader("Upload Your Picture:")
    teacher_signature = st.file_uploader("Upload Your Signature:")
    submit_button = st.button("Submit")

    if submit_button:
        return {
            "Name": name,
            "Favorite Food": favorite_food,
            "Favorite Pet": favorite_pet,
            "Favorite Color": favorite_color,
            "Date of Birth": date_of_birth,
            "Teacher Image": teacher_image,
            "Teacher Signature": teacher_signature
        }

# Function to generate unique combinations for the autograph
def generate_autograph(data):
    name = data["Name"]
    favorite_food = data["Favorite Food"]
    favorite_pet = data["Favorite Pet"]
    favorite_color = data["Favorite Color"]
    return f"{name} also known as {favorite_food} {favorite_pet} and loves {favorite_color}"

# Function to display the report with autographs
def display_report(teachers_data):
    st.write("## Farewell Autograph Report")
    st.write("Here are the autographs and fun combinations of the teachers:")
    st.write("```\n")
    for teacher_data in teachers_data:
        autograph = generate_autograph(teacher_data)
        st.write(autograph)
    st.write("```")

def main():
    st.title("Farewell Autograph App")

    # Load existing data or create new dataframe
    try:
        df = pd.read_csv("teachers_data.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Favorite Food", "Favorite Pet", "Favorite Color", "Date of Birth"])

    # Display teacher form and collect details
    teacher_data = display_teacher_form()
    if teacher_data:
        df = df.append(teacher_data, ignore_index=True)
        df.to_csv("teachers_data.csv", index=False)

    # Display report with autographs
    display_report(df.to_dict("records"))

if __name__ == "__main__":
    main()
