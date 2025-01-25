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


# Load the dataset
@st.cache_data
def load_data():
    """
    Load the data from a specified CSV file and return it as a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """

    return pd.read_csv("data/raw/Food_Time_Data_Set.csv")


data = load_data()


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
            "Precipitation",
            float(data["precipitation"].dropna().min()),
            float(data["precipitation"].dropna().max()),
            step=0.1,
            key="precipitation",
        )
        user_input["Restaurant_latitude"] = st.slider(
            "Restaurant Latitude",
            float(data["Restaurant_latitude"].dropna().min()),
            float(data["Restaurant_latitude"].dropna().max()),
            step=0.001,
            key="restaurant_latitude",
        )
        user_input["Delivery_location_latitude"] = st.slider(
            "Delivery Location Latitude",
            float(data["Delivery_location_latitude"].dropna().min()),
            float(data["Delivery_location_latitude"].dropna().max()),
            step=0.001,
            key="delivery_location_latitude",
        )
        user_input["Distance (km)"] = st.slider(
            "Distance",
            float(data["Distance (km)"].dropna().min()),
            float(data["Distance (km)"].dropna().max()),
            step=1.0,
            key="distance",
        )

    with col2:
        user_input["Delivery_person_Age"] = st.slider(
            "Delivery Person Age",
            int(data["Delivery_person_Age"].dropna().min()),
            int(data["Delivery_person_Age"].dropna().max()),
            step=1,
            key="delivery_person_age",
        )
        user_input["Restaurant_longitude"] = st.slider(
            "Restaurant Longitude",
            float(data["Restaurant_longitude"].dropna().min()),
            float(data["Restaurant_longitude"].dropna().max()),
            step=0.001,
            key="restaurant_longitude",
        )
        user_input["Delivery_location_longitude"] = st.slider(
            "Delivery Location Longitude",
            float(data["Delivery_location_longitude"].dropna().min()),
            float(data["Delivery_location_longitude"].dropna().max()),
            step=0.001,
            key="delivery_location_longitude",
        )
        user_input["Delivery_person_Ratings"] = st.slider(
            "Delivery Person Ratings", 1, 6, step=1, key="delivery_person_ratings"
        )

    with col3:
        user_input["Type_of_order"] = st.radio(
            "Type of Order",
            data["Type_of_order"].dropna().unique(),
            key="type_of_order",
        )
        user_input["Type_of_vehicle"] = st.radio(
            "Type of Vehicle",
            data["Type_of_vehicle"].dropna().unique(),
            key="type_of_vehicle",
        )
        user_input["Traffic_Level"] = st.radio(
            "Traffic Level",
            ["Very Low", "Low", "Moderate", "High", "Very High"],
            key="traffic_level",
        )

    with col4:
        user_input["weather_description"] = st.selectbox(
            "Weather Description",
            data["weather_description"].dropna().unique(),
            key="weather_description",
        )
        delivery_person_ids = [""] + list(data["Delivery_person_ID"].dropna().unique())
        user_input["Delivery_person_ID"] = st.selectbox(
            "Delivery Person ID", delivery_person_ids, key="delivery_person_id"
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
