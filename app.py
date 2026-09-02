
import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("salary_model.pkl", "rb"))

# Title
st.title("Salary Prediction")
st.write("Enter your details to predict your salary")

# Country dropdown
countries = [
    "United States",
    "United Kingdom",
    "Germany",
    "India",
    "Canada",
    "France"
]

country = st.selectbox("Country", countries)

# Education dropdown
education = st.selectbox(
    "Education Level",
    [
        "Bachelor's Degree",
        "Master's Degree",
        "PhD",
        "Less than a Bachelors"
    ]
)

# Years of professional experience
experience = st.number_input(
    "Years of Professional Coding Experience",
    min_value=0.0,
    max_value=50.0,
    value=3.0,
    step=1.0
)

# Prediction button
if st.button("Predict Salary"):

    # Create input data
    new_data = pd.DataFrame({
        "Country": [country],
        "EdLevel": [education],
        "YearsCodePro": [experience]
    })

    # Make prediction
    prediction = model.predict(new_data)

    # Display result
    st.success(f"Predicted Salary: {prediction[0]:,.2f}")
