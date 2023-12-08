filename = "input.txt"

with open(filename, "r") as file:
    path = file.readline()

houses_visited = {}
houses_visited[(0,0)] = 1

x_pos = 0
y_pos = 0
xr_pos = 0
yr_pos = 0
isRobo = False

for dir in path:
    if (dir == "^"):
        if(isRobo):
            yr_pos -= 1
        else:
            y_pos -= 1
    elif (dir == ">"):
        if(isRobo):
            xr_pos += 1
        else:
            x_pos += 1
    elif (dir == "v"):
        if(isRobo):
            yr_pos += 1
        else:
            y_pos += 1
    elif (dir == "<"):
        if(isRobo):
            xr_pos -= 1
        else:
            x_pos -= 1
    if(isRobo):
        if(not (xr_pos, yr_pos) in houses_visited):
            houses_visited[(xr_pos, yr_pos)] = 1
        else:
            houses_visited[(xr_pos, yr_pos)] = 1
    else:
        if(not (x_pos, y_pos) in houses_visited):
            houses_visited[(x_pos, y_pos)] = 1
        else:
            houses_visited[(x_pos, y_pos)] += 1
    isRobo = not isRobo

print(len(houses_visited.keys()))