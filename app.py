
import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('salary_model.pkl', 'rb'))

st.title("💰 Salary Prediction")

st.write("Enter your details to predict salary")

country = st.text_input("Country", "India")

education = st.selectbox(
    "Education Level",
    [
        "Bachelor’s degree",
        "Master’s degree",
        "Doctoral degree",
        "Some college/university study without earning a degree",
        "Secondary school"
    ]
)

experience = st.number_input(
    "Years of Professional Coding Experience",
    min_value=0,
    max_value=50,
    value=3
)

if st.button("Predict Salary"):

    new_data = pd.DataFrame({
        'Country': [country],
        'EdLevel': [education],
        'YearsCodePro': [experience]
    })

    prediction = model.predict(new_data)

    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")
