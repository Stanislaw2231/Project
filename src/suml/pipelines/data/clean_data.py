"""
This module contains functions for cleaning and preprocessing data.
"""

import pandas as pd


def clean_data(data):
    """
    Cleans the input data by removing columns and rows with missing values, converting the
    'TARGET' column to numeric, and handling infinite values.
    Parameters:
        data (pandas.DataFrame): The input data to be cleaned.
    Returns:
        pandas.DataFrame: The cleaned data after dropping missing and infinite values,
        and converting the 'TARGET' column to numeric.
    """
    # Drop columns with all NaN values
    data = data.dropna(axis=1, how="all")

    # Drop rows with any NaN values
    data = data.dropna(axis=0, how="any")

    # Convert 'TARGET' to numeric, replacing errors with NaN
    data["TARGET"] = pd.to_numeric(data["TARGET"], errors="coerce")

    # Check and handle infinite values
    data.replace([float("inf"), float("-inf")], float("nan"), inplace=True)

    # Drop rows with any NaN values
    data = data.dropna(axis=0, how="any")

    # Initialize LabelEncoder
    # label_encoder = LabelEncoder()

    # # Iterate over columns with object type and encode them
    # for column in data.select_dtypes(include=['object']).columns:
    #     data[column] = label_encoder.fit_transform(data[column])

    return data
