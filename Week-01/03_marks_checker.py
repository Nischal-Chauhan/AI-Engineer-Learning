marks = input("Enter marks: ")
marks = int(marks)

if marks >= 75:
    print("Distinction")
elif marks >= 50:
    print("Second Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
