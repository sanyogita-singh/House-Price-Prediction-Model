import streamlit as st
import numpy as np
import pickle

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏡 House Price Prediction App")
st.subheader("Enter the house features below:")

# --- USER INPUTS ---
sqft_living = st.slider("Living Area (sqft)", 300, 13500, 1500)
sqft_above = st.slider("Above Ground Area (sqft)", 300, 10000, 1200)
sqft_lot = st.slider("Lot Size (sqft)", 500, 1650000, 5000)
sqft_basement = st.slider("Basement Area (sqft)", 0, 5000, 500 )
bedrooms = st.slider("Bedrooms", 0, 33, 3)
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4, 5, 6, 7, 8])
grade = st.selectbox("Grade", list(range(1, 14)))
view = st.selectbox("View Rating", [0, 1, 2, 3, 4])
floors = st.selectbox("Floors", [1, 2, 3])
condition = st.selectbox("Condition", [1, 2, 3, 4, 5])
renovated = st.selectbox("Renovated?", ["Yes", "No"])
waterfront = st.selectbox("Waterfront?", ["Yes", "No"])

# Convert 'renovated' to numeric (assuming 1 for yes, 0 for no)
renovated_binary = 1 if renovated == "Yes" else 0
waterfront_binary = 1 if waterfront == "Yes" else 0

# --- PREDICT ---
if st.button("🎯 Predict Price"):
    input_data = np.array([[
        sqft_living, sqft_above, bathrooms, grade,
        bedrooms, view, sqft_lot, floors, condition, renovated_binary, sqft_basement, waterfront_binary
    ]])

    prediction = model.predict(input_data)[0]
    st.success(f"💸 Estimated Price: ${prediction:,.2f}")
