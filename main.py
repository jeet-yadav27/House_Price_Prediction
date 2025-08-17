import streamlit as st
import numpy as np
import pickle

# Load the trained model
from joblib import load
model = load("linear_regression_model.pkl")

# Streamlit app
st.title("🏠 House Price Prediction App")
st.markdown("Enter the property details to estimate the **house price**.")

# User Inputs
square_meters = st.number_input("Square Meters", min_value=10.0, max_value=1000.0, value=100.0, step=1.0)
has_yard = st.selectbox("Has Yard?", ["No", "Yes"])
has_pool = st.selectbox("Has Pool?", ["No", "Yes"])
floors = st.number_input("Number of Floors", min_value=1, max_value=10, value=1, step=1)
city_part_range = st.slider("City Part Range (e.g., 1 = rural to 5 = urban)", 1, 10, 2)
is_new_built = st.selectbox("Is Newly Built?", ["No", "Yes"])
has_storm_protector = st.selectbox("Has Storm Protector?", ["No", "Yes"])
basement = st.selectbox("Has Basement?", ["No", "Yes"])
attic = st.selectbox("Has Attic?", ["No", "Yes"])
garage = st.selectbox("Has Garage?", ["No", "Yes"])
total_area = st.number_input("Total Area (sqm)", min_value=10.0, max_value=2000.0, value=150.0, step=1.0)

# Convert inputs to 0 or 1 for boolean features
def binary(value): return 1 if value == "Yes" else 0

input_data = np.array([[
    square_meters,
    binary(has_yard),
    binary(has_pool),
    floors,
    city_part_range,
    binary(is_new_built),
    binary(has_storm_protector),
    binary(basement),
    binary(attic),
    binary(garage),
    total_area
]])

# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(input_data)
    st.success(f"🏡 Estimated House Price: **${prediction[0]:,.2f}**")
