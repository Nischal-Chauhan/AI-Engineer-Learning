try:
    age = int(input("Apni age likho: "))
    print("Age:", age)
except ValueError:
    print("Please enter your age as a number.")