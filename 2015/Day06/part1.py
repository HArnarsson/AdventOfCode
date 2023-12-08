class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x: " + str(self.x)  + ", y: " + str(self.y)

class LightGrid:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.grid = [[False for _ in range(n)] for _ in range(m)]

    def toggle(self, cell1: Pos, cell2: Pos):
        for i in range(cell1.y, cell2.y + 1):
            for j in range(cell1.x, cell2.x + 1):
                self.grid[i][j] = not self.grid[i][j]

    def turn_on(self, cell1: Pos, cell2: Pos):
        for i in range(cell1.y, cell2.y + 1):
            for j in range(cell1.x, cell2.x + 1):
                self.grid[i][j] = True

    def turn_off(self, cell1: Pos, cell2: Pos):
        for i in range(cell1.y, cell2.y + 1):
            for j in range(cell1.x, cell2.x + 1):
                self.grid[i][j] = False

    def count_on(self):
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                count += int(self.grid[i][j])
        return count
    
    def __str__(self):
        return str(self.grid)

class Instruction:
    def __init__(self, type: str, pos_1: Pos, pos_2: Pos):
        self.type = type
        self.pos_1 = pos_1
        self.pos_2 = pos_2

filename = "input.txt"
instructions = []
X_SIZE = 1000
Y_SIZE = 1000 
light_grid = LightGrid(X_SIZE, Y_SIZE)

with open(filename, "r") as file:
    for line in file.read().split("\n"):
        temp = line.split(" ")
        if temp[0] != "turn":
            type = temp[0]
            pos_1_x = int(temp[1].split(",")[0])
            pos_1_y = int(temp[1].split(",")[1])
            pos_2_x = int(temp[3].split(",")[0])
            pos_2_y = int(temp[3].split(",")[1])
            pos_1 = Pos(pos_1_x, pos_1_y)
            pos_2 = Pos(pos_2_x, pos_2_y)
        else:
            type = temp[0] + temp[1]
            pos_1_x = int(temp[2].split(",")[0])
            pos_1_y = int(temp[2].split(",")[1])
            pos_2_x = int(temp[4].split(",")[0])
            pos_2_y = int(temp[4].split(",")[1])
            pos_1 = Pos(pos_1_x, pos_1_y)
            pos_2 = Pos(pos_2_x, pos_2_y)
        instruction = Instruction(type, pos_1, pos_2)
        instructions.append(instruction)

for instruction in instructions:
    if instruction.type == "toggle":
        light_grid.toggle(instruction.pos_1, instruction.pos_2)
    elif instruction.type == "turnon":
        light_grid.turn_on(instruction.pos_1, instruction.pos_2)
    elif instruction.type == "turnoff":
        light_grid.turn_off(instruction.pos_1, instruction.pos_2)

print(light_grid.count_on())