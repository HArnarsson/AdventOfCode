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

galaxies = []
for i in range(len(universe)):
    for j in range(len(universe[i])):
        if universe[i][j] == "#":
            galaxies.append((i, j))

def find_row_idx(g):
    g_idx = -1
    for i in range(len(empty_rows)):
        if g[0] < empty_rows[i]:
            g_idx = i
            break
    if g_idx == -1:
        g_idx = len(empty_rows)
    return g_idx

def find_col_idx(g):
    g_idx = -1
    for i in range(len(empty_cols)):
        if g[1] < empty_cols[i]:
            g_idx = i
            break
    if g_idx == -1:
        g_idx = len(empty_cols)
    return g_idx

def find_empty_rows(g1, g2):
    # calculate number of empty rows crossed
    g1_row_idx = find_row_idx(g1)
    g2_row_idx = find_row_idx(g2)
    # calculate number of empty cols crossed
    g1_col_idx = find_col_idx(g1)
    g2_col_idx = find_col_idx(g2)

    return abs(g1_row_idx-g2_row_idx)*999_999 + abs(g1_col_idx-g2_col_idx)*999_999

total_dist = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        # add as if it didnt expand
        total_dist += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        total_dist += find_empty_rows(galaxies[i], galaxies[j])

print(total_dist)