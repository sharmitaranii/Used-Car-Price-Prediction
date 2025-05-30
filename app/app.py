import streamlit as st
import pandas as pd
import joblib

# Load model and column list
model = joblib.load("app/rf_model_log.pkl")
columns = joblib.load("app/model_columns.pkl")

st.title("🚗 Used Car Price Prediction App")

# User input fields based on the model's expected features
user_input = {}
for col in columns:
    if col in ["year", "owner", "km_driven", "mileage", "engine", "max_power", "seats"]:
        user_input[col] = st.number_input(f"Enter {col}", value=0)
    else:
        user_input[col] = st.text_input(f"Enter {col}")

# Predict button
if st.button("Predict Selling Price"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)
    st.success(f"Estimated Selling Price: ₹ {prediction[0]:,.2f}")
