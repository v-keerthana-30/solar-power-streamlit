import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained Random Forest model
rf_model = joblib.load("best_model_rf.pkl")

# Load the LabelEncoder
le = LabelEncoder()
le.fit(['Low', 'Medium', 'High'])  # Replace with your dataset Power_Level categories

st.title("Solar Power Generation Prediction")

st.sidebar.header("Input Parameters")

def user_input_features():
    distance_to_solar_noon = st.sidebar.number_input("Distance to Solar Noon", 0.0, 1.0, 0.5)
    temperature = st.sidebar.number_input("Temperature (°F)", 0, 100, 60)
    wind_direction = st.sidebar.number_input("Wind Direction (°)", 0, 360, 180)
    wind_speed = st.sidebar.number_input("Wind Speed (m/s)", 0.0, 50.0, 10.0)
    sky_cover = st.sidebar.number_input("Sky Cover (%)", 0, 100, 20)
    visibility = st.sidebar.number_input("Visibility (km)", 0.0, 20.0, 10.0)
    humidity = st.sidebar.number_input("Humidity (%)", 0, 100, 50)
    avg_wind_speed = st.sidebar.number_input("Average Wind Speed", 0.0, 50.0, 10.0)
    avg_pressure = st.sidebar.number_input("Average Pressure", 900.0, 1100.0, 1012.0)
    power_level = st.sidebar.selectbox("Power Level", ['Low', 'Medium', 'High'])
    
    power_level_encoded = le.transform([power_level])[0]

    data = {
        'distance-to-solar-noon': distance_to_solar_noon,
        'temperature': temperature,
        'wind-direction': wind_direction,
        'wind-speed': wind_speed,
        'sky-cover': sky_cover,
        'visibility': visibility,
        'humidity': humidity,
        'average-wind-speed-(period)': avg_wind_speed,
        'average-pressure-(period)': avg_pressure,
        'Power_Level': power_level_encoded
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

prediction = rf_model.predict(input_df)
st.subheader("Predicted Solar Power Generated (kW)")
st.write(prediction[0])
