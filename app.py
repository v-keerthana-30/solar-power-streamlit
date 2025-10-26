# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

st.title("Solar Power Generation Prediction")

# Load trained Random Forest model
rf_model = joblib.load("best_model_rf.pkl")

st.header("Adjust Environmental Conditions:")

# Sliders for interactive input
distance_to_solar_noon = st.slider("Distance to Solar Noon", 0.0, 1.0, 0.5, 0.01)
temperature = st.slider("Temperature (°F)", -50, 150, 58)
wind_direction = st.slider("Wind Direction (degrees)", 0, 360, 180)
wind_speed = st.slider("Wind Speed (m/s)", 0.0, 50.0, 10.0, 0.1)
sky_cover = st.slider("Sky Cover (%)", 0, 100, 20)
visibility = st.slider("Visibility (miles)", 0.0, 20.0, 10.0, 0.1)
humidity = st.slider("Humidity (%)", 0, 100, 50)
avg_wind_speed_period = st.slider("Average Wind Speed (Period)", 0.0, 50.0, 9.0, 0.1)
avg_pressure_period = st.slider("Average Pressure (Period)", 900.0, 1100.0, 1012.0, 0.1)

# Feature order as used in training
feature_cols = [
    'distance-to-solar-noon',
    'temperature',
    'wind-direction',
    'wind-speed',
    'sky-cover',
    'visibility',
    'humidity',
    'average-wind-speed-(period)',
    'average-pressure-(period)'
]

# Prepare input DataFrame
input_df = pd.DataFrame([[
    distance_to_solar_noon,
    temperature,
    wind_direction,
    wind_speed,
    sky_cover,
    visibility,
    humidity,
    avg_wind_speed_period,
    avg_pressure_period
]], columns=feature_cols)

# Predict
prediction = rf_model.predict(input_df)

st.subheader("Predicted Solar Power Generation (kW):")
st.write(round(prediction[0], 2))

# Interactive bar chart of input features
st.subheader("Input Feature Overview")
fig, ax = plt.subplots(figsize=(8,4))
ax.barh(feature_cols, input_df.iloc[0], color='skyblue')
ax.set_xlabel("Value")
ax.set_title("Input Features")
st.pyplot(fig)
