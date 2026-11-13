
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Actual student results
y_actual = [
    "Pass", "Pass", "Fail", "Fail", "Pass",
    "Fail", "Pass", "Fail", "Pass", "Fail"
]

# Model predictions
y_predicted = [
    "Pass", "Fail", "Fail", "Pass", "Pass",
    "Fail", "Fail", "Fail", "Pass", "Pass"
]

# Calculate evaluation metrics
accuracy = accuracy_score(y_actual, y_predicted)

precision = precision_score(
    y_actual, y_predicted, pos_label="Pass"
)

recall = recall_score(
    y_actual, y_predicted, pos_label="Pass"
)

f1 = f1_score(
    y_actual, y_predicted, pos_label="Pass"
)

matrix = confusion_matrix(
    y_actual, y_predicted, labels=["Fail", "Pass"]
)

# Display results
print("MODEL EVALUATION REPORT")
print("------------------------------")

print("Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")
print("F1 Score:", round(f1 * 100, 2), "%")

print("------------------------------")
print("Confusion Matrix:")
print(matrix)
