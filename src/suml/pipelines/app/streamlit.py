"""
This module contains the Streamlit application code.
"""

import pandas as pd
import streamlit as st
from autogluon.tabular import TabularPredictor

# Set application width
st.set_page_config(layout="wide", page_title="Delivery Prediction App", page_icon="🚚")

# Load the saved model
MODEL_PATH = "data/models"
predictor = TabularPredictor.load(MODEL_PATH)


def main():
    """
    Displays a Streamlit application for delivery time prediction.
    The function sets up a user-friendly interface where users can:
    1. Input weather, location, and delivery-related information through sliders,
        radio buttons, and text fields.
    2. Review the entered data in a live-updated table.
    3. Obtain a predicted delivery time by clicking a dedicated button.
    All provided user inputs are collected into a pandas DataFrame,
    which is then passed to a prediction model.
    """

    st.title("Delivery Prediction App")

    st.subheader("Entered Data")
    input_data_placeholder = st.empty()

    col1, col2 = st.columns([1, 1])
    user_input = {}

    with col1:
        user_input["Distance (km)"] = st.slider(
            "Distance", 1.0, 60.0, step=1.0, key="distance"
        )
        user_input["Traffic_Level"] = st.radio(
            "Traffic Level", ["Very Low", "Low", "Moderate", "High", "Very High"], key="traffic_level"
        )
        user_input["Type_of_vehicle"] = st.radio(
            "Type of Vehicle",
            ["motorcycle", "scooter", "electric_scooter", "bicycle"],
            key="type_of_vehicle",
        )
        user_input["Type_of_order"] = st.radio(
            "Type of Order",
            ["Snack", "Drinks", "Buffet", "Meal"],
            key="type_of_order",
        )
        
        

    with col2:
        user_input["weather_description"] = st.selectbox(
            "Weather Description",
            [
                "haze",
                "mist",
                "broken clouds",
                "clear sky",
                "scattered clouds",
                "overcast clouds",
                "light rain",
                "smoke",
                "fog",
                "few clouds",
                "moderate rain",
            ],
            key="weather_description",
        )
        
        user_input["humidity"] = st.slider(
            "Humidity", 27, 94, step=1, key="humidity"
        )
        
        user_input["temperature"] = st.slider(
            "Temperature (°C)", -50, 50, step=1, key="temperature", value= 0
        )
        
        user_input["precipitation"] = st.slider(
            "Precipitation", 0.0, 1.46, step=0.1, key="precipitation"
        )

    input_data = pd.DataFrame(user_input, index=[0])
    input_data_placeholder.write(input_data)

    st.write("---")
    if st.button("Predict"):
        prediction = predictor.predict(input_data).round(0)
        st.success(f"Predicted Delivery Time: {int(prediction[0])} minutes")


if __name__ == "__main__":
    main()
