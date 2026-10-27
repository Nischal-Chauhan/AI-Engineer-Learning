import pandas as pd

students = pd.read_csv("Week-06/messy_students.csv")

print(students)

print("Missing values per column:")
print(students.isnull().sum())

print("Duplicate rows:", students.duplicated().sum())