marks = [78, 85, 92]
marks.append(95)
marks[0] = 80
print(marks)
average = sum(marks) / len(marks)
print("Average marks:", average)
print("Total marks:", sum(marks))
print("Number of marks:", len(marks))
print(marks[0])
print(marks[2])
print("Marks one by one:")
for mark in marks:
    print(mark)