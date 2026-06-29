import streamlit as st
import joblib

st.title("Health Risk Predictor")

# Load pre-trained model
model = joblib.load("health_model.pkl")

age = st.number_input("Enter Age", min_value=1, max_value=100)
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0)
bp = st.number_input("Enter Blood Pressure", min_value=60, max_value=200)

if st.button("Check Risk"):

    input_data = [[age, bmi, bp]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.warning("High Risk - Please consult a doctor.")
    else:
        st.success("Low Risk - Maintain your current lifestyle.")
        