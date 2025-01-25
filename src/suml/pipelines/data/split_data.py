"""
This module contains functions for splitting data into training and testing sets.
"""

from sklearn.model_selection import train_test_split


def split_data(data, parameters):
    """
    Splits the input data into training, development, and test sets.
    Parameters:
    data (pd.DataFrame): The input data containing features and target.
    parameters (dict): A dictionary containing the following keys:
        - "test_size" (float): The proportion of the data to include in the test split.
        - "random_state" (int): The seed used by the random number generator.
    Returns:
    tuple: A tuple containing the following six elements:
        - x_train (pd.DataFrame): Training set features.
        - x_dev (pd.DataFrame): Development set features.
        - x_test (pd.DataFrame): Test set features.
        - y_train (pd.Series): Training set target.
        - y_dev (pd.Series): Development set target.
        - y_test (pd.Series): Test set target.
    """

    # Declare columns
    x = data.drop(columns=["TARGET"])
    y = data["TARGET"]

    # Split data
    x_train, x_temp, y_train, y_temp = train_test_split(
        x, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    x_dev, x_test, y_dev, y_test = train_test_split(
        x_temp, y_temp, test_size=0.5, random_state=parameters["random_state"]
    )

    return x_train, x_dev, x_test, y_train, y_dev, y_test
