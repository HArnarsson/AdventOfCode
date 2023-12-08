filename = "input.txt"

with open(filename, "r") as file:
    str = file.readline()

counter = 0
for char in str:
    if char == "(":
        counter += 1
    elif char == ")":
        counter -= 1
print(counter)