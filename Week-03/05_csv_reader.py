import csv

marks_list = []

with open("Week-03/students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        marks = int(row[1])
        marks_list.append(marks)

        print("Student:", name, "| Marks:", marks)

average = sum(marks_list) / len(marks_list)
print("Average marks:", round(average, 2))
print("Highest marks:", max(marks_list))
print("Lowest marks:", min(marks_list))