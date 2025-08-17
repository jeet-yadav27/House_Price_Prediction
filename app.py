import streamlit as st
import numpy as np
from joblib import load

# Load the trained model
model = load("linear_regression_model.pkl")

# Streamlit app
st.title("🏠 House Price Prediction App")
st.markdown("Enter the property details to estimate the **house price**.")

# User Inputs
square_meters = st.number_input("Square Meters", min_value=10.0, max_value=1000.0, value=100.0, step=1.0)
number_of_rooms = st.number_input("Number of Rooms", min_value=1, max_value=100, value=3, step=1)
has_yard = st.selectbox("Has Yard?", ["No", "Yes"])
has_pool = st.selectbox("Has Pool?", ["No", "Yes"])
floors = st.number_input("Number of Floors", min_value=1, max_value=10, value=1, step=1)
city_code = st.number_input("City Code", min_value=1, max_value=9999, value=100)
city_part_range = st.slider("City Part Range (e.g., 1 = rural to 10 = urban)", 1, 10, 2)
num_prev_owners = st.number_input("Number of Previous Owners", min_value=0, max_value=20, value=1, step=1)
is_new_built = st.selectbox("Is Newly Built?", ["No", "Yes"])
has_storm_protector = st.selectbox("Has Storm Protector?", ["No", "Yes"])
basement = st.selectbox("Has Basement?", ["No", "Yes"])
attic = st.selectbox("Has Attic?", ["No", "Yes"])
garage = st.selectbox("Has Garage?", ["No", "Yes"])
has_storage_room = st.selectbox("Has Storage Room?", ["No", "Yes"])
has_guest_room = st.selectbox("Has Guest Room?", ["No", "Yes"])
age = st.number_input("Property Age (in years)", min_value=0, max_value=200, value=10, step=1)
total_rooms = st.number_input("Total Rooms", min_value=1, max_value=200, value=5, step=1)
total_area = st.number_input("Total Area (sqm)", min_value=10.0, max_value=2000.0, value=150.0, step=1.0)

# Convert inputs to 0 or 1 for boolean features
def binary(value): return 1 if value == "Yes" else 0

# Ensure the input order matches model training
input_data = np.array([[
    square_meters,
    number_of_rooms,
    binary(has_yard),
    binary(has_pool),
    floors,
    city_code,
    city_part_range,
    num_prev_owners,
    binary(is_new_built),
    binary(has_storm_protector),
    binary(basement),
    binary(attic),
    binary(garage),
    binary(has_storage_room),
    binary(has_guest_room),
    age,
    total_rooms,
    total_area
]])

# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(input_data)
    st.success(f"🏡 Estimated House Price: **${prediction[0]:,.2f}**")
