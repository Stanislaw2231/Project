"""
This module contains functions for analyzing data.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def perform_analysis(data):
    """
    Perform exploratory data analysis on the given dataset by removing an 'ID' column (if present),
    printing data information and descriptive statistics, checking for missing values, and producing
    various plots such as histograms and a correlation heatmap.
    Args:
        data (pandas.DataFrame):
            A pandas DataFrame containing the dataset to be analyzed.
    Returns:
        pandas.DataFrame:
            The original DataFrame with the 'ID' column removed (if it was present).
    """
    # Load and inspect data
    if "ID" in data.columns:
        data = data.drop(columns=["ID"])

    # Inspect the data
    print(data)
    print(data.head())
    print(data.info())
    print(data.describe())

    # Check for missing values
    print(data.isnull().sum())
    sns.heatmap(data.isnull(), cbar=False)
    plt.show()

    # Plot histograms
    data.hist(bins=50, figsize=(16, 12))
    plt.show()

    # Correlation matrix for numeric columns
    numeric_data = data.select_dtypes(include=["number"])
    correlation_matrix = numeric_data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()

    return data
