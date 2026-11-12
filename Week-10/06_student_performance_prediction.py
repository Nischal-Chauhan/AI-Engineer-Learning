
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Student dataset
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

results = [
    "Fail", "Fail", "Fail", "Fail", "Pass",
    "Pass", "Pass", "Pass", "Pass", "Pass"
]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, results, test_size=0.2, random_state=42
)

# Linear Regression: predict marks
linear_model = LinearRegression()
linear_model.fit(X, marks)

# Classification models
models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

print("STUDENT PERFORMANCE PREDICTION")
print("--------------------------------")

for name, model in models.items():
    model.fit(X_train, y_train)
    prediction = model.predict([[7]])
    print(f"{name}: {prediction[0]}")

marks_prediction = linear_model.predict([[7]])

print("--------------------------------")
print("Predicted marks for 7 study hours:", marks_prediction[0])
