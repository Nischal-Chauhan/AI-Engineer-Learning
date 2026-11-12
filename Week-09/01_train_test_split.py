
from sklearn.model_selection import train_test_split

# 10 student records
study_hours = [[1], [2], [3], [4], [5],
               [6], [7], [8], [9], [10]]

results = [
    "Fail", "Fail", "Fail", "Pass", "Pass",
    "Pass", "Pass", "Pass", "Pass", "Pass"
]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    study_hours,
    results,
    test_size=0.2,
    random_state=42
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

print("Training data:", X_train)
print("Testing data:", X_test)
