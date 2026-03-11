import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("machine_failure_prediction.pkl")

st.title("Machine Failure Prediction System")

st.write("Enter machine sensor values to predict failure")

# Inputs
footfall = st.number_input("Footfall", min_value=0)
tempMode = st.number_input("Temp Mode", min_value=0)
AQ = st.number_input("Air Quality (AQ)", min_value=0.0)
USS = st.number_input("Ultrasonic Sensor (USS)", min_value=0)
CS = st.number_input("Current Sensor (CS)", min_value=0)
VOC = st.number_input("VOC Level", min_value=0.0)
RP = st.number_input("Rotational Position (RP)", min_value=0)
IP = st.number_input("Input Pressure (IP)", min_value=0)
Temperature = st.number_input("Temperature", min_value=0.0)

# Create dataframe
df = pd.DataFrame({
    "footfall": [footfall],
    "tempMode": [tempMode],
    "AQ": [AQ],
    "USS": [USS],
    "CS": [CS],
    "VOC": [VOC],
    "RP": [RP],
    "IP": [IP],
    "Temperature": [Temperature]
})

# Prediction
if st.button("Predict Machine Failure"):
    prediction = model.predict(df)

    if prediction[0] == 1:
        st.error("⚠ Machine Failure Likely")
    else:
        st.success("✅ Machine is Working Normally")
