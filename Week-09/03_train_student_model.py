
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Student study hours
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# Actual results
y = [
    "Fail", "Fail", "Fail", "Fail", "Pass",
    "Pass", "Pass", "Pass", "Pass", "Pass"
]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

print("Actual results:    ", y_test)
print("Predicted results: ", predictions)

# Evaluate model
accuracy = accuracy_score(y_test, predictions)

print("Model accuracy:", accuracy * 100, "%")

# Predict for a new student
new_student = [[8]]
result = model.predict(new_student)

print("Prediction for 8 study hours:", result[0])
