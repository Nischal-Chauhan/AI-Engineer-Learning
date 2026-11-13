from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create model
model = LogisticRegression(max_iter=1000)

# Perform 5-fold cross-validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

# Display results
print("CROSS-VALIDATION REPORT")
print("------------------------------")

for i, score in enumerate(scores, start=1):
    print(f"Fold {i} Accuracy: {score * 100:.2f}%")

print("------------------------------")
print("Average Accuracy:", round(scores.mean() * 100, 2), "%")