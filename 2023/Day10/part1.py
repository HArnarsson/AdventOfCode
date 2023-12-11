# idea is simple, go to next node in loop until all nodes in loop are visited, starting at S
# Then the max_distance will be len(visited)/2 if len(visited) is even
# or (len(visited)-1)/2 if len(visited) is odd

filename = "input.txt"

arr = []
with open(filename, 'r') as file:
    for line in file:
        tmp = []
        for j in range(len(line.strip())):
            tmp.append(line.strip()[j])
        arr.append(tmp)

directions = {
    "|":[[1,0], [-1,0]],
    "-":[[0,1], [0,-1]],
    "L":[[-1,0], [0,1]],
    'J':[[-1,0], [0,-1]],
    "7":[[1,0], [0,-1]],
    "F":[[1,0], [0,1]],
    ".":[],
    "S":[]
}

flag=False
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'S':
            start = (i, j)
            flag=True
            break
        if flag:
            break

visited = {start}

flag = False
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    new_i, new_j = start[0]+dx, start[1]+dy
    for dx2, dy2 in directions[arr[new_i][new_j]]:
        if new_i + dx2 == start[0] and new_j + dy2 == start[1]:
            visited.add((new_i, new_j))
            first = (new_i, new_j)
            flag=True
            break
    if flag:
        break

curr = first
while True:
    flag=True
    for dx, dy in directions[arr[curr[0]][curr[1]]]:
        if (curr[0] + dx, curr[1] + dy) not in visited:
            visited.add((curr[0]+dx, curr[1]+dy))
            flag=False
            curr = (curr[0]+dx, curr[1]+dy)
            break
    if flag:
        break

print(len(visited)//2)
