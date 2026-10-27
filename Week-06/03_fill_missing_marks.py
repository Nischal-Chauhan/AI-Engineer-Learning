import pandas as pd

students = pd.read_csv("Week-06/messy_students.csv")

average_marks = students["marks"].mean()
students["marks"] = students["marks"].fillna(average_marks)

print("Marks after filling the missing value:")
print(students)
students.to_csv("Week-06/students_with_filled_marks.csv", index=False)
print("Filled data saved.")