with open("Week-03/learning_note.txt", "w") as file:
    file.write("I am learning Python file handling.")

print("Note saved.")
with open("Week-03/learning_note.txt", "r") as file:
    content = file.read()

print(content)