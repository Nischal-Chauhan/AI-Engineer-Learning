
from sklearn.linear_model import LinearRegression

# Student study hours
X = [[1], [2], [3], [4], [5], [6]]

# Student exam marks
y = [35, 40, 45, 50, 55, 60]

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict marks for 7 study hours
prediction = model.predict([[7]])

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

print("Predicted marks for 7 study hours:", prediction[0])
