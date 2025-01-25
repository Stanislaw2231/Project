"""
This module contains functions and classes for evaluating machine learning models.
"""

import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_models(predictor, x_test, y_test, parameters):
    """
    Evaluate the performance of a trained model using various regression metrics.
    Args:
        predictor: A trained model that implements the 'predict' method.
        x_test: The test features to be used for making predictions.
        y_test: The ground truth values for calculating the metrics.
        parameters: Additional parameters or configuration for the evaluation process.
    Returns:
        A tuple containing:
            - A pandas DataFrame summarizing the evaluation metrics (MAE, MSE, R2).
            - The predictor instance, unchanged.
    The evaluation metrics calculated are:
        - MAE (Mean Absolute Error)
        - MSE (Mean Squared Error)
        - R2 (Coefficient of Determination)
    """

    # Predict
    prediction = predictor.predict(x_test)

    # Calculate metrics
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    r2 = r2_score(y_test, prediction)

    result = {"MAE": mae, "MSE": mse, "R2": r2}

    # Create a DataFrame with evaluation metrics
    results_df = pd.DataFrame.from_dict(result, orient="index").reset_index()
    results_df.rename(columns={"index": "Metric", 0: "Value"}, inplace=True)

    print("\nFinal Evaluation Results:\n")
    print(results_df)

    return results_df, predictor
