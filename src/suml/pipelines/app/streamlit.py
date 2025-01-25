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

    col1, col2, col3, col4 = st.columns([1, 1, 0.5, 1])
    user_input = {}

    with col1:
        user_input["precipitation"] = st.slider(
            "Precipitation", 0.0, 1.46, step=0.1, key="precipitation"
        )
        user_input["Restaurant_latitude"] = st.slider(
            "Restaurant Latitude",
            -30.902872,
            30.914057,
            step=0.001,
            key="restaurant_latitude",
        )
        user_input["Delivery_location_latitude"] = st.slider(
            "Delivery Location Latitude",
            0.01,
            31.054057,
            step=0.001,
            key="delivery_location_latitude",
        )
        user_input["Distance (km)"] = st.slider(
            "Distance", 1.55, 59.84, step=1.0, key="distance"
        )

    with col2:
        user_input["Delivery_person_Age"] = st.slider(
            "Delivery Person Age", 15, 50, step=1, key="delivery_person_age"
        )
        user_input["Restaurant_longitude"] = st.slider(
            "Restaurant Longitude",
            -88.352885,
            88.433452,
            step=0.001,
            key="restaurant_longitude",
        )
        user_input["Delivery_location_longitude"] = st.slider(
            "Delivery Location Longitude",
            0.01,
            88.563452,
            step=0.001,
            key="delivery_location_longitude",
        )
        user_input["Delivery_person_Ratings"] = st.slider(
            "Delivery Person Ratings", 1, 6, step=1, key="delivery_person_ratings"
        )

    with col3:
        user_input["Type_of_order"] = st.radio(
            "Type of Order",
            ["Snack ", "Drinks ", "Buffet ", "Meal "],
            key="type_of_order",
        )
        user_input["Type_of_vehicle"] = st.radio(
            "Type of Vehicle",
            ["motorcycle ", "scooter ", "electric_scooter ", "bicycle "],
            key="type_of_vehicle",
        )
        user_input["Traffic_Level"] = st.radio(
            "Traffic Level", ["Very Low", "Low", "Moderate", "High", "Very High"], key="traffic_level"
        )

    with col4:
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
        user_input["Delivery_person_ID"] = st.selectbox(
            "Delivery Person ID",
            [
                "",
                "INDORES13DEL02",
                "BANGRES18DEL02",
                "BANGRES19DEL01",
                "BHPRES11DEL01",
                "BHPRES09DEL02",
                "ALHRES13DEL01",
            ],
            key="delivery_person_id",
        )
        temp_input = st.text_input("Temperature (°C)", value="0", key="temperature")
        try:
            checked_temp = int(temp_input)
            if not -50 <= checked_temp <= 50:
                st.error("Temperature must be between -50 and 50.")
            user_input["temperature"] = checked_temp
        except ValueError:
            st.error("Please enter a valid integer for Temperature.")
            user_input["temperature"] = 0

    user_input["humidity"] = st.session_state.get("humidity", 0)

    input_data = pd.DataFrame(user_input, index=[0])
    input_data_placeholder.write(input_data)

    st.write("---")
    if st.button("Predict"):
        prediction = predictor.predict(input_data)
        st.success(f"Predicted Delivery Time: {prediction[0]} minutes")


if __name__ == "__main__":
    main()
