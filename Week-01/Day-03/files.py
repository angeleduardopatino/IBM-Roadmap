message = "IBM Roadmap - Day 03"

with open("week-01/day-03/notes.txt", "w") as file:
    file.write(message)

print("File saved")

with open("week-01/day-03/notes.txt", "r") as file:
    content = file.read()

with open("week-01/day-03/notes.txt", "a") as file:
    file.write("\nLearning Python files")

with open("week-01/day-03/notes.txt", "r") as file:
    content = file.read()    

print(content)