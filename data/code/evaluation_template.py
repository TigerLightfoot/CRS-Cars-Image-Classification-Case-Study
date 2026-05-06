"""
Evaluation template for the CRS Cars Image Classification Case Study.

Use this file after generating true labels and predicted labels from your model.
"""

from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd


def evaluate_predictions(y_true, y_pred, class_names):
    """
    Prints a classification report and returns a confusion matrix dataframe.
    """

    print("Classification Report")
    print(classification_report(y_true, y_pred, target_names=class_names))

    cm = confusion_matrix(y_true, y_pred)
    cm_df = pd.DataFrame(cm, index=class_names, columns=class_names)

    print("\nConfusion Matrix")
    print(cm_df)

    return cm_df


if __name__ == "__main__":
    # Replace these with real results from your model.
    y_true = []
    y_pred = []
    class_names = []

    if not y_true or not y_pred or not class_names:
        print("Add model predictions, true labels, and class names before running.")
    else:
        evaluate_predictions(y_true, y_pred, class_names)
