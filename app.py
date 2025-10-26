# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title("Solar Power Generation Prediction")

# Load trained model
rf_model = joblib.load("best_model_rf.pkl")

st.header("Enter Environmental Conditions:")

# User inputs
distance_to_solar_noon = st.number_input("Distance to Solar Noon", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
temperature = st.number_input("Temperature (°F)", min_value=-50, max_value=150, value=58)
wind_direction = st.number_input("Wind Direction (degrees)", min_value=0, max_value=360, value=180)
wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
sky_cover = st.number_input("Sky Cover (%)", min_value=0, max_value=100, value=20)
visibility = st.number_input("Visibility (miles)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50)
avg_wind_speed_period = st.number_input("Average Wind Speed (Period)", min_value=0.0, max_value=50.0, value=9.0, step=0.1)
avg_pressure_period = st.number_input("Average Pressure (Period)", min_value=900.0, max_value=1100.0, value=1012.0, step=0.1)

# Prepare input for prediction (match training columns exactly)
input_df = pd.DataFrame({
    "distance-to-solar-noon": [distance_to_solar_noon],
    "temperature": [temperature],
    "wind-direction": [wind_direction],
    "wind-speed": [wind_speed],
    "sky-cover": [sky_cover],
    "visibility": [visibility],
    "humidity": [humidity],
    "average-wind-speed-(period)": [avg_wind_speed_period],
    "average-pressure-(period)": [avg_pressure_period]
})

# Predict
prediction = rf_model.predict(input_df)

st.subheader("Predicted Solar Power Generation (kW):")
st.write(round(prediction[0], 2))
