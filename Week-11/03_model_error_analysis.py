
# Student performance prediction: Error Analysis

students = ["A", "B", "C", "D", "E"]

study_hours = [2, 3, 5, 7, 8]

actual_results = [
    "Fail", "Fail", "Pass", "Pass", "Pass"
]

predicted_results = [
    "Fail", "Pass", "Pass", "Fail", "Pass"
]

print("MODEL ERROR ANALYSIS REPORT")
print("------------------------------")

correct_predictions = 0
incorrect_predictions = 0

for i in range(len(students)):

    if actual_results[i] == predicted_results[i]:
        correct_predictions += 1

    else:
        incorrect_predictions += 1

        print("Incorrect Prediction:")
        print("Student:", students[i])
        print("Study Hours:", study_hours[i])
        print("Actual Result:", actual_results[i])
        print("Predicted Result:", predicted_results[i])
        print("------------------------------")

total_students = len(students)

accuracy = (correct_predictions / total_students) * 100
error_rate = (incorrect_predictions / total_students) * 100

print("Total Students:", total_students)
print("Correct Predictions:", correct_predictions)
print("Incorrect Predictions:", incorrect_predictions)
print("Accuracy:", accuracy, "%")
print("Error Rate:", error_rate, "%")
