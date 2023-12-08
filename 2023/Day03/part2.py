from math import prod
class Grid:
    def __init__(self, num_rows, num_columns):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.grid = [[' ' for _ in range(num_rows)] for _ in range(num_columns)]
        self.stars = {}

    @staticmethod
    def is_symbol(val):
        return not val.isnumeric() and not val == '.'

    def update_stars(self, i, j, num):
        self.stars.setdefault((i, j), []).append(num)

    def set(self, i, j, val):
        self.grid[i][j] = val

    def get(self, i, j):
        if 0 <= i < self.num_rows and 0 <= j < self.num_columns:
            return self.grid[i][j]
        else:
            return '.'
    
    def get_neighbors(self, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        neighbors = []
        for dx, dy in directions:
            new_i, new_j = i + dx, j + dy

            if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_columns:
                if not self.get(new_i, new_j).isnumeric():
                    neighbors.append((new_i, new_j))

        return neighbors

filename = "input.txt"

with open(filename, 'r') as file:
    num_rows = 0
    for line in file:
        num_columns = len(line)
        num_rows += 1

engine = Grid(num_rows, num_columns)

with open(filename, 'r') as file:
    i = 0
    for line in file:
        for j in range(len(line.strip())):
            engine.set(i, j, line[j])
        i += 1

counter = 0
for i in range(len(engine.grid)):
    j = 0
    while j in range(len(engine.grid[i])):
        if engine.get(i,j).isnumeric():
            num = ''
            k = 0
            neighbors = set()
            while engine.get(i,j+k).isnumeric():
                num += engine.get(i,j+k)
                neighbors.update(engine.get_neighbors(i, j+k))
                k += 1
            for el in neighbors:
                if engine.get(el[0], el[1]) == '*':
                    engine.update_stars(el[0], el[1], int(num))
            j += len(num)-1
        j += 1

summa = 0
for star in engine.stars:
    if len(engine.stars[star]) == 2:
        summa += prod(engine.stars[star])

print(summa)