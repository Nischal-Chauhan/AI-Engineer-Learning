student = {
    "name": "Aarav",
    "marks": [80, 85, 92, 95]
}

print(student["name"])
print(student["marks"])
def calculate_average(marks):
    return sum(marks) / len(marks)

average = calculate_average(student["marks"])
print("Average:", average)
print("Highest mark:", max(student["marks"]))
print("Lowest mark:", min(student["marks"]))
if average >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")