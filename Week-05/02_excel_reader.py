import pandas as pd

students = pd.read_csv("Week-05/students.csv")

students.to_excel("Week-05/students.xlsx", index=False)

excel_students = pd.read_excel(
    "Week-05/students.xlsx",
    engine="openpyxl"
)

print(excel_students)