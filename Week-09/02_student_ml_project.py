
from sklearn.model_selection import train_test_split

# Student study hours
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# Actual student results
y = [
    "Fail", "Fail", "Fail", "Fail", "Pass",
    "Pass", "Pass", "Pass", "Pass", "Pass"
]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Total students:", len(X))
print("Training students:", len(X_train))
print("Testing students:", len(X_test))

print("\nTraining data:")
for hours, result in zip(X_train, y_train):
    print(f"Study hours: {hours[0]}, Result: {result}")

print("\nTesting data:")
for hours, result in zip(X_test, y_test):
    print(f"Study hours: {hours[0]}, Result: {result}")
