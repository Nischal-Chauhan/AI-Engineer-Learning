
from sklearn.tree import DecisionTreeClassifier

# Student study hours
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# Actual student results
y = [
    "Fail", "Fail", "Fail", "Fail", "Pass",
    "Pass", "Pass", "Pass", "Pass", "Pass"
]

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X, y)

# Predict for new students
new_students = [[2], [5], [8]]

predictions = model.predict(new_students)

# Display predictions
for hours, result in zip(new_students, predictions):
    print(f"Study hours: {hours[0]}, Predicted result: {result}")
