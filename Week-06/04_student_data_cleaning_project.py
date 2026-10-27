import pandas as pd

# Messy CSV file read karo
students = pd.read_csv("Week-06/messy_students.csv")

print("Original data:")
print(students)

# Missing marks ko available marks ke average se fill karo
average_marks = students["marks"].mean()
students["marks"] = students["marks"].fillna(average_marks)

# Duplicate rows hatao aur index dobara set karo
clean_students = students.drop_duplicates().reset_index(drop=True)

# Feature engineering: marks se ek naya column banao
clean_students["passed"] = clean_students["marks"] >= 35

# Marks ko 0 se 1 ke beech scale karo
minimum_marks = clean_students["marks"].min()
maximum_marks = clean_students["marks"].max()

clean_students["marks_scaled"] = (
    (clean_students["marks"] - minimum_marks)
    / (maximum_marks - minimum_marks)
)

print("\nCleaned data:")
print(clean_students)

# Final data ko nayi CSV file mein save karo
clean_students.to_csv(
    "Week-06/final_cleaned_students.csv",
    index=False
)

print("\nFinal cleaned data saved to Week-06/final_cleaned_students.csv")