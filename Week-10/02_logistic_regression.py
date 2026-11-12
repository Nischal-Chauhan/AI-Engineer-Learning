
from sklearn.linear_model import LogisticRegression

# Student study hours
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# Actual student results
y = [
    "Fail", "Fail", "Fail", "Fail", "Pass",
    "Pass", "Pass", "Pass", "Pass", "Pass"
]

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Predict results for new students
new_students = [[2], [5], [8]]

predictions = model.predict(new_students)

# Display predictions
for hours, result in zip(new_students, predictions):
    print(f"Study hours: {hours[0]}, Predicted result: {result}")
