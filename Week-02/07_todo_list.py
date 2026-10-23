tasks = []

new_task = input("Write a task, or type done: ")

while new_task != "done":
    tasks.append(new_task)
    new_task = input("Write another task, or type done: ")

print("Your tasks:")
for task in tasks:
    print("-", task)