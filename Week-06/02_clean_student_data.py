import pandas as pd

students = pd.read_csv("Week-06/messy_students.csv")

clean_students = students.dropna(subset=["marks"])
clean_students = clean_students.drop_duplicates()
clean_students = clean_students.reset_index(drop=True)

print("Cleaned student data:")
clean_students["passed"] = clean_students["marks"] >= 35
print(clean_students)
clean_students.to_csv("Week-06/cleaned_students.csv", index=False)
print("Cleaned data saved.")