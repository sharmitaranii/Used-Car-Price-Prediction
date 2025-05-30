import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and column list
model = joblib.load('rf_model_log.pkl')
columns = joblib.load('model_columns.pkl')  # Make sure file is renamed correctly

# Page configuration
st.set_page_config(page_title="Used Car Price Predictor", layout="centered")
st.title("🚗 Used Car Price Prediction App")
st.markdown("Enter your car details below to estimate its resale price.")

# Sidebar inputs
st.sidebar.header("🛠️ Car Features")

brand = st.sidebar.selectbox("Brand", ['BMW', 'Chevrolet', 'Ford', 'Jeep', 'Land', 'Mercedes-Benz', 'Nissan', 'Porsche', 'Toyota', 'Volkswagen', 'Other'])
fuel_type = st.sidebar.selectbox("Fuel Type", ['Gasoline', 'Diesel', 'Hybrid', 'Plug-In Hybrid', 'E85 Flex Fuel', 'Unknown'])
transmission = st.sidebar.selectbox("Transmission", [
    'Automatic', '7-Speed', '8-Speed Automatic', 'Manual', 'A/T', '7-Speed A/T', '8-Speed Automatic with Auto-Shift'
])
clean_title = st.sidebar.radio("Clean Title", ['Yes', 'Unknown'])

model_year = st.sidebar.slider("Model Year", 2000, 2024, 2020)
milage = st.sidebar.number_input("Mileage (in miles)", min_value=0, step=500)

# Derived feature
car_age = 2025 - model_year

# Build feature vector
input_dict = {
    'model_year': model_year,
    'milage': milage,
    'accident': 0,  # Default assumption: no accident
    'car_age': car_age
}

# One-hot encode
for col in columns:
    if col.startswith('brand_'):
        input_dict[col] = 1 if f"brand_{brand}" == col else 0
    elif col.startswith('fuel_type_'):
        input_dict[col] = 1 if f"fuel_type_{fuel_type}" == col else 0
    elif col.startswith('transmission_'):
        input_dict[col] = 1 if f"transmission_{transmission}" == col else 0
    elif col == 'clean_title_Yes':
        input_dict[col] = 1 if clean_title == 'Yes' else 0

# Create DataFrame for prediction
input_df = pd.DataFrame([input_dict], columns=columns)

# Predict button
if st.sidebar.button("🔍 Predict Price"):
    log_price = model.predict(input_df)[0]
    predicted_price = np.exp(log_price)

    st.success(f"💰 Estimated Selling Price: ₹{predicted_price:,.0f}")
    st.caption("📌 Note: This is an approximate valuation based on historical data.")