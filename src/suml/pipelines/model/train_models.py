"""
This module contains functions and classes for training machine learning models.
"""

import pandas as pd
from autogluon.tabular import TabularPredictor


def train_models(x_train, y_train, x_dev, y_dev, parameters):
    """
    Trains an AutoGluon model using the provided training and development datasets.
    Args:
        x_train (pandas.DataFrame): Training features.
        y_train (pandas.Series or pandas.DataFrame): Training targets.
        x_dev (pandas.DataFrame): Development (validation) features.
        y_dev (pandas.Series or pandas.DataFrame): Development (validation) targets.
        parameters (dict): Configuration dictionary containing:
            - autogluon (dict): Must include 'model_path' specifying directory to save the model.
              Optional keys:
                - 'eval_metric' (str): Metric used for evaluation (default: "mean_absolute_error").
                - 'time_limit' (int): Maximum training time in seconds (default: 3600).
    Raises:
        ValueError: If 'model_path' is not found in 'autogluon' within parameters.
    Returns:
        TabularPredictor: A trained AutoGluon TabularPredictor.
    """

    print("Parameters received:", parameters)

    if "autogluon" not in parameters or "model_path" not in parameters["autogluon"]:
        raise ValueError(
            "The 'model_path' key is missing in the 'autogluon' section of parameters."
        )

    model_path = parameters["autogluon"]["model_path"]

    # Changing the way the target is printed, instead of printing the entire
    # Y_train, we print the column name
    print("\nTraining AutoGluon for target: TARGET")

    # Combining X_train and Y_train into a single DataFrame
    train_data = pd.concat([x_train, y_train], axis=1)
    dev_data = pd.concat([x_dev, y_dev], axis=1)

    # Checking the type of train_data
    print(f"X_train type: {type(train_data)}")

    # Defining the metric and problem type (default is "regression")
    eval_metric = parameters["autogluon"].get("eval_metric", "mean_absolute_error")

    # Training the model
    predictor = TabularPredictor(
        label="TARGET",
        eval_metric=eval_metric,
        path=model_path,
        problem_type="regression",
    ).fit(
        train_data=train_data,
        time_limit=parameters["autogluon"].get("time_limit", 3600),
    )

    # Evaluating the model's performance on validation data
    performance = predictor.evaluate(dev_data)
    print(f"Performance for TARGET: {performance}")

    return predictor
