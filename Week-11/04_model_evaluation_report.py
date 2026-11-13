
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Student dataset
# Features: Study hours, Attendance percentage

X = [
    [1, 50], [2, 55], [2, 60], [3, 65],
    [3, 70], [4, 65], [4, 75], [5, 70],
    [5, 80], [6, 75], [6, 85], [7, 80],
    [7, 90], [8, 85], [8, 95], [9, 90],
    [9, 95], [10, 95], [3, 50], [7, 65]
]

y = [
    "Fail", "Fail", "Fail", "Fail",
    "Fail", "Fail", "Fail", "Pass",
    "Pass", "Pass", "Pass", "Pass",
    "Pass", "Pass", "Pass", "Pass",
    "Pass", "Pass", "Fail", "Pass"
]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create machine learning model
model = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

# Train model
model.fit(X_train, y_train)

# Make predictions
y_predicted = model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_predicted)

precision = precision_score(
    y_test, y_predicted, pos_label="Pass"
)

recall = recall_score(
    y_test, y_predicted, pos_label="Pass"
)

f1 = f1_score(
    y_test, y_predicted, pos_label="Pass"
)

# Confusion matrix
matrix = confusion_matrix(
    y_test, y_predicted,
    labels=["Fail", "Pass"]
)

# Cross-validation
cv_scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

# Display evaluation report
print("COMPLETE MODEL EVALUATION REPORT")
print("--------------------------------------")

print("Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")
print("F1 Score:", round(f1 * 100, 2), "%")

print("--------------------------------------")
print("Confusion Matrix:")
print(matrix)

print("--------------------------------------")
print("CROSS-VALIDATION RESULTS")

for i, score in enumerate(cv_scores):
    print(f"Fold {i + 1} Accuracy: {score * 100:.2f}%")

print(
    "Average CV Accuracy:",
    round(cv_scores.mean() * 100, 2), "%"
)

# Analyse incorrect predictions
print("--------------------------------------")
print("ERROR ANALYSIS")

incorrect_count = 0

for i in range(len(y_test)):
    if y_test[i] != y_predicted[i]:
        incorrect_count += 1

        print("Actual:", y_test[i])
        print("Predicted:", y_predicted[i])
        print("Study Hours:", X_test[i][0])
        print("Attendance:", X_test[i][1])
        print("--------------------------------------")

print("Total Test Students:", len(y_test))
print("Incorrect Predictions:", incorrect_count)
print("Correct Predictions:", len(y_test) - incorrect_count)
