# 1. read through file, if numeric char is found, then do while loop to locate rest of digits
# 2. use check neighbors func for all digits in the number, if a non-period, non-numeric char is found in neighbors
# => add to sum

class Grid:
    def __init__(self, num_rows, num_columns):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.grid = [[' ' for _ in range(num_rows)] for _ in range(num_columns)]

    @staticmethod
    def is_symbol(val):
        return not val.isnumeric() and not val == '.'

    def set(self, i, j, val):
        self.grid[i][j] = val

    def get(self, i, j):
        if 0 <= i < self.num_rows and 0 <= j < self.num_columns:
            return self.grid[i][j]
        else:
            return '.'
    
    def check_neighbors(self, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for dx, dy in directions:
            new_i, new_j = i + dx, j + dy

            if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_columns:
                neighbor = self.get(new_i, new_j)

                if self.is_symbol(neighbor):
                    return True 
        
        return False

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
            is_valid = False
            while engine.get(i,j+k).isnumeric():
                num += engine.get(i,j+k)
                if engine.check_neighbors(i, j+k):
                    is_valid = True
                k += 1
            if is_valid:
                counter += int(num)
                j += len(num)-1
        j += 1

print(counter)

