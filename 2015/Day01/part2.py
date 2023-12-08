filename = "input.txt"

with open(filename, "r") as file:
    str = file.readline()

counter = 0
it = 1
for char in str:
    if char == "(":
        counter += 1
    elif char == ")":
        counter -= 1
        if (counter < 0):
            print(it)
            break
    it += 1
print(counter)