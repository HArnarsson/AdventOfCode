import numpy as np

filename = "input.txt"
with open(filename, "r") as file:
    lines = file.readlines()

data = [list(line.strip()) for line in lines]

universe = np.array(data)
empty_rows = []
for i in range(len(universe)):
    if len(set(universe[i])) == 1:
        empty_rows.append(i)

empty_cols = []
universe_t = np.transpose(universe)
for i in range(len(universe_t)):
    if len(set(universe_t[i])) == 1:
        empty_cols.append(i)

# reversed so that current row does not affect future rows
for row_idx in reversed(empty_rows):
    new_row = np.array(['.'] * universe.shape[1]) 
    universe = np.insert(universe, row_idx + 1, new_row, axis=0)

for col_idx in reversed(empty_cols):
    new_col = np.array(['.'] * universe.shape[0])
    universe = np.insert(universe, col_idx + 1, new_col, axis=1)

galaxies = []
for i in range(len(universe)):
    for j in range(len(universe[i])):
        if universe[i][j] == "#":
            galaxies.append((i, j))

total_dist = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        total_dist += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(total_dist)