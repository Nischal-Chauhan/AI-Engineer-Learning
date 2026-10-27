import pandas as pd

students = pd.read_csv("Week-05/students.csv")
print("Student records:")
print(students)
print("Number of students:", students.shape[0])
print("Average marks:", students["marks"].mean())
print("Highest marks:", students["marks"].max())
print("Lowest marks:", students["marks"].min())
print("Students scoring 90 or above:")
print(students[students["marks"] >= 90])
print("Average marks by city:")
print(students.groupby("city")["marks"].mean())