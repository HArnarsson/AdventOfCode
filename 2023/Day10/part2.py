# idea:
# make all edges of the grid outside, unless they are contained in the loop
# for every single node int the grid that is not visited, run BFS, if it reaches the
# edges, then all of the edges discovered in that bfs are outside
# if they dont reach the edge, then we know all of those are inside

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

# edges = set()

# g = Graph()

# # construct neighbors for non-loop nodes and add edges
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if (i,j) in visited:
#             continue
#         if i == 0 or i == len(arr)-1 or j == 0 or j == len(arr[i]):
#             edges.add((i,j))
#             continue
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             new_i, new_j = i + dx, j + dy

#             if 0 <= new_i < len(arr) and 0 <= new_j < len(arr[i]) and (new_i,new_j) not in visited:
#                 g.add_edge((i,j), (new_i, new_j))

# inside = set()
# outside = set()
# for border_node in edges:
#     outside.add(border_node)

# for node in g.nodes():
#     if node in outside or node in inside:
#         continue
#     flag = True
#     bfs = bfs_tree(g, node)
#     for node in bfs.nodes():
#         if node in edges:
#             # is outside
#             flag = False
#     if flag == True:
#         # is inside
#         for node in bfs.nodes():
#             inside.add(node)
#     else:
#         # is outside
#         for node in bfs.nodes():
#             outside.add(node)

# floodfilling does not work without expanding, so i just gave up

# the following is kinda unintuitive, see pdf

inside = 0
for i in range(len(arr)):
    parity = 0
    for j in range(len(arr[i])):
        # curr is not in loop
        if (i, j) not in visited:
            # if parity is odd, we are inside the pipe
            if parity % 2:
                inside += 1
            continue
        # we are in loop
        if arr[i][j] in ['|', 'F', '7']:
            parity += 1

print(inside)