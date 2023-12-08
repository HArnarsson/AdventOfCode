filename = "input.txt"

with open(filename, "r") as file:
    path = file.readline()

houses_visited = {}
houses_visited[(0,0)] = 1

x_pos = 0
y_pos = 0
for dir in path:
    if (dir == "^"):
        y_pos -= 1
    elif (dir == ">"):
        x_pos += 1
    elif (dir == "v"):
        y_pos += 1
    elif (dir == "<"):
        x_pos -= 1
    if(not (x_pos, y_pos) in houses_visited):
        houses_visited[(x_pos, y_pos)] = 1
    else:
        houses_visited[(x_pos, y_pos)] += 1

print(len(houses_visited.keys()))